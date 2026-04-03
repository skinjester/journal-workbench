
2021-07-06 16:56

Greg has itemized a number of design tasks that I'm now looking through

Here’s my first stab at what we need for IvedaPinPoint.
- Could you look at it as well as the screen shots I sent you and let me know if I missed anything.
- Also see if you can give me an estimate of how long it will take to complete this.
- We’ll need 2 skins, one for Iveda and one for Clara.
- It might be nice to have some movement or animation in your designs when appropriate (title screen, transitions between modes).


Did Greg miss anything? I guess he's talking about the enumerated list of screenshots as reference? Let me see if I can go through them and correlate them with the line items he provided.

Title / login
    If has signup needs (pre)approval from admin
    Prompts notification permissions
    Prompts location permissions

Notification Design
    Push Notification Look
    Settable frequency (per role)
    Settable alert levels (per role)

Notification feed
    Filter by Alert Level
    Filter by device type
    Filter by location
    Filter by idle time (last moved, might indicate if in use)
    Ability to mark certain alerts as resolved
    Mostly for out of bounds alerts
    We can do this automatically via location

Search for devices
    Ability to filter by device type (string?, list?)
    Sort by distance
    Sort by idle time (last moved, might indicate if in use)
    Click through to map

Map
    Shows location of device / devices
    Filter by device
    Shows idle time (last moved, might indicate if in use)

Reports
    Reports base on level / role
        Overall reports at users level
        Ability to dig down to each region / branch based on user level 
    Types of reports
        Show device location patterns
            Idle times tied to location
        Show query types and frequency
        Show Alert resolution times

Admin
    Ability to create roles
        Set what features user has access to
        Set which alerts / notifications  are visible
    Ability to set Alert Levels per role
    Ability to add / approve users
    Ability to upload maps and set base locations

[MENU]


2021-07-06 18:41
I've transferred this information to a mindmap so I can see it all at once. I'll post this map to:
- Slack
- Confluence Blog (?)



Tomorrow, I'll use this map to generate JIRA Stories and Sub-Tasks
- Is that the best use of my time?
    + its visible
    + its tangible
    + its countable


2021-07-06 18:46
Greg's 2nd post

Skins
- Iveda Cerebro (company livery)
- Claro (client livery)

Localization (selectable)
    - English EN-US
    - Spanish ES-MX
    - Future spoken language support


2021-07-06 19:33
greg's recent addition

Notification switch
Turn on / off notifications automatically based on schedule
Turn on notifications automatically when arriving at work
Turn on / off notifications manually


2021-07-07 09:14
I took a look at the Clustered mind map I'm building and examined it in a more presentable(?) format. Vertically scrollable. The generated outline view is also qquite nice.
What am I going to do with these maps and outlines? They're just my analysis. There's a month or more of work here depending on cadence and responsiveness.

Are there milestones?
Are there reviews?


I don't need to be thinking so far ahead. For me, this information is a Statement of Work. This morning, I can help Greg by capturing this inforrmation in Jira and making estimates. I don't need to finish the mind map to start that.


2021-07-07 10:18
I've completed the clustered mind map


2021-07-07 11:05
Completed & cleaned up maps
Generated markdown from the outline
Generated PDF
Posted to Confluence
Posted to Slack

NEXT
Make this material actionable by adding it to Jira as Tasks/Sub-Tasks


2021-07-07 11:20
OK, I've started working in Jira. Lets see how much intel I can add


2021-07-07 12:11
initial feedback from Greg on Slack is quite positive


2021-07-07 15:37
I've been adding stories and tasks to Jira pretty effectively. Practically I think. They're phrased in terms of outcomes or deliverables. On their own I can make plausible estimations. It looks like more than 1 month of work at a glance. That is perhaps dependent on how much UX they want, and how resourceful they want to be.

I've spent a number of hours on this today and am feeling weird about it now. I'll wrap up for today 


2021-07-07 15:47

NEXT
- create subtasks for MENU story
- estimate sub tasks
- Collate estimates per story
    - is it possible to generate a report in Jira from those estimates?
        + don't spend much time finding out
- communicate my findings to Greg


2021-07-08 10:09
adding subtasks to menu story


2021-07-08 11:17
I've added and described subtasks to the MENU story
I'm realizing that the ADMINISTRATION and REPORTING features are their own stories, so let me rearrange that


2021-07-08 11:44
That looks better. I also updated the clustered mind map I used as reference


2021-07-08 12:35
Spent time looking thru Jira sto see how to report estimates by story. Came across a reasonable solution as a saved Filter


2021-07-08 13:55
back from lunch break, continuing task estimation. I'd like to wrap this up the next 30m


2021-07-08 15:24
I've completed the estimates
I created a Filter called Design Story esitimates that collates the stories and lists the sum of the subtask estimates

https://iveda.atlassian.net/issues/?filter=10007

I created an Excel sheet with the estimates

NEXT
x Post update on Slack that I've organized, described and estimated UI requirements on the Jira Board

x DM Greg with spreadsheet. Mention the Design Story estimates filter I added to Jira Workspace


2021-07-09 18:31
ongoing chat with Greg who tells me a contract will be ready next week
The CEO "liked" a confluence post
They're interested in setting up a videoconference to look over the PinPoint product


2021-07-14 19:20
Spoke w Greg earlier who asked if I'd be willing to start working before the contract was delivered. I'm not. However I requested a walkthrough of the PinPoint software, and read through the confluence documentation he posted. Which looked like a reformatted version of the intially defined requirements. 

I also started pulling together moodboards for creative and Iveda identity. There's a lot of information on their website, and I'd like to spend 2h tomorrow gathering as much informatiion as I can. I felt that the 30 minutes I just spent on this yielded much more intel than I'd expected.

To follow up on that idea though, I'll make the milanote board shareable or public and will link to it from Confluence & Slack. 


2021-07-15 12:30
looking through the Iveda site and capturing to Milanote. I tested sharing those boards on Slack, and looks good. I don't want to spend more than an hour on this.


2021-07-15 15:32
I collated research on Pinpoint, Iveda identity and a moodboard. Shared this material on Slack for visibility


2021-07-19 14:36
Luz reached out to me with some information she needs for my contract


2021-07-20 11:09
Sent start date to Luz for inclusion in my contract
Setup meeting with Greg to discuss first steps and manage expectations


2021-07-20 14:02
shared some material from Wrld3D w Greg. My thinking is that I may use it to create graphics, but also wanted to call out how it switches from streep to indoor nav, and the navigation system for indoors


2021-07-22 10:03
Meeting w Greg now

- our check-in frequency

2021-07-22 11:28
good meeting with Greg will transcribe myu notes here


2021-07-23 11:09
Greg shared a PDF of a building plan, which I've added to my resoureces, etc. Not sure what the larger context of this building is. Where would I find it on a map?


2021-07-23 12:29
I did some research about that map, wondering how far I could go before I needed to read any docs. I captured that journey in a new Mapping moodboard and shared with Greg on slack



2021-07-26 09:57
checked in with Greg

MAP
- send sample SVG file to Greg with named polygons.
    - He wants to see if he can use that data as a region editor for WRLD3D
- step thru the WRLD3D tutorial on building indoor maps
    + is this something I can demonstrate for Greg?


JIRA
- can my Jira user credentials be changed to gboodhoo@skinjester.com? 
    + Your email change request could not be processed because gboodhoo@skinjester.com is already associated with another Atlassian account.

Simple answer - no. Apparently not without some significant effort on my part. Made the attempt.

- review the JIRA tasks that I identified
    + add an issue for introduction to vue.js
    + add an issue for WRLD3D evaluation

MEET & GREET
- I setup a meeting with Marko at 11a


notes fom meeting
trying to setup a demo for Sid
He's going to send me a link to a version of the webapp


pro
tracker updates are very reliable

SUMMARY
Marko is more on the production side of things, not so much the product sude. He was helpful and seemed nice. He gave me a link to the app, which is exactly what I needed to study

It was obvious before, but is increasingly more obvious that lack of customer definition/user roles is a problem. I'm not sure how much there is to see, anmd for who? I know that is very general purpose and that is certainly a strength, but i need criteria to evaluate my work by. I think it will take further conferencing with Syd? David? Greg? to define those intentions further

What can I do to start that conversation?
- provide a list of users and have them sort by importance?


2021-07-26 13:16
pinpoint prototype
https://app.ivedapinpoint.com/

username: mrodic@iveda.com
password: password


2021-07-26 14:29
doing some Jira housekeeping. All the tasks are listed in backlog status. Check w Greg about updating them to selected for development.


2021-07-26 16:10
almost forgot to send over the SVG testfile Greg requested


2021-07-27 10:43
brief back and forth with Greg this morning, he's with his wife before surgery at th moment, so I'll keep working silently with the intent of a broader data dump later in the week.


2021-07-27 10:44
What do you want to accomplish today?
- audit the Pinpoint demo app
    + share my notes as confluence documentation
- examine the commercial theme market for vuejs
    + find some candidates that are broad enough to refactor the pinpoint demo app layout in XD


2021-07-27 12:53
created board for capturing my UX audit


2021-07-27 15:15
spinning my wheels fixating on browser size for screen capture for the audit. I'm telling myself its because I want to be accurate. Really?


2021-07-27 15:15
Marko reached out to introduce me to teh Tracmo app, which is an IoT mobile app. He's set up an account w the same info visible in Pinpoint. Its all working. My button mashing the "ring" button was heard by him.
Uses same login as the pinpoint demo. Installed it on my phone


2021-07-29 10:07
1:1 meeting w Greg
Samson (Tracmo) was mentioned again

inFluxDB - a timebased database

History

NEW CUSTOMER
IVEDA (superuiser)
HOSPITAL (Claro)
REGIONAL MANAGER (NE/SW/HOSPITALS)
HOSPITAL ADMIN 
NURSE
GUARD


2021-07-29 10:28
how about setup mode?
Preconfigure what we can

Preload configuration is a thing. Think about how much time it takes you to setup a smart home config in your living room


What is the Out of Box experience for new customers

Think about how bulk config works
It implies bulk deletion


2021-07-30 15:13
I'm continuing my research into the IoT space and capturing what seem like typical UX pillars. I'm close to wrapping up screen capture for the webapp. It's not worth capturing the visual presence on mobile.

However, it may be useful to capture some screens from the Tracmo mobile app, if only to see where structure and fuction overlap


2021-08-02 09:54
what more do I need to capture from this app before I post it to Confluence/Slack

