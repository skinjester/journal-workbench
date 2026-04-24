# Connection map (1st-degree list → mutuals with you)

*Goal: for each “anchor” contact (from your Riot / recruiter **overlap** list, plus any **Riot 1st-degree** names you explicitly add), record who is in the **intersection** of: **your 1st-degree network** and **the anchor’s** network. On LinkedIn this is the **“mutual connections”** search: `origin=SHARED_CONNECTIONS_CANNED_SEARCH` + `connectionOf=[member id]`. This file builds a map: **anchor → { mutuals }**.*

**Interactive graph:** [network-graph.html](network-graph.html) — anchor vs mutual colors, R&D accent. The builder adds **co-list** links (dim) between every pair of names on the *same comma-separated* mutual bullet in this file (same line of your capture, not a claim they know each other; hide them in the graph with the sidebar toggle if it is too busy). Also: **you → anchor**, **anchor → mutual**, optional **extra** pairings in [network-map.peer-edges.md](network-map.peer-edges.md) when you want to mark a relationship the map does not encode, and 2nd→1st bridges. Regenerate with `python3 scripts/build_network_graph.py` after edits.

**2nd-degree Riot UX (outreach list, separate from anchors):** [riot-2nd-degree-ux-2026.md](riot-2nd-degree-ux-2026.md).

## How to re-open the full list in a browser

1. People search, **1st** connections:  
   `https://www.linkedin.com/search/results/people/?keywords=<URL-encoded name>&network=%5B%22F%22%5D`  
2. On the right card, click the **“… other mutual connections”** line (or the first line that lists mutuals). The URL will gain `connectionOf=…`.  
3. Add `&page=2`, `&page=3`, … to walk pages.

**Direct template** (if you have saved the member id from step 2):

`https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22<MEMBER_ID>%22%5D`

---

## Ed Knapp

- **Profile (public URL):** `https://www.linkedin.com/in/edknapp/`
- **connectionOf (member id):** `ACoAAAD242oBMHy6aShHYnbzB8vfoLIdDgu0Uwo`
- **Mutual search (copy/paste):** [Open mutuals with Ed (page 1)](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAD242oBMHy6aShHYnbzB8vfoLIdDgu0Uwo%22%5D)
- **Result size:** 9+ pages in LinkedIn pagination (snapshot 2026-04-23).

### Mutuals — page 1 only (captured 2026-04-23)

*Full graph requires walking pages 2–9 in LinkedIn or re-running the browser capture.*

- Chris Balser (Systems Designer)
- Jeremy Sera
- James Owen Lowe (Archetype; ex ZOS)
- Colin McGinley
- Paul Sage
- Steve Nelson II
- Dan Wellman
- Jason Williford
- Ben Jones
- Marc Hudgins (Project Art Director, ZOS)

---

## Quin Richards

- **connectionOf:** `ACoAABMv2AMB3iF0ebsjL4BuQv6N-w3PMNczBHI`
- **Mutual search:** [Open mutuals with Quin (page 1)](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAABMv2AMB3iF0ebsjL4BuQv6N-w3PMNczBHI%22%5D)
- **Result size:** 1 page (captured 2026-04-23).

### Mutuals (full list on page 1)

- Johnny White
- Derek Van Oss (Riot; UX)
- Bruce Harlick
- Celia Hodent
- Stephan Dube
- *(Card lines also reference larger networks: e.g. Marc Hudgins, Ryan Ward, Vic DeLeon, Alan Cooper — as “N other” on those rows.)*

---

## Jim Rivers

- **connectionOf:** `ACoAAAA-gmYB9wlhSLfDHhTX1L7kWWCLkLJ1mEI`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAA-gmYB9wlhSLfDHhTX1L7kWWCLkLJ1mEI%22%5D)
- **Result size:** 10+ pages on LinkedIn.

### Mutuals — page 1 only (sample)

- Jeff Seamster, Chris Balser, Rachael Masako Ing, Sammi Kim, Kim Herbst, Taylor Wright, **Ed Knapp**, Gabrielle Snowden, Adam Piper, Mila Pavlin

---

## Mags Ng

