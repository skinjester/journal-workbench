# ✎ 2024-08-11 05:14
Not sure how it happened, but the drive letters on the [[ONYX]] filesystsem have changed, and my Users/Gary branch is on a 4TB HD instead of a 2TB SSD as I'd thought. I had been noticing a vague sggishneszs but assumed it was my imagination since nothing had changed. Now it seems something has

- [x] #todo mirror HD-4TB (D:) Users/Gary to NVME-SSD-2TB (F:) 📅 2024-08-11 ✅ 2024-08-11
- [x] #todo relocate Win11 desktop folders to NVME-SSD-2TB (F:) 📅 2024-08-11 ✅ 2024-08-13

### 2023-01-11 12:51
2021-02-21 11:14
Setting up Synology to backup to Backblaze B2 bucket
I've successfully backed up the NAS using CloudSync, but I want to compare this operation to HyperBackup, which is a more standard incremental backup solution. The only drawback being that you must also use HyperBackup to recover data (or so I understand)


2021-02-21 11:22
I've successfully SSH'd into the NAS and have a BASH prompt
I am able to view the filesystem, as well as my stored files


2021-02-21 11:35
I've manually stopped the Synology Drive Server and Universal Search services.
Not sure what the long term inpact of this is, but drive/volume utilization have dropped t0-1% which is what I expected, as its not clear why there was processing going on there at all.

Cautiously optimistic.
Can I still access the NAS from this machine? YES
In fact access to the filesystm is MUCH faster, more in line with what I'd expected

Can I still sync this machine to the NAS?
Starting Backup to ARCHIVE sync operation now on ONYX


2021-02-21 14:33
need to generate a new master application key because I didn't make note of the old one?

Success! Your new application key has been created.
keyID: e443354c1db9
keyName: Master Application Key
applicationKey: 000b7e148d9f73a0a5060a38e22f09e6b01a21b4eb

keyID: 000e443354c1db90000000004
keyName: hyperbackup
applicationKey: K000HlEbFvdtYIKm7szXp1++Rg+RyIQ


2021-02-21 15:06
started backup operation for the entire drive


2021-02-21 16:22
at average rate of 30GB/h, the initial backup of the NAS (1.96TB used) will take 2.7 days. As I understand it, subsequent backup are differential block level (rather than file level) backsups and can be expected to run at a more practical rate

recovering the data should take as long as the initial write. As I understand it, this must be done through Hyperbackup (?) Backblaze offers a dervice to send a hard drive with the data on it (?)


2021-02-24 10:35
I successfully lubed and replaced the stabilizers on the Mode80. It sounds and feels fantastic. Everything went well and I'd tried out a different set of keycaps. Again, every thing was fine. Then I changed out the keycaps again, and all of a sidden I'm getting spurious behavior from the keyboard.

At first, it seemed to be completely disabled. Bry prfessing L-SHIFY/R-SHIFT/CTRL at the same time - that did... something, and the keyboard seemed to be providing input. But it was acting strangely. Tracing the problem down further. Its an issue with the left CTRL key. It behaves like its beingheld down. Sometime as if its being toiggled. Things can be done, and it can seem like its working, then all of a sudden will stop.

Monitoring the inputs using Windows On-Screen Keyboard and Via, I see the left CTRL key "flickering" between on and off, or sometimes just not working at all. I haven't fully tested it, but doubtthat its an issue specifc to ONYX-WIN10

Other keyboards don't exhibit this behavior. I'm using the Alt at the moment

NEXT
- observe behavior on LOCUTUS-WIN10
- observe behavior on ONYX-WIN10

research
- MODE Dischord server
    + if my issue isn't found, post a question describing the problem

- uninstall keyboard driver, shut down and power cycle ONYX before rebooting
    + plug in the ALT for input to get past bootloader, then unplug 

Have i inadvertently entered some sort of hardware state on the PCB itself, perhaps by inadvertently holding down dome keys while swapping out keycaps?
- what does hardware reset from PCB on keyboard do?
- what does QMK reset do?

Open up the keyboard
- visually inspect PCB at position of left CTRL key. ANything?
- test the switch contacts on the board using VIA to register inputs. Is there a signal?

I ordered a replacement PCB. Fortunately pretty inexpensive. If nothing above works, will replace the hardware.


2021-02-24 11:51
reading through the MODE dischord server, a couple of people report the same issue. In at least one case, the issue was a screw near that particular switch touching the circuit board. 