NAVIGATION
- App Menu/Submenu
- List Submenu
- Remove Tracker(s)
- Remove TempPad Logger(s)
- Remove Device(s)
- Remove Access Link(s)
- Revoke B2B Accounts

EXTERNAL CHANNEL
- Email: Password Change
- Email: PIN code

FEATURES
- Feed
- Notifications
- Account Management
- Advanced Search
- Tracker Map

COMPONENT
- Text Entry Field
- List Header Sort
- Tooltip
- Button (Refresh) 
- Switch (Notify On/Off)
- Button (Share)
- Button (Find this item on the map)
- Button (Call to Action)
- Button (Export CSV)
- Button (Choose Indoor Map)
- Dropdown (TempPad Unit)
- Dropdown (Temp Pad High Temp Alert)
- Dropdown (Low Temp Alert)
- Dropdown (Alert Type)
- Dropdown (TempPad Analytics Time Range)
- Map Pin

DIALOGS
- Change Photo
- Tracker Analytics
- Account Management
- TempPad Analytics
- Create TempPad Logger
- Create Access Link
- Create B2B Account


2021-08-02 12:21
There's a bit more to capture and organize than I realized. I'll export as PDF for sharing purposes later.



2021-08-03 11:20
productively distracted by Google Maps. I captured detailed survey of interface methods and layouts used in that product. Probably enough for its own board


2021-08-03 11:47
continuing my work on the audit. What's the ETA? Any reason this can't wrap up in 2h?

*PM: post audit of the Pinpoint web to Confluence/update team on Slack
*PM: attach relevant gfx from audit to corresponding Jira issues


2021-08-03 11:59
Greg called out the scrum posts to Slack I just started doing as a good working practice for the team :)


2021-08-03 16:28

MENUS
x App Menu/Submenu
- List Submenu

REMOVE ITEM FROM LIST
- Unassign Tracker(s)
x Remove TempPad Logger(s)
- Remove Device(s)
x Remove Access Link(s)
x Revoke B2B Accounts
x Delete Map

EXTERNAL CHANNEL
- Email: Password Change
- Email: PIN code

FEATURES
- Feed
- Notifications
- Account Management
- Advanced Search
- Tracker Map

COMPONENT
- Text Entry Field
- List Header Sort
- Tooltip
- Button (Refresh) 
- Switch (Notify On/Off)
- Button (Share)
- Button (Find this item on the map)
- Button (Call to Action)
- Button (Export CSV)
- Button (Choose Indoor Map)
- Dropdown (TempPad Unit)
- Dropdown (Temp Pad High Temp Alert)
- Dropdown (Low Temp Alert)
- Dropdown (Alert Type)
- Dropdown (TempPad Analytics Time Range)
- Map Pin

DIALOGS
- Change Photo
- Tracker Analytics
- Account Management
- TempPad Analytics
- Create TempPad Logger
- Create Access Link
- Create B2B Account


2021-08-03 18:44
I'm regrouping the content I captured into columns for easier handling


2021-08-04 00:12
completed UX audit

NEXT
export board
post to confluence
share on Slack

THEN
take a look at the Jira tasks you created and update w relevant assets


2021-08-04 10:44
exporting the UX Audit board 


2021-08-04 11:26
setting up Design Project Page and Pinpoint UX Audit pages in Confluence. I can use this documentation as a kind of calling card when I reach out to the other stakeholders. I don't have to flesh out all the refinements and details just yet. Just set up the page and icnlude the basic information


2021-08-04 16:47

Iveda has partnered with interaction designer Gary Boodhoo to design the Cerebro User Experience for its Smart IoT platform, starting with Iveda Pinpoint. Phase 1 will concentrate on design decisions and focus on the Iveda Pinpoint web app.

Goal:
Create a modular and responsive UX/UI framework for this web application. Make it more fun.


2021-08-04 20:18
I've constructed a confluence structure for Iveda. Its all stubbed in right now, but I want to apply visuals to each page, and also link the pages to related jira issues


2021-08-04 22:46
Despite some initial procrastination, the confluence & milanote documentation I've been working on looks like realness now. 


2021-08-04 22:50
NEXT
- continue associating Jira tasks w confluence pages
- read through Greg's requirement listings and make sure that those line items are addressed in relevant documentation
    + I need to know which parts of this relate specifically to what Greg requested


2021-08-05 11:02
1 on 1 with Greg went well. 
I spoke about the UX audit and the ConfluenceWeb that came out of that task

I spoke broadly about the 2 main UX challenges I documented:
- switching contexts between indoor/outdoor
- asset analytics

We spoke a while about the value of aggregating information, being able to tag what you needed. 

He's following up with the team at WRLD3D later today


2021-08-07 16:48
I've started adding "pain points and opportunities" commentary on the confluence pages I created. Once completed, all of this can be collated, prioritized, grouped, etc.


2021-08-10 11:56
I'm looking through vue,js templates for Dashboards, Blogs and Admin Interfaces.


2021-08-10 17:00
After calming down I'm taking the time to explore the world of vue.js. Pretty amazing really. Sort of like jQuery, but better. Even better it looks like it may be simple to evaluate design work in the browser. Theres a service called CodeSandbox that takes care of the server and dev environment stuff. Lots of features to share & embed work elsewhere.

2 parts to the design pipeline:
Adobe XD (sketching, layout with a UX kit, clickthru)
Vue.js (sketching, demonstrating, including)


2021-08-12 14:06
Greg is completely sold on using WRLD3D technology for our mapping. This removes some of the constraints I've been diligent about - or at least defers them a bit more realistically. I checked the WRLD3D map stuff and its really just a layer of JQUERY on top of the map tech.

Greg wants to get a basic design spec together to send out to them for estimation and pricing. That doesn't really change the scope of UI work I need to do, but does add some urgency. I'm gooing to do low fidelity wireframes using WRLD3D bkg assets. All, the same material needs to be covered. This will effectively be an overall view (low fidelity) of the application.

What needs doing?
Need to present 2 postures: Mobile (portrait) and Desktop (1080)

Follow up w Greg tomorrow. to show where I've progressed


2021-08-13 09:53
The Tracmo app on iPad has some good ideas about how to handle lists

NEXT
setup XD project file
    - create mobile (portrait) artboard w grid
    - create desktop 1920x1080 artboard w grid

THEN
sketching

THEN
metrics:


FEED
    - vertical sidepanel?
    - horizontal sidepanel (like tracmo)
    - switch between gallery and list views?



    - 

gather screen captures from the Tracmo iPad app as reference


2021-08-13 17:24
gathered research all day, including tracking Thea when she went to lunch. Many screen captures demonstrating validated patterns for feeds, menus, contexts and map views at a different range of views. I want to use that material for scale

now the sketching


2021-08-16 12:20
its all in my mind I guess. Everytime I start designing this though I tense up. Its only as comp,icated as it is. Maybe some overthinking. I just need to demonstrate a skeletion of this to Greg later

specifically:

P3 hand held view (mobile) vs Desktop views.
    - how do the elements translate?
P1 application skeleton in mobile view
P1 safe areas
    - full screen
    - navigation top


2021-08-17 18:41
The information architecture ideation I spent a good amount of time on was worth it. I stood up a basic application skeleton for Greg, and he's onboard. IO spent today doing what felt like nothing much. I want to rebuild the XD file I made in a well-formed manner so I can make global changes. Was that really ever a reaasonable goal though? I feel like it should be? I feel like it has the potential to eliminate a lot of copy/paste. I feel like its the best way to accomplish theming, etc. But not if its tedious.

Earlier Greg had some questions for Calvin about the authentication API's that Iveda is using in conjunction w Tracmo (not sure what that relationship is). In any case the Pinpoint app communicates w the Tracmo app. I took a deeper dive into login and some related user-centered functions - change PIN, change email. I'd previously identified some missing UI in the Login story. Captured and organized the audit and shared to Slack. Greg appreciated the detail. I told him I'd stub in User management in the App Menu, and could probably stub in a management screen using another list-type screen as a template, if only to get that more solid


2021-08-18 00:29
To get my mind off of this, I purchased 2 UI Kits for general purpose wireframing. I need to step away from the idea of implementation right now. Spending more time pre-optimizing than getting my hands dirty. I need to look thru the material I downloaded - the Constructor set then rebuild the design using those elements


2021-08-18 12:06
I'm reviewing the Constructor UI Kit. Really wish I'd thought to use something like this for previous work. Greag sent out an updated list of requirements around login

Admin Roles

Depending on role level the UX will show a hierarchical graphical map or thumbnail of domain, branch …, location which can be clicked on by the user
Admins should be able to get various reports graphically and be able to dig down by clicking on the various charts (perhaps they can change from bar to pie if appropriate)
Need to track alert counts / rates, resolve counts / rates, battery drain rates, device loss rates, etc.
 

User Roles

User roles are different than administration roles in that they can be scheduled based on work schedules
Notifications are filtered based on job type and work schedule
 

Notifications

Can you check if Amazon SNS has a platform agnostic payload that can include rich content? We want to include images and links into our content.
We need to be able to have templates for our notifications that can be filled in and localized.
Notifications need to be sent out to specific users based on user role
Need to have notification ID’s so and Device ID’s so device can point at notification and notification can point at device for UX
Notifications will have a resolve button, with some predefined reasons as well as a text field if there is a nonstandard reason. Reasons could be defined by user (or auto populated into text field based on previous ones?)
 

Device Information

In the UX we will show battery level
In the UX we will show and latest unresolved notification based on highest priority
In the UX we will show any other pertinent information (i.e. temperature)
In the UX we will be able to click a device and bring up detailed information
In the UX we will be able to click on the unresolved notification and bring up the notification details
In. the UX we will be able to show the history of the device in the 3D interface, video thumbnails, or a graph depending on the device.
 

Analytics

Need a database to track every click in the UX
Need a standard taxonomy for each button so we can see what the path to it is
Need to be able to generate a report from this data so we can find pain points and improve UX
Need a way to generate a message of the day based on stats, might be a leader board, might be a helpful hint
 

Please keep these things in mind as you are designing your side of the project. If you 


2021-08-18 13:35
I created a new confluence doc, Roles and Permissions
I edited the Itemization confluence doc and refined to include the requirements Greg sent.


2021-08-19 12:12
Organizing the UI Kit blocks. The variety is a bit of overwhelm. Goingthru XD component and library documentation.


2021-08-20 17:23
The entire style guide is presented here
https://constructor.spline.one/

For my puroposes, maybe its just a matter of making sme choices and remoging all the unused definitions from the UI Kit's style guide? 