- **Search hint (1st):** keywords `Mags Ng production` (ex-Riot in headline)
- **connectionOf:** `ACoAAAAGmQIB9y0vxe2pmRUX4VSwd6flb6Bga24`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAAGmQIB9y0vxe2pmRUX4VSwd6flb6Bga24%22%5D)
- **Result size:** 5 pages (2026-04-23).

### Mutuals — page 1 (sample)

- Rodrigo Aguilar, Sammi Kim, Glenn Entis, **Ed Knapp**, Brian Schneider, Ray Mazza, Lisa Martin, Peter Grassi, Alex Chatfield, Justin McLeod

---

## Ryan Ward

- **Search hint (1st):** keywords `Ryan Ward Jagex` (headline: Building Forever Games / ex Jagex)
- **connectionOf:** `ACoAAAAANfYB06XykGHOYY1IUSAwq9BPGV9vfcY`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAAANfYB06XykGHOYY1IUSAwq9BPGV9vfcY%22%5D)
- **Result size:** 10+ pages (2026-04-23).

### Mutuals — page 1 (sample)

- **Ed Knapp**, Adam Piper, Brian Schneider, Kento Kojima, Nat Dart, Timothy Nice, Brian Nestor, Lisa Martin, Dan Wellman, Peter Grassi

---

## Nathaniel Nordfelt

- **Search hint (1st):** `Nathaniel Nordfelt Riot` (Dir. Software Engineering, Riot)
- **connectionOf:** `ACoAAAAjT3wBLO8iFLdQTD4dCNKblWw71klz1WI`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAAjT3wBLO8iFLdQTD4dCNKblWw71klz1WI%22%5D)
- **Result size:** 3 pages (2026-04-23).

### Mutuals — page 1 (sample)

- Murtaza Nemat Ali, **Alex Chatfield** (Tripwire), Matt Thazhmon, Derek Brinkmann, Miguel Molinari, Dale Russell, Paul Teall, Scott Nagy, Peter Santoki, Oge Young (many rows show **Steven Chiang** as a through-line)

---

## Allen Warner

- **Search hint (1st):** `Allen Warner Narrative Baltimore`
- **connectionOf:** `ACoAAAEjWgYByq6SLqMQxwUwUTKxEQWvbIb9eFs`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAEjWgYByq6SLqMQxwUwUTKxEQWvbIb9eFs%22%5D)
- **Result size:** 10+ pages (2026-04-23).

### Mutuals — page 1 (sample)

- Jeff Seamster, David Swanson (UX, EA NHL), Kim Herbst, **Ed Knapp**, Gabrielle Snowden, Mila Pavlin, Brian Schneider, **Jeremy Sera**, **James Owen Lowe**, John Chaffee (Guerrilla)

---

## Jason Smith (Game Caviar)

- **Search hint (1st):** `Jason Smith Game Caviar`
- **connectionOf:** `ACoAAAApcvYBvI35wuUSBWBzEJ0HJf28B9MVxSs`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAApcvYBvI35wuUSBWBzEJ0HJf28B9MVxSs%22%5D)
- **Result size:** 10+ pages (2026-04-23).

### Mutuals — page 1 (sample)

- Jeff Seamster, Sammi Kim, Glenn Entis, Christopher Jimison, Ron Kee, Adam Piper, Ray Mazza, Mark Lee, Kento Kojima, Dmitry Andreev

---

## Victor Keenan

- **Search hint (1st):** `Victor Keenan Riot Mill Valley` (Staff SWE, Riot)
- **connectionOf:** `ACoAAAFJv3MBNRbkNw4vmxctxFtCD4J_vtPlGPM`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAFJv3MBNRbkNw4vmxctxFtCD4J_vtPlGPM%22%5D)
- **Result size:** 5 pages (2026-04-23).

### Mutuals — page 1 (sample)

- Ron Kee, Mark Lee, Stella Balmoria, Jasmine Sarmiento, Mike Bates, Peter Grassi, Chris Ocampo (Reality Labs), Dave Cross, John Yoo, **Adam Murguia**

---

## Nicholas Konkle (Riot)

