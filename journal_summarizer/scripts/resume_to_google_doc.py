#!/usr/bin/env python3
"""
Create a Google Doc from a local Markdown resume.

Example:
    python3 journal_summarizer/scripts/resume_to_google_doc.py \
        --input resumes/gboodhoo-resume-connect.md \
        --title "Gary Boodhoo Resume"

Before first run:
1. Create an OAuth Desktop App in Google Cloud.
2. Enable the Google Docs API for that project.
3. Download the OAuth client JSON file.
4. Pass it with --credentials google-docs-credentials.json

The script stores the refresh/access token locally so later runs can reuse it.
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError:  # pragma: no cover - dependency availability varies by machine
    Request = None
    Credentials = None
    InstalledAppFlow = None
    build = None


SCOPES = ["https://www.googleapis.com/auth/documents"]
DEFAULT_INPUT = Path(__file__).resolve().parents[2] / "resumes" / "gboodhoo-resume-connect.md"
DEFAULT_CREDENTIALS = Path(__file__).resolve().parents[2] / "google-docs-credentials.json"
DEFAULT_TOKEN = Path(__file__).resolve().parents[2] / "google-docs-token.json"
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


@dataclass
class TextStyleSpan:
    start: int
    end: int
    style_fields: dict[str, bool]


@dataclass
class Paragraph:
    text: str
    paragraph_style: str | None = None
    bullet: bool = False
    text_styles: List[TextStyleSpan] = field(default_factory=list)


@dataclass
class PositionedParagraph:
    paragraph: Paragraph
    start_index: int
    end_index: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="Markdown resume to upload.",
    )
    parser.add_argument(
        "--title",
        default="Resume",
        help="Title for the new Google Doc.",
    )
    parser.add_argument(
        "--credentials",
        type=Path,
        default=DEFAULT_CREDENTIALS,
        help="OAuth client JSON downloaded from Google Cloud.",
    )
    parser.add_argument(
        "--token",
        type=Path,
        default=DEFAULT_TOKEN,
        help="Path used to cache the Google OAuth token.",
    )
    return parser.parse_args()


def ensure_google_dependencies() -> None:
    if all((Request, Credentials, InstalledAppFlow, build)):
        return
    raise SystemExit(
        "Missing Google API dependencies. Install them with:\n"
        "pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib"
    )


def load_credentials(credentials_path: Path, token_path: Path) -> Credentials:
    creds = None

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if creds and creds.valid:
        return creds

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        if not credentials_path.exists():
            raise SystemExit(
                f"OAuth client file not found: {credentials_path}\n"
                "Download a Desktop App credential JSON from Google Cloud and pass it with --credentials."
            )
        flow = InstalledAppFlow.from_client_secrets_file(str(credentials_path), SCOPES)
        creds = flow.run_local_server(port=0)

    token_path.write_text(creds.to_json(), encoding="utf-8")
    return creds


def strip_markdown_comments(text: str) -> str:
    return COMMENT_RE.sub("", text)


def parse_inline_styles(text: str) -> tuple[str, List[TextStyleSpan]]:
    plain_parts: List[str] = []
    spans: List[TextStyleSpan] = []
    i = 0

    while i < len(text):
        if text.startswith("**", i):
            end = text.find("**", i + 2)
            if end != -1:
                inner = text[i + 2 : end]
                start = sum(len(part) for part in plain_parts)
                plain_parts.append(inner)
                spans.append(TextStyleSpan(start=start, end=start + len(inner), style_fields={"bold": True}))
                i = end + 2
                continue
        if text.startswith("*", i):
            end = text.find("*", i + 1)
            if end != -1:
                inner = text[i + 1 : end]
                start = sum(len(part) for part in plain_parts)
                plain_parts.append(inner)
                spans.append(TextStyleSpan(start=start, end=start + len(inner), style_fields={"italic": True}))
                i = end + 1
                continue
        if text.startswith("_", i):
            end = text.find("_", i + 1)
            if end != -1:
                inner = text[i + 1 : end]
                start = sum(len(part) for part in plain_parts)
                plain_parts.append(inner)
                spans.append(TextStyleSpan(start=start, end=start + len(inner), style_fields={"italic": True}))
                i = end + 1
                continue

        plain_parts.append(text[i])
        i += 1

    return "".join(plain_parts), spans


def make_paragraph(text: str, paragraph_style: str | None = None, bullet: bool = False) -> Paragraph:
    plain_text, text_styles = parse_inline_styles(text.rstrip())
    return Paragraph(
        text=plain_text,
        paragraph_style=paragraph_style,
        bullet=bullet,
        text_styles=text_styles,
    )


def parse_markdown(markdown_text: str) -> List[Paragraph]:
    paragraphs: List[Paragraph] = []
    cleaned = strip_markdown_comments(markdown_text)

    for raw_line in cleaned.splitlines():
        stripped = raw_line.strip()

        if not stripped:
            paragraphs.append(Paragraph(text=""))
            continue

        if stripped.startswith("# "):
            paragraphs.append(make_paragraph(stripped[2:], paragraph_style="HEADING_1"))
            continue

        if stripped.startswith("## "):
            paragraphs.append(make_paragraph(stripped[3:], paragraph_style="HEADING_2"))
            continue

        if stripped.startswith("### "):
            paragraphs.append(make_paragraph(stripped[4:], paragraph_style="HEADING_3"))
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        if stripped.startswith("- ") or stripped.startswith("* ") or stripped.startswith("• "):
            content = stripped[2:]
            nesting = "\t" * (indent // 2)
            paragraphs.append(make_paragraph(f"{nesting}{content}", bullet=True))
            continue

        paragraphs.append(make_paragraph(stripped))

    while paragraphs and not paragraphs[-1].text:
        paragraphs.pop()

    return paragraphs


def build_document_content(paragraphs: List[Paragraph]) -> tuple[str, List[PositionedParagraph]]:
    buffer: List[str] = []
    positioned: List[PositionedParagraph] = []
    cursor = 1

    for paragraph in paragraphs:
        line = f"{paragraph.text}\n"
        start_index = cursor
        end_index = cursor + len(line)
        buffer.append(line)
        positioned.append(
            PositionedParagraph(
                paragraph=paragraph,
                start_index=start_index,
                end_index=end_index,
            )
        )
        cursor = end_index

    return "".join(buffer), positioned


def build_requests(positioned_paragraphs: List[PositionedParagraph]) -> List[dict]:
    requests: List[dict] = []

    for item in positioned_paragraphs:
        paragraph = item.paragraph
        has_visible_text = bool(paragraph.text.strip())

        if paragraph.paragraph_style and has_visible_text:
            requests.append(
                {
                    "updateParagraphStyle": {
                        "range": {"startIndex": item.start_index, "endIndex": item.end_index},
                        "paragraphStyle": {"namedStyleType": paragraph.paragraph_style},
                        "fields": "namedStyleType",
                    }
                }
            )

        if paragraph.bullet and has_visible_text:
            requests.append(
                {
                    "createParagraphBullets": {
                        "range": {"startIndex": item.start_index, "endIndex": item.end_index},
                        "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE",
                    }
                }
            )

        for span in paragraph.text_styles:
            if span.start == span.end:
                continue
            requests.append(
                {
                    "updateTextStyle": {
                        "range": {
                            "startIndex": item.start_index + span.start,
                            "endIndex": item.start_index + span.end,
                        },
                        "textStyle": span.style_fields,
                        "fields": ",".join(span.style_fields.keys()),
                    }
                }
            )

    return requests


def create_google_doc(title: str, content: str, requests: List[dict], creds: Credentials) -> tuple[str, str]:
    service = build("docs", "v1", credentials=creds)
    document = service.documents().create(body={"title": title}).execute()
    document_id = document["documentId"]

    batch_requests = [{"insertText": {"location": {"index": 1}, "text": content}}, *requests]
    service.documents().batchUpdate(documentId=document_id, body={"requests": batch_requests}).execute()

    return document_id, f"https://docs.google.com/document/d/{document_id}/edit"


def main() -> None:
    args = parse_args()
    ensure_google_dependencies()

    if not args.input.exists():
        raise SystemExit(f"Resume file not found: {args.input}")

    markdown_text = args.input.read_text(encoding="utf-8")
    paragraphs = parse_markdown(markdown_text)
    content, positioned_paragraphs = build_document_content(paragraphs)
    requests = build_requests(positioned_paragraphs)
    creds = load_credentials(args.credentials, args.token)
    _, doc_url = create_google_doc(args.title, content, requests, creds)
    print(doc_url)


if __name__ == "__main__":
    main()