2021-08-22 15:28
standard icons
APP_MENU_BINS
- Alert
- Temp Pad
- Trackers
- Stations

USER_PROFILE
Avatar Cartoons
- Female1
- Female2
- Female3
- Female4
- Male1
- Male2
- Male3
- Male4
- Avatar Group 


https://iveda.com/iot-sensors-and-devices/
TRACKER_PROFILE
    - VEHICLE IDENTITY
        - brandlogo1
        - brandlogo2
        - car-sedan-icon
        - car-SUV-icon
        - car-
        - carphoto1

    - TRACKER IDENTITY
        - bluetooth icon
        - Type 1 small
        - Type 2 flat card
        - Type 2+ Trakkar
        - Watch
        - TempPad

BASE_STATION_PROFILE
    - BaseStation icon




NEXT
update confluence w this asset listing 


2021-08-22 17:00
updated confluence and cleaned up itemization for component building


2021-08-23 14:30
Meeting w Greg oushed back to Wednesday am
What do I expect to review then?
- completed flow for mobile view
- collated design specification

What do I need to do to make that happen?
- complete the layout work I'm doing 
- Take a look at how the UI kits I've downloaded communicate their specifications
- Take a look at how Bootstrap communicates design specification
- Take a look at the components in the XD library


2021-08-23 15:29
XD does generat4e an interesting kind of specification on a per artboard basis, not really like a style guide or design system. Still its interesting to see and I can think of so many times when screenshots of resentation of this material would have made everyone's life easier.


2021-08-24 11:05
The most obvious thing is most easily overlooked.
I mapped out the screen listing for the design last night. I'd already done so as part of the UX audit. Only now did I think to populate the XD project with those named views.

It looks like a long list, but there's a fair amount of duplication there. Most immediately:

TRANSFORM report listings to handheld view
- make a reporting list component

x connected? [T/F]
x profilepic
x profilename
x last seen [timestamp]
x location
x geofence name [MyOffice, Urgent Care Clinic ]
x City, State [San Francisco, CA]
- battery life %
- in motion? [T/F]


2021-08-24 22:34

Screens


Feed
    - Feed Minimized
    - Feed Menu
    - Feed Drawer
    - Feed Maximized
    - Tracker Itemization
    - TempPad Itemization
    - Feed Listing Groups

Item
    - Item Profile
    - Item History

Application
    - Application Menu
    - Application Submenu 
    ⁃ Search Menu
    - Notifications

User Account
    ⁃   account settings
    ⁃   upload custom profile pic
    ⁃   change username
    ⁃   Change password
    ⁃   Create PIN
    ⁃   Change email
    ⁃   Delete Account



Tracker Admin
    ⁃   Tracker Dashboard
    ⁃   Change Tracker Picture
    ⁃   Change Tracker Name
    ⁃   Share this Tracker
    ⁃   Tracker Dashboard Options
    ⁃   Tracker Dashboard Multiselect
    ⁃   Tracker History Log

Station Admin
    ⁃   Station Device Listing
    ⁃   Change Station Picture
    ⁃   Station Dashboard Options
    ⁃   Station Dashboard Multiselect

TempPad Admin
    ⁃   TempPad Dashboard
    ⁃   Create Logger
    ⁃   Edit Logger
    ⁃   TempPad Dashboard Options
    ⁃   TempPad Dashboard Multiselect

TempPad configuration 
    ⁃   TempPad Device Listing
    ⁃   Change TempPad Name
    ⁃   Assign TempPad device to Logger
    ⁃   TempPad device options
    ⁃   TempPad Device Multiselect

Activity Admin
    ⁃   Signed in device list
    ⁃   Signed in device options
    ⁃   Signed in device multiselect
    ⁃   Remove device(s)
    ⁃   Security logs
    ⁃   Access link
    ⁃   Access link details 
    ⁃   Create access link
    ⁃   Delete access link

Integrator tool
    ⁃   B2B account list
    ⁃   Create B2B account
    ⁃   Revoke B2B account 
Map
    ⁃   map pins
    ⁃   selected map pin
    ⁃   Building interior markers (wrld3d)



2021-08-25 00:24
I've finished adding the application struture as artboards in the XD project
With that stuff in mind, what goes in the application menu?



2021-08-25 03:26
I'll have about 2h before the meeting tomorrow
What can I prepare in that time?
- Temp Pad feed listing
    + Incl


Widget area
- heat map: report type



2021-08-25 13:17
meeting w Greg went well. Also productive. I spent time updating and reorganizing JIRA. Not entirely accurtate, but exposes the work I'm doing better. Updated confluence pages w the revused information as well

JavaScript Error: SyntaxError - Unexpected token '%'

JavaScript Error: SyntaxError - Unexpected token '%'
JavaScript Error: ReferenceError - objDate is not defined
JavaScript Error: SyntaxError - Unexpected token '%'


2021-08-30 15:16
Its been a while since I checked in but I solved the content and layout problem I'd been having with the Tracker Feed over the weekend. Just finished working up my August invoice and am sending that out to Luz (cc:Greg) in a moment


2021-08-30 16:05
Tweaking the invoice page UX and layout. 


2021-08-31 11:48
I've posted the working dataset I'm using as fictional basis (back story)
for various lists. Feed, Notification, Reports

I've come far in my understanding of the Feed actually. Its taken longer than expected, but the design feels effortless and simple to extend. Its nothing I haven't seen before really, but that's actually the point of it. Understanding what data matters, matters.


2021-08-31 12:09
Right now I'm finding and extracting images of various types of tracker products and SKU's to add specificity to the design. Don't spend much longer on this


2021-08-31 12:50
finished collecting those assets. I dont need to process them right now. But I'd like to unzip and collate them in a common place. I've found some interestinghardware, mayvbe even for home use. But also came across some diagram-style PNG icons, etc.


2021-08-31 23:46
I've created and placed components in the Feed, showing different groupings, and so forth
I've updated the Application menu

NEXT
- group alerted item at top of relevant list

a couple of areas that I've not touched. Which will have the most impact?
- Asset Profile
- Reporting Page
- Profile
- Notifications
- Search

I think the most productive use of my time is to layout a report template, since this can be applied in a number of areas


2021-09-01 10:44
pushed back meeting w Greg to 4p in order to address an apparent IT problem with ONYX OPS
https://garyboodhooworld.atlassian.net/browse/OPS-68


2021-09-01 23:54
I've finessed the ordering of feed assets for a variety of use cases
I've built out the framing for the Item profile in drawer and fullscreen configuration


2021-09-02 03:50
NEXT

wakeup 7a
worksession: 3H 630-930

P1 Add a managed access block to asset profile. This shows the user who may own the asset and includes a share with… button
    - Which expands into a dialog allowing user selection from icon/label and also search field which can include an email address or username 

P2 Add a waypoint timeline similar to googles.
    - The number of nodes in the timeline are what get counted
    - Scale for this should be in days not hours
    - Show the last n-days and allow dragging or L/R nav w buttons
    - Legend beneath each histogram shows:
        - Day of the Week (Monday, Mon, M)
        - Month/day (JUN 8, 6/8)

P2 Update feed items by type. Right now everything is showing a temperature
    - What would a Tracker show? What would a base station show?
    - Use full address of location instead of City, State
    - When inside identify the facility by name and represent travel by proximity to rooms or floor “Upstairs", "2 floors up”, “Near the lobby”

P3 Add a path on the map showing any travel for that day


2021-09-02 11:31
meeting went well despite my not being able to show everything I want to. Greg and I are on the same page and he digs my ideas. He said "that was agreat meeting" which felt great. I want to make him look good, and it is imperative to be stand up this full design so that I can communicate with it to vendors and stakeholders.


2021-09-06 14:17
I'm rethinking how I plan and track my work in Calendar. Also want to start the workday here the same way every day. Like Scrum.

Y: OOO
T: Planning

IV-31 IV-31 Standards-compliant wireframe for Locator Pins
- screen captures of interior and exterior maps from WRLD3D
- replace default wireframe bkg with map component

IV-58 Standards-compliant wireframe for the Reports feature
- identify relevant assets in UI Kits (iOS and the Constructor UI Kit)
- create another page in the Excel data set to capture asset names and values
    + use the pinpoint app screens for reference
- layout iterations
    + need to communicate how these tables will behave in restricted widths
    + I'd like to use the same component for the desktop view
        + take a moment to understand how XD responsive layout feature works

IV-28 Standards-compliant wireframe for the Feed
- clean up the data for each instance so that it is relevant for the asset type

B: None


2021-09-06 16:50
IV-28 Standards-compliant wireframe for the Feed
- clean up the data for each instance so that it is relevant for the asset type


2021-09-07 03:01
I've completed IV-28 and optimized the list item and list components. I*'ve switched over to using the Apple fonts in the UI Kit as well. Performance in this document was pretty laggy when I started, the time spent optimizing should make moving forward a lot more fluid


2021-09-07 19:09
good discussion w Greg earlier that led to my spending much of the day thinking about and responding to the device data model. It took a few hours. I'll pick up the design later. Hey - remember. Start identifyuing what you're doing today in the am.

Y:  IV-28 Standards-compliant wireframe for the Feed
T:  data-modeling
        [need to create/repurpose a JIRA task to track this]
    IV-31 Standards-compliant wireframe for Locator Pins
    IV-58 Standards-compliant wireframe for the Reports feature
B:  Became overly focused on the data model (maybe). I felt like it was meaningful, but need to prioritize my time more effectively. Timebox better.



2021-09-09 00:48
Based on conversation w Greg about data types, I've updated the design of what was previously called the Subtitle Line in the feed item. Thats now a stacked group of tags. I've styled the tags to resemble those found all over the web, and to my eye, thats excactly what they read as. Entire system looks quite refined


2021-09-09 13:44
Y:  IV-28 Standards-compliant wireframe for the Feed
T:  IV-58 Standards-compliant wireframe for the Reports feature
    create JIRA task for Design chart template: Histogram (appears in Feed, Profile, and Reporting)
    create JIRA task for Design chart template: Location Timeline (appears in Tracker Reporting: Analytics)
B:



2021-09-09 14:49
created a new dropdown menu component. added filter icon to feed artboards. adding tag selection filter control


2021-09-09 15:13
could you send me the list of stuff we are going to have for employees? I'm going to make a super simple notifications. I'm guessing we need a pointer to their browser so we can send them notifications.

not sure what he's asking for:


2021-09-09 16:10
OK I worked out a model


2021-09-10 11:29
good meeting with Greg this morning. The User datatype definition definitekly required some thinking and mindmeld to simplify the matter. I'm pretty excited abnout how tags and usergroups have merged into a general UX pillar