- **Profile (public URL):** `https://www.linkedin.com/in/nick-konkle/`
- **Search hint (1st):** `Nicholas Konkle Riot` (Game Director, Riot; Culver City)
- **connectionOf:** `ACoAAAD2cycBJLUt8gJ7AEWHsZLjkAAc-4Fr85M`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAD2cycBJLUt8gJ7AEWHsZLjkAAc-4Fr85M%22%5D)
- **Result size:** 7+ pages (2026-04-23).

### Mutuals — page 1 (sample)

- Ed Knapp, Jeremy Sera, James Owen Lowe, Marc Hudgins, **Seth Hall** (and others; walk `&page=2`+)

---

## Greg Faillace (Riot)

- **Search hint (1st):** `Greg Faillace Riot` (Sr. Art Director, MMO R&D at Riot)
- **R&D (profile):** **MMO R&D** appears in the Sr. Art Director / team line (search card). *See also [riot-games.md](riot-games.md) (section **R&D profile flags (LinkedIn)**).*
- **connectionOf:** `ACoAAAARBzABxC5UjAV9mpmzqzYG1tCuMlKt8oc`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAARBzABxC5UjAV9mpmzqzYG1tCuMlKt8oc%22%5D)
- **Result size:** 6 pages (2026-04-23).

### Mutuals — page 1 (sample)

- Rodrigo Aguilar, Jeff Seamster, Brian Schneider, Ray Mazza, Lisa Martin, Chris Ocampo, **Seth Hall**

---

## Seth Hall (Riot)

- **Search hint (1st):** `Seth Hall Riot VFX` (Principal Tools & Pipeline Technical Artist, Riot; LA)
- **connectionOf:** `ACoAAABAg64BIVXcfD9VjtOdngD9upy5VvQzMqk`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAABAg64BIVXcfD9VjtOdngD9upy5VvQzMqk%22%5D)
- **Result size:** 10+ pages (2026-04-23).

### Mutuals — page 1 (sample)

- Taylor Wright, Casto Edward Vocal Jr, Adam Piper, Dale Cieslak, Kento Kojima, Dmitry Andreev, Nat Dart, Timothy Nice, Brian Nestor, Cedrick Collomb

---

## Teck Lee Tan (Riot)

- **Search hint (1st):** `Teck Lee Tan Riot Singapore` (Manager, Technical Art, Riot)
- **connectionOf:** `ACoAAABb7oQBOqPF-cqVXT-KmsegpQgcbkCVTT0`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAABb7oQBOqPF-cqVXT-KmsegpQgcbkCVTT0%22%5D)
- **Result size:** 3 pages (2026-04-23).

### Mutuals — page 1 (sample)

- Altair Martinez, Shawna Tanskanen, Shawn Pitman, Charles Durairaj, Hafiz Zainal Abidin, Jano Vesina, Edmund Shen, David Kirscheneder, Aaron LeMay, Claudiu Dumitru

---

## Geoffrey Marsi (Riot)

- **Search hint (1st):** `Geoffrey Marsi Riot Technical Game Design` (Senior Manager, Technical Game Design, Riot; LA)
- **R&D (profile):** experience line **Unannounced R&D Project** (May 2023–present) under the current Riot role. *See also [riot-games.md](riot-games.md) (section **R&D profile flags (LinkedIn)**).*
- **connectionOf:** `ACoAAAe0JY4B7kvLm-VHeZO897OGwwQTYcxM0bg`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAe0JY4B7kvLm-VHeZO897OGwwQTYcxM0bg%22%5D)
- **Result size:** 4 pages (2026-04-23).

### Mutuals — page 1 (sample)

- Chris Balser, Ed Knapp, Jeremy Sera, James Owen Lowe, Colin McGinley, Paul Sage, Lea Jacqueline Evans, Dan Kline, Christofer Strasz, Chris Dillman

---


## Gina Jaio

- **Profile (public URL):** `https://www.linkedin.com/in/ginajaio/`
- **Search hint (1st):** `Gina Jaio Riot` (✨Talent Acquisition Leader | Riot Games; Irvine, CA)
- **connectionOf:** `ACoAAABL5f0Bpn5HxNLxAGuJvPEwVyW2N3rupwM`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAABL5f0Bpn5HxNLxAGuJvPEwVyW2N3rupwM%22%5D)
- **Result size:** ~121 mutual connections with you (profile line 2026-04-23); ~10 people per page in search.