2021-02-24 11:52
The hyperbackup process continues to ru n. It's at 77% with about 800GB left to go. I expect this to be completed by Sunday. As I understand it, this initial backup is the initial hurdle. Subsequent backups will be incremental at the block level.


2021-02-24 14:11
I believe I found the promblem with the Mode80. There is a screw slot tightly placed on the PCB between the CTRL key and another. It looks like screwing it in all the way was causing intermittent contact between surfaces. I just tested the disassembled gear and everything seems fine :)

The ALT keyboard has been a good backup for this, and I still like the way it looks wouild be a great idea to replace the stabilizers. Perhaps later today or this weekend. I am also curious about packing strips of foam inside to reduce the resonance a bit. There's a noticeably hollow sound that I think can be made better!


2021-02-24 14:59
I've used VIA to setup an initial keymap for the MODE80
FN + 1: opens file manager to view This PC
FN + 2: opens Windows Mail
FN + 3: opens Edge Browser
SCROLL LOCK: Previous Track
PAUSE BREAK: Next Track
PRINT: Play/Stop 
R-CTRL: Print Screen (captures fullscreen to clipboard)


### 2021-02-25 13:23

NAS backup operation completed.
I did a quick test of doing another (incremental) backup afterwards, which only took a few minutes to cmplete. I also completed the CloudSync operation I'd paused, which also took only a few minutes.

The Sync and the Backup operation use 2 different Backblaze B2 buckets. I need to think about the relative merits and extended use cases around how each of these work. 


2021-02-25 14:00
running into a repeated issue, with minimum consequence for my current situation, but potential confusin overall. Where do these project journals exist?
- If they exist where you'd expect, along with the project, then there can be multiple unique journals on each machine, only one of which will be the last one synced to the NAS after daily archival operations. Entries on other machines won't get archived, but even - worse - the older version might end p on the NAS as the result of a later sync, where it happened to be the last version written.

- that means the journal files shouldn't exist on local machines, but on a network share. That material won't get backed up by a local machine, but will get backed up when the NAS gets backed up.
    + What bothers me is that there are only 2 copies of the material - locally on the NAS filesystem, and in the cloud backup
- still, i think this method of working with project journaling from the NAS and excluding the journal text files from any local machine is the best option here.


2021-07-09 13:51
Out of nowhere, some network connectivity issues with MULE
It had been a non-issue previously
2021-07-09 13:49
OPS-54  investigate ethernet connectivity issues on MULE
I've stepped through numerous oprtions on this matter. Still not resolved. 
It just stopped working all of a sudden.
- check the network cable
- reinstall windows


2021-07-09 16:44
resolved the issue. Problem with network cable. Purchase new 6ft cable


2021-07-09 16:49
took a look at
OPS-52 add network sharing protocols to MULE
Although I can see the shared machines, I'm running into authentication issues
I shouldn't have to enter the credentials of an existing user on that machine, which is where I'm running into trouble. Reviewing a video about the subject
https://www.youtube.com/watch?v=3-C3v82zOgE&ab_channel=Windows11%26Windows10Guru


2021-07-09 17:13

N:ARCHIVE
X:LOCUTUS
Y:ONYX
Z:MULE


2021-07-09 17:21
some success in this newer approach from the video. Apparently you have to share with:

I added "Everyone" and provided read/write access. In some case that was all I needed to do. Connected with LOCUTUS easily
However not able to connect with ONYX without being challenged for authentication. That's not supposed to happen, right?

I'll pick this up later. Its like a detective story


2021-08-02 15:31

ARCHIVE
static IP:      192.168.0.132 (maps to Synology static IP)
subnet mask:    255.255.255.0
gateway:        192.168.0.1

Dynamic IP hostname: exoholo.ddns.net (via no.ip.com)
username: gboodhoo@gmail.com
password: 7aTXONm4rIij



2021-08-06 16:59
Lets try this again.
Watching a youtube video on the subject


2021-08-06 18:58
Getting nowhere. But this:

After you have registered a domain name with No-IP, it will take 24-72 hours for your domain name to propagate to all of the root DNS servers. Your domain may show up in the WHOIS database before it has fully propogated to the root DNS servers.


2021-08-07 16:52
working through detailed tutorial found on r/synology
https://www.wundertech.net/synology-nas-initial-setup-ultimate-guide/#41_Accessing_your_Synology_NAS_Outside_of_your_Local_Network