2021-09-12 12:50
I've just finished building a spreadsheet of the Trackers in the pinpoint demo app. Interestingly, each of the trackers has a timestamped list of locations its been to. The duration between the first entry and the current day is the device's Age, although I'm calling it histoy. With that numbber though you get a picture of which devices came first, which devices joined the network together. Its cool


2021-09-12 13:24





2021-09-12 18:57
I've created a min-width version of a table (not collpsed) Very precise amd controlled. The current layout resembles a compressed view. Probabbly overly-tight for real-world mobile presentation

NEXT
- Data Modeling
    x create Jira issues (Trackers, Users, Notifications, Tags)
    x update Tracker data modeling
    - update data modeling for User
    - create initial Data Model (mind map) for Notifications
    - create initial Data Model (mind map) for Tags
    - share w Greg on Slack
- duplicate and create another version where the profile pixs are shown at default size
- work out a single row accordion treatment with datalabels stacked vertically as in the responsive table demos I looked at today


2021-09-13 14:04
Slight shift of direction. My focus is moved to an investor demo which is intended to communicate the UX pillars and featyures of the design I've been conceiving.

NEXT
- get in contact w Luz and set up a meeting to ask what she'd like to see
- duplicate and create another version where the profile pixs are shown at default size
- work out a single row accordion treatment with datalabels stacked vertically as in the responsive table demos I looked at today

STANDBY
- Data Modeling
    x create Jira issues (Trackers, Users, Notifications, Tags)
    x update Tracker data modeling
    - update data modeling for User
    - create initial Data Model (mind map) for Notifications
    - create initial Data Model (mind map) for Tags
    - share w Greg on Slack


2021-09-13 19:00
continuing work on the report list
I've repurposed the Feed Tabs as a tab menu allowing for paging between Tracker, Temp Pad and Station Configuration. Is this really a valid approach though? The same space could be dedicated to list controls and so forth?
What can I do from The Configure Tracker Screen?
- refresh the list

For Each List Item
- rename Tracker
- change Tracker picture
- remove tracker
- share tracker

List Options
- Select Multiple items
    - remove tracker
    - share tracker
x refresh list
- export CSV

Sort By
- sort by:
    connection,
    name,
    location,
    MAC Address Firmware
    Last Seen
    Battery Level
    Age
- reverse sorting order (A-Z)

Filter By
- connected Devices
- disconnected Devices
- tagged Devices
    - shared with tag[usergroup]
    - assigned to tag[usergroup]
    - tags


2021-09-14 13:03
After sleeping on it and thinking on it further, the pattern of tabbed listings for any of the Reporting screens is wrong. Its seductive though. Visually, it appears to make sense, but holding the XD artboard in my hand on my phone, it feels off. I think its going to be more productive and efficient to consider each of the configuration screens as seperate destinations

If it feels necessary to combine them, then consider making a dropdown under the Screen Title.



NEXT
x follow up w contact at WRLD3D
x follow up w Greg: status report
- figure out where the controls in the header go
- build out the mobile list



2021-09-14 16:39
critical stats mobile view
Name
Profile Pic
Connection Status
Battery


2021-09-15 22:15
purchase full iOS UI Kit that I've been using a subset of before. Mostly fro graphs and charts. I'm sure it will remain useful


2021-09-16 03:22
The UI Kit purchase was a good idea. Helped me think through some use cases with good examples. Great job today.


2021-09-16 10:07
I pushed back the sync w Greg so I can properly map out the interactions and data definitions we spoke about earlier. I still have a number of use cases I need to solve for in the COnfiguration Screen

FOR EACH LISTED ITEM, HOW DO YOU
Rename a Tracker?
Change a Tracker picture?
Remove the Tracker from the list
Share the Tracker with other users

FOR THE LIST, HOW DO YOU
Select Multiple Items?
- Select All?
- Select None?
Refresh the List?
Remove the Tracker from the list?
Share the Tracker with others?
Assign the Tracker to others?
Export the List as CSV?

HOW DO YOU SORT THE LIST
By Connected/Disconnected
By Name
By Location
By MAC Address
By Firmware Version
 By Last Seen
By Battery Level
By History Length (Age)
How do you reverse the sorting order?

HOW DO YOU FILTER THE LIST
Connected Devices
Disconnected Devices
Tagged Devices

HOW DO YOU INSPECT A DEVICE AND SEE IT ON THE MAP?
You will transition from the main (configuration) screen to a secondary screen. The secondary screen is a dedicated map view, similar in nature to the Primary Tracker Map, except modal. Exiting this mode returns to to Tracker Configuration

WHAT SPECIAL NEEDS DO THESE OTHER SYSTEMS HAVE?
- Base Station configuration
- TempPad configuration
- Administration: Signed In Devices
- Administration: Security Logs
- Administration: Access Links
- Administration: B2B accounts

WHAT ABOUT USER MANAGEMENT?
- I don't have a guide to go from here. Standby.



2021-09-17 17:21
Good meeting with Greg asked as many questions as it answers. Its cool to engage with him, and it seems like he's interested in the work we're doing.

I'm transiting the current XD doc into a new one for cleanup and refresh before going further. I've spent time working with the data modeling spreadhseets as well. in part during the meeting, and then afterwarrds for cleanup.

Greg asked me to do same for Notifications. I'd started down this path already, but I want to be very specific and limit the possibilities. When demoing this morning, I realized I could only call upon my own narratives to support the rich notifier I designed.



2021-09-17 17:51
<!-- Some Real Talk. Howdoes this technology work -->
Each tag transmits a unique identifier using Bluetooth. The nearest beacons receiving this signal transmit their location along with an estimated distance for the tag.

Geofencing is setting up a network of beacons to make determiniations about what is within a physical space, when it enters, when it leaves.


CONSIDER THESE 3 USE CASES:

Often, mobile medical devices are not where caregivers need them. Pinpoint can identify the exact location of every piece of equipment on a map with Bluetooth trackers. An alert can be sent to appropriate individuals when equipment is removed from an area or taken out of the building.

Iveda’s TempPad sensors can be used to monitor patients’ temperatures. This eliminates nurse’s visits to patients’ rooms for temperature monitoring at all hours of the day, reducing the number of times patients need to be disturbed.

The TempPad sensor can be employed in the private sector as part of a Covid-19 installation to thwart the spread of the virus. Workers at factories and employees at hotels can wear a small TempPad while they are on duty. An alert is sent to appropriate individuals at the organisation when a high temperature is detected. Pinpoint can show the exact location of the worker and where that worker has been, which helps in contact tracing.


WHAT IS A NOTIFICATION?

WHAT IS AN ALERT?
- a type of notification for when things go wrong.
- what can go critically wrong?
    + Device loses power
    + Device measurement (temperature) is out of $RANGE 
    + Device signal strength is less than $THRESHOLD
    + Device no longer registers on network
- mistakes
    + Device isnt powered on
    + Invalid measurement $RANGE

WHO SEES NOTIFICATIONS?





WHO SEES ALERTS?

WHO RESOLVES AN ALERT?

WHAT IS THE DIFFERENCE BETWEEN *SHARE WITH* and *ASSIGN TO* 



2021-09-20 18:05
Very interesting meeting with Iveda this morning. Its documented in my notes. Some greater insight into what they're calling a Cerebro UX trailer. I kind of understand what they are asking for, at it actually includes B-roll as well. I'm setting up the project after reviewing and thinking about my notes. I promised Luz I'd send out a summary today and am getting prepared to do so. I've created a new JIRA epic for this work. I've created a new Milanote board to collate a creative brief. Sounds like a story for Jira


2021-09-21 17:09
I've been working on a creative brief all day



2021-09-22 01:04
Start the day tomorrow in the XD project
Refactor the feed items
- replace accordion dropdown caret with a "next" ( > ) icon
- the line item will open like an accordion (more like an overlay actually) as currently designed but, triggered on long press
- replace all inline tags with current design

Refactor the tags
- the inline tags will reveal a "next" ( > ) icon on hover
- color code "assigned" usergroup tags
- color code "shared" usergroup tags

Work with the WRLD3D map layer
- this design can easily be brought to life with the map layer, but it will need color correction


2021-09-22 13:34
I've spent about 1.5h on the creative brief. I pinged Luz to let her know I'd be sending it her way for feedback and clarification. The board is ready to send out. Here's what I need to include in the email

- link to Creative Brief milanote board
- link to Google Drive filesharing
- link to Jira project epic
- am I able to invite her to Slack?


2021-09-27 12:48
checked in w Greg on my status
sent mail to Luz to check on availability


2021-09-28 11:49
I'm working on the UX survey. I'd like to wrap this up by 1p and move on
I did some project planning/management. Added additional JIRA stories for CEREBRO UX Trailer. Updated my time status on PINPOINT. The stuff I capture from WRLD3D today can serve both projects. I want to spend most of my time today w Pinpoint, so lets do that.

Set up a review with Greg on Thursday @2p and i want to deliver:
- Flows as shareable XD prototypes
    + I'll share the link with him so he has an opportunity to touch the design
- Reworked Feed
- Reworked Map View
- Device Profile
- Notifications
- Profile Menu
- App Menu
- Device Configuration
- Device Reporting

How realistic is this? I want to set some limits for myself and avoid going deep and avoid XD housekeeping as much as I can

In an XD worksession, how do I spend my time?
- stepping away from machine to think
- capturing reference
- studying the UI Kit
- Sketching
- Prototyping
- Explaining




2021-09-28 23:32
Hello Iveda, I'm Gary Boodhoo. I’m a product designer working with you on  Pinpoint and Cerebro. This research will help me understand the company's core values. 

recognize similarities with video games I’ve worked on as well as various smart home apps my family relies upon. 

This survey helps me connect solutions with human motivations.
Your responses are anonymous. Completing the survey will take about 5 minutes


That’s a big ask but I believe together we can push the  can Cerebro be fun? How is Cerebro a part of your life
How does Cerebro benefit society
What role does CEREBRO play in my life. My investments. My security. My wealth. My security. My peace of mind. 

Freedom from choice
Inanimate world aligns with your responsibilities

 on UX related and have a few questions about your organization . This survey keeps me in touch with industry sentiment throughout my network and makes me a better creative partner—everyone wins! Your responses are anonymous. Completing the survey will take about 5 minutes

ADDITIONAL QUESTIONS
Name some characteristics you'd like investors to associate with Iveda

PURPOSE

PERCEPTION