### Mutuals — pages 1–2 (captured 2026-04-23)

**Page 1**

- Rodrigo Aguilar
- Ed Knapp
- Fran Court
- David Reed Monroe
- Jasmine Sarmiento
- Steve Nelson II
- Terri Lou Tiongson
- Lisa Martin
- Jason Williford
- Stephen Busfield

**Page 2**

- Vivek Sangubhotla
- Marc Hudgins
- Adam Arrigo
- John Stafford
- Noah Watkins
- Nikita Puranik
- Dave Cross
- Elijah Freeman
- John Yoo
- Kursad Can

---


## Seren Mason (vesabios)

- **Profile (public URL):** `https://www.linkedin.com/in/vesabios/`
- **Search hint (1st):** `Seren Mason Riot` (Game Design Architect, Riot Games; San Francisco, CA)
- **connectionOf:** `ACoAAAEzVA8B3BK5nNzfCE0IYIgmicuylxkkp8w`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAEzVA8B3BK5nNzfCE0IYIgmicuylxkkp8w%22%5D)
- **Result size:** 14 mutual connections with you (profile: “Victor, Nicholas and 12 other…”, 2026-04-24); 10 + 4 in search = full list on 2 pages.

### Mutuals — pages 1–2 (captured 2026-04-24)

**Page 1**

- Sammi Kim
- Taylor Wright
- Ammon Haggerty
- Adam Arrigo
- John Yoo
- Adam Murguia
- Greg Faillace
- Christine Brownell
- Ole Goethe
- Joel Anderson

**Page 2**

- Josh Santangelo
- Nicholas Konkle
- Victor Keenan
- Alex Churchill

---


## Derek Van Oss (workwithdvo)

- **Profile (public URL):** `https://www.linkedin.com/in/workwithdvo/`
- **Search hint (1st):** `Derek Van Oss Riot UX` (Principal UX Designer + Prototyper, Riot Games; Los Angeles, CA)
- **connectionOf:** `ACoAAAAHaN4BtuS66tu0GuFcGzjcsLpTf15e3xg`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAAHaN4BtuS66tu0GuFcGzjcsLpTf15e3xg%22%5D)
- **Result size:** 11 mutual connections with you (profile: “Stephan, Charlene and 9 other…”, 2026-04-24); 10 + 1 on two search pages.

### Mutuals — pages 1–2 (captured 2026-04-24)

**Page 1**

- Quin Richards
- Kristen Diane McDonald-Brown
- Cole Nelson
- Stephan Dube
- Charlene Zvolanek
- Amy Li
- David Sheldon-Hicks
- Andrew Snell
- Jeff Pearce
- Valeria Magalí Sanchez

**Page 2**

- Andrea Marchiotto

---

## Dan Kline (dankline)

- **Profile (public URL):** `https://www.linkedin.com/in/dankline/`
- **Search hint (1st):** `Dan Kline Riot` (Senior Game Design Manager, Riot Games; South San Francisco, CA)
- **connectionOf:** `ACoAAABxyAkBGX2YYP-b-0sohvDYIaBEckIRt4g`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAABxyAkBGX2YYP-b-0sohvDYIaBEckIRt4g%22%5D)
- **Result size:** ~74 mutual connections with you (profile: “Isa Anne, Timothy and 72 other…”, 2026-04-23); 8 pages in LinkedIn pagination.

### Mutuals — pages 1–2 (captured 2026-04-23)

**Page 1**

- Adam Piper
- Dale Cieslak
- Ray Mazza
- Kento Kojima
- Scot Brew
- Chris Huybregts
- Timothy Nice
- Aaron Yonas
- Michael Arnold
- Reid Kimball

**Page 2**

- Stephen Busfield
- Chris Marvin
- Alex Rozgo
- John Stafford
- Seth Hall
- Paul Rand Pierce
- Greg Knight
- Jonathan Tilden
- Joseph Kubiak
- Isa Anne Stamos

---

## Steven Chiang (steven-chiang-98689)