Upgraded DSM on the NAS to v7.0


2021-09-03 20:03
I've finally mounted a BRIO webcam on the railing behind my monitor. Its cool. I'd forgotten how good the image quality was! The little ball head I picked up mounts fine, but turns out I need something with a bit more length. The camera needs to be "floating" above and maybe even a little in front of the monitor. Some kind of tripod mount that allows for extension of the image plane. I have it plugged into the monitor with one of those weird LED cables, but I'm getting a complaint from the Logitech camera app when I try to switch between sources. There isn't enough USB bandwidth available to run both at the same time. Takes about 10 seconds to switch between them and they can't be viewed together.


2021-09-13 16:49
These days, I'm logging into Windows using Windows Hello authentication on the BRIO



2021-09-14 13:10
Finally playing around with the tripod accessories mounted to the back on my monitor. Definitely oddd looking, and maybe more appropriate for lighting than the camera? I think The Hue Play lights can be mounted using the same rig?


2021-09-28 14:46
Not so happy with where the tripod for webcam is mounted. Its awkward. I haven't setup the Hue lights properly. I guess I'm expecting for there to be a new display there, and I don't want to make any commitments yet? 


2021-10-08 01:38
purchased new monitor [[Dell U4021QW]]
Expected arrival is 10/18. Exciting news. Its been a long time coming. All things considered this isnt the optimal solution, but this seems to be where the market is at right now. Additional DisplayPort inputs, or HDMI 2.1 inputs would be great, as it runs at 30Hz over HDMI. Even so, I'm looking forward to its arrival 


2021-11-21 11:26
Several new Hue lights have arrived
2x Hue Play with white casing replace the ones on the back of my monitor
1x Hue Gradient Light Strip. Its beautiful. I intend to purchase more
4x A19 1100 Lumen bulbs. Replaces the 2 in Floor Lamp and the 2 in Utility Room


2021-11-21 11:35
I've lived w this new monitor a few weeks now and it still surprises me how beautiful it is. I love how much picture there is. I'm dragging my feet on the desk replacement though. For one thing, after flipping it over and tightening the screws in the l;egs, I'm no longer havingb the same stability problems with it. What's the holdup otherwise though? 


2022-04-14 09:38
Purchased Melgeek Mojo68 keyboard as a birthday gift. I'll replace the switches and lube the stabilizers when it arrives. My first purchase through aliexpress. 


2022-04-22 18:44
I've added 1x 12TB drive to the NAS. Apparently will take several hours for the filesystem to "repair" itself. Once that happens, I'll add the 2nd 12TB drive


2022-04-22 18:46
As long as I'm working with drives, how about upgrading the storage on ONYX. Wondering if I will need to replace the existing 4TB drive, or can I simply add the new drive?


2022-04-23 15:49
I've added the 2nd 12TB drive to the NAS and am now rebuilding the storage pool. Will take several hours to finish.


2022-04-23 15:55
I exported the Confluence docs from the deepdreamvisionquest confluence space and imported successfully to the garyboodhooworld confluence space. I have switched the deepdreamvisionquest space to a free membership, so no reason to delete. I've also switched the garyboodhooworld confluence & Jira spaces to the free membership tier


2022-04-23 16:03
Once the NAS filesystem is healthy again, I'll need to increase the volume size to fit the max capacity of the drives.


2022-04-29 01:34
NAS upgrade complete
Added additional HD to ONYX


2022-05-29 19:43
[[Project HOLODECK]]  is now [[Project Ansible]]
After sourcing and learning about rackmounting, I purchased and assembled a handsome 12U rack to relcoate all the gear to.
I'm collating a list of accessories, such as shelves, and cables to accomodate the new work area
I've purchased the SVS SoundPath Triband Wireless Audio transmitter and 2 receivers so that I can decouple the subwoofer positioning fom the AV center.
I'm interested in how the miniDSP soluition + REW xcan workl in this configuration. Same as before?


2022-06-05 15:20
For a while now, we've not had the internet bandwidth I expected, and previously observed. The AT&T Fiber 1000 (all fiber plans) are supposed to offer symmetrical upload a& download.

Previously, I was getting a great download speed - 940Mbps or higher. but very "low" upload speeds of 120Mbps or so. Wifi speed seems unaffected? I never really tested that actually. After doing some tinkering/educated guessing on the AT&T gateway, I am seeing an increase in UL speed. Its significantly higher now at 488 MBps.