IDENTITY
Who are your competitors?
Who are your customers?
Who are your partners?


VALUES

EXPERIENCE
What makes your customer experience better than your competitors?



2021-09-29 03:46
I completed editorial work on the survey. Its a lot simpler and shorter. I'll distribute in the am. Will need to edit the email introduction. Shorter. Just repeat the survey intro if that works 


2021-09-29 12:26
Ugh. I went too far out in scoping the Cerebro UX trailer. I got an email from Luz and her tone was frustrated. But to be fair, I was blocked by not knowing  4pthe deliverables she was requesting, as I felt our earlier conversation was very high level. Our phone call was pleasant. Everything is fine. She needs fantasy UI for Cerebro screens. These are b-roll elements ultimately. They don’t need ti be hugely specific but they do need to look “interface-y” and shiny. This is straight up visual design, not UX or even the strategic storytelling I expected

I've updated the Jira story and created subtasks for the deliverables


2021-09-29 12:28
I'm preparing to send out the brand value survey

NEXT
- collate some intel for the What is Cerebro Board
- reschedule Thursday meeting w Greg. Monday afternoon will give me some space to work on the goals I want to meet for the review
- update Cerebro creative brief to include new facts. Same stuff I added to Jira

THEN
- capture imagery from WRLD3D
- visual design for the login screen
    + Take a look at the initial UI reference board and take cues from Tron.
        * Add surprise by presenting dark mode and light modes 
    + use the UI Kits and avoid thinking too much about where youre going with this
    + The goal is to provide assets to Luz for any course correction
- post work in progress to Luz at 4p


2021-09-30 12:48
Today's goal is to deliver a Cerebro desktop layout incorporating a WRLD3D MAP to Greg and Luz
---

NEXT
- capture imagery from WRLD3D

THEN
- layout a MAPVIEW screen
- integrate WRLD3D imagery

2021-09-30 16:24
I've captured a variety of WRLD3D screenshots at 3840x1600 21:9
I'm going to see if I can capture some video as well.


2021-10-01 13:18
Let's timebox this. Setting up 2h work blocks 
What do I want to accomplish 

- application framework
    + sketch
        * device feed
        * where are notifications shown?
        * what would a pinned feed look like if it didnt need to be pinned to the list?
        * search - tags / sort / filters / text field
    + add application layer to XD from sketches
    + add sidebar layer to XD from sketch
    

2021-10-01 15:28
Haven't started the Sketching session yet. Greg contacted me and asked about where we were with the Phase 1 deliverable. I'll put together a list based on Jira. I'll tag the relevant items in Jira and see if I can organize in that manner as well 


2021-10-01 15:56
I've collated the work issues in JIRA under an MVP tag as well as P1,P2,P3 tags for priority.

NEXT
- go through the identified tasks and revise any estimates
- add a new story


2021-10-03 15:22
How's the skethcing going? Are you done? No. 
Let's rock then. go!


- application framework
    + sketch
        x device feed group
        x  device feed list
        x device profile
        x where are notifications shown?
        x what would a pinned feed look like if it didnt need to be pinned to the list?
        x search - tags / sort / filters / text field


2021-10-03 20:27
I think I'm clear on how this layout looks and works. I need to get it setup in XD now

- draft
    + add application layer to XD from sketches
        * app menu
        * headr and stats (online count, offline count, last updates)
        x feed groups
        x feed list
        * device profile
        


2021-10-04 00:52
working on the feed listing. There's some additional framing to consider


2021-10-04 01:13
I worked out the framing metrics for the feed, and added the additional detail. Looks pretty good. Ev 6aerything is now in dark mode

NEXT
- feed groups

bed: 2p
wakeup: 6a
    

2021-10-04 10:25
as exopected, I spent time refining the Feed List. Same as Before. Its what I like best I guess. This is definitely the best visualization of it yet.

What do I want to present to Greg today?
How long will it take me to prepare. No new design. Continue clean-up from where I left off. Stand up as XD prototypes
3h?

that would meen starting on it at 11a, In 30m
I'll give it 2h and see where it goes
There's more to discuss than the design work
- state of the design
    - estimates
    - manage expectations
        + desktop layouts
        + functional spec
- MVP deliverable
    + frame this around an exec presentation
    




2021-10-04 14:03
Define the criteria for MVP
Take a look at JIRA estimates

Good meeting. I captured Greg's priorities in the Excel doc I used to summarizze Jira tasks.

Wasted an hour being "precious" about made-up funtionality for the left sidebar. because it didn't look "busy" enough isn't a great starting point. Thing is, I'm trying to uimply purpose here. But honestly, I', ideating instead of assembling. Do better. Get past this.


2021-10-05 15:29
Wrapped up device group panel. 
Starting on Device profile panel
Started blocking out vertical App menu

- draft
    + add application layer to XD from sketches
        * app menu
        * headr and stats (online count, offline count, last updates)
        x feed groups
        x feed list
        * device profile



2021-10-05 17:39
I'll pick up the device profile design in my next worksession
I created a couple of simple variations of the exiting layout
I cleaned up the dropdown menu in the "device iventory"


2021-10-06 00:56
continuing work on the device profile
added controls to expand/collapse a list of users assigned to this device
added controls to expand/collapse a list of users sharing this device, including their online/offline status.
Working on the device history
- I also want to show the devices age
- replace the user profile pics with the same 




[Device management
Add new devices
Camera device-type

Camera device profile
History reporting for cameras

Tag management
Add/Remove tag(s)!
Tag list

User management
On duty/off duty status
User Daily schedule
User History
User list
User profile

Group management
Join/Leave groups
Create/Remove groups
Add/Remove user(s) to group(s)
Group list
Group profile]()



2021-10-06 15:28
P1 Notifications
P1 H


Map
unnaxsignment states
unauthorized entry
Device


2021-10-07 15:56
I spent much longer today on project management than expected. Some of it from unfamiliarity w Jira. Some of t=it just thinking things through. I've moved everything under an MVP story and created my own Board which only shows tyhese issues. I need to think a bit further on how the workflow should look
I had assumed that items would move from
To Do to Handheld wireframe to Desktop wireframe to Documentation

Maybe that is actually
Handheld Wireframe (in-progress)
Desktop Wireframe (in-progress)
Documentation (in-progress)

But what about cases where multiple items are in progress or work isn't proceeding sequentialy?

Exactly.  



2021-10-08 00:25
doing some XD project cleanup. XD is acting pretty flaky at the moment. Maybe due to Win11 update? Maybe due to too much stuff in the project.


2021-10-08 01:32
project seems ok now. I cleaned up the feed listing and then cleaned up the artboards in the Feed Posture flow. First thing tomorrow, I want to capture some appropriately sized assets from WRLD3D, similar to what I did previously then integrate them into these artboards

Before meeting w Greg, I want to do more work on the Desktop design
- collapsed Device Group
- add tracker history to Device Profile
- App Menu
    + what items need to be in this listing?
- Notifications
    + pull from mobile design and integrate

If its easy, I'd like to try showing a mobile layout and a desktop layout using a nice presentation template.


2021-10-08 12:57
I set up a meeting w Greg at 2p. Part of our more agile working process. I want to go over the Notification system with him again. I'm preparing that material in the handheld layout and want to see if I can getf it stubbed in to the desktop so he'll have a different context


        

Informational (something is about to)

Warning
Alert
System
Access-Control

Nobody on call? alert who?

Camera


Thermal
Motion Event

When creating user groups,,include a point of contact if nobody is on call
a point of contact. Groups can have nobody on call if asked
there can also be an alert frequence. An alert frequency can be set

Rooms can be set to occupied/unoccupied

A user group needs to be able to alert someone (designated person ) on call if there's nobody in it

If there's a room that is occupied but theres no one assigned to it (condition:something is wrong)


we discussed a new persistent state for rooms:
in use/not in use
this can be signified similarly to on-duty/off duty

ROOM PROFILES
think about how to profile a room or area  

the area is plotted on a cerebro map , which is part of a floor, which is part of a facility, which is part of a region

EastCoast.MayoClinic.Floor1.NurseStation

Inside this boundary there may be multiple devices. These devices are assigned to the location in the same way they can be assigned to a User/Usergroup

The room can have a schedule of availability. This is just the hours when the room is considered "on-duty"

The room may be flagged as occupied/unoccupied (based on camera input, based on tracker position)

When a room is off duty but occupied, it will broadcast an alert


ALERT-HANDLING
Notifications are setup in a relevant Asset Configuration screen

Alerts have a timer. When the timer runs out the alert is escalated and broadcast to the next person(s) of interest designated on the asset

Multiple persons of interest can be added to the escalation chain. Each rung of the chain has a timer that escalates to the next rung if it runs out



2021-10-11 15:46
Pushed back meeting w Greg so I could think through Notification types & states more thoroughly. I made some edits to the handheld menu bar so I could think about how to communicate the "on-Duty" state. In apps like Slack, Messenger, this is signified by a filled in or empty circle. next to the profile pic


2021-10-11 16:32
Finished reworking handheld menu. Better sizing. Defined the on-duty/off-duty state. Applied changes to existing layouts 


2021-10-11 18:01
I'm working on the notification list. I'm not feeling 100% about it.


2021-10-12 00:21
I fixed up the notification page title, but it was more than that. I had my layout patterns for the flow a bit mixed up. This version is better, and I can use the same pattern for others screens. 


2021-10-12 01:20
I penciled in a meeting w Greg at 11a. Let's see how notifications looks after an hour of work in the am


2021-10-12 16:16
Greg isnt available today or tomorrow so I'm going to post my work to Slack for visibility


2021-10-13 01:39
I've created a content matrix of notifications which calls out
Asset Type
Notification Type
Escalation
Resolution

Warning
Alert
System
Access-Control

When creating user groups,,include a point of contact if nobody is on call
a point of contact. Groups can have nobody on call if asked
there can also be an alert frequence. An alert frequency can be set

Rooms can be set to occupied/unoccupied



ROOM PROFILES
think about how to profile a room or area  
the area is plotted on a cerebro map , which is part of a floor, which is part of a facility, which is part of a region

EastCoast.MayoClinic.Floor1.NurseStation

Inside this boundary there may be multiple devices. These devices are assigned to the location in the same way they can be assigned to a User/Usergroup

The room has a schedule of availability. The schedule designates when the room is  "on-duty"

The room may be flagged as occupied/unoccupied
The room may be flagged as on-duty/off-duty
When a room is off-duty AND occupied, it will broadcast an alert

USERGROUPS
A user group will broadcast a system message when it is empty
A user group will broadcast an alert when there are no members on-duty