- **Profile (public URL):** `https://www.linkedin.com/in/steven-chiang-98689/`
- **Search hint (1st):** `Steven Chiang Fortis` (President, Fortis Games; San Francisco, CA)
- **connectionOf:** `ACoAAAACyjYBw1PlT7dZ7yFpGNlwxMvq0-lRrTQ`
- **Mutual search (page 1):** [Open](https://www.linkedin.com/search/results/people/?origin=SHARED_CONNECTIONS_CANNED_SEARCH&network=%5B%22F%22%5D&connectionOf=%5B%22ACoAAAACyjYBw1PlT7dZ7yFpGNlwxMvq0-lRrTQ%22%5D)
- **Result size:** ~95 mutual connections with you (profile: “Paul, Albert and 93 other…”, 2026-04-23); 10 pages in LinkedIn pagination.

### Mutuals — pages 1–2 (captured 2026-04-23)

**Page 1**

- Sammi Kim
- Tommy Cinquegrano
- Glenn Entis
- Judy Wolf
- Mark Mongie
- Brian Schneider
- Sam Hofer
- Kento Kojima
- Jeff Poole
- Peter Grassi

**Page 2**

- Matt McEnerney
- Sheetal Bandi, PMP
- Albert Holaso
- Alex Chatfield
- Justin McLeod
- Elijah Freeman
- Matt Thazhmon
- Paul Robinson
- Simon Kandah
- Derek Brinkmann

---

## Hubs (repeat names across many anchors’ page-1 samples)

*Not exhaustive; updates as more pages are captured.*

- **Ed Knapp** — Mags, **Ryan Ward**, Allen
- **Ryan Ward** / **Tim Train** — most large lists; Ryan anchor list is the hub-by-definition view
- **Fiona Cherbak, Steven Chiang** — Jason Smith, Mags, Nathaniel, Victor rows
- **Robert Huebner, Jon Knoles** — cluster on Victor (Riot-adjacent art/leadership)
- **Marc Hudgins, Jeremy Sera, James Owen Lowe** — ZOS / East Coast design cluster (Ed, Allen)
- **Vik Sohal, Lisa Martin, Peter Grassi** — SF / network-heavy producers and founders
- **Seth Hall** — shows up on **Nicholas Konkle** and **Greg Faillace** page-1 mutual samples (large overlap with your overall network)
- **Gina Jaio** (Riot TA) — pages 1–2 sample: **Ed Knapp**, **Marc Hudgins**, **Lisa Martin**, **John Yoo**, **Steve Nelson II**, **Jason Williford**; strong overlap with SF / Lightspeed + ZOS art cluster
- **Seren Mason** (Riot; `/in/vesabios/`) — full 14-mutual list: **Greg Faillace**, **Nicholas Konkle**, **Victor Keenan**, **John Yoo**, **Sammi Kim**; design + Riot anchor cluster
- **Derek Van Oss** (Riot UX; `/in/workwithdvo/`) — 11-mutual list: **Quin Richards**, **Charlene Zvolanek**, **Jeff Pearce**, **Stephan Dube**; direct overlap with your Quin anchor + SF design leaders
- **Dan Kline** (Riot design leadership; `/in/dankline/`) — pages 1–2 sample: **Kento Kojima**, **Seth Hall**, **Timothy Nice**, **Adam Piper**, **Reid Kimball**; bridges production / animation and SF game-design peers
- **Steven Chiang** (Fortis; `/in/steven-chiang-98689/`) — large mutual set; pages 1–2 sample: **Kento Kojima**, **Peter Grassi**, **Brian Schneider**, **Alex Chatfield**; overlaps **Mags Ng**-style cross-studio producer lists (also referenced as through-line on Nathaniel page 1)

---

## Remaining anchors (same workflow)

*Current queue: [network-map-anchors.json](network-map-anchors.json) `pending_anchors`.*

- Patrick Bostwick, Gregory Molnár, Karen LeBlanc, Greg Wessman, Alexei Ryan, **David Kaye**, Johnny Waterman, Lucas Martín Alvarez, Sepideh Asgharian Shahri, Fernando Forero Pinilla, Paxton Galvanek, Darren Bell Jr.

*Say **continue** to run the next batch in the browser.*
