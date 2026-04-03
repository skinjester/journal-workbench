2016-01-19 00:11:32
studying the deep dream code. have been doing so fairly seriously for the past few days.
reacquainting myself with the environment. understanding it better

net.blobs['data']  	# input image is stored (caffe format) in network's data blob2026-02-16

net.blobs[end]		# destination layer (end = layer name)
src					# input image (instance of net.blobs['data'])
src.data
src.data[:]
src.data[0]			# image data apparently stored here?
src.diff[0]			# back propagated error correction matrix (2D)
detail				# an image array created to draw network produced detail
octave_base			# the image contained in the octave currently computed
dst					# the neural layer identified as the end layer
dst.diff[:]			# assumed to be the 2D neural weights & structure of the end layer (?)
dst.data
octave_base			# the current image stage (octave) being dreamed upon



images in OpenCV are Numpy arrays

blob (binary large object) often used to multimedia data types such as images and audio

thinking about arrays more clearly:

for an array with shape (2,2,3): 	2 layers of (2,3) 				= 12 items
for an array with shape (2,3): 		2 layers of a list of 3 items 	= 6 items
for an array with shape (3):		a list of 3 items 				= 3 items

reshape method allows the number of dimensions and the size of each dimension to be changed as long as the total number of array elements remains the same



2016-01-25 22:20:07
what happens if you run rem.py right now?

2016-07-26 07:24:20
apparently I was self documenting here, but it never really took off. Picking it back up as I tyake a look at what the v1 project needs to be

2016-07-26 07:24:50
At the moment I'm going thru the code line by line cleaning up the formatting so the Linter program (Adaconbda/Sublime Text3) stops complaining. Busy work? Maybe - but is a good way to get a sense of what I had previously written

2016-07-26 07:44:04
Or maybe not - tedious. I'll make sure everything is clean

2016-07-27 07:41:33
Getting started mapping out the signal flowe of this program. Its more complex (and likely redundant) than I know how to move forward with

2016-09-06 21:33:30
I lost my way, thought I found it again, sort of did, athen lost it again. But I'm here now. I'm back.
Finishing the website turned out to be more than just taking some amateur video in my living room. It was nearly 2 months ago, right before going to nucl.ai conference. I had so much fun that night and that morning playing with the "AI"

Watching it in the living room (as a video) isn't compelling. I have an idea about doing a shoot with models or dancers and projecting the imagery. A sort of beta test as visual support for live performance. What would it take to make that happen. hire models? book a space?
A good intermediate ide ais to start showing the project off socially - because its easier to meet people when theyre aliens too

Another intermediate is to record output directly from the display. I think I'd done so with the microsoft game recorder previously?

Some new developments:
1. I spent time working with RPyC which allows for asynchronous callbacks that let one script communicate with another. My intention is to decouple the motion detection component from the game loop and run it as a seperate process. I'd played with Visual Studio to profile the code. Unsurprisingly, most of the time is spent processing the NN in Caffe. My expectation is that motion detection can be made to work more fluidly.

2. nVidia has newer faster GPU's. Significantly faster. I wonder how much speedup could be realized running on the new TitanX?

3. Studied Pythin basics a bit further. Everywhere I used a Class, I should have used a Module

4. Ive not been able to visualize the code to my satisfgaction. Partly because I dont know what I'm doing, partly because I haven't defined the problem clearly enough. What do you hope to gain from the desired output.

5. Rebranding. I like the name. But its a mouthful. I've noty come up with anything more compelling. When the project was named, my understanding was much vaguer. nonexistent really. What is my uderstanding now?

6. Need to do a site audit - tasks, priorities. There's a lot of work I can do right now.

2016-09-09 11:50:40
I really want to rename this thing. I dont know why, but cant let it go
Reading about Bestiaris.

"The bestiary, then, is also a reference to the symbolic language of animals"

2016-09-11 19:11:01
I'm submitting a proposal for CODAME Art & Tech Exhibition
ARTIFICIAL EXPERIENCES is the name of the exhibit
Proposal Due by Saturday 9/17
Artist notification by 9/21
Showing in SF 11/11


Description of Project *
A project description in 500 words (max) that includes any collaborative partners and relation to theme "Interface"

Links to high-resolution image(s) of your artist image and your proposed work
Estimated Materials Cost and Time
Artist Biography * A 100-200 word bio for publication in press materials (reference bios on CODAME site)
Artistic Resume including past works, exhibitions, commissions, videography (provide a list of videogames, etc)
Technical specifications
How large is the artwork, size on the wall or floor footprint (metric preferred)? Any technical requirements like wifi or power? How long does it take to set up and break down?



2016-09-15 14:16:04 DATA
Designed humane user interfaces for AAA videogames enjoyed by millions internationally.

Has worked on games including Madden NFL, The Sims, Star Wars: The Force Unleashed and The Elder Scrolls Online

Creative director

On the verge of a personal vision of collaborating with artificial inn telligene as a kind of robopsychiatrist. They;'re a better breed than us, but we made them so

Invisible interfaces

Designs for your thumbs

Grateful that humans don't behave rationally. It makes the job easier

good friend
loving husband
flawed human not hopeless

Became bored with that life and is a fine artisty afgain

living link betwee the 80's and the new era of machine hallucination


While still in art school I once wrote a dope  program that synchronized each of the 16 Apple IIe machines 

using their MIDI ports so that I could make all the computers in the lab blink at the same time. It was uncanny.

And adjusted the vertical timing of 


I lost my way, thought I found it again, sort of did, athen lost it again. But I'm here now. I'm back.


Experience an interactive psychedelic journey with a computer. Using the DeepDream convolutional neural network algorithm and real-time video feedback, the system turns your image into a vision of its own thought processes--a magic mirror. Questions about DeepDream, the magic mirror setup, and the spirit realm inside the machine are all welcome.

Takeaway
Attendees will leave with an understanding of how neural networks may be used for image synthesis, and specific steps for creating their own Deep Dreaming Magic Mirror.

Intended Audience
Anyone interested in interactive art experiences will be glad they came.

Finally! Someone speaking my language! The language of Spirit.
A language that cannot be used in the workplace. A language rarely acceptable in social gatherings (including most churches). Truth be told, the so-called "Spiritual Path" has led me to place of isolation. When I saw "Find Your Spirit Animal In A Deep Dream Vision Quest" - I quietly hoped I would meet someone that I could talk to. I sometimes yearn for belonging, but I refuse to shapeshift just to fit into someone else's tribe.

When I discovered it was YOU giving the presentation, I could not control my enthusiasm! I could not wait to see you again. I realize we cannot know who we are now from the slice of childhood we briefly shared. But the moment you started talking about "masks" - I could totally picture you and I having that conversation (I wanted to have it right there and then!). Your presentation was very exciting to me. And, if I may, let me say that you have a charismatic presence on stage. But I digress...

Simply stated, I would love to hang out with you. At the very least, we should get together and catch up on over 30 years. Let me share my contact details with you.

2016-09-15 15:29:51
Anyone or anything that has influenced the artist’s artworks.

Any education or training in the field of art

Any related experience in the field of art

A summary of the artist’s artistic philosophy

Any artistic insights or techniques that are employed by the artist

2016-09-15 15:29:48
The bio should summarize the artist’s practice—including medium(s), themes, techniques, and influences

mediums
photography
videogames
sound design
performance art

themes
the alien in the familiar, the familiar in the alien
the language of the spirit
Mythology and storytelling
Emptiness


2016-09-15 15:29:45
The bio should open with a first line that encapsulates, as far as possible, what is most significant about the artist and his or her work, rather than opening with biographical tidbits, such as where the artist went to school, grew up, etc. For example: John Chamberlain is best known for his twisting sculptures made from scrap metal and banged up, discarded automobile parts and other industrial detritus.



DESCRIPTION OF PROJECT
A project description in 500 words (max) that includes any collaborative partners and relation to theme "Interface"

Experience an interactive psychedelic journey within a computer interface. Using the DeepDream convolutional neural network algorithm and real-time video feedback, the system turns your image into a vision of its own thought processes--a magic mirror. Questions about DeepDream, the magic mirror setup, and the spirit realm inside the machine are all welcome. Attendees will leave with an understanding of how neural networks may be used for image synthesis

LINKS TO HIGH-RESOLUTION IMAGE(S) OF YOUR ARTIST IMAGE AND YOUR PROPOSED WORK
artist image:
[find a picture you like]

proposed work:
http://www.deepdreamvisionquest.com/

ESTIMATED MATERIALS COST AND TIME
N/A


ARTIST BIOGRAPHY
A 100-200 word bio for publication in press materials

Gary Boodhoo combines videogames, machine learning and interface design to discover ancient images — spirit animals. Born in Jamaica, relocation to the United States provided a crash course in how to construct mythology out of the 1980's. Then computers happened and then Dungeons and Dragons happened. Today he is an industry veteran. He designs and bleeds user interfaces for videogames including The Sims and The Elder Scrolls Online. His work examines the rhythms of emergent behavior in shared digital environments. He lives in San Francisco and develops humane experiences for game studios and other creative clients.


ARTISTIC RESUME
(including past works, exhibitions, commissions, videography (provide a list of videogames, etc)

The Ghost in the Machine Has Many Mansions, 2016
Part of a speaker series on technological rituals
Presented by the Society for Ritual Arts
http://societyforritualarts.com/join-us-on-1219-in-san-francisco-for-the-ghost-in-the-machine-has-many-mansions/

DeepDreamVisionQuest, 2016
presented for the Game Developers Conference 2016, San Francisco
http://schedule.gdconf.com/session/find-your-spirit-animal-in-a-deep-dream-vision-quest

The Elder Scrolls Online, 2015,
A massively multiplayer online roleplaying game
platform: PlayStation 4, XBox One, Windows, OSX
publisher: Bethesda Softworks
developer: Zenimax Online Studios

Zombie Apocalypse, 2009,
An apocalyptic multiplayer shoot-em-up
platforms: PlayStation 3, XBox 360
publisher: Konami
developer: Nihilistic Software

The Sims 3, 2009,
A life simulator game
platform:Windows, OSX
published and developed by Electronic Arts

Star Wars: The Force Unleashed, 2008,
An epic science fiction action-adventure game
platform: PlayStation 3, XBox 360
published and developed by LucasArts

Madden NFL, 2004,
A football simulation game
platform: PlayStation 2, XBox, Windows
published and developed by Electronic Arts



TECHNICAL SPECIFICATIONS
How large is the artwork, size on the wall or floor footprint (metric preferred)? Any technical requirements like wifi or power? How long does it take to set up and break down


DeepDreamVisionQuest space requirements are flexible. It can be run sitting in front of a computer with a webcam. The technology was designed to be used socially so there must tbe room to comfortably observe and participate. There are 3 working areas to consider. Previous exhibits worked best when these areas were in close proximity to one another, with room for the computer and operator off to the side.

1. Staging area for live video capture
-	3.5 square meters
-	Hardware
	-	lighting (2)
		-	prefer to use house lighting when possible
	-	webcam
	-	tripod
	-	chair

2. Display area
-	Requires line of sight to staging area so participants can interact with video imagery
-	Hardware
	-	Large TV or projector (depends on the space)
		-	prefer to use house systems when possible

3. Control area
-	Positioned less than 3m from Staging Area to accomodate cable runs
-	Hardware
	-	desktop computer
		-	USB input from camera
		-	HDMI output to display
	-	computer monitor
		-	need surface to place or mount monitor
	-	computer keyboard
		-	need surface to place or mount keyboard
	-	Game controller


HARDWARE BREAKDOWN
Lighting (2) [can venue provide ?]
Large TV or Projector [can venue provide?]
Table/Desk [can venue provide?]
Chair [can venue provide?]
Webcam
Tripod
Desktop computer
Computer monitor
Computer Keyboard
Game controller
30' USB cable
HDMI cable (length TBD pending venue details)

SETUP/TEARDOWMN
Setup/Teardown takes 30 minutes. I will need to do a technical rehearsal in the space before going live



2016-09-17 01:14:44
After all, the computer trained on pictures all humans understand. We train them by showing them many examples of what we want them to learn.

2016-10-04 10:23:00
The project has moved over to Linux for scalability and so forth. I'm using a new Titan X Pascal gfx card and needed to go through a chain of dependencies to work properly - which wasn't happening in Windows. I am seeing a bit of a speedup in basic dreaming, and have confidence that seperating motion detection into a different process will also help.

There's so much to think about - what do I really want to do with this? I need to assume there is no operator other than myself if necessary - would like to see more behaviors happening on their own - or possibly in response to inputs other than the game controller?
Would it be difficult to integrate MIDI?

2016-10-04 10:28:00
Why am I unable to change the size of the frame buffer?
Oh - ut was at the top of the script
Wow! Dreaming at 960 x 540 is extremely fast, but seems like motion detection gets broken?
Oh - its the threshold values (counting fewer pixels now)

2016-10-04 10:34:00
Its so much faster that I must rethink what's happening w the motion detection and transition between dreamed frames

2016-10-04 20:50:44
studying that code. What's the plan for Artificial Experience?

2016-10-08 10:21:25
doing some houisecleaning w the deepdreamvisionquest code. I think that everything that's currently a class, shoule be a module for easier maintainability and understanding wtf is going on

-	MotionDetector
-	Viewport
-	Framebuffer
-	Model
-	Amplifier

2016-10-08 13:32:45
modules are:
-	a python file w some functions and/or variabes in it
-	you import that filee into another
-	you access the functions or variables in that module using the dot (.) operator


2016-10-08 14:28:41
still reading up on modules and remembering how the code works
One observation is that the viewport sizing I;'m doing isn't consistent
The expectation is to be rendering and processing at 960 x 540 (a rem cycle lasts 4 secons)
and scaling that view to 1920 x 1080, but is seems like that's getting mixed up and maybe its only the camera images that are coming in at the lowere rez?

2016-10-08 14:54:32
maybe the uprez can be done by the OS itself - scaling the output x2?

2016-10-08 17:10:41
dont fixate on the interaction at this time - get the structure you want in place

2016-10-08 19:00:30
To get a list of the modules that have already been imported, you can look up sys.modules.keys()





2016-10-09 00:21:22
still refactoring the motion detection class
haven't yet converted it into a model
good improvements on responsiveness though - enough so that the idea of running it in a seperate process doesn't seem as high priority as before.
getting decent balance between speed and quality at 1280 x 720 w cycle time of 2 sec

2016-10-09 13:34:31
It isn't making sense converting from classes to modules - and for what? learning? pride? convenience?
Is a major pain in th ass to croll around this single rem.py. Would be so much easier to bve dealing with seperate files as functional chunks.
What am I not getting?
-	global state in a module isn't being retained in functions without messy and weird global declarations for each usage in a function.
	-	A class construct just handles this shit better

- Each of the modules is totally unique. Its not like they could ever run on their own or be plugged into some other code as-is

- all i need is the ability to maintain seperate namespaces


2016-10-09 15:41:01
I'm not sure how much effort to place into restructuring this code in a more manageble way. Its not unmanageable, but can't shake the feeling that its built on an unsteady foundation, hence the desire to look further

I'm taking another look at that camera capture demo (cameo) that I'd studfies a few monbths ago

program hub
	import SomeModule
	class ComputerProgram
		__init__(self,params)
			classvars
			instatiate SomeModule.class()
		run(self)
			SomeModule.class().function()
		functions(self)
	if __name__ == '__main__':
		ComputerProgram().run()

SomeModule
	class Module
		__init__(self,params)
			classvars
		functions(self)

2016-10-09 17:54:23
I've looked into structural optimization as far as I can for the moment
Its clear that there's a real issue (opportunity?) with these various bundles of state/behavior referencing one another globally

2016-10-09 23:19:56
pushed and committed recent work to git

2016-10-10 01:28:28
I've externalized the class definition of MotionDetector

2016-10-12 09:01:57
Trying to understand what this code is doing so I can modify it
Taking Cory's advice in following what the data is doing. Very difficult to think of these little machines as small bits of functionality.

------------------------------------------
How it works, a romance in simple language
------------------------------------------

#	CAMERAS are STORED in MOTIONDETECTOR
#	CAMERA is STORED in FRAMEBUFFER1

#	GAME LOOP
		Framebuffer.is_new_cycle = True
	#	SEND FRAMEBUFFER1 to VIEWPORT
	#	PROCESS the CAMERAS STORED in the MOTIONDETECTOR
		-	STORE HISTORY to prepare for new input
			-	self.wasMotionDetected is stored as HISTORY
			-	self.delta_count is stored as HISTORY
		-	the difference between CAMERAS IS STORED as self.t_delta_framebuffer
		-	the COUNT of non-zero pixels in self.t_delta_framebuffer IS STORED as self.delta_count

		#	OUTCOMES
			-	OVERFLOW: all delta_count(s) were above detection threshold
				-	self.delta_count == 0
			-	MOTION DETECTED
				-	delta_count > delta_trigger AND HISTORY < delta_trigger
					-	SET self.wasMotionDetected = TRUE
			-	MOTION ENDED
				-	delta_count < delta_trigger and HISTORY > delta_trigger
				-	SET self.wasMotionDetected = FALSE
			-	BENEATH THRESHOLD
				-	SET self.wasMotionDetected = FALSE

		#	REFRESH the images STORED in the MOTIONDETECTOR
			-	ADD new CAMERA to QUEUE
			-	REMOVE oldest CAMERA from QUEUE
	#	FRAMEBUFFER1 = DEEPDREAM(FRAMEBUFFER,etc.)
		-	NET
		-	ITERATION_MAX
		-	OCTAVES
		-	OCTAVE_SCALE
		-	STEP_SIZE
		-	MODEL.end

	#	DEEPDREAM
		#	SETUPOCTAVES
			#	Framebuffer.is_new_cycle = FALSE
			#	INITIALIZE the OCTAVEARRAY with NETBLOB
			#	INITIALIZE the DETAIL BUFFER to STORE network output
			-	we can provide new values for OCTAVE_SCALE, ITERATION_MAX during SETUPOCTAVES

		#	OCTAVEARRAY CYCLE
			#	ITERATE from small to large
				-	OCTAVE is index for OCTAVEARRAY
				-	OCTAVE_CURRENT is framebuffer for each OCTAVE
				-	RESAMPLE DETAIL to mat ch shape of OCTAVE_CURRENT
					-	DETAIL comes from SETUPOCTAVES or previous OCTAVEARRAY CYCLE
				-	RESIZE the NETBLOB
				-	ADD DETAILS + OCTAVE_CURRENT to NETBLOB

				#	OCTAVECYCLE
					-	WHILE STEPCOUNT < ITERATION_MAX
						-	PROCESS the CAMERAS STORED in the MOTIONDETECTOR
						-	WasMotionDetected ?
							-	BREAK out of OCTAVECYCLE

						#	MAKESTEP (model, OBJECTIVE, step parameters)
							-	parameters arrive here from initial deepdream function call
							-	makestep operates upon the neural net's data blob
							-	we can affect guide image and step size here (per iteration)
							-	NETFORWARD to OBJECTIVE
							-	NETBACKWARD
							-	APPLY gradient ascent step to NETBLOB
							#	POSTPROCESS NETBLOB
								-	dat gaussian blur
								-

						-	CONVERT NETBLOB to RGB and WRITE to FRAMEBUFFER1
						-	SEND FRAMEBUFFER1 to Viewport
						-	OCTAVE_CURRENT ++

				#	EARLYEXIT
					#	LASTOCTAVE
						-	OCTAVEARRAY CYCLE reached OCTAVE_CUTOFF
						-	SET Framebuffer.is_dreamy = TRUE
						-	CONVERT NETBLOB to RGB and STORE as EARLY_EXIT
						-	Return EARLY_EXIT

					#	MOTION WAS DETECTED
						-	SET Framebuffer.is_dreamy = FALSE
						-	CONVERT NETBLOB to RGB and WRITE to framebuffer2
						-	Return CAMERA

				#	WRAPUP OCTAVECYCLE
					-	STORE the DETAILS produced during OCTAVECYCLE
					-

			#	WRAPUP OCTAVEARRAYCYCLE
				-	SET Framebuffer.is_dreamy = TRUE
				-	CONVERT NETBLOB to RGB and STORE as FINISHED
				-	Return FINISHED


#	FRAMEBUFFER

------------------------------
What is the COMPOSER?
	NumPy array with shape (height,width,RGB)
	Always contains RGB image data
	Stores Game Loop SOURCES prior to display
		-	Deep Dream
		-	Motion Detector
		-	Overlays
			-	HUD
			-	Alerts
	Processes Game Loop SOURCES into OUTPUTS
		-	compositing
		-	resizing
	Flexibility
		-	SOURCES in the COMPOSER can be any size
			-	SOURCES in the COMPOSER are resized to the COMPOSITE W,H when composited
		-	OUTPUTS from the COMPOSER are resized to the VIEWPORT W,H

------------------------------
What is the VIEWPORT
	An OpenCV window we created to draw on the screen
	An Event Listener for external input
		-	listens for keyboard events every frame
	Flexibility
		-	window can be drawn at any size
		-	supports multiple windows
			-	all windows use the same event listener
		-	provides PREPROCESS inserts
			-	color transform
		-	provides POSTPROCESS inserts
			-	HUD overlay
			-	ALERT overlay



currently,
we almost always write directly to buffer1
-	camera image
	-	fetch camera before entering game loop
	-	return value from deepdream when motion detected during OCTAVECYCLE

-	computed image
	-	initialized with zeros at startup
	-	REM cycle
		-	deepdream return value after non-interrupted REM CYCLE
		-	running inceptionxform (on self) after non-interrupted REM CYCLE
	-	Interrupted REM cycle
			-	composited with buffer2 at beginning of new REM CYCLE if previous cycle was interrupted
	-	OCTAVE CYCLE
		-	neural output from each non-interrupted iteration of OCTAVECYCLE
		-	composited with buffer2 after interrupted OCTAVE CYCLE (is it?)


we sometimes write directly to buffer2
-	initialized with zeros at startup
-	motion was detected during the OCTAVECYCLE
	-	buffer2 stores the last hallucinated frame
	-	deepdream exits and returns camera
	-	buffer1 stores deepdream return value (camera)

2016-11-07 17:03:13
-	Tracking
	-	automate tracking thresholds
	-	trigger events based on "hot" areas of the screen
		-	screen edges?
		-	the cell of an n x n grid with the brightest value?

-	dynamics
	-	cleanup the "programs" currently in use to allow switching between them
	-	cleanup color processing on viewport
	-	add support for automated events

-	display
	-	keep a buffer of final output data (history buffer)
	-	playback history buffer
	-	composite / replace live with history
	-	global frame blending (as in after effects)
		-	 no longer special case new camera image acquisition
		-	 all frames are averaged together before display

-	HUD cleanup
	-	image export
	-	twitter post on demand (?)

AUTOMATE TRACKING THRESHOLDS
every time I set up a session, I have to double check the threshold and lower it or raise it so that motion is detected at a known degree of sensitivity.

if subjects are close to the camera, all the counted values increase

AUTOMATED EVENTS
-	different kind of transforms on REM cycle
	-	scale vertical vs. cale vertical + h, anchor left
	-	value of scale variable
		-	random?
		-	sequenced?
		-	cycle?
		-	related to number of pixels counted during motion detection?
	-	blur multiplier
	-	different feature maps on a given layer

BEST LAYERS
inception_4d_5x5_reduce

2016-11-07 18:06:56
theres a bug with the viewp[ort scaling - its scaling from upper left anchor instead of center anchor

2016-11-07 23:20:57
a more efficient way to resample the viewport?

2016-11-08 01:32:23
added feature map selector to make_step() wow...

2016-11-08 14:45:10
taking a second look at feature map rendering style
priority for this work session is to get tracking automated
better metrics on HUD
fix viewport scaling to work from center instead of top left edge

username
settings
threshold
last
now

2016-11-08 15:40:51
CREATE AN INVENTORY OF EFFECTS. BE ABLE TO SWITCH BETWEEN THEM

for what I'm looking at right now I want to specify:
-	Model
	-	Layer Index
	-	Feature Index
-	Deepdream basic parameters
	-	Iterations
	-	Octaves
	-	Octave cutoff
	-	Octave scale
	-	Step Size
	-	Step Size multiplier
-	Renderer
	-	Make_Step()
	-	Make_Step_Feature_Map()
	-	REM cycle flag (TRUE/FALSE)
		-	TRUE (current value, hallucinate until new camera input)
		-	FALSE (stop processing until new camera input)
-	Modifiers
	-	Feature Index incrementor
	-	Layer Index incrementor
	-	Octave Scale
	-	Pause Motion Detection
	-	REM Transform scale
	-	REM Transform center point

2016-11-08 22:47:32
about to start work on automated tracking. I think that collecting the last n samples of the delta_count then calculating a moving average from that to select the threshold i sthe right place to start

x check the full range of display resolutions available for camera

2. draw stats on screen as needed

3. represent delta count as % is the value the same independent of capture size ?

2016-11-09 02:45:47
I've made the motion detection threshold dynamic - the raw delta count values are placed in fifo queue with fixed length, the queue values are averaged with each step. the threshold value is set to that. Its effective

2016-11-09 03:09:32
working very well, cool feature - still needs a bit of refinement - but playing with some tweaks makes it easier to bias the averaged value. Having them values as history is also cool - the way to deal with closeups is to attenuate large value differences, which should stand out in the sampled delta counts

2016-11-09 10:14:51
if the detector history window width is 2 then its just averaging the last 2 values?

2016-11-09 10:26:52
camera dimensions
# max 2304 x 1536
# 1920 x 1080
# 1600 x 896
# 1280 x 720
# 960 x 720
# 864 x 480
# 800 x 600
# 640 x 480
# 352 x 288
# 320 x 240
# 320 x 180

2016-11-09 11:33:48
maybe there is another way to calculate moton detection?

2016-11-09 12:09:00
maybe. need to move on to other things though. the current method is an improvement

2016-11-09 12:58:45
lookimg so Dark when webcm contrast/exposure is made sorta noir

2016-11-09 15:26:49
Looking at creating "programs" that I can switch between

2016-11-09 16:21:43
how do I "switch" programs now?
Amplifier.set_package('ghost')

what if I could keybind that behavior and switch between?

what is a "program"?
what is the difference between program A and program B?

# 1
A: begins at inception_4d/5x5_reduce
B: begins at inception_5a/5x5_reduce

# 2
A: octave_scale = 1.8
B: octave_scale = 1.2

# 3
A:	uses make_step_featuremap
B:	uses make_step

# 4
A: static mode
B: REM mode

# 5
A: uses 'places' model
B: uses 'cars' model

# 6
A: starts at featuremap[1,2,3,4,5] index 0
B: starts at featuremap[5,10,15] index 2

2016-11-09 20:15:10
moved event listener out of Viewport class is now a global function

2016-11-09 20:24:21
passing the listener function to Viewport instance

2016-11-10 09:36:59
changing layers forces new cycle now, implementing same for featuremaps

2016-11-10 12:03:55
verifying feature map incrementor setup

2016-11-10 12:12:14
works. doing some cleanup before commiting

2016-11-10 15:45:02
modifying the program data definitions

2016-11-10 17:50:12
remaining
x	fix pause functionality
-	work out how to switch programs with program select
x	exporting stills
-	create programs and test

2016-11-10 19:12:55
fixed pause functionality - much less convoluted than previous implement

2016-11-10 21:19:50
assigning layers to those specified in a program's layer list

2016-11-10 23:17:59
pulling layer list from program definitions now

2016-11-10 23:35:53
pulling featuremap list from program definitions now

2016-11-11 08:18:26
Setup 1p at Hotel Zetta. Take the next hour to look at switching network models with progam

2016-11-11 09:32:07
autosaving fully composited frames at end of cycle. still need ability to save on demand

2016-11-11 09:50:37
forced refresh will save the return value from deepdream early exit - this will be a clean camera image. Saving on demand also implemented - this saves whatever is in the image buffer - scaled up to dimensions of viewport.
clean saves of high res material are guaranteed only when a cycle is completed - and that saving is automated

2016-11-11 09:53:05
-	work out how to switch programs with program select
-	create programs and test

2016-11-11 10:50:01
modifying program list data structure

2016-11-11 11:10:21
wtf did that code work the first time through :) :) :)

2016-11-11 11:21:08
adding some error handling to prevent crash when featuremap index goes out of range for a particular layer

2016-11-11 11:24:07
now isnt really the time for that... revisit iof possible

2016-11-11 11:30:46
fixed the problem at featuremap selection

2016-11-11 11:39:46
basic program selection working - need to flesh out further

2016-11-11 12:41:05
model parameters not updating when I switch programs - may need to abandon that idea for now

2016-11-11 12:47:43
simple fix. working now.
give yourself 30 calm minutes to find some cool settings
add more from the location

Turning up the silence in Sci-Fi city at @codame artificial experience show


2017-03-12 15:53:49
rethinking some ideas for the L.A.S.T Festival exhibit


2017-03-14 14:59:45
Its working again, but had to wipe everything. The program was behaving strangely on this new machine. Described above. Despite dreading it, I reinstalled Linux and then the deep learning dev environment. Refined the notes I've been keeping on this. Maybe some new advantages. OpenCV is now at v3.2. I compiled it with option to do linear algebra with Cuda library. It seems faster. but hard to say definitively


2017-03-14 15:43:07
GOALS
CODELOCK
HARDWARE
INSTALLATION
UNINSTALLATION


2017-03-18 17:13:39
I've sourced a mobile AV cart w some accessories and will be placing that order shortly.


2017-03-18 17:36:16
can i make it show only fully rendered frames?
well first of all, lets review how it works



2017-03-19 14:44:13
I have the camera transform working in a test project
probably
overthinking.
the goal:
rotate the camera input upon reading it

is this a matter of:
1. creating a wrapper function to extend cv2.VideoCapture.read()
2. decorating the existing function?

2017-03-19 15:06:02
motion detection runs in portrait now


2017-03-19 21:23:50
getting close. its a bit of a hack.


2017-03-19 21:33:03
hardcoded portrait orientation is working

NEXT STEPS
- study python function decorators
- cleanup camera orientation functionality
	- choose between portrait and landscape at launch
- examine frame export
	- what's it currently doing?
- investigate the functionality of a Memory class
	- stores rendered output in RAM as an array
	- playback rendered output to framebuffer
- guide images
- switch between 2 cameras
	- camera 1 faces faces the viewer and acts as a mirror
	- camera 2 is behind the screen and acts as a window


2017-03-21 21:34:43
I reimplemented the camera capture system as a threaded queue after a bit of sould searching. Not sure what I was expecting to see. Something? Nothing? Is the system behaving more smoothly now? I can't actually tell. Seems largely the same. How would I be able to tell?
Is there a way for me to profile the systems performance?
- avg. iteration time
- octaves/sec
- current calculation time
- last cycle time


2017-03-21 21:37:58
Is the motion capture not threaded enough? should all of that be happening on a seperate thread? what would be the benefit?
Instead, could it happen on a seperate process?
What if the deepdream computation was happening on a different thread instead, and the output was being queued so that
deepdream.read() would return the next frame in the queue? how woyuld this change the approach to frame buffering?


Python threading doesn't multiprocess - it just makes more efficient use of the CPU
What about the rpyc stuff I'd previously looked at?
The idea is that motion detection and deep dreaming happen in seperate processes
The expected benefit:
computation happens in queues and results fill up a bin
Asynchronous
- decouples display rate from computation rate
display pulls the next available frame from a bin and shows it
may be possible to compute upon bin1.read() + bin2.read()


2017-03-21 23:14:29
looking at rpyc
reading up on python multiprocessing, which offers similar API as Threading

The multiprocessing module comes with plenty of built-in options for building a parallel application. But the three most basic (and safest) are the Process, Queue and Lock classes.

PROCESS
The Process is an abstraction that sets up another (Python) process, provides it code to run and a way for the parent application to control execution.

from multiprocessing import Process

def say_hello(name='world'):
    print "Hello, %s" % name

p = Process(target=say_hello)
p.start()
p.join()

QUEUES

Queue objects are exactly what they sound like: a thread/process safe, FIFO data structure. They can store any Python object (though simple ones are best) and are extremely useful for sharing data between processes. Queues are especially useful when passed as a parameter to a Process' target function to enable the Process to consume (or return) data.

from multiprocessing import Queue

q = Queue()

q.put('Why hello there!')
q.put(['a', 1, {'b': 'c'}])

q.get() # Returns 'Why hello there!'
q.get() # Returns ['a', 1, {'b': 'c'}]
q.get() # waits for more data to pass through the queue

LOCKS

Like Queue objects, Locks are relatively straightforward. They allow your code to claim the lock, blocking other processes from executing similar code until the process has completed and release the lock.


2017-03-22 08:29:11
looking at the test application,significant speedups are possible, but how can I apply these ideas to deepdreamvisionquest?
QUEUES:
	next camera frame
	next deepdream render
	next displayed frame

* is it possible to retrieve data from the queue that has already been read? is it random access, or is it sequential by definition?

I'm assuming that queung this information lets me address it asynchronously. For example, show the deepdream rendered que once every second


2017-03-22 08:47:04
who are the workers?

the deepdream function
the capture function

the compose/viewport functio


2017-03-22 19:50:21
I came across some code samples showing a single threaded, multithreaded and multiprocess approach to structuring code. I'm becnhmarking those approaches to see what they do

range: 1,10000,1

SINGLE THREADED
runtime: 50.6829841137s
CPU load during run: 0.96
1 core is in 100% usage throughout

MULTITHREADED
runtime: 83.9671368599s
2.10
all cores are approx 19-30% in use
* note that this

MULTIPROCESSOR
runtime: 72.0738749504s
2.05
all cores are approx 30-40% in use
* note that this

these results are unexpected. taking out the print statements and remeasuring
ending some processes to get a cleaner benchmark

10000, 100000, 100

SINGLE THREADED
runtime: 86.0674118996s

MULTITHREADED (4 threads)
runtime: 89.8049190044s


MULTITHREADED (8 threads)
runtime: 96.2501211166s


MULTITHREADED (16 threads)
runtime: 106.664397955s


MULTIPROCESS (4 processes)
runtime: 88.1409959793s

MULTIPROCESS (12 processes)
runtime: 88.1409959793s


2017-03-22 21:11:22
No room to investigate this much further beyond tonight.My fundamental premise is the right one - decouple computation from display, but implementation is too expensive


2017-03-22 21:23:25
trying one more exercise - slightly different method



2017-03-23 00:47:04
pulled myself away from the optimization experiments and started looking at image processing.
there's a difference between using nd.filters and cv2.filters
getting significantly wider blur fx with some new methods


2017-03-23 00:52:21
ending worksession - frustrating and rewarding at once. there's so much I dont know


2017-03-23 19:01:48
doing some remedial work on numpy before starting this image processing worksession


2017-03-23 21:17:43
wrapped up the remedial work. took a closer look at numpy arrays and matplotlib


2017-03-23 21:18:32
so moving forward - how would I subtract from the output red channel each frame, checking to see if it was 0


2017-03-25 01:05:29
figured out the crash that turned up during last session - or at least figured out how to avoid it. When the number of max iterations is reduced, less time is spent computing. It seems that if the same image is passed to the network at a high enough rate, it crashes. No idea why. Its arcane. Anyway, by scaling the recycled input with a multiplier > 0 the problem doesnt turn up.

More sigfnificantly, I made some exciting progfess towards a more expressive visual language. I costs nothing to color correct and transform the output after its been computed. I'be also tweaked a number of the deepdream make_step parameters. not sure what will stay, still experimenting.

The danger is to get caught in a loop of experimentation though.
1. how can I save the settings and configurations I come across so I can find them again?
2. camera 2
3. what are the controls exposed to participants
4. program USB pad w ASCII sequenceas for controls


2017-03-25 10:28:52
goals (Saturday)
- transforming during the cycle
	- is possibnle? how?
- color correction beta
	-	color
	-	luminance
- image transformation beta
	-	scaling (zooming in)
	-	warping the frame buffer

goals (Sunday)
-	dual cameras
-	guide images


2017-03-25 10:38:44
studying image translation

translation basically means that we are shifting the image by adding/subtracting the X and Y coordinates. In order to do this, we need to create a transformation matrix,

rotation matrix
We can specify the point around which the image would be rotated, the angle of rotation in degrees, and a scaling factor for the image


2017-03-25 18:52:56

reading about 2D convolution (in regard to image processing)

What does "frequency" mean in an image? Well, in this context, frequency refers to the rate of change of pixel values. So we can say that the sharp edges would be high frequency content because the pixel values change rapidly in that region. Going by that logic, plain areas would be low frequency content. Going by this definition, a low pass filter would try to smoothen the edges.


2017-03-25 20:39:01
came across a section on how to make a vignette.
this is probbaly something that should happen at the post rendering stage, similar to the HUD


2017-03-25 21:54:54
came across method for gamma correction


2017-03-25 22:52:24
I've been able to get a kind of color grading happening with what I've learned today. The code is sluggish at the moment as not of what I've added is optimized, and in particular  the vignette that I'm adding is sort of expensive. Also not sure if gamma correction on the input or the output or both is the way to go. I have the computation setup on the camera input, but again, pretty wasteful - is calculating the lookuptable every frame, when it only needs to do so on init and when the gamma value changes.

I'll want to add a control for increasing/decreasing gamma. Interesting to see how it reacts to exposure and brightness set on the Linux camera control utility


2017-03-26 10:08:30
turned off the color grading functionality created yesterday until I can optimize a bit further.
goals:
	- integrate camera 2
		- realtime switching between cameras
		- composite views
			- overlay
			- 2-up
		- just had an odd idea - is it possible or desirable to create a small snapsot of the camera and composite that on to the viewposrt so that, multiple frames are always shown.
			- further, it would behave liek the queue I'd been thinking about, the most recent capture would always be shown as the last image, and would push older images out of the stack.


2017-03-26 10:12:25
easy enough to access the different cameras by indes. a good start :)
- add a keybind to switch between cameras at runtime


2017-03-26 11:16:41
Just ran it with 2 cameras simultaneously at 1280 x 720. Not wuite sure what the expense was. System seemed responsive - perhaps a bit less fluid than before?


2017-03-26 13:15:01
I'm wanting to replace all the print statements w proper logging

The different levels of logging, from highest urgency to lowest urgency, are:

CRITICAL
ERROR
WARNING
INFO
DEBUG
The setLevel() call sets the minimum log level of messages it actually logs. So if you fh.setLevel(logging.ERROR), then WARNING, INFO, and DEBUG log messages will not be written to the log file (since fh is the log handler for the log file, as opposed to ch which is the handler for the console screen.)

To write a log message in one of these five levels, use the following functions:

logger.critical('This is a critical message.')
logger.error('This is an error message.')
logger.warning('This is a warning message.')
logger.info('This is an informative message.')
logger.debug('This is a low-level debug message.')


2017-03-26 14:00:54
there's a lot more to logging than expected, but I've got a good replacement for all those print statements, now - back to work on that camera!


2017-03-26 14:50:46
realizing that yesterdays tests that I thought were running on a 1920 x 1080 input were actually running on a 1280 x 720 input and scaling up to 1920 (which looked great actually). Those values were hardcoded into the camera instance


2017-03-26 14:52:18
crashes when I set portrait_alignment = False. but why?


2017-03-26 20:23:43
reverted back to the point before I added logging, will continue with print statements as before.


2017-03-26 22:56:58
getting there - able to toggle portrait_alignment without crashing


2017-03-27 11:49:30
struggling with the viewport.
Here's the problem.

I want to be able to toggle portrait_alignment on/off
why?
so that the viewport shapes itself to match whatever the camera is outputting


2017-03-27 17:49:33
making some progress wi the viewport finally


2017-03-27 22:04:44
It seems that the Composer.buffer array needs to be reshaped as well
Hunting this down is so much harder than it needs to be. It points out the fallacy of decentralizing these sources.


2017-03-27 22:11:59
Here's the reality. you need to move on. Forget about the idea of generalizing the camera orientation. Just assume it to be oriented properly when the program starts. It doesn't need to switch back and forth at run time.

With that in mind - I can do something like this:

create camera objects
derive viewport size from camera.width,height
de


2017-03-27 22:37:19

typed in a bunch of stuff maybe it works.
basic idea was to pull capture_size from the camera object
Viewpoert_size has become an instance of the class Display, which exists at the moment only to house a width and height value accessible thrui dot notation. Once I get it working, I'll replace that bit with a dictionary, or movit back to the Data module.

mocing on, I made global substitutions to reference these changes. At a minimum it shpuld crash in the same way as before.


2017-03-27 23:18:28
its hallucinating on either camera in landscape again
and crashes on portrait just as before - same reasons


2017-03-27 23:40:22
a bit more detail has it crashing further along. This time it showed the camera output in portrait orientation before crashing. Now that the display size is being adjusted when initialized, the previous conditions I wrote there no lobger applies


2017-03-27 23:43:22
There we go - its working.
I can switch between portraint and landscape modes when the program initializes

Let me try to sum up:

The Display is the onscreen framebuffer.
The display supports 2 aspect ratios:
-	landscape (16:9) default
-	portrait (9:16) transposed counter clockwise
-	the display can be flipped horizontally and vertically in any aspect

The Camera is the framegrabbing and Queing system

Create a camera object, specifying:
- capture_width,
- capture_height
- portrait_alignment

The Display object relies upon the camera object
-	display width, height are stored here
-	display width, height are swapped here to match the camera alignment
	-	if the orientation is portrait then the specified display width and height have to be swapped
- the Viewport class relies on knowing the proper Display width, height so:
	- Viewport.show() can scale lower ocataves in buffer1 proportionally to match the display size
- the Composer class relies on knowing the proper Display width and height so:
	- Composer.update() can run inceptionxform on buffer 1
	- buffer2 can resize itself to match the Display width
- show_HUD() relies on knowing the proper Display width, height so:
	-	the function draws HUD updates to a seperate frame buffer that needs to match the DIsplay size

/* I'm noticing that Viewport.show() and Composer.writeBuffer2 basically do the same thing
Viewport.Show() is actually writeBuffer1() + show() */


2017-03-28 00:57:33
cleaned up the logging (print statements) - got rid of most of it
The camera/display issue isnt fully resolved, the frame buffer isnt calling the inceptionxform properly, so it just sits on the same image


2017-03-28 13:28:56
Added expandable logging framework to debug the code better and I guess also as a bit of a programming exercise. Was not happy with my  progress yesterday, enough so that I took a day off from work  to  get my momentum back


2017-03-28 14:56:16
replaced all print statements with logging calls. In a much better position to debug efficiently.


2017-03-28 22:28:52
I have the system up and running on the Monolith. It looks startling. Its amazing. Numerous conclusions to be drawn from the initial test run:
-	the video4Linux Control Panel is only addressing a single camera. Is there a way to run 2 instances of this program and specify the camera?
	- as a fallback, is it possible to emulate aspects of the control panel in software?


2017-03-29 00:34:41
Yes, there is a way to run 2 instances of the video4Linux control panel. There's a lot more functionality there than I knew. It also turns out to be trivial to mirror the captured image vertically and horizontally. Vertical mirroring is surprisingly cool, the forms that emerge are a bit disconnected from your movements.

I'm going to implement camera switching next and then camera flipping
Before getting to that, there's a rendering bug where:
x the sine wave transform doesn't get picked up by the next rendered image, so it appears briefly then disappears instead of propogating
x the octave size frequency mod isn't working
x the inceptionxform funtion isn't calculating the transform correctly


2017-03-29 20:52:59
x	camera switching by pressing F1 / F2
P1 	refine motion detect to allow getting close
P1	sequencing - motion between programs
P1	parameters - what are they - create a list
P2	saving good values - how?
P2	guide images
P3	image capture


2017-03-29 21:18:56
HUD is back online. making the text smaller
am also wondering if possible to output those values to a MatPlotLib window?


2017-03-30 01:19:27
both cameras are running simultaneously. I'm not seeing any real slowdown or latency as a result


2017-03-30 10:24:24
camera switching is working and its cooler than I thought it would be - except for the initial switch, which seems to rely on motyion being detected instead of the viewport being forced to refresh


2017-03-30 11:07:31
camera switching looks like its working - have not fully tested motion detection. looking at that next


2017-03-30 22:26:37
some problems re-addressing camera by index when I switched the USB ports prior to rebooting. Still trying to remember how I brought up the control panels for the cameras

2017-03-31 00:05:32
P1 	refine motion detect to allow getting close
P1	sequencing - motion between programs
P1	parameters - what are they - create a list
P2	saving good values - how?
P2	guide images
P3	image capture
P2	duration based time-out from dreams
	-	forces end of cycle based on how long its been running
P1	transition from end of cycle to beginning of next so the progression is not quite so abrupt


2017-03-31 13:47:00
taking a look at MatplotLib for analyzing what the motion detector is doing .
Keep in mind that there are 2 other areas needing momentum.
P1 	refine motion detect to allow getting close
P1	sequencing - motion between programs
P1	parameters - what are they - create a list



2017-03-31 15:03:21
I found some code to do realtime plotting w matplotlib, looking at it running now. Is pretty CPU intensive.


2017-03-31 23:18:05
added support for flipping camera input horizontally or vertically


2017-03-31 23:20:49
taking a second look at gamma cprrection


2017-04-01 02:38:11
I put some rough  monitoring in place on teh motion detection viewer, but all it showed me was that the behavior is  more fluid and complicated than I thought. The previous concept of an "overflow" when the current sample and next sample are both over the threshold, doesn't seem to happen any more becaus the threshold is raised by the average value of the last 50 samples

or something like that. In any case its hard to quantify the conditions that result from large motions near the camera. To solve this problem further, I need to look at the data that gets generated.

For tomorrow - put this aside, and work on program settings
- need an explorer setting (which allows me to navigate the space)
- need a way to toggle back and forthe between explorer mode and automated mode
	+  for demonstration
	+  for identifying settings
- need categories for program settings
- need a timer to switch between programs
- need a way to switch network models from within a program
	+ what else needs to be captured within a program?
		* brightness cycle


2017-04-01 14:27:41
reading up on file handling in preparation for saving out program settings.

WHAT ARE PROGRAM SETTINGS?

Currently:

	name:
	iterations:
	step_size:
	octaves:
	octave_cutoff:
	octave_scale:
	iteration_mult:
	step_mult:
	model:
	layers: []
	features: []

new parameters:
capturefx: [] 	# ordered list of image processors called each capture
stepfx: [] 		# ordered list of image processors called each step
cyclefx: [] 	# ordered list of image processors called each cycle


2017-04-01 17:09:30
status:
I've created an FX class
inside are 2 functions - xformarray and octave_scaler
I'm instantiating an FX object  and manipulating that
currently as explicit commands:
FX.xform_array(Composer.buffer1)
FX.octave_scaler(model=Model)

how would I pass these in from a list, or dictionary?

# xform_array, Composer, octave_scaler, Model are all global references available to the FX class
cyclefx = []
cyclefx.append({
	which_func: xform_array,
	which_params: Composer.buffer1
})
cyclefx.append({
	which_func: octave_scaler,
	which_params: Model
})







FX = FX(composer=Composer, model=Model, fxlist={function1, function2} )

class FX(object):
    def __init__(self, composer, model, fxlist):
    	self.composer = composer
    	self.model = model
    	self.fxlist = fxlist
        self.direction = 1

        cyclefx = []
        cyclefx.append({
        	which_func: xform_array,
        	which_params: [Composer.buffer1, 10]
        })
        cyclefx.append({
        	which_func: octave_scaler,
        	which_params: [self.model, 0.1, [1.2, 1.6]]
        })

    def process(self):
    '''
	iterate thru the functions in fxlist here. where do the parameters come from?
	1. xform_array needs:
		- reference to relevant image, assumed to be from Composer.buffer1
		- multiplier value for step function

	2. octave_scaler needs:
		- pointer to Model where the deep dream params are stored
		- scaling factor
		- upper and lower limits
    '''
[self.composer.buffer1, shift_amount]
[self.model, scaling_factor,[1.2,1.6]]
FX.process(cyclefx)


2017-04-01 23:04:48
taking a different approach after some futher thought. Added a cyclefx dictionary containing pointers to functions within an existing program dictionary. Its working as expected. Experimenting with placement of the funtions that get dispatched. These functions are cufrrently defined in the same Data module as the program definitions themselves.


2017-04-02 00:02:37
closer to working now. successfully calling the function specified if the program with the arguments specified. Messy looking. Seeing where I can cleanup.


2017-04-02 01:39:15
cleaned up the data structure of the program a bit so that the fx block is structures like this:

'cyclefx':[
	{
		'func': function1,
		'params': {'param1':'dogs', 'param2':99}
	},

	{
		'func': function2,
		'params': [1,2,3,4]
	}
]

cyclefx is a list containing dictionaries which store function pointers and parameters to be called upon with each cycle

fxlist = Model.program[Model.current_program]['cyclefx']
do_fx = fxlist[index]['func']
params = fxlist['params']
do_fx(**params)


2017-04-02 10:03:22
This syntax is so tortured, it can't be right, but uit's working.  Needing excpert advice (Spoto?)  to take a look through this.  What I'm doing feels well intentioned, but is so messy it must be a haCK?


2017-04-02 10:07:23
Those parameters could come from anywhere, and might superficially cleanup the code to do som, but doesn't make sense that the function parameters would be seperated from the function pointers


2017-04-02 15:17:10
note to self before I forget. Anyone who's ever wanted to "learn to code" needs to experience this moment to truly get it. The stakes seem so high to me right now, and looking backl I've put so much of myslef into understandingthis idea and how to realize it. Learning python has been a big part of that. I didn't realize how beautiful the language is. Truly, its like Elvish. But right now - thinking through the trial and error of passing functions and parameters as part of a "program" that drives my artwork is the most challenging computer science ever. Its bitter to know that you could have done it differently, that you didnt understand something the way you thought, or that  you are almost certainly missing out on a basic concept, knowledge of which would make this current impasse invisible. Still - I'm hacking my waty to the solution, and its happening right now!


2017-04-02 15:57:00
Fantastic - just demonstrated solution to storing functions and function parameters in pre-programmed definitions


2017-04-02 17:41:33
Still not there. What if I'd been making the wrong assumptions entirely. The functions in question could be  written to the Model class, just like the rest of the current mocel parameters, such as step)size and so forth.


2017-04-02 18:18:49
working implementation now. Demonstrated switching between 2 different programs with different params for the xform_array cyclefx.
x implement same for octave scaler
x iterate thru the list stored in Model.cyclefx
- implement feature for stepfx


2017-04-02 21:24:32
until now it wasn't really obvious to me that a higher octave_scale led to a faster cycle time. not just by a little, either


2017-04-02 21:40:17
Fantastic news! its working as designed. NMot quite the way I thought it would, but ended up cleaner than prior work sessions suggested. A smuch as I want to pass in a "job list" of functions to each of these programs, I don't know how to setup the system to make that happen. The problem is that the Program data structure is just attached to its module luike a filing system. Its difficult to reach into and pass pointers to dynamic quantities, such as Composer.buffer1. I found it difficultr to do while also passing in specific values - parameters that I wanted top pass to a function, such as blur=3

Maybe after a day and half of hacking it, if I were to readress the probglem, I'd know how to solve it better. Already some ideas, such as turning the Program data structure into its own class. Not sure why I previously didn't.


2017-04-02 22:50:44
adding stepfx now


2017-04-03 00:35:17
added inception_xform to cyclefx list
cleaned up program deginitions somewhat


2017-04-03 01:47:34
added median filter and an opacity function to stepfx. Median Blur behaving oddly though, disallowing kernel sizes > 5 Otherwise working as expedted

- bilateral filter
- gaussian filter
- duration_cutoff (early exit to rem cycle based on timer)

[not sure if these are stepfx or cyclefx]
P1 program switcher (chooses another program based on timer)

P1 Vision Quest
	- explore program settings
	- write out textfile w current settings on demand

P! Controls
	- new keybindings
		+ Toggle Camera
		+ Reset to default program
	- verify functionality w external USB keypad
		+  can Thea help with key labels?

P1 Exporting Images & Video


2017-04-03 18:31:44
added bilateral filter to stepfx list
x bilateral filter
x gaussian filter
x duration_cutoff (early exit to rem cycle based on timer)


2017-04-03 19:28:45
How does the duration cutoff stepfx work?
- specify a duration
- make note of the time when each cycle starts
	+ where?
		* The FX object?
- with each call to the duration_cutoff() function, get the elapsed time by subtracting the current time from the start time
- if the elapsed time is greater than the specified duration then
	+ how to force a new cycle to start?
		* force MotionDetector.wasMotionDetected = True ???
		* use the descriptively named Viewport.force_refresh flag?
			- yes, this. I created a refresh() function to wrap that

2017-04-03 21:32:53
I have the basic timer function setup, and verified registering time on the FX.cycle_start_time property each cycle. It's getting the data passed to it from the program declatration as well.


2017-04-03 21:43:43
The cutoff function is working and can also be used as the basis for the program timer, but its's rough. calling Viewport.refresh() immediately refreshes the viewport, but would be much more fluid if the new cycle and the old dissolved - exactly the way it happens during motion detection and Composer.is_compositing_enabled = True. SO how does that work?


2017-04-03 22:04:37
the transitional behavior I'm describing takes place during the normal course of things when
	- we've entered a new cycle, AND the MotionDetector is NOT in a 'resting' state
	- what does 'resting' mean? just that the readings have stabilized enough that the current reading matches the previous reading
		+ so when the MotionDetector isn't resting it just means that the current value was different than the previous one. Which must happen often enough.
		+ From what I can tell, the resting state can only refer to a condition where there is stillness (of course).
			* the  pixel count values must be zero or beneath the floor, , and so are reported as zero.
		- this period of stillness corresponds to the hallucinating state -. In other words, 'it can only see you when you're moving'

2017-04-03 22:58:30
did a bit of invetigation into how motion detection works. Calculating a "ratio" based on pixels_detected/total_pixels. This shows a percentage of how much of the screen is in motion. One of the areas I wanted to enhance was relaxing motion detection when subjects are close to the camera. This is the basis for that determination


2017-04-03 23:02:33
The reason I'm getting an immediate "cut" instead of a dissolve for the duration_cutoff function is because I'm only refreshing the Viewport to force a new cycle. I also need to override the MotionDetection resting state.


2017-04-03 23:13:57
That worked. FInished implementing the duration_cutoff stepfx. Playing around with it , I;m not sure how much value it has. Its definitely a different experience. It feels closer to realtime, especially when the duration is set low,  which effectively delivers a consistent (although low) frame rate. Thing is, the images generated are incomplete and in some case, pretty low resolution. Maybe not si attractive. Will have to test this feature out to see the valdity.


2017-04-03 23:16:20
Picking up work on the Sequencer control next. This is a stepfx almost identical to duration_cutoff.

What does the sequencer need to know?
- index of next program
- time remaining until start next program

Does the sequencer need to be specified in program declaration?
- no

Where is the program duration stored?
- let's assume that all program's run for the same durayion
- when a program starts, it registers its start time in the FX class
- actually, no - its more self contained if all that info is kept in the Model class, with all the other program params

- specify a duration
	+ where?
		* attached to each program?
		* specified by the function call (so all programs are of the same duration)
- make note of the time when each program starts
	+ where?
		* The FX object
- with each call to the sequencer() function, get the elapsed time by subtracting the current time from the start time
- if the elapsed time is greater than the specified duration then
	+ select another program
		* how?
			- step thru program list indices, just like prev/next controls already do
			-
		* force MotionDetector.wasMotionDetected = True ???
		* use the descriptively named Viewport.force_refresh flag?
			- yes, this. I created a refresh() function to wrap that

-

2017-04-03 23:41:46
removed Viewport.refresh() from the duration_cutoff() function. Its more interesting now that it doesn't re-do the whole screen.


2017-04-04 07:23:04
implemented basic program sequencer. It just cycles through the program list by calling Model.next_program()
- what about "themed" programs? For example, "afternoon" and "evening"?
The program list is 1 dimensional at the moment, but could do something like this:

program = {

}

program = [1,2,3,4]
kb
program = [
	[1,2,3,4],
	[1,2,3,4]
]

This would be the basic structure allowing  me to access programs banks
program = {
	'am': [1,2,3,4],
	'pm': [1,2,3,4]
}

This is how the program declaration would look
program['am'].append({
	'name':'geo',
	'iterations':10,
	'step_size':3.0,
	'octaves':4,
	'octave_cutoff':4,
	'octave_scale':1.4,
	'iteration_mult':0.5,
	'step_mult':0.0,
	'model':'places',
	'layers':[
		'inception_3b/5x5',
	],
	'features':[-1,0,1],
	'cyclefx':cyclefx_default,
	'stepfx':stepfx_default
})


2017-04-05 00:06:19
Programmed the USB keypad with some keyboad macros and am validating on Linux


2017-04-05 00:30:13
I've validated the input from the USB keypad. It works! Need to change a few function assignments to match though.
- Toggle Camera
- Reset All
- Prev/Next Program Bank
- stub in listener definitions for unassigned keys

Think about the kind of logging that is most useful in realtime - in the terminal
Motion detection status:
floor
delta_threshold
current value
Ratio
program change
layer change
featuremap change

How are images being saved?
Have you tried the other network model? Is it possible to switch between them  in a program? What happens when you try?


2017-04-05 01:11:01
taking a quick look at how the network model is imported. It seems that its is assigned to the model instance with a keyvalue when the object is created.

the choose_model() function is only called when the class is initialized


2017-04-05 01:25:18
Uh... wow . Swapping the model as part of aprogram change seems to work just fine. That's great! The Model class is a bit of a mess. I knew a lot less then. What will my code look like  6 months from now?


2017-04-05 01:56:48
What's left?
P1 Implement Program Bank system
P1 Prev/Next Program Bank
P1 Pause Seqeuncer - for demoing or live exploration through  layers or featuremap without the program change interrupting
	- can create a dedicated bacnk for a program(s) that support this behavior
	-
P1 Exporting images
	- every octave?
	- every new cycle?
	- every completed frame?
		+ is there a way to identify completed frames in the filename?
		+ Is it possible to export buffer2 as well?
P1 Create and curate programs
x Toggle Camera
	P4 what would it take to combine the camera views? Where would that be done? How?
P1 Reset All
P2 Add listener definitions for unused keys
P3 Take another look at motion detection. Is it possible to gate the detection behavior when the ratio is above a certain threshold?


2017-04-05 14:06:42
working on Toggle Camera


2017-04-05 15:22:12
reorganized listener function and logging. verified keypad input


2017-04-05 15:30:15
How do we know which camera is the current one?
Webcam.current is the index in the camera list
Webcam.get() return s a pointer to the current camera

How do we set the current camera by index?
Webcam.set(index) will return a pointer to the current camera and update the Webcam.current value


2017-04-05 16:11:23
implemented toggle camera


2017-04-05 16:27:42
testing what's working with image export before diving further into the program bank system


2017-04-05 16:38:39
getting too many chaff frames, what if I just wanted to see fully rendered frames
or what I wanted to see only composited frames?


2017-04-05 16:44:59
Best place to export frames is from the same  cyclefx case that runs inception_xform. What if  thet fx hadn't been used for a program  though? Where would rendered images appear from?


2017-04-05 16:53:16
completed export pipeline.
- add a control to enable/disable feature to finalize
- add HUD label for "exported: [filename]"

2017-04-06 00:08:18
It's close. You need to think about simplifying and finishing. Great beta test earlier this evening w Scott Storrs and Aileen. Some kind words, but more importantly - the chanc eto see how the current system behave in a public situation. Some outcomes

1. Dont expose anything but camera selection on the control panel
	Maybe also the HUD
	And pause motion detect
	The rest of the controls stay assigned to the keyboard, which is easily accessible
	Doing so requires me to repogram the USB keypad

2. Keep every program in bounds of current parameters
	Reset parameters when switching programs (pretty suire this is already happening)


2017-04-06 01:14:40
Disabled image export for the moment. Dont forget to re-enable it


2017-04-06 01:33:31
interesting that I can make some changes to the placement of the  the inception xform effect within the Composer update function.


2017-04-06 01:35:46
I've moved the inceptionxform effect to the is_compositing enabled path way. Moving that block of functionality makes the transformation happen at different "pahases" of the update. I.m not entirely clear why. Just an intuition. Its looking very interesting placed where it is.  more fluid



2017-04-06 16:34:05
setting up at the  Hammer Theater in San Jose


2017-05-07 17:57:03
I gained some insights at LASTFEST2017, it was the most nuanced and interactive show thus far. There was a big payoff for staging it with dedicated gear, as I did. One unexpected consequences of that is that I now have a storage space - needed somewhere to stor ethe gear for easy deployment
.

I'm back to the project after some time away. Will organize my goals and thoughts a bit later but here are the outcomes I achieved

- invitation to speak at Piero Scaruffi LAZER talk in July
- private show being planned here with primary goal being promotion and a night of hallucinations that I want to turn into a portrait series.

- next steps?
- many more possibilities than I'd realized, maybe a bit afraid to say it out loud?

2017-05-07 18:02:11
stepping back into python and studying multiprocessing again.

2017-05-07 18:39:36
 The multiprocessing module allows you to spawn processes in much that same manner than you can spawn threads with the threading module.

2017-05-09 16:00:42
CTRL-J joins the line below to the end of the current line
CTRL-L selects the current line
CTRL-C copies current line if no selection
CTRL K,B toggle sidebarx


2017-05-09 17:01:15
Try and Except.
If an error is encountered a Try block execution is stopped and transferred down to the Except block. In addition to using an Except block after the Try block, you can also use the Finally block. The code in the Finally block will be executed regardless of whether an exception occurs.


2017-05-09 18:09:59
the join() method tells Python to wait for the process to terminate.
2017-05-16 20:39:15
Feeling so blocked by upcoming talk and the private show I've been thinking about
How to stop feeling blocked? Do something now.
- work on my talking points
- collate current work
- update deepdreamvisionquest.com
- contact Piero S to discuss upcoming event and my topic
- create guest list for event
- transfer equipment from storage

2017-05-16 20:53:15
I've setup a local repository on the MacBook

2017-05-26 14:01:41
The upcoming LASER talk has been sublimating even as it seemed like procrastination.
The title:
	So Much Neural
The subject:
	I want to talk about how my life as a videogame designer has influenced my new work and describe the ways I learned to use 	psychedelic machine learning to look for Universal Images

The Theme:
	Deep Dreams, Universal Images

Notes
This talk answers the question, “where do the images come from”, “why these images are important”, “where do these feelings come from”,”I can’t take my eyes off it. Why?”, What is the meaning?

For show and tell,
- it uses a series of computed portraits with imagery produced by my Deep Dream Vision Quest neural video installation.
- full setup with magic mirror
- projected setup

What have I discovered from live shows
- people matter
- staging and setting matter
Where does the data come from and who owns it?
What do I get out of it?
Applications
- entertainment
- therapy
- outreach
- surveillance
- roleplaying

Talking Points

We live in a hyper modern world where things blur together, the categories are blending together.

What does human mean now? The Othering. To be Other.


My mom is seeing AI in her camera. Its a filter that restyles the world like a painting. How is that app on her phone different than my work?

The Mandela Effect - why?

We seek to surface that which lies submerged – desire, guilt, fear, ambition – to bring to light the truth the waking mind keeps hidden
Why?
To find the Familiar in the Alien
Why?
Because the contrast is exciting
Why
Because there are Universal Images
Why
They resemble the classifications of a neural network
Why
The underlying behavior of learning machines must be universal
Why
Because the algebra and the architecture is the same

Therefore:
All perception begins as hallucination
Mental images from activated neural patterns  project outward as iterations in a feedback loop of recognition-reclassification
Neural patterns?
Yes. Archetypes. Geometric memories.  Arrays of filters.
Projected from where?
The Center
What is at the center?
Me. I am hiding something

What are some of the themes common to this imagery
Repetition
Embellishment
Replacement
Structure
Autocompletion
Suggestion
Shorthand
Radial Symmetry
Scale

2017-05-28 10:31:40
Configured Windows w Sourcesafe and so forth

2017-05-28 21:32:58
building the feature block on the main deepdreamvisionquest page
- create blog posts
    + Beginning
        * setup
        * testing
    + Middle
        * moments
        * best of
    + End (these are placed in a seperate media gallery accessible from top menu)
        * encounters (video)
        * portraits

2017-05-29 16:21:58
Not sure how much I really accomplished in this worksession. The site looks different. probably better. Definitely cleaner. But where is the new content?

2017-05-31 15:21:17
Reading up on the LASER talks


The LASERs are a national program of evening gatherings that bring artists and scientists together for informal presentations and conversation with an audience


Fromm Hall
2497 Golden Gate Ave
San Francisco, CA 94118

Fromm Hall hosts art studios, student housing, the Fromm Institute for Lifelong Learning, and Saint Ignatius parish offices.

Informal
35 minutes
assumptions: projector screen (how big)
USF, Fromm Hall, Berman Room, FR115

2017-05-31 16:13:19
The question I'm trying to answer is how can I show realtime hallucinations in the room?
Can I rely on the projector?
Should I consider my own projector?
Should I consider the full Deep Dream rig?

setup time needs to be minimal. talk is only 35m
need to setup and test before the talk

The talk is a show & tell
The showing is more epic when it points at an audience
With the right rig - could demonstrate specific effects & setups - camera, light

2017-05-31 16:23:42
requested more info about the space from @usfca

2017-06-01 08:46:15
no response from @usfca

2017-06-01 08:46:30
collating prior LASER abstracts


Mainland China has staged one of the most impressive economic booms in the history of the world, without a single recession in 30 years.The nation is now undergoing another transformation, from a manufacturing-based economy to an IT-based economy.The Chinese like to talk nonstop about "innovation", but "innovation" can have wildly different meanings in the USA and in China.

    THEME
    How does innovation transform global economies differently?

    OBSERVATION
    Innovation can have wildly different meanings in the USA and China

    WHAT PROMPTED OBSERVATION?
    The Chinese like to talk nonstop about innovation

    TOPIC
    Mainland China has staged one of the most impressive economic booms in the history of the world

    TOPIC MOVES FROM A TO B
    The nation is now undergoing another transformation from a manufacturing based economy to an IT based economy


The story of the development of the arts in Silicon Valley has just begun to be told.Its art history is filled with people who were often marginalized, people who stood up to the status quo, people with the guts and love to persevere and build a community that nourished all, at a time when that was not easy to do.It's time to tell the story.How did we get from the largely monochromatic, exclusive, and repressive landscape of the 1970s to where we are now? Silicon Valley blossomed in the last quarter of the 20th century with the formation of arts offshoots, spin-offs, and startups that tapped into the area's increasing ferment of ideas and involved myriad supporters across all walks of life.

    THEME
    It's time to tell the story about the art community in Silicon Valley

    OBSERVATION
    The area's increasing ferment of ideas involved myriad supporters across all walks of life.

    WHAT PROMPTED OBSERVATION?
    Silicon Valley art history is filled with people who were often marginalized

    TOPIC
    Silicon Valley blossomed in the last quarter of the 20th century with the formation of arts offshoots, spin-offs, and startups

    TOPIC MOVES FROM A TO B
    How did we get from the largely monochromatic, exclusive, and repressive landscape of the 1970s to where we are now?


Pantea Karimi presents and discusses her medieval and early modern scientific manuscripts research project. Karimi's research topics include: Medieval Math, Medieval Paper Wheel Charts Calculators, Medieval Cartography, Medieval Medicinal Botany and Optics. Through her work she invites the viewer to observe science and its history through the process of image-making. In her talk she presents the scientific manuscripts pages, the process of research and how she uses the visual elements in early science to create her art.

    THEME
    A decolonialized view of science history through the process of image-making

    OBSERVATION
    n/a

    WHAT PROMPTED OBSERVATION?
    n/a

    TOPIC
    The artist's medieval and early modern scientific manuscripts research project

    TOPIC MOVES FROM A TO B
    How she uses the visual elements of early science to create her art.



As an astronomer, I view new telescopes as a steadily increasing number of senses, new interfaces to the world, that bring otherwise inaccessible phenomena into my intimate awareness. I will present a brief history of the universe informed by this perspective. Most people on this planet have never met a scientists nor used a scientific instrument. I believe that part of the cultural change needed to build a sustainable society involves making scientific knowledge acquired through instruments an intimate part of daily life. Just as the inability of large banks were to respond to the daily needs of individuals led to the micro credit movement, I argue that scientific institutions are unable to respond to the scientific needs of individuals, and that a micro-science movement is needed. I will give examples of the work of artists that in my view are exemplars of intimate science

    THEME
    Making science intimate

    OBSERVATION
    Most people on this planet have never met a scientist nor used a scientific instrument

    WHAT PROMPTED OBSERVATION?
    As an astronomer, I view new telescopes as a steadily increasing number of senses, new interfaces to the world, that bring otherwise inaccessible phenomena into my intimate awareness.

    TOPIC
    The cultural change needed to build a sustainable society involves making scientific knowledge acquired through instruments an intimate part of daily life.

    TOPIC MOVES FROM A TO B
    Just as the inability of large banks to respond to the daily needs of individuals led to the micro credit movement, I argue that scientific institutions are unable to respond to the scientific needs of individuals, and that a micro-science movement is needed


New computer methods have been used to shed light on a number of recent controversies in the study of art.For example, computer fractal analysis has been used in authentication studies of paintings attributed to Jackson Pollock recently discovered by Alex Matter. Computer wavelet analysis has been used for attribution of the contributors in Perugino's Holy Family. An international group of computer and image scientists is studying the brushstrokes in paintings by van Gogh for detecting forgeries. Sophisticated computer analysis of perspective, shading, color and form has shed light on David Hockney's bold claim that as early as 1420, Renaissance artists employed optical devices such as concave mirrors to project images onto their canvases. How do these computer methods work? What can computers reveal about images that even the best-trained connoisseurs, art historians and artist cannot? How much more powerful and revealing will these methods become? In short, how is computer image analysis changing our understanding of art? This profusely illustrate lecture for non-scientists will include works by Jackson Pollock, Vincent van Gogh, Jan van Eyck, Hans Memling, Lorenzo Lotto, and others. You may never see paintings the same way again

    THEME
    How is computer image analysis changing our understanding of art?

    OBSERVATION
    You may never see paintings the same way again

    WHAT PROMPTED OBSERVATION?
    Sophisticated computer analysis of perspective, shading, color and form is increasingly used for attribution and authentication of artwork

    TOPIC
    New computer methods have been used to shed light on a number of recent controversies in the study of art.

    TOPIC MOVES FROM A TO B
    What can computers reveal about images that even the best-trained connoisseurs, art historians and artist cannot?


A very brief history of the accidental discovery of natural radio in the late-19th Century, the musical aesthetics of scientific research in the 1920s and 30s, and the beginnings of amateurism and arts in the second-half of in the 20th Century.

    THEME
    The electromagnetic Imaginary

    OBSERVATION
    n/a

    WHAT PROMPTED OBSERVATION?
    n/a

    TOPIC
    A very brief history of the accidental discovery of natural radio in the late-19th Century, the musical aesthetics of scientific research in the 1920s and 30s, and the beginnings of amateurism and arts in the second-half of in the 20th Century.

    TOPIC MOVES FROM A TO B
    Accidental discoveries and correlations

The "Sounds of Space" project is being developed to explore the connections between solar science and sound, to compare visual and aural representations of space data, mostly from NASA's STEREO mission, and to promote a better understanding of the Sun through stimulating interactive software. I will be talking about the work I am doing with musicians to sonify current solar wind data (particle data and magnetic fields) and images of the Sun.

    THEME
    Promote a better understanding of the Sun with interactive software

    OBSERVATION
    Comparing visual and aural representations of space data engages the public

    WHAT PROMPTED OBSERVATION?
    n/a

    TOPIC
    The "Sounds of Space" project is being developed to explore the connections between solar science and sound

    TOPIC MOVES FROM A TO B
    I will be talking about the work I am doing with musicians to sonify current solar wind data and images of the Sun.



Mat-forming Cyanobacteria in San Francisco Bay salt marsh ponds move in a gentle coordinate dance of 3.5-billion years, creating our oxygen atmosphere. I wanted to capture, in motion and music, a sense of this deep time and relentless movement.

    THEME
    Motion and Music

    OBSERVATION
    Mat-forming Cyanobacteria in San Francisco Bay salt marsh ponds move in a gentle coordinate dance of 3.5-billion years creating our oxygen atmosphere

    WHAT PROMPTED OBSERVATION?
    Our oxygen atmosphere.

    TOPIC
    Deep Time

    TOPIC MOVES FROM A TO B
    I wanted to capture, in motion and music, a sense of this deep time and relentless movement.

3D printed architecture has the ability to transcend the way that buildings are made today. 3D printers allow architects to be material morphologists.They expand our ability to construct because they open the door for us to test material, form and structure simultaneously and instantly. 3D printing is a sustainable method of manufacture and can take advantage of local and ecological material resources. In an era of throw away consumerism and over consumption, excessive energy use, too much waste, and toxic materials, architects have a responsibility to the public, and the planet, to change our mindset about what our buildings are made of, how they function, and to inform the manufacturing processes used to construct architecture. Our research challenges the status quo of rapid prototyping materials by introducing new possibilities for digital materiality.In this scenario it is not solely the computational aspects that have potential for material transformation but also the design of the material itself. Because of the nature of these materials, they can be sourced locally (salt, ceramic, sand), come from recycled sources (paper, rubber), and are by products of industrial manufacturing (wood, coffee flour, grape skins); this would situate them within the realm of "natural building materials". However, the expansive and nascent potential of these traditional materials, when coupled with additive manufacturing, offers unnatural possibilities such as the ability to be formed with no formwork, to have translucency where there was none before, extremely high structural capabilities and the potential for water absorption and storage, the materials that we all know as natural building materials are now unnatural building materials.

    THEME
    New possibilities for digital materials

    OBSERVATION
    The materials that we all know as natural building materials are now unnatural building materials.

    WHAT PROMPTED OBSERVATION?
    Traditional materials, when coupled with additive manufacturing, offer unusual possibilities

    TOPIC
    3D printed architecture has the ability to transcend the way that buildings are made today.

    TOPIC MOVES FROM A TO B
    Architects have a responsibility to the public, and the planet, to change our mindset about what our buildings are made of, how they function



Take Me To Your Dream (Dream Vortex) is a work-in-progress, a virtual installation for the KeckCAVES 3-D imaging facility at the University of California, Davis, and an artistic experiment with many layers of collaboration. In addition to the primary relationship with my scientific collaborator, geobiologist Dawn Sumner, there is a network of potential contributors including every researcher who works in the facility. This talk uses the experiences and challenges of the project as a way of thinking about collaborative processes in general,and as a way of finding creative gates in the fences between public/private, objective/subjective, traditional media/new media, and scientific/artistic forms of investigation.

    THEME
    How to collaborate with scientists

    OBSERVATION
    Take Me To Your Dream (Dream Vortex) is an artistic experiment with many layers of collaboration.

    WHAT PROMPTED OBSERVATION?
    In addition to the primary relationship with my scientific collaborator, geobiologist Dawn Sumner, there is a network of potential contributors including every researcher who works in the facility.

    TOPIC
    This talk uses the experiences and challenges of the project as a way of thinking about collaborative processes in general

    TOPIC MOVES FROM A TO B
    Finding creative gates in the fences between public/private, objective/subjective, traditional media/new media, and scientific/artistic forms of investigation.


A funny thing happened on the way to the millenium: The world went digital. Prophets had predicted for years that a single new digital medium would replace all the old analog media. What had been ink and paper, photographs, movies, and TV, would become just bits. Well, the Great Digital Convergence happened. It crept upon us unannounced, but it's here. This talk heralds that signal moment, a massive change in our culture. The elementary particle of the revolution is the much misunderstood pixel. The talk tackles head-on the fundamental mystery of digital-that spiky represents smooth, that the discrete stands for the continuous. How can that be? The full message is an explanation of how the whole digital world works and why it deserves our trust. The beginnings go back two centuries to a man who was almost beheaded and knew Napoleon too well. And to early last century when a Russian scientist, unknown to most Americans, defined the pixel while managing to stay out of the Gulag under the protection of a brilliant woman married to one of Stalin's bloodiest henchmen.

    THEME
    The talk tackles head-on the fundamental mystery of digital

    OBSERVATION
    Prophets had predicted for years that a single new digital medium would replace all the old analog media.

    WHAT PROMPTED OBSERVATION?
    It crept upon us unannounced, but it's here.

    TOPIC
    The full message is an explanation of how the whole digital world works and why it deserves our trust.

    TOPIC MOVES FROM A TO B
    The beginnings go back two centuries to a man who was almost beheaded and knew Napoleon too well. And to early last century when a Russian scientist, unknown to most Americans, defined the pixel while managing to stay out of the Gulag under the protection of a brilliant woman married to one of Stalin's bloodiest henchmen.


Black hole and cosmological horizons play a crucial role in physics.They are central to our understanding of the origin of structure in the universe, while continuing to provide vexing theoretical puzzles. They have become accessible observationally to a remarkable degree, albeit indirectly. I will review how horizons appear in general relativity and quantum field theory. Then I will move to a systematic study of their breakdown and its relevance -- or more precisely, `dangerous irrelevance' -- to thought experiments and real observations in specific situations. After describing the sensitivity of primordial cosmological perturbations to heavy degrees of freedom and large field values, I will share some results exhibiting the breakdown of effective quantum field theory for string-theoretic probes of black hole horizons.

    THEME
    Thought experiments compared to observations of black holes

    OBSERVATION
    Black hole and cosmological horizons play a crucial role in physics.

    WHAT PROMPTED OBSERVATION?
    They are central to our understanding of the origin of structure in the universe, while continuing to provide vexing theoretical puzzles. They have become accessible observationally to a remarkable degree, albeit indirectly

    TOPIC
    I will review how horizons appear in general relativity and quantum field theory.

    TOPIC MOVES FROM A TO B
    I will move to a systematic study of their relevance to thought experiments and real observations in specific situations.

2017-06-01 17:20:13
finished analysis of the provided abstracts, now I'm ready to write my own. Its going to clear up my own thinking too I expect.


2017-06-01 19:08:44
still thinking



Gary Boodhoo combines video games with machine learning to create interactive science fiction. He invents artificial experiences.

Deep Dream Vision Quest is a video synthesizer that creates multiplayer hallucinations. Live cameras reveal the world to a neural network which progressively misunderstands what it sees. Choosing between the front facing or back facing camera turns the AI dream into a mirror or a window.


note to self before I forget. Anyone who's ever wanted to "learn to code" needs to experience this moment to truly get it. The stakes seem so high to me right now, and looking back, I've put so much of myslef into understanding this idea and how to realize it. Learning python has been a big part of that. I didn't realize how beautiful the language is. Truly, its like Elvish. But right now - thinking through the trial and error of passing functions and parameters as part of a "program" that drives my artwork is the most challenging computer science ever. Its bitter to know that you could have done it differently, that you didnt understand something the way you thought, or that  you are almost certainly missing out on a basic concept, knowledge of which would make the current impasse invisible. Still - I'm hacking my waty to the solution, and its happening right now!

Experience an interactive psychedelic journey within a computer interface. Using the DeepDream convolutional neural network algorithm and real-time video feedback, the system turns your image into a vision of its own thought processes--a magic mirror. Questions about DeepDream, the magic mirror setup, and the spirit realm inside the machine are all welcome. Attendees will leave with an understanding of how neural networks may be used for image synthesis

Attendees will leave with an understanding of how neural networks may be used for image synthesis, and specific steps for creating their own Deep Dreaming Magic Mirror.

When I saw "Find Your Spirit Animal In A Deep Dream Vision Quest" - I quietly hoped I would meet someone that I could talk to. I sometimes yearn for belonging, but I refuse to shapeshift just to fit into someone else's tribe.

We found them by showing the world to a neural network through a live camera

Our interactive video installation shows the world to a neural network through a live camera. Clusters of artificial neurons light up when the network recognizes features it has learned before. Using Google's Inceptionism method, we synthesize imagery (dreams) from neural signals. We loop these graphics and project them back into the installation space.

But, until the camera detects movement in the space, the computer dreams about the last thing it saw. The audience and the environment dissolve. Strange creatures emerge from a familiar landscape. Only in stillness are they visible to us, only in motion are we visible to them.

I've presented living machine hallucinations to audiences for the past year as a way to share my own reactions to creative AI. It is still unclear where the intelligence emerges and where it ends. The best moments are when the environment itself seems to have an agenda. It wants to turn you into a kind of reptile. It wants to find ghosts(!) That's science fiction theatre, but is it a mirror or a window?

This talk answers the question, “where do the images come from”, “why these images are important”, “where do these feelings come from”,”I can’t take my eyes off it. Why?”, What is the meaning?

For show and tell,
- it uses a series of computed portraits with imagery produced by my Deep Dream Vision Quest neural video installation.
- full setup with magic mirror
- projected setup

What have I discovered from live shows
- people matter
- staging and setting matter
Where does the data come from and who owns it?
What do I get out of it?
Applications
- entertainment
- therapy
- outreach
- surveillance
- roleplaying

Talking Points

We live in a hyper modern world where things blur together, the categories are blending together.

What does human mean now? The Othering. To be Other.


One of my parent's friends asked me about the AI in his camera. The one that makes the video look like a painting. How is that app different than my work?



Why I've presented living machine hallucinations to audiences for the past year.
    - I seek to surface the stories that lies submerged underneath vision
Why?
    - To better understand the images I respond to and prepare for consumption
Why?
    - To recognize the alien as familiar, and to recognize how alien the familiar is

Why
Because there are Universal Images
Why
They resemble the classifications of a neural network
Why
The underlying behavior of learning machines must be universal
Why
Because the algebra and the architecture is the same

Therefore:
All perception begins as hallucination
Mental images from activated neural patterns  project outward as iterations in a feedback loop of recognition-reclassification
Neural patterns?
Yes. Archetypes. Geometric memories.  Arrays of filters.
Projected from where?
The Center
What is at the center?
Me. I am hiding something

What are some of the themes common to this imagery
Repetition
Embellishment
Replacement
Structure
Autocompletion
Suggestion
Shorthand
Radial Symmetry
Scale

2017-06-01 21:54:59
lots to think about

THEME
Where do the images come from?



OBSERVATION


WHAT PROMPTED OBSERVATION?
One of my parent's friends asked me about the AI in his camera. The one that makes the video look like a painting. How is that app different than my work?

TOPIC
Why I've presented living machine hallucinations to audiences for the past year.

Well? Why did you do it?


TOPIC MOVES FROM A TO B


Well? Why did you do it?
Fame, glory, getting out of my comfort zone, curiosity

Why did you keep on doing it?
The code kept getting better and suggesting new directions. When people saw it, their reactions suggested new ways of coding and presenting. Their reactions included silence and pantomime. I saw an opportunity to shape these behaviors further with new code and stagecraft. I continue to search for ways to extend the moments of surprise and extend them into meaningful experiences. I've always maintained the fiction that this was some kind of videogame, until it became a truly reactive system. As I've shown it, I have observed that some people just "get it" more than others. The repeated but hallucinatory patterns that emerge in response to activity in front of the camera changes that activity. Currently I see this kind of feedback loop iterating (recursing) 2-3 times. Someone does something and sees it multiplied on screen, they pose and point at the screen and the image continues to change. They learn to shift their posture and play with the camera (which to my surprise) has turned out to be a hugely responsive game controller.

What does it do?
The video installation shows the world to a neural network machine through a live camera. The machine reconstructs what it sees. We project that image back into the installation space. Until the machine detects motion, it dreams about the last thing it has seen. With each uninterrupted dream cycle the transformation of this memory becomes more extreme. Strange creatures emerge from alien landscapes. Only in stillness are they visible. They fade away when you move. This reflective "hurry up and wait" quality provides the basis for emergent gameplay.

Why did you make it?
A year later, It is still unclear where the intelligence emerges and where it ends. The best moments are when the environment itself seems to have an intention. It likes some things, and perhaps some people more than others. It wants to turn you into a kind of reptile. It wants to find ghosts(!) That's science fiction theatre, but why is it so easy, and is it a mirror or a window?

2017-06-02 10:38:35
I've generated several schematics for potential talks. Here they are


#
    THEME
    Hacking the solution

    OBSERVATION
    Anyone who's ever wanted to "learn to code" needs to experience this moment to truly get it.

    WHAT PROMPTED OBSERVATION?
    The trial and inference of passing functions and parameters as part of a "program" that creates artwork is the most challenging computer science ever.

    TOPIC
    How I use neural network machines to make pictures

    TOPIC MOVES FROM A TO B
    I've presented living machine hallucinations to audiences for the past year as a way to share my own reactions to creative AI.

#
    THEME
    Where they come from

    OBSERVATION
    I seek to surface that which lies submerged

    WHAT PROMPTED OBSERVATION?
    One of my parent's friends asked me about the AI in his camera. The one that makes the video look like a painting. How is that app different than my work?

    TOPIC
    How I use neural network machines to make pictures

    What I've learned from presenting machine hallucinations to humans and living rooms for the past year.

    TOPIC MOVES FROM A TO B
    I've presented living machine hallucinations to audiences for the past year and am discovering a design language to extend moments of surprise into meaningful experiences



make the theme more active:
Where they came from

// doing something. Finding
Find your spirit animal in a deep dream vision quest

Deep Dreams, memories and confessions

Conspiring to uncover a universal interface

Confessions of a universal interface

finding the universal interface to the memory palace

Finding the universal interface to legacy reality

Uncovering their tracks

Hunting for a universal interface

Uncovering rituals with widespread deep dreaming

Improving the quality of ritual interfaces for humans

Deep Dreams, high scores and epic dread

High sco


Deep Dreams, Omens and Premonitions.

Sharing memories with machine intelligence

Deep Dream, Ritual Interface
Deep Dream, Ritual Interface to the Library of Babel


Machine Learning teaches us something amazing. It doesn't take much to invent the world. Any technology capable of recognizing images must also create them. Wherever we find aliens they'll be artists too.



2017-06-03 12:03:24
What's not being said:
My experiences over the years with an intense lucid dream where I asked Jesus to help me.
My experiences with psychedelics, specifically the reality that DMT uncovered.
Any mention of legacy reality


It's not that I seek to uncover the submerged. It's that the visual memories shared by machines and people conspire to uncover the truth of a universal interface.

The surprising emergent property of hyperplatonic digital is archaic dreamtime. Everything, everywhere is an event horizon, infinitely receding and
The visual memories shared by people and machines conspire to reveal universal images. The kinds of images that build dreams and over time build civilizations. The design space is a metaphor that constructs legacy reality.
[example ]

Legacy Reality means the kind of reality that can be sensed with a camera. An electromagnetic field really. Functionally this is the source of the datasets a visual intelligence can learn to classify.

Hallucination means that the memories of Legacy Reality are reconstructed visually, in a feedback loop, running on any hardware capable of representing a large enough array of summed multiplication. Like a visual cortex, and also like a GPU.

2017-06-03 17:02:57
Wherever we find aliens they'll be artists too.

can Alien be removed from this statement, while preserving the intent? Its too much of a shortcut. I don't like how its becoming a default word.

Wherever we find ourselves, we'll be artists
When we find ourselves we'll be artists
arists find selves wherever they are
The


The eye as transmitter is found worldwide, as is a prohibition against staring at people.

Even in our society you don’t look directly at someone for any length of time without speaking. People in prison avoid eye contact since it’s seen as an aggressive act.

Young children believe that the eye is a transmitter and that the eye beams of people can mix or clash.

In the comics, Superman is able to heat a hotdog or open a safe with his eye beams.

The eye objectifies, which is why we speak of “sex objects”. Not enough attention has been given to the way in which cultures train people to use their senses.

In medieval times the dictum was “fides ex auditu” (faith comes from hearing) but by the Renaissance the Protestants were reading the Bible.

Another medieval dictum was “nil intellectu quod non prius in aliquodo modo in sensibus”. There is nothing in the mind which is not first, in some manner, in the senses.

2017-06-03 17:19:53
1st draft

    THEME
    The memories shared by machines and people conspire to uncover universal images. Where do they come from?


    OBSERVATION
    It doesn't take much to invent the world. Any system capable of recognizing images must also create them.


    WHAT PROMPTED OBSERVATION?
    As I coded variations on the feedback loop used to create pictures, I soon realized that people were completing the synthetic images with their own memories and expectations. Perception must be a kind of hallucination derived from universal images which are mirrored by the latent space of a neural network.


    TOPIC
    The surprising emergent property of Big Data is the archaic dreamtime we remember from 50000 years ago.


    TOPIC MOVES FROM A TO B
    I've presented living machine hallucinations to audiences for the past year and in that time discovered a generative design language to extend moments of surprise into long term meaningful experiences

what's missing?
no reference to cargo cult of machine intelligence. The imagined internal life of a machine intelligence is so much bigger than the machine intelligence. Is this just another way of expressing surprise that human beings seem much smarter than they need to be?

2017-06-03 18:30:44
does the topic involve the audience sufficiently?
what's so interesting about the archaic dreamtime then?
- we all share it at our most vulnerable
- animals share it too
- maybe it can also be found outside of a nervous system

what's important to my mom about the archaic dreamtime?
- it draws a line between the unknown and the unknowable
- it is the wellspring. Of spirituality, and maybe even hope
- the spirit of the age (legacy reality) is shaped by archaic dreams. What dreams may come aren't random, but rather, generative

Unpack that - reactive?
Like a computer UI, the recombinant spirit of the age isn't waiting for input, its always creating even when surrounded by darkness. Interfaces like this uplift the "user" into communion with the Unknowable, The Alien Other. The Electromagnetic Imaginary. The Mystery


Psychedelic AI space erotica
Psychedelic AI space invasion
Psychedelic AI space exploration

The psychedelic AI cargo cult of machine intelligence

Deep Dream, a psychedelic creative intelligence
Deep Dream Vision Quest for a

Psychedelic space invader

You know all those ancient aliens you hear about in the news? I'm the worst one.

Human encounters with a gregarious creative intelligence in quest of a universal interface

Quest for a universal interface

Quest for an automated dreamtime

deep dream vision quest for creative intelligence

Portraits of a gregarious creative intelligence

Machine Hallucination

Science Fiction Thriller

Cargo, Mana and Taboo

Deep Dream Cargo Cult

As such, commodity fetishism transforms the subjective, abstract aspects of economic value into objective, real things that people believe have intrinsic value.[1]

Millenarianism has been found through history among people who rally around often-apocalyptic religious prophecies that predict a return to power, the defeat of enemies, and/or the accumulation of wealth. These movements have been especially common among people living under colonialism or other forces that disrupt previous social arrangements.

A cargo cult is a millenarian movement first described in Melanesia which encompasses a range of practices and occurs in the wake of contact with more technologically advanced societies. The name derives from the belief which began among Melanesians in the late 19th and early 20th century that various ritualistic acts such as the building of an airplane runway will result in the appearance of material wealth, particularly highly desirable Western goods (i.e., "cargo"), via Western airplanes.



THEME
Memories shared by machines and people reveal universal images. Where do they come from?


OBSERVATION
It doesn't take much to invent the world. Any system capable of recognizing images must also create them.

The surprising emergent property of Big Data is an iteractive and archaic dreamtime.


WHAT PROMPTED OBSERVATION?
As I coded variations on the feedback loop used to create pictures, I soon realized that people were completing the synthetic images with their own memories and expectations. Perception is a kind of hallucination made up from universal images which are mirrored by the learned classifications of a neural network.


TOPIC
How I use neural networks to find pictures


TOPIC MOVES FROM A TO B
I've presented living machine hallucinations to audiences for the past year and in that time have discovered a design language to extend moments of surprise into long term meaningful experiences


THEME
Serendipity rewards stillness

OBSERVATION
AI in 2017 may be understood as a cargo cult (?)
[not uninteresting - but does it leads the conversation away from or towards the role of serendipity ]

WHAT PROMPTED OBSERVATION


TOPIC
How I use neural networks to find pictures



THEME
Serendipity



Dreams emerge from a process called gradient descent. Neural activity is added back to the picture that caused it. Thus creating a feedback loop which serves to make any detected features more like themselves. The software doesn't generate fully realized images all at once. Instead the neural network dreams repeatedly, building up a picture from nothing but statistics. Its incredible.

Deep Dream is a lens to reveal how visual concepts are represented by a learning machine. The computer simulates a vast cortical array whose geometry is called a neural network. Neural, because it is said to behave like a nervous system.


Neural networks come in different shapes and sizes. Deep Dream Vision Quest uses a popular implementation of Google's Inception architecture (like the movie) called GoogLeNet. It may come as a surprise, but the network doesn't contain images. It contains only habits. GoogLeNet was trained on over 1 TB of images, but is itself only 50 MB in size.

A
This is a story of a guy who saw on the internet and became curious about how they were made. He was a hacker and an artist and an on-again off-again Radical Platonist who wanted to put everything inside of a box

B
Decades of psionic research provided tantalizing hints. But what can you say about the Unspeakable?

Yes, he had faced UFO's and the creatures that drive them. He had regarded the reptile mammal insect plant entity inside himself with Dread and Awe. Most of all he was stubborn.

C
Showing it to people

As he coded variations on the feedback loop used to create pictures, he realized that people were completing the synthetic images with their own memories and expectations. Perception is a kind of hallucination made up from universal images which are mirrored by the learned classifications of a neural network.

Then he saw a ghost. He pointed the camera at the empty auditorium and turned around to finish setting up the equipment. Meanwhile on the television, something emerged from the vacant seats. Spirit animals, machine elves. The same hybrids

The machine dreams were alien but also familiar. The pictures it made apparently lack any logic beyond the amplified coincidences found in the source material.

identify your unique spin on a universal theme
I am an artist who uncovers the familar in the alien
I am the oldest son who welcomes the stranger
Under my blanket I found a spider
Th

2017-06-10 22:03:24
I just want to talk about the work I'm currently doing and what has led me to this point. The unexpected insight I gained along the way was that this technology can transform environments and change the way people behave.


Bio:
Gary Boodhoo combines video games with machine learning to invent interactive science fiction. He arrived in the United States from Jamaica along with the first personal computers determined to find or build a new world.
Millions of players around the world use the game interfaces he directed and designed for Madden NFL, The Sims, Star Wars: The Force Unleashed and The Elder Scrolls Online. Working as SKINJESTER, he helps creative organizations build humane software.

Title:
Deep Dreams, Omens and Premonitions
Human encounters with a gregarious machine intelligence

How is live machine hallucination different than the app on my phone

2017-06-11 13:16:52
You've not yet asked what the audience wants. I know my own motivations for wanting to present but why did that person sitting in front of me bother to come? How much can you find out about them?

WANT
Curiosity
The subject of machine learning fits into their view of the world
Desire to feel smart and share personal observations
They arrive with something they want to express about the subject although they may not have put it into words (its hard!) They came to be entertained. Show them how to get what they want. How do you know what they want?

They wanted to feel smart
They wanted to feel like their interest is validated
They want to learn - guide them through a step by step analysis of how

No one comes to these talks without an interest in the subject.
It may be that some people are figuring it all out themselves and are putting the presentation on a spectrum of what they know or assume

The importance of credibility
My credibility validates their interest

They came because they have an interest and want to see where my story fits into their personal narrative.

Some people just came to meet other people. Maybe make some kind of personal connection. Maybe find perspective.

No one goes to these things to judge me, and my big fear is that I'll be judged.

What parts of myself have I not shown?
- the arcane researcher who wants to know how it all works together
- the person who spent money to make it work faster
- I taught myself to do everything
What parts of myself has it felt best to share?
 - the arcane setup that kept evolving and led me to this moment, it was epic just making it work at all! Made me feel like a real hacker
I'm going to talk about something your parents and the clergy told you never to discuss in polite company.

If you don't think you're in sales, I want you to think about the last time you wanted sex...

In this fun and personal talk, Caroline shares a story of moving from stage-paralysis to expressive self. Accompanied by an unusual prop, she encourages us to use our voice as an instrument and really find the confidence within.



As I child I wondered if I'd seen everything a person could see. I wasn't jaded yet, but maybe everything to come would be just a combination of all the patterns I was already familiar with. I wondered - could there be images that no one had imagined yet?


In this talk, Gary shares a story of how he befriended an intelligent machine and became an artist again.  Learning to code in Python was the gateway


 We train the neural network to recognize images and then "run it backward" by amplifying the signals it makes during image recognition and adding them back to the image it attempts to recognize. This leads to wild visual feedback which to us appears as a "machine hallucination". Yet how interesting it is that these hallucinatory images resonate with our own internalized visual language. The expression of which has resonated throughout human history in our cave art and our dreams. As soon as I connec

In traditional computing decisions are yes/no, true/false affairs. Neural computation is a bit different. Instead, decisions emerge from a little more of this, a little less of the other thing. Choices are more like habits. Learning then, is the process of adjusting all the biases so a neural network gets into the habit of recognizing new input. Machine learning is the art of getting it to do this on its own.



An alien intelligence surrounds us. Even now, in this very room.

To achieve these results we've constructed artificial memories that represent more than just data, they are a model of nervous systems work.

We call them neural networks.

By doing so, we gain a better understanding of how our own minds work. Specifically, how do we understand what we see.




Machine learning show how to extract intelligence from the environment. The underlying assumptions of a learning machine are shaped by its training. Neural networks have habits, and with the right training they can get into the habit of recognizing spam email or the habit of avoiding pedestrians

Image classification and the deep Dream algorithm are both deterministic. Given the same image, the machine will draw the same hallucination every time. But the world is less deterministic than the model. Showing the outside world to the network with a live camera, the input is never the same.

2017-07-11 00:26:43
getting hung up on the background section
- deep dream
- style transfer








The software doesn't generate fully realized images all at once. Instead the neural network dreams repeatedly, building up a picture from nothing but statistics.

2017-06-13 13:26:54
LASER Talk Summary:

HUMAN ENCOUNTERS WITH A GREGARIOUS LEARNING MACHINE

Suddenly, computers are good at seeing and understanding. Learning machines have arrived, bearing unexpected cargo. The surprising truth behind artificial intelligence is that Mind emerges from the environment.

In 2015 a team at Google led by Alexander Mordvintsev released the first "Deep Dream" images to an amazed internet. These were instantly recognizable as photographs of the psychedelic experience. The algorithm is a dozen lines of code. It exaggerates a provided picture using habits the machine has learned.  It's a deterministic process. For any given image, the machine constructs the same hallucination every time.

I create video installations that show the world to a learning machine through a live camera. Deep Dream Vision Quest is a neural image synthesizer that creates multiplayer hallucinations. Although the algorithm is predictable, the world is not. At live performances I'm often asked where the images come from. I've come to recognize how easy it is for humans to complete them with our memories. In this talk I describe how I use stagecraft, creative coding, and game design to make pictures of Minds.


2017-06-13 14:16:21
TITLE:
Human encounters with a gregarious machine intelligence

[identify your unique spin on a universal theme]
THEME
universal: what is the nature of perception?
A mirror is a mask that looks at you

OBSERVATION
Intelligence emergences from the environment

PROMPT
The same program that identifies spam in your inbox can also identify a pedestrian in your car. Machine learning is the study of how to generalize information efficiently. Big Data

TOPIC
How I use neural networks to find pictures

TOPIC MOVES FROM A TO B
I've presented living machine hallucinations to audiences for the past year and in that time have discovered a design language to extend moments of surprise into long term meaningful experiences


This time, with proofreading. Thanks Piero. G

LASER Talk, 11 July 2017

Human Encounters With a Gregarious Learning Machine

Suddenly, computers are good at seeing and understanding. Learning machines have arrived, bearing unexpected cargo. The surprising truth behind artificial intelligence is that Mind emerges from the environment.

In 2015 a team at Google led by Alexander Mordvintsev released the first "Deep Dream" images to an amazed internet. These were instantly recognizable as photographs of the psychedelic experience. The algorithm is a dozen lines of code. It exaggerates a provided picture using habits the machine has learned.  It's a deterministic process. For any given image, the machine constructs the same hallucination every time.

I create video installations that show the world to a learning machine through a live camera. Deep Dream Vision Quest is a neural image synthesizer that creates multiplayer hallucinations. Although the algorithm is predictable, the world is not. At live performances I'm often asked where the images come from. I've come to recognize how easy it is for humans to complete them with our memories. In this talk I describe how I use stagecraft, creative coding, and game design to make pictures of Minds.

2017-06-25 16:55:26
Bringing Deepdreamvisionquest.com site into the modern era again. Working out details of the upcoming LASER talk

2017-06-25 17:43:45
Questions:P

Where does the idea that neurons are the basis of the Mind come from? Is it true?

Expressive mode, regenerative mode

2017-06-25 18:04:20
Shifting focus back to immediate needs of the website. What's missing here?
Wht prevents me from sharing this w peers, colleagues, new contacts> Obviously insecure about missing something

2017-07-08 17:03:27
working on the presentation now.
computer at the facilities is a macintosh with keynote and powerpoint installed
- test inclusion of local video content in a powerpoint doc
- do this work on the mac


2017-07-08 17:57:33
Shifted to MacOS and looking thru keynote
Installing Powerpoint here as well


2017-07-08 18:15:46
Artists frequently focus only on their own work as if it happened in a vacuum, while the audience really likes to place it in a context; sacrificing 10 minutes of the 20 for a survey of the field is worth it: they will appreciate the following 10 minutes a lot more. One of the rare standing ovations at a LASER talk was given to Robert Buelteman, who managed to tell the story of photography from the beginning to his own work in 20 minutes. I bet all the people who heard that talk still remember it to this day.


2017-07-08 18:42:32
Human Encounters With a Gregarious Learning Machine




2017-07-09 15:51:24
after touching it for a while yesterday, I've determined the structure of the presentation

Presentation structure

Start at the end first with a montage

These are my outcomes
- Art 1
    - Style transfer series
- Art 2
    - Pre-rendered
- Art 3
    - Live [postprocess]
- Art 4
    - Live [encounter loop]

How it began
- What is a neural network?
- They only see what they have learned to see and we feel the same.
- Show misidentification
- Misidentification in nature
- world of faces
- Show hallucination of imagenet class
- What is deep dream?
    - Show example
- What is style transfer?
    - Show example


Something is missing
Live Camera
- People
    - Too much emphasis on the learning machine.
    - Not enough emphasis on how people react to the machine
- The Environment
    - Live camera
    - Infinite diversity of the real world no matter how mundane

I found the missing thing

Multiplayer hallucinations
- Social encounters
- The environment contributes far more than the technology
- Stagecraft
    - Crafting how the experience is presented in social spaces
    - Mounting a 50” TV vertically did 2 things
        - Participants stand close to it like a magic mirror
        - Participants slow down
        - The generative images read more like a painting than a TV

What happens next?
- Its not an app, its an encounter
- Broaden audience
    - Storefront installations
    - Trade Shows
    - Hotels
- Interdisciplinary collaboration
    - Dancers
    - Actors
    - Musicians
- Projection on architecture
- Smart cameras
    - Drones
    - Depth sensing
- End with a call to action


2017-07-10 10:45:05
- slides: deep dream description
- slides: style transfer description


2017-07-11 03:44:21
Comnpleted 1st draft presentation


2017-07-11 11:38:46
collecting talking points


2017-07-11 14:43:50
rehearsing


2017-07-11 15:50:16
getting better

University of San Francisco 
2130 Fulton Street 
SF, CA 94117 
Fromm Hall - Berman Room 
2130 Fulton Street, San Francisco, CA 94117-1080 


Ville-Matias Heikkilä
www.youtube.com/watch?v=UFVB5rnqjyY


2017-07-12 08:11:29
Presentation last night was a success.


2017-07-12 09:08:04
LASER Talk Presentation Notes
also add these to squarespace as notes

Presentation structure

Start at the end first with a montage

These are my outcomes
- Art 1
    - Style transfer series
- Art 2
    - Pre-rendered
- Art 3
    - Live [postprocess]
- Art 4
    - Live [encounter loop]

How it began
- What is a neural network.
- Training and Classification
- Misidentification (and interpretation)
- Deep Dream
- Style Transfer


- They only see what they have learned to see
- Training and classification
- ImageNet
- Show misidentification
- Misidentification in nature
- world of faces
- Show hallucination of imagenet class

- What is deep dream?
    - Show example. What about this example interests me?
- What is style transfer?
    - Show examples. What about this example interests me?


Something is missing
Live Camera
- People
    - Too much emphasis on the learning machine.
    - Not enough emphasis on how people react to the machine
- The Environment
    - Live camera
    - Infinite diversity of the real world no matter how mundane

I found the missing thing

Multiplayer hallucinations
- Social encounters
- The environment contributes far more than the technology
- Stagecraft
    - Crafting how the experience is presented in social spaces
    - Mounting a 50” TV vertically did 2 things
        - Participants stand close to it like a magic mirror
        - Participants slow down
        - The generative images read more like a painting than a TV

What happens next?
- Its not an app, its an encounter
- Broaden audience
    - Storefront installations
    - Trade Shows
    - Hotels
- Interdisciplinary collaboration
    - Dancers
    - Actors
    - Musicians
- Projection on architecture
- Smart cameras
    - Drones
    - Depth sensing
- End with a call to action

——
Dictionary
ILSVRC12
Is a subset of the ImageNet database used for a popular machine learning challenge in 2012. Sometimes just referred to as ImageNet - as in “trained on ImageNet”

Some Facts
Neural Networks have been successfully applied to a wide range of data-intensive applications
Source: http://www.alyuda.com/products/forecaster/neural-network-applications.htm

Finance
Stock Market Prediction
Credit Worthiness
Credit Rating
Bankruptcy Prediction
Property Appraisal
Fraud Detection
Price Forecasts
Economic Indicator Forecasts

Medicine
Medical Diagnosis
Detection and Evaluation of Medical Phenomena
Patient's Length of Stay Forecasts
Treatment Cost Estimation

Operations
Process Control
Quality Control
Retail Inventories Optimization
Scheduling Optimization
Managerial Decision Making
Cash Flow Forecasting
Scheduling

Science
Pattern Recognition
Recipes and Chemical Formulation Optimization
Chemical Compound Identification
Physical System Modeling
Ecosystem Evaluation
Polymer Identification
Recognizing Genes
Botanical Classification
Signal Processing: Neural Filtering
Biological Systems Analysis
Ground Level Ozone Prognosis
Odor Analysis and Identification

Education
College Application Screening
Predict Student Performance

Data Mining
Prediction
Classification
Change and Deviation Detection 
Knowledge Discovery
Response Modeling
Time Series Analysis

Sales
Sales Forecasting
Targeted Marketing
Service Usage Forecasting
Retail Margins Forecasting

Human Resources
Employee Selection and Hiring
Employee Retention
Staff Scheduling
Personnel Profiling

Energy
Electrical Load Forecasting
Energy Demand Forecasting
Short and Long-Term Load Estimation
Predicting Gas/Coal Index Prices
Power Control Systems
Hydro Dam Monitoring

Machine Vision
Animation
Art
Automated vehicles
Facial Recognition
Object and Scene Recognition
Photography
Robotics



2017-07-12 09:26:59
working on LAST Festival blog post


2017-07-12 10:00:38
CODAME slides for Matchbox Talk due 7/14, presentation is on 7/20 *next Thursday)

3 minute artist talk: Randy Reyes + Gary Boodhoo. After investigating each other for a week, we meet for the first time and present 10 "facts" in 3 minutes. Happy hour after.




2017-07-17 08:15:22
put together a map for talk about Randy.
Estimated 7hrs to completion of this project


2017-07-20 08:25:17
completed final edit for slides last night
- confirm w Jordan that he's seeing them
- notes
- rehearsal


2017-07-20 08:25:55
spending this am updating deepdreamvisionquest.com


2017-07-21 10:50:21
still minor tweaks for presentation quality, getting to the content in a moment. Yesterday's attempt was wrong, but enough so to point me in a better direction.

https://vimeo.com/190130949
LAST Festival + Paseo Public Prototyping Festival

.video-caption-wrapper


2017-07-22 17:36:15
significant cleanup of home page
added assets to blog post - remains interesting or at least reads well with a much longer stack of images than expected


2017-07-28 17:59:15
working on LAST Festival blog post. finishing!

deep dream vision quest



2017-07-28 18:41:51
created FB public page with this title:

Deep Ḏ̶̨͆̈́r̴̤͒e̵̱̍a̶̕͜͝m̵͎̭̏̄ ̴̬̑ͅV̶̱̌̃i̴̫̙͂s̷̈́͜i̴̱͐ò̷̪n̶̥̲͂ Quest



2017-07-29 19:15:43
completed 1st pass content curation for LAST Festival blog post. Much longer than expected - still too long, but surprising to find that the length isn't such a limiting factor when most of it contains big pictures and videos



2017-07-31 12:42:26
good 2nd pass of LAST Festival blog post
1 more editorial pass before applying this template to the ARTEX blog post


2017-07-31 17:57:06
this worksession
apply template to ARTEX blog post

next worksession
create Eventbrite exhibition invite


2017-08-01 16:12:31
1st pass for ARTEX post
needs further curation of images


2017-08-01 22:14:05
further curation of ARTEX images


2017-08-02 07:14:09
culled some of the images posted last night


2017-08-02 17:43:15
curated images for ARTEX post and added editorial
This is a reasonable stooping point
moving on to the GDC post
Game Developers Conference 2016


2017-08-06 14:54:44
completed 1st pass for GDC conference post


2017-08-02 18:44:32
An appropriate MLA citation would read:
Smith, John. "My Conference Speech." 2013 English Professor's Convention. UCLA, Los Angeles. 30 May 2013.

Boodhoo, Gary. "Find Your Spirit Animal in a Deep Dream Vision Quest." 2016 Game Developers Conference. Moscone Convention Center, San Francisco. 18 March 2016

A citation for the same event presented in APA style should be formatted:
Smith, John. (2013, May). "My conference speech." Paper presented at 2013 English Professor's Convention, Los Angeles, CA

Boodhoo, Gary (2016, March). "Find your spirit animal in a deep dream vision quest." Poster and technology demo presented at 2016 Game Developers Conference, San Francisco, CA



2017-08-03 14:55:02
Tease
Gary Boodhoo combines videogames, machine learning and interaction design into emotional sci-fi experiences. His project, Deep Dream Vision Quest, shows the world to a neural network through a live camera. Is it a mirror or a window?

Creative
Humane interface design for videogames and other shared hallucinations. Hacker. Dreamer. Typophile.

Corporate
Gary Boodhoo combines videogames and machine learning into dramatic interactive sci-fi experiences. Born in Jamaica, he arrived in the United States at the same time as the personal computer. A game industry veteran, his work examines roleplaying and transformation in digital environments. He's been a design lead on some fun games including Madden NFL, The Sims, Star Wars: The Force Unleashed and The Elder Scrolls Online. He lives in San Francisco where his company Skinjester, Inc. provides direction and design for creative clients.



Gary Boodhoo combines video games and machine learning to create interactive science fiction. A Jamaican-born industry veteran, millions of players around the world use the interfaces he invented for games including Madden NFL, The Sims, Star Wars: The Force Unleashed and The Elder Scrolls Online. He speaks regularly about learning machines and i and gameHis artwork has been exhibited at The Game Developers Conference and at festivals in the San Francisco Bay Area. His design studio skinjester, inc. helps organizations build humane software.



Gary Boodhoo combines videogames and machine learning to create interactive science fiction. A Jamaican-born industry veteran, millions of players around the world use the interfaces he invented for games including Madden NFL, The Sims, Star Wars: The Force Unleashed and The Elder Scrolls Online. His work examines how digital environments overlap real ones.


2017-08-03 14:55:22
decided to push pack the LIVINGROOM show to 1st weekend of September. There, its easier to talk about now. I've spent tim playimng with Eventbrite and I think that by using a private invite + sharable link, I'll be able to do 2 things:

1. share the link easily on any channel
2. track responses from a single place
3. create rich media presentation for the event


2017-08-04 00:36:24
put a bit of UX and iteration into the event invitation. Have set the sghow date to September 9 as Burning Man happens the previous week


2017-08-04 10:35:48
creating another test event with what I practiced yesterday


2017-08-06 09:48:10
back to the website for a bit today
finalizing the GDC event post
2016/7/11/dreaming-at-gdc-2016
2016/11/11/codame-artificial-experiences-2016
2017/5/28/life-science-art-technology-festival-2017
2016/11/upcoming-artificial-experiences-2016


2017-08-06 10:21:47
fixed some legacy URLS for blog posts


2017-08-06 16:09:30
completed 2nd pass of GDC post


2017-08-10 15:45:30
worksession goals:
convert index page titles to URLs
rewrite LEARN MORE section

2017-08-10 17:40:55
inject into footer
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js">
 </script>
 <script>
 $(".parallax-item[data-url-id=URL'] .page-title").wrap("<a href='/page'></a>");
 </script>

 looks like this
 - finds a collection of (1) parallax item with specific parameters
 - wraps each item in the collection with <a href=''></a> where href points to destination

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
<script>
$(".parallax-item[data-url-id='life-art-science-technology-festival-2017'] .page-title").wrap("<a href='https://www.deepdreamvisionquest.com/cms/2017/5/28/life-science-art-technology-festival-2017'></a>");
</script>

2017-08-10 18:07:18
works.

2017-08-10 18:37:38
page tweaks - image height. re thought CTA text in description.
See More. Such and such
Learn More. such and such
Collaborate
Contribute
Exhibition

2017-08-11 19:03:10
for this next worksession how can I make the most progress?
when to be sending out those invitations? now seems like a good time

2017-08-12 18:40:28
https://www.deepdreamvisionquest.com/cms/2016/11/11/codame-artificial-experiences-2016

https://www.deepdreamvisionquest.com/cms/2016/5/28/dreaming-at-gdc-2016

2017-08-13 00:08:47
spending a lot of time on responsive layout refinement. best layout yet, but content is not organized properly. started making a content map in powerpoint to define further and for comparitive analysis of a few other sites.

for this worksession:
start first pass on Deep Dream Vision Quest post

2017-08-13 14:02:26
there's an issue w the page footer layout needing further attention after the changes I made last night. mot sure what it is, possible a Safari-specific problem?


2017-08-13 14:53:09
not obviously a Safari problem. Seeing no issues there in developer tools, etc. Only seeing the problem on my phone


2017-08-13 15:42:53
cleaning up buy crowns ax document


2017-08-13 16:24:12
working in the browser. why are these offers so big?
- to contain the Platform CTA

what if the platform CTA was decoupled from the offers - just a modal dialog that appeared on selection?
- provides uniform treatment of platform icons (they fit the screen instead of the wrapper)

what do the wrapper look like smaller?


2017-08-13 16:54:06
this page can be designed differently. should be. but I don't want to get caught up in advanced surgery


2017-08-13 17:23:46
removal of T0 header
addition of page title from guide/news page
full screen bkg cover

this looks fantastic in an iphone6 viewport
plausible in an ipad layout (needs responsive text sizing)
desktop view needs work
- offer slots are too wide


2017-08-14 17:48:09
some oddness related to the footer issue. it goes away if I open a linked video from the gallery.
returning to the previous page (using the back gesture) shows a normal footer there as well
the issue returns after a page load

2017-08-18 18:22:53
picking back up with writing for "Deep Dream Vision Quest, A Neural Synthesizer"

a neural synthesizer
a nostalgia synthesizer
a multiplayer hallucinator
a sentimental synthesizer

a hard-working video orchestra
An enthusiastic video synthesizer

An enthusiastic video instrument


A Dreamy Video Orchestra with an enthusiastic interface

Lean How we're maki
computers dream like animals
multiplayer hallucinations
Dream like an animal with a machine

learn how computers dream
What do computers dream about?



What do computers dream about?
What does a computer dream about?
What is a computer dream?
A dreaming machine
Machine dreaming
Is it a mirror or a window?
Why do machines dream?

The mysterious world of mechanical dreams

Welcome to a mysterious world of multiplayer hallucinations. Find out what machines dream about.

What do machines dream about? (It's people)
Finanother inside multiplayer hallucination
to a multiplayer hall


Multiplayer Hallucination

Find out why machines dream
What do machines dream about?
Why do machines dream?

Multiplayer Hallucinations and Mirror worlds.

When I showed the world to a neural network through a live camera, it misunderstood.

An interactive video orchestra that plays multiplayer hallucinations.

Why do machines dream so much?
Deep dream vision quest is an interactive video orchestra

Deep Dream Vision Quest is a neural image synthesizer that creates multiplayer hallucinations and turns dreaming into a shared experience.

I showed the world to a neural network through a live camera, it misunderstood.

2017-08-19 18:12:59
Finally got the tone for the editorial:


I showed the world to a neural network and it misunderstood.

Deep Dream Vision Quest is an interactive video installation that paints multiplayer hallucinations. See what I've learned so far.

2017-08-19 18:24:29
https://www.deepdreamvisionquest.com/cms/2016/1/1/deepdreamvisionquest-a-neural-image-synthesizer

2017-08-20 09:45:40
A Synthetic User Interface for Multiplayer Hallucinations


2017-08-21 09:20:09
I didnt expect tp be spending any time on this, but I've deconstructed the squarespace breakpoints to get better (understandable) control over the layout. I think I've got the sequencing I want now. Experimenting with that a bit more

2017-08-21 09:23:26
so, are the default values for everything the ones that get set in the style editor?

yes. they should be considered the site default for desktop views

2017-08-21 10:07:12
rethought the entire page layout to be blog-centered. Interesting approach that hadn't occured to me until now, and yet I feel its the right one. It makes the site navigation simpler, and increases the information density. there was not real value in exposing those index blocks as though they were "featured" or prioritized when there is so little blog content.

It also lets me simplify the top navigation and be explicit with the language.
Instead of "Home" and "about"
it is "Project" and "Artist"

2017-08-21 10:44:38
moving forward with this direction. closing out this worksession by adjusting responsive typography

2017-08-21 11:04:39
adjusting the title block

2017-08-21 11:14:48
great work session. so much better

2017-08-21 16:20:38
layout is poorly spaced, fixing

2017-08-21 17:10:17
much better now

2017-08-27 11:19:15
completed 1st draft for Deep Dream Vision Quest, a Neural Image Synthesizer
- create eventbrite invitation
- editorial pass for blog post

2017-08-27 13:18:40
worked on the About Deep Dream post, not yet first draft
started post about hardware spec, using material previously captured in One Note

System details for [[MULE]]

2017-08-27 13:54:52
added data and HTML table to Hardware post

2017-08-27 14:19:14
updated Deep Dream Vision Quest, A Neural Image Synthesizer post banner image - betterf ro sharing now

2017-08-31 11:27:36
fixed the display bug that was bothering the fuck out of me. seems like I can now display 2 cols in the event postings without layout breaking on my iphone

2017-08-31 11:34:04
fixed that. moving on needed to fix this, was becoming a strange attractor blocking evenything else. Hopefully no unforseen consequenses, custom CSS I added is a bit of a hack.

2017-08-31 11:57:38
working on the ABout post

Presentation structure



Start at the end first with a montage



These are my outcomes

Art 1
Style transfer series
Art 2
Pre-rendered
Art 3
Live [postprocess]
Art 4
Live [encounter loop]


How it began

What is a neural network.
Training and Classification
Misidentification (and interpretation)
Deep Dream
Style Transfer




They only see what they have learned to see
Training and classification
ImageNet
Show misidentification
Misidentification in nature
world of faces
Show hallucination of imagenet class


What is deep dream?
Show example. What about this example interests me?
What is style transfer?
Show examples. What about this example interests me?




Something is missing

Live Camera

People
Too much emphasis on the learning machine.
Not enough emphasis on how people react to the machine
The Environment
Live camera
Infinite diversity of the real world no matter how mundane


I found the missing thing



Multiplayer hallucinations

Social encounters
The environment contributes far more than the technology
Stagecraft
Crafting how the experience is presented in social spaces
Mounting a 50” TV vertically did 2 things
Participants stand close to it like a magic mirror
Participants slow down
The generative images read more like a painting than a TV


What happens next?

Its not an app, its an encounter
Broaden audience
Storefront installations
Trade Shows
Hotels
Interdisciplinary collaboration
Dancers
Actors
Musicians
Projection on architecture
Smart cameras
Drones
Depth sensing
End with a call to action


——

Dictionary

ILSVRC12

Is a subset of the ImageNet database used for a popular machine learning challenge in 2012. Sometimes just referred to as ImageNet - as in “trained on ImageNet”


2017-08-31 16:04:10
completed leading parapgraph. retooling for structuring this post like my LASER talk.

2017-09-01 10:21:55
further editorial work on the aboyut post. trying to tell my story better. advice is to stop fine tuning th edits and just get the words out.

2017-09-04 11:41:10
- complete 2nd draft of About post
- create event invitation

2017-09-04 12:02:39
the problem I'be having writying this is that I don't have an outline or a limit on the amount of text. I'm probably conmbining GOALS and TOPICS, when only the TOPICS are meant to be explicit.

GOALS
Who is this for?
What purposes does this serve
What is the outcome I want
	What happens after reading this?
How can I arrive at this content

TOPICS

2017-09-06 00:13:27
Is the LIVING.ROOM show going to be on 9/23 or 9/30
either date seems plausible. Probably best to provide a buffer between invite and event though?

23-7 = 16 days until == 2 weeks
30-7 = 23 days until == 3 weeks

The 30th is the target date

This worksession:
- create draft invitation

what are you waiting for before sending?
- completed About the Project blog post
- editorial pass for About Me section

2017-09-11 21:16:38
Did not use time efficiently on this an am pushing back to October. Feeling guilty and weird and unsure of myself. How willing am I to look closely at the most embarassing details and amplify them? I'm looking back at the previous invitation I'd composed. Surely this is worthwhile? Why am I hesitating so blatantly?


2017-09-11 22:43:05
constructing the Eventbrite invitation now


2017-09-11 23:36:42
1st pass editorial


I'm trying out some new work on humans

I'm running human trials on some new work

It works best with humans

You're invited to LIVING.ROOM, a domestic expedition into a gregarious learning machine.

It's a reactive video installation that uses artificial intelligence to make science fiction cave paintings.

Read more about the project and see what we've learned so far.


2017-09-12 10:18:27
completed the invitation text

I'm trying out some new work. On humans. You're invited! Please join me for LIVING.ROOM, an exclusive and perhaps, hilarious expedition into a gregarious learning machine. My video installation uses artificial intelligence to make science fiction cave paintings. Read more about what I discovered. See you on the other side.
deepdreamvisionquest.com


2017-09-12 14:35:43
testing out imagery for the invitatiion


2017-09-12 16:49:57
arrived at a good working candidate image.



2017-09-13 14:27:01
Ive made the event live for testing


2017-09-13 16:11:30
You're invited to LIVING.ROOM, a multiplayer dream for friends and colleagues. RSVP by completing the (mostly effortless) registration.


2017-09-13 16:48:07
Gary Boodhoo combines videogames and machine learning to create science fiction romance. A Jamaican-born UX designer, millions of players around the world use interfaces he's invented for games including Madden NFL, The Sims, Star Wars: The Force Unleashed and The Elder Scrolls Online. He recently teamed up with a gregarious learning machine; together they're making pictures of Minds.


2017-09-13 16:54:57
I'm trying out some new work. On humans. You're invited! Please join me for LIVING.ROOM, an exclusive and perhaps, hilarious encounter with a gregarious learning machine. This interactive video installation uses artificial intelligence and a live camera to make science fiction cave paintings | Read more about what I've discovered | deepdreamvisionquest.com

See you on the other side,
Gary Boodhoo


2017-09-14 07:42:54
invitation is looking pretty good
noticed that the registration confirm doesn't also describe the event
did not notice how to get back to the event page


2017-09-14 08:02:19
Your Links
Your Organizer URL: https://deepdreamvisionquest.eventbrite.com [change]
Share this event on Twitter: https://www.eventbrite.com/e/livingroom-registration-37833029610?ref=estw
YOUR EVENT URL

https://deepdreamlivingroom.eventbrite.com


2017-09-14 08:16:18
to post confirmation message is good
it can't redirect back to the event brite page because that gets locked out once youve registered with a personal invitation.
What if the personal invite wasn't needed and I sent the event link by email?


2017-09-14 10:09:06
You're invited to LIVING.ROOM, a personal encounter with a gregarious learning machine for friends and colleagues. Registration adds you to my guest list and you won't need a ticket to enter. Please indicate how many are expected in your party.


2017-09-14 10:12:59
Turning off invitation only enables viewing of the event page from the Registration confirmation email


2017-09-14 10:30:55
testing the invitation send/accept flow. I think I've got it. Need a better picture for the organizer portrait though


2017-09-14 10:51:44
Solid


2017-09-14 11:48:03
updated Trello
- why is the About post taking so long. Whatever you're doing with it now, do half as much.

2017-09-15 17:09:52
continuing with the About post


2017-09-17 13:08:19
simplify this:

CONCEPT INTRO
The smell of old books always awakens in me memories of a vast and archaic library. Vivid enough to read and vague enough to slip through my fingers each time. Until now.

TECHNOLOGY INTRO
In 2015 a team at Google led by Alexander Mordvintsev released the first Deep Dream machine hallucinated images to an amazed internet. These were instantly recognizable as photographs from inside the psychedelic experience. Enthusiastic communities formed around what these images were, how they were made, and how you too could make them. Just like fractal images from 20 years ago, Deem Dream and machine hallucination is a heroic journey into really important computer science hiding under pop culture and garish sentimentality.

PROJECT INTRO
It has never been easier to listen to artificial intelligence technology which silently reshapes the world. 
It has never been easier for you the become the artificial intelligence technology which silently reshapes the world


Don’t assume that thing too must also be superscience done somewhere else by other people. On the contrary, creative AI thrives on diversity. Its a drum circle not a classroom after all. Gregarious learning machines renew the same creative possibilities found in cave painting dreamtime virtual reality. Artificial Intelligence has arrived and its made of people. 

THEME
But what is Deep Dream? Its a computer program for generating archaic illusions from a visual database. Its all those Borges  stories where the original was indeed unfaithful to the translation. Deep Dream is the radicalized fiction of the quantified Self. 

EXPOSITION
Interested in cats? Showing the learning machine millions of cat pictures is all it takes to form the habit of finding them. Cat pictures show more than cats. They also describe cat owners and the places cats live. This extra information contributes a bias to the virtual representation of cat-space. Cats don't emerge from nothing. They're a combination of parts like tail, four legs, body and head. And those parts are a combination of smaller features. All images are fundamentally formed within a continuum of gradients and edges. This is what "cat" looks like inside a learning machine, and this is also the source of the machine's dreams. 

EXPOSITION
I create video installations that show the world to a learning machine through a live camera. Deep Dream Vision Quest is a framework for creating multiplayer hallucinations by amplifying the signals inside a neural network. Until the camera detects movement in the space, the computer dreams about the last thing it saw. The audience and the environment dissolve. Strange creatures emerge from a familiar landscape. Only in stillness are they visible to us, only in motion are we visible to them.

EXPOSITION
Given the exact same image and settings the neural net will always deam about the same thing. Although the algorithm itself is predictable, the world is not. Small changes to the input lead to endless novelty. I use stagecraft, creative coding, and game design to make pictures of Minds.

CONCLUSION
A year later, it is still unclear where the intelligence emerges and where it ends. The best moments are when the environment itself seems to have an agenda. It wants to turn you into a kind of reptile. It wants to find ghosts(!) That's science fiction theatre, but is it a mirror or a window? 

CONCLUSION
Machine Learning teaches us something amazing. It doesn't take much to invent the world. Any technology capable of recognizing images must also create them. Wherever we find aliens they'll be artists too. 


2017-09-17 13:13:24

What is Neural Art?
	- What is a neural network.
	- Training and Classification
		- ImageNet
		- Class Visualizatiions
	- Misidentification (and interpretation)
		- Deep Dream
		- Style Transfer
		- They only see what they have learned to see
		- Misidentification in Nature
			- world of faces
			- Show hallucination of imagenet class

Something is missing
	Live Camera
	- People
	    - Too much emphasis on the learning machine.
	    - Not enough emphasis on how people react to the machine
	- The Environment
	    - Live camera
	    - Infinite diversity of the real world no matter how mundane

I found the missing thing
	Multiplayer hallucinations
	- Social encounters
	- The environment contributes far more than the technology
	- Stagecraft
    	- Crafting how the experience is presented in social spaces
    	- Mounting a 50” TV vertically did 2 things
        - Participants stand close to it like a magic mirror
        - Participants slow down
        - The generative images read more like a painting than a TV

What happens next?
	- Its not an app, its an encounter
	- Broaden audience
    	- Storefront installations
    	- Trade Shows
    	- Hotels
	- Interdisciplinary collaboration
    	- Dancers
    	- Actors
    	- Musicians
	- Projection on architecture
	- Smart cameras
    	- Drones
    	- Depth sensing
	- End with a call to action


2017-09-17 14:01:41

TITLE:
Human encounters with a gregarious machine intelligence

[identify your unique spin on a universal theme]
THEME
What is perception?

OBSERVATION
Intelligence emergences from the environment

PROMPT
The same program that identifies spam in your inbox can also identify a pedestrian in your car. Machine learning is the study of how to generalize information efficiently. Big Data

TOPIC
How I use neural networks to find pictures

TOPIC MOVES FROM A TO B
I've presented living machine hallucinations to audiences for the past year and in that time have discovered a design language to extend moments of surprise into long term meaningful experiences



Human Encounters With a Gregarious Learning Machine

Suddenly, computers are good at perception. Learning machines have arrived, bearing unexpected cargo. The surprising truth behind artificial intelligence is that Mind emerges from the environment. These gregarious learning machines renew the creative possibilities and emotional gestures that appeared in the first cave painting virtual reality entertainment systems.

In 2015 a team at Google led by Alexander Mordvintsev released the first "Deep Dream" images to an amazed internet. These were instantly recognizable as photographs of the psychedelic experience. The algorithm is a dozen lines of code. It exaggerates a provided picture using habits the machine has learned.  It's a deterministic process. For any given image, the machine constructs the same hallucination every time.

I create video installations that show the world to a learning machine through a live camera. Deep Dream Vision Quest is a neural image synthesizer that creates multiplayer hallucinations. Although the algorithm is predictable, the world is not.


At live performances I'm often asked where the images come from. I've come to recognize how easy it is for humans to complete them with our memories. In this talk I describe how I use stagecraft, creative coding, and game design to make pictures of Minds.


2017-09-17 14:27:36
simnplify this

Suddenly, computers are good at perception. Learning machines have arrived, bearing unexpected cargo.

The surprising truth behind artificial intelligence is that Mind emerges from the environment.

My interest with machine learning arises from a certain sympathy for the computer when it gets the answer wrong. It should come as no  surprise that it misidentifies the starship Enterprise, when it never learned about Star Trek. But truly, the Enterprise-D is something like a vacuum cleaner, a hair dryer, a battleship and a CD player. The computer is merely wrong but together we arrived at poetry.


In 2015 a team at Google led by Alexander Mordvintsev released the first Deep Dream machine hallucinated images to an amazed internet. These were instantly recognizable as photographs from inside the psychedelic experience. Enthusiastic communities formed around these images and you too could make them. Just like fractal images from 20 years ago, Deem Dream and machine hallucination is a heroic journey into really important computer science hiding under pop culture and garish sentimentality.

I dream of projecting live hallucinations of architecture on to architecture

I dream of painting dancers in motion from the

My part in the robot uprising came from an unexpected willingness to meet them halfway.

In 2015 a team at Google led by Alexander Mordvintsev released the first Deep Dream machine hallucinations to an amazed internet. These were instantly recognizable as psychotropic fragments of a universal language. Enthusiastic internet communities formed around these images; how they were made, and how you too could make them. This was my introduction to a new story about artificial intelligence embracing the alien Other and radical anthropomorphism.


A new story of artificial intelligence that embraces the alien Other free from the assumption that there is nothing new under the sun.


2017-09-18 07:49:01
I'm almost at a 1st draft with the ABout post, Adding pictures may help minimize the text, which seems a bit verbose (although well written)

This was my introduction to a new story about artificial intelligence embracing the alien Other and radical humanity.


This was my introduction to a humane story about artificial intelligence.

---
It should come as no surprise that a learning machine misidentifies

--
(Remove date)
Accompanied only by the short caption “this image was created by a computer on its own”

--
psychotropic fragments of a universal visual language

--
This was my introduction to a gentler, more humane story about artificial intelligence.

--
But the cat pictures show more than cats. The environment around the subject--things that also appear in the pictures makes its own contribution to the They also show the environment around cats. Things that happened to be in the training imagery.

--
The extra unclassified information contributes a bias to the learning

--
A lower level within a convolutional neural network is learning about edges and directions

--
—They also show cat owners and the many places where cats live.\

2017-09-19 09:57:08
very close to first pass, adding some images to the post to close out this short work session


2017-09-20 00:51:34
will call this iteration the 1st pass
- what's missing?
- does the story make sense?
- what am I talking about?

2017-09-20 08:06:34
what's missing? THE middle of the story
- some discussion of running deepdream on movies, and using it like a filter. those results were fantastic, but they were always the same unless I adjusted the parameters.
Disconnected from me
- part of what amzed me most about making deep dream images was that I could see them emerging from nothing into hyperspace as the semantic video feedback spiraled inward.

predictable results
- something was missing. Unpredictability, so therefore people

Yes the story makes sense, but it lacks a middle

I am talking about my introduction to the field and how I dound my own voice in iot


2017-09-20 16:28:14
continuing to edit the About piece. adding the middle part of the story and attaching media.

following that I will edit the Bio section.

For my next worksession
- import guest list into eventbrite
- send out invitations


2017-09-20 16:31:54
It should come as no surprise when a learning machine misidentifies the starship Enterprise, having never learned about Star Trek in the first place. But, the Enterprise-D is indeed something like a combination of CD Player, Odometer, and Digital Clock. The computer is merely wrong but together we arrived at poetry.

In 2015 a team at Google led by Alexander Mordvintsev released the first Deep Dream machine hallucinations to an amazed internet. These were instantly recognizable as psychotropic fragments of a universal language. Enthusiastic internet communities formed around the images; what they were, and how you too could make them. This was my introduction to a gentler, more humane story about artificial intelligence.

Showing the learning machine thousands of saxophones is enough to get it into the habit of finding them. Peeking inside, it's apparent that details in the environment contribute to the classification of a subject. The learning machine attaches vague impressions of hands and even a musician wearing a purple suit to its understanding of "saxophone". Most of the examples it learned from must have also included this subject matter.


2017-09-21 09:09:47
It has never been easier to embrace the artificial intelligence technology which silently reshapes the world.

2017-09-21 09:44:22
editing some video for addition to about page


2017-09-21 11:08:51
https://vimeo.com/234795103


2017-09-21 11:44:44
completed alpha version of About post


2017-09-21 14:30:39
completed beta version of About post
moving on to the Bio post


2017-09-21 15:57:56
cleaning up some CSS issues before getting into the bio


2017-09-21 17:35:01
video editing and postp[roduction for bnio page header. using the crazy video I made with Generate app on my phone.]


2017-09-21 19:00:32
trying to find a reasonable portrait


2017-09-22 09:56:03
found a great portrait - one thea took at the star trek museum of me in a borg regeneration alcove. I'm doing a bit more work on the header anim that I created yesterday. Perhaps its too much, but I have to know

I'll get the biography cleaned up in the am, then do a quick site review.
Any issues that come up I'll deal with in the am.
- add CTA to event section
- If you'd like to be on the guest list please let me know at deepdream [at] skinjester.com

The afterbnoon is dedicated to mailing invitations out


2017-09-22 10:54:59
working on the bio

He studied performance art and computers at the Massachusetts College of Art and proceeded to design screens for television during its Cambrian explosion in the 1990's. He remembers making broadcast graphics using a stat camera (yeah, look it up) and loved it.

In addition to design direction and consulting  under the name skinjester,


2017-09-22 11:13:12

[Name] is a [title] who works with [who you help] to [how you help them].

Gary Boodhoo is an Interface Designer and Creative Director who works with videogame studios to create humane software. A Jamaican-born industry veteran, millions of players around the world use the interfaces he invented for games including Madden NFL, The Sims, Star Wars: The Force Unleashed and The Elder Scrolls Online.


[First name] [knows/believes] [what you know/believe about the work you do].

[First name] has [landed/secured/garnered/worked at/supported] [insert your most compelling experiences and wins].

[First name] is a [trained/certified/awarded] [insert relevant trainings, awards, honors, etc].

[First name] holds a [insert degree] in [insert area of study] from [insert university].


Gary has presented interactive video installations at the Game Developers Conference and at gallery spaces for art and technology festivals. He's slowly becoming a better public speaker, with presentations on Creative AI for the Society for Ritual Arts, CODAME, and the Bay Area LASER Talk series.


2017-09-22 15:35:27
I'm done adding content to the site. Doing an audit to see if its ready for release


2017-09-22 15:56:18
CSS tweaks, typography


2017-09-22 16:02:23
Gary has presented interactive video installations at the Game Developers Conference and at galleries in the San Francisco Bay Area. 

His video installations have been shown at the Game Developers Conference industry event, hotel lobbies with a DJ and also at universities, where a group of interested students provided an impromptu code review. He's slowly becoming a better public speaker, with recent presentations on Creative AI for the Society for Ritual Arts, CODAME, and the Bay Area LASER Talk series.


2017-09-22 16:12:31
Bio is good enough. Will no doubt refine further later. continuing site audit


2017-09-22 17:08:28
I'm close to starting the invitation pass #1 eta 15m
just doing some last minute proofreading and writing


2017-09-22 23:29:19
I'm trying out some new work. On humans. You're invited!

Please join me for LIVING.ROOM.01, an exclusive and perhaps, hilarious encounter with a gregarious learning machine. This interactive video installation uses artificial intelligence and a live camera to make science fiction cave paintings. Read more about what I've discovered. | deepdreamvisionquest.com

See you on the other side,

Gary Boodhoo


2017-09-23 09:31:21
formatting guest list spreadsheet for CSV export to

test email invite
test twitter invite
test facebook invite (messenger)


2017-09-23 22:14:19
testing twitter invite flow

// creates rich media card on twitter linking to event
Share this event on Twitter: https://www.eventbrite.com/e/livingroom01-registration-37833029610?ref=estw


// on twitter, this is just a plaintextlinjk
Your URL
https://deepdreamlivingroom.eventbrite.com


2017-09-23 22:23:29
invitation details should read:
You're invited to LIVING.ROOM.01, a personal encounter with a gregarious learning machine for friends and colleagues. Registration adds you to the guest list and you don't need a ticket to attend. Please indicate the number of humans in your group.


2017-09-24 12:17:20
successfully sent invite to Thea
compiling guest list


2017-09-24 14:13:14
organized guest list into groups of invitations. almost ready to send out group A


2017-09-24 14:44:23
I need to take a second look at the invitation message before sending and emphasize the website URL for further guidance


2017-09-24 17:39:10
ready to send group A


2017-09-24 17:46:20
sent group A. Heart is sort of pounding


2017-09-24 17:50:17
testing FB sharing of site content


2017-09-25 09:19:28
testing instagram sharing, apparently uses facebook cache


2017-09-25 10:13:15
sent out a number of invitations on instagram


2017-09-25 23:25:08
I think the response was reasonable? Some kind words all around from the people I invited. I've agreed to repeat my LASET Talk on 10.4 at UC-Berkeley. Posting that as an event on the website


2017-09-26 00:45:05
added 1st pass event post for next week's LASER Talk
- ask yourself, how does this post look when shared on FB, instagram, twitter
- how can this post be used to drive interest in my work and the site?




2017-09-26 12:22:51
sending out some more invitations

Hi $firstname My wife and I are hosting a private exhibition of machine hallucination artwork. It's an interactive video installation. Hope you will come by and take a look. We would love to see you.

https://deepdreamlivingroom.eventbrite.com


2017-09-26 12:49:37
updating facebook share from home page, new text, new image

https://static1.squarespace.com/static/56f0c91337013b8f45f72009/59caae6f2aeba5d7b67e33b0/59caae8032601e3f295deaff/1506455189430/Animals_Insects_Eye_spots_butterfly_035757_a.png

https://static1.squarespace.com/static/56f0c91337013b8f45f72009/59caae6f2aeba5d7b67e33b0/59cae9968dd041342461d808/1506470342070/P4074415-crop1x1-tight.png

https://static1.squarespace.com/static/56f0c91337013b8f45f72009/59caae6f2aeba5d7b67e33b0/59cb54479f7456fb2e21d4d6/1506497613521/thumbnail-homepage-2-1.png


2017-09-27 01:47:21
updated event listing for LASER Talk, tested FB share


2017-09-27 08:13:29
LinkedIn & Twitter posts for LASERTalk event are poortly formed. Need to take a look a Twitter Cards and see if there's metadata I can add to get a clean post (one in which the img preview, title and excerpt are all shown)


2017-09-27 08:59:41
Adding metadata for Twitter cards to posts

<meta name="twitter:card" content="photo" />
<meta name="twitter:site" content="@skinjester" />
<meta name="twitter:title" content="Leonardo Art/Science Evening Rendezvous" />
<meta name="twitter:image" content="https://static1.squarespace.com/static/56f0c91337013b8f45f72009/59caae6f2aeba5d7b67e33b0/59cbcddca9db098ede4e77c4/1506528735963/Laseron-2x1-1200x600-1.png" />
<meta name="twitter:url" content="https://www.deepdreamvisionquest.com/new-events/2017/10/4/leonardo-artscience-evening-rendezvous" />
<meta name="twitter:description" content="In this talk I describe how I use stagecraft, creative coding, and game design to make pictures of Minds.">


2017-09-27 09:17:25
this validates properly on the twitter validator

I'm at UC Berkeley 10/4 7p speaking about my sci-fi cave painting video installations
https://www.deepdreamvisionquest.com/new-events/2017/10/4/leonardo-artscience-evening-rendezvous

2017-09-27 09:36:48
posted LASER Talk event to LinkedIn

I'm at UC Berkeley 10/4 7p speaking about my sci-fi cave painting video installations. This talk describes how I use stagecraft, creative coding, and game design to make pictures of minds.


2017-09-28 08:46:39
checking delivery time and cost of Moo postcards
working on that design this worksession


2017-09-28 08:56:18
after sending in the design, I can get the postcards by
10/2 +$31.00
10/4 +15.75


2017-09-28 08:59:05
some self-examination before getting into it

"A one-sheet is a single-page document that SHOWCASES a specific product or service with the goal of promotion. Think of a one-sheet as a SNAPSHOT of a particular part of your business that includes the most relevant and valuable information for a specific TARGET AUDIENCE."

Who is it for?
It is a simple one-sheet for live events that provides customers with branded artwork that directs to the project website

Why would anyone want it?
- Reinforces personal worth
	+ Involvement
	+ Interestingness
	+ Intelligence
- Customers advertise their own interests under my brand
	+ lets me extend brand to others who weren't at the live event

Where is it released?
Live Events. Its not an invitation though. Its collateral that is made available for those events
- LASER Talk
- LIVING.ROOM

When is it released?
- During an event

What outcome do you want from it?
- capture more attention
	+ increase number of instagram followers
	+ increase visits to project site
- referrals
	+ invitations to speak
	+ invitations to exhibit
	+ collaborations

Why are those outcomes valuable?
Because they let me scale this project up and branch into new ones like a Cambrian Explosion
- because they extend my reach
- because they take me out of my comfort zone
- because they establish my reputation
- because they are my first practical steps towards monetization
- because they are steps that keep it going and bring others into it
- SPECIFIC USE CASES
	+ exhibit work in Europe (Berlin, London, Paris, Vienna, Switzerland)
	+ speak at Webvisions conference
	+ exhibit work at trade shows
	+ consulting offer from Google, Facebook, Microsoft, Apple, AKQA
	+ consulting offer from Gray Area, SwissNex, Root Division

What is the subject?
Sci-Fi Cave Paintings
- this isn't a promotion for a specific event

FRONT

T0	DeepDreamVisionQuest
T1	A Little Robot Uprising Goes a Long Way
T2	My science fiction cave paintings are sometimes a mirror and sometimes a window. I never imagined I'd use stagecraft and algebra to make pictures of minds. Now is the time to understand and embrace the artificial intelligence technology which silently reshapes the world. Wherever we find aliens they'll be artists too.

Contact
Gary Boodhoo, Artificial Experience Designer

instagram: @deepreamvisionquest
deepdream@skinjester.com

deepdreamvisionquest.com

BACK
img1
Gary Boodhoo, Title, Year


2017-09-28 12:03:46
working on Postcard design in Photoshop after a false start


2017-09-28 14:12:37
laying out a number of candidate back images


2017-09-30 00:07:50
some good ideas emerging, finally at a point where I can rapidly iterate


2017-09-28 18:52:56
collating images for postcard


2017-09-29 12:30:55
adding candidate images to photoshop doc


2017-10-01 14:08:18
rapid iteration on postcard layout. getting close I think. eta 2h


2017-10-01 22:37:38
finished layout, exporting to moo.com


2017-10-02 00:14:40
made some corrections exporting to Moo


2017-10-02 01:28:22
completed postcard design, placed order from Moo, expected before 10:30a 10/4


2017-10-02 12:57:52
shared deepdreamvisionquest About post on LinkedIn


2017-10-02 12:58:33
P1 review presentation video
P2 send event reminders
	- Pantea


2017-10-03 20:50:26
reviewing presentation


2017-10-03 23:11:22
Boodhoo, Gary (2015). Invoked by Movement [Painting]. New York, NY: Museum of
 Modern Art.
Ville-Matias Heikkilä,  A neural network tries to identify objects in ST:TNGintro,www.youtube.com/watch?v=UFVB5rnqjyY


2017-10-04 01:11:46
completed 1st pass cleanup to keynote presentation. have listened to pprior presentation 2x now. Will do so again in the am.

when will you start rehearsing tomorrow
Do you need any new assets
What can be removed


2017-10-04 08:29:40
working on the network diagrams, as sketched out last nite


2017-10-04 09:43:52
collecting a few GIUS of convnet in action

Venelin Valkov (2017), Building a Cat Detector using Convolutional Neural Networks, https://medium.com/@curiousily/tensorflow-for-hackers-part-iii-convolutional-neural-networks-c077618e590b


2017-10-04 09:59:48
correcting the visualization slides


2017-10-04 11:06:48
making some edits, and taking some notes

With each layer, the network transforms the data, creating a new representation.2 We can look at the data in each of these representations and how the network classifies them. When we get to the final representation, the network will just draw a line through the data (or, in higher dimensions, a hyperplane).


2017-10-04 12:31:39
I'm done editing the presentation slides


2017-10-04 13:48:29
writing up presenter notes
the postcards have arrivved they look great!


2017-10-04 14:45:35
finished writing up presenter notes
will most likely want to cull some of the backgorund info


2017-10-04 15:10:46
rehearsing


2017-10-04 16:02:55
rehearsal is going well, although wishing Thea was here to keep me honest. so strict! Time for 2 more full runs before I get ready to head out


2017-10-04 16:25:07
good run through time for 1 more


2017-10-04 17:11:40
saving presentation to thumb drive
ready to go


2017-10-05 09:33:20
UC Berkeley presentation was a winner. Good job


2017-10-06 11:15:34
back into the deep dream code again, preparing for the LIVING.ROOM.01 private exhibition. Familiarizing myself with how it all works!

camera dimensions
# max 2304 x 1536
# 1920 x 1080
# 1600 x 896
# 1280 x 720
# 960 x 720
# 864 x 480
# 800 x 600
# 640 x 480
# 352 x 288
# 320 x 240
# 320 x 180

2017-10-06 11:22:40
need to create test program to work out some new details in isolation of everything else

questions
- timed hallucination mode (uses timer instead of motion detection)
- how does this respond to colored lighting?
- lower resolution?
	+ is this really improving the computation speed, or is it experienced more or less the same?
- hallucination transform?
	+ did i remove the ability to zoom in/out?
	+ need to see more wafeform of the sin wave transform
	+ how sensitive did I leave this for parameter changes to get broader range of fx
- motion detection
	+ how is this really behaving when subject is close to camera?
	+ is it possible to refine this, so that  it triggers less often?
- USB keypad
	+ button assignments
		* what do they do?
		* how to prevent crashing?

2017-10-06 14:10:08
reading up on fil input and output. I want to graph the threshold values being output by the motion detector

2017-10-06 14:25:18
specifically, I want to graph delta_count vs delta_theshold

T
2017-10-06 14:28:57
and also, how to prevent the programs I've setup from cycling - I just want to use one at a time. no doubt very simple, probably I set up to address by name, or a default value

2017-10-06 16:15:26
I've successfully exported  count, trigger and history values from the motion detector into a spreadsheet and am looking at a graph now

it shows how the trigger value (the threshold at which motion is detected) increases and decreases in response to the input data. Although perhaps more conservatively that I realized


2017-10-06 16:41:56
these graphs are very ionteresting - and led me to a code change that may be meaningful. motion detection does seem a bit more controlled - bot at near and far distances. Worth digging into further, but moving on for now

I need to figure out how I structured these programs, and specifically the options attached to each.


2017-10-06 17:31:49
maybe optimized for closeup usage a bit better?


2017-10-06 18:10:15
taking a moment to get video screen capture sorted out


2017-10-06 18:52:44
looking at how programs are setup, I want to tweak existing and add some new ones


2017-10-07 08:58:20
printing Guest List
Thea & I are about to set up the rig before she makes a run to the supermarket for drinks, food and supplies

2017-10-08 17:03:34
getting over a well-earned hangover
- transfer files from the linux machine to dropbox
- find good stills - associate w attendees
	+ send out attendee stills as personal  than-you email


2017-10-09 15:35:22
preparing another order of postcards - considering these as research for preference and print quality

2017-10-11 09:46:14
reviewing and collating runtime footage

2017-10-11 16:37:49
reviewing and collating runtime footage
- find snapshots of guests
- identify sequences for encounter loops

- contact Solomon Chi at BCEC
	- what is the event format?
		- panel w Q&A
	- what will I need to present?
	- confirm date, time, location

2017-10-12 17:50:54
continuing to collate and export data

video postproduction on show montage is looking great. Figured out how to remap to based on audio waveform, and suroprisingly another journey into iPad music production

2017-10-18 16:48:12
I'm getting a bit hung up on organizing and figuring out what to do next. Here's the plan:
- BCEC talk at UC Berkeley
- Instagram promo
- Website
- Postcard Mailing
	- create envelope template in Word

2017-10-20 16:41:36
I've sent out 2 postcards to Noah Rappaport, my instagram contact who asked

2017-10-20 18:03:44
I've printed all the ZOS envelopes except the one for Ala Diaz. New envelopes arriving 10/26 and will send out then. This will give me time to update the site with the new event post and the hardware post

2017-10-26 10:07:32
new envelopes arrived, added some additional names to my mailing list
going to the post office at lunch to get the stuff mailed out
speaking tonight at UC Berkeley - a student organization - Berkeley Careers in Entertainment Club

2017-10-29 10:17:28
creating encounter loops from camdera footage. Not bad stuff, but also not as controlled as I would have liked (better framing, locked down camera, and so forth)
I have the AV setup here in the living room and its time to start using it for research and development

2017-10-29 12:07:07
rendering out sequences for vimeo

2017-10-29 14:28:37
postproduction for runtime loops

2017-10-30 08:32:35
done with the video export.
Next work session
- purchase paper at Blick Art Materials on Market St
- create personal note boilerplate for postcard mailer
- print remaining envelopes
- print notes
- package postcards in envelopes w notes
- create galleries for each section of the new event post
- 1st pass editorial

2017-10-31 09:58:45
printing more envelopes

2017-10-31 12:22:03
finished packaging postcard mailer

2017-10-31 12:33:38
heading to the post office


2017-11-03 15:29:07
started working on 1st pass of LIVING.ROOM event post
Purin has invited me to participate in a pop up exhibition that he's staging. It's short term, but I'm prepared - and have time to make some improvements. More on that later.
- will need promo material from him to create an event

2017-11-03 18:22:24
working on first pass
did a bit of writing - for the first time ever di not feel compelled to read it afterwards. Looking at the images I've constructed now and adding them to the galleries

2017-11-04 15:28:55
collatinng images for the various galleries

2017-11-04 15:57:43
Exhibition next weekend w Purin is on. Take some time to set that up in Trello, etc. Immediate priority at the monemt is to finish curating these images.

2017-11-05 11:51:30
Opening: Friday November 10, 6:30-9pm
On view: Saturday November 11, 4-8pm

Location: 219 Design
67 E. Evelyn Ave #1, Mountain View, CA

Artificial Intelligence: A Group Pop-Up Art Exhibit
Featuring works by Albert Lai, Kevin Ho, Yotam Mann, Purin Phanichphant, and Gary Boodhoo

Recently, news about experimental Facebook machine learning research has been circulating with increasingly alarming, Skynet-esque headlines. “Facebook engineers panic, pull plug on AI after bots develop their own language,” one site wrote. “Facebook shuts down A.I. after it invents its own creepy language,” another added. While the massively over-exaggerated headlines were debunked as fake news (literally, “artificial intelligence”), the damage has already been done: many of us will never completely trust A.I. in our lifetimes.

While remaining neutral on the debate between optimists and pessimists, the exhibit aims to examine other tangible forms of A.I. as perceived by artists and creatives working with technology. Part educational and part thought-provoking, the show aims to attract and spark dialogues among thought-leaders in the field, as well as aspiring next-generation technologists.

2017-11-05 14:47:50
spending a bit more time figuring out the event post banner image than I'd expected. Needs to travel well - FB, LinkedIn, Twitter, IG

2017-11-05 16:49:38
settles on banner image. may candidates, but I think this one is the most people-focused, and also has eyeballs in it

2017-11-05 17:11:21
back to collating image galleries
creating event page for upcoming Artificial Intelligence show first

2017-11-05 17:36:40
Twitter message:
I'm showing at Artificial Intelligence: A Group Pop-Up Art Exhibit, opens 11/10 18:30-21:00 https://goo.gl/maps/QVnN8ohC4g42

2017-11-05 17:58:28
completed event post looks legit

2017-11-05 23:07:19
updated events section

next worksession
- finish curating image content
- 1st pass image captions
- validate sharing to FB, Twitter, LinkedIn
- examine video header bug that turned up

2017-11-06 07:55:18
noticing some weirdness with the video header where the page loads, but the video doesn't expand to fit the viewport. This just started happenening, and not sure why. Will look into this further today


You're invited to Artificial Intelligence: A Group Pop-Up Art Exhibit, featuring interactive art pieces by Kevin Ho, Albert Lai, Yotam Mann, Purin Phanichphant, and Gary Boodhoo.

The event is generously hosted by 219 Design at their space in Mountain View (67 E Evelyn Ave #1, Mountain View, CA) and opens Friday November 10, 6:30-9pm. The exhibition continues for one more day on Saturday November 11 during 4-8pm.

2017-11-06 09:43:59
I scaled the video up to 2560 x 1440
still seeing the placement/scaling issue in Chrome, not at all in Firefox
I can't imagine that squarespace is somehow favoring a standard video resolution, but rendering out a sample at 1080p to see if that makes a difference


2017-11-06 11:33:18
the problem may be with vimeo itself?


2017-11-06 11:57:40
Uploaded some video to YouTube
The YouTube embed is working as expected


2017-11-07 07:59:46
purchased LED strips for bias lighting arriving later today

2017-11-07 20:05:54
practicing python w camera input before diving back ingto the rem.py code


2017-11-07 21:30:05
after some poking ariound and re-remembering old news, I was able to set up a video calibration - straightforward - just shows the output of any connected cameras in seperate windows. adding some functionality to transpose and flip the image as necessary to get the proper aspect ratio



2017-11-08 00:14:51
ran into some odd issues with KVM switch where I wasnt able to switch back to linux machine - no idea why - apparently something to do with placement of the outputs from the gfx card?



2017-11-08 08:55:19
- is it possible to switch the renderer between layer activations and feature maps
	+ yes, just pass -1 as the featuremap
- USB controls
	+ what functions to include
	+ previous layer
	+ next layer
	+ previous featuremap
	+ next featuremap
	+ freeze frame (disable motion detection)
	+ toggle HUD
	+ toggle motion detect

this worksession
- examine the renderer
- other models?
	+ VGG19 is pretty cool - entirely different appearance, especially when cycling thru featuremaps


2017-11-08 12:33:54
continuing to work with VGG19 to discover good program settings


2017-11-12 17:15:34
Mixed feelings about the event. On the one hand, some good conversations with people who really "got it". Great that everyone thinks I'm a "genius", etc. But on the other hand, I felt there was a lack of energy I hadn;t encountered before. I wasn't thrilled about the placement of the piece either, and wish I'd spoken with Purin about it in detail. The problems were:
(1) the view of the empty room was arbitrary and poorly framed
(2) the location by an open door prevented a feeling of being enveloped. There was a big negative space competing with the positive space I was trying to project
(3) I should have used the foot lights as I'd planned - partially because they define the space for interaction and partly because they photograph well.
(4) some personal issues

In hindsight I feel a better placement would have been in a corner, where the empty view would have shown the entire exhibit or next to the neural net model - as I felt these 2 pieces complemented each other very well - looking at the output of one explains the other nicely.

I can't keep on relying on handheld/incidental documentation. Need to include documentary camera as part of the setup

I can't rely on people getting as close as I'd like. Need to mark off the area of engagement with (tape? LED strips? signage?)

From what I can tell, no traffic to instagram or the project site despite handing out approx 50 postcards. Thea pointed out that the postcards don't have a CTA on them, and yeah - that's true - I didn't think I needed one, but the next round will incorporate that.

Similarly - the instagram icon + username is pleasant to look at and compact. But it expects too much. Its too compact. Needas to spell out Instagram. And needs to provide a CTA here too - "follow me on instagram" would be fine

I haven't gone through the runtime footage yet. I'm pretty sure there are some good encounters captured there as well.


2017-11-13 11:03:55
refining event section on website and taling a look at some structural changes
https://youtu.be/AO2UifljuMU


2017-11-21 21:04:12
great - reconnected to my remote on github
pushing my local changes there


/home/gary/Dropbox/sciencefictionthriller/2017 LAST Festival/video/run= video


2017-11-22 11:03:01
Git isn't working the way I thought it would - at least with regard to the github remote. Be sure to  provide a unique name for the github repo as this caused some confusion before when they were identically named
I deleted that remote repository and am going to try to walk thru that process again




2017-11-22 12:01:49
created new (empty) repo on github, set that as my remote from the command line
git remote add origin https://github.com/skinjester/remote-vision.git

pushing my local changes to github now


2017-11-22 12:40:24
it is the network models that are exceeding the size of git remote push

remote: warning: File models/bvlc_googlenet/bvlc_googlenet.caffemodel is 51.05 MB; this is larger than GitHub's recommended maximum file size of 50.00 MB
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
remote: error: Trace: cd67c04f8c1679c8ede51f8ba49e1cb3
remote: error: See http://git.io/iEPt8g for more information.
remote: error: File models/VGG_ILSVRC_19/VGG_ILSVRC_19_layers.caffemodel is 548.05 MB; this exceeds GitHub's file size limit of 100.00 MB
To https://github.com/skinjester/remote-vision.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://github.com/skinjester/remote-vision.git'


2017-11-22 16:00:07
git workflow is back up and running again. too tedious to describe further. other than to state how large files, such as images need to be place doutside the git repo


2017-11-22 16:13:59
inside the code again
changing picture location to be external to repo directory


2017-11-22 17:39:58
updated to export images to my Pictures directory (hardcoded location)
updated timestamped filename to include month, day, and better human readable format


2017-11-22 18:09:58
taking a close look at how I setup the logging system - I want to be able to output exported image status to console if I want at runtime


2017-11-22 18:45:15
creating a new branch for next steps.
what are they?
- I want to understand how motion detection is working better
	+ I want to generate signals when motion happens in different areas on screen
- I want to incorporate camera gamma processing into program settings
- I want to composite vignettes and blurs into the renderer


2017-11-22 20:01:00
figuring how i setup logging. sorta awesome


2017-11-23 09:06:38
playing around a bit with the logging mechanism


2017-11-24 10:52:34
after thinking about it for a bit yesterday, here's what I want to take a look at:
- graph the delta value over time
	+ the count of pixels that are changing each frame
		* how does this react to 2 parameters
			- distance from camera
			- motion speed

what if instead of inferring the state of the moving image, I simply counter the number of pixel changes over a duration. if that value is above a threshold then get the next camera frame.

On the surface this sounds simopler than what I'm doing now, with fewer special cases, and agnostic towards the kind of motion that is happening


2017-11-24 14:30:58
finished setup for tracking delta value over time


2017-11-24 15:25:10
studying graphs of my motion. not quite as responsive as I'd previously thought. maybe try loweing processing resolution?

observations
- faster motions have higher deltas
- increasing the threshold for camera input reduces  delta values
- removing the bluring stage when the detection queue refreshes makes detection more responsive


2017-11-24 15:50:01
looking ath the threshold function in the motion detection code. is possible its been set too low all this time. Increasing it reduces the amount of detail in the captured motion


2017-11-25 16:41:47
after an excursion into how to combine data series in excel and google sheets charts, I'm able to create rich graph of the data I'm looking at including
delata_count
delta_history
delta_trigger
motion detection states (as booleans)

2017-11-25 18:01:59

there's a lot more going on with tyhe motion detection code than I realized. Its ingenious


2017-11-26 14:55:53
After graphing the motion detection output, I've decided to make that processing run in its own thread for what I hope will be greater responsiveness. One problem that I'm seeing now is that because motion detection gets sampled aperiodically (depending on deepdream iteration params), the values I'm currently getting are spread further apart in time than I'd like them to be.

The thinking is that if teh comparision is constantly being made - even though any polling may be asynchjronous, at least the sampled frames will be closer together.

So far so good, I've created a motiondetection thread which I can
- start
- stop
- update
- poll


2017-11-26 15:29:17
MotionDetector.isResting
	- this is a use case in which wasMotionDetected amd the last value of wasMotionDetected are the same
	- we infer from this that the MotionDetector is resting (state has not toggled)
MotionDetector.wasMotionDetected


2017-11-26 17:12:04
have been experimenting a bit with different frame sizes and seeing how that affects performance
at 640 x 360, processing is extremely quick - its a completely different experience actually, but the resolutuion is a problem unless exaggerated.
It does seem like 2 gfx cards would each be able to compute half the image at the same time for significant speedup

Its definitely easier testing motion detection at these lower resolutuions due to the reduced latency - hopefully the multithreaded apporach will pay off and help decouple motin detection from computing the image


2017-11-26 18:36:28
moved the MotiionDetector.process() function into the thread.update() function
It doesn't crash. Sort of working. camera data may be wrong?


2017-11-26 18:39:15
yeah, I think there's something odd with the camera data - not seeing the differences I expected to see - I think that there may be duplicates of the the same frame getting used in the calculation?


2017-11-27 16:53:01
starting worksession
when I left off, everything was working but imperfectly and my thinking is that the problem is happening because of how multithreading samples the camera, but doesn't necessarily get a unique for each sample.

The goal is at capture time, compare the capture with the currently stored data, if they're the same then return, but if they're different then replace the current frame w the


2017-11-27 17:35:51
to expand further on that idea
- in the Webcam class, create a 3 element queue
	+ this will take the place of the current t_minus, t_now, and t_plus buffers
- at capture time, capture the frame as normal
	- check for differences between captured and stored
	+ if different then push the captured frame on to the queue
		* which pops the last frame in the queue


2017-11-27 18:23:43
the differences I'm calculating as a test in the Webcam.update() look a lot more like what I'd expect them to


2017-11-27 23:53:57
multithreading the camera capture (and subsequent motion detection) doesn't decouple it from latency created by running the dream cycle. I..


2017-11-28 00:13:45
so, motiondetection doesn't need to happen in a seperate threaded routine - it happens in the camera capture routine instead. Should be possible to retain all or most or the MotionDetector.process() function with a few new assumptions
- without using a global variable, how to communicate delta count from WebCamStream to MotionDetector?
- The code in rem.py is looking for values set to MotionDetector
	+ wasMotionDetected
	+ isResting
- it is not looking directly at the delta values between frames, and if it need to it would get that information from the camera (?)


2017-11-28 09:25:38
rewriting the motion detection so that the camera stream delegates this functionality to the MotionDetector machine (class) and so that any calls to MotionDetector.process() in rem.py are removed


2017-11-28 10:16:54
after some refactoring, testing to see if it still runs. It does.


2017-11-28 16:49:58
need to do some remedial work on classes. not quite sure about how the "attach" a motion detector object to a camera object

need to instantiate a MotionDetector object from within the WebcamVideoStream class
	- this allows each camera object to have a unique motion detector attached to it
	- this prevents defining a global object that instantiates Motion Detector just so I can refrence from inside the WebcamVideoStream class


2017-11-28 16:58:02
ok! pretty straightforward!


2017-11-29 08:02:50
I've nearly completed refactoring the motion detection system


2017-11-29 08:09:19
everything appears to be working , and logging text file is being created and populated with data, however there seems to be some mix-up with the delta_count and delta_history values which appear identical now that I look at the file.So close. I believe the payoff in responsiveness will be worth the time spent


2017-11-29 10:13:08
not quite sure why motion detection isnt working - but want to figure it out before beginning worksession for ZOS

delta_trigger is returning the values I'd expect
which means that the add_to_history function is also behaving as expected


2017-11-29 10:18:48
and in fact, the graph of delta count and delta trigger look good
the problem is that delta_history isn't being set properly. it';s currently mirroring the delta_count values


2017-11-29 10:21:00
graph of the time values looks completely different than before - linear instead of stepped.


2017-11-29 10:27:51
previous rhythm was :
- store current value of delta_count in history
- get new raw value of delta_count
- motion detection comparisions
- adjust delta_count value

current hythm is:
- receive new raw value of delta_count
- motion detection comparisions
- adjust delta_count value
- store current value of delta_count in history


2017-11-29 10:35:47
cool, motion detection is working again


2017-11-29 10:40:57
for next worksession:
Postcards
	- how soon can 50 cards be delivered
	- Collate new artwork
	- Write new copy
		+ include strong CTA
		+ ask yourself =- what is the measurable outcome I want to see from giving away this card
Website
	- add event post
Code
	- further refinement of motion detection
	- take a look at the compositing feature
		+ seems a bit half-baked
		+ I want to prevent sudden jumps in the output
			* when the input changes, it should fade in
			* why does it fade in sometimes and jump sometimes
			* what if I wanted to dynamically composite another image, how would I do that?


2017-11-29 16:48:55
creating a test program with large number of early iterations to test responsivemess


2017-11-29 16:55:39
what this graph is telling me is after  detection is triggered, deltacount is reduce. what if it wasn't?


2017-11-29 17:13:48
will continue taking a look at how motion is detected - especially continuous motion




2017-11-29 18:48:31
holy crap - I remived some legacy(?) conditionals and the thing is super responsive more so thabn its ever been

will graph this in a moment and see whats going on unde rthe hood!


2017-11-29 21:32:43
responds to sudden motions much more readily than continuous ones


2017-11-29 21:57:51
observing that a larger dp...elta_count history buffer causes the triggering to spread out to encompass the entire delta count peak


2017-11-29 22:02:38
any triggering oproblems arise when the delta_count samples appear "spiky" on the  graph


2017-11-29 22:15:22
setting the detection comparision to a hardcoded minimum may be promising. The most responsive case so far, but I wonder if this is actually unrealistic given the amount of ambient motion in a public space


2017-11-29 22:36:49
the detection events are being captured a t a fine resolution during the threaded i/o but detection status could be missed depending upon the timing of the next iteration.


2017-11-29 23:54:34
great job on the motion detection refactor - significantly more responsive - allowing for some dramatic and predictable movements.

Its sort of incredible at lower resolutions as wll and I'm wondering if the tradeoff in respoinsiveness is worth it?


2017-11-30 09:30:34
A postcard order placed today can arrive as early as Dec 4


2017-11-30 17:54:24
performance space will be open
Friday 1st: 6-9p
Saturday 2nd: 12-6p

Contact William Lockwood about setup
 347 446 5325 to introduce myself and confirm


Next week we'll do installs and sound check on Friday 8th, and then final setup early Saturday afternoon.


2017-11-30 18:41:00
Followed up with William and Sam at NOIZE FLOOR


2017-12-01 09:07:10
placed an order fon amazon for additional front & back lighting options
going to see the space this weekend



2017-12-01 09:33:06
iterating on the postcard front
I've removed the image is text only
now states

SCIENCE FICTION CAVE PAINTING
tune in Instagram @deepdreamvisionquest
turn on deepdreamvisionquest.com

I'm working out the layout now
ETA 1h


2017-12-01 10:46:48
completed 2nd pass design for postcard front
making a test pribnt to validate


2017-12-01 11:39:43
yeah, its done


2017-12-01 15:49:01
plac ed postcard order, expected to arrive on Dec. 5
moving on to the event post on the website


2017-12-01 18:34:01
working on the event post

FB promo
Introducing Noize Floor, a collective of electronic musicians specializing in modular synthesis and focused on developing their art form in a live, improvisational setting.

For this launch event we're partnering with Beyond Beyond, an art collective that invades empty spaces downtown and curates pop up exhibitions. They are inviting video and film artists to animate the space. It's going to be fun!

instagram promo
Noize Floor is a music collective dedicated to modular synths and other quality electronic music live performances.
The inaugural event (free!) will be held in an empty gallery downtown, and will feature a ridiculous amount of talent


2017-12-01 19:17:39
doing some site cleanup and bug fixing
added the event. refining it. then test fb & twitter share functionality


2017-12-02 17:09:42
viewed thd space and met Sam, one of the organizers. its pretty raw. I've got a great secrtion - a kind of alcove dedicated to the setup so hoping for some nice whitespace around the display. The windows behind will apparently be covered to prevent some streetlighting from entering

continuing to work on the event posting - not liking how its balanced, and there are some inconsistencies in the site overall I'm fixing


2017-12-02 17:22:53
looks like the space for setup has changed - a bit smaller, described as having 2 walls - I dont really remember it, waiting for photo


2017-12-04 08:04:38
Samuel sent photos of the space


2017-12-04 09:19:46
finalizing event post
- share on FB
- share on instagram

2017-12-04 09:39:24
FInally - was able to rework the promo art into something usable for my site. kudos to noize Floor for including an .ai file in their promo pack

realizing that when I do my own media kit, I'll also need to account for post-submission edits, such as the one I'm doing right now


2017-12-04 10:04:04
event post is ready to share I think


2017-12-04 10:08:42
applying event format to previous events for consistency


2017-12-04 10:12:58
testing FB share

FB
Deep Dream Vision Quest returns to SF after a month of user research and a brief refactor. I'm really looking forward to live (machine) hallucinations immersed in synthetic soundscapes. Hope to see you there! https://www.deepdreamvisionquest.com/new-events/2017/10/4/noizefloor

INSTAGRM
I'm so excited to a part of the Noize Floor show in SF on Saturday Dec. 9th 7:30 PM - 1 AM.  Noize Floor is a music collective dedicated to modular synths and other quality electronic music live performances. The inaugural event (free!) will be held in a pop-up gallery space downtown at 155 Main Street, San Francisco, California 94105, and will feature a ridiculous amount of talent, including amazing visuals from @gravity.max, @deepdreamvisionquest, and music performances by @andrewvanwart, @jr_rankltd, @plzsendpzza, @yo.res, @birdsofrhythm and @_la_fortune. Come say hi and be a part of the synesthesia.


2017-12-04 13:03:42
Samuel posted some guerilla photos for promo on FB and I replaced the graphics I was using with one of those images, ended up re-sharing the post to FBG - its just a better image all around

maybe should do same for instagram - but I've put enough time into this.



2017-12-05 12:59:43
Havent looked at deepdreamvisionquest in a few days. its badass
merging recent code changes to the main branch now


2017-12-05 13:02:28
maybe not quite yet...
there are cases I'm seeing where motion detection happens on the camera thread before the value is checked for within the event loop. Is there a way to solve for that? maybe to toggle some value on when motion is detected - and keep it on until it gets referenced?


2017-12-05 17:29:06
I'm studying the code I previously wrote
Not quite done with motion detection optimizations


2017-12-05 21:40:23
why is Viewport.force_refresh a method of the Viewport class?
what does the Viewport class do?

it constructs and manages Viewports
- the render viewport
	+ the HUD overlay
- the motion detection viewport
- related to openCV window management
	+ event handling is a function of openCV windows
- material displayed in these windows is a visualization of other processes
- material displayed in these windows isn't fed back into the neural net

METHODS
show()
export()
refresh()
monitor()
shutdown()


2017-12-06 08:57:03
refresh() actually refreshes the framebuffer in the composer. should  be a part of that class instead.

Model.set_endlayer()
	force_refresh
Model.set_featuremap()
	force_refresh()
Viewport.__init__()
	self.force_refresh = True
Viewport.refresh()
	self.force_refresh = True

the action based on the force_refresh condition is run each iteration from inside the deepdream() function

terms
Main
Subgroup
Send
Insert
Channel


2017-12-06 09:23:50
the compositing algorithm is setup to rely on a single Main output
the neural net is dreaming about the Main output
the neural net is writing directly to the Main output
	- which means the shape of that buffer is changing with each octave - is that correct? Yes. verified.
	-  which means that viewport.show () does the work of reshaping the buffer to fit the viewport.  Yes.
when the cycle is refreshed
- we start writing the webcam to a secondary buffer in the Composer
	+ the write function is specific to this buffer and handles resizing the camera image to match the viewport so it can be composited


2017-12-06 09:52:52
the problem I'm seeing here is that buffer1 is doing double duty as the Main mix and as an input channel (for hallucinations)


2017-12-06 10:13:04
Composer
- accepts any input shape and will resize it to match the Display.width, height


2017-12-06 11:27:08
continuing to rework the Composer class


2017-12-06 14:32:42
I have the Composer compositing the webcam signal with the dream signal to live output now


2017-12-06 16:57:14
having some difficulties with crashes for programs that use an octave cutoff greater than 2 iterations.  Surely has something to do with hopw that's implemented and not the compositing mechanism which gets bad (how bad?) data and fails

the 2 immediate issues I'm seeing at the moment
motion detection
- there's an issue with the MotionDetector.isResting() function
- not sure if its returnuing the values I think it should be
blending between  webcam and dreamvision smoothly
	- the viewport.show function is happening in  deepdream() function with each iteration
	-  the viewport.show() function is happening in the  main() function at the beginning of each event cycle


2017-12-07 09:39:54
Composer.is_dreaming
- True:  dream loop continues dreaming about its own output
- False: dream loop gets new camera frame and starts new dream


2017-12-07 13:10:12
motion detection refactor continues. its going well I think - the system is much more nuanced and responsive now - still a bit off though. There's some legacy code in the Composer that may be problematic now


2017-12-07 14:00:44
stripping out the previous Composer compositing functionality to see if that's causing some of the ghosting behavior I'm seeing. Its sorta cool I'd admit, but not predictably so, and often breaks the flow of an otherwise continuous experience


2017-12-07 15:05:45
stripped out legacy compositing functions


2017-12-07 15:09:03
found a bug - an unintended consequence - the dreamcycle isn't being refreshed and doesn't feedback on itself. similarly - the cyclefx functions aren't getting called


2017-12-07 16:35:49
Composer.update() is called from Viewport.show
in addition to compositing
it was an entry point for Cyclefx. does that still hold true?


2017-12-07 16:58:59
fixed the cyclefx bug - seems to be working not fully tested
- the main issue remaining is incorporating the raw camera image into the MIX.
- Previously, this happened anytime motion was detected

I'm also wondering about the basis of motion detection from comparing 2 images, where previously three were used. The output of the motion dtector seems quite sparse - is this a good thing? need to read up on the prior method


2017-12-07 17:51:24
doing some testing and integration of a differential image method I found on the web


2017-12-07 18:54:33
integrated into script, but checking values and seein g i can filter out some noise


2017-12-07 19:16:29
getting closer .
the motion detection data is better formed, can see facial detail as well as edges - pretty tweakable. need to fine tune the detection values though


2017-12-07 20:19:51
its the delta_trigger value that is problematic. not sure if the averaging method formerly in use is the way to go.


2017-12-07 20:54:29
in the ballpark (w motion detection) (again) (I think) It's more  predictably responsive than ever, although enough so that blinking can trigger a refresh. Deriving the trigger values from rolling average of delta_count as before helps smooth out smaller details (I think) - such as blinking


2017-12-07 21:25:07
the activity graph from the last run with a  history queue length of 50 looks pretty good - the best coverage of motion I think I've seen


2017-12-07 21:31:39
working on the compositing now


2017-12-07 22:05:16
wow - at 864 x 480, the responsiveness is incredible - not exactly realtime - but


2017-12-08 00:25:31
cleaned up some code, added better logging, added rais/lower noise floor functions. seeing a crash on a certain program at 1280 x 720 that I'd not seen before though on the strangerthings program. noticed at that time that about 4GB was in use on the gfx card. after rebooting it now shows 1.3GB used


2017-12-08 01:06:23
not seeing a problem with 'strangerthing' and was the first time in days of uptime that I'd seen a problem at all


2017-12-08 01:12:22
for compositing, here's what I;m imagining:
always use mix() funtion to combine camera and dream input
most of the time the camera input opacity is 0
when motion is detected
start a rate function that decrements an opacity value from 0.5 to 0.0
pass that opacity value into the Composer.mix() function
if retriggered, then start again from 0.5 to 0.0


2017-12-08 02:01:00
I implemented gamma adjustment using Pg up/down
- add the gamma value to hud
- log the gamma value to console

2017-12-08 02:30:06
- add support for USB keypad
- single control - every button does the same thing - advances to next program


2017-12-08 11:06:15
doing some cleanup on keyboard listener before getting into compositing



2017-12-08 15:08:21
the 864 x 480 output on the TV looks fine, but comparing w 1280 x 720
obvs 1280 x 720 looks crisper - but not hugely so. The gain in responsiveness at lower res is worth the tradeoff


2017-12-08 15:13:53
adjusting HUD for smaller screen size


2017-12-08 15:35:57
here's a surprise - I correctly implemented gamma correction on the input using pg-up/pg-down. Works as expected - except when the gamma value drops beneath 0, at which point the color mapping of the input becomes bizzare

- need to write gamma value to console and HUD

2017-12-08 15:42:13
gamma value written to HUD now


2017-12-08 16:45:58
there will be several hours later to get the compositing code worked out
- composition on motion detect
- curate existing program settings

2017-12-08 17:02:30
doing a bit of research on python timer objects before getting organized for setup and load out
- need to get monitor arm working and setup on the computer cart.
	+ monitor cable
	+ monitor power cable
- need to get CPU setup on computer cart



2017-12-09 09:22:51
challenging setup last night as the power outlets at the venue are on the ceiling. Thea was a big help in getting the cables run. Preliminary feedback from the  other people setting up was extremely positive, but also called out the need for the compositing feature I've been thinking about.

I believe I understand what to do - how to do it. The timer function is a seperate thread, and every time it gets called it cancels itself and restarts a new thread. That thread is part of the Composer machine, and when running will decrement the opacity value of the camera mix until 0. At that point the thread will cancel itself

The effect should be that - on motion detection, the webcam output becomes visible, behaving as a "guide", after a short duration (0.5sec?) the webcam dissolves out

If motion is detected while dissolving out, the opacity resets and the counter resets, and opacity begins its descent again.

TO BRING
- postcards
- shelf for AV cart
- backup webcam
- remotes
- wireless keyboard

TO DO
- compositing functionality on motion detect
- verify runtime image saving
- curate programs1

2017-12-09 10:08:36
I've added back cv2.dilate() to em-biggen the noise detection signal. may need to tone this back for the event ruintime


2017-12-09 11:58:53
testing use cases for the COmposer.mix() function before moving forward. completed some finetuning of the detection img processing earlier this morning
I'm dilating the differenced images before thresholding and this seems to capture broader motions more predictably


2017-12-09 12:18:17
created framework in COmposer machine for counter thread


2017-12-09 12:36:00
debugging ramp counter


2017-12-09 12:38:42
ok - looks like the the framework is in place - can start, stop, update and escape properly. Need to handle the case for it restarting itself when called during runtime


2017-12-09 12:52:08
I am working on making the ramp thread start and stop itself when triggered by the motion detected flag. getting close


2017-12-09 13:40:30
Further details about python threads I dont have time to understand at the moment. however...
it occurs to me I don't necessarily need to start/stop the thread - I just need to toggle a flag - sone state dies soemthing (decrements opacity) and the other state does nothing


2017-12-09 13:50:58
fantastic, I have the ramp state switching mechanism working
how to call that on motion detect?
state 0:
	init: opacity = 1.0
	decrement opacity for mix

state 1:
	init: opacity = 0.0


2017-12-09 14:24:22
great - that ramp function is working for real now
testing w conditional boundary on one of the states
great, that works
testing w motion detection trigger
need to make it initialize counter when state is set to true


2017-12-09 14:31:44
great - I implemented an init state for the ramp when it gets set to true
testing w motion detection again
great - that's woprking as expected


2017-12-09 14:33:51
applying this mechanism to mix opacity now


2017-12-09 14:40:37
omg its working


2017-12-09 14:46:33
its working great but I wonder if it could be even smoother
currently when the detection flag is set
mix opacity immediately jumps to 1.0 and then the update function starts decrementing

what if - instead of initializing to 1.0
the increment was set to a positive value
so it would increment up to 1.0
and when it hit that value the increment would be set to a negative value
so it would increment down to 0.0


2017-12-09 15:33:02
totally working :)



2017-12-09 16:20:48
- test saving  functions

2017-12-09 17:54:37
fine tuning at the noizefloor venue


2017-12-10 17:38:04
The show was quite a success, and everyone had a good time, several people spoke to me about their appreciation of the intimacy the experience provided. Met new people, and maybe started a new friendship.

In fact, the show was great. At least two people were very excited about what they were seeing, and thought it was brilliant. The coolest thing he'd ever seen, said one felow

Norm Alien paid me a great complement when he said I only go on instagram to look at pretty girls and your feed. lol, but yeah!

Many ideas to explore from here
- multiple camera (combining images)
- incorproation of non hallucinated imagery
- new multithreaded Viewport - decoupled from deepdream rendering
- post processing
- multiprocessing
- additional inputs (audio/midi)
- multiple viewports


2017-12-10 17:43:28
not so thrilled with the runtime captures - they'll probably be ok for video looping and certain stills, but I don't feel like I'm seeinmg all the iterations and I'm not seeing the ghosted webcam compositing


2017-12-11 20:31:36
studying Python
with statement
decorators


2017-12-11 22:02:29
functions


2017-12-12 08:45:59
continuing a review of python functions, which will lead up to:
- the "with" construct
- the decorator construct


2017-12-12 09:55:11
came across this interesting discussion on the deepdream reddit about motion processing
https://www.reddit.com/r/deepdream/comments/3cadj8/people_are_doing_videos_incorrectly/

in particular it seems that you can run optical flow on successive frames:
 can use the function cv2.calcOpticalFlowFarneback on a pair of successive frames instead of extracting the flow from the encoded video.


2017-12-12 10:01:55
back to python

it turns out that closures - the fact that functions remember their enclosing scope - can be used to build custom functions that have a hard-coded argument

def outer(x):
	def inner():
		print x + 1
	return inner

# custom functions w hardcoded params
custom1 = outer(10)
	outer() returns inner, which contains a reference to a variable "x" that was created when outer was called.
custom2 = outer(100)

custom1()
11

custom2()
101

# we're building custom versions of the inner function that remember what number they should print
def
# outer is like a constructor for inner with x acting like a private member variable


2017-12-12 10:11:37
finally, on to decorators

A decorator is just a callable that takes a function as an argument and returns a replacement function

def outer(some_func):
	def inner():
		print 'before some_func'
		ret = some_func()
		return ret + 1
	return inner

def foo():
	return 1

foo()
1

outer(foo)()
before some_func
2

Part of why I've had a hard time understanding decorators was because I didnt understand function calling. In the example above, outer will return the function 'inner' when called. that return value (being a function) can itself be called. literally:

outer(foo)()
outer(foo) -> returns inner
inner contains the return of foo()
inner returns a modified value of foo() - in this case, it adds 1
calling outer(foo) - written as outer(foo)() calls inner(), which is regarded as the "decorator"

its more likely that instead ouf calling outer(foo)(, you would assign outer(foo) - whose output will be the paramterized function inner() - to a variable

decorated = outer(foo)
decorated()

We can say that the variable decorated is a decorated version of foo  - decorated by inner. In this case, it is literally foo() plus something

if we wrote a useful decorator we might want to replace foo with the decorated version altogether so we always got our "plus something" version of foo when we called it

foo = outer(foo)

instead of writing sopmething like
sub = wrapper(sub)

we finally introduce the pythin decorator syntax

@wrapper
def sub(a,b):
	# something...


2017-12-12 16:18:22
spent most of the day understanding python functions and decorators


2017-12-14 06:47:05
merged code to master branch in preparation for work on the renderer


2017-12-14 06:57:53
studying python
the "with" statement
the "try" statement

The with statement is an error handling statement similar to the try statement
with is used to clean up objects automatically, typically opening files, but many other applications

set things up
try:
	do something
finally:
	tear things down

The Try statement also allows for exception handling, more on this as necessary



2017-12-14 08:01:07
moving on to multiprocessing in Python


2017-12-14 16:02:44
continuing with python study


2017-12-14 18:11:59
copntinuing to study pythions multiprocessing module, which apparently uses same syntax as the threading module.


2017-12-15 09:40:46
continuing further study of pythin multiprocessing module


2017-12-15 09:49:09
as a refresher, what have I learned about multiprocessing so far

The multiprocessing module API is based on the API for threading (which I've already used)

Process()
	target function
		can pass args or kwargs to this
	determining current process
		multiprocessing.current_process().name can be called within each process, and it identifies itself
		multiprocessing.pid is the numeric ID
	daemon processes
		by default the main program will not exit until all the children have exited, can override this default Process().daemon = true/false
	waiting for processes
		To wait until a process has completed its work and exited use the join() method
		Block the calling thread until the process whose join() method is called terminates or until the optional timeout occurs.
		The name join is used because the multiprocessing module's API is meant to look as similar to the threading module's API, and the threading module uses join for its Thread object. Using the term join to mean "wait for a thread to complete" is common across many programming languages, so Python just adopted it as well.
		by default, when the main process is ready to exit, it will implicitly call join() on all running multiprocessing.Process instances.
	Terminating processes
	logging
		There is a convenient module-level function to enable logging called log_to_stderr(). It sets up a logger object using logging and adds a handler so that log messages are sent to the standard error channel.

MULTIPROCESSING SUPPORTS 2 TYPES OF COMMUNICATION CHANNELS BETWEEN PROCESSES:
As with threads, a common use pattern for multiple processes is to divide a job up among several workers to run in parallel. Effective use of multiple processes usually requires some communication between them, so that work can be divided and results can be aggregated.

	Queue
		A way to pass information between processes
		There is the basic Queue() machine, but also a JoinableQueue() machine. What is the difference between them?

			from multiprocessing import Queue
			q = Queue()
			q.put(item) # Put an item on the queue
			item = q.get() # Get an item from the queue

			from multiprocessing import JoinableQueue
			q = JoinableQueue()
			q.task_done() # Signal task completion
			q.join() # Wait for completion

		so... JoinableQueue has methods join() and task_done() which Queue hasn't

	Pipe
		returns a pair of "connection" objects which by default is 2-way

USING A POOL OF WORKERS

	Pool
		manages a fixed number of processes where the work can be broken up and distributed between processes independently

		the return values from the jobs are collected and returned as a list.

		ny default Pool creates a fixed number of worker processes and passes jobs to them until there are no more jobs. setting the maxtasksperchild parameter tells the pool to restart a worker process after it has finished a few tasks. this can be used to avoid having long ruinning workers consumer system resources.

Event
	Another way to pass information between processes, but typically state information (set/unset) with additional management for listening and timers, etc.

Lock
	Provides a way to control access to resources

Semaphore
	Allows a resource to be acessed by more than one process at a time

Condition
	Synchronizes workflow between processes so that they run in parallel of sequentially

Manager
	coordinates shared information between its users
	can create a shared namespace




2017-12-15 17:58:22
continuing  python study. still going through multiprocessing. came across a script I'm studying further to understand some basics. One new concept I've come across over the last few days is how to use classes more effectivel


2017-12-16 10:14:12
continuing to work my way thru the concepts in the multiprocessing module. I'm not fully understanding the example about events. with and without timeout

	an event can be toggled between set and unset states
	users of the event object can wait for it to change from unset to set, using an optional timeout value




2017-12-16 10:33:00
found a better example of event behavior, along with a neat bit of code :
pool.map_async( func, [i for i in range()])

map( aFUnction, aSequence)
One of the common things we do with lists and other sequences is applying an operation to each item and collect the result.
>>> items = [1, 2, 3, 4, 5]
>>> squared = []
>>> for x in items:
	squared.append(x ** 2)

	can be expressed with map, like this:
	items = [1, 2, 3, 4, 5]
>>> def sqr(x): return x ** 2
>>> list(map(sqr, items))
[1, 4, 9, 16, 25]



2017-12-16 14:23:04
more info on multiprocessing events can be found in the Threading.Event documentation


2017-12-16 14:37:18
purchased domain syntheticaf.com
I am going to change my DBA name to this in the next month


2017-12-19 11:33:33
diving back into the multiprocessing module
when I last was here, I was confused about Events, had seen a couple of ways to implement and didn't really understand some python fundamentals it seemed.

	- we create an event object
	e = multiprocessing.Event()

	1 we create a process/processes and pass the event to target function as an argument
	w = multiprocessing.Process(target=func, args=(e,))

I think I get it now

event = None
def my_setup(event_):
  global event
  event = event_
  print "event is %s in child" % event

if __name__ == "__main__":
    event = multiprocessing.Event()
    p = multiprocessing.Pool(2, my_setup, (event,))
    print "event is %s in parent" % event
    p.close()
    p.join()

the above example creates an event instance in the global namespace
we create a pool of processes that target some function and pass a reference to the event instance to each
each process in the pool is "synchronized" to the event object in the global namespace

event = None

def my_worker(num):
    print "event is %s in child" % event #inherited from parent namespace

if __name__ == "__main__":
    event = multiprocessing.Event()
    pool = multiprocessing.Pool(2)

    # let's call my_worker for every process in the pool.
    pool.map_async(my_worker, [i for i in range(pool._processes)])

    pool.close()
    pool.join()
    print "event is %s in parent" % event

HOWEVER...
Passing a global event instance as an argument to a target function isn't necessary. By default, we inherit the global namespace upon  creating an instance of a Pool. So the target function can reference "event" as if it had been globally define, which in fact - it was.


2017-12-19 12:16:30
Controlling access to resources using Lock
in situations where a single resouce needs to be shared between multiple processes, a lock can be usind to avoid conflicting accesses.


2017-12-19 12:24:21
no idea what the example is showing me.


2017-12-19 14:01:07
moving on to Synchronizing Operations with the Condition() object


2017-12-19 14:13:15
the provided example uses the python with: statement - not fully clear on how that works.

	The with statement is used to wrap the execution of a block with methods defined by a context manager

	This allows common try…except…finally usage patterns to be encapsulated for convenient reuse.

	The execution of the with statement with one "item" proceeds:
	1. the context expression is evaluated to obtain a context manager
	2. the context manager's __exit__() is loaded for future use
	3, the context manager's __enter__() method is invoked
	4. if a target was included in the with statement, the return value from __enter__() is assigned to it
	5. The suite is executed
	6. the context manager's __exit__() method is invoked

	A common usage pattern is a File Handler.
	When manipulating files in Python your code performs the following steps:
	1. open a file
	2. do stuff with file
	3. close open files

	def read_log_file(self, the_file):
		f = open(the_file, 'r')
		lines = f.readlines()
		f.close()

This can also be expressed as so:

	def read_log_file(self, the_file):
		with open(test_file, "r") as f:
			lines = f.readlines()
		return lines

Or similarly, using Try, Except, Finally:

	def read_log_file(self, the_file):
		try:
			f = open(test_file, 'r')
			lines = f.readlines()
		except:
			raise Exception
		finally:
			f.close()
		return lines

Context managers are just Python classes that specify the
__enter__ and __exit__ methods

the __enter__() method is where you put the code that is ghoing to run before you enter the scope of the with block

the __exit))() method is where you put the code that you want to leave the scope of the with block

with is handy when you have two related operations which you’d like to execute as a pair, with a block of code in between. The classic example is opening a file, manipulating the file, then closing it:


2017-12-19 15:04:36
skipped past the section about multiprocess.Manager()
moving on to Process Pools


2017-12-19 19:00:58
just for fun
[10] * 3
..[10,10,10]


2017-12-19 19:18:22
I've read about as much as I can about multiprocessing


2017-12-23 13:43:07
I'm archiving the year's style transfer renderings
prelimanry setup work which can apply to
- storefront
- gallery section
- rethink site strategy (?)
- 	deepdreamvisionquest is a sub-project of SyntheticAF, a Skinjester company

2017-12-28 11:44:06
continuing work on what has turned into an archiving project
I want to make some further moves on my site and make it more actionable overall, perhaps even profitable, but need to know what I have available to share, and curate that collection. Instagram has been a good benchmark for what people like, and for the kinds of images that seem tomake a difference. There are other avenues where I want to expose this work as well
- behance
- pinterest

2017-12-29 22:04:20
I've collated all style transfer work into named bins in lightroom, goiong through and curating them now

2017-12-31 18:16:32
have organized and culled all style transfer in LR folders
making some intitial collections
adding new work

2017-12-31 20:12:57
completed archiving project

2017-12-31 20:31:55
creating series - finding images that go together
- Class M
- House of El


2018-01-01 15:36:04
setting up the JCJohnson neural-style repo on LINUX machine




2018-01-01 16:05:16
and then I found myself re-installing torch/Luayes after removing prior install
compilation errors upon some of the dependencies listed in the neural-style readme
starting again

INSTRUCTIONS
https://github.com/skinjester/neural-style/blob/master/INSTALL.md

2018-01-01 16:17:40
installed Torch without incident
  ______             __   |  Torch7
 /_  __/__  ________/ /   |  Scientific computing for Lua.
  / / / _ \/ __/ __/ _ \  |  Type ? for help
 /_/  \___/_/  \__/_//_/  |  https://github.com/torch
                          |  http://torch.ch


Optional dependencies:

For CUDA backend:
x CUDA 6.5+
gary@HALLUCINATR:~$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2016 NVIDIA Corporation
Built on Tue_Jan_10_13:22:03_CST_2017
Cuda compilation tools, release 8.0, V8.0.61

x cunn
	built without incident
Updating manifest for /home/gary/torch/install/lib/luarocks/rocks
cunn scm-1 is now built and installed in /home/gary/torch/install/ (license: BSD)

- loadcaffe
	x depends on google protocol buffer library
	gary@HALLUCINATR:~$ protoc --version
	libprotoc 2.6.1

		already installed from deepdream setup

loadcaffe installed without incident
loadcaffe 1.0-0 is now built and installed in /home/gary/torch/install/ (license: BSD)

th -e "require 'cutorch'; require 'cunn'; print(cutorch)"
{
  createCudaUVATensor : function: 0x402501d0
  getPeerToPeerAccess : function: 0x40255ba0
  getStream : function: 0x40255f58
  isCachingAllocatorEnabled : function: 0x40255e68
  getDeviceCount : function: 0x40255ac0
  isManaged : function: 0x40250230
  setHeapTracking : function: 0x40258c28
  manualSeedAll : function: 0x40258b38
  streamWaitFor : function: 0x40256000
  toCudaUVATensor : function: 0x40250210
  toFloatUVATensor : function: 0x402501f0
  setKernelPeerToPeerAccess : function: 0x40255da8
  reserveBlasHandles : function: 0x40255a98
  manualSeed : function: 0x40258ae8
  hasHalfInstructions : function: 0x40258ec8
  getBlasHandle : function: 0x40255c90
  hasFastHalfInstructions : function: 0x40258f20
  setDefaultStream : function: 0x40255fb0
  getMemoryUsage : function: 0x40258e70
  createCudaHostIntTensor : function: 0x4024ffe0
  streamBarrier : function: 0x402560b0
  createCudaHostLongTensor : function: 0x40250060
  seedAll : function: 0x40258f98
  createCudaHostHalfTensor : function: 0x40250128
  driverVersion : 9000
  CudaUVAAllocator : torch.Allocator
  synchronize : function: 0x402553f8
  createCudaHostByteTensor : function: 0x402500e0
  reserveStreams : function: 0x40255ce0
  createCudaHostDoubleTensor : function: 0x4024ff68
  getDevice : function: 0x40256190
  createCudaHostFloatTensor : function: 0x4024ff00
  withDevice : function: 0x4024fe30
  seed : function: 0x40258f70
  test : function: 0x4024fdc8
  _stategc : userdata: 0x41d2d790
  getNumStreams : function: 0x40255d30
  getRuntimeVersion : function: 0x40258dc8
  deviceReset : function: 0x402561e0
  Event : {...}
  CudaHostAllocator : torch.Allocator
  isManagedPtr : function: 0x40258c50
  getState : function: 0x40258c00
  setRNGState : function: 0x40258bb0
  synchronizeAll : function: 0x40255a40
  initialSeed : function: 0x40258ac0
  getDeviceProperties : function: 0x40255ec0
  getRNGState : function: 0x40258b88
  getNumBlasHandles : function: 0x40255b28
  _sleep : function: 0x40258b60
  setStream : function: 0x40255d80
  getKernelPeerToPeerAccess : function: 0x40255e08
  createFloatUVATensor : function: 0x40250190
  createCudaHostTensor : function: 0x4024ff00
  getDriverVersion : function: 0x40258e20
  streamSynchronize : function: 0x40256168
  streamWaitForMultiDevice : function: 0x40256060
  setDevice : function: 0x40258f48
  setPeerToPeerAccess : function: 0x40255bf8
  hasHalf : true
  streamBarrierMultiDevice : function: 0x40256110
  setBlasHandle : function: 0x40255b78
  _state : userdata: 0x00db9030
}


- download pretrained neural networks
cd neural-style


2018-01-01 17:00:01
created AWS account. Waiting for sign-up to complete. Reading up on how it works


2018-01-01 17:15:04
before setting up on AWS here's what needs to be done:

- install docker-machine on local desktop
- have an account on AWS
	+ create access/secret key pair
	+ open ticket to AWS support to increas the limit of P2 or G2 instances available


2018-01-01 17:17:51
still waiting for neural network models to download from local neural-style setup


2018-01-01 17:18:51
reviewing some Python ideas while I wait.

DECORATORS
MULTIPROCESSING


2018-01-01 19:05:45
Amazon AWS acct is up and running
reading up on the P2 instance type which incorporates up to 8 nvidia Tesla K80 GPU's



2018-01-01 20:29:57
Virtual machines on AWS EC2, also called instances, have many advantages
- highly scalable
- easy to start/stop

2018-01-01 20:38:40
setting up an instance
Key pair name:scificavepainting


2018-01-01 20:51:00
You have requested more instances (1) than your current instance limit of 0 allows for the specified instance type. Please visit http://aws.amazon.com/contact-us/ec2-request to request an adjustment to this limit.

submitted request to increase limit of P2 instances I can use. currently 0. requested 1


2018-01-02 07:51:14
Amazon Web Services
Jan 1, 2018
11:31 PM -0800

Hello,

We have approved and processed your limit increase request(s).  It can sometimes take up to 30 minutes for this to propagate and become available for use.  I hope this helps, but please reopen this case if you encounter any issues.

Summary of limit(s) requested for increase:

  [US West (Oregon)]: EC2 Instances / Instance Limit (p2.8xlarge), New Limit = 1

AWS is setup as needed now


2018-01-02 22:45:48
installing docker
gary@HALLUCINATR:~$ docker-machine version
docker-machine version 0.13.0, build 9ba6da9


2018-01-02 22:58:10
I think I'm setup... here goes
It looks like the docker-machine command will create the EC2 instance?


2018-01-02 23:32:28
had to setup an administrator account and workgroup in AWS console
username: Administrator
passwd: Helvetica99
amazonec2-access-key AKIAIT5NE5ZJHUGYFKIQ
amazonec2-secret-key 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


docker-machine create --driver amazonec2 \
--amazonec2-instance-type p2.8xlarge \
--amazonec2-access-key AKIAIT5NE5ZJHUGYFKIQ \
--amazonec2-secret-key 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 nvidia-docker-1



2018-01-02 23:48:44
having some trouble getting this working. The machine setup spins up for a bit then fails out with this message

gary@HALLUCINATR:~$ docker-machine create --driver amazonec2 \
> --amazonec2-instance-type p2.8xlarge \
> --amazonec2-access-key AKIAIT5NE5ZJHUGYFKIQ \
> --amazonec2-secret-key 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 nvidia-docker-lg
Running pre-create checks...
Creating machine...
(nvidia-docker-lg) Launching instance...
Error creating machine: Error in driver during machine creation: Error launching instance: InstanceLimitExceeded: You have requested more instances (1) than your current instance limit of 0 allows for the specified instance type. Please visit http://aws.amazon.com/contact-us/ec2-request to request an adjustment to this limit.
	status code: 400, request id: 6d8f05e8-ec86-4e41-a7e2-487c29fa010e

NEXT WORKSESSION
- verify that I can create p2 instance type from amazon console
- reboot system to make sure there isn't some liongering issue w docker-machine
- is it because created a new user and the new user did not setup a new instance limit?


2018-01-03 09:30:14
apparently unable to create a p2 instance from the web-based console as well


2018-01-03 09:40:57
apparently now able to create a p2 instance. Only change's I made were to:
- login under the Administror acct I created last nite (instead of AWS root user)
- created a new key pair admin-syntheticAF.pem


2018-01-03 09:44:54
attempting to connect to the newly  created inmstance using SSH
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for 'admin-syntheticAF.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "admin-syntheticAF.pem": bad permissions
Permission denied (publickey).


2018-01-03 09:46:23
successfully connected to created instance
gary@HALLUCINATR:~$ ssh -i "admin-syntheticAF.pem" ubuntu@ec2-34-212-180-26.us-west-2.compute.amazonaws.com
=============================================================================
       __|  __|_  )
       _|  (     /   Deep Learning AMI  (Ubuntu)
      ___|\___|___|
=============================================================================

Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-1022-aws x86_64v)

Please use one of the following commands to start the required environment with the framework of your choice:
for MXNet(+Keras1) with Python3 (CUDA 9) _____________________ source activate mxnet_p36
for MXNet(+Keras1) with Python2 (CUDA 9) _____________________ source activate mxnet_p27
for TensorFlow(+Keras2) with Python3 (CUDA 8) ________________ source activate tensorflow_p36
for TensorFlow(+Keras2) with Python2 (CUDA 8) ________________ source activate tensorflow_p27
for Theano(+Keras2) with Python3 (CUDA 9) ____________________ source activate theano_p36
for Theano(+Keras2) with Python2 (CUDA 9) ____________________ source activate theano_p27
for PyTorch with Python3 (CUDA 9) ____________________________ source activate pytorch_p36
for PyTorch with Python2 (CUDA 9) ____________________________ source activate pytorch_p27
for CNTK(+Keras2) with Python3 (CUDA 8) ______________________ source activate cntk_p36
for CNTK(+Keras2) with Python2 (CUDA 8) ______________________ source activate cntk_p27
for Caffe2 with Python2 (CUDA 9) _____________________________ source activate caffe2_p27
for base Python2 (CUDA 9) ____________________________________ source activate python2
for base Python3 (CUDA 9) ____________________________________ source activate python3

Official Conda User Guide: https://conda.io/docs/user-guide/index.html
AWS Deep Learning AMI Homepage: https://aws.amazon.com/machine-learning/amis/
Developer Guide and Release Notes: https://docs.aws.amazon.com/dlami/latest/devguide/what-is-dlami.html
Support: https://forums.aws.amazon.com/forum.jspa?forumID=263

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

30 packages can be updated.
14 updates are security updates.


*** System restart required ***

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ubuntu@ip-172-31-0-105:~


2018-01-03 09:47:44
terminated instance from EX2 console



2018-01-03 10:19:03
same instance limit message as before when I attempt to creat a new docker machine



2018-01-03 10:27:26
submitted a new limit increase request, this time when logged in as my IAM Administrator acct.Waiting for response (should take a few hours)


2018-01-03 12:06:47
What is SSH?
- crypotographic network protocol for operating network services securely over an uinsecured network.
- bext known application if for remote login to a command line
- designed as a replacement to Telnet



2018-01-03 12:25:12
from what I;m seeing in the EC2 limit view I have access to a single p2.8xlarge instance

- verify that I can create p2 instance type from amazon console
	- YES
- reboot system to make sure there isn't some liongering issue w docker-machine
	+ YES
- is it because created a new user and the new user did not setup a new instance limit?
	+ NO
- is it because I'm looking at the wrong kine of limit?
	+ What is a Host Limit?
		* currently states: RUnning On-Demand p2 hosts: 0
		* A host (or dedicated host) is a physical server with ec2  instance capacity fully dedicated to your usage
		*

NEXT
- read thru docker's Amazon Web Services docs

WHat is Docker-Machine?
- a tool that lets you install docker engione on virtual hosts (such as EC2) and manage the hosts with docker-machine commands
	+ point the machine CLI at a running managed host and you can run docker commands directly on that host
- previous to Docker v1.12 machine wa sthe only way to run Docker on Mac or Windows

If you want to run docker commands locally, all you need to do is download ansd install Docker Engine
If you want to run  docker comands  remotely, use docker-machine

When people say “Docker” they typically mean Docker Engine
	- client-server application made up of
	- 	the Docker daemon
	- 	a REST API that specifies interfaces for interacting with the daemon
	- 	a command line interface (CLI) client that talks to the daemon (through the REST API wrapper).

Docker Engine accepts docker commands from the CLI, such as docker run <image>, docker ps to list running containers, docker images to list images, and so on.

Docker Machine is a tool for provisioning and managing your Dockerized hosts (hosts with Docker Engine on them).
	- Typically, you install Docker Machine on your local system
	- Docker Machine has its own command line client docker-machine and the Docker Engine client, docker
You can use Machine to install Docker Engine on one or more virtual systems.
	- These virtual systems can be local (as when you use Machine to install and run Docker Engine in VirtualBox on Mac or Windows)
	- or remote (as when you use Machine to provision Dockerized hosts on cloud providers


2018-01-03 12:47:21
uninstalled docker-machine
re-installing docker-machine
gary@HALLUCINATR:~$ docker-machine version
docker-machine version 0.13.0, build 9ba6da9



docker-machine create -d amazonec2 \
--amazonec2-region us-west-2 \
--amazonec2-instance-type "t2.micro" \
--amazonec2-access-key AKIAIT5NE5ZJHUGYFKIQ \
--amazonec2-secret-key 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 \
aws-test

ran this without incident and created this instance, however unable to login to the shell



2018-01-03 14:20:38
after entering
docker-machine ssh aws-test

I'm now in a shell on the EC2 instance

how do I terminate this instance. can I do so from the command line?
docker-machine rm aws-test

looking in EC2 dashboard, the created instance is shutting down
aws-test is now terminated

If I'd started w this article it would have saved a lot of time:
https://alexanderzeitler.com/articles/a-lap-around-aws-and-docker-machine/


2018-01-03 22:35:32
making the attempt again

docker-machine create -d amazonec2 \
--amazonec2-region us-west-2 \
--amazonec2-ami ami-d8bdebb \
--amazonec2-instance-type p2.8xlarge \
--amazonec2-access-key AKIAIT5NE5ZJHUGYFKIQ \
--amazonec2-secret-key 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 nvidia-docker-test2


2018-01-03 22:38:59
it is running!

trying to setup nvidia drivers, running into some issues

ERROR: Unable to load the kernel module 'nvidia.ko'.  This happens most frequently when this kernel module was built against the wrong or
       improperly configured kernel sources, with a version of gcc that differs from the one used to build the target kernel, or if a driver such
       as rivafb, nvidiafb, or nouveau is present and prevents the NVIDIA kernel module from obtaining ownership of the NVIDIA graphics device(s),
       or no NVIDIA GPU installed in this system is supported by this NVIDIA Linux graphics driver release.

       Please see the log entries 'Kernel module load error' and 'Kernel messages' at the end of the file '/var/log/nvidia-installer.log' for more
       information.


ERROR: Installation has failed.  Please see the file '/var/log/nvidia-installer.log' for details.  You may find suggestions on fixing installation
       problems in the README available on the Linux driver download page at www.nvidia.com.




2018-01-04 08:37:51
I think the problem with the nvidia-docker install ast night may have had something to do with the nvidia drivers? I'm going to create another test instance and step through it again. No idea what the proper drivers are, but working thru some steps found at
https://deepdive.tw/2016/12/17/installing-nvidia-gpu-driver-and-nvidia-docker-in-ubuntu-ec2-instance/
https://github.com/NVIDIA/nvidia-docker/wiki/Deploy-on-Amazon-EC2



2018-01-04 09:52:44
P@ instances use NVIDIA Tesla K80 GPU




2018-01-04 09:54:43
before deploying GPU containers we first need to provision an EC2 P2 instance

docker-machine create --driver amazonec2 \
                      --amazonec2-region us-west-2 \
                      --amazonec2-zone c \
                      --amazonec2-ami ami-efd0428f \
                      --amazonec2-instance-type p2.8xlarge \
                      --amazonec2-vpc-id vpc-cf4f82b6 \
                      --amazonec2-access-key AKIAIT5NE5ZJHUGYFKIQ \
                      --amazonec2-secret-key 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 \
                      aws01

EC2 instance is up and running

Once the provisioning is completed, we install the NVIDIA drivers and NVIDIA Docker on the newly created instance (using a Ubuntu 16.04 AMI).
- Note that if you create a custom AMI, you could simply reuse it instead of doing what follows:

2018-01-04 11:17:44
omg. its working


2018-01-04 12:31:17
I'm using the docker image. It shows the GPU config from nvidia-smi as:
ubuntu@aws01:~$ nvidia-smi
Thu Jan  4 20:32:11 2018
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 387.26                 Driver Version: 387.26                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla K80           Off  | 00000000:00:17.0 Off |                    0 |
| N/A   36C    P8    27W / 149W |     11MiB / 11439MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   1  Tesla K80           Off  | 00000000:00:18.0 Off |                    0 |
| N/A   30C    P8    30W / 149W |     11MiB / 11439MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   2  Tesla K80           Off  | 00000000:00:19.0 Off |                    0 |
| N/A   41C    P8    27W / 149W |     11MiB / 11439MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   3  Tesla K80           Off  | 00000000:00:1A.0 Off |                    0 |
| N/A   35C    P8    30W / 149W |     11MiB / 11439MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   4  Tesla K80           Off  | 00000000:00:1B.0 Off |                    0 |
| N/A   39C    P8    26W / 149W |     11MiB / 11439MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   5  Tesla K80           Off  | 00000000:00:1C.0 Off |                    0 |
| N/A   32C    P8    29W / 149W |     11MiB / 11439MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   6  Tesla K80           Off  | 00000000:00:1D.0 Off |                    0 |
| N/A   42C    P8    27W / 149W |     11MiB / 11439MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   7  Tesla K80           Off  | 00000000:00:1E.0 Off |                    0 |
| N/A   34C    P8    31W / 149W |     11MiB / 11439MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+




2018-01-04 12:33:47
cloning the https://github.com/albarji/neural-style-docker repo
cloning https://github.com/jcjohnson/neural-style


2018-01-04 12:37:45
seeing how to stop the machine and restart from where I left off


2018-01-04 12:40:40
looks like I can manage stopping directly from docker-machine on my local machine. EC2 console shows the machine entering the stopped state


2018-01-04 12:50:32
so yes, everything is as I left it.
need to verify dependencies though
https://github.com/jcjohnson/neural-style/blob/master/INSTALL.md

Step 1: Install torch7
http://torch.ch/docs/getting-started.html#_
ubuntu@aws01:~/torch$ th

  ______             __   |  Torch7
 /_  __/__  ________/ /   |  Scientific computing for Lua.
  / / / _ \/ __/ __/ _ \  |  Type ? for help
 /_/  \___/_/  \__/_//_/  |  https://github.com/torch
                          |  http://torch.ch

th>


2018-01-04 13:03:10
Step 2: Install loadcaffe


2018-01-04 13:04:22
download the pretrained neural network models:
ok


2018-01-04 13:07:20
CUDA is missing


2018-01-04 13:09:10
There are AMI's offered that pre-include basic ML tools and libraries. I should be using one of those instead I think


2018-01-04 13:11:38
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=runfilelocal

https://developer.nvidia.com/compute/cuda/9.1/Prod/local_installers/cuda_9.1.85_387.26_linux


also - how to create my own AMI so I don't need to rebuild this machine step by step?


2018-01-04 13:20:13
terminated this aws instance
will start again from a ML-focused AMI. did not want to find myself installing dependencies by hand.

I also think I was mis-using the nvidia-docker image that was made
The commands I was sending were to the base machine and not the container
commands to the nvidia-docker container look like this:
nvidia-docker run --rm -v $(pwd):/images albarji/neural-style --content somecontent.png --style somestyle.png

or like this:



2018-01-04 23:42:00
creating new instance using Deep Learning Base AMI (Ubuntu)
Light-weight base AMI with foundational building blocks of deep learning: Nvidia CUDA 8 and 9, CuDNN 6 and 7, CuBLAS 8 and 9, NCCL and more

docker-machine create --driver amazonec2 \
                      --amazonec2-region us-west-2 \
                      --amazonec2-zone c \
                      --amazonec2-ami ami-041db87c \
                      --amazonec2-instance-type p2.8xlarge \
                      --amazonec2-vpc-id vpc-cf4f82b6 \
                      --amazonec2-access-key AKIAIT5NE5ZJHUGYFKIQ \
                      --amazonec2-secret-key 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 \
                      aws01


2018-01-05 09:10:09
running into issues with this since last night
Error creating machine: Error in driver during machine creation: Error launching instance: InvalidBlockDeviceMapping: Volume of size 16GB is smaller than  snapshot 'snap-0756f97fcc5defbbe', expect size >= 50GB
	status code: 400, request id: dbbc039a-5450-4029-992d-d7662f6fbbb2



2018-01-05 22:24:36
- create instance using AMI from EC2 console
	+ ssh into this machine
	+ verify neural-style dependencies

- create instance using AMI from docker-machine




2018-01-05 23:35:42
I created an instance using the Deep Learning Base AMI

I connected to it with ssh
ssh -i "synthetic_rsa.pem" ubuntu@ec2-34-212-176-10.us-west-2.compute.amazonaws.com

Verified CUDA install
ubuntu@ip-172-31-9-143:~$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2017 NVIDIA Corporation
Built on Fri_Sep__1_21:08:03_CDT_2017
Cuda compilation tools, release 9.0, V9.0.176

Checking Torch installation
not present
installing using instructions here: http://torch.ch/docs/getting-started.html


2018-01-06 00:08:20
there's an error with the Torch installation
came across this issue - which may be specific to CUDA 9.
the stated fix, detailed here: https://github.com/torch/torch7/issues/1133
export TORCH_NVCC_FLAGS="-D__CUDA_NO_HALF_OPERATORS__"

re-trying


2018-01-06 00:16:13
installed torch successfully
ubuntu@ip-172-31-9-143:~/torch$ th

  ______             __   |  Torch7
 /_  __/__  ________/ /   |  Scientific computing for Lua.
  / / / _ \/ __/ __/ _ \  |  Type ? for help
 /_/  \___/_/  \__/_//_/  |  https://github.com/torch
                          |  http://torch.ch
th> exit
Do you really want to exit ([y]/n)? y



2018-01-06 00:17:01
install loadcaffe


2018-01-06 00:20:25
install neural-style


2018-01-06 00:21:26
download neural networks


2018-01-06 00:33:57
opened another terminal window and ssh'd into the server
Install CUDA backend for Torch


2018-01-06 00:40:25
will need to figure out how to:
- move material to the server
- move material from the server to local filesystem

2018-01-06 00:54:34
To use scp with a key pair use the following command:
scp -i "synthetic_rsa.pem" ubuntu@ec2-34-212-176-10.us-west-2.compute.amazonaws.com:temp


2018-01-06 01:01:20
transferring cudnn archive to server
while waiting I'll verify that neural-style is working as expected


2018-01-06 01:04:35
its working on the CPU


2018-01-06 01:22:07
its working on the GPU


2018-01-06 01:23:31
installing CuDNN


2018-01-06 01:28:41
CuDNN install does not work, possibly a version mismatch
non-CuDNN rendering works fine though
https://github.com/soumith/cudnn.torch/issues/383


2018-01-06 01:53:39
after finding a fix, CuDNN rendering works now:
git clone https://github.com/soumith/cudnn.torch.git -b R7 && cd cudnn.torch && luarocks make cudnn-scm-1.rockspec

then:
export CUDNN_PATH="/usr/local/cuda-9.0/lib64/libcudnn.so.7"

to verify installation of these dependencies:

```
th
require 'cutorch'
require 'cunn'
require 'cudnn'
```


2018-01-06 01:57:44
not necesaarily seeing a huge speedup w CuNDD< but will need to figure out some benchmarks later. Thrilled to see it working, and will look into muli-gpu rendering next


2018-01-15 16:40:00
remedial python: closures & decorators


2018-01-15 19:28:27
finished up remedial pythond session. I don't knnow why I've become so fixated on decorators really - multiprocessing is what I need to review more urgently. Its just that there's a conceptual shift involved w decorators that I'm not completely grasping. I mean I do get it, and the rate limitring example is pretty useful for the type of stuff I do.

2018-01-26 16:43:28
reviewing my previous multprocessing notes and reacquinting with some Python basics

- what modules do I need to import?

from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Pipe
from multiprocessing import Lock
from multiprocessing import Value



2018-01-27 21:56:49
continuing remedial python cram session



2018-01-27 22:41:57

PROCESS
Process(name, target_func, args)
Process.start()
Process.join()

QUEUE
Queue.put()
Queue.get()

POOL
- these are equivalents to Pythin's built-in apply and map functions
- they will lock the main program until all processes are finished
	Pool.apply()
	Pool.map()

- by contrast the async versions submit all processes at once and retrieve the results as soon as they are finished. We then need to use get() after the apply_async() call in order to obtain the return values of finished processes

Pool.apply_async()
Pool.map_async()


2018-01-27 23:18:16
have learned a bit more about looping in the course of this study. The list comprehension construct in particular:
[some_func for i in range(n)]
[some_func for i in some_list]
its  pretty versatile - and I think there can be conditionals involved here to filter the values returned by the loop

yes, as so:
[some_func for i in some_list if condition ]
jobs = [multiprocessing.Process(target=some_func) for i in range(100) if i%2 == 0 ]


2018-01-27 23:54:28
I think I've learned all I can about the multiprocessing module from examples, I need to think about where the technique fits into my code though. In general, I want to be able to read from the frame buffer at a specific frequency, rather than waiting for the next rendered frame. I am assuming that I'll get multiples of the same frame sometimes, but I think that's ok. That's the basic idea. It can probabl;y be expanded much further.

next worksession
- the try and wait statements continue to be unknowns. I only know about them in the context of error handling, but I'd previously read about using the wait construct as a way to setup an environment, do somethiong. then do something after doing something ETA 30m
- deepdreamvisionquest
	+ site home page
	+ structural work
		* turn blog posts about events into:
			* event listings
			* galleries
		- not sure which. Event Galleries seem like the right choice though
			+ especially because I shouldn't have to stage a show to post work in a gallery
			+  because the event section is intended to be more like a calendar
				*  can create a summary of event gallery in the event listing though (these would all appear in the past events section)


2018-01-28 11:37:36
working on the site again. feeling unfocused. time to set some goals!
x create events for each event blog post
- create event gallery for each event blog post
- remove event blog posts

2018-01-28 13:36:31
events page is looking pretty good after some CSS tweaks and template parameter styling.

2018-01-28 13:44:05
yeah the structure of that page is good. continuing to move in content from event blogs

2018-01-28 13:51:21
the event pager (which identical to what's used in blogs) need some formatting work. Tweaked it, but reverting changes until I work on the blog presentation

2018-01-28 15:36:18
I've populated all the events that need to be there
P1 create event gallery for each event blog post
P1 edit & normalize event posts
	+ include gallery link and thumbnails where relevant
P2 remove event blog posts
- replace photo currently used in bio

2018-01-28 18:13:14
fleshed out artist bio page further. really need a better portrait. A proper headshot on white bkg

2018-01-29 21:17:39
started tonight's worksession
focus is on gallery pages and curation
- create a science fiction cave paionting gallery (mini portfolio)
- create gallery for GDC event
- create gallery for ART+TECH 2016 event

2018-01-29 21:53:34
started with a bit of cleanup for the Event Summary page - which has a ferw things going for it that the event list page does not
- labeled areas "Upcoming" & "Past"
- seperate controls for both lists (show thumbnails for upcoming

2018-01-29 22:02:48
even so - I'll stick with the native element (the event list) until theres a reason not to. coloring in the event tags makes a good difference


2018-01-29 22:58:40
Just chatted with David Myatt about his contact Rose McGowan. Apparently some kind of relationship there. Regardless of that, his timing was right. Solidifies deadline - I told him 2/11/2018 and can stick to that. His questions were fantastic though - real use cases:

David: hmmm. I know she's going to want to see the details... and understand the work, it's process, it's limits and its potential... is there anyway to push for a casestudy like pdf that addresses those questions, and some higher res images?

Gary: What's her interest?

David: For example, could you do graphics at a concert?
Could you do high rez album work?
Could you create filters for photos that her fans could apply to their images?
Could you do work that could be applied to advertising (make up brand).
Is there a way to collaborate with her in LA and you in SF?

yep. hop to it. Let's get you famous!
Also think about music video work and how you might collaborate with a director.
Or if you - might even be... a director.
What kind of work might you be able to do for public rallies (outdoor projections)?
What kind of work could you do in more tradtional speaking engagements?
Perhaps even how you two could collaborate to create "sticky" instagram feed images that are just fun...
She'll be comeing to SF for her book tour.
<<-1>>
I'm trying to nail her down for dinner. Is there any chance the site could be up mid/late Feb?

Gary: Of those cases you've mentioned - the ones I've given thought to arel: hi-rez work (fineart), visuals for brand identity, and projection for live events.

2018-02-01 07:23:34
working on CODAME proposal for exhibition

BIO
Interaction designer Gary Boodhoo uses software, stagecraft and game design to make pictures of minds.

This Jamaican-born machine learning enthusiast turns neural networks inside out to uncover a storehouse of collective memories. "When real AI transforms the world, how will human nature also transform?" Boodhoo asks. His creative practice records emotional connections to objects that viewers can no longer distinguish from themselves.

He describes his current work as science fiction cave painting owing to its freeform roleplay and psychedelic imagery. His video installations have appeared at conferences and festivals around the Bay Area. Boodhoo has a background in game development and is the founder of design studio Synthetic-AF.

2018-02-01 08:50:19
completed 1st draft of ART+TECH proposal

2018-02-01 09:15:53
completed editorial pass for ART + TECH proposal. Ready to send this out as Word doc and PDF

2018-02-01 10:19:05
completed 2nd editorial pass - swapped out some older images with new
exported to Word & PDF
Sening out to Vanessa at CODAME

2018-02-04 14:39:27
Style Transfer Notes

What is it - it's a process where a learning algorithm combines the features of one image with the style of another.
- deep neaural networks are called deep because they have many layers
	+ each layer is good at recognizing parts of an image, lower layers might recognize lines or gradients, a little higher up, the layers might connect lines to form shapes. Even higher up, layers recognize features, like eyes, ears and entire faces.
	+ This recognition isn't engineered, the neaural net learns these distinctions after seeing numerous examples of the same thing
	+ Vision has evolved independently at least 8 times since life emerged, and it now seems that the underlying mechanism behind it is universal.
	+ Neural networks are computer programs - simulations, actually, but they aren't written in a recognizable language. That's why visualization techniques were invented, to better understand how complex neural networks behave. FOr example, do they really understand pictures?
	+ There is a class of pictures, called adversarial images that are designed to fool neural networks.
	+ The images however, may be the exception that proves the rule. To the human eye, there uis something familar about these adversarial images. They appear somehowm, iconic and unspoken. Just like graphic design
		* in graphic design a line is never just a line, its scaffolding. The spaces between things are constructed to arrange information, to please, to convert, etc.
		* You could say them that if vision is like a movie, graphic design is like a myth. Something archaic. Having to do with how perception is engineered.

2018-02-04 14:56:02
the lower neural layers pick up on features like lines, directions, textures and so forth. In real images, these features correspond to color planes, edges and brushstrokes.

the higher neural layers pick up on fully formed features, such as eyes, faces, bodies and environments. In real images, these features will correspond to subject matter or composition.

There are several methods to combine the style of one image with the content of another. One method is to pass noise through the neural net and keep adjusting the pixels until you get lower level features similar to the "style image" and higher level features similar to the "source image". This can be hugely timeconsuming and resource intensive.

Fortunately each neuron in the network performs the same calculations, Instead of running them one at a time on a general purpose CPU, many neural calculatuions can be performed simultaneously on a Graphics Processing Unit (GPU).

Turns out these are widely available because videogames have relied on GPU's for decades.

2018-02-04 15:24:23
PICABO WEBCAM DEMO
Multiple styles are combined in real-time and the resulting style is applied using a "single style transfer network". In the video, the user is an active participant in producing the synthetic image.

- my take on this is that the parameters in the computer program are a "vel 1" conceptual adjustment. There are many effects and output possible by adjusting the values for style calculations. But what about the subject? Real world inputs are always noiy and never the same. The camera and environment provide a vast range of inputs, that are easy to produce and broadly flexible. These are the "level 2" levers I think can speak to the greatest range of artistic intent.

2018-02-04 15:32:42
A QUICK HISTORY OF STYLE TRANSFER

“A Neural Algorithm of Artistic Style"
https://arxiv.org/pdf/1508.06576.pdf
The first paper I came across, which was later implemented in a much-shared repository on github https://github.com/jcjohnson/neural-style

The pastiche image is found via optimization: the algorithm looks for an image which elicits the same kind of activations in the CNN’s lower layers - which capture the overall rough aesthetic of the style input (broad brushstrokes, cubist patterns, etc.) - yet produces activations in the higher layers - which capture the things that make the subject recognizable - that are close to those produced by the content image. From some starting point (e.g. random noise, or the content image itself), the pastiche image is progressively refined until these requirements are met.

This work is considered a breakthrough in the field of deep learning research because it provided the first proof of concept for neural network-based style transfer. Unfortunately this method for stylizing an individual image is computationally demanding.

EARLIER WORKS
this practice falls under the broader category of image-based rendering, which has been studied for the past 60 years.
https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/papers/efros-siggraph01.pdf

Texture analysis and synthesis has had a long history in psychology,
statistics and computer vision. In 1950 Gibson pointed out
the importance of texture for visual perception [8], but it was the
pioneering work of Bela Julesz on texture discrimination [12] that
paved the way for the development of the field. Julesz suggested that two texture images will be perceived by human observers to
be the same if some appropriate statistics of these images match.
This suggests that the two main tasks in statistical texture synthesis
are (1) picking the right set of statistics to match, (2) finding an
algorithm that matches them.

http://mrl.nyu.edu/publications/image-analogies/analogies-fullres.pdf
great examples provided in this paper
http://mrl.nyu.edu/projects/image-analogies/
or on this site

Texture synthesis has many applications including, style transfer, semantic textures (texture by number), super-resolution, removing blur,

2018-02-04 15:55:31
SPEEEDING UP STYLE TRANSFER


2018-02-04 21:06:33
created an email account with Network Solutions for deepdreamvisionquest.com
info@deepdreamvisionquest.com
UNIverse999!@

2018-02-04 21:31:39
verified senting email from that account
unverified sending email to that account - will giove it a minute and see if that functionality comes online soon or if something was misconfigured during acct creation

2018-02-04 22:11:46
having trouble with thiis email;, will need to look into it further later

2018-02-05 00:10:32
I could not change the machine, but instead I showed it something unpredictable—the World.

My video installations show an unpredictable world to a gregarious learning machine through a live camera. My software runs the Deep Dream algorithm continuously on the camera feed. Any changes to that view encourage the neural network to form new interpretations, which are continually being redrawn.




The Jamaican-born interaction designer machine learning enthusiast uncovers collective memories by turning neural networks inside out. "When AI transforms the world will we notice?" Boodhoo asks. His creative practice encourages emotional connections with smart objects that viewers can no longer distinguish from themselves. He describes his current work as science fiction cave painting owing to its freeform roleplay and psychedelic imagery. His video installations have appeared at conferences and festivals across the Bay Area. Boodhoo has a background in game development and is the founder of design studio Synthetic-AF.


Interaction designer Gary Boodhoo uses stagrcraft and expressive code to make pictures of minds. A michine learning adviocate and enthusiast, his work turns neural networks inside out to uncover a storehouse of collective memories.

Interaction designer Gary Boodhoo uses software and stagecraft to make pictures of minds. His creative practice encourages emotional connections with smart objects viewers no longer distinguish from themselves.

2018-02-05 00:29:19
SHORT BIO FOR LAST Festival
Interaction designer Gary Boodhoo turns neural networks inside out to make pictures of minds. A machine learning enthusiast, his creative practice encourages emotional connections with smart objects viewers can no longer distinguish from themselves.

PROJECT DESCRIPTION
Title:
DeepDreamVisionQuest: American Cylon

Description:
This interactive video installation reveals an unpredictable world to a neural network through a live camera. My software finds deep dreams - machine hallucinations synthesized by running the network the wrong way. I wanted to make intimate generative art that engages viewers through constant recognition and novelty.

2018-02-05 02:15:42
collated 4 representative images. Pare that down to 3 and include American Cylon gfx

2018-02-05 09:29:54
sent out revised artist bio, project description and promo images to Emily at LAST Festival

2018-02-05 09:32:05
new email to info@deepdreamvisionquest is online now. Was apparentkly just a matter of waiting for Network Solutions changes to be pushed through their system.

2018-02-05 09:42:05
set up gmail to sort messages to/from info@deepdreamvisionquest.com to its own bundle


2018-02-05 12:32:31
Working on CODAME workshop description

# title
Creating Augmented Narratives Workshop

## subject
With augmented reality as our tool of choice this workshop will teach you how to work with drawings, images, simple 3D shapes, and 3D models.

## activity
We'll not only give 2D work an augmented reality overlay - which can be fun all on it's own! - but also learn how to think about telling, changing, and creating stories that use the unique affordances of AR.



/* secondary detail */*
This workshop will be taught using open source tools available on GitHub. The development environment will be distributed for Mac & Windows machines so we can get to creating art sooner than later. No programming experience is necessary.

2018-02-05 12:46:26
created github repo for project management
under info@deepdreamvisionquest.com account
https://github.com/scificavepainting


2018-02-05 12:55:31

# title
Simplify Sensors for Interactive Installations Workshop with NodeRed

# overview
## problem
Trying to create simple communication between computers, apis and hardware doesn't have to be a programming nightmare.

## solution
Thats where Node-RED comes in. Node-RED is a node-based programming tool for wiring together hardware devices, APIs and online services in new and interesting ways. It provides a browser-based editor that makes it easy to learn and even easier to be creative with.

## activity
In this workshop students well learn how to simplify communication with hardware devices using a ESP32 Wireless Microcontroller, manage data streams with MQTT and explore new ways to connect sensors and LEDs to create interactive installations.

What we'll do: Explore new ways to connect sensors and LEDs to make interactive installations


2018-02-05 13:07:10

# title
FREE business masterclass event in your area that teaches you how to start an online business by leveraging the power of internet marketing.

# problem/aspiration
Most people get another job when they want to earn an additional income,

# solution
instead, you should focus on working smart instead of working hard.

# overview
When you start a business there are things you need
1. You need to be passionate about it
2. You have to start it with little cost
3. It has to take you little time
4. It has to generate an income on the side

# invitation
This actionable training event is perfect for people who are looking to create a second income on the side. You will learn tried and tested strategies and business models that are working in today's market that can be started with zero experience.



2018-02-05 13:08:56

# problem/aspiration
How would you like to find out how to build an online marketing business from scratch using the latest marketing strategies?

# solution
During the Event You Will Learn:
The formula for creating an online business from scratch by using the internet to sell your products, tools and services

# invitation
We will show you how to license other products if you don't want to create them yourself.



2018-02-05 13:09:43

# title
Terrarium Workshops!

# problem/aspiration
Terrariums add a little fun and greenery to any room or office.

# solution
Our workshops will go through the process step-by-step

# invitation
and you’ll go home with a delightful terrarium.You can then personalize your little oasis with anything that makes you smile!


2018-02-05 13:10:16
# title
Resume Workshop

# problem/aspiration
Want to improve your resume?

# solution
Learn how to make your resume stand out and get one-on-one help reconstructing it with recruiters of various tech companies and industry professionals. Bring a copy of your resume and a computer to use for editing it.

# invitation
This workshop is free and open to the public so feel free to share with friends and coworkers. An RSVP is required for each person as we have limited space! Light refreshements be served.


2018-02-05 13:10:57

# title
Sourdough Starter Workshop

# problem/aspiration
In this workshop, you can look forward to a fun, hands-on session going over everything you ever wanted to know about using and maintaining a wild-yeast, naturally fermented sourdough starter.

# solution
By learning the techniques used by artisan bakers, you'll get peak performance from your starter and will learn how to prepare it for baking all your favorites like pizza, flatbread, and traditional rustic loaves.

# activity
In this 2-hour workshop, we'll look at all the angles to feeding and maintaining a healthy sourdough starter, and use it to make a wonderfully crisp and flavorful flatbread in class.

# invitation
You'll go home with your own starter, as well as the knowledge and confidence to use it to bake your own sourdough bread at home.


2018-02-05 13:12:20

Making Beats and Basslines with Ableton Live
An introductory course to learn how to make original beats and music in Ableton Live.


2018-02-05 13:14:58

# title
Deep Learning Weekend Introduction Workshop

# overview
Deep Learning is the biggest change happening in computer science right now. It powers everything from Google’s Alpha Go to Tesla’s autopilot to Amazon’s Echo.

# problem/aspiration
Every company is trying to figure what it’s AI strategy is going to be. Deep learning makes all kinds of new applications possible but presents a whole new set of challenges like exotic hardware and non-determinism. That’s why companies can’t hire experts fast enough.

# invitation
We strongly believe you don’t need a degree from Stanford or MIT to build your own algorithms and use this amazing technology.

# solution
While there are plenty of online resources, we know it's tough to learn a technical topic without a teacher. We're bringing together expert engineers in the field of machine learning, deep learning & AI who will help you learn the basics in a hands-on approach to learning deep learning.

# requirements
This is an extremely hands-on course to take students from little knowledge of deep learning to comfort building real world models. It requires very little math, but reasonably proficient programming skills.

# outcome
At the end of class students will be able to build models on their own, and more importantly be able to quickly find resources to help them with new problems they encounter in their domain.


2018-02-05 13:16:43

# title
Zero to Deep Learning 3 weekends course

# problem/aspiration
The workshop is meant to introduce you to the concepts of machine learning and deep learning

# solution
and provide a solid base to build deeper knowledge in the field.


2018-02-05 13:17:43

# title
Creative Momentum: Project Mapping for Writers, Artists and Academics
Writers, Artists and Academics!

# problem/aspiration
Ready for Clarity, Focus and Project Completion in 2018?
If...
You’re frustrated trying to narrow your ideas and sketches down to one project
Building a finished product out of a great idea feels intimidating
You usually prefer to stay in the initial inspired state, rather than deal with organizing your work
Deadlines stress you out
You feel scattered

# solution
This workshop will help you:
Use creative blocks as windows into your project’s next steps
Make organizing and structuring your project feel meaningful, doable, and exciting

# invitation
Bring your ideas into fruition as a finished piece this year, so you can give yourself and your audience the gift you were meant to create!

# outcome
You'll walk away with...
Your personalized 2018 Project Completion Map
Grounding, Focus, and Motivation
Keys for finding consistent satisfaction in your practice in 2018
Confidence that you will complete your project!


2018-02-05 13:18:31

# title
ArtSpan Artist Workshop: The Inner & Outer Game of Selling Your Art
Is it hard for you to sell your art?

# problem/aspiration
Do you think that being a good sales person requires you to be pushy or manipulative? Are you confused about what to do or say when someone walks into your studio to look at your work? Do you frequently wonder how the art sales process works and how to do it right?


# invitation
If you answered YES to any of these questions then this workshop is for you! Many artists find the sales process difficult and daunting and most do not take the time to learn how to sell. It’s easier to stick to the belief that the art will sell itself or resign to the idea that that you simply do not have the personality to be a good sales person.

# solution
If more artists took the time to learn about selling, they would sell more art, be more successful with their art businesses and actually enjoy selling and getting to know buyers and collectors. What a novel idea!

# outcome
In this workshop you will learn:
The top 5 limiting beliefs that most artists have about the sales process that keep them from making more sales or selling their art all together
A new paradigm for looking at selling that feels more authentic, engaging, and fun
The 8 stages of selling art (from meeting buyers to closing the sale) giving you a clear framework on how to handle the sales process
How to speak about your art in a way that is more interesting and engaging so that people are more likely to buy
Tips and ideas on how to cultivate collectors


2018-02-05 13:19:08

# title
Machine Learning Tutorial

Machine Learning is not just a concept, it has come to our lives. This lecture will introduce methods and techniques for machine learning. After this lecture, you will understand how machine learning works. You will learn the data types including operational or transactional data such as data for sales, cost, and inventory; nonoperational data such as forecast data and macroeconomic data; and metadata, and learn their patterns, associations, or relationships, and how to use this information for decision making. Statistical learning concepts such as regression, classification, decision trees and model reduction techniques such as principal component analysis will be introduced. Specific examples of engineering and businesses using data mining techniques will be introduced in the lecture. To apply the machine learning techniques in your work, however, a 8-week machine learning course will be needed.


First we'll build a neural image synthesizer on a laptop. But then what? This workshop examines methods for constructing narratives and effects using neural style transfer.

2018-02-05 13:20:29

#title
Decolonizing Social Innovation

# problem/aspiration
Decolonizing Social Innovation is a 1-day conference-style retreat dedicated to the idea of dismantling the colonizing practices inherited from our shared colonial past.

# solution
# invitation
This will be a day of exploring how the history of colonization manifests in socially innovative practices today, and sharing practical measures we can each take to engage in intentional cultural shifts to decolonize businesses, products, and daily operations in the world around us.


2018-02-05 16:08:19

# title
Machine Learning for Creativity and Design

#invitation
In the last year, generative machine learning and machine creativity have gotten a lot of attention in the non-research world. At the same time there have been significant advances in generative models for media creation and for design.

# problem/aspiration
The goal of this workshop is to bring together researchers and creative practitioners interested in advancing art and music generationto present new work, foster collaborations and build networks.

# solution
This one-day workshop explores several issues in the domain of generative models for creativity and design. We will look at algorithms for generation and creation of new media and new designs, engaging researchers building the next generation of generative models (GANs, RL, etc) and also from a more information-theoretic view of creativity (compression, entropy, etc).
We will investigate the social and cultural impact of these new models, engaging researchers from HCI/UX communities.
We’ll also hear from some of the artists and musicians who are adopting machine learning approaches like deep learning and reinforcement learning as part of their artistic process.  We’ll leave ample time for discussing both the important technical challenges of generative models for creativity and design, as well as the philosophical and cultural issues that surround this area of research.


2018-02-05 19:50:35
I'm mapping out content to fill the blocks I'fve defined. Just writing mostly will assemble shortly. ETA 1h



2018-02-05 21:40:59

well. mnore than 1h obviously :) Making good progress though on the draft

A Visual Interface for Neural Image Synthesis
We often think of Style as subjective, so how well can software represent those qualities? Artistic style transfer is an AI technique that attempts to apply the style of one image to another. Apps such as Prisma put this technology in anyone's hands and yet there is a point where the novelty becomes a toy. Lacking a pipeline for extending this image making into other creative practices, blah-de-blad de blah blah. We need to go deeper.


2018-02-05 23:10:41
completed 1st draft. Analyzing.

#title
Visual Strategies for Neural Artistic Style Transfer

# invitation ?
We often think of Style as subjective, but how well can software represent those qualities? Artistic style transfer is an AI technique that attempts to apply the style of one image to another.

# problem/aspiration
Apps such as Prisma put this technology in anyone's hands and yet there is a point where the novelty becomes a toy. Without a pipeline for extending this kind of image making into other creative practices, other outputs, it lacks depth. We need to go deeper.

# solution
We'll train and run the style transfer algorithm on a laptop. Our neural network will redraw images from a webcam in the style(s) we choose. Anyone who's ever taken a selfie knows that making interesting pictures means editing the world a bit. We will experiment with strategies for exaggerating the environment and the camera itself. Previous programming experience isn't required. A prepackaged deep learning framework will be available for your machine before the workshop.


2018-02-05 23:24:27
completed 1st editorial pass. The #solution section seems verbose, can it be refactored?


2018-02-05 23:50:26
final candidate

Workshop Description

Visual Strategies for Neural Artistic Style Transfer

We often think of Style as subjective. How well can software represent those qualities? Artistic style transfer is an AI technique that attempts to apply the style of one image to another. Apps such as Prisma put this technology in anyone's hands and yet there is a point where the novelty becomes a toy. Without a pipeline to extend this image making into other creative practices, the outcomes lack depth. We need to go deeper.

We'll train and run the style transfer algorithm on a laptop. Our neural network will redraw images from a webcam in the style(s) we choose. Anyone who's ever taken a selfie knows that making interesting pictures means editing the world a bit. We will experiment with strategies for exaggerating the environment and the camera itself. Previous programming experience isn't required. A prepackaged deep learning framework will be available for your machine before the workshop.


2018-02-07 22:10:42
looking at the jcjohnson fast-neural-tyle repo on github
- do I have all the dependencies installed?
- is the webcam connected? YES



2018-02-07 22:20:58
fast-neural-style is code written to support a paper

Perceptual Losses for Real-Time Style Transfer and Super-Resolution
Justin Johnson, Alexandre Alahi, Li Fei-Fei
Presented at ECCV 2016
https://cs.stanford.edu/people/jcjohns/eccv16/
- Training/test code (uses Torch/Lua)
- Pretrained models
- Live webcam demo




2018-02-07 23:34:34
verified script working on CPU


2018-02-07 23:37:22
running into some issues w GPU - CUDNN related maybe, perhaps I already have it installed?


2018-02-07 23:48:16
there's a flag to disable CUDNN
verified working on GPU
may be worth checking the LINUX dev environemnt on the WIndows machine. I'm not sure how well the dev environment is set up on that - pretty sure it can run deepdreamvisionquest though, so Caffe, CUDA, etyc. at the least. Possibly setup for style transfer and  usnd CUDNN already iof I recall correctly



2018-02-07 23:52:37
need to install a few more packages to support the camera


2018-02-07 23:59:57
and there's a problem installing one of the packages
apparently relate dto opencv


2018-02-08 00:13:32
potentials solution found...
https://github.com/torch/demos/issues/65


2018-02-08 00:19:37
camera input is working, but looks odd.


2018-02-08 00:23:24
interesting - the other models - the ones that aren't "sinstance normalized look as expected"



2018-02-08 00:40:09
fantastic! - found an easy fix. Just update and rebuild Torch. There's a handy scripty provided inside the Torch directory that does so
https://github.com/jcjohnson/fast-neural-style/issues/137

All of the trained networks are working now and yeah - the instance normalized ones look good


2018-02-08 00:42:42
hmm a 1920 x 1080 model causes an out of memeory issue


2018-02-08 00:45:56
1280 x 720 works - appears to use about 10GB on the GPU. CPU is also pretty busy with load average of 3.0



2018-02-08 09:13:45
CODAME workshop post is up. Leading paragraph needs editing

Join us for a workshop on Visual Strategies for Neural Artistic Style Transfer with Gary Boodhoo, using Neural Network and Deep Learning and show the outcome of the work at the CODAME ART+TECH Festival [2018]


2018-02-10 17:31:29
I've setup fast-neural-style of both LINUX machines with ionteresting results

LOCUTUS
Open CV 2.4.13
CUDA 8.044
CuDNN Yes
GPU TitanX Maxwell

HALLUCINATR
Open CV 3.2.0
CUDA 8.061
CuDNN No
GPU TitanX Pascal

The difference between the 2 configurations is significant. For webcam-based use cases: On LOCUTUS I can compute images at 1920 x 1080 or larger, with minimal memory usage on the GPU (no greater than 4GB at any time). On HALLUCINATR, I run out of memory on the GPU at resolutions larger than 1280 x 720. Not sure if the differnes have to do  with:
- presence/absence of CuDNN
- older version of OpenCV requires less memory

My goal is to get the dev environment setup on Macintosh and Windows as well to go through the steps and understand any complications that arise.

# install Torch


2018-02-10 18:23:55
ran into a hitch while getting Torch up
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools)

apparently need to (re)install xcode developer tools to fix the problem
xcode-select --install


2018-02-10 18:28:49
continuing Torch install


2018-02-10 18:41:29
has the terminal crashed? wow.

rebooting


2018-02-10 18:49:42
running the install script again, seems ok so far. maybe something else was the culprit



2018-02-10 18:53:32
has it crashed again??? I was sorta messing around with the window, maybe that was the issue.


2018-02-10 20:09:55
getting this up and running on a Mac is harder than it would appear. Using this guide
https://e-lab.github.io/html/wiki-torch7-installation.html

installing xcode from the app store
--- taking a while


2018-02-10 20:31:05
xcode still installing itself


2018-02-10 21:43:02
xcode installed
installing homebrew -  Homebrew is the easiest and most flexible way to install the UNIX tools Apple didn't include with OS X
https://brew.sh/



2018-02-10 22:09:37
GCC compiler for Multi-threading support
You will need to install GCC >= 4.6 to get proper multithreading support for Torch7 (a known MacOS issue)

gcc 4.9,5 and 6 are available. Using 4.9 as per the example. This should update the existing version from 4.2.1 to 4.9


2018-02-10 22:38:11
te instructions I was using are a couple of years old and the github repo it points to doesnt exist - forging ahead with instructions for installing Torch from Torch quick start
http://torch.ch/docs/getting-started.html


2018-02-10 23:16:49
incredible - Torch framework now installed


2018-02-10 23:44:56
cloned the fast-style-transfer repo to this machine


2018-02-10 23:50:38
needed to modify download model script(s) to use "https:"


2018-02-11 00:00:11
lets see if its working
fantastic - the fast_neural_style script works. pretty slow, not unbearable though

will the webcam demo work?


2018-02-11 00:02:35
problem installing the camera package


2018-02-11 00:09:17
https://github.com/clementfarabet/lua---camera

turns out MacOS needs OpenCV 2.X installed
doing so
using homebrew. nice


2018-02-11 00:14:11
trying camera package install again


2018-02-11 00:14:47
no opencv wasnt the issue error states:
fatal error: 'QTKit/QTKit.h' file not found


2018-02-11 00:28:31
The deprecation of QTKit in current MacOS is a real problem, but it seems thre's a forck of the camera package that claims to support Apple's new AV framework
https://github.com/jdonald/lua---camera



2018-02-11 00:36:04
wow - that worked. And some insights into git as well.
I cloned the lua---camera repo
I fetched a specific change (the modified code changes, including modified rockspec)
I switched to the new branch containing those changes
I was able to muse the local rockspec to add the package (!)


2018-02-11 00:39:10
unfortunately - the other package qtlua, also requires QT4.x


2018-02-11 01:06:05
I don't believe I can go further with this - the webcam demo wont work on current versions of MacOS


2018-02-11 08:14:59
I came across another fast style transfer repo
https://github.com/ghwatson/faststyle
This repository is a Tensorflow implementation of fast neural style transfer, a method by which the content of one image can be fused with the style of another image. It is based upon JC Johnson et al.s' fast style transfer paper combined with D. Ulyanov et al.s' instance normalization paper.
Dependencies
Python 2.7
Tensorflow 1.0.0 (If training: with GPU support + CUDA + cuDNN recommended)
Numpy
OpenCV 3.1.0*

There is a webcam demo as well


2018-02-11 08:22:50
interview with CODAME writer for Medium article today at 11a. Setting up webcam on macbook - o gret, it's plug and play.


2018-02-11 08:39:45
cleaned up camera viewport for simple image - adjusted height of desk. Ready for that call


2018-02-11 09:03:25
installing tensorflow on macbook in python2.7 virtualenv
Note that you must activate the Virtualenv environment each time you use TensorFlow in a new shell. If the Virtualenv environment is not currently active (that is, the prompt is not (<i>targetDirectory</i>), invoke one of the following commands:

$ cd targetDirectory
$ source ./bin/activate

When you are done using TensorFlow, you may deactivate the environment by issuing the following command:

(targetDirectory)$ deactivate


2018-02-11 09:05:22
validating tensorflow install
validated


2018-02-11 09:19:17
need to install opencv 3. I think I can do it through homebrew which was previously installed


2018-02-11 09:37:13
installing opencv3 is a bit more complex. Using these instructions
https://www.pyimagesearch.com/2016/11/28/macos-install-opencv-3-and-python-2-7/

ls /usr/local/Cellar/python/2.7.*/Frameworks/Python.framework/Versions/2.7/lib/python2.7/config/libpython2.7.dylib
/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/config/libpython2.7.dylib


2018-02-11 09:57:17
running into some uncertainty with these steps, whhich assume that I installed a version of python w homebrew, instead of using the python probvided in tensorflow install

jesus this is so confusing



2018-02-11 11:03:20
I'm using a Python installed as part of the TensorFLow install
I'm not using the homebrew Python installs
The tutorials I'm coming across assume that I'm using the Homebrew Python installs
THis makes it indeterminate where opncv is built


2018-02-11 11:06:58

I've de-installed tensorflow. Goping to try installing it differently after installing openCV


2018-02-11 11:08:34
should I be looking fdr a Docker solution to this instead?


2018-02-11 11:34:54
installed Docker, reading through intro


2018-02-11 11:36:57
also worth noting that the system version of Python at /usr/bin/python has openCV 3.4.0 install working fine


2018-02-11 11:39:02
interview rescheduled for next Sunday. Requested calendar invite


2018-02-11 11:40:37
A container is launched by running an image. An image is an executable package that includes everything needed to run an application–the code, a runtime, libraries, environment variables, and configuration files.


2018-02-11 12:09:25
gmail integration for info@deepdreamvisionquest.com either isn't working or is working slowly


2018-02-11 12:11:49
created Docker cloud account
username:
deepdreamvisionquest
password:
Helvetica99


2018-02-11 12:23:45
could this be what I'be been looking for all along?
https://github.com/floydhub/dl-docker

Specs
This is what you get out of the box when you create a container with the provided image/Dockerfile:

Ubuntu 14.04
CUDA 8.0 (GPU version only)
cuDNN v5 (GPU version only)
Tensorflow
Caffe
Theano
Keras
Lasagne
Torch (includes nn, cutorch, cunn and cuDNN bindings)
iPython/Jupyter Notebook (including iTorch kernel)
Numpy, SciPy, Pandas, Scikit Learn, Matplotlib
OpenCV
A few common libraries used for deep learning


2018-02-11 12:51:26
Obtaining the Docker image
You have 2 options to obtain the Docker image
Option 1: Download the Docker image from Docker Hub
docker pull floydhub/dl-docker:cpu (note: this is a 3GB download, will need appropriate free space on machine)

Option 2: Build the Docker image locally
Alternatively, you can build the images locally. Also, since the GPU version is not available in Docker Hub at the moment, you'll have to follow this if you want to GPU version. Note that this will take an hour or two depending on your machine since it compiles a few libraries from scratch.


2018-02-11 12:54:09
Running the Docker image as a Container
Once we've built the image, we have all the frameworks we need installed in it. We can now spin up one or more containers using this image, and you should be ready to go deeper

I created a local directory to serve as a conduit between my machine and the docker image
mkdir ~/dockershare (arbitrary name)

docker run -it -p 8888:8888 -p 6006:6006 -v ~/dockershare:/root/sharedfolder floydhub/dl-docker:cpu bash

this gives me a bash prompt, where I am logged in as root to the docker image


2018-02-11 13:10:04
seeing if I can run fast-style-transfer
everything was installed
script starts running
but states "killed" instead of rendering an image after a short wait

ignoring that for the moment and seeing what happens when I attempt to install the camera packages


2018-02-11 13:25:14
interesting - the additional packages installed without incident
but script fails because it doesn't see the camera
and sure enough, there is no video device listed inside /dev

The script had also complained about missing a graphics output option
Unable to connect X11 server

is there a way to use a Docker image to get visual output?
- Jupyter notebook
	+ would this provide ability to access a webcam though?


2018-02-11 13:53:01
ending worksession here. My conclusion is that MacOS is going to be problematic, at least with regard to a ntive (Docker-less) install. Docker images will work, but it may be necessary to:
- use a Jupyter notebook to run examples
	+ how will this support webcam?
- use some advanced Docker skills to enable a GUI from the Docker container
	+ how will this support webcam

The larger goal is to
- minimize setup issues on multiple platforms
	+ Linux
	+ Windows
	+ MacOS
- enable the usage of the webcam as an input device

I feel that the best course of action for the next worksession is to:
- investigate how Docker can be used with a GUI. Here's a good first step
	+ https://stackoverflow.com/questions/25281992/alternatives-to-ssh-x11-forwarding-for-docker-containers/25334301#25334301

It doesn't matter whether I can install the various dependencies for any platform, because that's a huge blocker (bot for me and for attendants). The self contained Docker approach is great, just need to get gfx out of it. Performance isn't going to be more of an issue than the bottleneck of running the code on the CPU


2018-02-12 19:09:27
hacking again. The goal is to expose a GUI from Docker image
some things to consider
- is Docker on its own my only option here?
- what is virtual box?


2018-02-12 21:16:58
working through the problem with potential solutions from the internet

docker run --rm -e DISPLAY=192.168.0.3:0 \
    -i -t -v /Users/garyboodhoo:/home/timlinux \
    kartoza/qgis-desktop qgis



2018-02-12 21:55:13
that particular solution went nowhere
I'm installing VirtualBox in the hope that I can use a LINUX as virtual machine and pass control from webcam to it more directly.


2018-02-12 23:08:09
attempting to create Ubuntu 16.04 VM
downloading a 1.5GB ISO from Ubuntu site


2018-02-12 23:18:19
this download is taking quite a while - will pick this up in the am


2018-02-12 23:50:53
well, ubuntu has downloaded. continuing


2018-02-12 23:57:37
so after getting Linux installed on this macbook, then what?
- webcam support
- deep learning support
	+ run docker within Linux to prepackage libraries, dependencies?
	+ create virtual machine image with prepackaged libraries, dependencies?


2018-02-13 08:47:37
reviewing some background on VM's
FOund what may be the solution - a detailed Medium post "Try Deep Learning in Python now with a fully pre-configured VM"
https://medium.com/@ageitgey/try-deep-learning-in-python-now-with-a-fully-pre-configured-vm-1d97d4c3e9b

ah - it states that it prefers VMWare over VirtualBox, and in fact:
"An alternate version of this VM for VirtualBox is also available, but the performance in VirtualBox can be pretty bad. So don’t the VirtualBox version unless you don’t have any other choice."

VMWare for OSX is a paid product @ 79.99
however there is a 30 day trial available


2018-02-13 09:25:34
installed VMWare
now downloading the 5.4GB machine image from internet archive - neeed to create account here to do so
https://archive.org/details/DeepLearningVM_Ubuntu_16.04_64Bit_vmware


2018-02-14 00:34:14
attempting to start the preconfigured deep learning VM. Its big, unpacks to a 17GB file


2018-02-14 00:39:24
ubuntu is booting up


2018-02-14 00:45:07
awesome. it does support a USB webcam (!)
or the Facetime cam (!)


2018-02-14 00:56:52
attempting to install Torch
VM uses Python3

having some issues installing software
same issue when attempted to install htop


2018-02-14 00:57:52
I'm going to attempt install of vanilla Ubuntu 16.04 for the ISO I got last nite

hmmm. no issues as root
htop


2018-02-14 01:15:44
installing fresh Linux. Does the webcam come along by default?


2018-02-14 06:58:36
yes, webcam functionality comes by default


2018-02-14 07:13:18
installing torch


2018-02-14 09:57:24
continuing Torch install and some experimentation on linux VM on macbook


2018-02-14 10:09:37
Torch dependencies installed.
running the install script


2018-02-14 10:17:04
Torch is installed
going thru the other fast-neiural-style dependencies


2018-02-14 10:27:24
testing webcam demo (!)


2018-02-14 10:29:05
runs out of memory it seems. This must have been the same issue I had w the prebuilt VM


2018-02-14 10:43:30
demo is riunning. is incredibly slow, using up all available RAM and most of allocated swap memory - well actually usage peaks at 850MB - if I allocated more RAM to this machine...

2018-02-14 10:55:34
still incredibly slow. not really fast enough to be interactive
seeing if reducing capture size helps
it does. significantly getting about 2fpx w 5.9GB RAM usage


2018-02-14 11:14:50
some conclusions
- will running this on WIndows be any faster than in a VM?
- will running this in bootcamp on a Mac, on windows be a better solution
- what is the Windows installation procedure?
- are there other repositories that work better, or native to MacOS


2018-02-14 12:20:40
taking a look at a repository mentioned in an article on runnin style transfer on your macbook
https://cuicaihao.com/2017/10/26/fast-neural-style-transfer-by-pytorch-mac-os-draft/

- installing Anaconda pythion distribution
- installing PyTorch


2018-02-14 12:57:07

a permissions issue getting this to work, but probably not major. Thing is - this isn't a webcam demo


2018-02-17 13:17:19
I am continuing to look for interactive style transfer solution that can run on a macbook, have been surprised not to find anything obviously usable yet. Maybe it doesn't exist.

TODAY
- finish examining macbook interactive style transfer options
- write down a user experience. pretend you're attending this workshop. what do you wnat to take out of it


2018-02-17 15:42:58
collecting my research in OneNote


2018-02-17 22:21:40
installing opencv3
note that I previously installed anaconda python package for macos
so am installing opencv thru that mechanism
conda install opencv


2018-02-17 22:27:55
verified opencv install
v3.3.1

verified numpy install (came w anaconda)


2018-02-17 22:30:03
looking at installation options for tensorflow
verified tensorflow install;


2018-02-17 22:36:43
I've met all the dependencies for https://github.com/ghwatson/faststyle
cloning that repo now


2018-02-17 22:40:46
repo is working for fast style transfer
testing webcam demo
omg - its working

renders a 1280 x 720 frame every 10sec on this machine
renders a 640 x 480 frame every 3 sec on this machine

python stylize_webcam.py --model_path ./models/candy_final.ckpt --resolution 1280 720


2018-02-17 23:37:42
incredibly - running multiple instances of the python script at once w 2 output windows. Not seeing noticeable performance hit - still rendering 640  480 evry 3-4 sec


2018-02-17 23:46:13
taking a look at the other tensorflow-based implementation
https://github.com/lengstrom/fast-style-transfer


2018-02-18 00:18:02
its running, but not showing an image. Is it expecting a GPU? not sure why it wouldn't work/ perhaps an issue with openCV - the repo states that it was tested on v2.4


2018-02-18 00:24:44
downgrading opencv to 2.4 breaks everything :(
)


2018-02-18 00:45:30
restoring it back to v3 makes it work again

python run_webcam.py --width 320 --disp_width 800 --disp_source 1 --horizontal 1

2018-02-21 07:44:34
picking up where I left off on getting deepdreamvisionquest.com up and running in full again. Its become a priority. This will be a good link from the CODAME Medium interview, and can also provide Vanessa with hi-rez images from a gallery here.

After today's worksession, make an audit and estimate time to completion. Need to think about an MVP approach here as well. Specifically - what is the least amount of content I can go live with

2018-02-21 08:04:37
next immediate goal

EVENT PAGE
- find a way to isolate past events in the CSS
	+ hide the view event button for past events
	+ is it possible to hide a thumbnail for past events? hiow would this affect layout?


2018-02-21 15:28:31
meeting w CODAME to solidify workshop agenda and draft proposal to


2018-02-21 16:29:01
great conversation w Jordan. Very specific agendas for workshop now, and also a performance-based aspect,. The WORKSHOP is about image capture and manipulation, then seeing outcomes using style tansfer. It will run a web-based interface to an AMazon EC2 instance that I setup. Some technical requirements there that I need to identify this week
The SHOWCASE is a video installation. LOCUTUS is used to run the fast style transfer demo in realtime, with projected display and CPU display. Some hardware dependencies there - for example splitting the HDMI output so it can go to prohjector, display and recording device. The camer acontrol panel is made available for people wgho want to dig deeper. I'll help them with that part. The camera is movable with long USB cable. Will need rto have extra cameras available - just in case. May be possible to run 2 cameras at once. Camera(s) need to be made inviting to be picked up. actually considering putting it into the moputgh of a stuffed animal


Workshop Description
2 hours (noon to 2) on 27th and 28th
20 people max for each workshop day
Attendees will be able to process 2 to 3 batches of images in that time
Focus on narrative and strategies of style transfer
Emphasis on iterative image generation and capture
Exploration will be balance of free form and prompted exercises
Alter camera (wide angle lens)
Alter style
Alter ??? their own!
LED lights will be around for creative use
Play around with camera and context
Output will become part of the showcase and ART+TECH Festival showing


Showcase Description
Gary to be present for the showcase days, but with at least 1 volunteer at all times
Active on 27 + 28 when workshops are not
Maybe: April 26 (Evening VIP event) and 29th expo only
Realtime Style Transfer Technique projected large on the wall
Interactive camera (well indicated, maybe in a prop)
Portable handheld LED lights available for play
Camera control panel will be up for people who are curious
1080 output to projector
Daylighted displays with HD collection
Room lights dim or off, illumination coming from projector, screens, led lights

2018-02-21 22:23:52
working on deepdreamvisionquest again
oh good 0 looks like I previously found a way to identify past events in CSS

2018-02-22 00:42:06
added CODAME Art+TEch event

2018-02-22 02:06:58
completed tonights worksession. Added and completed 2nd editorial pass on Codame Art + Tech event. The source copy on the CODAME site needs massaging. Implemented some layouit refinements, switched back to OpenSans, added interesting animated hover to inline text links



2018-02-22 09:18:28
collating recent IG posts. Pick several and add to Google Drive for CODAME
eta 1h

2018-02-22 20:12:27
importing current style transfer work since lats import.
- looking for samples to send out to CODAME

NEXT
x follow up w CODAME correspondence
x follow up w LAST Festival correnspondence
- deepdreamvisionquest gallery curation

2018-02-22 22:47:28
wrapped up correspondence finally. Made some edits to CODAME proposal to IfSo, What for style transfer demo and workshop
https://docs.google.com/document/d/10AJEgeipwKuJU5UVVIP2Bd6v2LjRRnnZw5n-KmmBNqE/edit

2018-02-22 23:51:50
1st pass curation on newly imported style transfer images

2018-02-23 00:28:07
moved new imports into named style transfer folders, did a bit of housekeeping

NEXT
- go thru the style transfer collection and rank thenm
- look at instagram history, which ones performed best?
- add to squarespace gallery


2018-02-24 12:51:01
continuing my work on gallery formatting, UX and curation

2018-02-24 15:42:14
continuing my work on gallery formatting, UX and curation

2018-02-24 17:36:37
reformatted gallery nav and changed responsive behavior to keep it from otherwise reasonable jumping to the other side of the page (out of the sidebar) in a shorter/narrower view. This was causeing that text to overlap wider images on ipad portrait aspect. The only constraint here thopugh is that description text length will need to be kept shorter than a certain length, otherwise the menu

2018-02-24 19:13:17
came across odd CSS hack to disable mouse events (to prevent navigation prev/next when clicking on an asset), but now it has disabled the "play" controls for videos as well. jeez.

2018-02-24 20:22:29hacing at this behavior in the CSS is the wrong way to go. I get the behavior I want when I remove the event handler from .collection-type-gallery #slideshow .slide in the dev console. Is there a way to do so on the squarespace page?

$().unbind('click');

<script>

$(document).ready(function() {
  $('.collection-type-gallery #slideshow .slide').unbind('click');
});

</script>


div#slideshow.slideshow.sqs-gallery-design-stacked

2018-02-25 13:11:54
I need to get that click handler from gallery pages removed. Was using juery without success, but now I'm reading that ss uses YUI3 framework. Basic example:

Y.one("#selected-element").detach("click",  "undefined");

2018-02-25 13:35:05
maybe addiing this script to top of page isn't what it seems. This code returns null:
<script>
	var item = Y.one('div#slideshow')
	Y.log(item);
</script>

I don't think the node exists when the script is called. Maybe possible to run the script when document has loaded? or to insert script in page footer, so it runs after all documents noeds have been created?

2018-02-25 13:39:11
ok. inserting that script (globally) in the page footer does return a node when on a gallery page type. How can I see what event handlers have been attached here?

2018-02-25 14:16:04
I think the problem I'm having removing the event is that my code is running before the event gets bound? When I delay execution of said code, the event is removed as expected

2018-02-25 14:24:12
feeling a need to move on from this, can return later for a more informed solution. Will try delauded execution. Still feeling this is too much and that a CSS based solution is possible? What I'm trying to do is remove pointer events from all slideshow content except video

2018-02-25 15:05:41
completed UX modification to gallery. testing on phone and ipad though

2018-02-25 15:27:17
Am I expecting too much or does this squarespeace gallery kind of suck? looking at thhe hub page, its not at all obvious what is video and what isnt. Is this really an improvement over showing the summary view opf a gallery page?

2018-02-25 16:04:01
styling the mobile menu

#mobileNav > div > nav:nth-child(1) > ul > li.mobile-folder > ul > li
#mobileNav > div > nav > ul > li.mobile-folder > ul > li.gallery-collection

2018-02-25 21:06:52
continuing to work on mobile menu format and behavior. nearly there.
need to remove click event or link on Gallery menu header text. clicking it in the mobile menu links to 1st listed gallery. Shoulldn't be clickable at all, or even better, could show a hub page of all galleries. For my purposes, disabling the link at this screen size is better

2018-02-25 21:15:07
disabled that gallery link with pointer-events: none;

2018-02-25 21:33:46
completed low-contrast menu.
taking a look at higher contrast

#mobileNav > div > nav > ul > li.page-collection.active-link

2018-02-25 22:18:01
mobile menu looks great
taking another look at galley pg vs gallery summary on a page

2018-02-25 23:40:23
better gallery now, some choices to review

2018-02-26 20:10:08
couple of layout tweaks to increase type contrast. Building a candidate gallery

2018-02-26 20:13:27
reading back through the use cases discuissed earlier

case study
- the details... and understand the work, it's process, it's limits and its potential... high rez images

could you do graphics at a concert?
Could you do high rez album work?
Could you create filters for photos that her fans could apply to their images?
Could you do work that could be applied to advertising (make up brand).
Also think about music video work and how you might collaborate with a director.
What kind of work might you be able to do for public rallies (outdoor projections)?
What kind of work could you do in more tradtional speaking engagements?
Perhaps even how you two could collaborate to create "sticky" instagram feed images that are just fun...

Of those cases, the ones i'm interested in describibng are:
hirez artwork (fineart)
brand identity
projection & live events.
speaking engagements
online store

Case Studies, Resources & onboarding will take place seperately once the rest of the site is stood up to my satisfaction and is live. Consider it a Tier-2 feature

The Contact form is a good place to expand upon services, and should in fact be labeled that in the menu

2018-02-26 20:25:24
part of the procrastination in building out these galleries has been doubt over what to include. I think that to start with creating event galleries are a good idea. What does the GDC gallery look like?

2018-02-26 21:35:23
completed 1st pass of GDC gallery
updated video to loop and push out camera view and posted to vimeo
doing some type spacing for stacked gallery block labels

``yui_3_17_2_1_1519709673705_108 > div > h3

2018-02-26 21:39:33
tis gallery looks succesful and informative. Its brief, and shows avariertyu of media. A content checklist:

- shows installation in its environemnt
- shows process
- shows my identity
- shows audience engaging
- moving pictures

is this too much? Or, what's missing from this list:
- postproduction
	- fineart artifact
- marketing
	- merchandise
	- collateral

2018-02-27 12:33:25
made some simple contrast-related typography tweaks this am and the site is looking much more chohesive.

2018-02-27 21:36:48
adding CODAME Art + Tech event gallery

actually - think this through for a minute in terms of end users, not a file tree

What gallery do these go in?
- Vanessa asked for sample images for marketing and promo
- Jordan & Bruno asked for sample style transfer images for print and display
- Joel & Emily needed specifics about installation setup and placement
- I want to sell prints
	+ of what?

The gallery menu needs to be as compact as possible
instead of listing each live event seperately, why not have a live event gallery page?

2018-02-27 22:31:23
still working through those questions. There's a lot more to selling prints than I can tackle now, so the galleries need to reflect choices and assets I can make now.

If  I'm not selling images, then the purpose is:
- documentation
- promotion
- exhibition

2018-02-27 23:17:25
I've refined the menu structure to match my immediate needs

Synthetic Gallery
- artwork by series/collectuion
	- style transfer
	- postproduction

Live Gallery
- event footage
- live capture
- developer footage
- installation setup
	+ best practices(?)


Interaction designer Gary Boodhoo makes pictures of minds. This Jamaican-born machine learning enthusiast uncovers collective memories by visualizing neural networks. His creative practice encourages emotional connections to smart objects viewers no longer distinguish from themselves. He describes his current work as science fiction cave painting.

2018-03-01 08:08:42
collating gallery assets. getting hung up on depth instead of breadth. Best way to move forward is to get each event posted to the gallery and then circle back around for curation. Curating these images one by one and adding them one by one is slow going

2018-03-01 09:12:37
added CODAME Art+Tech 2016 gallery page and refined gallery page layout overall with some data points - who, what, where, when for context


2018-03-01 09:29:01
adding LAST Festival gallery, then wrapping up this worksession

2018-03-01 09:49:58
added LAST festival gallery
made some changes to gallery nav - added new Media gallery

Synthetic Gallery
- Class M
- Seed Vault

Live Gallery
- LAST Festival
- 2016 CODAME
- 2016 GDC

Media Gallery
- Staging
- Promo <need better name here I think. who is this for?>
	+ who is this for: Vanessa at Codame
	* why does she need it? needs content for Medium article, event promotion, codame website
	* how does this help me? Allows me to choose the images that will represent this project outside of my own efforts. lets me make a first impression


next steps:
pull content from existing galleries to represent the best this project has to offer and populate the [promo] gallery with them
- high resolution
- postprocessed
- science fiction cave painting

2018-03-01 22:30:52
realized upon reflection that I needed to maintain a proper project cover page. I had entertained the idea of using the Artist info page as the landing page, and maybe I'll revert back to that idea, but I'm reconstructing the cover usesd obn my temp site to see how it feels

2018-03-01 22:52:03
this old desccription is limiting:
DeepDreamVisionQuest is an art machine that creates multiplayer hallucinations about it's environment. Live cameras reveal the world to a neural network which progressively misunderstands what it sees.

a better description would talk about how I've used the gregarious art machine to generate artifacts

2018-03-01 23:06:33
I'm wrong about needing a project page. Or am I? The way I'm doing it for the cover page, and the way I've previously done it have been limiting. I am looking at the Apple Watch site (just purchased one!) and as an about to be new owner its useful to see product features listed

Phone and Messages
Make calls and send texts with just your watch

Music
Stream 45 millionb songs with Apple Music right from your wrist

Siro
Ask Siri to set a reminder, send a calendar invitation, or give you directions, all without your phone

Notifications
Leave your phone at home and still get alerts from your favorite apps.


Can I think about DeepDreamVisionQuest as a product listing? This ties into the "Services" section I'd considered adding.

Something that speaks to these points:

help me understand the work
- what is the process
- what are the limits
- what is the potential

I see that you've done small-scale installations, but what else can you do?
- can you project these images on a stage
- can you project these images in the environment

I see the camera is a critical part of your process?
- does it have to be a webcam?
- could I run video through it?
- could I send footage from a drone to the art machine?



case study
- the details... and understand the work, it's process, it's limits and its potential... high rez images

could you do graphics at a concert?
Could you do high rez album work?
Could you create filters for photos that her fans could apply to their images?
Could you do work that could be applied to advertising (make up brand).
Also think about music video work and how you might collaborate with a director.
What kind of work might you be able to do for public rallies (outdoor projections)?
What kind of work could you do in more tradtional speaking engagements?
Perhaps even how you two could collaborate to create "sticky" instagram feed images that are just fun...

Of those cases, the ones i'm interested in describibng are:
hirez artwork (fineart)
brand identity
projection & live events.
speaking engagements
online store

2018-03-01 23:21:28
Also, there doesn't need to be a "Project" link in the menu. Its in there now for dev purposes, but clicking on the logo "DeepDreamVisionQuest" at the top of the page goes to the landing page (which will be the project page)

2018-03-02 00:18:10
I got a start on the landing page. Will need to collect my thoughts though and be honest about my expectations and needs.

2018-03-02 14:47:41
2 opposing goals to focus on today
1. new content & art for new landing page (depth)
2. curate existing content and create new galleries (breadth)

will start this worksession with the intent of making the site "wider" by adding new galleries. once I've stood up a few galleries, I'll curate what I just did. Will probably repeat this. The question I'm interested in answering is how many galleries can exist before the menu nav gets too heavy?

2018-03-02 15:00:10
The media Gallery shouldn't be broken up by submenus
and I'm not sure any submenus are a good idea at all. surely the same thing can be accomplished by showing all galleries on a hub page?

2018-03-02 21:27:52
worked out details of a HUB page. need to a gallery to contain thumbnails, attach URL to content. Flexible layout options

`block-yui_3_17_2_1_1519927330274_61241 > div > p > strong`

2018-03-02 23:39:55
fleshed out Media Kit section. Will need 2nd editorial pass.

2018-03-02 23:40:20
creating a new event gallery
- ah out of curated images though
- need to pick candidates for Artificial Intelligence and Living Room

2018-03-03 00:00:17
next
- create 1st pass event post for style transfer workshop
- add additional style transfer galleries
- curate noize floor gallery
- curate Living Room gallery

2018-03-03 17:23:58
creating a first pass event post for Style Transfer workshops

2018-03-03 21:35:10
created 1st pass editorial post for workshops and curated inner image, also determined they use the same banner image orwill appear to be entirely different

2018-03-03 21:42:19
Without a context from which to extend creative AI into other practices, the outcomes may lack conviction. We need to go deeper.

2018-03-04 01:21:30
working on Noize Floor gallery
rendered out some video sequences from the runtime - added AE optical flow and color correction for export to Vimeo. Getting some great ideas for American Cylon

what is American Cylon?
Unlike prior shows the emphasis is on faces. its intended to show exaggerated views of faces. will need to provide a spot to stand on.

it needs to be able to playback sequences that its previously captured

2018-03-04 11:38:51
added new Noize FLoor video assets to Vimeo

2018-03-04 11:53:25
added Noise floor video to gallery

NEXT
curate Noize Floor gallery to alpha candidate
- are there any missing photos?
- missing video?
- what can be removed

curate LIVING ROOM gallery
- review filesystem - lots of stuff was rendered out for instagram
- what's on Vimeo currently
- missing photos
- what can be removed

curate Promo gallery
- add postcard photos currently placed in LIVING ROOM
	+ call these a promo postcard set for LIVING ROOM event
- review filesystem for promo and editorial images already created
- review LAST Festival & LIVING ROOM postproduction


2018-03-04 20:23:14
adding content to promo gallery & living room gallery

2018-03-05 20:13:37
2nd curation pass for promo gallery. Show now more than 10 items here

2018-03-05 21:10:31
only noticing now that the mobile menu doesn't have a way to toggle it open/closed. Instead it pushes the page down and you have to scroll down to it - its awful

wondering if the bavior can be reconsidered - is there an easy fix?
1 - add close widget to menu

2018-03-05 23:46:59
completed 1st pass curation of promotional page

2018-03-06 08:35:02
reduced number of items in promo gallery to 10

2018-03-06 09:04:49
Promotional gallery is alpha-complete

ALPHA COMPLETE STATUS
x Event Page
x Artist Bio Page
x Media Kit Page
- Landing Page
- Galleries
	x Promotional Gallery
	- Staging & Dev Gallery
	x Class M
	x Seed Vault
	x 2017 Noize Floor
	- 2017 Living Room
	x 2017 LAST Festival
	x 2016 CODAME
	x 2016 GDC
- Current Events
	x 5th LAST Festival
	+ Workshop: April 14
	+ Workshop: June 4
	x Art+Tech Festival
- Past Events
	+ Noize FLoor
	+ Artificial Intelligence
	+ Living.Room
	+ LASER Talk UC Berkeley
	+ LASER Talk University SF
	+ 4th LAST Festival
	+ CODAME Art+Tecg 2016
	+ GDC
- Blog
	+ A neural network that misunderstood

2018-03-06 09:54:39
created spreadsheet to track completion
https://docs.google.com/spreadsheets/d/1qH9QEhYZHpx4A30NVu9qRciTMpFXWARV9Jlj6mN_Vmo/edit#gid=0


2018-03-06 17:15:23
added custom CSS to keep mobile menu link in fixed position so it always appears. Testing that fix - ah - regrettablly the link remains visible when scrolling the page as well.

2018-03-06 19:26:35
continuing work on the site

2018-03-06 20:56:52
finetuning promo gallery

2018-03-06 21:01:45
promo gallery is alpha complete
working on staging & dev gallery now. first of all, that name...

2018-03-07 00:49:30
good progress
93% alpha complete
52% beta complete

2018-03-07 21:30:46
working on the staging/dev gallery

2018-03-07 23:16:43
cleaning up the 2 workshop events

2018-03-08 00:14:28
93%		alpha complete
63.3%	beta complete
56.67%	ready

(assuming Past Events to be KS)
93%		alpha complete
90%		beta complete
83%		ready

2018-03-09 11:28:10
working on the landing page
what's missing
- curated featured images
	+ must all be 1:1 aspect ratio
	+ color correct as necessary
- Feature list
- wrapup (closing statement or content block)
- Call To Action
	+ contact form ?
	+ follow me on instagram
	+ request for help
		* interested in collaborating
		* interested in speaking
		* interested in demo
		* interested in booking
		* interested in volunteering
			- technical support (doding)
			- setup
			- writing and curating editorial content for blog

Tier-1
match existing landing page

2018-03-09 15:22:08
blocxked out section concepts

Tier-2
add feature list

Tier-3
add call to action

2018-03-09 12:59:40
exporting header gfx candidates - did a full search of all content in LR

2018-03-09 14:49:07
curated landing page header images
matching the rest of the cover page features

2018-03-09 15:13:11
2nd pass curation for about page images

2018-03-09 18:34:58
working on landing page editorial
just be honest

I became interested in the art of neural networks after watching humans respond to the images they made. visualizing the activity of neural networks by watching them draw pictures step by step. Emotionally charged images

2018-03-09 20:08:53
first draft for "How to Contribute" section on landing page

2018-03-11 11:04:45
working on landing page. Putting some thought into the various CTA's, which admittedly I'm a bit shy about.

Instead of thinking of it as asking for help, could it instead be:
- ask for advice
- make people heard
- make people feel valued and important

"Get Involved"
"Can I Use Your Brain?"
"Join the Team"
"Volunteer"
- Instead of calling for volunteers, ask for people to do the specific jobs you need volunteers for.
	+ "Volunteer Opportunities"
		* follow with sopecific job descriptions
"We can go deeper (with your help)"
"Take Action"
"Take your interest further"
"Opportunities"


Get Specific
Create Fun & Specific Job Titles
Create Short-Term Project Teams
Focus on Their Benefits, Not Your Needs
- Making a difference
- Using their skills and talents for good
- Meeting others in the community
- Working for a cause they believe in
- Helping others

2018-03-11 11:52:08
working towards alpha completion on the Landing Page. Can already tell this will take a few hours before getting the general shape of what I want and clarifying my intentions (be honest)

What can I work on and get some immediate results?
curate LIVING.ROOM gallery -> beta
curate LAST Festival -> final
format blog post

2018-03-11 11:54:33finalizing LAST Festival Gallery

2018-03-11 12:51:15
why give a workshop at all? why go to the trouble of it?
It makes me feel important, makes me feel like I'm part of something larger than myself, but am at the leading edge of it

why des it make you feel important?
because I know something that you dont

It sounds like you don't want to hold that aginst anyone though - you'r enot better than anyone surely?
NO - I'm not better than anyone. My fear of being involved with peopel has actually always been that they'd see through me and think I was naive or juvenile or clueless or otherwise lame

I've notioced at shows how easy it is to talk to people because I'm the expert.

So part of the reason I want to give worskhops is top meet a wider range of people and feel like I'm speaking to them as equals.

And as equals - the communication between you is evenly matched?
Well - Its like I need to hold the reins so to speak - I'm a bit of a control freak, but its not the end of the world

I chose to give workshops because it was a risk, and I didnt want to be afraid anymore. By controlling the rules of engagement, I feel like I'm able to step into the role of a Teacher and gain a level of respect.

So the simplest answer to the question is:

Why give a workshop at all?
To earn respect.

2018-03-11 13:04:29
spent a bit more time on the landing page plainly stating the purpose and outcomes I wanted for each section. Hopefully that helps when I circle back to it. Moving on to LAST Festival Gallery finalization

2018-03-11 13:36:53
finalized LAST Festival gallery

2018-03-11 18:24:21
finishing up LIVING.ROOM event gallery.

2018-03-12 08:53:48
working on contact email link before taking a look at blog post format

2018-03-12 10:51:20
updating some of the writing (inevitably) on this intro blog post.

2018-03-12 20:00:34
testing new (4K HDR) webcam on Linux machine

2018-03-12 22:49:03
cleaned up mail icon display before text using CSS solution - easy and flexible!
I've put off working on the landing page until now, and am working on saying what I want clearly

2018-03-12 22:57:29
actually that method fails when font aweome isnt installed as a sytem font - need to look further into this

2018-03-12 23:38:12
fixed the font awesome icon issue

2018-03-12 23:46:23
unstuck mobile menu label. The behavior it uses in thiis template is questionable, would be so much better if it could just be easily closes without having to scroll. another tiome though.

2018-03-12 23:51:32
going through each page and checking permalinks

2018-03-13 08:33:12
completing Landing Page

Learning Machines teach us something amazing—it doesn't take much to invent the world. Any technology capable of recognizing images must also invent them. My science fiction cave paintings are mirrors that reflects hidden selves.

My science fiction cave paintings reflect, amplify and integrate hidden selves with waking consciousness

My science fiction cave painting ask the conscious mind to take a break and let the hidden selves within come out and

My science fiction cave paintings are drawn on the geometry of memory

My science fiction cave paintings emerge from the geometry of collective memories.

My science fiction cave paintings recombine collective memories

Everything within is a shifting configuration of haunted rooms and spirit animals, lurking into existence whenever the neural network dreams about them.

The shaman lurks in a dark cave in a trance, painting images of its visions with some notion of drawing power out of the cave walls themselves.

2018-03-13 09:14:03
writing is so hard. what are you trying to say here. Who is this for. It needs to summarize everything. Surely you've dobne this before in 240 characters of less. That's all this opening paragraph must be.

for example:
Inspired by Alan Turing, their newest performance marries choreography for five dancers with machine learning technology and a stage designed for interactivity between performers, drones, virtual dancers and other objects.

DEEP DREAM VISION QUEST IS A NEURAL IMAGE SYNTHESIZER THAT CREATES MULTIPLAYER HALLUCINATIONS AND TURNS DREAMING INTO A SHARED EXPERIENCE

DeepDreamVisionQuest is a neural image synthesizer that creates multiplayer hallucinations and turns dreaming into a shared experience.

These science fiction cave paintings combine the collective memories inside a neural network with the uncertainty of the real world.

At some point, hidden selves emerge.

Learning machines have arrived, and they're Zen. The surprising truth behind artificial intelligence is that Mind emerges from the environment.

For any given image, the algorithm constructs the same hallucination every time.

I create video installations that show the world to a learning machine through a live camera. Deep Dream Vision Quest is a neural image synthesizer that creates multiplayer hallucinations. Although the algorithm is predictable, the world is not

A kōan is a peculiar dialog between a Zen master and a student whose apparent absurdity channels psychic energy towards a breakthrough.

2018-03-13 10:22:23
completed leading paragraph. nice.

DeepDreamVisionQuest is a neural image synthesizer that creates and explores multiplayer hallucinations. These science fiction cave paintings combine the memories inside a neural network with the uncertainty of the real world. Hidden selves emerge. You complete the circuit. The surprising truth behind artificial intelligence is that Mind emerges from the environment.

http://skinjester.com/

2018-03-13 10:56:38
nned to wrap up this worksession shortly - taking a pass at the CTA sections
moved landing page to aklpha-complete. could launch with it in its current form

2018-03-13 11:49:48
made a start of it
1st pass on leading paragraph for Exhibitions & Comissions section. Lots of massaging needed here, but once the voice is found I am hoping to replicate it for the other sections.

2018-03-13 21:44:26
2nd editorial pass for Exhibitions and comissions section

I make synthetic art with machine learning technologies for environmental and editorial applications. Custom work and comissions are available by appointment.

2018-03-13 22:30:02
filled in the Exhibitions and Comissions section including a range of services

2018-03-14 00:21:21
1st pass on Workshops and Talks section
continuing

2018-03-14 01:15:42Almost there. working on the Contyribute section.
Very rough, needs clarification. Filling in further details before wrapping up this worksession

2018-03-14 02:38:01
completed all sections, removed the dishonest parts. needs additional editorial pass. Calling it beta-complete though

post launch I'll want to
- additional style transfer galleries

2018-03-14 13:31:05
launching shortly. Following up on editorial pass for landing page and blog post

2018-03-14 13:47:04
completed editorial pass of landing page! its final!

2018-03-14 14:23:34
completed editorial pass of blog post! its final! The site is content complete.

2018-03-14 14:25:33
the site is live!


2018-03-14 21:33:12
reviewing my previous code
how does this all work?!!!



2018-03-14 22:14:01
doing some ubuntu housekeeping
tempted to downgrade my versions of OpenCV and Cuda for better memory utilization, as was found on the Linux install on LOCUTUS


	2018-02-10 17:31:29
	I've setup fast-neural-style of both LINUX machines with ionteresting results

	LOCUTUS
	Open CV 2.4.13
	CUDA 8.044
	CuDNN Yes
	GPU TitanX Maxwell

	HALLUCINATR
	Open CV 3.2.0
	CUDA 8.061
	CuDNN No
	GPU TitanX Pascal

	The difference between the 2 configurations is significant. For webcam-based use cases: On LOCUTUS I can compute images at 1920 x 1080 or larger, with minimal memory usage on the GPU (no greater than 4GB at any time). On HALLUCINATR, I run out of memory on the GPU at resolutions larger than 1280 x 720. Not sure if the differnes have to do  with:
	- presence/absence of CuDNN
	- older version of OpenCV requires less memory



2018-03-14 22:51:40
areas to explore

timing of the composer ramping function and motion detection
additional program settings tested on AV rig
	- how to add more variation to program settings
strategies for saving rendered output
guide images
mirroring
looping previous content
improved inception xfrom scaling
	- could this use the average position of motion as the anchor point?
post processing effects
	- vignette
	- blur
	- color transforms - brightness/contrast/color mapping


2018-03-15 00:29:28
next

- test rem.py on LOCUTUS to see if it uses less memory. I'm unable to effectively show 1920 x 1080 hallucinations with current program settings
- create a vanilla program setting for testing
	+ should use no effects
	+ should work at 1920 x 1080 and higher
	+ no octave scaling
	+ no step scalining
	+ etc
- is there a way to show the supoorted resolutions of the webcam?
-  prioritize and scope development goals


2018-03-15 22:04:43
running at 1280 x 720 or lower is fine
with mirroring implemented, higher resolutions may be achieved if only half the screen is being rendered. no time to compare memory usage on a different machine - however keep an eye on the memory usage of each program and document this

right now I'm just figuring where the logging calls are being made so i can disable moment by moment updates in the console


2018-03-15 23:21:47
just about have the logging sorted out - there are a series of movement detected/ended messages that are useful to see but not as log.info, and I don't want to make them as low level as log.debug

how about the default log level be set to log.warning, then the motion detection status can be log.info



2018-03-16 00:35:30
taking a closer look at how motion detection works (I've broken it somehow at the moment), but noticing that that motion detectio events get triggered at multiple times as long as the detection_toggle value is true. Which means that it must be getting turned on then off on consecutive frames before any compositing is able to get started

maybe this is exactly how it should be, but I want to see hwat happens if when a motion is detected, the compositing doesn't get retriggered until the motion registers as ended.

the first time I check for motion.detection_toggle I need to set another flag - let's call it detection_active
- let's call detection toggle, detection_init instead


2018-03-16 02:49:32
having trouble implementing this. spent a while in the ramp_update function and its in a broken state at the moment, having a hard time wrapping my head around what I want to do


2018-03-16 09:35:33
to clone an existing terminal window do this:
history -a && gnome-terminal


2018-03-16 10:22:38
compositing routine still broken, but starting to see the effect I want


2018-03-16 10:58:02
seeing some interesting behaviors, but itys not behaving the way it was before.  considering reverting


2018-03-16 11:04:15
reverted code and working as expected, but why?


2018-03-16 11:29:32
tweaking some existing oarameters
the way it works now the live camera image is always visible (except when the hallucinations begin to feed on themselves?)
I need to undersatnd how I set this up to work - its more subtle than I previously realized, but getting some great resultsd - running at 640 x 360 is amazing - the hallucinations for quickly enough that tehy're always resolved. At highr resolutions, motion often retriggers the hallucinations and they're not building up as fully


2018-03-16 17:52:14
let's take a look at this compositing code and see how its working


2018-03-16 17:57:15
how does compositing (without a ramp) work?


2018-03-16 18:30:36
Tracy Shintaku from FB nueral art group

add to guest list:
Tracy Shintaku
Larry Shintaku

send email to Joel to provide Tracy Shintaku's name as my assistant during setup


2018-03-16 22:49:09
how does compositing (without a ramp) work?

# write RGB data to a buffer (there are 2 of them)
Composer.send(0, img)
Composer.send(1, img)

# mix 2 buffers
Composer.mix(buffer, buffer)

# store an RGB version of the neural netblob
	- looks like this was created so there would always be aan RGB compositing source
Composer.dreambuffer

# show an RGB buffe
rViewport.show(buffer)


2018-03-17 00:34:10
interesting - part of the inconsistency I was seeing in the composer ramping had to do with the values changing too rapidly -added time.sleep on increment and definitely working better, maybe with some creative flexibility as well


2018-03-17 01:13:56
but motion detection is too sensitive


2018-03-17 03:23:41
great progress today
made some screen recordings, and wondering if I can do same during live installation


2018-03-17 04:17:58
experimenting w some program settings


2018-03-17 16:58:25
there are 3 things I want to explore further today
- how to make trails from the camera input
	+ add new camera input to old as single webcam source
- how to crop and mirror a region of the camera input`
- how to scale to an arbitrary anchor point


2018-03-17 23:39:05
experimenting with slightly different composituing method on the way to painting with the webcam image Experimenting with some old program settings as well -fewr iterations needed for some of these than expected


2018-03-18 01:03:59
I don't know how to get the echo/painting effect I want. maybe looking in the wrong place?


2018-03-18 01:27:28
there are 3 things I want to explore further today
x how to make trails from the camera input
- how to crop and mirror a region of the camera input`
- how to scale to an arbitrary anchor point


2018-03-18 01:55:09
reading up on image cropping


cropped = img[y1:y2, x1:x2]
cropped = img[0:720, 0:640]

display buffer is same shape as non-cropped input
copy cropped
flip copy horiz

draw cropped into buffer
draw copy into buffer

	For cases where your images happen to be the same size (which is a common case for displaying image processing results), you can use numpy's concatenate to simplify your code.

To stack vertically (img1 over img2):
vis = np.concatenate((img1, img2), axis=0)

To stack horizontally (img1 to the left of img2):
vis = np.concatenate((img1, img2), axis=1)

import cv2
import numpy as np
img = cv2.imread('img.png')
vis = np.concatenate((img1, img2), axis=1)
cv2.imwrite('out.png', vis)f



2018-03-18 12:49:12
let's see if I can get mirroring working


2018-03-18 14:02:33
working on mirroring now after some housekeeping


2018-03-18 14:07:20
I've got basic crop and concatenate working. it's interesting. Seeing a glitch related to motion detection and compositing though


2018-03-18 14:27:29
demonstrated working at camera capture
how to make the mirroring happen at display time only (and thus computing dreams only on the cropped capture?)


2018-03-18 15:20:32
hilariously stretching the cropped cammera frame to fill the display area
the dreamed material is also being scaled
what is the shape of the camera img when it's retrieved?


2018-03-18 16:40:15
understanding the details of cropping behavior. problem I'm solving now is that the motion detection continues to happen on the non-cropped camera input


2018-03-18 17:23:46
ok, great  - motion detection is being performed and monitored from a cropped view. performance on this subset of the image is much faster - as expected


2018-03-18 18:03:54
so - how to flip and composite the image now?
will want to do this on the main viewport first


2018-03-18 19:28:22
ha - 1st pass is not what I expected =- seeing ultrawide aspect window. but is working - and its running recursively - with each new cycle the number of mirrored images doubles


2018-03-18 20:00:22
need to make a map of signal flow, I'm having unintended consequences and not sure where to make edits



2018-03-19 01:16:00
not sure if I should be  mirroring the motion detection buffer
not entirely convinced that mirroring is a good idea - not feeling l;ike I'm looking at me because I see 2 of me


2018-03-19 09:34:43
stepping away for the frame buffer mirroring idea. Some lessons learned for later, but overall what I was able to get running distanced me from the output and did not draw me in. Reverting those changes


2018-03-19 10:24:14
running well after removing crop functions. At this point, all that's left to do is:
- verify frame capture for runtime
- is it possible for the content of a new cyle to fade in on top of the old instead of appearing immediately?


2018-03-19 11:00:47
next step is to setup on the AV rig


2018-03-19 10:30:15
need to review work later today and create a list of priorities
- light levels and program settings
- light levels and motion detection
- screen recording


2018-03-19 21:54:35
connecting to AV rig, setup LINUX display as 1280 x720


2018-03-20 15:24:28
mounting webcam to AV rig. be sure to mark off the position and camera settings


2018-03-20 16:08:08
having difficulties w camera mounting. its not sticking to the side and back of TV because of the materials its made from. I tiook of the mounting brace and have it physically lashed on to side of display.

bit now I'm finding that the field of view isn't sich that I can pan the frame to see myself standing in front of it

looking at camera mounts

considering older camera

wondering if i can crop a 1280 x 720 image from the 4K image in a horizontal mount congfig - at top of screen?``


2018-03-20 17:55:46
I'm going to see if I can crop the camera input at capture time based on what I learned over the weekend


2018-03-20 18:56:46
this camera  captures at 1080p  max under Linux. It may require a USB3 connection to see 4K, I'm only using USB2 Worthwhile cropping this area? Curious to see actually. Ordered a USB3 extension


2018-03-21 16:12:05
Figured a soukltion to the camera issue. I've mounted it to the top of the screen. Eliminates parallax issues that were also a problem. The zoomed in image however is a bit lo-rez, especially coming from  a 1920 x 1080 input. Going to text the USB3 cable in a moment and see if I can capture at higher rez


2018-03-21 17:27:43
just tested 4K capture with a USB3 connection. verified. Seeing if a long cable run makes a difference with the USB extender that has arrived


2018-03-21 17:48:32
the USB extender doesn't seem to work without a 5v power source. Not showing  up in Linux


2018-03-21 17:56:17
not really seeing a difference in the 4K capability - the area that can be zoomed and panned seem the same, as does the video output


2018-03-21 19:23:39
iterating through a couple of program variations and then audit. Wondering how I can add internal variation - incrementing through a list of feature maps for example:
	- when is the next featuremap shown
	- is this a cyclefx
		+ triggered after cycle ends
	- is this a stepfx
		+ triggered each iteration

Also wondering out of curiosuty what a guide image looks like in the current renderer


2018-03-21 20:18:03
discovered amazing game mode
the res a camera behind me that is zoomed in on the  TV display and causing a feedback loop. stepping into it triggers exciting, and sort of breathtaking visuals with a unique look - physics is doing a lot of the calculation - the video feedback.

I'm setting up a 2 camera config to allow switching between the cameras


2018-03-21 20:27:17
regrettably, camera switching is broken due to the multithreading camera caoture method. Will fix later


2018-03-22 15:40:11
- Audit program settings
- setup lights
- inspect camera mounts
-
- program setting refinement andf discovery


2018-03-23 01:08:19
updated performance settings. Several people came by and was able to test overall reaction and movement. Ready to disassemble then loadout in the am


2018-03-23 12:52:06
setting up at SLAC

2018-03-27 09:56:52
I thought that my skinjester.com Amazon EX2 credentials had been revoked because on non-payment, but I see that for this account billing is automatic and I still have privileges. Yeah. just checked it the account under gboodhoo@gmail.com that is problematic.


2018-03-27 11:28:54
meeting with CODAME shortly. Here are my action items

Confirm Dates
x April 14th at Swissnex has been removed
- IfSoWhat Festival
	+ Venue: Palace of Fine Arts
	+ Style transfer Workshops
		* Friday 4/27 12-2
		* Saturday 4/28 12-2
		* Sunday 4/29 12-2
	+ Neural Art Showcase
		* Thursday 4/26 - Sunday 4/29, 5-10p
- CODAME Art + Tech Festival

CLEANUP
	CODAME Artist portrait
		- provide portrait gfx to fit aspect ratio
		- revise DeepDreamVisionQuest description with new copy that Thea wrote
		- choose new leading graphic for style transfer workshop posting - related to style transfer instead of deepdream

	PROMO
		- need to update date tag on the CODAME event page, as it still states 14 April
		- I feel like we're not promoting the Showcase portion of the IfSoWhat event
		- What is status of the Medium article feature on Gary Boodhoo

WORKSHOP DEVELOPMENT
- [currently] working on method for participants to upload files to GPU cloud for style transfer processing
- [next] create a script for guiding the workshop
- [upcoming] will need to communicate this script to assistants
	+ how many assistants are we counting on per workshop?
	+ will any be necessary for the showcase as well?

SHOWCASE
to create the showcase, I plan to use the next generation of DeepDreamVisionQuest, which incorporates an AV Rig as well as a projector.
	- it may be possible to use 2 projectors, but that is an scenario I've not explored at all, and is very dependent on setup
	- are the walls of the space suitable for projection or will we need a screen
	- is it possible to go view the space?


2018-03-29 12:47:44
not liking how mail to info@deepdreamvisionquest is being handled
needs its own gmail account, instead of relying on Network Solutions

2018-03-31 00:37:37
updated workshop event postings

2018-03-31 10:57:54
started process for domain name transfer to Google. Incredibly this takes 3 days before I receive a necvessary authorization code. There's no good reason to stick with Network Solutions, and will be transfering all my domains once I see how this goes.

2018-04-01 02:12:22
site cleanup and event posting

NEXT
- create event post for Society of RItual Arts showing June 2nd
	+ http://societyforritualarts.com/information-and-registration-spring-festival-2018
	+ verify dates and times


2018-04-01 11:23:30
I'm looking at the email simplification issue again.
As an example:

skinjester.com is a domain purchased from network solutions and hosted by network solutions
- I have a Google G-Suite account for the domain skinjester.com
	+ G-Suite has 2 users
		* gboodhoo@skinjester.com (Admin)
		* purchasing@skinjester.com

HOW?
- turn off/disable network solutions mail service for deepdreamvisionquest.com
- can I just create another G-Suite account for my comm purposes?
	+ you can create email addresses and aliases at any of your domains
		* If you just want your current users to be able to receive mail using an address at the new domain, add it as a domain alias and leave your primary domain as is. For details, see Give users an address at another domain.

If you also want your users to be able to send mail using their new address at the new domain, see Send mail from a different address or alias.

2018-04-01 12:00:53
updated CNAME records (DNS) on network solutions for GSuite verification


SOON
Find 2nd draft of Workshop description (google docs) and share w Codame
send pre-cropped portrait image to codame for artist profile (thumbnail)
send revised DeepDreamVisionQuest text to CODAME (project description)

I'm running a workshop @ If So, What (ISW) Festival on how to apply the style of one image to another and have it mean something. We'll use the camera and the environment as an interface for personal image synthesis with a neural network.

I'm running a workshop @ If So, What Festival on how to apply the style of one image to another. We'll use the camera and the environment as an interface for personal image synthesis with a neural network.

2018-04-01 15:47:31
Press
https://medium.com/codame-art-tech/lightning-stalkers-the-finale-matchbox-b2078215aa08

zffsezjdt3drges2ckls
n4xe6bv6igzx

2018-04-01 17:46:17
continuing to solve email setup
codified DNS on Network Solutions and verified ownership for Google

2018-04-01 23:08:06
MX records validation is in progress. Changes can propagate within 2 hours, but may take up to 72 hours. When completed, presumably I'll be able to create email accounts for this domain just as I previously did for skinjester.com

2018-04-01 23:36:16
Site is looking great, edits made dthis weekend really pulled it together. Still some outstanding work, but more than MVP complete

CONTENT
P1 create 2018 LAST FELTIVAL gallery

P2 collate other artist portraits

QA:
P2 cleanup all event posts to use common format
	- NOIZE FLOOR
	- ARTIFICIAL INTELLIGENCE
	- LIVING.ROOM.AI
	- 4TH LAST FESTIVAL
	- 2016 CODAME
	- 2016 GDC


2018-04-02 11:16:50
reviewing some new network models for use with deepdream


2018-04-02 12:15:41
not finding any deploy.prototxt files with these models
I think the expectation is that you'll generate (train?) your own?

it's just a case of downloading the caffemodel and prototxt files and substituting them in the script. You also need to look in the prototxt file and pick a layer to use instead of 'inception3c...' one (or whatever).


2018-04-02 13:56:13
Found a new working Model called Miles_Deep. exploring it now


2018-04-02 14:13:36
behaves very differently than the others. huge visual effects achieved with octave scale, and seems like it may need more iterations to geth there


2018-04-08 19:07:36
researching and setting up style transfer on an ec2 instance
- is the instance I previously setup waiting for me?


2018-04-08 20:38:44
found my previous p2.8x large instance. launching it and taking a look inside
named it syntheticaf-dev for easy reference


2018-04-08 20:41:30
having started it, how do I open up a shell?
ssh -i "synthetic_rsa.pem" ubuntu@ec2-54-187-221-243.us-west-2.compute.amazonaws.com


2018-04-08 22:02:46
working out how to transfer files with a GUI
probably possible using defaulty ubuntu file manager, but process is unknown
I don't need to be running linux to access the ec2 instance, so the solution is better if cross platform
trying out Filezilla


2018-04-08 22:07:24
2 ways to sign into EC2

** for a user named Administrator:

Account Id:
751796329511

IAM username:
Administrator

Password:
Helvetica99

** root user signin

Email: gboodhoo@skinjester.com
Password:Helvetica99!


2018-04-08 22:35:02
successfully connected to ec2 instance with filezilla
successfully connected with Nautilus as well, just needed to enter fully qualified username and machine address:
ubuntu@ec2-54-187-221-243.us-west-2.compute.amazonaws.com


2018-04-08 22:38:56
copying over some known good style images


2018-04-08 23:32:35
running neural style default to check rendering speed
its using:
source:	examples/inputs/tubingen.jpg / 1024 x 768
style:	examples/inputs/seated-nude.jpg / 640 x 845
output resolution is: 512 x 384


2018-04-08 23:40:22
need to create smaller/cheaper instance for development & testing


2018-04-09 00:11:49
testing multiple gpu usage
You can use multiple GPUs to process images at higher resolutions; different layers of the network will be computed on different GPUs. You can control which GPUs are used with the -gpu flag, and you can control how to split layers across GPUs using the -multigpu_strategy flag.

-gpu 0,1,2,3 uses the first 4 GPU's
-multigpu_strategy 3,6,12
GPU 0: layers 1-2
GPU 1: layers 3-5
GPU 2: layers 6-11
GPU 3: layers 12-19

3,5,7,10,12,15,17
GPU 0: 1,2
GPU 1: 3,4
GPU 2: 5,6
GPU 3: 7,8,9
GPU 4: 10,11
GPU 5: 12,13,14
GPU 6: 15,16
GPU 7: 17,18,19
 <!-- (how many layers are there? - maybe assume 19 for VGG-19) -->



2018-04-09 00:50:17
th neural_style.lua -style_image ../pictures/style/01-mech.jpg -content_image ../pictures/content/01.jpg -gpu 0,1,2,3,4,5,6,7 -multigpu_strategy 3,5,7,10,12,15,17 -output_image ../pictures/output/01-mech-03.jpg  -content_weight 100 -style_weight 3000 -init image -normalize_gradients -style_scale 0.5 -image_size 1024


2018-04-09 01:01:19
I'm not seeing a significant speedup with more GPU's but the memory usage is significantly reduced per GPU. In a situation where multiple images need to be processed quickly there are a couple of questions:
For a given output size, what is the difference between computing on 1 -> n GPU's
If there's no real speed gain in using multiple GPU's, it may be possible to process 8 images at once.

For rendering tests I need to use Pikazo output as a benchmark for quality & styling success. I can't tell if what I'm working with now is a good combination, although does not necessarily seem bad

Also need to be sending continuous batches from shell scripts to the instance to maximize its availability, so figure out the bash shell script basics - examples provided in the github repo


2018-04-09 01:04:40
v4
th neural_style.lua -style_image ../pictures/style/01-mech.jpg -content_image ../pictures/content/01.jpg -gpu 0,1,2,3,4,5,6,7 -multigpu_strategy 3,5,7,10,12,15,17 -output_image ../pictures/output/01-mech-03.jpg  -content_weight 100 -style_weight 3000 -init image -normalize_gradients -style_scale 2.0 -image_size 1024


2018-04-09 01:17:23
th neural_style.lua -style_image ../pictures/style/05-icon.jpg -content_image ../pictures/content/01.jpg -gpu 0,1,2,3,4,5,6,7 -multigpu_strategy 3,5,7,10,12,15,17 -output_image ../pictures/output/01-mech-05.jpg  -content_weight 10 -style_weight 3000 -init image -normalize_gradients -style_scale 1.0 -pooling avg -image_size 1024 -tw_weight 0 -backend cudnn -cudnn_autotune


2018-04-09 01:39:31
trying out this gpu strategy
2,3,4,6,8,11,12
GPU 0: 1
GPU 1: 2
GPU 2: 3
GPU 3: 4,5
GPU 4: 6,7
GPU 5: 8,9,10
GPU 6: 11
GPU 7: 12,13,14,15,16,17,18,19

th neural_style.lua -style_image ../pictures/style/05-icon.jpg -content_image ../pictures/content/01.jpg -gpu 0,1,2,3,4,5,6,7 -multigpu_strategy 3,6,12,15,20,26,31 -output_image ../pictures/output/01-icon-02.jpg  -content_weight 10 -style_weight 3000 -init image -normalize_gradients -style_scale 1.0 -pooling avg -image_size 1024 -tv_weight 0.01 -backend cudnn -cudnn_autotune


2018-04-10 08:43:51
damn it. I left the EC2 instancve running last night. Be sure to stop it when you're donme. And don't start it until you're ready to use it. Not a huge bill, but $62 that could have been saved.


2018-04-10 09:11:02
setting up for some br this afternoon by creating a shell script to run neural-style


2018-04-10 09:47:21
doing some remedial shell scripting


2018-04-10 09:32:07
was having some trrouble reconnecting to the ec2 instance in the file manager and filezilla. Turns out that the public DNS changes every time the machine is re-started. Wondering if there is a way to refer to the machine in a different way? By some sort of ID or other nomenclature?


2018-04-10 10:32:21
GPU 0
GPU strategy 0
output size 512px
backend cudnn autotune lbfgs
style_weight 5e2
style_scale 2.0
iterations 1000
render start 17:48:30
render complete  17:53:49

2018-04-10 10:54:17
GPU 0
GPU strategy 0
output size 512px
backend cudnn autotune lbfgs
style_weight 5e2
style_scale 1.2
iterations 1000
render start 17:55:38
render complete 18:00:18


ec2-34-212-134-47.us-west-2.compute.amazonaws.com
ec2-34-216-9-144.us-west-2.compute.amazonaws.com
ssh -i "synthetic_rsa.pem" ubuntu@ec2-34-216-9-144.us-west-2.compute.amazonaws.com


2018-04-10 21:49:19
coming along with rendering experiments
what's changed from before?
- now rendering from shell scripts
- benchmarking to spreadsheet
- demonstrated running 2 scripts on different GPU groups
- better understanding of sftp & ssh file transfer (on Linux anyway)
- better understanding of parameters and documented imagery
	+ need to name output images the same as the generator script for easy reference
- basic BASH scripting and filename manipulation
- maybe a slightly faster GPU strategy for 2xGPU renders
- some basic heuristics for parameter settings:
	+ it looks like there should be 2 orders of magnitude difference between STYLE_WEIGHT and CONTENT_WEIGHT to get "Pikazo-like" results (at least with content/style images 03-1K.jpg/07-cosimo-4K)
		* there are different effects are produced with different values of the exponents (5e0/5e2, 5e2/5e4)
		* there are limits to the weights
- the upper limit for style weight is 5e5 (500000)
	+ only seeing gray rendered images when I go higher than that
- number of GPU's involved doesn't improve render time, although different GPU strategies have an effect on render times - up to 30 seconds difference in some cases
- added timestamp to bash prompt on ec2 instance
- figured out some known good default settings for parameters


2018-04-10 23:00:52
for presentational part of the workshop - include website, instagram and info@deepdreamvisionquest credentials
- encourage people to follow my journey on instagram

What do you want out of this workshop?
- its adressed in the mindnode doc I created. Look at that again. still valid?


2018-04-10 23:54:30
taking a look at the differenc the normalize_gradients parameter makes


2018-04-11 00:59:32
the normalize_gradients parameter seems to  "tighten up" the style transfer overall. its definitely a higher quality result. the range between content and style weight is significantly reduced. for 03-1K/07-cosimo-4K the working range I found was
STYLE_WEIGHT=5e2
CONTENT_WEIGHT=2e2

can I generalize that and say that normalize_gradients works when the content and style weights are of the same exponent?


NEXT
benchmark 1024 and 2048px outputs


2018-04-11 20:50:42
Amazon also offers P3 instances, which use NVIDIA Tesla V100 GPU's instead of NVIDIA K80 GPU's. I'm going to set one up and see if it is significantly faster for my purposes


2018-04-11 21:53:10
I've connected to ec2 instance from MacOS using terminal as expected. Copied the synthetic_rsa.pem key to my home directory. No issues.

Wondering now if I can have the Finder connect to the server as I did in Linux
Connect to Server:
sftp://ubuntu@ec2-54-218-32-191.us-west-2.compute.amazonaws.com


2018-04-11 22:07:16
apparently not possible to connect to the instance with the Finder. I downloaded a trial copy of a program called "Forklift" which seems similar in nature (more modern) than Filezilla

speaking of which - I'm going to try making the connection in Filezilla as i did in Linux

successfully connected


2018-04-11 22:28:11
setting up neural style transfer on this machine


2018-04-11 22:57:04
Torch is failing to build, but why?
maybe a more simply configured machine type?
trying this one
Deep Learning Base AMI (Ubuntu) Version 4.0 - ami-7625b90e


2018-04-11 23:29:14
still unable to build Torch on a different AMI


2018-04-11 23:53:01
fixed the torch install and verified working
Its an issue with CUDA 9 that I'd previously run into and solved

	2018-01-06 00:08:20
	there's an error with the Torch installation
	came across this issue - which may be specific to CUDA 9.
	the stated fix is:
	export TORCH_NVCC_FLAGS="-D__CUDA_NO_HALF_OPERATORS__"

	re-trying


	2018-01-06 00:16:13
	installed torch successfully
	ubuntu@ip-172-31-9-143:~/torch$ th

	  ______             __   |  Torch7
	 /_  __/__  ________/ /   |  Scientific computing for Lua.
	  / / / _ \/ __/ __/ _ \  |  Type ? for help
	 /_/  \___/_/  \__/_//_/  |  https://github.com/torch
	                          |  http://torch.ch
	th> exit
	Do you really want to exit ([y]/n)? y

I typed this:

	./clean.sh
	export TORCH_NVCC_FLAGS="-D__CUDA_NO_HALF_OPERATORS__"
	./install.sh

Step 1: Install torch7
Step 2: Install loadcaffe
Step 3: Install neural-style
Step 4: Install CUDA backend for torch
Step 5: Install torch bindings for CuDnn

	# neural-style can be made to work with CuDnn 7 with this
	git clone https://github.com/soumith/cudnn.torch.git -b R7 && \
	cd cudnn.torch && luarocks make cudnn-scm-1.rockspec



2018-04-12 00:34:57
neural-style is running on GPU w CuDNN support on the new P3 instance


2018-04-12 00:52:58
benchmarking now
can already tell this is much faster
holy shit


2018-04-12 00:59:45
except - the script is running and I'm not seeing that its's saving any images...
forgot the -gpu 0 flag - was that the problem? ok - its rendering now


2018-04-12 01:05:58
render times confirmed - this was the quickest I've ever seen it run (!)


2018-04-12 01:36:37
increasing style_scale increases memory usage. Went from caluclating a 1920px image to a 1600px image with almost same memory usage for moth after changing style_scale to 1.5

2018-04-12 01:54:30
created a p3.8xlarge instance for testing hi-rez output vs p2 equivalent
installing neural style

2018-04-12 02:22:02
neural-style installed on this new instance

next
- what is RAM usage/render time of 1024px image uses on P2 instance w GPU x 2
- what is RAM usage/render time a 1920px image uses on P2 instance w GPU x 2
- setup on windows
	+ how to get UNIX shell?
	+ how to get GUI to filesystem


2018-04-12 09:31:09
getting a hi-rez render test underway using multiple GPU's on a P3 instance

watch -n 0.5 nvidia-smi


2018-04-12 10:24:42
not getting the amazing hi-rez output I was expecting actually. detailed areas are just blurring out. It could have something to do with my image files, or it may be a matter of parametrs, or both. I'm trying to get a baseline for renders of this size


2018-04-12 10:41:12
normalize_gradients does make a significant difference with test image 03-1K.jpg. Wondering if a larger version of the content file makes a difference?



2018-04-12 13:43:38
rendering a higher-res image in 1 pass is not nearly as tight as at smaller sizes - at least with the parameters I've been usimg. Wonder if there is value in building up the render in stages - there's a multipass rendering script in the neural-style repo that's worth taking a look at

for tyhe moment though - render quality aside, I'm very interested in compariung 1920 px output on P3 vs P2 instances


2018-04-13 20:27:17
moving back to the p2.8xlarge instace (syntheticaf-dev)
I want to get known good settings for 1920 output and above. It may be that this isn't possible in a single render pass, so am taking a look at the multipass render example - but first that benchmark for comparision w the P3 instance



2018-04-13 21:28:49
its taking quite a long time to render at 1920px on p2 vs p3 instance. Started the render 7 minutes ago and it is hasn't yet reached iteration 200. Is likely to take 20 minutes or more


2018-04-13 21:36:06
also testing a 2*GPU render for 1920px output


2018-04-13 21:54:26
- will not render on 2 GPU's, out of memory


2018-04-13 22:07:39
rendering test on p2 instance w 4xGPU took about 45 min


2018-04-13 23:03:29
reading thru the issues on jcjohhnsons neural-style repo is fascinating. Like a social network full of useful information. There are a handful of author whose names kept coming up (in 2016) Many subtle issues

about to kick off a multires rendering


2018-04-13 23:10:36
something wrong with my script for 3rd pass render
found the problem
trying again with benchmarking in spreadsheet


2018-04-13 23:32:11
investigate next:
- what happens if another script tries to use a GPU already in use?



2018-04-13 23:48:59
another error when attempting a multipass render - believed related to GPU memory full


2018-04-14 01:53:08
mult-pass rendering has a resolution limit based on GPU memory. The output looks amazing, better than Pikazo

limit for P2 instance appears to be 2048px
limit for P3 instance is?


2018-04-14 02:04:29
bencmarking the P3 instance at 3620px
its incredibly fast


2018-04-14 02:09:10
what is the largest image than can be computed on a single GPU?


2018-04-14 02:49:29
It's unexpected, but square aspect images take more memory than any other kind


2018-04-14 11:51:47
Today

x set up deepdreamvisionquest AV rig
- collate known good style images
- collate known good content images
- collate known good rendering scripts at different resolutions
	+ 512px
	+ 1024px
	+ 2048px
- setup EC2 GUI/CLI  workflow on Windows


2018-04-14 18:36:24
setting up deepdreamvisionquest with projector and AV rig as displays. There are more variables than I had realized to make front-facing video feedback happen. Taking visual notes on that.

My daily goals for wortkshop tech exploration remain


2018-04-15 00:42:26
spent most of the day experimenting with the deep dream projector setup. Not an obvious win, at least in the scenario I setup. A single display makes sense from what I can tell so far

The problems I encountered:
- aspect ratio of projector is different than the AV rig, one of them always gets cropped
- hard to position screens so that feedback effect happens effectively. Tight zoom appears the most promising
- hard to control auto exposure, suggesting the use of lights on the subject so that the other screen is exposed reasonably
- too much going on at once on the screen (withouyt a tight zoom anyway). Looking at it on a single display felt much more calming

2018-04-16 21:28:57
pulled numerous style transfer candidate images for exhibition. will collate in the am and send out to respective partners. Picking back up on workshop documentation

2018-04-17 01:20:18
working on workshop documentation. I can already tell it will be a wall of text - need to break it up into steps
seperate pages for creating CLI, creating GUI
needs to feel like you're making progress instead of scrolling

2018-04-17 09:12:46
collating selected imeages for Jordan & Betty ETA 1h

2018-04-17 14:34:41
Took a bit more than the estimated hour, but I've pulled several series from my archives and shared them with Jordan & Betty

2018-04-17 18:54:14
updated website with new galleries from the assets I pulled this am

2018-04-18 02:29:34
completed Windows setup for downloading software and installing PuTTY

next
- document steps to install FileZilla
- document steps to configure Filezilla
- demonstrate FileZilla by dragging a file into the root window

For all platforms:
document usage of Filezilla
encourage participants to explore the file structure of the server and point out the resources we'll be using
- be sure to save the scripts and pictures in the same directory

2018-04-18 22:35:32
continuing to work on the windows setup documentation. Spent toime cleaning up the format and editorial. With what I've learned, it shouldn't take nearly as long to describe FileZilla setup

The core of this document is the examples and analysis that I've not yet started thinking about

2018-04-19 01:02:52
completed windows setup guide will need to d redo the Mac setup guide in the same format. For the moment I've just copied the WIndows instructions into this doc. THis doc will be shorter, as we can use the Terminal directly instead of installing and configuring PuTTY


2018-04-19 12:05:27
completed mac setup steps up to Filezilla connection to server


2018-04-20 01:35:39
Filezilla is a bit tedious for doing this fluidly. Forklift offered a much more Mac-like experience. But still - if there are mixed groups of Windows and Mac users it woild be 4x as complex to switch workflows between Filezilla (Win) and Forklift (Mac). So Filezilla it is. Previewing files in context is the issue. You cant help wanting to see it in a file browser.

Are there any other cross platform SFTP solutions?


2018-04-20 02:29:30
resynthesized a couple of Marpi's images that He'd sent over wondering what they would look like styled with Haeckel. Some interestiung results - one in particular where I applied radial blur to the edges of the imnage - which worked well with that image - caused parts of it to deattenuate. The motion blur reads like depth of field or lens effects in the finished render.


2018-04-20 20:07:16
Cyberduck is much simpler to setup than FileZilla and allows for standard MacOS preview using spacebar
- redo FTP setup setps for MacOS

2018-04-20 20:46:29
Cyberduck is less usable on Windows.

I need to change the way I think aboyut this
The problem I'm solving is that people need to see the imagery they're working with. Attemting this in a FTP application isn't going to work. It would be easier for participants to download material from the server to their local machine where they can use their native tools to review and manage imagery

- so no need to specify a different FTP App
- Need to fill in MacOS terminal ssh connection details though
- need to end the steup with instructions to download a single folder from the server which will contain all images and scripts
	+ the goal is to enable drag and drop froma window into FileZilla and not think about navigating any directory structures in Filezilla


2018-04-21 14:47:26

I'm working on the UX for managing and submitting files to the server and trying to simplify this to avoid switching between directories
- annotate basic render script for participant edits
- save basic scripts for different resolutions
	+ 512px
	+ 1024px (use multi-rez method on single GPU)
	+ 2048px (use multi-rez method on GPUx2 (?) - it may take 4GPUx4 to render at this size
- investigate creation of user accounts on ec2 server


2018-04-21 15:06:37
one scenario which has happened more than the others is:
- when I'm iterating through an image, I have a script in front of me that I'm editing from the server. That is to say, every time I save this file, the server prompts me if I want to upload & overwrite the original
	+ this is great for rapidly iterating through images, but because the output file name is derived from the script name, any prior output files are overwritten when the edited version of the script is rendered
	+ A couple of possibilities occur to me:
		* tell participants to save their output files to the desktop
		* include a timestamp in the output filename
		* include an output filename string in the script


2018-04-21 15:36:54
hard to say what the proper workflow is without iterating thru seravl renders and watching what I do


2018-04-21 15:38:47
creating new users on the ec2 instance is probably the best practicem, but will involve further setup details I'm not prepared to implement or document. SO instead, I am going to create a fixed number of user folders on an ec2 instance


2018-04-21 17:13:31
setting up a user folder to test with. This method involves duplicating neural-style for every user folder. The network model is large - about 600MB


2018-04-21 17:30:38
I'm not sure I can just move neural-style around like this. ah - actually yes, I can.


2018-04-21 17:54:14
observing myself. I'm zeroing in on something I like and experimenting by changing the values in the script opened remoptely from the serve
every time I save the script I lose my old values
but that's fine - if I see something I like, I can save a copy of the script to the desktop and upload it later
for the moment, I'm more interested in changing values
every time a render completes I refresh the output folder and right click to view/edit the rendered image (which is named after my script)
If I want to compare images or see progression, I save these images to the desktop
I can organize them later
sometimes I delete everything in the output folder so that I can clearly see new files as they render and don't get confused
the output folder should be treated as temp/volatile storage
if there's anything in there you want to keep its best to save it locally
rename this as "temp" to emphasize that
this workflow is super easy because I don't have to type anything into the console after doing so the first time I run the script, I can just keep pressing the up arrow and use command history

the exercise I'm doing now with this wasp image demonstrates refining abnd image to resolve details better


2018-04-21 18:24:22
is it possible to run the render script from outside the neural style directory


2018-04-21 19:00:16
fast-style-transfer and associated webcam demo not working on the Lunux machine. Unclear why. The last time I was here it was.


2018-04-21 20:09:20
created a second user folder and rendering successfully from that. maybe it would be better tio have a seperate directory for scripts after all?


2018-04-21 23:34:59
neural-style on Linux works just fine. So why isn't fast-neural style working?


2018-04-22 09:37:28
creating and setting up a p3.16xlarge instance for this afternoon's workshop rehearsal


2018-04-22 09:42:28
this message again:
Launch Failed
You have requested more instances (1) than your current instance limit of 0 allows for the specified instance type. Please visit http://aws.amazon.com/contact-us/ec2-request to request an adjustment to this limit.


2018-04-22 09:45:39
I've submitted a case number to increase my number of instances of this type to 2. For the rehearsal I can get by with the existing p3.8xlarge


2018-04-22 10:00:23
USERNAMES
- Fox
- Otter
- Raven
- Tiger


2018-04-22 10:27:18
I've setup the Tiger account w render scripts pointing to gpu 0
duplicating to create the others


2018-04-22 10:43:02
I've setup all the accounts and edited the render-512.sh script to use single gpu. Performing render test now - its all working as expected - each user is rendering simultaneously. What I am curious about though, is what happens if a mult-rez render is taking place, and an additional rendering job is submitted?


2018-04-22 11:31:42
testing high-rez render script


2018-04-22 12:02:50
working. copying over to other users


2018-04-22 12:18:15
testing hirez script w other users. interestingklty it seems that at least 2 instances of this can be rendering simultaneously. maybe more


2018-04-22 12:42:48
editing the wiki. Remember - before the rehearsal you'll need to edit and connection text to reflect the current DNS

- add final configuration step for copying pictures folder to local machine so that images may be easily inspected and managed).
	+ direct participants to find their user folder in:
		* FileZilla
		* Terminalo
	- Here are some use cases
		+ an image was edited and needs to be uploaded to the server
- add Worklow Tutorial page
	+ inspect the workspace
		* GUI File Transfer Manager
			- file structure
		* CLI Unix Shell
		* GUI File Manager/Preview (OS)
	+ render default image using the CLI
		* render-512.sh
		* monitoring the rendering process
		* viewing the output
			- must navigate to output folder in FileZilla
			- must right-click on file and choose View/Edit
				+ image will in assigned OS preview app
				+ how to save this image to your laptop
				+ how to delete temp images


2018-04-22 12:52:22

3h before workshop. I'm on track with my time to present
- how to view output on projector (from MacBook)
	+ can Macbook be setup on CPU cart?
- display wi-fi password on projector
- hand write usernames and assign to people

	+ setup initial (default) re

I've setup the macbook on the cpu cart and am mirroring laptop display to projector so I can step through the workshop along w the team


2018-04-23 23:26:27
The workshop rehearsal was a lot of fun. There was a lot of enthusiasm and experimentation once people got into the flow of it. It seemed to me like it took an hour for the entire group to get there. I was surprised to see the natural workflows people came up with after reading my instructions. I requested feedback about the workflow people discovered for themselves

- is the setup documentation too specific?
- review the workflow feedback and derive a common series of steps for a Workflow page
x I noticed that there was always some uncertainty about the freshness of the output folder
	+ some participants got into the habit of immediately downloading the output folder to the desktop. But even then there was always uncertainty.
	+ I would like to add a unique identifier to each rendering job, but I dion't know how to do so other than appending a timestamp to the filename. The script doesn't know how many times its been run.
x how many 512px images can be run on a single GPU?
x how many 2048px render can be run simultaneously?



2018-04-23 23:56:50
I am still awaiting a response from amazon on increasing the number of servers I can run, but also wondering if the request is overkill. I need to try rendering multiple images on a single GPU


2018-04-24 00:12:07
It is possible to render at least 4 multiple 512px images on a single GPU, although I saw memory usage spike to 13GB briefly before stabilizing at maybe half that value. Rendering time is much longer than beofre. I looked up expecting all 4 to be completed but the first one is only now at 900/1000 iterations


2018-04-24 00:39:25
fantastic - found a way to increment a string every time a script is run.


2018-04-24 00:15:12
what if all the renders started at the same time? would it work?
no apparent problem doing so for 512px images
I was able to start a 5th render, and that caused no problems either, which is encouraging. Perhaps the impact of 2 participants on a single GPU is not huge. If so, then a single p3.16xlarge instance could support 16 participants


2018-04-24 01:11:41
Took a bit of hackery to get sequentially named rendering working, but looking solid now



2018-04-24 02:00:57
participant notes on workflow

Gabrielle
- most of the time used the images I preloaded
	- navigated or defaulted Filezilla left panel to show desktop folder
	- downloaded the render script to desktop by drag/drop in Filezilla
		+ opened it in sublime text
		+ saved file
		+ refreshed desktop panel in filezilla
		+ uploaded the renderscript to server using drag/drop in Filezilla
	- used command history in CLI to run the new render
	- downloaded temp folder to desktop
	- renamed temp folder on dekstop

- when using her own images
	+ copied image to pictures folder on desktop
	+ renamed image to match the sequential naming I used
	+ navigated to pictures folder on Desktop in Filezilla
	+ dragged new image to pictures folder on server in Filezilla
	+ edited render script on desktop to use filename she created
		* saved, uploaded, rendered as mentioned above

- she notes that seeing the jcjohnson examples gave her the confidence and excitement to get a certain look and feel (style vs content weight, style scale)

Sepid
- suggests downloading everything, including output since viewing from content menu in Filezilla did not work (Sepid had other defaults applications than a plain windows install)
- Make it clear than when processing photos, these new images must be uploaded back to the server by dragging them into filezilla
- mentions some indeterminacy when working with the temp output folder
	+ at the time, all new output overwrote old output
	+ have since modified that to save each render with a sequentially updated identifier so that nothing is overwritten
- she brought up the need to create seperate rendering scripts
	+ no_gradient true
		* default values for style weight content weight appropriate
	+ no_gradient false
		* appropriate default values for style & content weight

Jordan
- Jordan is expert user and had no problems
	- He modified the scripts to keep a record of each render
- suggested timestamping or otherwise differentiating the temp output files
	+ brought up possibility of creating new temp directores with each render instead of creating new (timestampped) files in the same temp directory
		* let me think that through - is segmenting them per render the better choice?
			- speaks to sepid's comments about needing to download the output to view it. it seems like it would be easier to download an enture directory with your output instead of selecting specific files.
			- how expensive is it to make that change in the script?

2018-04-24 02:23:11
4 simultaneous 2048 renders fail. I kicked these off more or less at the same time, let me try staggering them a bit


2018-04-24 02:45:35
2 of the 4 2048px renders I started failed, while interestingly - 2 did not. So it seems that 2 hi-rez rnders can be run simultaneously on a 4 GPU system


2018-04-24 02:47:27
- is the setup documentation too specific?
- review the workflow feedback and derive a common series of steps for a Workflow page
- how can the outputs of the group be presented to the group for discussion?
	+ for the first few exercises it will brungthe group together if we can look at everybody's outputs and talk about them
	+ when people begin experimenting, showinggroup activity and talking about it isn't the right flow, but it may be interesting to do a bit of performance art
		* is there an automator behavior or commandline tool (ffmpeg?) that ec2can automatically create gIF's from a folder?
		* I could download user temp folders as the workshop runs, turn them into GIF's and loop them as the workshop switches into experimental mode
- as part of the parameters discussion, the role of normalize_gradients should also be mentioned along with examples and constrainst of using it vs not using it


2018-04-24 08:27:06

Amazon responded by allowing another instance for the p3.xlarge server type. Setting up that machine now


2018-04-24 11:26:15
finished setting up neura-style on the new p3.xlarge server
- create user folders
	+ create new users
		* total of 16
	+ for half the new users, setup render-2048.sh to use gpu 4,5,6,7


2018-04-24 11:32:50
I'm going to terminate that xlarge machine and setup a new one. the home folder has the dependencies in it, and I preferred a clean home folder so the users folder was obvious


2018-04-24 20:56:26
rebuilding server


2018-04-24 20:59:22
looking at participant research


2018-04-24 21:15:08
server setup validated -
running neural style

Gabrielle
- most of the time used the images I preloaded
	- navigated or defaulted Filezilla left panel to show desktop folder
	- downloaded the render script to desktop by drag/drop in Filezilla
		+ opened it in sublime text
		+ saved file
		+ refreshed desktop panel in filezilla
		+ uploaded the renderscript to server using drag/drop in Filezilla
	- used command history in CLI to run the new render
	- downloaded temp folder to desktop
	- renamed temp folder on dekstop

- when using her own images
	+ copied image to pictures folder on desktop
	+ renamed image to match the sequential naming I used
	+ navigated to pictures folder on Desktop in Filezilla
	+ dragged new image to pictures folder on server in Filezilla
	+ edited render script on desktop to use filename she created
		* saved, uploaded, rendered as mentioned above

- she notes that seeing the jcjohnson examples gave her the confidence and excitement to get a certain look and feel (style vs content weight, style scale)

Sepid
- suggests downloading everything, including output since viewing from content menu in Filezilla did not work (Sepid had other defaults applications than a plain windows install)
- Make it clear than when processing photos, these new images must be uploaded back to the server by dragging them into filezilla
- mentions some indeterminacy when working with the temp output folder
	+ at the time, all new output overwrote old output
	+ have since modified that to save each render with a sequentially updated identifier so that nothing is overwritten
- she brought up the need to create seperate rendering scripts
	+ no_gradient true
		* default values for style weight content weight appropriate
	+ no_gradient false
		* appropriate default values for style & content weight

Jordan
- Jordan is expert user and had no problems
	- He modified the scripts to keep a record of each render
- suggested timestamping or otherwise differentiating the temp output files
	+ brought up possibility of creating new temp directores with each render instead of creating new (timestampped) files in the same temp directory
		* let me think that through - is segmenting them per render the better choice?
			- speaks to sepid's comments about needing to download the output to view it. it seems like it would be easier to download an enture directory with your output instead of selecting specific files.
			- how expensive is it to make that change in the script?
				+ not expensive. I have the basic mechanism working


USERNAMES
- ant
- bear
- bee
- dolphin
- eagle
- elephant
- fox
- housecat
- lobster
- otter
- octopus
- pony
- rabbit
- raven
- snake
- spider
- tiger
- wolf


2018-04-24 22:49:52
added some additional code to render script to avoid edge case where output directory alreeady exists. testing that now before adapting multirez
great. looks like its working


2018-04-25 00:55:18
I'm prepariung my thought about what kinds of examples to show
Best to keep moving and detail the workflow


2018-04-25 15:29:19
making good progress on the wiki documentation.
completed Prepare your workspace page
working on Create your first image page

x Prepare your workspace
	x replace pictures found in this doc
x Create your first image
x Learning the workflow
x choosing content and style
% changing styling parameters
- manipulating input
- high-resolution output


2018-04-25 19:34:12
end of the activity pages is in sight, they can be progressively less detailed as the operations described become familiar

For the overview of my work with Style Transfer and neural visualization, I'll use the deepdreamvisionquest.com site as support material.


2018-04-25 21:59:39
picking back up on wiki documentation. My goal is to complete Choosing Content and Style and Changing styling Parameters in the next hour then move on to working on deepdreamvisionquest for tomorrow's exhibition.


2018-04-26 00:31:02
I've completed as much wiki documentation as I can and its looking good. Its solid. There is still additional content remaining to create before the workshop, which will need to be done tomoorow night after the opening.


2018-04-26 00:32:04
It's much later than I wanted it top be, but runing through deepdreamvisionquest to curate and cleanup the program settings ETA 3h



2018-04-26 01:27:01
running into some problems with native 1280 x 720 output being projected at 1280 x 800. The image doesn't fill the screen, instead showing letterboxing. It shopuld be possible to scale the display to an arbitrary size, but not eager to do this at this late hour.


2018-04-26 02:43:23
resolved issues with native display and  ubuntu titlebar visibility by using the projector's zoom function. Its zoomed in 1.25x, which reduces resolution but barely noticeable at the wall-sized projection


2018-04-26 02:44:40
Curating progam settings now



2018-04-26 03:28:06
getting somewhere new with updated JOI.00 program


2018-04-26 03:39:24
the xform array effect has been deprecated, but its interesting how it breaks up the screen -  its running much slower with the large numbers I entered. clearly affects performance


2018-04-26 05:35:02
completed adding and editing new programs

2018-04-26 14:01:48
I'm here at the Palace of Fine arts setting up. Stress is passing. Had to return home for webcam cable that I forgot to bring with me. No one is in the room right now.

Projector is connected. Just a matter of cleanup and refinement. Waiting for that projector table top arrive is currently on the floor


2018-04-26 16:16:42
cleaning up the install. Some hard lessons learned about objectifying the projector and integrating webcam into standalon config like this. No one is complaining about it but me, but instead of worrying, just listen asnd learn.

will want to rearrange the setup for tomorrow


2018-04-27 17:58:12
first workshop went well, room for improvemntthough - most notably, I will offer to setup anyone's machine who needs assistance in order to get to the image making sooner

While its running here, I'm making a note of program settings that are working and aren't working

- console
- cube
- metamachine
- Robot Lover
- JOI.00
- Aviary
- 0430
- Starship Maybe
- SEAWALL.01
- SEAWALL.02
- SEAWALL.04
- SEAWALL.``
-






2018-04-27 06:18:18
finalizing the documentation for today's workshop

SETUP
x verify mult-rez rendering script
x verify that all user accounts have default configuration
P2 create seperate user accounts on p3.large server

CODAME
P1 artist statement for Jordan

DOCUMENTATION
P1 Manipulating the Input
P1 High Resolution output
x before leaving, start the server, and include its ip in setup documentation


2018-04-27 06:32:25
verifying multirez render script


2018-04-27 08:14:49
created fully qualified user accounts with proper name, gpu and multi=gpu assignments. Cleared out contents of etc/ and temp/ folders.

I'm going to leave the server running so I can copy/paste the ip into the docs and verify that it's valid


2018-04-27 08:31:47

updated mac setup to include current server IP
updated mac setup to include current server IP

these setups were previously validated on macOS and Windows during last weekend's rehearsal


2018-04-27 08:54:29
I've repurposed a LASER Talk keynote to serve as my introduction


2018-04-27 09:23:34
completed High Resolution rtendering page


2018-04-27 10:46:05
completed manipulating input page
making quick edit to Editing OParameters page


2018-04-27 10:54:16
ready to present

2018-04-28 15:42:15
good workshop earlier

2018-05-01 08:50:36
- setup workshop retro with Jordan and Bruno for Thursday evening
- follow up w Euan about texh talk/exhibition at Stanford
- schedule private GPU server
    + name the event
    + invite Sonia Samagh
    + invide Gaston
    + invite Alex Glow
    + invite Jordan
    + invite Sepid
    + invite Gabrielle
- follow up on print inquiry submitted by email to info@deepdreamvisionquest.com
- setup CPU Cart for dev
- setup AV rig for dev
- more projector research
	+ return ultra short throw?
	    + return valid until 5/5

16 x 20
40.64 x 50.8

Gary Boodhoo, Artist
info@deepdreamvisionquest.com
https://www.deepdreamvisionquest.com/
Instagram | Twitter


2018-05-01 21:40:12
for workshop with Euan & Ramin at Stanford
target date is May 17

What I need from you, just to make it clear:
A timeframe - length of workshop and time that works for you - I've got you slated for Thursday the 17th of May as a placeholder, but lmk since it really is only a placeholder given what you'd informed both me and Ramin of in our call.
A couple of images you'd think would be the exemplars for promotional material, like your most shining prideful stuff, maybe source images like the images that led to this gorgeous agglomeration: [image of House of El - Buddha Face] Plus a brief artistic statement/bio, a pic of yo face, and an enticing description of the workshop. Please populate a Google Drive file and link it to us when you get around to it - the sooner the better!



2018-05-02 17:42:36
Here are the usernames/participants from 4/28:
Alligator - Ed
Bear - Alan
Cat - Alex
Dog - Pedro
Eagle - Brooke
Ferret - Jeff
Octopus - Gaston
Tiger - Bruno's kids


4/29 workshop
These are the people from today's workshop:
Alligator: Li Yu
Bear: Cindy Clark
Cat: Changboi Li
Dog: Yiying Lu
Eagle: Krista Gambrel
Ferret: Alex Tam
Octopus: Josh Santagelo
Tiger: Jordan Gray
Ant: Jeffrey

2018-05-03 19:00:19
putting together documentation Euan requested for Stanford ArtX event

A couple of images you'd think would be the exemplars for promotional material (like your most shining prideful stuff)
	- maybe source images like the images that led to this gorgeous agglomeration:
	- images you think encapsulate your work well!
		+ including technical images,
		+ diagrams
		+ formulae
		+ whatever you think would be relevant o convey a confluence between art and technology
x Brief artistic statement/bio,
x a pic of your face
x enticing description of the event

2018-05-03 19:33:05
1. introduce concepts & background behind neural imaging

2. present and discuss pre-rendered video and stills demonstrating my journey into the method (projected)

3. present and discuss realtime demos (projected)  using freestanding webcam

4. introduce the personal art object (deepdreamvisionquest) running on self-contained AV rig

my intent here is to treat the projection as impersonal and contrast with the "magic mirror" that you stand in front of

katyang@stanford.edu
rahmari@stanford.edu


2018-05-04 02:07:09
planning for Image Garden server access on Saturday

2018-05-05 11:21:55
IMAGE GARDEN
- who
- what
- when
- how
	- how to invite & communicate

Also taking a look at setting up webcam demo for fast style transfer. Why does it work on this machine and not my dedicated Linux box? what are the differences?

get CUDA version
nvcc --version

get openCV version
$ python
>>> import cv2
>>> cv2.__version__
'3.0.0'

get LUA version
th
print(_VERSION)


OpenCV version
- this machine (Win/Linux)
	- OpenCV v2.4.9.1
CUDA version
- this machine (Win/Linux)
	- Cuda compilation tools, release 8.0, V8.0.44
LUA version
- this version (Win/Linux)
	- Lua 5.1


2018-05-05 16:01:09
received new projector EPSON HC2150
its a standard projector type wirth a bit more flexibility in placement than tghe ultrashort throw, although with the additional possibility of getting in the way of the projector display and casting a shadow unless placement is considered, the ideal case is one in which the projector is mounted such that it is projecting dowmnward and precludes the possibility of getting in its way


2018-05-05 19:39:28
The Magewell HDMI to USB decice works and doesn't work. It's seen as a video device, and a program like Cheese webcam can view the signal (coming from my camera). Encrypted HDMI signal from AppleTV is unrecognized, and I see color bars w this message in Cheese webcam program

getting openCV to view the signal as a webcam input isn't working though. This meesage appears from Python:
VIDEOIO ERROR: V4L2: Pixel format of incoming image is unsupported by OpenCV

Frustrating, but sureley solvable? Seeing the issue elsewhere on the web for different use cases, including scientific cameras


2018-05-05 19:43:18
So far no RSVP for the image garden server tonight. feeling a bit bummed out about it.  Ah, Jordan is in. Cool


2018-05-05 19:52:31
some success with HDMI to USB. Initial problem may have been that Cheese webcam apop was running in the background and camera was not available. May not be significant, but  I set the camera HDMI out to 720p. At that point when running /code/bin/camera-sizer.py I was able to see the HDMI out from the camera

2018-05-05 20:26:19
getting server ready for Image Garden. Will be running for 4h. Apprimate cost is 4*24.48 = approx $100

2018-05-05 21:20:59
Image Garden is running

2018-05-05 23:43:44
Sepid RSVP'd. Not sure if she's logged in yet


2018-05-06 03:08:14
wrapping up image garden
made some great steps towards styling artist faces w CODAME poster
- collate and share on slack

2018-05-06 03:18:14
shutting down server


2018-05-08 00:53:55
Sepid had logged in the other night and made a fantastic artwork
I'm finally taking a close look at rem.py and related code. Not sure how much time is available for gthis until I do some planning & strategy, but is important to do so - I'm having a hard time understanding the consequences of any changes I make


2018-05-08 04:27:31
Very interesting variation on interaction style for deepdreamvisionquest. Without going into detail - using the composer rate funtion it  shifts the focus from tracking participants to trying not to disturb the computer. Weirdly disorienting (a bit terrifying at one point)  results at lower resolution rendering. Can  this be simulated without reszing the camera

Mapping the flow of this program in its entirety could take much longer than expected, but maybe bits and pieces of it are easier using a varierty of methods and not sticking to a single (unknown) method.

2018-05-09 13:40:39
visualizing some funtionality for rem.py
the main areas involve understanding and maybe reconsidering how rendering and compositing are done

2018-05-09 15:18:34
notes

# how many buffers are there?
2

# buffers are populated with
Composer.send(buffer, img)

# at what points in the flow are buffers being populated?
diagramming this

# how is an image displayed in the viewport?
Viewport.show()
- this takes 2 buffers as input and mixes them together with variable opacity
	+ the opacity is set by the Composer.ramp thread

# at what points in the flow is Viewport.show() called?
Its called after a full REM cycle returns
? should this use the image returned by Composer.dreambuffer = deepdream()

It's called within a dream cycle after each iteration completes

# What does the Composer.ramp do? Why is it a Thread?
This is intended to behave as a fader control. Its setup as a thread so that it can work asynchronously to the display rate (which is currently a variable frame rate due to deepdream calculation time)

# what does Viewport.force_refresh flag do?

# what does the Composer.isDreaming flag do?
this flag



2018-05-10 09:57:26
I want to take a closer look at how the webcam image is being composited to fix the "jumping" issue on inceptionxform - and also to fade out the webcam image when there is no motion registered

- how predictable is the motion start/stop registration
	+ its predictable enough as a rugh kind of filter but due to repeat triggering and noisy signal is not a reliable/smooth method for attenuating the webcam input when motion stops
	+ after studying the code for a while I realized that the delta_count_history value is already doing what I want
		* will need to get this value and apply it... when?
		* will need to scale this value so that its range is between 0 and 1 ... how?


2018-05-11 22:24:41
deepdream

if Viewport.force_refresh == True
	Composer.isDreaming = False

if octave == Model.octave_cutoff
	Composer.isDreaming = True

- end of iteration
	Composer.isDreaming = True


Composer
	update
		if self.isDreaming
			self.isDreaming = False


2018-05-12 14:54:42
I don't think it will be p[ossible to just normalize the delta_count_history value to a number between 0 & 1 - unless I set a minimum and maximum value that correlates with 0 and 1

what would this mean for small motions
what would this mean for large motions?


2018-05-12 15:54:34
looking at the values in the console output it seems like I could set a different max value (correlating to 1.0) for each  time the history ramps up - which it only does in response to motion


2018-05-12 20:47:45
How do I map a value (x=50) in a range of 0-100 to a new range of 0-10?

OldRange = (OldMax - OldMin)
NewRange = (NewMax - NewMin)
NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin

OldRange = (100 - 0)
NewRange = (10 - 0)
NewValue = (((50 - 0) * 10)/ 100) + 0


2018-05-12 21:55:58
use this helper function to scale ranges instead
def scale(val, src, dst):
	# src is [min,max] old range
	# dst is [min,max] new range
	return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]


2018-05-12 22:42:11
the mechanism for using the delta_history to modulate webcam opacity is working, perhaps too well. Any spurious noise in the image is causing peaks where opacity shoots up to 1.0 and the webcam image appears to flash on screen. how to filte rthis?


2018-05-13 19:11:45
the changes I made yesterday have the system smooher an more responsive than ever and in my tests last night 1080p output seemed pretty performant, although many of the vgg19 program settings caused a crash (out of memory)


2018-05-13 19:13:36
to run tensor flow material its looking like I need an updated setup which I'm reluctant to do. If I cant get the style transfer webcam demo working with current config, I'm going to look at the nvidia docker solution and hopefully be able to avoid setup with an existing container. If hat is the case will be interesting to see how deepdreamvisionquest runs in that configuration as well


2018-05-13 19:28:37
webcam demo is working
non-installation of CuDNN was the problem
there's a flag that lets you disable CuDNN (although it is the default)
similar issue with output quality as before
solution is described here, need to update Torch
https://github.com/jcjohnson/fast-neural-style/issues/137


2018-05-13 19:31:41
Install Nvidia CUDA 8 and cuDNN 6
https://yangcha.github.io/Install-CUDA8/


2018-05-13 20:09:37
playing with the projector. Amny doubts I had about it disappeared. extremely flexible positioning including sidewide. Not minding the shadows either, and in general and amazing light source

web cam style transfer demo is working, trying iout some options and also larger output

qlua webcam_demo.lua -models models/instance_norm/candy.t7 -gpu 0 -use_cudnn 1 -height 720 -width 1280


2018-05-13 21:51:52
installed CuDNN 5.1 (fast neural style apparently requires this version, possibly hardcoded filenames?) Testing that to see if performance is improved

Download cuDNN 5.1 from
https://developer.nvidia.com/cudnn

Install cuDNN 5.1
```
tar -zxvf cudnn-8.0-linux-x64-v5.0-ga.tgz
sudo cp -a cuda/include/cudnn.h /usr/local/cuda/include/
sudo cp -a cuda/lib64/libcudnn* /usr/local/cuda/lib64/
```

2018-05-13 21:53:41
wow - no problem w 1920 x 1080 output
resolution seems like it may be constrained by maximum camera image size. I don't think display widows are of arbitrary size. using C920 that max is 2304 x 1536


2018-05-13 23:22:39
some promising tensorflow solutions I;'d like to have available. Apparently installing tensor flow involves new drives, new Cuda, and not wanting toi dio that so taking a look at docker and nvidia-docker'


2018-05-13 23:34:14
installed Docker, verified working


2018-05-14 01:41:13
installed nvidia-docker, verified working
except apparently needing to run it as sudo


2018-05-14 10:29:27
now that nvidia-docker is online, then what?
I'm using floydhub prebuilt ML container
- build docker image locally
	+ I think this builds a version of Linux inside the container
- run  docker image as container

started build, but again had to do so as superuser, and not sure why


2018-05-14 12:09:18
looking any further into docker/tensorflow at this time is a red herring. Need to collate my current status - dteail what I can do/can't do/ wnat to do

specifically -
Deep Visualization Toolbox

Possible to generate class visualizations?


2018-05-15 00:08:14
yes, there's apython notebook I'm going to play with for a bit


2018-05-15 23:22:36
working on ArtX Presentation and technical setup on 2 external displays


2018-05-16 10:36:13
familiarizing myself with the class visualization  Python notebook. Modified code slightly so we can see each iteration being drawn


2018-05-16 14:31:57
class visualization is much more interesting and flexible than I realized. The strategic blurring in the "deepdraw" code is something I can apply to deepdreamvision quest to cleanup teh rendering, but also to expand on the vocabulary of renderings


2018-05-16 17:41:28
spent unexpected time working on deepdreamvisionquest. Improved rendering quality and discovered some additional parameters for manipulation. Expected to be deep into the presentation doc, but time well spent for demo


2018-05-17 12:13:01
completed presentation candidate. Exporting to Linux as HTML for testing and quick walkthrough


2018-05-23 21:56:08
continuing to examine  rendering and compositing in rem.py
what I want to try is this:

when motion is detected:
capture the last rendered frame to buffer3
buffer3_opacity = 1.0

when compositing the next frame
mix buffer3 + composite at opacity: buffer3_opacity
buffer3_opacity -= int(buffer3_opacity/2)


2018-05-24 01:20:01
I implemente dthe behavior described above in a rough form, and its very promising. The experience feels more continuous and smooth. There's an odd bit of timing wen the inception_xform scaling happens - whjere the scaling appears to overshoot the mark and jump back to a slightly smaller scaling. Also noticing an interesting relationship between the currently implemented opacity rampdown and the motiondetyectoion floor.

I actually want the opacity ramp down to happen in relation to the number of steps in an iteration, or at least ramp such that we see less of the lower rez images being rendered because they're hidden by the last high rez image.

similarly other variations - I'm taking any last frame rendered aftrer intewrruption or completion as the "last known good", but I think this should be reserved only for higher octaves - not every octave...


2018-05-25 23:13:15
experimenting a bit with newly arrived micro projector


2018-05-26 00:16:40
Need a stand or mount for better flexibility. Maybe some interesting options, but I've not really figured out how to incorporate projection yet

continuing to examine rem.py - the compositing is still jerky, can it be smoothed?


2018-05-26 13:10:26

Composer.buffer[0] dreams
Composer.buffer[1] webcam


2018-05-26 19:02:52
I've stripped out much of the existing compositing and motion detection behavior and building it back up around the delta_count_history ramping value


2018-05-26 19:31:55
going to refine the inception_xform glitch I'm seeing next


2018-05-27 01:11:06
store history of the value
update the value

compare (value_history + value)/2 with value


2018-05-27 12:44:12
It's working. I've rethought and reimplemented motion detection and compositiong. Still a bit rough around the edges, but sort of amazing actually - many possibilities have opened up, and I think the experience feels way more natural and less twitchy.


2018-05-28 10:18:58
re-incorporated the motion.floor threshold, which works a bit differently than before but continues to reduce the impact of spurious motion

for today
- add non processed camera inputs together into a motion trail
	+ the motion trail will be submitted to deepdream
- reduce motion sensitivity after completing a full rem cycle
- is it possible to dynamically adjust the mean of the network model while rendering?


2018-05-29 01:31:30
I think I've arrived at a tunable system that is responsive to near motion but filters out motion at a distance. Best hallucinations ever.

2018-05-30 17:48:43
working on the setup phase of the workshop
after testing out soem software (alternatives to FIlezilla), I'm going to analyze what I remember fromn the prior workshops
- what was the flow. The sequence of events
- what didn't I talk about
- what did I talk about too much
- what are some areas to simplify?
	+ setup
	+ working with the server
	+ failed renderings due to GPU out of memory
	+ identifying renderings better, and providing the means to recreate them easily
	+ setting up the workshop environment
		- manual creation and initialization of user folders instead of dynamic
- follow up
	+ correlate usernames with personal names and email
	+ how to continue the relationship
	+ promote workshop for workplaces
- how to share what everyone is doing - is it possible to automate a slideshow?

ec2-52-37-56-44.us-west-2.compute.amazonaws.com

ssh -i "synthetic_rsa.pem" :/


2018-05-30 18:10:29
oh this is fantastic. Amazon has a service called Elasrtic-IP that lets you allocate a public IP to an instance. Testing to see what happens if I shut down instance then start it again. Ah that's fantastic. works as expected. Also makes it possible to create meaningful named connections.


2018-05-30 20:31:27
For MacOS, Transmit is a superior solution
What about Windows though?


2018-05-30 20:32:30
Also with at least the current sample images, I'm able to render multi-rez at 2048px on a single GPU


2018-05-30 22:34:34
BASH is amazing and weirdly archaic, dating back to 1989. Way more powerful than expected. FOund a better way to create incremental values with each script run


2018-05-30 23:33:34
apparently not possible to use scp to transfer files from server to local machine from the shell on the server (it doesn't know where the local machine is) I am trying to synchronize the local & remote vies of the user folder


2018-05-31 01:25:06
ssh -i "synthetic_rsa.pem" ubuntu@52.37.56.44



2018-05-31 12:26:50

account template:

users
- username
	+ pictures
	+ renders
	scripts
- username
- username

2018-05-31 18:31:02
found a cool application for trello in confluence - where an interactive trello board is embedded in a confluence page. Perfect for showing a list fo sample picture. Maybe more.


2018-05-31 19:13:41
Oh nice, there is a shared solution for SFTP & SSH setup. From the makers of CyberDuck, MountainDuck maps an SFTP share to your local file system in Windows or MacOS, so the native file manager (explorer, finder) is used for file transfer.

On Windows (probably on Mac as well)


2018-05-31 23:32:59
To clear out stalled processes on GPU, use this
sudo fuser -v /dev/nvidia*
sudo kill -9 PID.

(these PID's are also shown in the nvidia-smi window)

2018-06-01 10:17:42
Bash script for workshop is nearly done. Appears to be working as intended, definitely supports workflow better. The idea is that whenever the script is run, it creates a new project folder where rendered images are stored and copies itself so that the images in that project folder can be re-rendered by running the new script. This allows users to stay in the text editor on the same script while spawning copies that can be executed at any time with specific results.

Users can also supply their own (meaningful) project names, so each rendering is identifiable.

If a user were to shift their focus to a newly created project script, so they might iterate from that point forward, the script will continue to behave as before. Any script executed without a projectname uses the scriptname as the projectname and adds an incremental prefix

Using this in conjunction with Mountain Duck (on both platforms) which exposes the server in the system's native file manager. This eliminates the distinction between local file system and the remote filesystem as they're presented in the same interface using the same methods

01_projectname
02_projectname

more simply, this lets you productively iterate upon images

I'm assigning Elastic-IP's to each ec2 instance so they can each have persistent network identity
I'm working out the script copying part now
I need to figure how to increment the suffix with double digits 00, 01, 02,

syntheticaf-S	52.37.56.44		p3.2xlarge	users:2		GPU:1 (Tesla V100)
syntheticaf-M	52.36.164.64	p3.8xlarge	users:8		GPU:4 (Tesla V100)
syntheticaf-L	52.36.164.64	p3.16xlarge	users:16	GPU:8 (Tesla V100)


2018-06-01 11:30:07
interesting caveat for sublime text on windows
make sure your editor is set to create files in UNIX format.
View > Line Endings > Unix

2018-06-01 16:05:55
I think the new rendering script is done. Adapting it for 512px version

2018-06-01 18:20:14
rehearsal is in an hour
I've written down some of the ideas and methods I want to cover, and will summarize them here as text

rebuilding user accounts on syntheticaf-M server

fox
otter
raven
tiger

2018-06-01 18:57:45
I'vr created and setup those user accouints. testing now

2018-06-01 19:01:01
just noticed that the ORIGINAL_COLRS flag is set to True on the 640px scripts

2018-06-01 19:11:15
everything looks fine with the accounts I created.
I had to go back in to each script and manually set the GPU index
need to replace that with some conditional logic based on username


2018-06-02 00:28:45
good rehearsal. Uncovered some significant issues, and spent time with Changbai afterworkds hanging out and working through the ballpark method I mentioned previously. Ran in unexpected and Major issues on Krista's machine though in which Mountain Duck.app was behaving unpredictably and not integrating with the Finder properly

Later I ran through the workflow with  Changbai using Transmit.
What are the differences between Cyberduck and Transmit as FTP clients?
There's a real value in using a cross platform tool, but if Transmit is the better software for MacOS, that's what should be used.

Still I can't help wondering why Mountain Duck went so wrong on Krista's machine. Perhaps it is a moot point though the new workflow method doesn't rely so much on FTP as before

The use cases are - as a viewer. Its useful to be able to see th material on the server, especially images with previews and standard OS behavior

On the other hand, the workflow was largely identical using Transmit, and even if previews aren't an option in Cyberduck, the images could be previewed in confluence. Figuring out the IT problem isn't the best use of my time. Best to move on and consider this problem solved by using Cyberduck oand/or Transmit instead of Mountain Duck

Also, importantly, we realized that the confluence site I'm setting up wasn't public facing and resolved that issue - which is verified working on my linux machine


2018-06-02 00:41:34
I'm looking at fixing the program settings bug in deepdreamvisionquest now

2018-06-04 10:58:20
preparing for tonight's workshop
- copy updated neural-style.lua to all servers
- edit and test script to generate GPU-ID by folder name
- deploy render script to all servers in dev accounts
- test render640.sh on all servers in dev account
- test render1920.sh on all servers in dev account
- construct test user folder on all servers
- test render640.sh on all servers in dev account
- test render1920.sh on all servers in dev account
- construct user accounts on all servers

- complete Activity documentation
	+ your first render
	+ a method for getting there
	+ parameter examples
	+ reference

2018-06-04 14:38:39
bit of a whirlwind. First the rendering scripts appeared broken. Not sure what the problem was, likely some unnoticed syntax error. I got them working again and implemented the GPU assignment functionality so I coan construct user profile folders by copying the dev folder. Which I am doing now on syntheticaf-L

2018-06-04 15:29:51
that issue cropped up again. I think its a permissions issue on data.txt. Actually, no.


2018-06-05 08:15:09
updating and refining program settings for CODAME ART+TECH Festival


2018-06-05 11:42:59
getting some good results and responsiveness from recent updates. Visually rich like never before actually. Wrapping up in 15min


2018-06-05 12:31:57
finished constructing program set for ART+TECH install


2018-06-05 13:12:18
loading out


2018-06-05 17:26:57
Almost completed  with install at The Midway


2018-06-05 18:54:34
completed initial configuration and lighting setup


2018-06-06 11:28:07
refining some programs here at The Midway


2018-06-06 18:02:49
bringing it online for tonight's exhibition


2018-06-11 21:05:28
cleaned up issue w git repo
studying methods of organizing my code better and consistently

Python modules are one of the main abstraction layers available and probably the most natural one. Abstraction layers allow separating code into parts holding related data and functionality.



2018-06-11 22:00:35

deepdreamvisionquest
	readme.md
	sample/__init__.py
	sample/core.py
	sample/helper.py
	tests/__init__.py
	tests/sometest.py

dreamer
	readme.md
	setup.py
	rem/__init__.py
	rem/rem.py
	rem/helper.py
	models/bvlc_googlenet/files
	scripts/__init__.py
	scripts/script.py
	tests/__init__.py
	tests/test.py



2018-06-13 01:15:48
there's a lot more to unit testing than I'd have imagined though admittedl;y seems abstract to me as I'm not sure how I'd incorporate it into my work.

I actually feel that for setup and configuration, it would be useful to have some utilities to evaluate systems in isolation
- motion detection
	+ with stat readout
	+ with graphs
- lighting assistant
	+ for setting camera parameters and lighting

Some Tests:
- is the camera working?
- how many cameras are attached?
- what is the input resolution?
- how many performance settings are available?
- what is the display resolution?


2018-06-13 23:16:51
after much initial exploration and a bit of soul searching, coding again. Organization is what I'm aiming for

rem.py
	Display
	Model
	Viewport
	Composer
	FX

camerautils.py
	Cameras
	WebcamVideoStream
	MotionDetector

data.py


2018-06-15 16:16:52
continuing to work on creation of a global configuration file. Creating new repo. At some point will create romote version of this on github as well


2018-06-15 16:46:11
...and reading about git again for the hundretdth time(!)


2018-06-15 18:15:00
I'll experiment and verify with a toy repo
The idea is to have 2 main branches with an infinite lifetime
- master
	+ code at HEAD in this branch always reflects a production ready state
	+ every commit on master is a new release by definition
- develop
	+ code at HEAD always reflects a state with latest development for next release
	+ when code in the develp branch reahes a stable point these changes are merged back into master and TAGGED with a release number

2018-06-15 20:06:05
worked through a typical usage scenario with a toy project. Much more refined than before, although still unclear on some of the specifics, like how to handle merge conflicts (I worked through a simple use case, but is obvious a real one would be more complicated)

reason_details-tag

refactor_config


2018-06-16 01:35:24
unexpectedly studying logging
I don't know where I gleaned my current information, but its quite flexible. More than I realize, is what I realize. Definitely simpler approaches are possible, but this is clean and comprehensive

remeber that wgen you set the logging level, you display messages of that priority and higher


2018-06-16 16:02:57
updating and understanding logging better


2018-06-16 16:10:54
interesting email arrived about participating in a sci-art-tech multimedia event being held in August(!)


2018-06-16 16:59:02
as in so many other ways it looks like what I'm doing here at the meta-level is testing and understanding how different bits of my code really work. While not a common scenario, its  pretty enlightening to readout the history buffer from motion detction process to see the underlying rhythm of data collection - but also recognizing the same sensitivity to deepdream calculation speed . long story short, the deepdream bit of the code needs to be running asynchronously and polled at a fixed frequency. Its evident seeing the rhythm of the log output I'm getting. That needs to be the big push for next full release



2018-06-16 17:25:32
TESTS
camera thread starts
deepdream returns initial image
can increment/decrement programs
can step through all programs
can increment/decrement featuremaps
can display last defined featuremap index in all programs
can toggle HUD on/off
can toggle motion monitor on/off
can increment/decrement gamma
can toggle pause on/off


2018-06-16 17:37:55
Hey not too bad - those were some logical and  trackable changes I just made there. Motion detection can certainly be refined further, but for the moment I'm trying to keep it at a higher level of organizing my code better


2018-06-16 20:15:31
getting a bit hung up on what to do next. cleanup is a pretty broad task. focus on the obvious sthough


2018-06-16 21:29:28
although not the immediate task some basic research on python socket programming provides an easy working example of interprocess communication which I think could be used to capture a username for sunsequent outreach:
- add to mailing list
- send image

DeepDreamVisionQuest - CODAME Art+TECH Festival 2018 | @skinjester


2018-06-17 01:36:02
sorta just playing around and discovering some new things. apparently possible to open a cv2.imshow window af fullscreen with no borders or header
seeing if also possible to position this window when initialized


2018-06-17 01:45:43
wow - so it is possible to open a full sized viewport on a specific monitor by default


2018-06-17 02:54:46
updated Viewport class to accept fullscreen flag and monitor assignment


2018-06-17 03:48:41
wrapping up this worksession after discovering some brittleness with the Model class and program settings.will pick up there next
also take a look at how program settings are being implemented.
- Is there a cleaner or more flexible approach?
- What would I want out of a more flexible approach?
- what other parameters can be modulated?

2018-06-18 00:27:12
studying the relationship of the Motion detectror process function and the compositing and motion detection behavior in the deepdream function and it smells wrong.

Why should deepdream (the renderer) know anything about motion detection - it just renders frames

Why should deepdream (the renderer) know anything about compositing, when there's already a Compositing class to organize that behavior

is motion.delta > motion.delta_trigger is the significance derived from the motion detector. Its just a flag though that should get set and acted upon elsewhere

that elsewhere is the Composer object, which should  be integrated  better into the event loop. At the moment, its used as a collection of auxillary functions called from the program flow through the deepdream function



2018-06-25 22:32:53
working in the codebase again. There are numerous opportunitues for featured enhancements, such as attaching program duration to programs themselves, or potentially to some kind of oscillator. The whole idea of oscillators - perhaps running as threads or even arriving from an external source is super-interesting. Before programming that kind of functionality though its important to take a look at existing frameworks which may provide better control of that kind of functionality. Processing? MAX? VVVV? Unity?

My immediate goal with these optimizations is to decouple the logic and seferences in a way that I can at least run the parts as seperate module.py files.

My broader goal is to rethink how rendering works, and at minimum have it operating as a seperate process that gets polled by a display loop at a stable frequency


2018-06-25 22:56:13
2 emails from Betty Bigas at Daylighted on inquiries about my work. What are my outcomes with this? Is this a comission? Can I use this direction to execute the ideas I have in mind for photographing projections?
- at a minimum, I am out of control of my Daylighted account, and need to take a look at that profile before responding so I can take stock of my current position on this platform.
-  how do I log into this profile
-  what is CODAME's relationship with this profile?
- How do I position myself on this profile?
	+ what support material can I provide for each entry here to promote?
	+ use this interest as a datapoint for content to amplify
- How can I represent myself any my interests to this client and turn this into a comission?
	+ what is their level of interest?
		* collector?
		* decorator?
		* casual?


2018-06-26 00:14:27
ive externalized the listener code block into an external file and am passing this function pointers to the objects it's always used. Working.


2018-06-26 00:58:13
externalized listener function fully with logging and hud logging, but motion detection floow ++/-- i handled poorly, making the computation and update in the lister itself rather than in the motion detector object


2018-06-26 01:41:08
abstracted all functionality out of listener so it now calls the appropriate method in whatever object.

next:
- move HUD into a module and verify working
- rethink how HUD is being drawn - is there another way?
	+ what's working
		* the green indication of updated values
			- implementable as decorator? if so, why? would imply this functionality is generalized for any changing values shown
		* the generalized approach to logging values
	+ what do you want to change?
		* code seems heavy and like there's too much of it for what they;re doing
		*  interested in making room for new features I've thought would be useful during dev and exhibition
	+ what is the HUD used for?
		* showing system state
	+ can it be used for promo purposes?
		*  it could show Event Name, My Name, Contact info, Instagram follow, CTA to sign up for mailing list
	+ can it be used to provide instructions?
		* potentially as part of a Messenger HUD mentioned below
	+ can it be used to provide feedback/confirmation?
		* there can be a second HUD mode which is meant to monitor event triggering
			- program change: show name
			- featuremap change:
			- gamma change
			- layer change
			- metering for delta, peak and floor values

I've wondered for a while about the inception_xform function
	- how does the "anchor point work"
		+ how to control the direction towards which scaling happens
	- is it possible (using opencv?) to calculate the center point of the current (raw) video image
		+ this would be independent of motion detection

How to go aboput creating a Recorder


2018-06-27 00:00:29
initial steps for HUD
- analyze what its doing and see if possible to simplify
-  how are messages sent to the HUD
	+  update_HUD_log function is passed to object that passes messaged
	+  update_HUD_log(key, message)

the key is part of a global dictionary
hud_log = {
    'octave': [None, None],
    'width': [None, None],
    'height': [None, None],
    'guide': [None, None],
    'layer': [None, None],
    'last': [None, None],
    'now': [None, None],
    'iteration': [None, None],
    'step_size': [None, None],
    'settings': [None, None],
    'threshold': [None, None],
    'detect': [None, None],
    'cycle_time': [None, None],
    'featuremap': [None, None],
    'model': [None, None],
    'username': [None, None],
    'scale': [None, None],
    'program': [None, None],
    'interval': [None, None],
    'runtime': [None, None],
    'floor': [None, None],
    'gamma': [None, None]
}

each key has a corresponding value, which is a list containing the current and previous values of the parameter being tracked

keyname: [newValue, oldValue]

the update_HUD_log(key, newValue) function
just writes the new value to the supplied key and tracks the previous value. This is so the values can be compared and drawn green if they're different (the value has changed)

So far these machinations only affect the hud_log dictionary. The HUD gets drawn by draw_HUD() during each call to Viewport.show() when the b_show_HUD flag is set

draw_HUD(image) is a standalone function that takes the composite image sent to Viewport.show(), draws the HUD on top of that and returns the image


2018-06-27 00:51:14
while reworking the HUD, it would be great to get some error correction in for feature map increment where list index goes out of range.
- why does it go out of range?




2018-06-27 09:57:32
analyzed the existing HUD code, and its pretty clever. Text is written to a row on the HUD by the ordering of a series of function calls. The key for each parameter to be monitored is set to a write_text() function, which gets the corresponding  value from dictionary and writes it to the current row. The current row is incremented each time this function is called
- what happens if a parameter key is specified that isn't in the dictionary?
	+ crashes w KeyError (Python raises a KeyError whenever a dict() object is requested (using the format a = adict[key]) and the key is not in the dictionary)



2018-06-27 11:04:15
I've got an hour left for this worksession, and perhaps finally a practical usecase for a decorator to count the number of times the write_text function is caller, and eliminating the dedicated counter already in place


2018-06-27 11:16:23
I don'tthink the decorator is a relevant structure here. The write_text function needs to know:
y:		which row to write in
x:		column to write the key value in
xoff:	column to write the msg value in
key:	the key name
msg:	the message string
color:	text color
screen:	img buffer for text drawing


2018-06-28 01:14:09
so I did end up using decorator pattern to increment row every time layout() is called. Or in the mioddle of doing so after succeeding with a test case


2018-06-28 02:59:48
refactored HUD, its working :)



2018-06-28 22:17:16
EXTERNALIZE CLASSES FROM MAIN PROGOGRAM LOOP

PREVENTING CRASHES
take a look at featuremap updates
- how do  I know how many feature map indexes are available for a given network layer?
- what happens when a featuremap index goes out of range?
	+ is there a way to prevent the condition from happeneing?
	+ is there a way to gracefully recover if it happens?



2018-06-28 22:42:57
working with externalizing the Model class
Model has a dependency on Viewport (when the program changes )

Viewport.refresh() has always been something of a mystery. It sets a flag (stored in the Viewport object) that the render loop checks for inside the deepdream() function each iteration. When true, deepdream exits the current cycle and returns a camera image instead of a hallucination. This image will be passed to the neural next on the next cycle. Certain interactions set this flag to true (and thus RESTART the cycle) such as, increment program, increment featuremap, increment layer

Why is this associated with the Viewport though? If anything it's a rendering flag, as it directs that behavior. However, it needs to be callable from anywhere...

- store this flag in data
	+ apply get & set methods
- move deepdream into a seperate module
	+ include the flag in this new module
	+ continue using refresh() method as before, but now called render.refresh()



it doesn't actually refresh anything
it's a switch that routes images from 2 sources to the deepdream function at the beginning of a cycle. a NEW rendering, if you will

render.py
	- deepdream
	- makestep
	- new

	if motion.delta > motion.delta_trigger:
	    log.critical('new dream')
	    render.request_new()

	if render.requested_new():
	    render.clear_request()
	    return Webcam.get().read()

perhaps?
the deepdream function should instead be inside a Render class, with each rendering process being an instance of this (this would allow multiple renders on different GPU's).

render.py
	- Render
		+ deepdream
		+ makestep
		+ request_new
		+ requested_new
		+ clear_request

	from render.deepream import deepdream
	Composer.dreambuffer = Render.deepdream(
	    Model.net,
	    Composer.dreambuffer,
	    objective=objective_L2,
	    iteration_max=Model.iterations,
	    octave_n=Model.octaves,
	    octave_scale=Model.octave_scale,
	    step_size=Model.stepsize_base,
	    end=Model.end,
	    feature=Model.features[Model.current_feature]
	)


2018-06-29 23:56:42
working on seperating deepdream rendering functionality from the game loop


2018-06-30 01:09:16
thinking about how to structure the deepdream renderer
I'd thought to make it a class because I though that would be the only way to track its state with writeable variables global to the scope of the funtionality (member variables of the class)

But now I'm realizing that concept of member variables isn't what I thought, these things are attributes that it would also be possible to set directly on a function without requiring a class. I thought only Classes had this feature.

I'm also realizing that the decorator I used to increment rows on the HUD whenever a certain function was called is a more abstract/dynamic implementation of attribution. All I'm doing is creating a new function that adds an attribute to the old one. But I could just as well set the counter as an attribute of the hud, whose scope would be available globally within the module

render.deepdream.Render.deepdream

renderer.deepdream.Artist.paint


2018-06-30 02:03:50
I need to move any motion detection out of the renderer. That should be a function of the Composer instead. The  Renderer just needs to process octaves and send output to Composer after every call to make_step()

AT that point the Composer will run the existing motion detection code and determine  the mix shown in the Viewport





2018-07-03 00:53:16
making progress with the renderer - I have it hooked up to the main program flow and am please to see how the HUD, listermer, biewport, etc. are working with the test renderer.

Also examining issues of render quality prior to and pre/post processing. By tweaking clipping values in paint() and make_step() independently there's  a range of contrast ratios that seem achievable, and these could beadjusted per step or per cycle or both


2018-07-03 21:52:30
getting hung up on recreating prior behavior
what I actually want to do is have the renderer running independently in a process, and poll its output at a regular frequency. Am I moving away from that goal? I don't think so. The next step in this is to move motion detection sensing out of the  renderer and into the composer


2018-07-06 01:35:42
motion based compositing is working, but not capturing new frame for next dream


2018-07-07 09:41:53
two bugs to fix:
- implement request_new() functionality to pass new camera view into deepdream
- look at what's happening w image brightness/contrast


2018-07-07 18:05:26
well that fix was trivial, just a matter of a mistaken function name
HUD isnt updating properly though


2018-07-07 18:12:12
for the moment get into the habit of copying work to dropbox. not ready to update github w this yet, as I want it to be documented and so forth and think about how I want the work to be presented, or if it is even publicly presented at all. Does that make sense? What if you want to access that code from somewhere else? There's no reason not to create a remote repository


2018-07-07 18:34:28
attempting to push master branch to a github project called "geo" Project:GEO. the network models are quite large, material has been pushing for a little while now


2018-07-08 01:47:51
after some flailing around, I rebuilt the repo so I could sync w a remote on github. Back where I started , but flattened out all the history I'd been keeping up until this point


2018-07-08 03:02:52
started examining a different compositing method, in which opacity is no longer coupled to motiond dection delta history. Possibly better? maybe  more responsive overall? Need to see it with fresh eyes to be certain. the method clearly shows the impact of deepdream computation time on compositing though. turning the renderer into a  seperate process is expected to fox this

2018-07-15 11:31:01
looking at a speaking opportunity at Game UX Summit Sep 26-27 om Vancouver. Responding to invitation on LinkedIn from Kristen Tudor who works in the Learning, Engagement and Performance team at Electronic Arts, Canada

 industry-wide event hosted by Epic Games aimed at:
 - discussing the current state of UX in the videogame industry
 - sharing best practices
 - spreading the love for user-centric insights and design

Hi Kristen, have I got a story for you!
Two years ago I began examining creative applications for machine learning. I first showed my performance art UI at GDC 2016 as a poster session titled "Find Your Spirit Animal in a Deep Dream Vision Quest". Since then, my art practice has expanded into gallery exhibitions, workshops, digital signage and outreach. Every aspect of my science fiction cave painting draws upon my experience in videogame UX/UI

I also run a hands-on workshop titled Visual Strategies for Neural Artistic Style Transfer here in the Bay area. No programming experience is required, but imagine my surprise when I realized there was also a social component to AI image synthesis! Exactly the kind of engagement and collaborative spirit I've sought to embody in my work for the past two decades. Perhaps there is an opportunity here to present this workshop at the Game UX Summit.

I welcome the opportunity to speak with you further about my work, my methods, and how I arrived at this point. I'm quite interested in submitting a proposal but would like to discuss the possibilities further, as the subject is broad. I have previously spoken, for example on topics such as:

- Human Encounters with A Gregarious Learning Machine (describes social and collaborative aspects of AI in social spaces )
- Write better code with English Lit. 101 (* describes the experience of teaching myself Python, and basic Linear Algebra & Calculus to understand implement my machine learning work)
- Visual Strategies for NEural Artistic Style Transfer (hands on imagemaking workshop and talk that introduces GPU computing and AI image sytheis to a non-technical audience)

Please find more about my work here: https://www.deepdreamvisionquest.com/

Thanks for reaching out to me, I hope we'll work together.





I run an interactive video installation titled "DeepDreamVisionQuest". I first showed this work at a poster session during GDC 2016

2018-07-15 14:03:11
adding ArtX event to deepdreamvisionquest.com
visual refinements and content tweaks

2018-07-15 16:31:55
completed refinement pass for website
need to look at making preview image visible when sharing on linked in
need to validate preview images on all pages for sharing on FB/Twitter


2018-07-17 01:48:23
In the process of decoupling the Model object into a seperate program module.
Stepping through numerous errors to integrate the changes. Will com[plte this next work session. Renderer does not seem to have expected values passed to it from the model.



2018-07-21 00:24:58
great my code is working again. was just a syntax error, not sure why I couldn't see it clearly before. Anyway moving on. I've successfully abstracted the Model object from the main event loop



2018-07-21 09:17:59
fixing the HUD


2018-07-21 15:34:08
still getting around to fixing the HUD, started playing around w program settings, discovered interesting aviation on compositing method


2018-07-22 19:45:55
working on re-enabling the HUD. simple enough to do, but trying to package that info more cleanly. Also realizing (belatedly) that all possible HUD stats should be passed at once


2018-07-22 22:03:46
that's not true. The way I'm already consolidating (logging) these values from where they occur makes sense


2018-07-23 00:31:46
feels like I've come full circle w this HUD modification. There was no obvious way to make it more efficient than I was already doing, and yet I feel that there must be!


2018-07-23 15:52:39
completed HUD update

next:
add cycleFX support
encapsulate Viewport object into its own module
encapsulate Composer object into its own module


2018-07-23 23:38:22
code left in broken state due to abstraction of FX class
the way that these functions are being called suggests that they aren't part of a class at all (there's only one instance) but rather, a collection of functions in the the module. The class member variables can be recast as module variables, but will need further refactoring

2018-07-24 14:25:50
researching upcoming UX Summit proposal

2018-07-24 15:35:22
I am talking myself out of giving a 30 minute talk in favor of giving the neural style workshop. Suppose you couldn't gve the workshop though. Do you have nothing to say?

I would talk about my experience bringing creative AI into social spaces.
Introduction
Act 1
Act 2
Act 3
Act 4
Conclusion

I would title the talk:
Is it a commercial for my workshop and gallery installation?
Is it a rags to riches story (what I learned when I overcame an obstacle)

What is the relevancy to game UX/UI?
It is a kind of interaction design that talks back to you, literally.
I came to trust players to have fun
It examines the role of smart objects in social spaces
Multiplayer Hallucinations

2018-07-24 17:58:58
We aim to have diverse representation from the industry, and we really have few limitations on talk topics submitted by our industry partners. Key criteria involves current relevancy, trending topics, and case studies or post-mortems that will provide insightful knowledge to the UX game community.

You'll notice a range of UX topics that have brought incredible engagement in past summits on our submission form:

https://docs.google.com/forms/d/e/1FAIpQLScv1SJqZORJZhTLQvAwJKobjT6ltshudCMCOYXwA-OxTtFyJg/viewform

I definitely encourage you to submit your different ideas through our intake survey. This helps us see the bigger picture when we're evaluating submissions from all those who are interested in speaking. Our Summit Chair (Celia Hodent) also gives a great recap of last year's talks at this link (in case you wanted to check out previous topics):

SO:
multiple proposals can be submitted

Instead of talking about the history of neural networks, talk about my own history


2018-07-24 22:48:20
going to sleep on these thoughts. I had not expected to give  atlk really, but rather a workshop. There's so much I can talk about regarding my intentions and what Ive learned, the challenge is to drame that as part of my own experience as a game designer, or rather a performance art user interface designer. Put another way, what can someonme in the audience bring away  from the talk? can they learn something, feel something, be inspired?


2018-07-24 22:54:01
working a bit on deepdreamvisionquest. The FX CLass turns out not to be a class at all, but rather a module serving as a namespace for related variables and functions

There's no reason to do this:
FX = postprocess.FX()

because you'll never do this:
FX1 = postprocess.FX()

instead, you'll do this:
rgb = postprocess.FX.median_blur(rgb, **fx['params'])

or this:
from postprocess.FX import median_blur
rgb = median_blur(rgb, **fx['params'])

or even better:
rgb = postprocess.median_blur(rgb, **fx['params'])

alternately:
from postprocess import median_blur
rgb = median_blur(rgb, **fx['params'])


2018-07-24 23:34:45
code is no longer crashing, continuing to work with the former FX class


2018-07-24 23:56:05
new functions in postprocess.py coming online.
came across issue I previously ran into where I need to access & update a variable outside a function, as if it was a global variable. Solved if previously w a decorator? maybe same here? or some kind of helper function to store & toggle the variable?

2018-07-26 21:07:29
On the DeepDreamVisionQuest side of things:
I heard back from Cate at California Academy of Sciences and there is some flexibnility regarding setup, so that show is on! It is such a weight off my shoulders and I'll follow up w the rest of the group tomorrow am.

2018-07-27 16:49:07
OK I think I'm done writing up this proposal. Will copy paste into the form and edit there!

2018-07-27 17:58:41
submitted proposal. Wondering if I should reach out directly to Celia Hodent about DeepFreamVisionQuest install? Why wouldn't I?

2018-07-27 18:23:52
For team at Seeker
- write-up of my work in layman's terms
- high res photos
- video samples
- logo

provide as publicly shared google doc?
provide as dropbox paper?
provide as keynote doc?


2018-07-27 20:33:52
continuing dev work on render fx system


2018-07-29 13:27:09
I am trying to increment the octave_scale value from its current value until it reaches maxvalue then decrement octave_scale until it reaches its min value

Actually what I am trying to do is set a range of values and a number of steps between these values for the octave_scale property to assume each time the function is called

minvalue = 1.0
maxvalue = 2.0
steps = 1
current octave_scale = 1.0

range = [1.0, 1.5, 2.0]

sooo... I could use itertools.cycle to create a cyclical list
that list would have to be rebuilt when the program changed
the range of values would be calculated and stored in the Model object and updated as part of existing  neuralnet.Model.set_program() function

When postprocess.octave_scaler() is called it does something like:
Model.octave_scale = Model.octave_scale_range.next()


2018-07-31 00:16:34
full circle. the way I was parsing program entries was what I wanted in the first place, and did not realize it supported multiple entries of the same effect and also sequential processing - the entries get processed in the order the are listed


2018-07-31 01:17:29
reimplemented octave scaling. I'm going to take a 2nd look at the xform_array function though which had maybe shown some promise, although I never implemented it properly the firt time. Is also possible it could be applied as a stepfx?


2018-07-31 21:18:48
It could be done with a generator too I think, and this would eliminate the need for setup_octave_scaler in  the Model object


2018-07-31 23:58:47
got distracted playing w the compositor. updta ebehavior - but seem to have come across a nice transition into the hallucination from the webcam view - it dissolves in. nice


2018-08-01 00:46:57
compositing is working beutifully with transition in to dream and out of dream when motion detected. It's amazing how much less motion detection logic I've been able to redesign and abstract from what I've had previously.


2018-08-02 01:20:13

added support for Miles Deep neural net


2018-08-02 22:48:47
picking up where I left off addinng stepfx support


2018-08-02 23:26:53
added median blur back to the step fx processor. Previously I'd been using an interval to enable or disable the processing for a given frame using modulus of  int value of current time and the specified interval. To think about in terms of a synthesizer - that's a square wave. But I think it would be cool to include the possibility of a sine wave as well, or a sequence of values.


2018-08-04 11:46:22
I came across some code for using a generator to create oscillators with a cool variety of physical and potentially nonlinear properties. Tested out some code sample, and its just what i needed!


2018-08-04 19:32:43
studying that oscillator code


2018-08-04 20:23:21
came across another example of a sine oscillator at a specific frequency
quite interestibng in that it allows for the addition of  multiple sine waves of different frequencies for additive synthesis


2018-08-05 00:51:55
fantastic! I've created an oscillator that can generate sine waves, square waves and sawtooth waves at an arbitrary cycle length and rate, which can remap its values from the input range to an arbitrary output range. Even better - its a generator object that can be instantiated on demand for any function that needs cyclical return values. Nice work.

next
x add parameter to select wave type: sin, square, sawtooth
- refactor previous octave_scaler function to use this mechanism


2018-08-05 21:17:45
after swimming around for a bit earlier, making some progress at last. I've demonstrated:
- passing a function without arguments as a stepfx parameter
- passing an iterable as a step fx function

these are defined in the program definition itself, along with everything else. I'm running inmto a structural issue though. Apparently if I import postporcess in the data module, which is where the program settings are stored, I get a circular reference and an error message I dont know how to fix

moving the settings to their own module seems like it might avoid that and let me import functionality without circularity I think


2018-08-05 22:59:14
getting closer to the solution


2018-08-05 23:14:25
Its spitting out nunmbers in a square wave pattern, just not the right ones for the square wave I expected. maybe a rounding issue? maybe something is wrong with the remapping function

yeah - the remapping function doesn't work as expected. I may need to calculate the output values differently? Not obvious why remap isnt working though, naybe it never worked the way I thought?

NEXT
- debug the remap function

2018-08-06 00:11:52

ok, I've fixed the math, cleaning that up for compactness

NEXT
cleanup up remap math for compactness


2018-08-06 08:41:09
not sure where I was going wrong w the remap function last night, but I've got it working properlyxxxxx.


2018-08-06 09:21:14
great - looks like I've implemented an oscillator for median_blur. The square wave function doesn't seem to output an exact square wave and I needed to filter the incoming values to do so. Checking up to see if there's something I missed with that function


2018-08-06 09:36:13
its working in the renderer, but need to account for a couple more use cases:
-  what if I want a constant value?
-  what if I want to cycle between 2 non zero values (currently the assunmption is that  the low value is 0, and no blurring takes place)
-  what if I want to change the phase of the wave?



2018-08-06 23:43:26
ah, great _ found a simple formular to generate waves between any 2 values that I think will serve my  needs better - at least in regard to square waves. Implementing that in the code now


2018-08-07 00:34:29
its working. its generating different kinds of imagery than I've seen before - the additional variation by the cyclical motion has some great possibilities. Going to see if I can  also implement he duty cycle function for scipy square waves


2018-08-07 01:26:35
so good, a whole new dimension to the hallucinations - and that's the combined dynamics of octave scale and median blur working together. i've never seen anything that looks like this before.



2018-08-07 21:56:35
working on implementing my previous solution for octave_scaler as an oscillator object solution. Everything is setup right, doing so was trivial actually once I mapped out the flow of operations. Now I need to modify the oscillator functions for sin & sawtooth waves to output mavules between a min and max value as I did for the sqaure wave type


2018-08-07 23:00:50
testing updated octave scaler - its working!!! seeing it make pictures I've never seen before. No one has.


2018-08-07 23:12:11
looking at bilateral filter
it has 3 values that can be manipulated independently

2018-08-08 00:19:25
implemented  oscilators for bilateral filter. validated setup. tweaking and adjusting for gfx


2018-08-08 01:24:29
implemented bilateral blur

next
x nd_gaussian blur
x step mixer
- duration cutoff
- xform array

then
move Viewport class into its own module
move Composer class into its own module


2018-08-08 20:59:36
implemented nd_gaussian


2018-08-08 21:52:50
brought cambrian implosion settings back online for testing


2018-08-08 22:28:34
implemented step mixer. the effect is subtle, not sure how much value it has


2018-08-08 22:30:20
maybe less subtle than I thought, for higher iterations and detail causes the dreamed imagery to "pulse"


2018-08-09 21:32:39
reviewing numpy again


2018-08-09 23:46:33
i am back in the camera-setup.py project. The grayscale image processing I was experimenting there can adapt to the luminance variations of video feedback pretty well and control the exposure from blowing out...

What I'm trying to do here though is construct a new test program for  storing buffered image sequences



2018-08-10 23:31:57
My test file is copying images into a buffer of fixed size. Thinking about how to get readout from the buffer independent of camera sequence. That is, while the camera is writing frame-n (0-99), the readout is showing frame-i


2018-08-11 00:00:19
not sure why I cant't playback this data


2018-08-11 10:03:47
verified playback from buffer - its interesting... showing time-delayed images - offset by length of buffer, which is set at 100 frames


2018-08-11 13:18:25
building out a camera and buffering system in this "sketch". Its exciting to see this time delay side by side with realtime input. Can't take my eyes off it actually, as if I can't wait to see what I do next while remembering having done it - yeah... its hide and seek


2018-08-12 23:13:42
after much experimentation, rebuilding my buffer code as a buffer class. I think I'm close to getting the results I want - or at least to see what I think I want looks like. The idea is to accumulate fully rendered deepdream frames (or some other criteria) and play them back in a loop, with new frames entering the loop when they meet said criteria


2018-08-13 08:27:06
will return to this shortly. Left it in a position where the new Buffer class is updating properly, and returning wjat was sent to it. Just need to figure out how to playback a view of the buffer from frame 0 to n



2018-08-13 21:10:32
left off working on sequenceing the frame buffer I created. Not working as expected, yet not obvious why - so looking closer


2018-08-14 00:33:51
the the process is working now, although needs a bit more refinement.


2018-08-14 13:01:45
I'm going to call the beta implementation complete, as its doing what I want for deep dream vision quest. next I'm going to set up a test where frames are sampled at random intervals and see how that looks
then I'm going to examine composuiting the two images together for trailing effects


2018-08-15 23:10:17
updated business card w better statement of objectives
picking back up w the Frame Buffer dev. I've got an idea on how to calculate average of multiple frames in a range for trail-y effects


2018-08-16 22:21:26
integrating  my frame buffer changes and creation into the deepdreamvisionquest code

should the Buffer class be in the same package as the Composer class? what are the similarities?

framebuffer = history.Buffer(ramp,buffer_size=BUFFERSIZE,width=1280,height=720 )

framebuffer = data.Buffer(ramp,buffer_size=BUFFERSIZE,width=1280,height=720 )


2018-08-16 23:56:52
cleaning up the Buffer class and making sure test cases are demonstrable before inclusion in main codebase


2018-08-18 12:39:57
the cycling feature isnt working the way I thought. Inspecting that further


2018-08-18 17:42:19

Ok that's basically working now. Could still use soem work when it comes to the  playback rate for the buffered frames. But still..


2018-08-19 15:12:19
taking another look at the cycling feature. I just have a funny feeling about how its implemented before moving it into the main codebase


2018-08-19 16:29:00
this refactor of the cycling feature is vastly improved. also less code


2018-08-19 18:15:57
completed a bit of refinement to slowshutter
now prepping for integration



2018-08-19 18:29:42
added buffer class to postprocess.py


2018-08-20 00:14:57
not really pleased with the cycling effect - There may be subtle variations I haven't thought of, but I can't say the implementatin experiments I've done improve the output, and in fact they distance me from what was already working pretty well.

I think my time is better spent righ
- refining the compositing behavior
- examining slow shutter speed

Frustrating, having spent so much time on this - and I still feel its a good idea, but the capture and playback is more nuanced than I'd imagined.


2018-08-22 01:26:45
last minute edits have me busy, but worth the effort. I'm turning the featuremap increment feature into a cycle that is specified by a "featuremap" performance setting. Toke a number of notes to approach the task surgically and efficiently. So far so good


2018-08-22 11:00:51
a stepfx like slowshutter has only one range of values that gets reset every time set_program() is called

step fx like feature map needs an oscillator defined every time the layer changes


2018-08-22 14:08:07
putting together mailing list signup form for the website.

HEADING
pitch (what are you offering)
CTA (join mailing list)

Get updates and special offers from  DeepDreamVisionQuest
Recieve more information about my exhibitions and workshops
Get the latest news about my work, upcoming exhibitions and workshops

Don't Forget to breathe.
Stay dreamy with a recap
with a ____

Zero intention of using your email for spam by the way - because grsoss.

Sign up for my mailing list for upcoming  woprkshops, exhibitions and speaking engagements.

Sign up for my mailing list
Join my mailing list for details of upcoming workshops and exhibitions. I don't have the time to spam you, but will send artwork from time to time



2018-08-22 15:47:15
updated landing page of website - removed extraneous info and inserted a newletter signup form on this page

need to update events page w this weeks events

2018-08-22 16:07:46
added mailing list signup and connected it to a mailchimp account. not sure how often mail chimp updates. Ive added 2 user

ok - testinmg user flow. soem room for improvement w better messaging

2018-08-22 18:19:22
Let’s make minds together. Check your email to confirm your subscription.

2018-08-22 18:39:54
completed setting up and testing Mailing List acquisition form


2018-08-22 22:36:59
everything is set up on the CPU and AV carts for rehearsal


2018-08-23 00:07:31
positioned camera on dashboard mount directly onscreen, and spent time adjusting position
adjusted zoom and pan settings in the control panel
adjusted position of a single light  to be useful but not obtrusive. The new lights that arrived are brighter than previous set. Berfore loadout I will make sure to document ttyhe positions of the gear, placement of camera and video control panel settings


2018-08-24 18:31:22
great show at California Academy of Sciences last night. I'm doing another tomorrow with NOIZE FLOOR. Taking a look at my codebase and seeing what I have time to tweak and update in response to observations of last night's show
- more program settings
- more variation
- ability to cycle thru layers as well as features`

specifically - I'm not so sure if the featuremap, uh.. feature is working the way I think it is



2018-08-25 02:10:52
['data', 'conv_1', 'pool1', 'pool1_pool1_0_split_0', 'pool1_pool1_0_split_1', 'conv_stage0_block0_proj_shortcut', 'conv_stage0_block0_branch2a', 'conv_stage0_block0_branch2b', 'conv_stage0_block0_branch2c', 'eltwise_stage0_block0', 'eltwise_stage0_block0_relu_stage0_block0_0_split_0', 'eltwise_stage0_block0_relu_stage0_block0_0_split_1', 'conv_stage0_block1_branch2a', 'conv_stage0_block1_branch2b', 'conv_stage0_block1_branch2c', 'eltwise_stage0_block1', 'eltwise_stage0_block1_relu_stage0_block1_0_split_0', 'eltwise_stage0_block1_relu_stage0_block1_0_split_1', 'conv_stage0_block2_branch2a', 'conv_stage0_block2_branch2b', 'conv_stage0_block2_branch2c', 'eltwise_stage0_block2', 'eltwise_stage0_block2_relu_stage0_block2_0_split_0', 'eltwise_stage0_block2_relu_stage0_block2_0_split_1', 'conv_stage1_block0_proj_shortcut', 'conv_stage1_block0_branch2a', 'conv_stage1_block0_branch2b', 'conv_stage1_block0_branch2c', 'eltwise_stage1_block0', 'eltwise_stage1_block0_relu_stage1_block0_0_split_0', 'eltwise_stage1_block0_relu_stage1_block0_0_split_1', 'conv_stage1_block1_branch2a', 'conv_stage1_block1_branch2b', 'conv_stage1_block1_branch2c', 'eltwise_stage1_block1', 'eltwise_stage1_block1_relu_stage1_block1_0_split_0', 'eltwise_stage1_block1_relu_stage1_block1_0_split_1', 'conv_stage1_block2_branch2a', 'conv_stage1_block2_branch2b', 'conv_stage1_block2_branch2c', 'eltwise_stage1_block2', 'eltwise_stage1_block2_relu_stage1_block2_0_split_0', 'eltwise_stage1_block2_relu_stage1_block2_0_split_1', 'conv_stage1_block3_branch2a', 'conv_stage1_block3_branch2b', 'conv_stage1_block3_branch2c', 'eltwise_stage1_block3', 'eltwise_stage1_block3_relu_stage1_block3_0_split_0', 'eltwise_stage1_block3_relu_stage1_block3_0_split_1', 'conv_stage2_block0_proj_shortcut', 'conv_stage2_block0_branch2a', 'conv_stage2_block0_branch2b', 'conv_stage2_block0_branch2c', 'eltwise_stage2_block0', 'eltwise_stage2_block0_relu_stage2_block0_0_split_0', 'eltwise_stage2_block0_relu_stage2_block0_0_split_1', 'conv_stage2_block1_branch2a', 'conv_stage2_block1_branch2b', 'conv_stage2_block1_branch2c', 'eltwise_stage2_block1', 'eltwise_stage2_block1_relu_stage2_block1_0_split_0', 'eltwise_stage2_block1_relu_stage2_block1_0_split_1', 'conv_stage2_block2_branch2a', 'conv_stage2_block2_branch2b', 'conv_stage2_block2_branch2c', 'eltwise_stage2_block2', 'eltwise_stage2_block2_relu_stage2_block2_0_split_0', 'eltwise_stage2_block2_relu_stage2_block2_0_split_1', 'conv_stage2_block3_branch2a', 'conv_stage2_block3_branch2b', 'conv_stage2_block3_branch2c', 'eltwise_stage2_block3', 'eltwise_stage2_block3_relu_stage2_block3_0_split_0', 'eltwise_stage2_block3_relu_stage2_block3_0_split_1', 'conv_stage2_block4_branch2a', 'conv_stage2_block4_branch2b', 'conv_stage2_block4_branch2c', 'eltwise_stage2_block4', 'eltwise_stage2_block4_relu_stage2_block4_0_split_0', 'eltwise_stage2_block4_relu_stage2_block4_0_split_1', 'conv_stage2_block5_branch2a', 'conv_stage2_block5_branch2b', 'conv_stage2_block5_branch2c', 'eltwise_stage2_block5', 'eltwise_stage2_block5_relu_stage2_block5_0_split_0', 'eltwise_stage2_block5_relu_stage2_block5_0_split_1', 'conv_stage3_block0_proj_shortcut', 'conv_stage3_block0_branch2a', 'conv_stage3_block0_branch2b', 'conv_stage3_block0_branch2c', 'eltwise_stage3_block0', 'eltwise_stage3_block0_relu_stage3_block0_0_split_0', 'eltwise_stage3_block0_relu_stage3_block0_0_split_1', 'conv_stage3_block1_branch2a', 'conv_stage3_block1_branch2b', 'conv_stage3_block1_branch2c', 'eltwise_stage3_block1', 'eltwise_stage3_block1_relu_stage3_block1_0_split_0', 'eltwise_stage3_block1_relu_stage3_block1_0_split_1', 'conv_stage3_block2_branch2a', 'conv_stage3_block2_branch2b', 'conv_stage3_block2_branch2c', 'eltwise_stage3_block2', 'pool', 'fc6', 'prob']



2018-08-25 16:58:41
Here at the Red Victorian setting up. Very clean and orderly loadout and install.hyperrational

2018-08-27 22:33:28
Refining mailing list opt-in form and UX

2018-08-28 00:28:43
updated website for cleaner more efficient display. Removed chaff. Placed newsletter opt-in in the sidebar. Will need to show/hide this control elsewhere for mobile viewports. Removed (empty) old mailing list and created a new one on mailchimp with the mor egeneral-purpose label "Science Fiction Cave Painting"


2018-08-30 01:31:59
experimenting with some alternate rendering methods. My thinking is that I am switching to a monochrome presentation to get the benefit of the equalization routines I've used in the bufferseq.py script. Also the thinking is that these images will be color mapped  at some later date, with color being an interactable param

2018-08-30 10:10:04
had a great time last night pointing the camera at the TV playing new wave/gothic videos. Pretty convincing demo of dreamy responsiveness. Wish I'd come across this solution last week, as I think it goes a long way for providing a connectedness w the imagery

people to add to mailing list
Noize Floor crew
CODAME crew
ArtX crew
ZOS crew
Spoto
Brent Ashe

2018-08-30 11:39:46
modified wording of newletter opt-in CTA


2018-09-19 09:25:13
I have been focused on experiments and optimizations to deepdreamvisionquest Composer.update() which handles compositing of video "streams"
I'm researching and learning about multiprocessing as a way to decouple the update() function from the expense of the rendering calculation. In practice this causes responsiveness to correlate with the octave currently being halucinated about. In worst cases, each octave may compute 2x slower than the previous one, which makes continuous motion and responsiveness less than what it might be.

My initial hackish research in centralizing all displayable outputs to  data.playback and updating that display with the camera thread (the hackish part) was promising and smooth and certainly inspires to push further. Buftr it is slow going. I took the day off today so I could really think about this and deep dive with my full attention. Here goes.

https://bitbucket.org/dani_thomas/multiprocenv


2018-09-21 01:19:51
Just completed entering and studying Adriran Rosebrook's multicamera motion detector. The multiple camera stuff may or  may not be directly relevant to me, but is a good working example of generalizing inputs from multiple sources

Before moving on, I want to see how I can generalize this further to process 1-n cameras. The way its currently setup assumes minimum of 2.

Not my immediate subject of interest, but some interesting concepts are implemented here. The position and area of largest detected motion is isolated from any other motion, including the background. Its fast, uses multithreaded videocapture class and provides significantly simplified method for detecting  motion (simple as in less code that does more)

- generalize camera usage to support 1-n camers
- what happens when motion is detected? how to quantify it?
	- how to check number of frames w consistent motion to filter out spurious motions


2018-09-23 13:24:53
studied the new motion detector a bit more closely to yield precise results in localized areas.

returning to deepdreamvisionquest
looking at adding Adrian Rosebrook imutils class


2018-09-23 18:42:22
awesome, I've externalized the Composer object into a seperate package


2018-09-23 20:47:00
Working on the final broad stroke for externalized packaged software functions - the Viewport object


2018-09-23 22:43:09
implementing a general purpose "component registry" to store common object references between modules. Working out this idea with the keyboard listener, but am going to extend this to other places where I felt funny about passing references directly to classes and functions


2018-09-23 23:01:50
created a special case version of component registry by writing function atributes to  the data module


2018-09-23 23:50:26
its all working!


2018-09-25 07:54:38
Having encapsulated all functionality into modules, what's next?
Feeling a bit like I'm floundering about with small tweaks here and there and not really going further.
Where did I want to be?
I want to incorporate the framebuffering work I completed with the performance
1. the motion trails that are created by slowshutter - how can I dream about the trails, rather than the endpoint , when motion is detected?
2. the frame buffer  wants to show previously rendered frames in a loop
3. the frame buffer wants to


2018-09-29 21:06:55
initial implementation of multithreaded compositor. testing now


2018-09-30 16:06:25
tracing down an error condition upon exit where the program keeps running

2147483647
574671192


2018-09-30 17:57:26
http://blog.acipo.com/python-multi-threading/


2018-09-30 18:51:34
interesting - researched my way into a good solution for system shutdown, yet feels a bit awkward. There's a function called thread.interrupt_main() that can be called to send a keyboard interrupt to the main thread from a subthread. Same as pressing ctrl-c. Because each of the subthreads are "daemon" threads (yeah) they terminate when the main thread terminates. presumably if they were not they would continue to run?

It's a bit weird though becuase the shutdown function is in the viewport module, when really I'd expect to find it in the main (rem.py) module itself


2018-10-09 00:20:52
some initial experiments w optical flow demo code

next
- color transfer between 2 images (to map palette of 1 image to another)
- optical flow


2018-10-13 13:24:32
taking a closer look at optical flow implementation, especially with respect to the framebuffering features I've added, although not yet fully exploited. I've shown in previous experiments though, how to maintain an image queue - just a collection of images captured asynchrously and playing back in realtime.

The idea is to compute optical flow from these images and use that information to cause the images to blend smoothly into one another. The theory is that this effect should look similar to some of the after effects work I've previously done on sequences where the framerate is altered and the "pixel blending" algorithm is used, which is also based on optical flow.

The reason its important to process this way:
1. visual effect is pretty great
2. earlier experiments w asynchronous buffering and sequential playback of deepdream content wasn't really tghought through fully - but still - it was very noisey - very jumpy. Not uninteresting, but not the smoothness I've been working to achieve.

2018-10-15 21:07:37

CONVERT MOV FILE FROM IPHONE TO 1280X720 JPG SEQUENCE AT HIGH QUALITY
ffmpeg -i IMG_9807.MOV -crf 0 -vf scale=1280:-1 -q:v 1 iphone-2_%04d.jpg


2018-10-17 08:55:47
ongoing experiments w optical flow are yielding some interesting results. The technique is much more dramatic with moving camera however.

2018-10-23 09:17:25
writing up promo for gallery talk

THE GEOLOGICAL GAZE


All around us and inside of us are networks that represent the world as a kind of dream; a geolo
Behind this screen is a neural network that hallucinates on the world it sees through a live camera, reconstructing input with visions from its own memory. Movement activates each new dream cycle, and the hallucination intensifies the longer its field of vision is motionless. Standing in front of it, you will see creatures emerge from suddenly alien landscapes, only to fade the second you move.

Represent information with geology
geology represents informa

To paraphrase Alan Watts, the machinery of the word is the mythic view of geological consciousness. The myth teaches us not to feel identical with the universe. As an experience designer, I wanted to []

Artist Bio
Gary Boodhoo combines videogames with machine learning to create interactive science fiction. He invents or discovers exotic places between artificial and real worlds.

DeepDreamVisionQuest is an interactive video synthesizer that creates multiplayer hallucinations. Live cameras reveal the world to a neural network which progressively reinterprests what it sees.

The surprising though perhaps obvious truth behind artificial intelligence is that Mind emerges from the environment.


In 2015 Alexander Mordvintsev released the first "Deep Dream" images to an amazed internet. These were instantly recognizable as photographs of a psychedelic experience, both alien and familar at once.

Gary Boodhoo creates video installations that show the world to a learning machine through a live camera. Deep Dream Vision Quest is a neural image synthesizer that creates multiplayer hallucinations. In this talk, Boodhoo describes how he uses stagecraft, creative coding, and game design to make pictures of Minds.

For more information, check out Gary's website: https://www.deepdreamvisionquest.com/

Come through if you're interested and share widely this to those who think about the self in an age of perceptive machines!


2018-10-23 10:10:36
somewhat related to the stament I'm writing. What is it exactly that I'm writing? Anyway - all my live exhibition work on deepdreamvisionquest.com is from 2017. There are 4 shows in 2018 that need to be added here

2018-10-23 10:19:39
I'm overthinking this writing task. Why?
Just use something short that you've already written. Doesn't need to be a full description of anything just needs to provide an attractive proposition.

What do people get out of my talk?
see yourself differently
learn where the images come from

DeepDreamVisionQuest, A Magic Mirror
The computer was wrong but together we arrived at poetry. My video installations show an unpredictable world to a gregarious learning machine through a live camera. Together, we're making pictures of minds. In this live demo I discuss how and why I built DeepDreamVisionQuest, a neural image synthesizer that creates multiplayer hallucinations.


2018-11-11 20:28:09
preparing for Gallery Talk on Wednesday. Not liking how the compositor is working, and looking into smoothing it out further. Was it always like this? Its definitely bothering me to see it. There's no problem switching from dreamed output to webcam output, but when motion stops we see dreams captured from the old static position, so the display appears to jump from new position to old position. How to solve for that time delay?


2018-11-11 21:30:34
I've hacked in a delay from fom the time of motion detection, and that solves the "flashing" out of sync issue I was previously seeing, but at the cost of responsiveness. Thinking I'm headed in the right direction though, especiallyu for a quick cleanup


2018-11-11 22:32:11
taking a look at the pause control. I'm a bit surprised it still works after all the changes this code has been through, but I'm having a hard time knowing when it has been engaged and disengaged. How can I know when it is engaged?
-  how about writing a message to the screen, showing it for a moment, then making it go away?


2018-11-12 00:23:17
great worksession. pretty pleased with the output I'm getting at 1080p for the first time. Still some functionality to add though - notably, exporting the frame buffer to a JPG file.

the featuremap updating during movement is a good idea, but need a way to freeze the current feature map and prevent itereation until unfrozen. [rev/next controls work as before]

Then I'll need to construct some programs for the demo

Need to review the HTML presentation I did at STanford. Is this viable? How did I make it?``


2018-11-12 14:27:02
I reviewed my Stanford presentation, it has some ghood material but gets too bogged down in details about inner working of neural networks. Need to cut that down overall. Not sure how I authored this in the first place. It looks like I exported HTML from Keynote?


2018-11-12 15:33:01
oh dear - something I did last night is causong the input not to feed back into itself correctly I think. Not seeing any effect on theinceptionxform postprocess


2018-11-12 15:36:29

ah good - fixed it. holy crap the smoothness has never been better. But also seeing the magical effect of the machical numbers in the update hack I made yesterday. They're different at 480p than 1080p


2018-11-12 16:39:32
close this dev session by
- complete googlenet enumeration
- add auto-feature function to performance setting definitions
	+ this should be a flag specified in the main block

program.append({
    'name': 'demo',
    'iterations': 2,
    'step_size': 2.4,
    'octaves': 4,
    'octave_cutoff': 4,
    'octave_scale': 1.8,
    'iteration_mult': 0.0,
    'step_mult': 0.0,
    'model': 'vgg19',
    'layers': data.layers_vgg19,
    'cyclefx': [
        {
            'name': 'inception_xform',
            'params': {'scale': 0.01}
        },
    ],
    'stepfx': [],
    'autofeature': True
})

This function causes the featuremap index to update upon motion detection

self.current_layer=0
set_endlayer[self.current_layer] # index

def set_endlayer(index):
self.end = self.layers[index]['name']


2018-11-12 23:20:32
finished functional edits to the pasuing function. had overcomplicated it and turned out it was working as expected when paused as a consequence of the design. Taking a look at file export now


2018-11-13 00:17:11
I have the export picture code working now, but not sure if I'm sending the right image. Using Composer.dreambuffer, but  should use whatever the viewport is refreshing


2018-11-13 00:27:09
refined the export picture code further. would it be possible or reasonable to guarantee output of a pic only when iteration is complete?


2018-11-13 02:48:53
pause mode isnt working the way I expected. It seems as though if a subject is already in motion, the condityion never triggers although the flag gets set


2018-11-13 09:25:18
fixed pause mode to work the way I expected. Testing that now


2018-11-13 09:47:48

interesting - the iteration multiplier I've been using is much more aggressive than I'd expected since it gets recalculated every iteration rather than every octave!


2018-11-13 10:08:18
I think I'm good with locking the code now. Any further iteration will be on the performance settings


2018-11-13 14:24:54
the only (minor) issue I'm seeing is that incrementing the featuremap while paused, refreshes the webcam w current image, which remains paused, instead of using the originally paused frmae.



2018-11-14 14:08:03
finalizing performance settings for tonights talk

From Pixels to Representations
- all layers: Googlenet
- all layers: Places 365

Stylized Motion


2018-11-14 15:43:50
ok. ready to present. checking map and starting loadout

2019-01-03 00:12:43
Invited to a panel discussion for private IfSoWhat event, and will be installing DeepDreamVisionQuest on location. I'm preparing my promo for official email

x picture
- name/title
- bio


Science Fiction Cave Painting, Gary Boodhoo
Gary Boodhoo is an installation designer and game developer who turns neural networks into immersive experiences. His creative practice uncovers emotional connections with smart objects in social spaces.

2019-01-03 17:09:44
working on syntheticaf.com dev environment

My goal is to:
TRANSFER A WORDPRESS SITE FROM LOCAL HOST TO WEB HOST
- create a throwaway demo site locally
- add content to demo site
- commit changes to git local
- push local repo to remote
- transfer remote repo to the web server using command line
- transfer the wordpress database from local to webserver
- success

I'm having with:
identifying the location of the webhost
identifying valid user for webhost read/write operations
setting up SSH using PuTTy client

Solutions:
x can you setup FTP access to Bluehost account?


notes
- I am able to navigate the filesystem using bluehost's web-based File Manager tool. My root directory as user synthex9 is /home3/synthex9
- is there an account from which I can view the /home3 directory?
- how do I switch users?

interesting. I had to re-login to the cpanel. i entered
username: synthex9
password: Four096Xx++

I am also able to do so when logging into bluehost account

unable to login w username synthex9_logs

synthex9 is listed as the only "webdisk" user
there are numerous FTP users listed

I updated the dev account previously created to use the webdrive. My expectation is that I should be able to access the filestystem as before, but from a different home directory

There is the main account (administrator) password
- this user is named synthex9
- You have complete, unrestricted access to manage your hosting account when you log in with the main account password. If you're the only one who logs in then this may be the only password you'll ever need for your hosting account.

There is the hosting password for an authorized user
-  Allows access to the hosting files and utilities needed to manage and publish your website

cPanel’s User Manager tool allows us to quickly create additional user accounts for e-mail, FTP or Webdisk services.


webdisk.cpanel-box5513.bluehost.com

2019-01-04 00:15:37
I'm getting a DNS lookup issue when I try to login w FTP. Suspecting this is related to the weirdness I previoulsly went through to map syntheticaf.com email to a gsuite account

2019-01-04 00:24:28
I'm spinning my wheels on this need to contact technical support


Please use the following FTP details:
Server/Host:162.241.217.216
Username:synthex9
Password: your cpanel password
port :21

2019-01-04 09:31:59
successfully logged in to FTP with synthex9 account
verified read/write access to filesystem

successfully logged in to SFTP with synthex9 account
verified read/write access to filesystem

2019-01-04 09:43:37
building out test site locally


2019-01-05 22:47:54
I've constructed a local site
x need to establish ssh connection to remote server in terminal
x am I able to connect via ssh thru PuTTY?
	+ sort of. contacting tech support for further help
I'm able to establish ssh connection to bluehost now

In the remote server, we will need to
x create a database
	x create a new database manually
- wp-config file
	+  make a copy of your local wp-config file
	+  change the database details and any other constants that should be changed for live use, such as WP_DEBUG
	+  upload it one level above the WordPress root directory with an FTP client.
- install directory, with nothing but an empty git repository.

2019-01-06 12:05:53
after completing the wordpress dev environment, I'm going to copy recent work from my phone into sciencefictionthriller, categorize, process and export new gfx for gallery on deepdreamvisionquest.com

I am wondering how the gallery setup I have can be made more engaging/stickier/or provide a broader (more exclusive?) goal. There's also an opportunity here to link this work back to the workshop

I say nothing on the website about my workshops. Maybe this can be expressed as a blog post? Pretty sure i've come across photographs from the events at ART+TECH and IFSOWHAT

2019-01-06 12:15:35
/** MySQL database username */
define('DB_USER', 'synthex9_WPKHR');

/** MySQL database password */
define('DB_PASSWORD', '9Y3TPeTngsuj9Kb6K');

/** MySQL hostname */
define('DB_HOST', 'localhost');

Creating a new database on bluehost with
username:
synthex9_DEV

password:
4096xx+

2019-01-06 13:40:06
in response to SHo's mention of best ways to present additional work, I just realized - the work preents best on a display, or projected (why not both?)
One lounge aarea in particular caught my attention when I visited. There was a large wall mounted display in that space. Is there another space where inmagfery can be projected?

2019-01-06 13:49:56
Error establishing a database connection from the filesystem created when I clones the github repo to bluehost. I'm not sure if this is a conseuence of the filesystem I created?
- can a wp site only be hosted from the root level public_html location?

Alternately, something coukld have gone wrong w the database I created? Altrhough not seeing how. The error states "Error establishing a database connection"

2019-01-06 14:04:00
or.. it could be that I'd entered the wrong username in the wp-config.php file (!) lol?

When I navigate to:
https://syntheticaf.com/live/www.example-1.dev.cc/wp-config.php
I am directed to the wordpress install script at
https://syntheticaf.com/live/www.example-1.dev.cc/wp-admin/install.php

2019-01-06 21:43:55
edited my bio to include a list of accomplishments and makes mention of my workshop series. Will no doubt returbn for additional editorial on this.

I make synthetic art using machine learning technologies for environmental and editorial applications. I also speak about AI for artists and run hands-on workshops to discover creative uses for this technology.

2019-01-07 01:09:04
completed and staged layout refinements to deepdreamvisionquest.com
next:
remove about page
add blog page

2019-01-07 13:18:30
copywriting
I make synthetic art using machine learning for environmental and editorial applications. I also speak about AI for artists and run workshops to discover creative uses for this technology.

2019-01-07 14:18:02
DeepDreamVisionQuest is a neural image synthesizer that creates interactive multiplayer hallucinations. Live video transforms into patterns, creatures and sometimes, places. This video installation engages participants while examining the socialization of smart objects in public spaces.

2019-01-07 14:32:27
adding If So What event to calendar
- need to add Visual Strategies for Artistic Style Transfer to calendar

2019-01-07 15:11:06
created first draft event post for IfSoWhat event
- assembline post for February workshop

2019-01-07 15:26:42
assembled various linked in event announcement posts to set a baseline

2019-01-07 16:28:29
finalizing some edits on business card design

2019-01-07 18:03:44
event post for ImageGarden2 is looking good. Sincle the audience is closed the intent is to publicise myself with bonafides on linkedin, ig and available on the site for ifsowhat traffic

If So, What? invites you to a private evening, diving into the latest trends in AI at the intersection of art and society.

2019-01-08 00:30:46
fine tuned the 2 events I added
fine tuned layout of eventy page
using Squarespace CMS for events now instead of constructing my own list

`yui_3_17_2_1_1546936655219_1068
//*[@id="yui_3_17_2_1_1546936655219_1068"]`5219_1068"]

2019-01-08 13:00:43
rebuilding the "Installations" feature

2019-01-08 18:25:17
I've fleshed out the content on the landing page and refined the layout overall including the site menu. I'm building out a new section titled "Installations" to show highlighted material from various installs

2019-01-09 11:00:49
curating site assets

2019-01-09 12:23:37
there's no room or time to create a Worskhop feature for this, but on the landing page it would turn the feature blocks into a 2x2 layout"
Installations	Visuals
Instagram		Workshops

2019-01-09 20:46:19
completed Installations page. Will probably try to remove some images from this later, or add video from aquarium

2019-01-09 20:47:08
switching to business card design as the order for these must go out tonight

2019-01-10 00:55:02
finished rebuilding Visual Section. Will want to add additional work here. My optical flow experiments and feedback experiments come to mind.

2019-01-10 18:34:53
taking a look at the site blog section and will work on that ubntil dfinner, then the return to deepdreamvisionquest


2019-01-11 17:37:53
rem.py is up and running, and noticing something a bit odd. Maybe it has always b een like this? but the portrait image I'm seeing appears vertially stretched


2019-01-12 00:25:20
adjusted data.viewsize to correct aspect ratio of displayed image for 480p


2019-01-12 10:24:05
when  I left off last night, I had the idea of storing data.webcam.get() in a data.buffer after renerer.wakeup_requested() is called


2019-01-12 11:19:51
I did so, and it doesnt look any different at first glance. The glitchy behavior on certain frame transitions is bothering me. Its the one part that breaks the otherwise seamless flow. But why does it happen?


2019-01-12 14:42:52
the modifications I made are great - significant improvements and visual interest


2019-01-12 18:13:03
to make further progress I need to verify my mental model of what's happening

P1 are the oscillaror values for various fx returning the values I expect at the intervals/frequencies  I expect?
	x update_feature
	- median_blur

x is it possible for the renderer to signal when it has received (and rendered an iteration) of the camera img after wakeup?

P2 create a utility monitor window that I can pass buffers to during composer.update() so I can see what's going on inside


2019-01-12 22:23:14
I've implemented constraints and signaling such that the glitchy compositing doesn't happen any more (?!) Initial tests for a worst case sitiation are looking good. This replaces the hardcoded delay I'd placed in the signal path, which attempted to wait for the renderer to catch up. continuing to test


2019-01-13 13:44:47
I think this is about as far as i can take the compositing routine now. Cleaning that up


2019-01-13 13:55:41
created a new branch "quality" to focus on render quality, color and contrast


2019-01-13 19:35:29
BW processing
widetime (?) what is this used for?
framebuffer looping
fix bug w HUD becoming part of hallucination


2019-01-14 09:53:51
doing some quick refinement to website

2019-01-14 10:32:52
I’m speaking at a mansion on a panel with Daniel Bay, Lead Engineer Amazon Echo / Hal Hickel, animation director at ILM about the social impact of artificial intelligence. Also showing interactive artwork for this private VIP event held at Roam SF, January 17 2019


2019-01-14 10:53:46
business cards are in, but I think the previous version was more on point. When I get a chance I'm going to revert back to that

2019-01-14 10:57:13
There's time to redo the business cards for next day delivery. doing so

2019-01-14 11:12:18
updated business card layout

2019-01-14 11:34:39
re-ordered business cards arriving 1/16 1030


2019-01-14 14:51:29
Provide work samples to Maya Ackerman later this afternoox


2019-01-14 14:56:18
basic implementation of cyclical playback working. needs more love though. Interesting possibilities ahead


2019-01-14 21:49:34
visited the roam space to examine the idea of secondary video. no obvious good space for projection except downstairs. Not feeling stringky about video loop on that TV either, as it seems, well. secondary. Time constraints prevent pursuing this idea further and need to focus on the obvious interactive goal


2019-01-14 21:51:06
working out details of camera place,ment. As much as I'd like to mount the camera on a c-stand, I'm wondering if there's even space to do so? I've never been 100% happy w the  camera mounted to the display, but am using same method as recent where the camera is mounted to the screen - experiencing it for myself as I work on the code


2019-01-14 21:52:13
for whatever reason the aspec ratio of captured video is weird. I need to do scome screen captures andf reality check my output. Also need to verify the camera hardware capture sizes. I thought I'd done all of this before. This feels like a new problem, as there's no way I wouldn't have previously noticed. What has changed?

Is it worth checking out some earlier code releases to see if the problem exists there? Best to start w  the utility scripts I'd previous;y written


2019-01-15 11:10:54
spent an extended worksession trying to make the cycle behavior work cleanly. Its interesting but unconstrained and I'm not sure how much further I can take it in the time remaining. code lock is end of day today so I can spend all day working on program settings tomorrow


2019-01-15 11:12:35
taking a closer look at the aspect ratio issue I've been seeing

2019-01-15 13:38:33
peparing some support assets for the slideshow Maya is putting together

2019-01-15 14:02:55
repaired layout to instagram feed on website

2019-01-15 15:01:39
collated and sent image & video samples to Maya. contacted Sho to let her know I'm not going to be showing auxillary video


2019-01-15 15:37:32
reverted back to an older version

if (self.opacity + self.opacity_step < 0.0) or (self.opacity + self.opacity_step > 1.0):
                self.opacity_step = -1.0 * self.opacity_step
            self.opacity += self.opacity_step

seeing the same elongation there however...



2019-01-15 17:39:03
aaand, just "fixed" that bug was a matter of setting capturesize to a landscape "orientation". Wondering how this could be prevented. Mu logic sorta failed me in hunting this down


2019-01-16 00:51:59
compositing and rendering are better than ever, although at the cost of responsiveness. Can probably live with it for now, but exploring some options to fix it

what I need is a flag that is set to true when a motion event completes and is set to false when an update happens ithout a nmotion event


2019-01-16 02:44:36
what a difference this worksession has made - difficult and stressy, but handled really well. The cyclical behavior implented yesterday is so much more coherent now as a result of the rework I did to the compositing update systm. wow


2019-01-16 03:59:41
amazing progress today. congratulations


2019-01-16 12:57:57
x duplicate photobooth720 module as an event specific module
x setup listeners for postprocess.equalization (clipping +/- and gridsize +/-)
P2 setup Framebuffer.cycle as a program setting
P2 setup Framebuffer.widetime as a program setting
P2 rank the existing program settings and identify opportunities there as seperate program settings
P2 revert to earlier builds and identify any interesting programs there
P2 construct and experience new program settings
P3 setup softbox light source to see how it can be integrated
P3 install workstation in display area

TOMORROW
P3 artist summary keynote presentation for projection
P3 disassemble for loadout
P1 Is there a question I can pose to the audience?


2019-01-16 20:54:41
final stretch of development. working towards code lock so I can focus on program settings then physical setup.


2019-01-16 21:14:54
looks like I already implemented an autofeature toggle in the listener

2019-01-16 23:48:30
I've decided to keep the equalization as a global feature for visual consistency this time rather than implementing it as a performance setting

x setup Framebuffer.cycle as a program setting
x setup Framebuffer.widetime as a program setting
P2 rank the existing program settings and identify opportunities there as seperate program settings
P2 revert to earlier builds and identify any interesting programs there
P2 construct and experience new program settings
x setup softbox light source to see how it can be integrated
P3 install workstation in display area

TOMORROW
P3 artist summary keynote presentation for projection
P3 disassemble for loadout
P1 Is there a question I can pose to the audience?


2019-01-17 01:27:26
P2 construct and experience new program settings
x rank the existing program settings and identify opportunities there as seperate program settings
x revert to earlier builds and identify any interesting programs there
x setup softbox light source to see how it can be integrated

TOMORROW
P3 artist summary keynote presentation for projection
P3 disassemble for loadout
P1 Is there a question I can pose to the audience?


2019-01-17 01:34:25
softbox is too large to fit into space. Attaching LED lights to AV panel for test.

2019-01-17 02:05:17
tested attachment placement and output w LED clip-on lights. solid. looks great too - like antenna

program.append({
    'name': 'GAIA',
    'iterations': 10,
    'step_size': 2.5,
    'octaves': 4,
    'octave_cutoff': 3,
    'octave_scale': 1.8,
    'iteration_mult': 0.25,
    'step_mult': 0.01,
    'model': 'places',
    'layers': [
        'inception_4c/1x1',
        'inception_4c/3x3',
    ],
    'features': range(111, 256),
    'cyclefx': [
        {
            'name': 'inception_xform',
            'params': {'scale': 0.15}
        },
        {
            'name': 'octave_scaler',
            'params': {'step': 0.2, 'min_scale': 1.4, 'max_scale': 2.0}
        },
    ],
    'stepfx': [
        {
            'name': 'bilateral_filter',
            'params': {'radius': 3, 'sigma_color': 20, 'sigma_xy': 50}
        },

    ]
})

program.append({
    'name': 'neomorph-neo',
    'iterations': 10,
    'step_size': 2,
    'octaves': 5,
    'octave_cutoff': 3,
    'octave_scale': 1.5,
    'iteration_mult': 0.0,
    'step_mult': 0.01,
    'model': 'googlenet',
    'layers': [
        'inception_4c/5x5',
        'inception_4c/5x5_reduce',
        'inception_4c/output',
        'inception_4c/pool',
        'inception_4d/3x3',
        'inception_4d/5x5'
    ],
    'features': range(64),
    'cyclefx': [
        inception_xform_default
    ],
    'stepfx': [
        {
            'name': 'octave_scaler',
            'params': {'step': 0.01, 'min_scale': 1.4, 'max_scale': 1.7}
        },
        {
            'name': 'bilateral_filter',
            'params': {'radius': 7, 'sigma_color': 16, 'sigma_xy': 60}
        }
    ]
})

program.append({
    'name': 'kwisatzhaderach',
    'iterations': 5,
    'step_size': 3,
    'octaves': 4,
    'octave_cutoff': 4,
    'octave_scale': 1.8,
    'iteration_mult': 0.0,
    'step_mult': 0.002,
    'model': 'vgg19',
    'layers': [
        'conv5_1',
        'conv3_1',
        'conv3_2',
        'conv3_3',
        'conv3_4',
        'conv4_1',
        'conv4_2',
        'conv4_3',
        'conv4_4',
        'conv5_3',
    ],
    'features': range(90, 512),
    'cyclefx': [
        {
            'name': 'inception_xform',
            'params': {'scale': 0.2}
        },
        {
            'name': 'octave_scaler',
            'params': {'step': 0.1, 'min_scale': 1.5, 'max_scale': 2.0}
        },
    ],
    'stepfx': [
        {
            'name': 'nd_gaussian',
            'params': {'sigma': 0.7, 'order': 0}
        },
    ]
})

program.append({
    'name': 'metamachine',
    'iterations': 10,
    'step_size': 1.8,
    'octaves': 6,
    'octave_cutoff': 6,
    'octave_scale': 1.8,
    'iteration_mult': 0.2,
    'step_mult': 0.0,
    'model': 'vgg19',
    'layers': [
        'conv5_1',
        'conv3_1',
        'conv3_2',
        'conv3_3',
        'conv3_4',
        'conv4_1',
        'conv4_2',
        'conv4_3',
        'conv4_4',
        'conv5_3',
    ],
    'features': range(-1, 512),
    'cyclefx': [
        {
            'name': 'inception_xform',
            'params': {'scale': -0.5}
        },
        {
            'name': 'octave_scaler',
            'params': {'step': 0.1, 'min_scale': 1.5, 'max_scale': 2.0}
        },
    ],
    'stepfx': [

        {
            'name': 'nd_gaussian',
            'params': {'sigma': 0.3, 'order': 0}
        },
        # {
        #     'name': 'octave_scaler',
        #     'params': {'step': 0.001, 'min_scale': 1.2, 'max_scale': 1.8}
        # },
    ]
})

program.append({
    'name': 'cambrian-implosion',
    'iterations': 10,
    'step_size': 10.,
    'octaves': 4,
    'octave_cutoff': 4,
    'octave_scale': 1.8,
    'iteration_mult': 0.25,
    'step_mult': -0.01,
    'model': 'googlenet',
    'layers': [
        'inception_4b/5x5',
        'inception_4b/pool',
        'inception_4c/pool',
        'inception_4b/3x3_reduce',
        'inception_4b/5x5',
        'inception_4b/5x5_reduce',
        'inception_4b/output',
        'inception_4b/pool_proj',
        'inception_4c/1x1',
        'inception_4c/3x3',
        'inception_4c/3x3_reduce',
        'inception_5a/output',
        'inception_5a/pool',
        'inception_5b/1x1',
        'inception_5b/3x3',
        'inception_5b/3x3_reduce',
    ],
    'features': range(-1, 256),
    'cyclefx': [
        {
            'name': 'inception_xform',
            'params': {'scale': 0.02}
        },
    ],
    'stepfx': [

        {
            'name': 'nd_gaussian',
            'params': {'sigma': 0.7, 'order': 0}
        },
        {
            'name': 'octave_scaler',
            'params': {'step': 0.001, 'min_scale': 1.2, 'max_scale': 1.8}
        },
    ]
})

program.append({
    'name': 'Geologist',
    'iterations': 30,
    'step_size': 3.5,
    'octaves': 4,
    'octave_cutoff': 4,
    'octave_scale': 1.8,
    'iteration_mult': 0.25,
    'step_mult': -0.01,
    'model': 'places365',
    'layers': [
        'inception_4c/1x1',
        'inception_4c/3x3',
    ],
    'features': range(93, 127),
    'cyclefx': [
        {
            'name': 'inception_xform',
            'params': {'scale': 0.25}
        },
        {
            'name': 'octave_scaler',
            'params': {'step': 0.13, 'min_scale': 1.5, 'max_scale': 2.0}
        },
    ],
    'stepfx': [
        # {
        #   'name': 'step_opacity',
        #   'params': {'opacity':0.5}
        # },
        # {
        #   'name': 'bilateral_filter',
        #   'params': {'radius': 3, 'sigma_color':5, 'sigma_xy': 10}
        # },
    ]
})

program.append({
    'name': 'Rivendell',
    'iterations': 30,
    'step_size': 3.5,
    'octaves': 4,
    'octave_cutoff': 4,
    'octave_scale': 1.8,
    'iteration_mult': 0.25,
    'step_mult': -0.01,
    'model': 'places365',
    'layers': [
        'inception_4c/1x1',
        'inception_4c/3x3',
    ],
    'features': range(127, 256),
    'cyclefx': [
        {
            'name': 'inception_xform',
            'params': {'scale': 0.2}
        },
        {
            'name': 'octave_scaler',
            'params': {'step': 0.13, 'min_scale': 1.5, 'max_scale': 2.0}
        },
    ],
    'stepfx': [
        # {
        #   'name': 'step_opacity',
        #   'params': {'opacity':0.5}
        # },
        # {
        #   'name': 'bilateral_filter',
        #   'params': {'radius': 3, 'sigma_color':5, 'sigma_xy': 10}
        # },
    ]
})

program.append({
    'name': 'ACCIO',
    'iterations': 10,
    'step_size': 2,
    'octaves': 4,
    'octave_cutoff': 4,
    'octave_scale': 1.7,
    'iteration_mult': 0.5,
    'step_mult': 0.01,
    'model': 'vgg19',
    'layers': [
        'conv4_3',
        'conv3_3',
        'conv4_2',
        'conv3_1',
        'conv3_2',
        'conv3_4',
        'conv4_1',
        'conv4_4',
        'conv5_1',
        'conv5_2',
        'conv5_3',
        'conv5_4'
    ],
    'features': range(34, 255),
    'cyclefx': [
        {
            'name': 'inception_xform',
            'params': {'scale': 0.025}
        },
        # {
        #   'name': 'octave_scaler',
        #   'params': {'step':0.1, 'min_scale':1.3, 'max_scale':1.8}
        # }
    ],
    'stepfx': [
        {
            'name': 'bilateral_filter',
            'params': {'radius': 3, 'sigma_color': 20, 'sigma_xy': 100}
        },
    ]
})

program.append({
    'name': 'JOI.02',
    'iterations': 20,
    'step_size': 1.2,
    'octaves': 6,
    'octave_cutoff': 5,
    'octave_scale': 1.3,
    'iteration_mult': 0.5,
    'step_mult': 0.02,
    'model': 'vgg19',
    'layers': [
        'conv5_2',
        'conv5_3',
    ],
    'features': range(15, 256),
    'cyclefx': [
        {
            'name': 'inception_xform',
            'params': {'scale': 0.1}
        },
        {
            'name': 'octave_scaler',
            'params': {'step': 0.05, 'min_scale': 1.2, 'max_scale': 1.5}
        },
    ],
    'stepfx': [
        {
            'name': 'median_blur',
            'params': {'kernel_shape': 3, 'interval': 3}
        }
    ]
})


2019-01-17 05:00:11
I'll have some time to review additional performance settings in the am.



2019-01-17 12:05:57
ready for disassemble

2019-01-21 22:30:04
setting up Python on Windows for IMAGEGARDEN dev

2019-01-22 01:10:42
created IMAGEGARDEN project and verified working

2019-01-22 21:11:03
The term socket is used for an internal endpoint of a locak INTERPROCESS COMMUNICATION (IPC) over a network

The network can be a
- logical network
- local network to the computer
- an external network, with its own connections to other networks, such as the internet


2019-01-22 21:22:43
By the end of this tutorial, you’ll understand how to use the main functions and methods in Python’s socket module to write your own client-server applications.

2019-01-22 21:50:44
Installing Python 3.7

The most common type of socket applications are client-server applications, where one side acts as the server and waits for connections from clients.

2019-01-22 23:25:05
the with statement uis actually very simple once you understand the
problem it solves:

set things up
try:
	do something
finally:
	tear things down

It’s handy when you have two related operations which you’d like to
execute as a pair, with a block of code in between.
The classic example is opening a file, manipulating the file,
then closing it:

 with open('output.txt', 'w') as f:
     f.write('Hi there!')

 the file will automatically be closed after the nested code blok completes

 2019-01-25 09:55:57
 I'm doing an impromptu lunch presentation at Britelite Immersive, invited by John Fesenko. Have added additional recenet dev video to the site. Need to clearout Vimeo however and re-upload some content as some of it is very low resolution unexpectedly

 2019-01-25 10:32:13
 I've created a new EC2 instance. The new p3dn.24xlarge includes 8x Nvidia Tesla V100 GPU upgraded to 32GB VRAM each, which should certainly allow for much higher resolution output. Cost is somewhat prohibitive though at $31.20/hr

 2019-01-25 10:49:31
 will need to set it up for neural style transfer w Torch install, etc.
 perhaps consider a Docker container?
 One of the resources I can share from the workshop is a Docker container (a link to one) with required environment for self exploration

 also need to set this machine up w a Public DNS for EZ access

 My opening presentation is for engineers, and I think its worth expressing some of the technical details. Just sharing my notes would be OK. (from iPad, this text file)

 2019-01-25 10:54:52
 interesting. I was able to spin up a new p3.16xlarge instance without further intervention. I recall having to deal w customer support previously.

 2019-01-25 17:53:15
 assigned elastic IP to other Lg instance (8 GPU x 16GB), Apparently only 5 can be in use at one time, so leaving out the XL instance

 2019-01-25 17:59:57
 created ssh connection to syntheticaf-L-2 machine


2019-01-25 18:05:15
RESOURCES
https://towardsdatascience.com/important-resources-if-you-are-working-with-neural-style-transfer-or-deep-photo-style-transfer-719593b3dbf1

https://pytorch.org/tutorials/advanced/neural_style_tutorial.html

https://github.com/cysmith/neural-style-tf

 2019-01-25 18:25:21
 ran into issues building torch on new machine. not sure why. Need to retrace steps

 2019-01-26 23:06:53
 successfully installed neural style on syntheticaf-L-2 server

 2019-01-26 23:27:28
 found a python library called GPUtil that can be used to monitor GPU memory & utilization

2019-01-27 13:41:30
installing neural style, etc on syntheticaf-XL


2019-01-27 14:01:22
for proper Torch instull with CUDA 8+, you'll want to enter this flag before running the install script

export TORCH_NVCC_FLAGS="-D__CUDA_NO_HALF_OPERATORS__"
./install.sh

sudo apt-get install libprotobuf-dev protobuf-compiler

2019-01-27 14:25:45
successfully installed neural style on syntheticaf-XL
successfully installed GPUtil python library

2019-01-27 14:37:57
NEXT
- write a python script to send params to neural_style.lua (via bash?)

th neural_style.lua -gpu 0

2019-01-27 23:32:16
successfully installed neural style on syntheticaf-dev
successfully installed GPUtil python library

This K80 GPU is likely comparable to TitanX, so will be best to develop locally on Linux machine. Watching it render, its pretty amazing how much advamcement has happened w the Tesla100 GPU

.location-landing .culture-slide .culture-slide-title {
    margin-bottom: 25px;
}

2019-01-28 16:03:17
Jusr noticed this text:
we suggest using alternative instance types and/or spreading your instances across regions.

I created a p3dn.24xlarge instance on N.Virginia region.

2019-01-28 22:38:54
just attempted 1920px render on one of the new instancdes. Even w 32GB RAM, it fails with out of memory. AT least using a single stage rendering process

2019-01-28 22:41:08
taking a closer look at multistage rendering on a smaller instance. Maybe the 32GB instances are overkill? Looking at usage on syntheticaf-S p3.2xlarge instance:
1 Tesla V100 GPU w 16GB VRAM @ $3.06/hr

2019-01-29 00:40:28
I'm running the existing render1920.sh script on this single GPU instance. It uses a multipass rendering method to minimize memory requirement

2019-01-29 00:52:00
sooo. its addictive. Just one more render before bedtime!

2019-01-31 00:30:31
working on documentation

A former Wall Street quant sounds an alarm on the mathematical models that pervade modern

Simple, plain-English explanations accompanied by math, code, and real-world examples.

The definitive guide to Docker. Docker takes a standardized piece of software and runs it as a Game Boy would run a game.

—


Creative AI examines three issues central to both intelligence and human  experience: misinterpretation, imitation and ambiguity. The truth behind current day AI is that machines aren't intelligent, but data can capture the intelligence emerging naturally in the world. For the case of neural style transfer, the outcomes provide insights into how meaning emerges from vision. What does it mean to capture the "style" of something? Indeed, what is Style? We know style when we see it, and can even imitate it, but just can't say it out loud. Questions like these are slippery and elude easy answers. Except, here is an answer.




Frank Rosenblatt was a research psychologist and head of the cognitive systems section at Cornell Aeronautical Laboratory. His work on neural networks and learning, led to the development and construction of the Mark I Perceptron in 1960.

2019-02-02 11:49:47
assessment of progress

- course notes
	+  onboarding
		* welcome to image garden
			- add contact information
		* what is creative AI
		* about neural style transfer
		x GPU computing
	+ setup and configuration
		* setup for macOS
		* setup for Windows
		* setup for Linux
	+ activities
		* Exercises
		* Parameter reference
	+ sample content
		* curated style images
- machine configuration
- intro presentation

TODO
P1 editorial about neural style transfer
P1 setup for macos
	+ can use same RSA key for all servers?
	+ will users of US East server need unique key?
P2 add contact information to onboarding
P2 embed star trek mis-classified youtube video on Crteative AI section
P3 test neural style on Linux  machine
	+ unpack and setup Linix machine
	+ walk thru setup of location w her
P2 for activities
	+ mention that you may want to style your own images
		* bring some in w you
		* use your phone to capture imnages and style them
P3 call out max number of available users io onboarding
	+ mention that some participants may need to partner up with others
P3 contact Esther status report




in light of the striking similarities between performance-optimised artificial neural networks and biological vision, our work offers a path forward to an algorithmic understanding of how humans create and perceive artistic imagery.

A Neural Algorithm of Artistic Style, 2015, Gatys, Ecker, Bethge
https://arxiv.org/abs/1508.06576

Briefly, neural networks are biologically inspired algorithms that learn how to recognize patterns. They interpret data by labeling and classifying input in terms of what they've learned. The patterns they recognize are vectors, which may be thought of as pathways into which all incoming data must be translated.


These pathways through a dataset were learned by training the elgorithm with samples typical



Content representation

content -lower laters, geometric structure & shape

We can hallucinate  new images whose features at a chosen convolution layer match the corresponding features of a given content image. We expect our hallucination will contain the same content — but not necessarily the same texture and style.


Gatys et. al found that the best results were achieved by taking a combination of shallow and deep layers as the style representation for an image.

we start with a blank image composed of random pixels
when training a neural network for image recognition, we ordinarily update its weights and biases to pass images through it along some optimal  path
but here, instead we update the image so that it passes through the (trained) network  along some "optimal" trajectory

the math behind style transfer determines the meaning of optimal trajectory.

For our purpose as artistic explorers, we soon realize that although you can pass any two images to this algorith and get results, some images work better than others. What we want are controllable outcomes. Style Transfer is a deterministic process. Given the same inputs it will always produce the same output. Without going deeper, this can lead to generic or uncontrolled outcomes. Our goal is to create personal imagery that exploits the fundamental design principles of line, shape, color, scale and sequence. It's a detective story. Unlike plugins or effects you may have used in other content creation tools, the neural network plays a large role. It's internal representation of "style" and "content" often corresponds with a human understanding of these ideas—sometimes amazingly so. Sometimes however, this is definitely not the case. Once you start tweaking the dials, a vast space of possible imagery opens up, which can be a bit daunting.

What you need to know
Images with similar content have similar representations in the higher layers of the neural network
By style we basically intend to capture brushstrokes and patterns, so we look at an images lower layer features, which capture geometric details.
The "best" results often come from combining images which have overlapping representations at both high and low layers.

editorial about neural style transfer
	x editorial 1st draft
	- revise, clean up editorial
	- add pictures
	- add related links

examples:


note - this section bmentions:
The "best" results often come from combining images which have overlapping representations at both high and low layers

Best I can do to illustrate this is analyze some prior successes
- create a section for "Why do some images work better than others"

2019-02-03 22:55:22
working on setup and config, and will be able to wrap up that editorial work for tonight's worksession. My target is to sent Esther this material on Monday afternoon so students will have a chance to review before the workshop on the 6th. I also need to confirm the workshop time w her.

what is the standard workflow I've observed?

install text editor
install FTP
install terminal
verify by entering siu

pick images
pick a content image
pick a style image

upload images to server

edit rendering script
navigate to script in FTP client and edit
- text editor needs to be setup as default editor

upload script to server

run script

navigate to export directory in FTP client
- may need to refresh window to update this view

copy export directory to local machine
- you can "peek" at images on the server w FTP client

review images

2019-02-03 23:46:59
ISSUES W RENDERING SCRIPT

- use default projectname when projectname isnt provided as an argument
- edit this msg: Your images will be saved here: /users/dev/devtest1
	+ Your finished images will be saved here: /users/dev/finished/devtest1
- rendering script should also be saved to finished/projectname directory

2019-02-04 08:43:15
finalizing the Workflow page
intention behiond this page is to provide high level overview of what participants will be doing during the workshop. This is the rhythm I've observed during prior events

So that you get results in minutes rather than days, you'll have dedicated access to a NVIDIA® V100 Tensor Core GPU (16GB) running on an Amazon EC2 P3 instance in the cloud.

Installation
Download access key
Download text editor
Install text editor
Download FTP
Install and configure FTP
Download Terminal
Install and configure Terminal
Locate your user folder in the Terminal
Verify installation by running the render script in your user folder

Get to know your workspace
Locate your user folder in the FTP client
Locate the rendering script in your user folder
Locate the finished folder in your user folder
Locate the pictures folder in your user folder

Pick images
Review the images on the server
Image list is provided on course wiki
On macOS you can preview files on the server by pressing SPACE for quicklook
Pick a content image
Pick a style image

Upload images
Upload any new images to your pictures folder

Edit the rendering script
Open the rendering script from the server in the FTP client
Change the filenames in the content and style fields to match your image names
Change any parameters by editing the relevant field

Upload the script
If you opened the script from the FTP client, save will upload your changes to the server

Start the render
In the Terminal, run the script and give this rendering project a name: ./render1920.sh projectname
The script notifies you when the rendering is complte

Download finished work
Locate the rendering project in the finished folder
Refresh window by clickiing button on the toolbar

Copy the rendering project to your local machine
On macOS you can preview files on the server by pressing SPACE for quicklook

Review finished work

2019-02-04 13:39:13
completed 1st draft for workflow section

2019-02-04 23:25:59
completed macOS setup

2019-02-05 03:28:40
finished editorial pass on macos & windows setup pages

2019-02-05 03:52:20
sent workshop documentation to Esther

2019-02-05 10:21:38
TO-DO

- reinitialize user setup on all 3 servers
- verify usage of existing RSA key w gfx servir un US East region
- update groups/username doc
- print groups/username doc
- create parameter reference examples
- curate demo styles
- create demo styles page
- verify Windows setup on Parallels VM
- create 5 slide deck (who am i) combining ArtX & Nature Gallery talk
- create quickstart notes for users who setup on the test server and now need to setup on graphics server
- - verify render.sh functionality on all servers

2019-02-05 12:00:54
- verify usage of existing RSA key w gfx servir un US East region
- update groups/username doc
- print groups/username doc

2019-02-05 12:15:16
just noticed bug in safari where downloading the .pem file append .txt extension to the download
solution is to zip the file for download?
or maybe host on a different server? NO, DOESN'T FIX
add this step to documentation

2019-02-05 12:55:40
provided zipped .pem file for safari users on macOS

2019-02-05 16:23:46
How many p3.16xlarge instances can I run on a single region?

I need to use this grouping
4	1 x p3.8xlarge 		US West (Oregon)
8	1 x p3.16xlarge 	US West (Oregon)
8	1 x p3dn.24xlarge 	US West (Oregon)
Total 20 GPUs

2019-02-05 21:06:27
verifying servers

2019-02-05 22:36:27
ran into a use case where I had to edit permissions of synthetic_rsa.pem to authenticate properly. Updated macOS setup doc to set permissions immediately after download to avoid the error. also detailed fix in troubleshooting section.

Wondering if the same issues will apply to windows? or is iot an entirely differnt matter w .ppk file as key?

experiment 1
weight ratio

A copy of this script was saved here: /users/dev/weightratio-a.sh
Your images will be saved here: /users/dev/weightratio-a


for serbver init
data.txt should be empty
use updated render1920.sh script
use updated lua script in neural style directory

2019-02-06 00:28:23
internet has gone down

- verify working on all servers
- create user folders for each server
- update keynote doc w usernames
- print username doc
- review demo pictures
- prepare notes on each parameter
	- STYLE_WEIGHT=5e2     # 5e2 (1e0 > 10e5)
	- CONTENT_WEIGHT=5e0    # 5e0 (1e0 > 10e5)
	- STYLE_SCALE=1.0     # 1.0 (0.1 > 2.0)
	- ORIGINAL_COLORS=0     # 0 (0 | 1)
	- POOLING=max           # max (max | avg)
	- NORMALIZE_GRADIENTS=""  # "" ("" | -normalize_gradients")

bass
bat
boat
body
brand
breakpoint
brooding
button
anagram
anodyne
anteater
antelope
cathode
cavepainter
cenobite
cook
coolhunter
cranberry
crayon
cub

2019-02-06 07:30:43
internet is back up. woke up early to take care the last minute details. I need to be ready to leave at 9a. Workshop is at 10:30

updating docs with myfirstrender instructions
updated rendering script
verifying duplicate project name. not working

ready to create user profiles
will copy dev and duplicate to all

2019-02-06 08:26:09
finished configuring syntheticaf.medium
starting config for syntheticaf.large.1

2019-02-06 08:47:36
finished configuring syntheticaf.large.1
starting config for syntheticaf.xlarge.1

2019-02-06 08:58:49
having trouble getting render script working on syntheticaf.large.1
going to hack at it over the next 10 minutes to see if Ican get it working, but if not  will restrict workshop to 12 participant, which may be more manageable overall, and will let people assist each other

2019-02-06 09:02:13
yeah - I'm unable to get that server working. will  work with reduced user group size

looking over my intro deck before packing up

2019-02-06 09:19:35
edited together intro presentation
packing up
ready to present

2019-02-06 14:12:37
That went well but could have been so much better. Really enjoyed the experience though, and I love how plainly I was abloe to speak about image synthesis in my opening presentation

WHAT WORKED
- people took the initiative and were able to setup their own machines from provided instructions
- people naturally started iterating on images
- people succeeded in working together
- it seemed like a failure at the time when I was unable to run the rendering script, but it restricted the number of users to 12, which was manageable overall
- kept a cool/casual attitude throughout and promoted my own work and journey well
- made new professional contacts - Maryanne and Ron, who run INSEEC SF
- strengthened professional contact w Esther
- invited to INSEEC class exhibition tomorrow
- engaged in conversation w several of the most interested students
- good handouts - included Group ID, server IP and promo
- got paid

WHAT DIDN'T WORK
- needed an assistant, possibly 1 assistant for every 10 participants
- setup instructions and method is too brittle, needs simplification
- Cyberduck was unstable on my machine, crashed on at least one other persons machine
- need to provide a visual overvuiew of the workspace (the config we're working towards)
- 2h workshop is 1h too short. 3h workshop would be better fit
- flow of the event needs more structure. needs to be structrured in terms of specific outcomes
- wasn't able to provide parameter reference in docs
- some confusion regarding the "username" on my handout and entering "ubuntu as username" on FTP config
- didn't take pictures or video

WINNING
- needed an assistant, possibly 1 assistant for every 10 participants
	+ Enlist "superusers" as assistants, call them superusers
	+ at INSEEC, I could have requested 2 students or staff ahead of time
		* beta tested workshop w them while training them
		* rewarded them w expertise
- setup instructions and method is too brittle, needs simplification
	+ Alternate hosting?
		* if Google had an equivalent service, what benefits would it offer w regard to setup?
	+ Update documentation and design
		* Where is there the most friction?
	+ Update UI
		* Is there a single dedicated crossplatform tool providing access to both a shell and a filebrowser?
		* Cyberduck isn't great. Why not use Filezilla?
		* Instead of downloading sublime text, use nano from the terminal
			- keeps focus on terminal windows and FTP client
			- eliminates steps for configuring FTP client w default text editor
- flow of the event needs more structure
	+ provide a goal
		* portrait
		* landscape
		* emphasize on gathering source images during workshop
			- provide only style images
	+ reduce number of demo style images to 5
	+ reduce number of demo content images to 1
		* discuss provided content and style images in terms of principles of design
- didn't take pictures or video
	+ need an assistant to do this w high level of detail
	+ My performance includes me taking 10 pictures of the event before/during/after on my phone

2019-02-06 14:21:52
spending the rest of the day creating parameter reference and starting new setup pages


2019-02-09 18:35:26
reinstalled Linux workstation
experimenting with rendering script locally


2019-02-09 18:43:54
rendering, wondering if 1920px output is possible?


2019-02-10 17:03:50
continued experimentation w rendering script. added support for multiple style images. impressed by how versatile the bash scripting language is, and yet can't help feeling this should be Python instead - especially if queing becomes a thing


2019-02-11 15:07:02
working toward some optimal image settings so as to provide baseline for parameter reference
Using various kinds of source and content images
self1-e variant is using  dense typography from illustrated book as style for saturated self portrait w isolated fg/bg

TODO
- for rendering script show resolution and filesize for style and content image
- parse normalize gradients parameter better
- show image size next to each iteration
	+ or bannounce each stage when it begins and show image size there
	+ can use this to show horizontal rule to seperate console output better
	+ show elapsed time there as well
- investigate rebuilding this in python
- perhaps interesting to capture content  and style and total loss in a csv file for further analysis or maybe comparison of profiles


2019-02-12 08:43:45
one issue I've noted after extended usage of the render.sh script is that when I open up one of the archived project scripts (the ones that are generated whenever a project is saved) its difficult to work with intention

Hard to express. Let me put it another way.

Its easier to open the archived script, copy the content, then paste it back into the render1920.sh scripty (the default)
Because when I am going thru a n iteration loop (new concept to express in docs), its easy to modify the default script, save it, press the up arrow in the terminal to repeat the previous render

(I realize its not working at the moment, but the rendering script is intended to generated a new numbered project name if it sees the current one is in use)

under this scheme, it takes the minimum effort to

- edit default render script
- execute renderscript with projectname
- examine the results
	+ in standardized working environment such as Linux VM, the final render could open automatically in the system file viewer
- repeat


2019-02-12 08:58:40

consider creating a section 8in the docs on how to set uup your own ec2 instance and run the workshop files
alternately - how to setip a local machine for linux install
that is perhaps its own seperate project. good documentation, and a chance to c reate a docker image (and experiment w same) however scope of this is quite broad

2019-02-12 18:20:41
Upcoming event
CARBON+
http://colorhythm.com/carbonplus/

event by COLORHYTHM
http://colorhythm.com/

hosted at 
Code & Canvas
http://www.codeandcanvas.org/



2019-02-17 19:13:27
decided against the code & canvas event to focus on workshop development. Feeling abit lame about it, but the timing is just wrong

installed pytorch implementation of neural-style. Possibly quicker/less memory intensive. Perhaps a better choice for rewriting rendering script as python


2019-03-07 11:01:19
I've been doing a lot of rendering style transfer work with the intent of collating the settings used in the scripts with the images to provide a parameter reference for my workshop documentation. When is that analysis going to happen?

2019-03-07 16:32:11
I had lunch with Ron at INSEEC SF, and we've started a conversation He invited me to beta test the Image Garden workshop for the various cohorts that run through the program there. Having lunch w Marianne next week.

2019-06-07 10:44:35
I'm working on some promotion and outreach today
- draft proposal to IEE VIS 2019 Arts Program
- draft description of Image Garden workshop for CODAME 

2019-06-07 10:45:54
made a few tweaks to deepdreamvisionquest.com layout and content, mostly to step back inside the work

2019-06-07 11:42:56
finished tewaking/simplifying deepdreamvisionquest.com for now. I haven't really looked at in in months. I renamed the "Visuals" section to read "Paintings", but I feel like that section wants to be about the workshops I've given - which would make the top-level menu more deliberate and purpose driven. To state:
HOME
INSTALLATIONS
WORKSHOPS
EVENTS

I can address that over the course of the weekend in conjunction with the writeup I'm doing for CODAME. For now though, without a doubt - the reduced body font size and simplification of the landing page are an improvement

https://new.precisionconference.com/submissions#

2019-06-07 18:14:55
completed abstract for proposal
created draft powerpoint doc to export PDF from
first pass curation of imagery to include for presentation
first pass curation of imagery to include as supplemental
added blog section to menu nav for deepdreamvisionquest

2019-06-08 00:43:12
finished sending the proposal. Its a first draft at best, but I believe it to be an honest and accurate reflection of the project and my intentions. Nice work.

2019-06-08 01:28:09
I refined the layout a bit and resubmitted the PDF doc

2019-06-08 16:59:26
axdditional design and content for deepdreamvisionquest.com

2019-06-09 12:04:10
removed PAINTINGS section, to be replaced with a WORKSHOPS section

2019-06-09 13:44:41
adding captions to assets in Installation Gallery

2019-06-09 13:49:37
- need to fix responsive menu text link color
- finish labeling Installation gallery assets
x use 13px font for Installation gallery items


2019-09-19 19:27:01
revisiting image garden rendering experiments from a few months ago. Collating them and correlating with the scripts that generated the images. At the time I'd expected to show the changing values and outcomes and use that to provide examples for documentation about process/workflow


2019-09-20 11:45:23
I've collated my dataset so that for each image there is a corresponding script used to generate it.
Need to take a look at the script agaion - what are the parts that change?
starting my analysis with a single image series


2019-09-23 17:36:58
mapped out workshop flow as a timeline
updating text for CODAME description now



SAMPLE

This hands-on workshop explores Digital Signal Processing concepts, acoustic phenomena like feedback and reverberation, and how to organize audio processes to create fun, expressive, and surprising sound-spaces.  Participants will use their own Mac/Windows laptop with a built-in microphone capable of running the demo version of Ableton Live to design a unique sound-space that transforms ambient sounds into a custom, evolving, interactive sonic landscape.  The workshop will culminate in an  exposition of our creations, open for attendees of all workshops to enojy!


SAMPLE

Learn how to create 360 sketches with both analog and digital tools that can be viewed just like 360 photos on the web or in VR headsets.  


As sketching is often quicker than 3D modeling, creating a quick immersive sketch for VR design, game design, or architectural design can be a great tool to ideate on and communicate a space, scene, or experience.  Bring both analog (pens, pencils for drawing on copier paper) and digital tools (tablets with drawing apps that support layers) and any VR headsets (Google Cardboard, Oculus Go, ect.) to view the results.


WORKSHOP OUTLINE
This is a 2 hour workshop which incudes both analog and digital exercises:
Introduction to Equirectagular Projections
Exercise: Drawing on Equirectangular Grid Paper
Photograph drawings, crop, and load into tablets & VR Headsets (like Oculus Go)
Demonstrate 360 Drawing with Sketch 360
Exercise options
Make 360 sketch with Sketch 360
Make 360 sketch with any drawing app using Equirectangular Grid underlay
Continue Paper 360 drawing
View results in tablets & VR Headsets

SKILL LEVEL
No coding experience is required to participate in this hands-on workshop.

WHAT TO BRING
Laptop running MacOS or Windows
Not a must: VR headsets (Google Cardboard, Oculus Go, etc) to view the results

WE WILL PROVIDE
Analog tools such as pens, pencils for drawing on copier paper
We can share one Oculus Go to experience your creations.

SOFTWARE TO BE INSTALLED
Drawing apps that support layers
Sketch 360


SAMPLE

The emergence of interactive art exhibits like 29Rooms, Museum of Ice Cream, Onedome, Artechouse has been recently trending. Now imagine others experiencing your creations without the need for them to travel or augmenting a pre-existing accessible physical space with your own creations. 

Join creative technologist Jasmine Roberts in learning to create surreal and immersive environments in the Unity Engine and play with concepts like scale and haptic interaction. 


Unity is used in 80% of AR/MR/VR so is a valuable tool to get acquainted with. Unity’s versatility opens a myriad of possibilities for creators.  

A lot of creation processes for quality experiences are very obscure because it is all based in technologies;  we will make this accessible, collaborative and fun. The goal is to demystify XR development! 

In addition to Unity, we will be using OpenXR so you can port your creation to different devices. By the end of this workshop, you will have created an interactive and immersive journey that you can potentially showcase and submit to exhibitions and festivals.

WORKSHOP OUTLINE

Below is an outline a 2 hour workshop:

Introduction to Unity: Basics
We will cover the Unity panels, how to create materials in Unity and how to implement shaders in Unity.

Tips and tricks when developing for XR

Importing a 3D model of yourself into Unity

Creating your personal environment (custom high-quality premade assets, shaders and scripts will be provided to all participants specific to this workshop)

Porting to deploying to mobile phone, VR or mixed-reality
(each participant will learn to deploy to bot)

SKILL LEVEL

No coding experience is required to participate in this hands-on workshop.

 

WHAT TO BRING

An open, creative, inquisitive mind

Laptop running MacOS, Windows or Linux
If you would like to create a VR piece please have a VR-enabled laptop
(i5-6500 or Greater CPU, NVIDIA GTX 980 or AMD R9 390 GPU or greater, 16GB+ RAM, SSD)

If you would like to port to mobile least Android 9.0 or iOS 11.0

 

WE WILL PROVIDE

We will have multiple devices to choose from: Windows Mixed reality headsets, a Google Daydream, and Oculus Quest 


SOFTWARE TO BE INSTALLED

The Latest Version of Unity3D

Optional: Blender, Cinema4D, any CAD software


 Science is a search for evidence, but science communication is a search for meaning. Nothing makes content more meaningful than a good story. Drawing inspiration from creative processes used in the film industry, this workshop will offer tools to help you share your scientific, tech, or any other content with the public in any space through effective storytelling. Using examples from both popular films and scientific studies, we will explore how to humanize a subject through story development and draw in broad audiences through visual storytelling.

 

///WORKSHOP OUTLINE

In this hands-on workshop, you will:

Learn effective communication strategies grounded in film story art methods, cognition research, narrative theory, and graphic design.

Explore and articulate your professional motivations through these strategies.

Develop your own story for use in a context of your choosing.

Build a conceptual framework for future communication opportunities.

 

///SKILL LEVEL

Intro

 

///WHAT TO BRING

Bring something to write on and something to write with.



Join creative technologist Jasmine Roberts in learning to create surreal and immersive environments in the Unity Engine and play with concepts like scale and haptic interaction.

this workshop will offer tools to help you share your scientific, tech, or any other content with the public in any space through effective storytelling.

This hands-on workshop explores Digital Signal Processing concepts, acoustic phenomena like feedback and reverberation, and how to organize audio processes to create fun, expressive, and surprising sound-spaces. 

Learn how to create 360 sketches with both analog and digital tools that can be viewed just like 360 photos on the web or in VR headsets. 






V1

[value proposition]
Learn how to create digital collages by exploring the visual language garden represented inside a neural network.

[Background]
This hands-on workshop answers the question, "what is style?" by demonstrating how to transfer the style of one image to another. The idea of sampling the real world to synthesize new imagery has been broadly applied in computer graphics and videogames since the 1990's. Neural artistic style transfer, a method for repainting images in the style of other images using a neural network is one such application.

No coding experience is required, however we'll configure a simple development environment on your laptop which will have you editing scripts and running GPU computations on a graphics workstation in the cloud. 

A course wiki will be shared with attendees for self-study, machine configuration and as a guide to further resources.

[Workshop Outline]
In this hands-on workshop, you will:

Generate unique, possibly thought-provoking high definition (1080p) images

Develop strategies to chieve controllable outcomes and tell stories by curating your sources

Uncover the hidden biases behind all machine learning technologies. We'll use these misinterpretations to make art instead of dystopia. 

You are invited to share your favorite images with CODAME for ongoing exhibition during the ART+TECH festival. 

WHAT TO BRING
- Laptop running MacOS, Windows or Linux
- Personal imagery. These can be JPG or PNG files.
- Optionally, you are encouraged to capture source material during the workshop with your phone. If you choose to do so, make sure you are familiar with transferring photos from your phone to your laptop ahead of time)

Software 
Cyberduck (FTP Client)
Sublime Text (Text Editor)
PuTTY (Terminal Emulator - required for Windows only)



2019-09-24 00:37:34
completed updated workshop description and sent out to CODAME



2019-10-04 16:30:20
collating my research on a sequence of 4 images. I'm looking to finish removing the parameters in these scripts so I can look at the changing values side by side



2019-10-07 08:42:45
I've placed a request for an instance limit increase and expect to hear back shortly
https://console.aws.amazon.com/support/cases#/6493721031/en


2019-10-07 09:42:02
rate limit has been increased. may take a while for change to persist to my setup. testing now though

the 2 large instances are starting
the medium instance is starting
the small instance is starting

Machine List
GPU count: 21
syntheticaf.medium 		p3.8xlarge 		4 	Tesla V100
syntheticaf.small 		p3.2xlarge 		1	Tesla V100
_syntheticaf.large.2 	p3.16xlarge 	8	Tesla V100
syntheticaf.large.1 	p3.16xlarge 	8	Tesla V100


2019-10-11 14:57:59
I'm reacquainting myself with the neural style setup and workflow.

logging into imagegarden.sm
ssh -i "synthetic_rsa.pem" ubuntu@100.21.156.90


2019-10-11 15:01:34
just noticed I was unable to run nvidia-smi
ubuntu@ip-172-31-24-209:~$ nvidia-smi
NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.


2019-10-11 15:05:22
seeing if updating the drivers works.
It does!
Will need to do same for all ec2 instances
details here:
https://stackoverflow.com/questions/55261785/nvidia-drivers-stopped-working-on-aws-ec2-instance-with-ubuntu-16-04-and-tesla-k


2019-10-11 15:15:13
need to setup the default rendering script to make a nice image
need to setup neural style transfer environment on new instance


2019-10-11 16:27:18
I'm going to rebuild these instances to be current. I'm getting some unexpected behavior


2019-10-11 16:59:09
aaaand I;m having trouble installing Torch


2019-10-11 17:25:56
good web demo here
https://tenso.rs/demos/fast-neural-style/


2019-10-11 17:33:12
not sure where the problem is. I'm able to run neural; style on a pre-existing machine:
imagegarden.medium

but I'm getting an error "no args provided" when I run the test render script

aaaand.... its because I didn't provide an argument, which it's expecting


2019-10-12 18:26:25
I'm still trying to setup that ec2 instance. I thought I might just clone an existing instance as an AMI and launch that, and it seems to work - I'm not sure why it wouldn't, but the style transfer code doesn't run, it just freezes and does nothing. Maybe I set that up wrong


2019-10-12 18:42:16
I took a closer look at the AMI I'm using on the existing instances and found a match to that. I'm launching that and setting up the environment manually


2019-10-12 19:50:27
Ok I got Torch built. Only difference this time was that I updated the system before attempting installation again

sudo apt install -f
sudo apt-get update
sudo apt-get upgrade


2019-10-12 20:31:05
the installation was successful (I think) I didn't pull down the neural style repositiory to test but al the dependencies installed properly

I'm taking a look at a setup where there are multiple users
installing torch & neural style in the home directory - the intention being that both users will be able to use this


2019-10-12 21:25:30
I've created a new user account for this ec2 instance
I've added my public key to the new account's .ssh/authorized_keys file
I've verified ssh login to this instance as the new user


2019-10-12 21:43:30
realistically - I don't think its the best use of time to figure out how to set this up on multiple accounts. The prior method of keeping everyone on a single account with user directories there works fine.


2019-10-12 22:49:14
installed neural style repo
running test render to validate
looks good


2019-10-12 23:19:45
running my shell script
rendering process seems slower than I recall though

NEXT
P1 verify workflow on MacOS
P1 verify workflow on Windows
P2 do a series of timed renders on the default rendering script
P2 setup user accounts
	- minimum content
		+ just include the images needed for the test render
		+ pick a cool looking sample as test
	- set up user accounts as templates on my local machine and copy replace on the instances when I update

2019-10-13 20:49:04
Testing Windows workflow
It occurs to me that whether I use Cyberduck or Filezilla - it should be possible to include the configuration file in the documentation which potentially saves a configuration step

2019-10-13 21:20:20
Maybe not though - Cyberduck needs to be provided with a hardcoded path to the .ppk key file

2019-10-13 21:34:29
The windows workflow to open a terminal Window from Cyberduck has a small wrinkle.
Upon connecting to server in Cyberduck, you choose to Open in Putty
The first time you do this, a terminal windo appears with an authentication message , requesting a yes/no response (yes is the proper response)
But when you press enter, the wiondow closes.
You have to return to Cyberduck and choose Go to Putty again.
This time, a system dialog appears with the same authentication message you confirmed previously
Once again, you select YEs
Now the terminal window opens and you're good to go

How much harder would it be to open a proper Shell from Windows?

2019-10-20 00:34:06
finished 1st draft of Windows setup

NEXT
cleanup page layout
	- make the software requirements list a seperate page?
start on MacOS setup doc

Setting up your login credentials
In practice, you'll use Cyberduck as a file manager - to move files between your laptop and the server, and to open scripts from the server. Here you'll configure it with the credentials of the neural-style server and provide the software with your server access key. Then you will tell it to use Sublime Text as its default text editor.
Launch and configure Cyberduck

2019-10-20 11:52:33
I've completed the WIndows setup section
will need to test this on fresh windows install
- parent's machine?

NEXT
update and author MacOS setup

2019-10-20 11:57:31
is it possible to have participants go to a mailing list sign up from confluence??

2019-10-20 23:41:27
completed macos setup
restructured doc to  remove chaff
collected various Pikazo triptychs for adding as a resource and for my presentation

2019-10-25 08:01:48
- cleanup user folders and include only know good images as subjescts and styles
- how to do simple photo edits?


Sign up to receive our profane advice delivered bi-weekly to your inbox!


cd ~/Downloads
chmod 400 synthetic_rsa.pem

2019-10-25 23:50:00
Taking a look at the rendering script. Its less dependent on style scale than the prebvious, but I forgot how I'd reactored this. At the moment, I am figuring out a way to store floating point calculations in a shell script so that I can:
- increment style scale by n each rendering pass
- decrement style scale by n each rendering pass
- keep style scale constant

I dont want o soend more than 20 minutes on this however. So the fallback is to set those values as constants and work from there. Maybe that's where I should be focusing though...



a=$(echo|awk 'BEGIN {print 100/213}')

scale_start=0.2


2019-10-25 23:57:13
try working with a scale that is hardcoded to increase

2019-10-26 03:47:34
I'm setting up user accounts on each server now. Wrapped up my Confluence work a moment ago

2019-10-26 05:20:51
All of a sudden, neural style isnt working on imagegarden.large.2 the new server. Going back through my notes, I verified it working and I remember doing so. What has changed?

I'm worried about a reinstall of torch, etc. on a new instance. I'm rebooting the instance before doing anything else

2019-10-26 05:34:23
reboot doesn't change anything
I'm going to try to create a new instance from an image I made of imagegarden.large.1

2019-10-26 05:58:36
created the new instance from the AMI. Tentatively hopeful.
the neural_style.lua script is running
imagegarden.sh script is running
takes much longer than expected to get started though?

2019-10-26 06:19:28
Fantastic. Everything is working. Doing quick stress test with 3 simultaneous renders from different user folders. Seems reasonable. The slowdown may go away on its own? It seems like it may be related to caching?

I've created the appropriate user folders on this new instance and have updated the handouts 

2019-10-26 06:26:26
get some rest. great work today. Quick thinking too.

NEXT
- reconnect to imagegarden.large.2 to verify working
- print handouts at front desk
- pack macbook 
- depart here at 8:30-9a

2019-10-26 15:25:48
Fantastic worshop. postmortem to follow, but good job man


2020-12-15 18:05
I've started reading the Feature Visualization presentation around the Lucid visualization framework (described as the spiritual successor to DeepDream) It relies on TensorFlow. Once I have the workflow nailed down it will be a great test to bring this work over to the Windows environment as well
https://distill.pub/2017/feature-visualization/


2020-12-18 10:46
As I read about deep dream and inceptionism in general, I realize my mental model about that process was a bit incorrect. Maybe even backwards. 

Deepdream is a way to optimize images to make neurons fire.


2020-12-21 12:53
I continue to experiment with tensorflow using docker, which is presenting some shifts in my thinking about the kind of development I've previously done/ Is there really a difference though? There's a conceptual bridge I haven't fully crossed yet. I'm stepping thru a python 3 & bash shell workflow to see how it works


2020-12-22 13:23
I feel like I'm losing sight of my goals in the details. let me state them clearly :)

I want to run the realtime object recognition demo mentioned here:
https://www.sicara.ai/blog/2017-11-28-set-tensorflow-docker-gpu

It does some interesting things:
- demonstrates providing webcam access to docker image
- requires OpenCV
- requires TensorFlow
- requires Python3

My expectation:
- I can locate a Docker image with a Tensor Flow GPU OpenCV environment
    - what's preventing that?
- I don't have to hand-roll anything because the whole pointer of Docker is trivial environment setup for the stuff I want to do


candidate
- fbcotter/docker-tensorflow-opencv
  - opens Jupyter server after Docker run. I need a bash prompt
  - able to enter bash prompt now
  - need to pull down git repository inside this environment
  - git command is available
  - opencv is available



2020-12-22 17:34
this particular repository isn't working properly, but its running. Not sure where the problem is. Suspected that I need a different version of tensorflow or opencv ?

In the meantime i verified webcam input to this machine using the familiar Video4Linux control panel



2020-12-23 11:17
better understanding of containers and images after doing some tutorial work with Docker
I found a collection of images that I may be able to pull down for my purposes

DOCKERFILE WITH NVIDIA GPU SUPPORT FOR TENSORFLOW AND OPENCV
https://github.com/datamachines/cuda_tensorflow_opencv/blob/master/README.md


docker pull datamachines/cudnn_tensorflow_opencv
docker pull datamachines/cudnn_tensorflow_opencv:10.2_1.15.4_4.5.0-20201204


docker pull datamachines/cudnn_tensorflow_opencv:9.2_1.15.2_3.4.10-20200423
- Cuda 9.2
- CudNN 7.65
- Tensorflow 1.15.2
- OpenCV 3.4.10

cudnn_tensorflow_opencv:
- installs Cuda 9.2
- installs CudNN 7.65
- Builds a GPU optimized TensorFlow
- Builds a GPU optimized OpenCV
- installs Jupyter
- installs Keras
- installs numpy
- installs pandas
- installs PyTorchdock
- installs X11 support
- python 2.7
- python 3.6

Testing GPU availability for TensorFlow:

CONTAINER_ID="datamachines/cudnn_tensorflow_opencv:9.2_1.15.2_3.4.10-20200423" ../runDocker.sh -X -N -c python3 -- /dmc/tf_hw.py


docker run -it --name testrun -v $(realpath ~/code):/dmc datamachines/cudnn_tensorflow_opencv:9.2_1.15.2_3.4.10-20200423 bash


2020-12-23 15:09
I'm getting closer to understanding how to use docker for my workflow, but even now feeling like I'm missing the point of it all. There are some fundamental assumptions I'm making that are getting in the way. I thought that the first challenge would be to verify webcam input to a docker container. It turns out to be more fundamental.

I spent time today understanding how to read/write between the host and a container. I was able to do so using the Volumes feature, but ran into permission issues while doing so. Best case I was able to achieve was verifying superuser password every time a file was saved from the host filesystem to the container. I'm reading that the Mounting feature may be the better option.

What am I expecting
- I expect to use sublime text to write code and data which will be stored in an understood project structure on my local filesystem
- I expect to use git for version control of my source materials, using same workflow previously established for deepdreamvisionquest
- I expect to choose a dev environment which matches dependencies of the software I use, instead of configuring the dev environment myself
- I expect that by using docker containers, I will avoid having to configure my machine at all
- I expect for a container to receive webcam input

What am I assuming
- the container needs to be running while I write code
- the command to execute code must be entered from a shell inside a running container

Instead of running code from a prompt inside the container
(like this)

root@f974732a7fdb:# cd ./code/myProject
root@f974732a7fdb:/code/myProject# python myApp.py

I could instead:
docker run -it -v $(realpath ~/code/myproject):/myproject python:latest python /myproject/myapp.py

verified working. extremly clunky though, but there are some ways to simplify
- I think its possible to abstract $(realpath ~/code/myproject) as 'myproject'
  - an added benefit is that now this declaration can be shared with other containers


2020-12-23 23:46
spent time setting up networking between LOCUTUS and HALLUCINATR. Sharing my Windows user folder to linux machine and am able to read/write to the filesystem from either machine


2020-12-24 00:48
following up on the material about docker mounts vs volumes

NEXT
create a container from opencv image
- validate basic webcam demo created at /code/cvwebcam/src/webcam.py


2020-12-24 17:43
moving these notes to the spiritanimal log


2020-12-24 17:50:50
I'm going to step through a docker exercise in we want to build a very basic website using a Node.js server with a React front end. For purposes of the tutorial we will Dockerize both server and client

actually ended up avoiding that tutorial because of the node.js related dependencies that cause my to spin my wheels.


2020-12-31 01:20:42
stepped through the docker tutorial again, and was able to get into the spirit of it better after some distance. The development workflow that I was confused about previously seems pretty straightforward now.


2021-01-04 10:26:58
let me recapitulate my progress.

I ran a docker image of the nginx web server as a background process and connected internal port 80 of the container to the external port 80 on the host (my machine). I assigned this container a name so I could access it in a friendly manner. I specified a host file paths (my local dev environment) to be mounted to relevant file paths on the container. This was quite easy because the nginx server has an 'html' folder from where it expects to serve content. The server is viewable as localhost:80 in a web browser

Now the web server is up and running, I can work as I would ordinarily work within my local dev environment. Any changes I make in the html directory are editable/actionable on the container. From my point of view, I just update a file then refresh the browser. If I wanted to, my file system could be version controlled an so forth - Docker doen't know or care about that

How would I apply this workflow to my use case for viewing webcam output using OpenCV using my prior code?
- check the dependencies for that code. Is it just OpenCV?
	+ Yes, its just OpenCV
- find an OpenCV docker image
- How will I run the code?
- how do I pass the host webcam device to the container?
- how do I view openCV output from the container?
	+ by making the host Xserver available to all users
	+ then mounting the host device path /tmp/.X11-unix to the container 

docker run --rm -ti --net=host --ipc=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix mnieto/opencv_gui ./sample/build/bin/opencvSample ./sample/docker.png


2021-01-04 12:09:39
I am able to run a text container demonstrating openCV output to the xserver on my host machine. a couple of warning messages appear:
libdc1394 error: Failed to initialize libdc1394
Gtk-Message: Failed to load module "canberra-gtk-module"


2021-01-04 12:24:16
Gtk-Message: Failed to load module "canberra-gtk-module"
I'm able to make the warning go away by installing the package within the container

sudo apt install libcanberra-gtk-module libcanberra-gtk3-module
sudo apt install libcanberra-gtk-module libcanberra-gtk3-module

The other warning has to do with inability to initialize libdc1394 because there's no such device within the container. This may not be hugely significant for my purposes though. Seems like it just has to do with a firewire (1394) interface


2021-01-04 14:19:42

docker run --rm -ti --net=host --ipc=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /home/gary/code/cvwebcam/src:/cvwebcam  /mnieto/opencv_gui bash


2021-01-04 14:39:11
I've mapped my python project directory to the container's filesystem
I've verified Python 2.7 running in the container

docker run --rm -ti --net=host --ipc=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /home/gary/code/cvwebcam:/code/cvwebcam mnieto/opencv_gui bash


2021-01-04 15:23:42
I need to setup video input to the container


2021-01-04 16:47:31
before setting up video input to the container let me verify that I can run a python program from the directory I mounted to the container'


2021-01-04 17:00:07
working w another Docker image which includes X11-Forwarding in the Dockerfile
The tutorial example includes video i/o and a test case

docker run --device=/dev/video0:/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -p 5000:5000 -p 8888:8888 -it spmallick/opencv-docker:opencv /bin/bash


2021-01-04 17:11:25
great. This example worked as expected to output an image from open CV running in a python script


2021-01-04 17:22:13
Here's a different set of images w OpenCV 3.1.0/3.2.0 + Python 2/3 binding
The default image, victorhcm/opencv points to version victorhcm/opencv:3.1.0-python2.7

verified Python2.7 import of OpenCV

docker run --device=/dev/video0:/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -v /home/gary/code/cvwebcam:/code/cvwebcam -e DISPLAY=$DISPLAY -p 5000:5000 -p 8888:8888 -it victorhcm/opencv bash


2021-01-04 17:41:34
python is apparently unable to open the camera...


2021-01-04 17:41:53
rebooting...


2021-01-05 13:58:32
I'm installing libcanberra-gtk-module in the container so it can access X11


2021-01-05 14:17:44
docker run --gpus all --privileged --rm -it 
--env DISPLAY=$DISPLAY \
--env="QT_X11_NO_MITSHM=1" \
-v /dev/video0:/dev/video0 \
-v /tmp/.X11-unix:/tmp/.X11-unix:ro \
-v /home/jkg/PycharmProjects:/dev/projects \
chipgarner/opencv3-webcam:python2 bash



2021-01-05 14:41:28
SUCCESS!
I have a working example with video input from webcam and output to a window
My original webcam tests from back in the day are working now as well
The window being shown has some UI elements visible at the moment which I hadn't seen previously, but I'm sure they can be removed

**2023-02-25 11:33**

[[_Artworld]]
[[Why your AI art matters]]