ALERT-HANDLING
Notifications are setup in a relevant Asset Configuration screen

Alerts have a timer. When the timer runs out the alert is escalated and broadcast to the next person(s) of interest designated on the asset

Multiple persons of interest can be added to the escalation chain. Each rung of the chain has a timer that escalates to the next rung if it runs out


2021-10-13 18:57
how long has there been a problem?
who else has been notified



2021-10-15 10:11
Greg is going to send over a PEO file for handoff to WRLD3D

wants me to take a look at it

someone clicks on a room
they can take action on it
can use Room Profile as control surface

What ae the actions you can take
Use the Device Profiles to show what an admin sees, what a user sees

is it possible to deliver different HTML in point of interest (profile)

On search we want to have voice queries

Localization support
for now we are using EN-US
want: ES
want: XX (the one for Mandarin)

Point of

our roadmap
PINPOINT -> IVEDAAI -> SENTIR

Robust Notification system
Robust user access system

our goal is to build this up in stages
SmartCiti



Dont forget about 
TEMPORAL ACCESS
HISTORY

If I click on a NOTIFICATION it goes bak in time and shows that you're looking at the PAST vs NOW (LIVE)

We're giving them an INTERIOR of the MESA office as Blueprints
I need to be able to discuss and describe how that map can be populated

DAVID and GREG want CYBERPUNK look and Feel

FUN!!!
do a cyberpunk 




Greg wants to have demo up nd running at office
By NEXT WEEK wants to send our roadmap out to WRLD3D
Want to build this up piece by piece

Need to setup my relationship w WRLD3D

Quickly be able to get to Facilities (based on my roles and permission)
from Facility 1


Each room is a geo-fence
get them started on the maps

This material isnt compete
but here;'s what we are trying to do
Notifications
Tagg'

How do you want the data for the trackers
Is it an API call?
Are they objects on a map.

Indoor map and an outdoor map
with 1 map per floor

We want each room or hallway to be seperate geofenced areas that align with each other

The zones shown here are for our usage and not relevant to the mapping. 



WATCH_DOGS 2 is a 2016 action-adventure game developed by Ubisoft Montreal and published by Ubisoft. It was released for the PlayStation 4, Xbox One and Microsoft Windows in November 2016, and Stadia in December 2020. Set within a fictionalized version of the San Francisco Bay Area



2021-10-20 09:54
I spent a lot of time - the whole day. A long day. reformatting the Powerpoint document I was asked to look at. I couldn't reasonably call it good corporate communication. I went with my gut. No regrets there, but I need to consider my unique contribution to the content, as well as use this document to lead the creative team. 

Think of what you need to communicate to the people making the map
what are they making?
what are they integrating>?
what is their time frame?

Who else is on the team?
Marko?

Assume then, that its just a high fidelity custom map
What is the bar for quality?
How do we determine quality?
What types of production design do we need?
    - the building exterior is fairly bland. Does it have to be?
    - what creative resources do they have there?
    
Lets say there is a creative lead there. This document is for them. Use what you can from the creative brief completed a while ago

Start from this point:
A detailed model styled to your requirements

Our requirements are:
- interior model of the mesa office, addressable by Zone and by 



2021-10-20 14:47
Send over some desktop work and incorporate CLARO branding elements in that work. Tell her that you heard 


2021-10-20 22:51
Building out newly title MVP deck based on the items Greg & I spoke about. I can correlate these to Jira tasks if necessary.

Tomorrow: confirm the physical address of the Mesa office
Finalize deck for draft v3

Luz would be thrilled to see some Claro branded desktop mockup work. 
How can you start incorporating that into the design by default?Send over some desktop work and incorporate CLARO branding elements in that work. Tell her that you heard 


2021-10-22 07:59
I got a bit of an urgent message from Greg. He's needing reassurances that we've got this. I could help but feel a little anxious, but the truth is - we've got this. I've added slides for all the details we discussed on Wednesday and am filling out the line items for each

To be honest, I'm not exactly sure what kind of document this is. It mostly resembles a kind of onboarding packet or maybe a statement of intent. Before meeting w Greg at 10a I will:
- fill out all UX Feature slides
- replace station pins with a nicer, more visible asset


2021-10-22 10:45
Meeting with Greg went well. I verified some specifics with him. He was able to see some missing parts as well. We're on the same page. One thing in particular that needs to be mentioned prominently is the relation of PinPoint within the Iveda CEREBRO ecosystem. I captured my notes about that and shared w Greg while we spoke to confirm. That text needs a bit of massaging


2021-10-22 10:47
I suggested that I just post updates to Slack. This is in part to manage expectatins but also keep me on track and transparent. This deck is shaping up pretty well

- normalize all content formatting
- finish the requirement text on remaining slides
- curate and add illustration from my design files and reference in support of the requirement slides
    + the harder ones
        * show device movement history
        * show camera view history
        * show a room profile containing all objects in the room

- construct a diagram showing the relationship of Pinpoint to the Iveda Ecosyste (I did a very quick sketch of this live w Greg)
- add link to zeroheight design system


2021-10-22 15:37

CONSTRUCT INTERIOR AND EXTERIOR MAP OF THE IVEDA OFFICE IN MESA, AZ


2021-10-25 09:58
Whew.
Up all night finalizing this deck. Maybe I've left some stuff out.
I collated my work and labeled the missing parts so Greg can get an overview at a glance.

Sending that out to him now and sharing current pptx on Slack



2021-10-25 13:48
reworked the Cerebro Server diagram. Cleaner


2021-10-26 15:17
Meeting w Greg at 4p to discuss next steps after the MVP demo deck misadventure. What are some questions I can ask to prompt a valuable conversation?


2021-10-26 17:39
Greg rescheduled meeting for tomorrow. We're focused on what to handoff to WRLD3D right. I had made the statement yesterday that the Feed and Notifications were the most developed and I could document them as screen designs (after some cleanup and editorial). I actually think the more useful vertical slice is The Feed and The Resource Inspector.

The Feed is better considered as an inventory, so I'm renaming it to RESOURCE INVENTORY, or simply INVENTORY




2021-10-27 10:49
I've thought about the recent disconnect and how to use the lessons learned as a win, rather than a loss. Here's what I've come up with.

- Switch from XD to Figma
    + More shareable
    + More social
    + Multiple layers of detail are inspectable by devs
    + Stakeholder get an overview of the design process and can participate too
    
- Make a list of MVP design work that needs to be completed
    + organize it into a series of "releases"
    + be sure to mention that the design documentation will be accessible to everyone before I finalize it
        * In that sense, we release continually
        


2021-10-27 12:10
MAP
- data integration w Calvin
- construct map view in world

NOV 20 TARGET
connect w Ian (technical), Nigel (bizdev)


2021-10-27 12:30
Ugh, that call w Greg was a bit strained. He's clearly stressed, and I can certainly empathize w his position. After giving myself some space, I'm surprisingly able to disconnect emotionally, and I hope thats a good sign.

Here is the priority

Get Custom Map Working in-environment

CALVIN
- Speak to Calvin about data integration requirements / connect via email cc. Greg Omi / connect via Slack start shared conversation w Greg Omi + Calvin
    + Send him revised MVP Demo deck including Map Reference only
    + Share WRLD 3D developers link w him
    * The team at WRLD needs to know how to integrate their map objects with existing Iveda Pinpoint map internals
    + We want to think about maps as a hierarchy
        * Facility.Map.Room.Station
    + The team at WRLD is expected to provide import and export of static map features to a common format like CSV
    
GREG
- manage his stress and make him feel like a hero
- Send him revised MVP Demo deck including Map Reference only
- Send him a link to a Figma workspace with content stubs

WRLD
we want the exterior modeled
we want the interior modeled
We want you to integrate a custom WRLD map with relevant data from Iveda Pinpoint back end
We want to know who our day to day point of contact is?
We want to login to the World Builder tool under an Iveda account



Locations
Data model
ID
Name
Facility.Map.Room.Stations
Import/Export
Common file format
Working Example
Construct map view in world



2021-10-27 13:40
Finished editing the new WRLD BUILDING REFERENCE deck
sent out to Greg

NEXT
- draft email to Calvin
x draft email to WRLD (Greg)
- construct Figma project
- transfer XD to Figma
- create Project structure incorporating all UX details identified in the previos deck's index.
- cleanup Jira to reflect task/issue updates


We want to put together a demo of the technology to show to partners. I’m sending a map of our Mesa office where we will have a tech proof of concept which I would like your team to build. Initially, it is fine to have on your public servers as this is not a real client location.
We would like to have each room a separate geo fence/region and be able to do wayfinding to each room or tracker. The map shows the locations of the base stations which will have additional information (id, mac address, etc.) that needs to be sent to our backend for calibration reasons. The coordinates are 64-bit integers and I’ve arbitrarily set the scale to 1cm per unit (for future improvements of accuracy). I believe with 64 bits we should be able to easily cover the whole world using the same coordinates.
After we have the initial map in, we will have to coordinate with your team on how you want to send and receive data between your code and our backend. We’ll get you set up with access to our temporary git repo to check in any changes that would be specific to our code. We’re currently setting up something more permanent (VPN, private repo, DevOps, etc.), but for demo purposes, we will work a little agile and get something stood up quickly in our temporary environment.
I’m fine getting things running with what your current engine does and then gradually adding or customizations. I think it might be best to set it up on a project-by-project basis and get cost estimates per project, rather than try to give you everything at once, and have one huge project. I suspect you already have many of our features implemented and we may just need minor modifications to get our data into your engine.


2021-10-31 16:34
Prepared invoice for sending out in the am
I've transferred the XD project to Figma, and still finding my way around the interface. It looks awesom though. Wish I'd started using it sooner.

I'm building out a design guide in conjunction with the design files. Here's what I want to distribute in the am with a shared link:

x About Notifications
x   What are Notifications?
x   Notification stages
 
Resources
- About Resources
    + transfer from Powerpoint

- Representing Resources
    + include datamodel spreadsheet
        * use mindmap instead actually
    + include list of devices in an inventory stack
    + include list of devices in notification stack
    + include WIP device inspector
    + include WIP map pin
    
- Representing Users
    + include datamodel mindmap
    + include list of users in an inventory stack
    + include list of users in an notification stack
    + include WIP user inspector
    + include WIP map pin
    