I didn't do much 
I disabled IPV6 LAN features (I don't think I was using them at all?)
I turned off packet analysis and security features

The increased rate is significant, although I definitely remeber it being higher than before. What's really bothering me however is that the data rate measures as symmetrical when speed testing at the gateway instead of the router.

Is my router too slow?
I doubt it.

Is there a connected device that's omehow slowing things down?
I doubt it. Maybe?

Is there some setting that is causing a slowdown at the router? at the network card?


2022-09-03 19:19
I've replaced the stabilizers on the Mode 80. Impressed all over again by the design of the thing. I'd forgotten it came with a case as well! In which I found, an additional PCB, additional A and B foam inserts and an additional (aluminum) plate. Almost enough to make an entirely new board. The TX Stabilizers I installed sound good. At least as good as the previous screw-in stabs did, and I think, maybe better? More consistent? I'm going to try the same on the Mode80 board later. I also installed the Hades switches, which are a bit unique. I haven't typed much so hard to say, but definitely more character to the acoustic signature. There's an interesting feel to the springs inside. "snappy" and crisp is the overall feeling. I installed the DCX profile WOB keycaps and must admit the deep blublack of tghe case. the profile, the colorway look and sound quite amazing


2022-09-04 13:43
Received new stablilizers for Drop Alt board and am in the process of rebuilding that


2022-09-06 15:50
I replaced the stabilizers on the Alt, tried out a couple of different switches but kept the lubed/filmed Linear Alpacas that were already installed. Swapped out keycaps to GodSpeed, looks anazing

I changed the keycaps on the Mojo68. Replaced Honey & Milk XDA set with dark & light keysterine caps onh alkphas and modifiers respectively. I may have displaced or dameged the LEDs though, as they are only displayintg on half the board

I've set this board up to be used at a distance from the computer, perhaps from the couch, using the TV as a huge monitor

###### 2023-01-03 11:01 ######

[[Project Ansible]]

- Hardwire [[ONYX]] USB-C/USB-C to [[iConnectivity AUDIO4C]] input 1
- Hardwire [[WORKSTATION2]] USB Hub USB-B/USB-A to [[iConnectivity AUDIO4C]] Host input
- Hardwire DIN MIDI-In from [[iConnectivity AUDIO4C]] DIN MIDI-IN to [[Casio MG510]] MIDI-OUT. When not in use this will be a loose cable that can be coiled on the side of the rack
- Move USB-C keystones to the far right of the patchbay so there's less cable travel from [[WORKSTATION2]] to [[WORKSTATION1]]

I'll take delivery of a [[DI Box]] and a [[MIDI Interface]] later this week. The [[KORG Minilogue XD]] will run MIDI to the USB Hub. The [[Casio MG510]] will run analog signal to the [[DI Box]] which will then plugged directly to the patch bay. 


18:05

Experimenting with MIDI routing. Not always sure why the signal comes from where it does. I feel there are more outputs than inputs. Still looking for a great MIDI utility. Does [[Ableton Live]] have this capability. It looked to me that the DIN to USB MIDI Adapter is working. 

###### ⏱️2023-04-25 10:02

New gear arriving this week: [[MOTU Monitor 8]], [[Behringer UMC1820]], [[Headrush FRFR108]]

I'm relocating the equipment rack to zone2 where the i/o can be consolidated. Lots of questions about making it work as a system, or systems. Not sure how MIDI i/o is to be accomplished. 

###### ⏱️2023-04-25 01:06

Possibilities for integrating MIDI into the system

- Bluetooth MIDI
- rtpMIDI
- MIDI interface
	- Process/Filter/Route MIDI data 
	- connect my USB/Power hub to the host port. This routes USB MIDI (from up to 8 devices attached to the hub) to the interface 
	- My [[Casio MG510]] can be connected by existing DIN cable to MIDI in
	- An iPad connected to the [[iConnectivity AUDIO4C]] interface is integrated with the MIDI network
		- use AUM as front end
			- Send MIDI (hardwired) 
			- Receive MIDI
			- Process/Filter/Route data
		- iPad could broadcast Bluetooth MIDI for wireless I/O to other devices - another iPad, for example 
		- iPad could broadcast network MIDI


###### ⏱️2023-04-25 01:26

Im seeing that the [[Behringer UMC1820]] has MIDI in/out so the connected iPad will be available over its USB connection. To integrate, I can use a DIN to USB cable  connected to the USB/Power Hub

MIDI from [[ONYX]] can be integrated by a USB connection to the Audio4C, or possibly even by connection to the USB/power hub. Treat it as another MIDI device. 

If so, that would free up the 2nd device port on the 4C and i could connect another usb audio device. 

###### ⏱️2023-04-28 11:18

new gear has arrived

inventory list for studio reconfig

1/4 TRS cables from [[Line 6 Pod Go]] main outputs to [[Headrush FRFR108]]  w 90 degree angled connectors  (2)

1/4 TRS to XLR male from [[MOTU Monitor 8]] to patchbay (2)

###### ⏱️2023-05-03 12:37

After some consideration I've purchased the [[MioXM MIDI interface]] MIDI interface, specificallly for the [[What is RTP-MIDI|RTP-MIDI]] features

###### ⏱️2023-05-03 07:06

I've purchased an 8U rack on wheels for Zone2 along with a 7in 1U shelf and cable routing for the back. Do I still have those PDU's? Or will i need another?

###### ⏱️2023-05-17 11:45

I've more or less finished moving stuff around during studio upgrade, but I haven't verified everything working yet. I'm wondering how to normalize/standardize the external inputs to the back of the cabinet. I just want all the cables entering the cabinet in the same place. I keep wondering about repurposing the 2nd patchbacy to the back for this purpose actually, where it could function as an input matrix and route signal to the front patch bay.

###### ⏱️2023-05-18 03:46

setting up [[MioXM MIDI interface]] RTP-MIDI connectivity

KorgXD

⏱️ | 2023-08-30 12:20

The end of a MacBook

This has been a great machine. I purchased it in 2016 upon returning to San Francisco from Baltimore, figuring I'd need it for traveling, interviewing, public speaking. All of that happened. The keyboard stopped wsorking and I don't feel like I can justify the investigation into the problem. A diagnostic says there's something wrong with the power supply.

- trade this machine in for gift card
	- directly at apple store?
	- online?
	- when would gift card be available for usage?

- find a new machine


2020 Apple MacBook Air M1 13-inch 8GB RAM 512GB SSD Space Gray 
$999 | $83.25/mo (12mo)
$884 | $73.66/mo (12mo) after trade-in received


⏱️ | 2023-08-30 05:01

I purchased a new MacBook


	
MacBook Air M1 13" (Space Gray)

**Apple Card Monthly Installments**
12 monthly payments, 0% APR, $73.66/mo.

**With the following configuration:**
Apple M1 chip with 8‑core CPU, 7‑core GPU, 16‑core Neural Engine
8GB unified memory
256GB SSD storage
13-inch Retina display with True Tone
Two Thunderbolt / USB 4 ports
30W USB-C Power Adapter
Backlit Magic Keyboard with Touch ID - US English
Force Touch trackpad
Accessory Kit

**Apple Trade In**
Trade-in value: $115.00
Your trade-in device:
MacBook Pro i5 2.7GHz 13" (Early 2015) 256GB SSD

Wouldn't you know it, the keyboard on my macbook started working again, as soon as I'd placed the order. But sporadically.

✎ 2024-01-13 01:46

After a storage limit "scare" I realized that my storage needs have changed. There are two areas for further growth:

- [x] #todo #ops Reintegrate NAS drive 🛫 2024-01-13 ✅ 2024-02-09
- [x] #todo #ops upgrade [[ONYX]] system drive 🛫 2024-01-13 ✅ 2024-02-09

$149 / Samsung 970 EVO Plus SSD 2TB NVMe M.2
This is the same drive in use as D:

$209 / Crucial P3 4TB PCIe Gen3 3D NAND NVMe M.2 SSD,

✎ 2024-02-08 07:43

I've finished setup of [[MULE]] as a video workstation. It's using the [[LG C7 OLED Display]] as a primary monitor, w wireless keyboard and mouse. It's running Remote Desktop which I've also setup on my [[MacBook]] and Thea's

✎ 2024-02-08 07:46

I've finished bringing the [[Synology DS220j|NAS]] back online. I verified that it's running daily backup to my Backblaze account. I updated all the required packages and so forth. 

Still need to re-establish backup routine w sync back on both [[MULE]] and [[ONYX]]