- Representing Spaces
    + create datamodel mindmap
    + include datamodel mindmap
    + include list of spaces in an inventory stack
    * include list of spaces in an notification stack
    + include WIP space inspector
    + include WIP map pin
    + include WIP map label

    *** NOTE ***
    Place Icons
    Icons on Interior maps represent OBJECTS (devices) or PORTALS (map UI that gets you from one place to another, such as an entrance, exit, elevator, doorm, stairway)

    Place Labels
    Places are represented by (selectable) text labeling on the map.
    - Selecting a Place Label shows an INSPECTOR
    - Choosing a Place Label
        + shows an INSPECTOR
        + shows an INVENTORY (all Resources in the Space)
        + The INVENTORY listing offers PREV/NEXT views (so customers can return to the previous "page")

NOTE!
Rooms get a dedicated Inventory Slot now, which allows you to list all the geofenced boundaries on the map.

Escalation

If an issue is unresolved for long enough, a designated usergroup begins receiving notifications from this device

While the issue is unresolved, additionally designated usergroups begin receiving notifications from the device

Upon resolution the timer stops and any assigned or designated users will be notified. Designated users no longer receive notifications from this device


2021-11-01 17:10
Good chat w Greg. He certainly seems more confident in the project again, so it good to have him back. I demoed Figma and showed him where I was at with the refactor and described the benefits for a distributed team. He asked me to:

Introduce myself to the WRLD team
    - general email to Ian & Nigel
Invite the WRLD team to our Slack
    - Ian
    - Nigel
    - https://join.slack.com/t/ivedadesignteam/shared_invite/zt-yffcgfvk-XQWZmI2rsdeTtxbHHArarA

I can do this without sharing the Figma workspace.



2021-11-02 09:54
drafting message to invite the team at WRLD to join IVEDA Slack

Dr Iain Bethune
iain.bethune@wrld3d.com

Head of Software Development

Nigel Fox
nigel.fox@wrld3d.com
Business Development Director



Hello Iain and Nigel,

[Gary Boodhoo] here. I'm working on product design for the Iveda Pinpoint application and wanted to introduce myself.
https://www.garyboodhoo.world/

Here's a invitation to our Slack workspace. Please share it with the relevant members of your team
https://join.slack.com/t/ivedadesignteam/shared_invite/zt-yffcgfvk-XQWZmI2rsdeTtxbHHArarA


Some of my concepts for Pinpoint were inspired by features observed in the Map & Place Designers. I want to get a creative dialog started in two areas: reactive behaviors on the map, and visual formatting of some front end bits. Who can I connect with?



2021-11-03 10:12
Iain joined our Slack and suggests we join Slack Connect which offers more flexibility. He said he's send an email invite bit not seeing it. He & Greg mentioned a meeting on Friday. I've not seen the invite, but going thru an email chain is the worst. Feel like I'm missing something there.

In any case - that's my target. Whatever I'm doing w Figma needs to be done today.

- I want to read the documentation for the Untitled UI Kit
- I want to setup the project like the ones I'm seeing with a preview image, etc...
- I need to block out artboards (frames) for all screen designs - call this a sitemap
- I need to post the URL to the team


2021-11-03 14:58
Team Libraries for sharing components across projects.
build on the foundation we established with Components to make design systems easier to create, maintain and use across an entire team





2021-11-04 12:06
Topics for discussion at Friday 9a meeting with WRLD

How are trackers (dynamic resources) represented on the map?

How would dynamic heatmaps be implemented in the WRLD framework?
Is this a vertex shader? Could it be?
For example, if I wanted to see how a resource moved around over the last 30 days, I also want to see when it was stationary. Presumably many objects do the same things, or don't move, and I'd like to communicate that in the environment as well as using a map pin.

How can I inspect map resource objects and view the datastructure already implemented? Is this covered in the documentation? 

Where does our map demo live - on a private server? Is that our server or WRLD's? Can anyone run a WRLD server?

When a resource is focused:
Boundaries, such as rooms, will be color coded. When hovering over a room, I want that room to appear brighter, by drawing everything outside the room a bit dimmer

Whenever a resource is selected:
Everything outside the region(s) containing the resource is defocused

Whenever a collection is selected (from search result, from inventory slot)
Everything outside the region(s) containing the collection is defocused


2021-11-05 09:04
meeting with WRLD


2021-11-05 09:06
Where do the maps live?
How can we restrict or control access to maps?

If I wanted to restyle the front-end gfx, where would I push those changes?

Its possible to restrict clients to an indoor map (they can't go outside)

Points of Interest (POI)
Was Ian saying that these are sperately handled for realtime?
Dynamic data doesn't go through WRLD, we handle that on the client side


2021-11-05 09:55
After asking about it, we decided that WRLD will share their working project with us. Sort a test harness before we arfe abe tostand up our own application


2021-11-05 10:09
You (and Calvin) should take a look through the WRLD API reference for a sense of what the system is capable of.


2021-11-05 10:21
Takeaways:
friendly knowledgeable team
gating factors: access to common repositories
for reviewing WRLD work - we can use a shared project
for front end work - not sure, I don't think we'll have a repository available, but surely we can get something ad hoc as needed. This would bve for a use case in which we were restyling th UI widgets using CSS


2021-11-15 15:04
Meeting w Greg
First look at Figma project

He really liked what he saw
Seemed super intrigued by the object-oriented natyre of it. I provided good use cases for theming and icon management


2021-11-17 11:50
I've sent a meeting request for Friday 11/19 9a PST to Ian & Greg
This will be the public debut of the design
Its important to look complete, even if unfinished

PRIORITIES
- continue cleaning up handheld sitemap
- construct desktop sitemap
- remove chaff assets
- verify URL and viewing in browser

2021-11-22 08:57
Meeting w Ian & Greg about the design, reviewing the design.
He's needing more scope - who is doing what - on the dev side. What process is running wwhen an event happens - there are results taking place on the map


2021-11-22 09:23
I think the meeting went well, and is actionable. With the holidays coming up I don't know how much will get done, which places me at the inflection point of this project. RIght now, my truth is the only truth. lol. I'm sure that will change, but I want to be aable to capture this for reference and because I think its a human factor that this design improves with.

My audience is:
Calvin: back-end
Ian: CTO/WRLD
Greg: CTO/IVEDA
UnknowDev: front-end dev

My role is:
facilitator
liasion
glue
product designer
visualdesigner
coolhunter


2021-12-01 20:34
I'm working out the details of the various resource inspectors for design review with Greg tomorrow


# What do I need to know about a Device?

## What is it's profile picture?
- default iconography if not customized

## What is its name?
- Device Friendly Name

## What kind of device is it?
- Bluetooth Tracker
- Bluetooth Beacon
- TempPad
- Sensor
- Watch
- Phone
- Vehicle
- Camera
- Media

## Where does it belong?
- Map Reference
    + What facility?
    + What floorplan
    + Collection of rooms/boundaries
    
## Where is it now?
- Indoors
    + Map Reference
    * position relative to a point of interest (beacon, fence)
- Outdoors
    + Point of Interest (address)
    + GPS coordinates (when there's no address)
- No location

## When was it last heard from?
- today (now)
- today (minutes ago)
- today (hours ago)
- date & time

## Is it connected?

## Is it on-duty?

## Is it occupied?

## What is its battery level?

## What is its signal strength (stations)

## How old is it?
- Does it’s age correspond with a significant event?
- Does it’s age correspond to a milestone of any kind?

Device Type: 

## What are its sensor readings?
- Current reading
- Signify if value is trending up/down
- How many readings have been logged todaycurrent temp 

## How much time has passed?
- Show how long a user has been on duty
- Show how much time a room has been occupied 
- For a camera, how much footage has been archived?
- For a station?

## How many alerts has this resource broadcast?
- last 24h
- last week
- last month

## Calls to Action
### Location Utility
- Play Sound
- Directions To

### Ownership Utils
- Assign To
    + Group
    + Space

### Alert Handling
- Mute
- Resolve Alert
- De-Escalate Alert
- Cancel Alert

### Analytics
- Location History
- Alerts History
- Configuration History
- Camera History

## Who is it assigned to?
- These usergroups receive this resource's notifications

## Who is it shared with?
- These usergroups can see this resource on the map

## Under what conditions does this resource broadcast an Alert?
- Out of Range
    + Resource is no longer located where it belongs
- Battery
    + Low Battery
    + No Power
- Connectivity
    + Disconnected
- Sensor Reading
    + reading is below minimum value
    + reading is above maximum value
    + no reading
- Radio
    + Low signal strength
    + No signal



Greg & I are talking abou6t the location graph
need to treat it like an audio editor scrubbing tool
The histogram becomes useful when tiny because you can see larger patterns

Need to be able to switch modes between history
Take a look at the iphone camera application for an example

consider using colors and shapes + overlay + size to indicate differences between calencar modes

Being able to look at history as a calendar is the value add
fluid navigation from years to months to days is the heart of the feature 
The iOS Calendar app was mentioned as a reference
I think that Audio/Video timelines are also a good reference

Allowed areas & Disallowed areas
Some spaces can be labeled Allowed. Leaving an Allowed space triggers an Out of Bounds warning
Some spaces can be labeled Disallowed. Entering a Disallowed space triggers a Trespassing warning

The History Navigator is the 
Make sure to define the UX clearly

Make sure to map out the flow for assignment
Make sure map out a basic 

we will add a sorting feature for notes: tabs


get a flow review on the calendar. 
for the components discussed today
include

Reach out to Calvin, and bring him into the project. Any concerns or consequences on the back end will influence the design.

I've had Calvin in mind for the Product Guide editorial I've been developing. I will ask him for feedback on the design guide in general.  


The rule engine.
Don't try to focus on all potential cases. Put your attention on cases that can be evaluated.
Consider using a "wizard" like 

Time is our secret sauce
What going on in the world at that time
All of a sudden this just became the Sims vs Sim City Game I always wanted to play
That csame clock control can include a method for stepping backwards and forwards. 

The map view can include a global Time CLock
Is it possible to go back in time? 
Not just a single device. All the devicess. The entire network

2021-12-05 13:19
I started organizing my reference and my thinking using Notion. I spent some time formatting and arranging and importing content about different features: Automation Features, History Features, Checking In
I am going to post the link to Slack a bit later once I have it clend up a but more

TODO
P1 prepare invoice
P2 DESIGN: Device History UI
P3 SKETCH: Automation (alert rule setup)
x cleanup and organize NOTION
P3 set a design review agenda for next week
P2 create a spreadsheet to aggregate top 10 content from sources Sam & I choose

NEXT
x prepare and send invoice
P1 PM: Setup Skinjestor Notion and verify guest invitations as well as public links
P2 DESIGN: Device History UI
P3 SKETCH: Automation (alert rule setup)
P3 set a design review agenda for next week
P2 share 
P2 create a spreadsheet to aggregate top 10 content from sources Sam & I choose



2021-12-06 17:05
what would a diagram of an alert being sent to a usergroup look like?
create a simple functional spec for temporal navigation through a device's history


2021-12-10 15:08
IvedaPinpoint is a cloud-based platform for tracking IoT devices on interior and exterior maps. Querying the history and current status of connected devices provides ongoing telemetry as well as rich insights into how the network operates. For example, according to the American Hospital Association (AHA), in 2019 devices per hospital bed has increased to 15 and utilization of medical equipment averages only 42%. Often, mobile medical devices are not where caregivers need them. IvedaPinpoint can identify the location of these assets and alert the appropriate staff when equipment is removed from an area or taken out of the building.

IvedaPinpoint is an integrated service within the Iveda CEREBRO technology stack. A compatible video surveillance system, for example, can share camera devices as Map Resources. 

Iveda Sentir Digital Transformation Solutions



2021-12-12 16:48
continuing to work on the Design doc in Notion

PINPOINT is an integrated service within the Iveda CEREBRO framework. A compatible video surveillance system, for example, can share camera devices as Map Resources. 


2021-12-12 17:40
In this strategy, the developer focuses on the main content and functions first and then adds extra capabilities if the browser and platform offer more frills around the edges. Related to progressive enhancement is responsive web design, in which content is designed to resize for specific platforms, such as mobile or desktop devices.


2021-12-12 23:02
The technology can be used to find people and items inside buildings, find directions, and more. The technology is cost-effective, easy to deploy, and requires minimal effort.


2021-12-13 09:34
Cluster list content by relevant criteria. Some of these groupings can provide greater insights into the items listed in the feed.



By owner
In motion
Near me
Recently viewed
By Room/Floor/Building
By Type
By Urgency
By Connectivity
New


2021-12-14 01:26
This system helps clients monitor resources they’re responsible for. Whenever some Pinpoint resource changes state, users and groups assigned to it are notified. 

# Ranking Notification by urgency
Pinpoint resources broadcast a notification upon any change of state. Pinpoint itself may send notifications of varying severity.

Low         Status Update (Resource)
            Status Update (Pinpoint)
Medium      Acknowledgement
            Warning
High        Alert
            Confirmation
            Error
Critical    System Failure

# Who receives Notifications?
An Alert is a high or critical urgency condition users assigned to a resource need to know about. Alert conditions are defined per each resource.


2021-12-14 09:57
Greg/Gary meeting
afterwards - add this meeting to JIRA
            - share 
            
Talking through my problem state
Greg mentions it will useful to tag a moment in time for easy r

David Moon will be setting up our private JIRA, CONFLUENCE, ETC
reach out to him to speak about project management tools, such as:
Notion
Figma

Room Inventory
when you see a room inventory you can see an indication of when there's a change. It points out things that

Can we apply histograms to the

In the example provided by the Glasswire scale, label the 

Reach out to some contacts and see if we can get

Sid is presenting material for CEREBRO 1.0 - this is the old approach to the technology

our material is called CEREBRO 2.0 - this is the approach Greg & I have been concepting. It turns out that what we are building is a tool for organizations to build collaborative policies around the management and tracking IoT resources within geofenced boundaries. 



2021-12-15 12:37
invited Calvin to the Notion and Figma workspaces
I'm spending the next 1h cleaning up the Figma project


2021-12-16 12:23
Iveda seems to have spun up a new working group, or some sort of organizational structuring in Mesa. They moved to a different (better?) office. The previous one was next to a firearms dealership, which may not be unusual in Arizona I guess. But they also changed to different bank accunts, and sent me a physical check number 002 from this new account, signed by David Ly. BoA will place a hold on the deposit until the funds are "verified" and that will happen on 12/23. Sooner perhaps.


2021-12-16 12:27
Calvin provided me w an iveda.com email and I'm re-inviting him to Figma and Notion




2021-12-16 18:25
Calvin is having some trouble accessing Figma. Seems to be email related? Perhaps some kind of firewall policy at iveda.com?


2021-12-17 14:26
Calvin was able to login to the Figma project with the public linjk I sent. obviously non-optimal. I suggested that he try creating a Figma account under his iveda.com mail. No response yet. Even so, why should this even be an issue at all. Sort of a drag that this isn't seamless. My hope is to have iveda run Notion & Figma on their corporate account.


2021-12-17 14:28
WHAT ARE YOU DOING RIGHT NOW?
I'm working on the Visualization section. I was copy/pasting the editorial text, but maybe better to get the chart gfx in there

A few basic charts are described here for common use cases. Incorporating a charting library such as chart.js provides a bridge between the data and the visualization



2021-12-17 22:16
looks like we're having a braindump meeting on Monday. New member of the team David Moon. I've sent out invitations and links to the Notion and Figma projects


2021-12-18 16:02
One of the Iveda VP's, Sid Sung will be joining us for the brainstorming meeting on Moday. Its in the evening at 5p

In the next hour, I want to
- clean up Resources Section
- add content to Mapping section from Powerpoint
x add Table chart example to Reporting section
- duplicate sitemap (handheld) as sitemap(desktop)

Beyond the Infinite Two Minutes
Nightmare Alley
Titane 

2021-12-23 10:31
meeting w David

missing docs - finalize

he is Sid's contact
he has worked w Calvin before

having a fun chat

talking about what Sid neeeds to see
I want him to be a creative partner

Sid needs to be able to touch things

Several actions are going on in parallel
- Conceptual/Design
- backend

I feel like there is also a third (unspoken) action
- working build

Maybe more than several actions actually.
Consider making a mind map to organize your thoughts about what needs to happen next, and how you can provide inputs


2021-12-23 15:55
My takeaway from meeting w David earlier is that I need to get faster ad producing my outputs. The main thuing slowing me down at the moment is constant restructuring of the docs for presentation. They look great as a result, but its a good time to shift focus to document completion


2021-12-31 11:20
I spent time yesterday further organizing the Iveda notions space, but we're going to be sticking with Confluence, as this is already univerrally available to everyone. That's cool. the work done yesterday wasn't for nothing, but I guess it was efferrctively a practice session.

Still, with the level of structure I have going now, I think it may be relatively straightforward to export or manually copy/paste intgo confluence

 

2021-12-31 11:22
Ah, I'd forgotten I'd initially begun the design guide here in Iveda COnfluence. There's already a structure I can build from



2022-01-23 16:06
I'm working on a presentation tomorrow to GREG and SID
The intention of this is to show progress since the last time.
What does that include?


2022-01-23 17:36

FIGMA
- desktop sitemaps correspond 1:1 w current handheld sitemaps
- Rule Construction in the Resource Inspection Panel
- Device Configuration
    + enables bulk Rule Construction
- Rewind Time
    + show UI for time display/state (live vs. historical) on HUD
    + show ranged selection for days/months/years

CONFLUENCE
- add simplified Rules Chart to Alert Policies Page


2022-01-24 03:00
I spent this worksession in Confluence and made some good progress there. There are still a number of holes in the documentation that I've identified in the documentation.

Tomorrow's work session will focus on
- creating desktop sitemaps from existing handheld work
- show UI for time display/state (live vs. historical) on HUD


2022-01-24 12:36
having trouble with restoring the project file from version history due to dumb mistake earlier

2022-01-24 16:37
review cancelled due to scheduling conflict. focusing my efforts on announcing my status, etc. on Slack.


2022-01-26 10:32
I've added proper metrics and som emockup device frames for presentational purposes. I've added browser chrome layer to the desktop templates

Desktop Sitemap build
- application themes
- browser viewport
- application views (relevant?)
- Inventory
- Search
- Device Inspectors
    + Tracker Inspector
- Notifications

Temporal Navigation 1
- design a component with a time counter which can show:
    + current time (live)
    + yesterday
    + last week
    + range
        * week
        * month
        * year


Finalize Device Inspectors
- Tracker [in-progress]
- Base Station Inspector
- Temp Pad Inspector
- Sensor (what kind? include?)
- GPS Inspector
  There are some UX matters around this, for example what happens when a person goes inside? Let's just assume that the map updates itself appropriately. Don't worry about he details now. What's needed is simply the panel layout
- Camera
- Usergroup
- User
- Room
- Floorplan
- Facility


2022-01-27 03:13
Jesus, I can't believe this has taken so long to truly understand the grid system in the UI Kit, and for dekstop layout in general. Finally there.



2022-01-31 12:50
I'm working on building Inventiory Slot and list components for desktop sitemap
I'm continuing to audit my design work and capture that status so I can see how much more is ahead of me and be tactical about this.


2022-02-04 14:58
finished itemizng working list of content for the sitemapping work ahead. I've reduced it initially, and feel its likely to be further condensed. The challenge is now to translate work over to a form that works for a desktop design

I'd suggest not frettng too much about responsiveness at this time. Just design for a single fullscreen profile. Youve got this. 


2022-02-23 16:03
project has wrapped
I'd like to do a post mortem of my work on this. There were some wins. Great ones. And also some losses.

David Moon reached out to me with some confusion about the Figma project I'd shared w Iveda. I said I'd make sure he got that. So I then spent tome adding detail and doing cleanup of the material. Before reaching back out to him I want to:
- ensure that the desktop sitemap frames match the ones in the handheld use case
- build out a skeleton UI which should include
    + Placement for global nav & search
    + Inventory List
    + Inventory Slots
    + Device Inspector
    + Notification list
    
ETA 3h

WHAT ARE YOU DOING RIGHT NOW?
cleanup & simplification of handheld sitemap

THEN?
build frames for desktop sitemap (empty frames are fine)


2022-02-24 01:21
I've built out the handheld Login section entirely from Untitled UI. To go further would require some minor editorial and logo gfx replacement


2022-02-24 17:26
I sent email to David Moon at Iveda pointing him to the archive project I'm cleaning up and finalizing better. Have not yet received payment for my last invoice. I will bring this up in an email tomorrow am. Still - I want to feel like I'm covered in terems of my deliverable, so I'm continuing to iterate on this work



2022-02-24 18:25
Added Sorting use case to Inventory block.


2022-02-25 14:25
rebuilding card component to generalize some cases encountered w Sorting
I'm still waiting for payment on the invoice I sent out a week ago.

NEXT
Contact Luz,Greg


2022-02-25 16:39
replied to Greg & Luz from the invoice approval mail sent to me on 2/16


2022-02-25 18:09
Greg replied back to me will look into it on Monday