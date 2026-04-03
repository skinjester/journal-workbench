
2021-04-12 10:07
Looking at Steve's sample video to make sure I'm encoding my output correctly. We'd run into some issues previously when I brought over high bitrate 4K content, where the media was viewable, but did not play smoothly or well

Codec: H264 - MPEG-4 AVC
Frame rate: 23.976023


2021-04-13 09:53
I'm watching a tutorial on applying mp4 video as a material in UE4. I'm liking the idea of putting together a cinespace virtual environment. I can get a good start using the 3rd person game template and build it up from there.


2021-04-13 10:02
RECOMBINANT MEDIA LABS (RML) was founded in 1991 by Naut Humon [https://grayarea.org/community-entry/naut-humon/], to research and deploy the cultural qualities and artistic potential of Spatial Cinema and music mediated electro-acoustic surround sound. RML acts as producer, propagator, and presenter of substantive intermodal artworks for its panoramic performance platform the CineChamber. Recombinant Festival is an annual autumn event series in San Francisco that showcases international immersive residencies from RML’s nomadic network. Co-presenters have been Gray Area and Obscura Digital and now STRRR TV.


2021-04-14 16:58
I've constructed an initial Cinechamber. The static mesh layout for each screen anyway. I need to test the orientation of these with materials. Need to name each of these to correspond with screen 1-10


2021-04-15 16:12
watching the UE4 Media Player to Texture tutorial


2021-04-16 18:57
Finished setting up a level with reasonable lighting for a dark space with 10 projection screens. All the screens are showing the same movie file. I learned how to attach audio objects to the scene. I learned how to spatialize the audio in the scene.

NEXT
- how do I assign a unique movie file to each "screen"
    + is there a way to automate this?
- can I assign a Left & Right audio channel to independent sound objects?
    + how would these be arrayes?
    + for now, I think its fine if there's an unattenuated audio source. The whole point of this layer is to previsualize work doen in After Effects


2021-04-17 17:38
I've finished constructing the environment in UE4

NEXT
- create a list of animations to examine in this space
- is it possible to switch animations on keyboard input?



2021-04-18 08:05
preparing material to bring with me to Gray Area for motion experience testing

- GRID
- FONT SIZE REFERENCE


2021-04-18 10:47
not able to get the font size reference. instead focused on a handful of use cases intended to explore speed, and in one case - velocity and strobing effects. It only dawned on me that the stuff I was doing with the grid was tileable and didn;'t need to be rendered for eveery screen.

We have 4h at gray area, and I don't want to rush anything. I hope we can get some conversations or reactions to experiencing this very simple material.


2021-04-18 10:49
I want to spend the rest of today getting ONYX-UBUNTU setup for deepdream. The version where I run it in a notebook would be fine. I want to have this setup as a Docker image. I don't need webcam input or display i/o. Everything can be handled by the notebook 


2021-04-18 11:33
Actually I want to spend the rest of the day figuring out how to get 360 degree output from Unreal. Is it possible to directly map this to the screen array? Possibly as a cube map? How?


2021-04-19 17:11
I've been doing some experimentation with panoramic images. The panorama capture image output from UE4 appears as a plausible continuous space in the cinechamber.

A high resolution panoramic photograph also works. Not as coherent as the UE4 scene, but enough so that I can recognize how the panorama projection resolves itself when reprojected into the space. Its kind of awesome.


2021-04-19 17:16
within the UE4 scene it would be great to have the ability to assign movie file references more efficiently. At the moment, I need to specify the sopurce for each configuration. I want to be able to switch between configurations though, when I press a button. How do you do that?


2021-04-19 18:08
I have some test code in the level blueprint that can set a filepath at runtime. At the moment, its pretty cumbersome and would actually be harder to use than the GUI, but this exposes the mechanism by which it works.

I'd like to be able to pass an indexed structure to a function and have it know:
1. Which "preset" ?
2. Which assets are in that preset?
3. Where did I specify assets and presets?
    - in a UE4 data structure of some kind with parameters exposed/edited in the GUI?
    - in a text file?


2021-04-21 17:37
still figuring out ndisplay


2021-04-23 08:03
I've watched a couple videos for examples and have taken a deep dive into the format of the nDisplay configuration file which is perhaps the trickiest part of the overall methodology. I find myself struggling to believe that someething lik ethis could exist, or even to describe it to myself let me try to describe it for my future self:


2021-04-23 09:24

EXPLORE NDISPLAY TECHNOLOGY: LIMITLESS SCALING OF REAL-TIME CONTENT
https://www.unrealengine.com/en-US/tech-blog/explore-ndisplay-technology-limitless-scaling-of-real-time-content

nDisplay enables you to reproject camera views to surfaces placed in the virtual world which correspond to surfaces in the real world. Spatial input from the real world, such as a head tracker maps to functionality in the virtual world.

My interest in this technology is to take material authored in UE4 and reproject the environment on to the surfaces (10 seperate screens) of the Cinechamber "cave". Playback for that environment is all pre-recorded as 10 seperate .mp4 files and various audio files.


2021-04-24 10:54
The usecase mentioned in the UE4 documentation I think can work for my purposes is:

ONE APPLICATION INSTANCE THAT RENDERS TO MULTIPLE DISPLAY DEVICES
With this option you run a single instance of your UE4 application on a single machine but you set it up to render multiple seperate rectangles of the scenes 3D space into different areas within a large window.

You then use a technology such as NVidia Mosaic or Nvidia Surround to split up that single large window and render each seperate area on a different display device. My basic idea has been that I could take that single image into after effects and assign the corresponding screen to it. This is dependent on the ability to:
- render out the big view as a sequence
    + it seems that UE4 has non-realtime rendering capabilities
        * How does that work?
    + I'd have to keyframe and assemble all animation using Sequencer
    ! I don't know how to access that image
    ! I don't know if its possible to render viewports frame by frame (as though they were seperate cameras) from a UE4 application running in nDisplay. I haven't seen anything that suggests this is possible



2021-04-24 13:12
I am not seeing a nontrivial way to get nDisplay output saved out as an image sequence: whether from seperate cameras or as a combined image to be sliced up


2021-04-24 13:41
suppose I shifty focus to panoramic solutions instead?
I've seen some success w the UE4 built in panorama capture plugin
- how can that output be rendered as a movie file or image sequence?

There's a plugin on the marketplace called camera 360 that looks full featured
- can it do what I want?

MORE SPECIFICALLY
Does any panoramic output automatically "work" when reprojected?
What makes one kind of panorama work better than another?


2021-04-24 17:08
I was able to run nDisplay example project with limited success.
- package UE4 project
- run ndisplaylistener
- run the packaged UE4 project w ndisplaylauncher
- no error messages
- configuration is wrong
- not processing input from keyboard or mouse


2021-04-24 17:18
I just observed that while running each viewport specified in the configuration is being rendered to a physical window onscreen. These must each be a running instance of the UE4 project. I was able to ALT-TAB between these windoes and can see a preview in the toolbar, but I'm unable to select or manipulate the windows themselves.


2021-04-24 18:49
After doing some additional testing in After Effects using a spherical panorama scaled to fit the 12800 x 720 viewport, I am a bit surprised by how coherently the space appears to reproject into the cinechamber sim. This is just some arbitrary image, so how much better can this get?

current drawbacks
- resolution
    + the source image is fairly lo-rez and is being upscaled '
- coherence     

    + the source image is precomputed, so I'm unable to move the viewport and see the world move in response to this
- the longer the animation runs, the more apparent some tearing in the corner between screen 10 and screen 1 is. Not sure why. I wonder if the geometry I'm using for the screens is accurately placed?


2021-04-25 11:10
There's a UE4 plugin called Camera 360 that seems like it can do what I want, and possibly more. It renders out panoramic views of different types at a high resolution using UE4 Sequencer Render Movie or maybe the new Movie Render Queue? [Which?]


2021-04-25 13:13
Testing with a 16000 x 4000 sample asset scaled to fit screenarray width.


2021-04-25 18:59
I'm convinced the panoramic rendering from UE4 is the right direction for this project. I've purchased the camera 360 plugin $(169.99) as well as a Projector plugin, which enables images to be projected as a lifght source (sort of the inverse of a panoramic render)


2021-04-26 09:05
A pleasant surprise! It turned out to be quite simple to make the movie sequences in my UE4 project restart playback whenever the first one reaches the end of playback. This goes a long way to keeping the sequences synchronized.

Although I am realizing that the longer the duration of the movie file used here, the more drifting will occur. I'm not sure its even possible to synchronize mp4 playback for multiple assets.


2021-04-26 09:15
It looks like it is possible actually, although non-trivial. 


2021-04-29 15:39
-RESX=12800 -RESY=720


2021-05-01 15:52
getting close to success. I've worked out just about all the details of a UE4 workflow that can be processed in AE and reprojected in the cinechamber


2021-05-04 10:06
I can't believe I figured out how to do it! I've successfilly crteated a workflow that allows me to reproject a UE4 environment into the cinechamber CAVE. 

Ive been working with the UE4 Winter Scene and am a bit surprised at the resolution I'm getting from it. Everything in that scene is distant, the scale is in kilometers. It does feel and look like its far away but the quality of some of the high frequency details nearer to the camera feels like there's something wrong.

As far as I can tell, I'm not missing any steps.
I'm submitting level sequences to the render queue
I'm using tiled output to get the resolution I want
    - I'm using manual exposure setting with EV +11.5
    - I'm overriding any prior antialiasing settings
        + I'm taking 8 spatial samples
        + I'm taking 1 temporal sample
    - I've set the output size to match AE screenarray (12800x720)
        + this causes the UE4 render to crop the 2:1 panoramic render to the 160:9 cinechamber protocol
    - I've also used the full 12800x6400 UE4 output and then cropped it in AE to match the cinechamber aspect

As an experiment I compared output from 360pano(mono) and 360pano(6 camera) options from the UE4 plugin. (no obvious differences)

As an experiment I have increased spatial sampling for AA to 64
    - not as impactful on the rendering time as I'd have thought.
As an experiment I have increased temporal sampling for AA to 4
    - very impactful on rendering times



2021-05-04 10:30
working hypothesis:
- distant objects in UE4 don't sample at the same frequency as nearby ones

NEXT
- setup a test project with metrics for distance
- populate cinemachamber demo with stylized characters
- replace 3rd person mannequin with a more stylized character
- investigate large scale urban environment scene


2021-05-06 07:42
I've been able to get good renders of the Ice Road environment. Raytracing helped. So did increasing the amount of light in the scene. There's still some grainyness in certain areas from the raytracer, but any antialiasing issues previously observed have been resolved

I've moved on to a new Factory Environment and am isolating an assembly line of robots for later rendering. This is going to be a more graphically oriented presentation instead of the full environment expressed in Iceworld


2021-05-07 09:01
I'm taking a first look at the factory environment reprojected into futureworld. There are a couple of things I hadn't recognized before. This first rendering is pretty basic:

RAYTRACING
disabled

HIGH RESOLUTION
2 tiles
0.0 overlap

OUTPUT
12800 x 720

ANTIALIASING
spatial samples 8
temporal samples 1
override antialiasing TRUE
Antialiasing method NONE


The main thing I've noticed is that the further from the camera an object is, the worse the antialiasing appears. Or so it seems? This is a pretty quick render so here's an opportunity for some tests


2021-05-07 14:41
I've finally worked out the basic issue with antialiasing.
It was only peripherally related to spatial and temporal sampling.
The main parameter is the Quality (Texture Size) in the Camera360 plugin itself
Remember: the rendering is literally that of a texture mapped plane mounted to the camera. It seems that the quality parameter is the size of the texture map.


2021-05-07 14:45
The reason I say the sampling params are peripheral is because they don't directly relate to the resolution of the panoramic output. I kept on getting pixelated output and was tryingto fix that through sampling. Without the texture quality set high enough the image remained blocky looking no matter what the sampling rate


2021-05-18 15:02
lost some of my previous notes due to not saving them.
In those notes I spoke about viewing the sample material for the first time at Gray Area, as well as what to look out for and capture when I went the next time.

All of that was great, very successful implementation of this pipeline.

I've been setting up Ubuntu for style transfer on video. There are a number of challenges there. I've had some technical difficulty that I've only just now corrected. Or maybe not. I'm running Ubuntu 21.04 and its possible that I'll need to downgrade to Ubuntu 20.04. That would be a real drag, but I'm able to get back to my work environment pretty quickly

Disappointingly, I've been unable to get Ubuntu 20.04/21.04 working properly on LOCUTUS as a dual boot system. Ubuntu installs properly, but will not connect to the wired network on that machine. I left that unresolved

At the moment I'm working/learning to generate point clouds from video imagery for presentation in the UE4 environment. The method uses an application called Agisoft Metashape to generate the point cloud data. Apparently Ue4 can import this without complication.

The idea of using this kind of imagery may be a way to find a personal voice in the tech. I've spent a lot of time figuring out how this environment can be constructed but not so much time figuring out what is unique about the environment. My test renderings are just first steps but already I recognize how impersonal they feel. The mechanical precision isn't unwelcome, but I remain uncertain about what there is to "say" if anything. Its eye candy at the moment. 


2021-05-18 18:08
starting some initial tests with generating a point cloiud. not really certain that video is the best input, when it seems photographs might work just as well with benefit of no motion blurring


2021-05-18 20:08
more images are better it seems. Initial experiments with stuff around the house is promising. Precision seems determined by capture? I'm wondering - is it possible to sample any video in 3D. For xample, a videogame?


2021-05-19 20:07
I'm taking a look at a category of ios Lidar scanning apps. Interested to see the difference in quality. Its definitely more convenient to do, although I'm not getting interesting scans - mostly because I'm doing this so randomly.

I've got Ubuntu 21.04 running on LOCUTUS machine. The networking issues were (apparently?) resolved by making a change to the BIOS. Something about enabling the "network stack" which allows for booting from the network(?) as well. All quite mysterious but working now. I have installed and verified Docier with GPU support


2021-05-19 20:39
initial testing of a Lidar scan in promising. Significantly less effort for the results I want


2021-05-24 15:04
Moving images stretched across a horizontal plane.

Curved glass and steel, polygons and points surround you. Your field of vision is carefully controlled. Try to ignore that you're a robot.

A giant machine moves and breathes. It is the Great Engine which pulses and rumbles and hums. The sounds it makes are too many things at once, and also exciting. It is a sea of sound

It was a grave and mad symphony, the kind of sound that makes you want to dismember someone and eat their corpse. It made you want to call your mother and just breathe on the phone for an hour.

The narrator is describing the RML CineChamber, a cinema experience that presents works from the RML archive and new works by emerging artists. The CineChamber is a large, but intimate, rectangular surround-screen apparatus that can be scaled to fit into auditoriums, theaters and concert halls. It offers extensive, immersive intermedia production opportunities for creators and innovators.

The CineChamber is described as an international artist's venue to create art and engage in a creative process. Artists like Alva Noto and Blixa Bargeld, Ryoji Ikeda, Maryanne Amacher, Christian Fennesz, Biosphere, Ryoichi Kurokawa, Speedy J & Scott Pagano, Chris Watson, Thomas Brinkmann, Monolake, Pan Sonic, Poie, Matmos, Rrose Christian Marclay, and many more have taken part in the CineChamber's history. The CineChamber's lineage can be traced back to 1897 and Raoul Gromoin-Sanson's ten synchronized movie projectors in the round that was featured in a world exhibition.

our unique 'Paradox Cut' technique ensures continuity between scenes


2021-05-25 14:20
I've become very involved with point clouds, the possibility for self expression, and general uncanny presentation is so cool.
There's been a lot going on with the technical work, the overall vision and relationship with Yoann.

There's maybe more to say than I have time to document. But basically - having him over last weekend where we could talk and sort of touch the project together was great. I think it sparked an enthusiasm in him as well as myself. 


2021-05-26 09:31
I'm rtaking a quick look at Houdini. So far, its amazing and all I've done was construct a sphere with smaller spheres placed on its vertices. But its all procedural. Its infinititely deep. More like an IDE for 3D data and images. I'm looking at it with the hope that I can:
- import point clouds into Houdini
- export point cloud from Houdini as data for the Houdini/Niagara plugin
- Use Niagara to generate particles that travel to the defined points

desired outcome:
make the static points clouds I've been working with dynamic.
The project can work without this kind of animation, but I believe its an integral part of where I'm heading and worth the time.


2021-05-26 16:37
I've learned some Houdini basics and am taking a look at the Houdini-Hiagara plugin

use the plugin to bring point cache data saved out as JSON into UE4 Niagra particle system, along with attributes such as age, life, ID and color. These caches can be static or animated point clouds created using procedural modeling techniques or using Particle, FLIP Fluid or Rigid Body simulation tools.

Elsewhere on the web I've seen an example of bringing in a point cloud for animated distortion within Houdini.
https://youtu.be/QiPImlxP-H0



2021-05-26 17:03
There are additional approaches to point cloud rendering native to a UE4 workflow, but all are non-trivial. Approachable at a later time.


2021-05-26 17:05
As far as animated point clouds go, there are 2 methods I've observed:
- revealing a structure by scanning it
    + this is what I see whenever I make a scan.
    + I've seen an example of custom code that reads point datga live from a Kinect during a UE4 runtime. Would need to contact the author
    + High end example is the realtime environment reconstructions of lidar scans for automated vehicles & drones
    + simulating this in UE4 (or Houdini) requires sequential PLY files, just like an image sequence
- point cloud modulated by particle system
    + this is what I'm working on with Houdini export. Somehow you can use the point data to spawn particles? become the endpoint of particle lifespan?


2021-05-26 20:10
I have the UE4 Houdini/Niagarta project up and running. Playing around with the samples


2021-05-26 20:38
Wow. Its beautiful sometimes. The possible range of looks and reactions seems infinite. My inexperience makes it seem like magic 


2021-05-27 18:52
spent much of the day working in the arctic project file, experimenting with lighting and animation. When I stepped back into Houdio export for Niagara I got confused by the difference between the Houdini Engine plugin and the Houdini Niagara plugin. For a moment I thought I needed a license to do what I want with this and uninstalled the softthinking I'd need to reinstall a different version. That was not the case.

Another workssession tonight. I'm reading that Medium article on point clouds for better understanding.


2021-05-28 09:03
There's so much more to pointclouds than the visual appearance that drew me to them. Its a huge surprise to realize that they don't work the way I'd assumed was natural. I had supposed that these point entities were just sort of floating in space based on the scanned x,y,z coordinates. That much is true. That's exactly what they are. But like the holographic principle states - a volume of 3D space can be completely described by a 2D encoding on its boundary. 

In the case of point clouds, I've learned that the points are encoded as a texture where R,G,B contain normalized values of the X,Y,Z point data. Apparently this texture is used to set the worldspace offset of an emitted point. To see all the points, you sample the texture uniformly to get the R,G,B values at each sample and offset the emmited particles as mentioned.

To do the things I want to do with the cloud, I'm still not sure what happens next. There's not so much information about it online. The one example I came across is absolutely amazing.

Basically though, and this is a general pribnciple - The GPU recieves and processes data in the form of a texture. Any computation and so forth takes place at that level -in UE4 this means that the computation takes place in the material editor. My own lack of deeper understanding is gating me. I lack a parctical understandimg of:
- the Material Editor
- Materials, in general
- Material Functions
- the UE4 particle system
- Niagara

Obviously I've used all these systems before, but tbh I'm just a curiopus monkey and I'm still figuring out how to drive the starship.

Since this is becoming a "sprint review" here's my summary for the week

WHAT WORKED WELL
- The brief glimpse I had of Houdini convinced me that this is the only kind of 3D modeling I'm interested in. Its a completely different approach to 3D than I've encountered before. Procedural and rule based.
- Transferring the Arctic project to LOCUTUS
- Visual development for Arctic project
- collated visual ideas and art direction on a Mood board in Milanote
- visual research on Hello App (iOS) and Rez (PS4)

WHAT DIDN'T WORK WELL
- I have done more this week than I remembered, but I've kept it to myself.
- I am not engaging Yoann in the creative process I am enjoying
- have not been updating my design notes regularly
    + I want to use the material I'm capturing as source text for my case study about this project
- Treating each day as a "sprint" isn't helping with long term thinking. This isn't the only project I'm involved in.

HOW TO PROCEED
- Better collaboration starts by talking
    + discuss my weekly status
    - share Milanote board w Yoann
    - setup shared worksession for Saturday
- Planning & Strategy session needs to elaborate my ongoing projects and goals
- Return to using JIRA as a planning tool
    + add Futureworld as a project

2021-05-28 09:12
WHAT ARE YOU DOING RIGHT NOW?
x Writing up a summary of my deep dive into point clouds this week
x "sprint review"
x transferring some material from Hello LIDAR app on my phone to icloud

NEXT
collate transferred iOS material
add to Mood Board


2021-05-28 10:03
What are todays goals
- 1 minute of panoramic output from Arctic project
- Transfer one of my point clouds to UE4 using Houdini/Niagra workflow
- study UE4 particle system
- study UE4 Niagara system
- Chat w Yoann


2021-05-28 10:15
good reference for setting up a point cloud material at 3:38
This doesn't affect the RGB value of the point, only the primitive shape that gets drawn
https://youtu.be/VuQU9FiaVjY?t=218


2021-05-28 10:33
incredible web demo here
https://pcsb.quentinlengele.com/


2021-05-28 11:23
What are you doing right now?
I'm on LOCUTUS in the Artic project. I want to reorganize the material into levels so I can turn them on/off. I want to produce some animation from this project

Before getting into that, I'll do some study

NEXT
x study UE4 Niagara system
x study UE4 particle system


2021-05-28 16:26
I've learned a bit more about both Niagara and Cascade


2021-05-28 17:03
Houdini Niagara plugin UE4.26
https://github.com/sideeffects/HoudiniNiagara/releases


2021-05-28 17:19
I've confirmed (re)installation of the HoudiniNiagara plugin. I've (re)downloaded the demo UE4 project. The sample files also includ eth Houdini projects used for exporting to UE4


2021-05-29 11:00
Experimented with Niagara settings and UE4 display modes in the test project. Had some fun with it and added samples to mood board

Next
Continuing w Houdini Niagara tutorial

I’ll speak w Yoann at 1p. I want him to come by, take a look at the moodboard. take a look at Rez. 
Improvise, categorize, delegate.

I need him to take the lead on assembling the after effects template(s) we spoke about last week. I'm not as far along as I thought because I've invested time in point cloud animation and deep dive into the technology.

How soon is now? Next week I will add the project to Jira and establish a timeline


2021-05-29 20:21
Big step forward today in my understanding of computer graphics in the 21st century. If not that, then at least I’m seeing an animated point cloud in UE4. Finally! 
The journey to this outcome is both unexpected and hard won. All the study and hackir mindset of the last week has paid off. I gotta admit that for a while I was afraid I was wasting my time. I felt that way strongly earlier in the day when it seemed like I just was unable to get the results I wanted, or any results at all really.

Summary
- I captured a point cloud of Yoann with the lidar on my iPhone
- I imported that data into houdini and processed it before outputting a JSON file for Niagara
    - The problem I was having before turned out to be simple. I had to add a “life” attribute to the data so that Niagara would know how long to make the emitters active
- In Niagara I added a vector field module to the system and I am using vector fields that come with UE4 to direct the movement of the spawned particles
Some of the animation possibilities are mundane. Some are incredible. There are a number of sources for free and paid vector field assets, and I think I'll be able to create them in Houdini as well.


2021-05-30 09:23
I've started exploring another 3D scanning app on iOS. I forget the name at the moment, but it allows for many other kinds of exports, including textured geometry and has some built in editing features as well. 

I played with the parameters of the dynamic point cloud last night to stretch out the duration and so forth. I am seeing some glitching towards the end of the lifecycle that doesn't appear in the Niagara preview window. Maybe its a problem w particles hitting the bounding box? I'd seen something metioned about GPU collision settings as well?


2021-05-30 09:26
I'm processing the yoann3 scan and bringing it into UE4


2021-05-30 10:27
I think that scan may be pushing the limits. UE4 keeps crashing (out of video memory) when I try to use it. Rebooted to see if it persists. Either way though, the imported assets are going to need some simplified.

WHAT I WANT TO KNOW
- verify movie render queue to render video files
- verify panoramic output

2021-05-30 10:32
yoann1.hbjson:                  8.56MB
yoann3.hbjson                   51.5MB
yoann3-clean.hbjson:            42.5MB
yoann3-clean2-sparse.hbjson     5MB


2021-06-01 12:11
I've setup a JIRA project to track FUTUREWORLD developments. Yoann is coming by for happy hour later today and I want to do a bit of show and tell but also discuss workflow and some strategy. I'm limited on available time today but am working on verifying import and rendering of these niagara systems


2021-06-01 12:30
I'm reviewing the work I was doing on export from houdini to niagara. The sparse point cloud I exported is too sparse, but also came in upside down. Why?


2021-06-01 16:18
I'm doing some cleanup of the demo point cloud animation scene to show Yoann a bit later


2021-06-01 20:22
good meetup w Yoann. I showed off the fluid point cloud particle sim I've been working on and I think it had a great effect for both of us realizing we can do less than we thought. The particle animation IS the animation. Yoann shared some audio with me from a prior live performance that I'l;l be using as a reference.


2021-06-01 23:27
studying Niagara


2021-06-03 12:00
shared mood board w Yoann

WHAT ARE YOU DOING TODAY
FUTURE-21 Study UE4 Niagara system

IS THERE ANYTHING ELSE YOU CAN DO?
While I study, I can also work on:
FUTURE-5 verify movie queue rendering of UE4 point cloud assets

How much more study do you need? Are you OK with saying that FUTURE-21 will wrap up today?


2021-06-03 13:53
NEXT
I can use the Niagra system I've been playing with as a rendering test


2021-06-03 16:42
working on FUTURE-5 related task and verifying movie queuee output of GPU particles


2021-06-03 18:10
Working out some stuff with thee rendering queue that I thought I'd gotten figured out before. Why is my designated camera not being used? Where is my camera?


2021-06-03 18:26
Ah, there it is. gotta have a camera cuts track so UE4 knows what you want
Rendering 1080p at this quality level is rapid


2021-06-03 19:07
after a coule of variations, I've got the rendering workflow happening

NEXT
take a look at a high resolution rendering - tiled or otherwise


2021-06-03 23:24
I'm rendering out a 12800x6400 sequence. ETA 01:58:04
GPU load is very high
VRAM is almost entirely consumed 22.4/24.0GB

I don't need to render the entire sequence but I do need to see it working with particles filling the screen


2021-06-04 09:42
that high rez (non-tiled) rendering worked out just fine
I'm going to test out a tiled configuration and wrap up the investigation

I'm going to wrap up [FUTURE-21 Study UE4 Niagara system] after:
- complete the tutorial here: 
    - https://www.youtube.com/watch?v=ziwNVtOyKSU&ab_channel=SemSchreuder
- review the examples in the HoudiniNiagaraSetup project
- review the UE4 Niagara content examples


2021-06-04 14:56
switched over to LOCUTUS to get work started on [FUTURE-22 render Arctic scene flythru for Animatic]


2021-06-04 16:38
reorganizing material in Arctic project


2021-06-04 19:55
experimenting with the lighting and atmospherics.
couuld do so forever
I've got a much better impression of the space and am able to navigate it efficientlt now
how about working on some fly-throughs next?


2021-06-05 10:27
After messing around with the Arctic project I pushed too far, got sort of lost and wanted to make sure I was starting from the baseline I liked so much. So I created a new project for the Animatic production and putting what I learned to good use in making some tweks.

At the moment I've gotten a bot hung up on camera DOF. Have never seen it used. Not sure if its possible for Camera360, but feel its important enough to study this before moving on.

How about timeboxing it to an hour?


2021-06-05 10:30
Timebos: study UE4 camera dof

console command
r.TemporalAA.Upsampling 0

to add this value in Sequencer, you'll need to set it in the level blueprint
(which I've now done)

// does this also imply you're using temporalAA?r
consider adding the following to a movie render queue pipeline
r.TemporalAA.Upsampling 0

//are these just for raytracing though?
// Epic actually suggests disabling the denoisers if you render with high enough subsampling, aka 64+
r.AmbientOcclusion.Denoiser.TemporalAccumulation 0
r.GlobalIllumination.Denoiser.TemporalAccumulation 0
r.Reflections.Denoiser.TemporalAccumulation 0
r.Shadow.Denoiser.TemporalAccumulation 0


2021-06-05 13:20
running a test (raytrace-scenedefault) render at 1080p [ETA 47m]


2021-06-05 15:23
crane-test isn't that impressive.
- needs to be 2x longer
- dof is much too shallow
- camera


2021-06-05 19:41
combined a rail and a crane and got a nice, aerial camera move


2021-06-07 10:30
good session with Yoann yesterday. I did some scanning at his place. We looked at the material I brought over, and I got to hear him react to it live. A couple moments of serendipity. We talked about the editing process a bit, and we're both agreed on this broader heuristic:
provide transitions and small reveals in the enviroment like a DJ, then do one big reval where its another world entirely. A strategy of tease, tease, release, transcend.

Practically, for the Wintermute scene, this means rendering out multiple versions of each camera move I've setup, so that during edit we can transition to these versions or play other games with the 10 screens while maintaining consitent timebase

We also took note of how certain juxtapositions of footage worked together when we had them all playing at once. Its important to match camera moves with any other motion. If the camera is turning right, then the next view should follow that up by continuing to turn right, or rotate right, etc.

All motion needs to be continuous. Sharp cuts aren't what we want. We may find that dissolving between things has its own voice.

I've discovered a new scanning technique of following the subject while moving through a space. It creates a snakelike worldline for the subject while the enviroment remains constant. While reviewing the pointcloud I discovered that if you position the POV behind the subject and then move the camera through the volume, you will see the motion of the subject recreated as you move through each sample taken. It came by surprised and I'm eager to see it on the computer.

Earlier this morning I found an app that records pointcloud videos. It exports thee standard formats and I'm curious to see how that output works with the methods I've looked at for working w pointclouds in UE4. If I import that data w the LIDAR plugin do I get the animated data as well? Do these files work with the Houdini Niagara pipeline?

I deprioritized the Houdini Niagara data processing to work on Wintermut camera anim last week but would like to resolve any further questions I have about that process as well as know any limitations and workarounds.

TODAY
- continue working on Wintermute drone 3 sequence
    + goal: start a 5400 frame render of this material tonight

- organize my scans
- setup a UE4 project to review sequential scans
- install UE4 on MULE
- data processing for Houdini Niagara import

THIS WEEK
I want to tighten the loop and my connections with Recombinant Media Labs. I cant to show them some of the work I've been doing.

I don't want to simply share screenshots and movies on my phone, I want to give them a URL, which will also let me add some description for context.

What is the easiest way to do this?
- Confluence?
- Milanote?
    + would also allow me to share Futureworld Moodboard
    + what does Milanote look like when sent as a public link?

Milanote is a great solution.
I want to share annotated samples of the work I'm doing with Steve and Nout


2021-06-07 11:41
FUTURE-1 organize 3D scans


2021-06-07 14:43
oh that's interesting. The "animated" point clouds from that new app are sequences of .ply files. Unsurprisingly they are very storage intensive
(or seem storage intensive when exported as .ply sequences. Impractically so. On the phone they consume much less room. This isn't something I want to dive deeply into right now. Will pick up this investigation later


2021-06-07 15:04
I've transferred all my scans from my phone to ONYX. I'm doing a bit of review and organization. There's a lot of data here. I can't see it all at once. How can I narrow the scope a bit? Just giving these better names and getting rid of obvious chaff would be useful

I've started UE4 install to MULE, but needing to update Windows, etc first


2021-06-07 16:10
How am I looking on the Wintermute animation? I need 3+ hours to get that going




2021-06-08 13:09
There's been a change of plan. I just spoke w Yoann about it. Cinemachamber 2021 will be running June 24 with pre-existing content. The artists who were invited to show will be on the cinemachamber 2022 program. I feel so disappointed and broken right now, but I have to figure out my next steps. All this wasn't for nothing. I found something here. I was planning to document this journey as a whitepaper demonstrating social immersive content or something like that. but niow the game has changed and all my plans feel like they have come to nothing.

Looking at that promo and not seeing our names on it was a punch in the gut. I'm reflecting on that and realizing how much worse it would havee been to see our names on it. I would not be able to meet that date and was targeting end of July as plausible. Truth is though, the date was always unknown, and while I felt I had the freedom to "go with the flow" it was a red flag that there would be issues ahead.

Gary, real talk. I know it feels like something died and that you're feeling lost and alone. Its not the end of the story though man. Its the beginning. Creativity means having an audience. Creativity also means having a team. Yoann is on my team, and although at the moment I'm unimpressed by Nout and Recombinant Media Labs, I know he's only doing what he has to. He (or at least his setup) can still be on my team giving me the opportunity to document the work in this space

I'd like to see what the point cloud material looks like in that space, and record it for my documentation. I can make that happen if I reach out to Steve today. How soon can I have material prepared though? Could I have a sequence rendered out by Sunday?

Put another way: what needs to happen to have material ready to show in the space on Sunday?

output is: 360 degree sequence of point cloud level design/animation 
unknowns:



2021-06-08 13:33
not related to the psychodrama but yesterday I started collating my existing scans and posting screencaptures and video to a new Milanote board.


2021-06-08 13:45
for purposes of the whitepaper I'll also examine the use case of reality capture from videogames (photogrammetry from video capture)


2021-06-08 13:52
x I want to contact Steve to setup a time for demoing some material
P2 I want to schedule the work around making a deliverable of new material for this weekend
P3 I want to continue reviewing the scans I've made


2021-06-08 16:26
I spoke with Steve. They're doing some calibration and setup at Gray Area, but he expects they'll be open after Wednesday for work to be viewed. He'll get back to me w details


2021-06-08 16:28
what needs to happen to have material ready to show in the space on Sunday?
P1 I need to setup a UE4 project for the demo
P1 I need to know which assets I'm using
P2 I need to reliably bring in point clouds for animation in Niagara
P2 I need to verify the panoramic rendering pipeline w Niagara pointclouds
P3 I need to place metrics in the scene to guide composing for the aspect ratio
P3 I need to setup a sequence where the POV follows the subject of a sequential cloud


2021-06-08 17:35
- make all the imported clouds have same alignment and position during Houdini processing
- how can I show RGB values of each point?


2021-06-09 09:06
I processed some candidate scans for processing w Houdini. Cleaned them up statistically, cropped content and aligned to grid. Let's do this.


2021-06-09 11:50
I'm getting Houdini environment setup correctly.


2021-06-09 12:32
I've organized Houdini better.


2021-06-09 13:06
new7 asset is upside down. correcting in Cloud Compare


2021-06-09 13:15
corrected that asset's orientation. Ah damn it, no I didn't I was looking at the wrong Houdini output


2021-06-09 13:55
exported new7.hbjson 39.3MB 981855 pts


2021-06-09 16:05
I'm working with some of the Houdini Niagara material I'd studied before. Taking a look at how the emitters work. I'm noticing how GPU and CPU emitters spawn a bit differently.


2021-06-09 16:39
What I'm not understanding is why particles in this basic emitter:
- don't seem to have an independent spawn rate
- spawns particles that flow from the origin to the emitter

looking more closely, the particles do spawn from the emitters as expected the first time thru the lopp, and subsequently spawn from the origin


2021-06-09 16:46
part of the problem is that I still don't really understand Niagara'


2021-06-09 19:19
making some progress. I'm able tp make forms persist and build in a more controlled manner.


2021-06-10 08:15
Spent yesterday in a dep dive wit Niagara trying to understand how I could control some of the Houdini point cache demo samples. I got much further than I was before and also came across an interesting tip

https://mycgdoc.com/Houdini-UE4-Niagara-04f372491ef84fbf811fb943fa2c1dad

the point cache system has a MaxSampleTime variable (the length of the Houdini rendered sequence in the cache) that needs to be correlated with emitter LoopDuration under emitter update.

    Particle color updates seek vector4 data types, which include an alpha channel, but this is not included in the incoming point cache asset's vector3 color. To address this, use the drop-down menu next to the parameter input and select an option that allows for splitting the vector4 into a vector3 + float as separate values.

    Example: The Color module added to the Particle Spawn section has an option to Make Linear Color From Vector and a Float. With this setting reassigning the vector via the drop-down menu will access the Houdini color attribute as a vector3.

The same source also had advice on how to use the color values in the cache, as well as including Houdini's pScale value in the render to JSON.

    Example: The Color module added to the Particle Spawn section has an option to Make Linear Color From Vector and a Float. With this setting reassigning the vector via the drop-down menu will access the Houdini color attribute as a vector3.


2021-06-10 10:20
completed OPS-50 install UE4 on MULE
I installed this on my 3rd machine to open up capabilities of network rendering, ndisplay, and pixel streaming


2021-06-10 11:16
spent time doing strategy and planning with JIRA . Cleaned up my dashboard. Added Tempo app for planning and time tracking

NEXT
apply the new information about point cache MaxSampleTime to yesterdays work. Is it now less chaotic?

THEN
import new7.ply point cloud
- any issues with the number of points here?
- is there an upper limit for the number of points that can be imported into a point cache?
- is there an upper limit to the number of points Niagara can display (CPU/GPU) from a point cache?


2021-06-10 13:52
after some hacking around I found a way to correlate emitter loop duration with the cache length. It works. The behavior at the end of the loop now causes the particle field to expand forever though. 


2021-06-10 16:34
I think I know about as much as I can from this Niagara study session. Feeling a bit more comfortable in the system. Pleasantly lost. I did achieve the engame I wanted, but now the sampel shape expands infinitely once the pointcache has been read.

I'm going to step through the 6 minute Niagara tutorial I've wanted to complete. Maybe there's some last thing I can know


2021-06-10 23:07
I spent most of the day studying Niagara and have taken it so much further than where I was earlier this week. Frim doing what I thought was a basic tutorial I came across a simple method of using the (normalized) diustance between the camera (or any other point) to ramp between colors of a sprite. I realized I could apply this to particle scaling so that particles wouldn't appear to grow larger when you got close to them. I implemented that in a few minutes and while it could use some refinement, the basic idea is realized, and it looks so coolr.temporal


2021-06-12 11:20
updating JIRA planning
Steve Pi got back to me and mentioned theres an opening 12-2 on Sunday. I won't be able to hit that target. The scope of learning different systems and workflow, specifically Niagara has been an order of magnitude more involving than I thought. Its nothing to be ashamed of, but you need to acknowledge the cost of learning/playing/research

I asked Steve if there would be availability at the Gray Area space later next week or weekend. He wasn't certain, but confirmed that the installation will remain up during July. Still - it seems like it might be up in the air a little bit, and my own priorities have me there sooner than later.

Its worth taking some time to reflect on my Team. I'm not really sure what I mean by that, but its a realization emerging from the corollary to my statement that Creativity means having an audience. Specifically, Creativity means having a Team.

Who is my team?
Steve Pi
Yoann
Thea
Ruwan


2021-06-12 13:31
completed some JIRA cleanup and work updates
starting my worksession now


2021-06-12 14:14
I'm stepping through an audio reactive niagara tutorial. For some reason my setup at the beginning doesn't match what I'm seeing on screen. The scale mesh size module doesn't work at all? Examining

Particle Update
Maintain in Camera Particle Scale
this seems like an automated and refined implementation of the mechanic I discovered to change particle size by distance from particle to the camera


2021-06-12 14:29
OK I got it. The mesh particle wasn't initialized after spawning


2021-06-12 15:33
I created a niagara system that reacts to audio!
Playing with it


2021-06-13 16:07
Good meeting with Yoann today. We're on the same page about how to proceed. Big picture
- interactive workflow
    + OSC input
    + audio input
        * prerecorded
        * live
    - dedicated machine for pixel streaming
- figure out how to best utilize access to gray area
    + how does audio work in the space
- use Slack for communication hub


2021-06-13 17:14
I setup a basic Slack workspace which I scheduled time tomorrow for a bit of refinement before inviting Yoann


2021-06-14 13:02
I did some cleanup, planning and population for the Future World Slack before inviting Yoann to join. Just sent invite


2021-06-16 13:16
imported new7.hbjson into UE4
98155 points
1 frame


2021-06-16 13:40
success!
I've also brought in the RGB colors from the scan

A couple of questions:
- I had to set a reference to the Houdini Point Cache I'm using a few times in the tutorial module. How can I set that  system-wide? (I'm only working with the emitter at the moment)

As before, using GPU sim, the point cloud starts expanding after time 0. Is that just of using a constant value for sampling AGE. Is that module even necessary for my purposes?

Onb Initialization, a number of particles are spawned from the Houdini point cache. They have a lifetime. When the particle updates, nothing should change.


2021-06-16 14:37
I may have scaled the pointcloud too large by an order of magnitude or so


2021-06-16 14:47
I've rexported new7.hbjson 10x smaller


2021-06-16 14:57
still gigantic when viewed in the environment
exported from Houdini with no scaling this time


2021-06-16 17:57
The 1x scale is maybe a bit too small?
However it's also possible to change the scale by changing the age at which the point cache is sampled (it expands outward when there's only a single fram eto sample from)

- why does the point cloud disappear sometimes in the UE4 camera view?
- theres' something about the looping and/or particle lifetimes that I'm not quite understanding.

- how does the life value exported with the data relate to the particle.lifetime value?


2021-06-17 00:26
I studied some of the Niagara content examples and have a greater understanding of emitter looping and lifetime. Some of it is qite non obvious, but simple enough. I also learned some methods for manipulating niagara actors in a level sequence. I learned that I can add user parameters to a niagara system and keyframe those values from sequencer, which is great! There's a lot that can be done with blueprints of course, but thats not my level of engagement right now, as I remain under the constraint of rendering out cinematic ocntent rather than creating interactive content


2021-06-17 00:56
I've rexported the new7 point cloud with a scaling factor of 10.

This was a good session. I'm now able to treat the Niagara editor timeline and the sequencer timeline the same. I'm able to scrub thru niagara system age in the sequence. I'm also able to set up the Niagara system/emitter stat to loop for the duration of the component lifecycle sequencer track. Any emitter looping I setup in the Niagara editor loops continually in the sequencer for the duration of the timeline. Its very flexible to change things up this way.
I think I can apply everything learned here back to the point cloud asset next session. Great work man.


2021-06-17 01:13
holy shit, the point cloud is melting just the way I wanted. I'm so amazed and happy


2021-06-17 14:45
I'm doing some research on particle materials and adding new material types to the project


2021-06-17 15:41
Wasn't really able to figure out the example the unreal docs give for particle radius. Maybe look into why later.
I've added a user parameter to pointclous_sys that I'm using to drive the pointcache custom age value, and using that behavior as a scaling factor. It exploits the behavior of GPU particles with the hN system. Its pretty useful that for cached assets without time values, incrementing the age causes the space between the points to expand. 


2021-06-17 16:40
Ive setup a basic level sequence for inspection . Putting some of what I've learned of materials to the test. When I step back into this I want to take a look a positioning noise fields, and using vector fields.
- can a vector field be placed external to the niagara system and affect it?
- can the curl noise force be positioned or localized so it doesn't affect the entire cloud at once?

2021-06-17 16:50
looking at the ambient occlusion view of this scene w larger 1-sided particle sizes really brings back the solidity of the model. Maybe something like this is behind the various shders I've admired in Cloud Compare and Meshlab


2021-06-18 13:24
doing some material testing with lights in the scene
Today I want to step out of explorer mode and do bulk import of the 3D scans
closing out


2021-06-18 17:40
sspent a few hours experimenting with materials and lighting hacking around actually. pretty much what I said I wanted to avoid doing. Even so, I've refined my basic point cloud material to the limit of my understanding, which is great. I still want t5o duplicate some of the shaders I'd seen elsewehere

I'm going to regroup and start the dataprocessing for my scans


2021-06-19 14:06
I'm looking through scans, deleting some chaff and bringing them into cloudcompare


2021-06-19 15:08
using Meshlab to work with yoann-home_sampled_hirez, which I'd previously processed to extract a 10^6 point cloud from the ARKit mesh I captured of Yoann's place. Its kind of slow goung. feeling like I must be missing something basic. How is it I can't immediately switch to a fron/left/top orthographic view oriented to the global coordinate system? Spending a lot of time tweking that by hand.


2021-06-19 15:22
oh there is a way to snap to standard views. Window>View From
Glad I checked, as this model is oriented improperly
Actually no - it isn't it's oriented with Z-UP


2021-06-19 16:08
Having aligned the model, how do I make the transform stick? I tried exporting
ah... There'sFilters>Mesh Layer>Matrix:Set from translation/rotation/scale


2021-06-19 16:33
I am really liking the effect of using the camera clipping plane to reveal successive slices of the cloud. Similar can be done with a Lidar volume for that content pipeline. I'm sure its possible w Niagara as well, although not yet certain how


2021-06-19 16:46
screenspace ambient occlusion looks good on these clouds. I wonder how to duplicate the efect in unreal?


calculating AO using the mesh normals is taking a very long time. will probably halt. not sure if these colors are saved into the verts? Trying again. I can see its computing on the GPU, butvery slow. not practical


2021-06-19 17:22
these clouds can be sliced up into as many sections as I want... Hadn't considered the posibility of that. Maybe will look into it a bit further?


2021-06-19 18:59
doing some clenup and organization in the UE4 project to bring in scans


2021-06-20 01:51
Slow going today, as I was examining the details of a larger kind of import and experimenting a bit with the data processing. Lets see if I can get a good cadence going tomorrow


2021-06-20 11:07

Houdini is seeing bad data in this export.
yoann-home_sampled_hirez-aligned.ply

Houdini doesn't import .e57 files

renamed as loft.ply
retrying w ASCII encoding .ply with all non vertex flags in meshlab turned off


2021-06-20 11:18
noticing these smallish values in the export
-2.077061 2.066123 5.255773 
-2.098372 2.067847 5.258376 
-2.07387 2.080254 5.257646 

I'm going to do an alt version scaled up in meshlab


2021-06-20 11:50
taking a better look at the data. It does appear small in Houdini,
Houdini aslo seems to expect Y-UP instead of Z-UP


2021-06-20 18:23
worked out soem structural details of exporting and alignment ans scale. the new7 point cloud seems much too large compared to the reference mannequin. Lets see wht the loftz pointcloud looks like upon import


2021-06-20 18:36
the loftz asset has come in overly large I think


2021-06-20 18:44
OK, worked out the scaling factor from Houdini (10x, not 100x)


2021-06-20 18:57
success with the new import to be honest it looks a bit sparse. Would it be possible to reprocess this mesh and sample 2M points instead of 1M


2021-06-20 19:43
Its definitely sparse. Will address later after further imports. I thought I'd have worked through more of these by now. But I guess there were still some unknowns that I had to work out for the efficiency


2021-06-22 12:02
I exported scan13_4M.ply for testing in UE4 with
Houdini/Niagara workflow
Lidar import worklow

I was feeling bad yesterday that this seems to be taking so much time, but I'm learning as I go. I've never done this before, and I need space to understand. However I've mistakenly fixated on the viosual appearance in MeshLab or CloudCompare. Let me focus my attention better. Any rendering outside of UE4 is only useful for documentation, and the meshlab project file can be revisited later.


2021-06-22 23:52
The lidar plugin import works just fine. The controls are pretty different than houdini niagara

GPU runs out of memory when trying to import the same data into Niagara.
How about if the clud was sliced up into parts, then each part was imprted seperately as a seperate houdini pointcache with a dedicated emitter, and a Niagara system was used to recombine the assets?

That's a cool technique. Was thinking about it earlier as a way of triggering animation on different parts of a cloud. 

For this scan however, I want to dive further into what the LIDAR plugin can do. I don't have to do the UE4 work right now. Best thing to do is to keep processing the data.


2021-06-23 11:06
I want to take a look at how the clipping plane volume can be used on Lidar point data in UE4


2021-06-23 12:32
Steve Pi reached out to me and mentioned that with performances running, Mondays & Tuesdays will be open to artists.

NEXT
- schedule session next Monday
- confirm w Yoann


2021-06-23 12:33
I've exported a few more large assets
soma-bigscan_3.4M.ply
soma-bigscan_3.4M.e57
soma-bigscan_1M.e57
soma-bigscan_1M.ply
bigscantest-x.fbx


2021-06-23 15:05
Steve Pi texted me to let me know that now the exhibition is happening at Gray Area, the space will be available to artists on Mondays & Tuesdays only. I asked him if we can set something up on Monday. He said he'll get back to me soon. If I don't hear from him today'll I'll follow up tomorrow. Looks like there's a target again for my journey


2021-06-23 15:18
cloudwalker-1_4_5M.e57 is too small
the transforms were misaligned when bringing into the Lidar plugin
this means that the Houdini/Niagara plugin assumes a different orientation than the Lidar plugin.

My Houdini project is setup to export Y-Up, looking towards the negative Z-axis
When the Niagara system is placed in world at 0,0,0 0,0,0 it orients as
Z-Up, but I am looking towards the positive X-axis

The normalized orientation I want for each of the cloud assets is:
Z-up, 

This is the default transform and orientation I want for each of the point cloud assets. This is the front view:
Z-up, facing +X axis

Houdini assets need to be rotated 90 degrees around the Z-axis to conform to that standard


TO-DO
- conform exports for Houdini/Niagara to normalaized orientation


2021-06-23 18:43
reprocessed cloudwalker-1_4.5M-n and it looks as expected when imported to UE4

taking a look at soma-bigscan
all of that will need to be reoriented I think


2021-06-23 20:19
processed soma-bigscan
resampled at various vertex counts to see if I can also create a niagra system from this large area

updated Houdini project
re-exporrted new7.hbjson


2021-06-23 20:51
holy shit this looks amazing


2021-06-24 14:40
Having imported some scanned content with variety I have a better sense of how long it takes to move stuff into UE4. Lot of that time was spent familiarizing myself with the options, but admit to being fascinated with the various shading options and views

I have a good enough testbed to verify how this works with Camera360
FUTURE-6 · Verify panoramic workflow with Niagara point cloud assets


2021-06-24 15:00
added Lidar clipping volume to the cloudwalker scan. Nice.


2021-06-24 15:14
oh how interesting. The volume clips all instances of Lidar plugin point clouds. They can only be differentiated by priority


2021-06-24 16:04
More interestingly though, reading thru the lidfar pludin docs, there are some interesting console variables
Including r.LidarIncrementalBudget, which progressively draws surfaces, as if streaming them in. 

It gives everything an "active" effect, and seems to help performance in the viewport as well, as lidar point clouds don't fully resolve until such time as they fully stream in


2021-06-24 16:26
if I'm not mistaken, that Minimum Screen Size parameter might be the distance culling I was expecting?



2021-06-25 11:53
I'm taking a closer look at the lidar point cloud settings and methods.
One thing I'm finding is that very bright values aren't so great looking unless they're an emphasis. The average luminosity needs to be at 0.5 or lower


2021-06-25 15:37
There are a number of variables to consider for the character of various point cloud renderings
the opacity mask on a particle
the luminance of the material on a particle
particle size

How to implement world space textures on lidar clouds or niagara particles?



2021-06-25 19:04
I've succeeded in a small way in applying worldspace textures to the point cloud. From ideas here


2021-06-25 19:14
oh here's something interesting M_LidarPointMath material test


2021-06-26 11:01
taking a look at how multiple lidar clipping volumes affect the point cloud.
taking a look at how blueprint work with the lidar plugin


2021-06-26 11:31
demonstrated ability to address a pointcloud in the level and change the point size. left the code in the level blueprint for later reference.
 brief description of the blueprint interface here
 https://docs.unrealengine.com/4.26/en-US/BlueprintAPI/LidarPointCloud/


2021-06-26 12:09
taking a quick look a UE4 tutorial on Material World position


2021-06-26 13:19
A little bit of knowledge goes a long way. I have a very complicated material in effect right now that is appplying a texture to the point cloud in worldspace. I've had success applying a flipbook as that texture as well, and at the same time, using the world position offset to animate a sine wave through the texture, causing the point cloud to move rhythmically. Its sort of amazing actually. I also tweaked the lighting of the scene by adding another postfx volume., specifically for color grading. And... finally, exaggerated the screenspace ambient occlussion to provide better depth.

The scenario I've been working thru this morning is a "fat pixel" approach. Everything is very chunky, and satisfying




2021-06-26 13:36
SO MANY PARAMETERS
getting some nice results with whatever this material is, by incorporating masking


2021-06-26 16:24
discovered method to have masked points dissolve when camera passes through cloud using Pixel Depth input


2021-06-26 17:24
I can't even believe how cool this material, and the techniques I learned have turned out. What I'm seeing looks so organic, structured and chunky and organic at once.


2021-06-27 14:34
I finished the World Coordinate tutorial and learned a method for applying a texture in worldspace to X,Y,Z axes. Previously I'd looked at the (simpler) usecase that returned X,Y, X,Z, Y,Z
https://www.youtube.com/watch?v=8aYe54XrZYI&ab_channel=MathewWadstein


2021-06-27 16:00
the worldspace mapping method for objexts works fine, but the material doesn't seem to translate to the lidar point cloud planes. May have to do with the nature of these particles - they're always facing the camera


2021-06-27 22:02
The DOF example provided in the camera 360 tutorial isn't working. I've sent email to the developer for further instruction. I see that UE4.27 preview2 is available, and I'm downloading it in the background. 

Apparently some improvements to pixel streaming - a cloud based solution?

Share all of your progress with anyone, anywhere via the cloud with production-ready Pixel Streaming.

LiDAR Point Cloud Plugin Improvements. Unreal Engine 4.27 brings several enhancements to the LiDAR Point Cloud plugin that improve the import and manipulation of point cloud data.

    Better Point Size Algorithm. The scalable algorithm has also been improved and a fixed point mode has been added. This new mode can be especially useful when working with a noisy asset.

    Improved Performance and Stability. Several improvements to the processing and streaming of the point cloud data have significantly improved performance for the end user.

    Improved Save/Load Performance. The serializer and streaming mechanic has been significantly improved.

    Simple Gap Filling. Points are enlarged and rendered using a new technique that minimizes visible overlap.

    Disable Frustum Culling. It is now possible to disable Frustum Culling which can help with the data stream delay when shooting cinematics.

    New Selection Methods. New Polygonal, Lasso, and Paint selection methods have been added.


2021-06-27 22:47
no problems w cam360 demo scene at 1920 x1080


2021-06-27 23:41
some apparent issues with lidar point cloud and camera 360. I wasn't seeing all or many of the points in the panoramic view and was unsure why. There's no good reason for it, but adjusting the perspective view seems like it may have resolved the issue? All I did was rotate the scene until it all resolved correctly. This also works with whatever camera is displayed by the viewport. I don't know why there'd be any relationship there at all. However the output I'm seeing in the Camera_rec_360 view appears valid. Seeing how this renders. I've reset the scen so that the main camera is travelling on a rail, and the camera_point_360 object is attached to it


2021-06-27 23:49
A quick rendering test reveals what looks to be questionable output
GPU memory usage is 21.6/24.0 GB
5hr render time for 1800 frames

I don't understand the output I'm seeing. What can I do?
If there's a way to disable the LOD system, that might help
UE4.27 seems like it has greater flexibility with this

The problem might be that the particles are all trying to face the camera, which may be indeterminate now. What if they orient to the point normals instead?


2021-06-28 00:23
I've included a lidar pointcloud volume to maybe restrict the number of points to display. The output still looks bad. No apparent difference. However I'm rendering locally and GPU usage has dropped to
4.3/24.0 GB. Rendering times (at 1920 x 1080) are much more reasonable with 1800 frames estimated at 6min


2021-06-28 00:25
Both pointclouds were setup to face normal. I've change dthem both to prefer facing camera/point shape square


2021-06-28 00:31
The thing is - I'm seeing a correct view in the viewport pictur ein picture. The renderer is where things go wrong. I've switched to 360 Mono projection (1 camera) variant to see if this makes a difference


2021-06-28 01:12
Oh here we go... After hacking around I changed the project setting for Node Grid Resolution. Shifted it up from 96 to 4096. Now I'm getting the expected results. At 1920 x 1080. What about at a higher resolution?


2021-06-28 01:17
output at 12800x6400 looks good. Need to see it in After Effects to evaluate further. I think I'm winning?


2021-06-28 01:25
looking at the output, its possible that the camera isn't moving. 


2021-06-28 01:30
I kicked off another render to inspect in the am.

GPU 15.7/24.0 GB
ETA 4h

its likely that the camera isn't moving, but at least I'm seeing the point cloud

(the camera was moving after all - the renderings worked out ok)


2021-06-28 12:44
FUTURE-36
I'm setting up the UE4 project on LOCUTUS
I'm debating whether to use the NAS as a shared folder, or make a copy of the project for transfer to LOCUTUS. If the network speed feels ok to work with, I'll use the NAS as a shared folder. I'm just not sure how UE4 will react to assets changing. Would be a great time to enable multi-user support. I'm curious to see how much of a difference it would make.

Each computer that you want to connect to the same Multi-User Editing session needs to have the same version of Unreal Engine installed.

Each computer also needs to have a copy of the same Unreal Engine Project, each with exactly the same content.
- which means copying the project file from ONYX to LOCUTUS
- The typical way to achieve this is to store your Project in a version control system such as Perforce, Git, or Subversion, and to sync every computer to the same revision or changelist.
- The Multi-User Editing system doesn't absolutely require you to use source control. You could simply copy your Project folder from one computer to all the other computers that you want to join the same session. You may find this useful for initial testing of the Multi-User Editing system. However, avoid relying on this approach. Using version control effectively within your team is the safest way to maintain and share your Project content.


2021-06-28 12:56
For the moment though, I'll create duplicates of the maps & sequences I'm working with, so that each machine's changes remain independent. I can copy/past into these as needed.


2021-06-28 13:19
doing some project cleanup and setup for usage w 2 machines


2021-06-28 15:53
maybe I had it all backwards last night? The project settings for lidar plugin content need to be low values, not high ones. 


2021-06-28 16:02
I'm doing a 1920 x 1080 test for the updated project settings


2021-06-28 16:51

Project Settings -> Plugins -> Lidar Point Cloud
Octree
    Duplicate handling:  ignore
    Max Distance for Duplicate: 0.0001
    Max Bucket Size:    (200)
    Node Grid Resolution: (96)

Performance
    Multithreading Insertion Batch Size:    (500000)
    Use Async Import:   (TRUE)
    Prioritize Active Viewport: (TRUE)
    Cached Node Lifetime:   (5.0)

IO
    Use Compression:    (TRUE)


r.HLOD 0
r.LidarPointBudget 10000000
r.LidarBaseLODImportance 0.1
r.LidarIncrementalBudget 0
r.LidarScreenCenterImportance 0


2021-06-28 17:08
I've also turned off the HLOD system in World Settings
ok the output from the CineCameraActor1 is clean (was this setting what I was looking for all along??? 

Current data for soma-bigscan_3.4M is:
node count: 1597
data size: 53MB

I reimported the data to be certain, and yeah - those are the values for the plugin defult project settings


2021-06-28 23:45
The Lidar point cloud Rendering section contains a parameter called Bounds Scale. I've had some success (cleaner rendering) when this is larger than 1


2021-06-28 23:44
I've constructed these animations for demo:
lidar-pointcloud-review-ONYX
lidar-color-y

soon:
cloudwalker
scan-preview-sandbox

next:
verify hirez rendering on ONYX for
- lidar-pointcloud-review-ONYX
- lidar-color-y

transfer project to LOCUTUS

verify hirez rendering on LOCUTUS for
- lidar-pointcloud-review-ONYX
- lidar-color-y


2021-06-29 00:49
cleaned up 1500 frame loop for lidar-color0y
it looks amazing


STATUS
- lidar-color-y
    + default
    + fog


   
2021-06-29 01:12
ONYX: lidar-color-y at 2160x1080 looks good


2021-06-29 01:18
ONYX / lidar-color-y / color-y / Panoramic-12800x6400
rendering time for 1500 frames:
2:45:00





2021-06-29 01:43
I've copied the project to LOCUTUS
rendering lidar-color-y
    + default
    + fog

saving the output to ONYX desktop

LOCUTUS / lidar-color-y / color-y / Panoramic-12800x6400
rendering time for 1500 frames:
7h


2021-06-29 01:54
output from LOCUTUS looks good.
should be done by 9a


2021-06-29 02:28
I'm taking a look at the lidar-pointcloud-review renderings completed yesterday in After Effects

The plan is to get those renders processed to the cinechamber format 

Tomorrow am, I'll render out a Niagara sequence. Hopefully no surprises and a quick render

I should be able to get everything processed in After Effects in an hour

by 10:30a I hope to start packaging up the material I'll bring to Gray Area


2021-06-29 02:58
Render Garden is so great. Very satisfying to see it working so hard, and so conveniently.


2021-06-29 03:01
When the AFter Effecs job finished I'm going to kick off
lidar-color-y
    + fog

That way I should have both of them available in the am 


2021-06-29 03:17
That After Effects job is taking a while
4/10 of the v2 sequence complete
0/10 of the v4 sequence complete

at 5 min/screen it will taka about 1.5h for the AE job to complete. Perhaps I can kick off the UE4 render when I wake up in a few hours

Great work today. You got a lot done.


2021-06-29 09:01
LOCUTUS / lidar-color-y / default should be completed in 30m

I started LOCUTUS / lidar-color-y / fog on ONYX but am surprised to see the ETA of 10:31:00. Regrettably this version won't travel w me.


2021-06-29 10:12
collating files from LOCUTUS/lidar-color-y.color-y.v001[1497]

LOCUTUS did an amazing job with this rendering. I watched each of its systems working right at the limits of their capacity. Especially system RAM. It must have been paging from SWAP at a high frequency. Very proud of this machine. I was 50% certain the render would crash overnight, I find myself wondering how to upgrade and maintain LOCUTUS
- could the RAM be upgraded to 64GB?
- could the RAM be upgraded to a faster configuration?
- fan replacement?
- could the CPU be upgraded?


2021-06-29 10:45
FUTURE-38 package video assets for transfer to cinechamber
processing lidar-color-y.color-y.v001[1497]to format
I'm going to get a Flash drive set up, and take a look at what may already be on there from last demo


2021-06-29 11:02
Messaged Steve that I'm running late will meet at 1230
Departing here in 1h


2021-06-29 11:14
Ah, neglected to double check the paths of the AE render. For a moment was concerned some material didn't render. Is all good.


2021-06-29 11:40
AE processing is completed. taking a look at previous demo transfers


2021-06-29 12:18
revised ETA at Gray Area is 1p, spoke w Steve

External Hard Drive:BLACK is ready
copying to Flash Drive:Samsung USB
- ah that only has the animatic stuff. what about the other Flash Drive?
- ah damn it. that has Ubuntu on it


2021-06-29 12:22
copying BLACK -> Samsung USB
eta: 3m


2021-06-29 12:30
heading to Gray Area
- be sure to capture 3D ARkit mesh of the environment
- dont rush


2021-06-30 12:00
So I did forget to make a 3D scan, but plan to return next week and subsequently. It would be pretty great to show cinechamber on cinechamber.

I'm very happy with the consistency, clarity and scope of what I documented yesterday. Even As I was there I realized that I still hadn't seen the work because I was so focused on capturing it. Think about that.

I want to do some audio focused sessions. Hilariously sent Naut a casual stream of consciousness text intended for Yoann. I'd like us to get together for an audio-focused worksession

I want to ask Steve how the Touchdesigner XML config can be applied to the audio setup at Gray Area.

    <module name="lidar-v2" path="D:/modules/FutureWorld">
        <effects>
            <effect name="delay" frames="0" direction="0"/>
            <effect name="scale" scaleX="0" scaleY="0"/>
        </effects>
        <screen number="1" file="../lidar-v2_screen-05_H264.mp4"/>
        <screen number="2" file="../lidar-v2_screen-06_H264.mp4"/>
        <screen number="3" file="../lidar-v2_screen-07_H264.mp4"/>
        <screen number="4" file="../lidar-v2_screen-08_H264.mp4"/>
        <screen number="5" file="../lidar-v2_screen-09_H264.mp4"/>
        <screen number="6" file="../lidar-v2_screen-10_H264.mp4"/>
        <screen number="7" file="../lidar-v2_screen-01_H264.mp4"/>
        <screen number="8" file="../lidar-v2_screen-02_H264.mp4"/>
        <screen number="9" file="../lidar-v2_screen-03_H264.mp4"/>
        <screen number="10" file="../lidar-v2_screen-04_H264.mp4"/>
        <audio channels="2" file="../ApollointheClouds2.wav" preset="51"/>
    </module>

What are the possible values of the audio channel block?


2021-06-30 17:46
rolling back to an older driver
constant corruption of dropdown menus, where the content just disappears
apparently this resolves?


2021-07-01 02:24
rolling back the driver was the solution


2021-07-01 02:24
spent quality time working with a niagara sequence. Reorganized project as layers. Doesn't look like there are any issues w panoramic rendering. Running a render now. testing antialiasing strategies as well, as I felt the output last time was a bit soft.


2021-07-01 02:32
initial attempt rendered black screen. Perhaps the gPU particles need to warm up first?


2021-07-01 02:33
2nd attempt is producing black frames. will debug in the morning


2021-07-01 16:37
It took me a while to get back to something of the quality I reached last night. Lost those edits as the project wasn't archived. I'm explicitly doing so now and will return to this a bit later. Still want to know what's happening with the rendering


2021-07-01 22:32
OK, now its happening. Theblack frames previously seen may have been "warmup" frames requested by the GPU. Have noticed that the actual render doesn't start until frame 24 or so


2021-07-01 22:42
kicked off a hi-rez rendering w 32 spatial sammples for antialiasing
I'm guessing there are command line options that might serve my needs better. The rendertime has become lengthy with these settings. Will let it run overnight though.

ETA 12:45h


2021-07-02 14:56
sooo. that rendering sucked. Black frames. I am not sure why. Maybe related to image resolution? The low res test I did yesterday worked. Let me double check that however.


2021-07-02 15:04
transferring the material I captured earlier this week to the project archive. I'd played around with this on AppleYV. The photostreaming functionality sort of sucks. Looks like everything has been resampled and compressed. Is this a setting to "save Space" that I can turn off? I was adjusting the TV tring to make the best of the image quality. Then I tried streaming it thru airplay, and was surprised by how much better it looked. More or less the way I saw it on my phone. Naturally, I am curious to examine what was "really" captured on my workstation.


2021-07-02 15:31
There's a different workflow for importing iphone 4K HDR Dolbyvision. Installing Premiere to see for myself.


2021-07-02 16:03
the image quality is significantly better in Premioere
also I can playback the footage in realtime, where after effects wants me to playback a rendered cache
I'm doing a test rendering for import into after effects to see if there'es a difference. The goal is to copnverty it from HDR to SDR


2021-07-02 16:17
export is through media encoder. Running a test now and stepping back into UE4


2021-07-02 16:59
I'm not really seeing a difference in After Effects. Once the colorspace is converted in Premiere it looks exactly like an import of the file into After Effects, which I'd do by default. It definitely looks better in Premiere as the color space has been designed for it, and the additional benefit is realtime playback (among others)


2021-07-03 09:31
Successful rendering from Niagara ssystem at last. Not sure what made the difference however. Evolved and hacked my way to a truly weird emitter program that incorporates camera position for... something.. and somehow managees to feedback on itself. That's what I rendered out and I'm super interested to see how it works spatially. Due to the feedback loop, its not especially performant and slowed ONYX to a crawl as it tried computing in realtime. 


2021-07-03 12:47
revisiting the cinechamber project for the first time is interesting
There's a sandbox I made with weird multiple placements of yoann3 point clouds.
My demo work hasn't really explored this possibility yet
I'm integrating last night's [exoholo-loft-v015] render for previewing


2021-07-03 13:12
some problem w cinechamber import. Traced it down to the source files? or so it seems. I'm getting a message that the assets I added are invalid?


2021-07-03 13:16
as. its working. bad path name
this video looks great. wow


2021-07-03 15:47
Some interesting experiments with mapping different movies to different screens. creating fragmentary cohesive spaces instead of a single one. super interesting. The sequencing could be done with After Effects 


2021-07-03 15:48
I'm going to take a look at the wintermute scen on LOCUTUS
I want to get the network addressing matter worked out:

ONYX:

LOCUTUS is shareing its local D:\Users\Gary with me:
I've mapped that share to X:


\\LOCUTUS\G


2021-07-03 21:10
taking a closer look at getting file sharing working right


2021-07-04 01:08
I was able to solve filesharing issues
rendering out an earlier variation of exoholo-loft. 
examining effect of temporal sampling
increased cam360 outputsize from 6000 to 8000
ETA 6h


2021-07-05 15:42
I considered contacting Steve Pi and seeing if I could access the cinechamber space to review some output, but (a) I wasn't prolific this week, and (b) I need to do some planning for a commercial UX project tomorrow.

What is the nature and desired outcome at the get together at Gray Area on Wednesday?
- I mentioned to Yoann, we're both going
- I am prepared to show existing work
- preparing new work for presentation isn't a goal this week

WHAT DO I WANT FROM THIS EXPERIENCE?

I want to look at longer, "causal sequences". The various dissolving pointclouds are great, but I also want the chance to navigate thru the space and THEN something happens. I came across a good reference for keyframing Niagara parameters w Sequencer

I want to adopt better practices for my workflow
- file naming conventions
- version control
- multiuser workspace


2021-07-05 16:01
The last version of exoholo-loft is difficult to distinguish from the other version:

Yesterday
exoholo-loft.exoholo-loft-1.v001.0000.png

Last week
exoholo-loft.exoholo-loft-1.v015.0000.png

Get in the habit of naming level sequences uniquely
Think about what the After Effcts builder project is called. I've been using the generic term "session-n" which is maybe ok? It becomes hard distinguishing between them. For the work I've done already, names like this would be better:

FACTORY
SOMA
LOFT
WINTERMUTE

Think about how you'd enter this information in Jira. SHould you be entering this material into Jira? No. Not now. Version control is the better mode


2021-07-05 17:32
exoholo-loft-v016 demonstrates offsetting and compositing copies of a single panoramic rendering together so that environment is "anchored" to the space on two different screens


2021-07-06 11:31
FUTURE-43 visual stories EXOHOLO
I've created a baseline map/level sequence for reviewing scans
It's setup for the loftz_1M scan, but no reason it cant be used generally
I've also setup a Niagara emitter inside the loftz system as a baseline representation of the point cloud data. Meaning thatg it's static and persistent for any duration. 

I remain uncertain about version control but am setting up a test project on LOCUTUS to understand how Perforce works. Seems like Unreal Game Sync is a front end for perforce. Much of its functionality comes from making builds and even building the engine from source.

My iwn needs are really just version history. is UGS overkill for that, does it matter? How does P4 sork if you're not using UGS


2021-07-06 16:16
Fantastic, I'm logged into the LOCUTUS P4 Server on ONYX. Needed to add P4 server to the list of firewall exceptions


2021-07-07 16:29
I'll try something Practical with Perforce
move the Winter project on LOCUTUS to D;\Users\Gary\Unreal
setup UE4 to use Perforce for Source Control
create a new workspace: EXOHOLO
add the Winter project to source control
inspect outcome in UE4 locally
activate Unreal Game Sync


2021-07-07 17:47
There's some intrigue around setting up locations for different kinds of data. Its actually optimal if each of these is on a seperate directly attached drive (internal or external).

Metadata
Journal
Versioned

Backing up has some requirements as well:
Helix Server backs up its metadata in files called checkpoints.

Backup all checkpoints, journal files and versioned files regularly
Do not backup metadata files directly. Doing so may "lock" the files which can interfere w regular Helix server operation


2021-07-07 18:57
I've screwed something up with the way I removed Ubuntu from that spare 240GB SSD Drive. The machine restarts with a GRUB prompt leading nowhere. How do I remove GRUB entirely and boot directly into Windows?


2021-07-07 19:06
I'm back in Windows on LOCUTUS. Needed to change BIOS settings
However the changes I made to Environment variables have made it so I can't log into the Helix Server. I think it will be quickest to uninstall and restart this process


2021-07-07 19:21
Reinstalling.

Server
1666

Username:
Admin


2021-07-07 19:36
installed Helix Server. It's running


2021-07-07 23:54
after some effort, I'm no further along but can at least identify the problem I'm having. I can't seem to get the p4 database and depot
- stored on the same drive at G
- stored seperately
    + database on C
    + depot on G

I have a feeling this will look clearer in the morning 


2021-07-08 13:26
After some reading, it may be possible to use symlinks to map one drive to another. Everything could install in the default location, but the depot files could be symlinked to a destination on G:

Or I could just install Perforce to G: instead?


2021-07-08 15:58
Here we go again. I'm starting from a blank slate, as before


2021-07-08 19:16
and again. having trouble for the first time w the typemap 


2021-07-09 00:00
And again. Need to get this sorted tonight or defer until next week


2021-07-09 00:53
Well the 5th time is the charm I think I've got a depot & database for WINTERMUTE setup locally on LOCUTUS, on a dedicated internal SSD. The workspace is setup in a Perforce directory under D:/Users/Gary where it will get backed up by the daily archive

TO-DO
- additional backup scheduling for local & NAS archives
- test connection to LOCUTUS from ONYX
    + setup Workspace
    + get latest from WINTERMUTE depot



2021-07-09 01:27
I worked with the WINTERMUTE project in its new workspace. Made some changes and submitted to P4 


2021-07-09 01:40
Verified working
I'm accessing the P4 server on ONYX and getting latest from the Depot


2021-07-09 12:34
Doing some project planning in Jira
Organizing each of the environments I've been working with by Name
LOFT
WINTERMUTE
FACTORY
CLOUDWALKER

Creating a set of standardized subtasks to serve as a pipeline.
Maybe these will become Epics later.


2021-07-09 13:49
OPS-54  investigate ethernet connectivity issues on MULE
I've stepped through numerous oprtions on this matter. Still not resolved. 
It just stopped working all of a sudden.
- check the network cable
- reinstall windows


2021-07-09 18:29
That's good progress. I've setup what I think is a reasonable version controlled Unreal workflow. It seems like a lot of work for my immediate use - synchronizing projects on different machines for rendering, etc. I'm sure all the other uses will become apparent when necessary


2021-07-09 19:34
I've added the Scans project to version control in workspaces on ONYX and LOCUTUS

adding the Cinechamber project
added camera360 project
added Factory project


2021-07-09 23:46
while waiting for the new couch to be assembled, I played around with some point cloud data in UE4.27 
The handling of this data is much improved and I'm wondering if the new preview release is stable enough to run the SOMA project?


2021-07-10 16:39
I've been organizing map and related sequence files. I plan to split the SCAN project into a seperate LOFT and SOMA projects. Spent way too much time working on a non point cloud geometric fantasy wuith a grid. Its cool, but was ready to move forward 2h ago. I'm checking everything back in and will see how kicking off a render on LOCUTUS works


2021-07-10 19:35
cleaned up chaff
started render for grid-loop on LOCUTUS

first version uses 64 temporal sample, which seems like a lot, but wanted to see the output and rendering time, which is looking like it will be very long

2nd version uses 16 temporal samples and tiling x 4 
render quality seems identical for ths subject matter
Elapsed: 1:00
ETA 4:56



2021-07-11 08:46
goddamnit last nights render doesn't include the camera moves. Its just a static camera. Why? 
grid.grid-loop.v002


2021-07-11 08:56
rendering again on ONYX
ETA 2h

I'll monitor as it goes and see if the problem persists


2021-07-11 09:03
the new render 
grid.grid-loop.v003 seems ok


2021-07-11 15:57
I'm doing some work in the cinemachamber project that emerged from what I wanted to share w Yoann. He called out of our session today at the last moment, and not sure how to feel about that. On the one hand, I needed to do more prep work. On the other hand, it puts any kind of audio edits to the last minute. Which is the best time I guess.

Are we still partners? I feel like we've lost momentum, but he hasn't beeen to the space since they upgraded the audio. I am doing my best to stop thinking about me and to think about how I can support him so he'll have a cool experience when we go there on Tuesday night. We made plans to meetup on Monday night. 

I want to have additional material rendered out for that as well. Updated version of SOMA is what I was planning on. I also have a new GRID video



2021-07-11 16:01
I've learned how to fire events to a level blueprint (perhaps any blueprint) from Sequencer. A bit convoluted? A bit familiar though. Vaguely remeber doing something like this before for ZOS. Seems like it opens up possibilities, although the more immediate one for sequencing Niagara parameters uses a different workflow?

For my immediate purposes, this will allow me to use movie render from sequencer and trigger the level blueprint from the timeline instead of having it listen for BeginPlay.

The way it had previously been setup was to add the level sequence to the map and have it autoplay and populate the media files, etc. That's more of an interactive workflow. The only way to capture output (may still need to do it this way) is to use Microsoft or Nvidia screen recorder

I'll see if this works for my purposes.

I also created a new "preview" anim for packaging up video files
(I dont just want to package them up, I want to include some of the spatial character for Yoann & I to riff on)

Lots more work on this today than expected. Not without value. Worried about my team. What would Ruwan say?


2021-07-11 17:23
Sooo. The sequencer event behavior does work in a movie render que context. I was getting turned around by the behavior in editor. Its also possible to show that behvaior by enabling the PIE switch on the event properties. Probably the mehanism already in place (using benin play) would alo have worked without needing to fire a custom event. lol

Yeah. Verified. Works as expected with my original blue


2021-07-11 19:23
setting up some output
figuring out how to make movie render queue burn-in match what I setup for the level sequence


2021-07-12 08:59
I feel like a got a whole lot of nowhere yesterday. I was overly concerned about the presentation quality for the material I was planning to bring over to Yoann's and then he canceled. Frustrated. Wondering what the goal is for tonight, or will there even be a worksession tonight? 

I intend to bring over two looped pieces rendered from the cinechamber prototype. I'd like to have those prepared and rendering in the next hour.

Following that, I'm going to shift my focus to pixel streaming and OSC input to UE4. I want to keep working with Yoann. For personal, artistic and social reasons, but I can't ignore the elephant in the room. There's a major disconnect between our commitment levels. I don't feel like its up to me to tell him to work the way that I do, but the entire reason I got into this was to work together, and I dont think we're connecting that way. How can that be addressed? Maybe short form remothe interactive experiments will light that spark and give us both that shared sense of purpose that I remember feeling so good.


2021-07-12 10:10
updated BLOCKWORLD environment. New Map, level sequence, and materials so that I can continue to process or render the older version as needed. Maybe I'll have a chance to render this out later. At the moment though I'm wondering if/how environmental fog can be rendered w the panoramic camera?
blockworld_v02_loop is the new level sequence


2021-07-12 10:36
Turns out that, yes, environmental height fog can be captured by the panoramic camera. There's a flag to activate 


2021-07-12 11:48

LOFT
sequence: blockworld-loop-dark
movierenders: color-y.v001.[1496]
screenrenders: lidar-color-y_screen-01_H264

the output needs to be coupled to the level sequence that generated it
for archiving, rename files such that:

sequence: blockworld-loop-dark
movierenders: blockworld-loop-dark.v001.[1496]
screenrenders: blockworld-loop-dark_[10]


2021-07-12 12:00
the other one I want to work on - the blue/red/purple one was rendered as
exoholo-loft.exoholo-loft-1.v001

I'm just going to call this

map: loft-sdiff
sequence: loft-diff-a
movierenders: loft-diff-a.v001.[372]


2021-07-12 13:32
creative work on the staticdiff variant
map:LOFT
sequence:loft-staticdiff
movierenders:LOFT.loft-staticdiff.v001.[3000]
screenrenders:LOFT.loft-staticdiff.v001.[10]

let me check rendering time for this sequence [3000f]
nice. 
ETA:33m

I'll use this version as one of the pair I'll bring to Yoann's with me
NEXT:
- package LOFT.BLOCKWORLD
- package LOFT.STATICDIFF


2021-07-12 15:17
moving LOFT.loft-staticdiff.v001 into After Effects


2021-07-12 15:44
Processing in After Effects now

NEXT
- import into Cinechamber project
- screen record he output packaged for Yoann. I don't want to do another rendering pass, and I think this machine runs it just fine.
I'd like to have the material packaged up for Yoann in the next hour


2021-07-12 16:31
Meeting up w Yoann at 18:30


2021-07-12 23:45
good session. I knew he just needed an audience
rendering iteration loft-staticdiff-2
eta 30m


2021-07-13 09:00
Yoann transfered audio and I've just downloaded it
FIRST:
I want to take a look at the material I rendered last night as loft-staticdiff-2

NEXT
For the postproduction task FUTURE-61 I will begin by dropping the audio into the packaged videos we used for reference.

THEN
I'll either iterate on LOFT.STATICDIFF, or I'll iterate on LOFT.BLOCKWORLD with some of the feedback Yoann gave 


2021-07-13 09:45
taking a look at loft-staticdiff-2
processing for output as screens in AE


2021-07-13 10:00
started AE render


2021-07-13 10:50
transferring output to cinechamber project


2021-07-13 11:20
Ah. Unreal. Always some project management and optimization. Hopefull git ruid of the dynamicdatacach emessage I've been getting. Maybe improved system performance. I've set cinechamber project to raytracing. Just want to see the difference.


2021-07-13 12:00
Fixed cinechamber floor and walls. this was a good outcome but a distraction. Raytracing may be a distraction. I don't need to do vizdev for this. Move along man!


2021-07-13 12:08
The screen sequences I output for transfer to gray area will need to be 
- reprocessed in AE as looped footage for specified duration. Let's say 6m
- if the original source doesn't exist, then the MOV output will need to be looped and output as specified duration

Here are the assets to consider:

P1 loft-staticdiff-a
P1 loft.v015 (to be mapped as alt configuration in XML)
P2 loft-staticdiff-b
P2 blockworld-loop-dark


2021-07-13 13:32
started rendering 6m clip of looped footage 
loft-staticdiff-a

2021-07-13 15:25
loft-staticdiff-a
rendering complete

that took a lot longer than I'd expected.
I setup loft.v015 on LOCUTUS and am going to render that now and verify in prototype on LOCUTUS


2021-07-13 15:42
loft.v015
started render. Shortened clip duration to 5m. Added additional core to render farm. So hopefully no more than 1.5h


2021-07-13 15:44
verifying that output in cinechamber prototype. Adding audio and can screencapture for sharing


2021-07-13 16:19
audio capture from xbox game bar doesnt work so well.
Getting a bit concerned about the loft.v015 after effects processing time

Its a good idea to get rendergarden implemented on LOCUTUS as well. Didnt feel like I had time to do so today, but for longer durations like this, it would be a real productivity booster.

NEXT
I'm going to export my sequences to external media for transfer to Gray Area
I'm going to update the XML file 
    - loft.v015
        - use the designation found in cinechamber project to assign media to screens
        - add LOFT-v03.wav as the audio source
    - loft-staticdiff-a
        + add ApollointheClouds2.wav as the audio source



2021-07-13 16:27
loft.v015
only uses
screen-03
screen-04
screen-05
screen-06
screen-07


2021-07-13 16:28
should I cancel the rendering and resubmit just those comps?


2021-07-13 16:38
I launched a new render queue for screens 03-07 and it is more efficient. This was the right call. Its still a long render though, need to push back start time from 6p to 7p


2021-07-13 17:13
I spoke w Yoann and Steve. I'm just going to let this sequence render and consider it a reality check

render garden is saying that a mov sequence took 38m to complete, and then it has to transcode that to MP4


2021-07-13 20:17
That went OK. The world didn't end because I was unable to provide the other environment. Yoann was able to get good information and feedback regarding audio and how material works in the space. Incredibly, loft.v015 is still rendering in After Effects. wtf. I'm going to setup LOCUTUS and get MULE installed in the workspace, so I can use them each for rendering


2021-07-13 20:36
Just as a note, The way I have the Jira board setup is going against the grain of Jira. The stories LOFT, FACTORY, WINTERMUTE, SOMA, CLOUDWALKER would make better Epics than Stories. These would replace the non-specific Immersive Point Cloud Video epic.


2021-07-13 22:42
I've reorganized Jira


2021-07-13 22:46
I'm noticing that rendergarden is rendering all of the screens I specified. I'd cancelled the rendering erlier, and I think they were still hanging around waiting to be rendered. I think that the seed directory probably needs to be cleared out in order to prevent that. Some material may have been rendered 2x


2021-07-13 23:15
I have rendergarden and its dependencies set up on LOCUTUS. I'll read more about network clients in the morning. Great work day. 


2021-07-14 16:21
I've packaged loft.v015 to bring w me to Gray Area. Hoping we may get a chance to load it up and experience


2021-07-15 09:31
It doesn't seem like there's much of a point in recording HDR video on my phone. The material looks weird/flat to anyone not viewing it on an iphone. From what I've read the DolbyVsion iomplementation is unique to Apple. If the material needs conversion to SDR anyway, then what's the point. Is the additional data significant for color correction or image processing in general?

Anyway, I've converted the video I shot using iMovie and am transferring it to this machine now for further comparison


2021-07-15 11:17
When viewing the HDR and SDR files side by side in VLC Media Player, I don't see a difference in the content. I can see a difference in a Premiere project setup to import that material with an appropriate LUT.

Dolby Vision HDR can also be used for movies etc., however, the look is baked in and so you don't have much room to manipulate that image in post (unless you work in SDR, then the HDR metadata is stripped away )


2021-07-15 12:30
I'm processing the mov files in Handbrake for export as mp4 assets


2021-07-15 15:33
What’s the next step for LOFT?

I’ve seen how repeatable the loop
Structure can be. Especially if polyrhythmic and a bit chaotic 

Think about the loop-entry state
What does that animation look like? What does it mean?
Assume that it uses the loft asset
Where did I enter from. Another asset?

Think about the loop exit-state
What does that animation look like. What does it mean?

Assume that it uses the loft asset
Where am I going. Another asset?


2021-07-16 12:11
Here's my understanding of how to setup rendergarden for networked rendering

For networked machines without an after effects license, there are some steps needed to use aerender.exe as a rendering process

python & ffmpeg dependencies must be installed on the networked machine
        - ffmpeg must be installed at the same local filepath on each machine
the gardener script must be installed on the networked machine


To run rendergarden over the network, you launch the Gardener script on the networked machine(s) This launches instances of aerender.exe, which is a version of after effects used for rendering only. 

Rendergarden managed operations using a seed directory. Each of the render processes watches the seed directory for new jobs and updates the seed directory while working on a job

The seed directory must be a network share
each networked machine must map the same drive letter to the share
each networked machine must use an identical path to the seed directory


2021-07-16 12:25
the shared network drive:
should be a local drive on the machine that will be used for the combine (combining segments) job


2021-07-16 12:42
I'm going to use the external USB drive on ONYX as the shared drive



2021-07-16 13:32

- shared drive
- installed rendergarden on network machine
- install python on network machine
- install ffmpeg on network machine
- 


2021-07-16 14:43
the project to be rendered over the network needs to live on the shared drive

I am somewhat resigned to reinstalling windows on ONYX to deal with the issue I'm having with Chrome (I know, its crazy)
However, if so, I could take that opportunity to change the drive letters on ONYX

LOCUTUS
SSD-500GB   C: (system)
SSD-TTB     D: (data/projects)
HD-4TB      E: (archiving)

uh.. hold that thought. That's crazy. Just watch the video and I think your real use case is covered


2021-07-16 16:02
The rendergarden tutorials are a bit vague, but I think I've got it working.

2 processes (gardeners) are running on LOCUTUS
2 gardeners are sunning on ONYX


2021-07-16 16:13
I killed the gardeners, then started 4 news ones
Memory usage w 4 gardeners is high 27.4/32GB
What would happen if I added 4 more?


2021-07-16 16:35
It looks like everything is working. I'm re-rendering loft.v015 since the render time came as such a surprise.

This time around, I specified 20 seeds, meaning each comp in the renderqueue will be divided into 20 "jobs" that get picked up by the 14 gardeners I have running (ONYX x 10, LOCUTUS x 4)

The most obvious bottleneck on ONYX is RAM
It looks like the After Effects disk cach is on an internal hard drive rather than an SSD, or even split across multiple drives..


2021-07-16 17:04
I updated the After Effects prefs and the system pagefile prefs on LOCUTUS. Seeing greater CPU utilization. Difficult to state how much more performant the render queue is. What if I were to include MULE? That machine has 16GB RAM, but also a faster CPU (I think)

possible I'd get 4 more rendering nodes? With a lot of page swapping,


2021-07-17 12:36
Chrome is working again. More specifically remote desktop is no longer a problem to solve


2021-07-19 09:50
I've been playing around with sequencer and using cameras to make animations with an A, B, and a C. Its part of what I want to do with game levels like LOFT. How do you enter, what happens while there, how do you exit. Or more generally. Where's the entrance. Where's the exit. What happened inside? It feel like directingm, really.

I am working through nome Niagara examples. Learning a bit about how to use custom modules. There's a section I want to work throughh this morning which exposes Niagara params to Sequencer.

I also want to get serious about collating my documentary in a structured form. I've been thinking Confkluence, becaus its so basic. What are my other choices?
Milanote? That's great for ideating, but its not great at structured text, and video assets don't behave as expected on iphone. Maybe not such a big deal though?

I want to figure out (this mornig) Why not Confluence?


2021-07-19 11:33
I've finished up a pretty satisfying level sequence with 3 cameras exploring different aspects of my new particle system toy (Niagara)

NEXT - WHERE'S THAT BEAT?
Use the niagara parameter animation here to control the spawn rate
Dig up the reactive audio technique explored in an earlier project. It would look pretty cool if audio amplitude was modulating the sphere emitter (instead of the sine wave I'm currently using for rhythm)


2021-07-21 09:41
I'm adding MULE to the collective. I'm thinking I will relocate MULE to Yoann's place for a while. I believe the way forward is using UE4 in realtime. Not sure what that means exactly, but here are some of my dreams and functions

- loop, sequence, playback material in realtime, or near real-time
- adjust rates, ranges, etc. in response to what's happening in the space
- automate, or drive the UE4 level with signals from Abelton, audio amplitude, OSC
- import recorded audio for immediate feedback while recording audio
- use sequencer to cut up and arrange imported audio
- familiarize and empower Yoann with this workflow 


2021-07-21 09:47
For each machine in the collective, this mapping will apply

Users (\\archive) (N:)
Users (\\LOCUTUS) (X:)
Users (\\ONYX) (Y:)
Users (\\MULE) (Z:)

Compliance
x LOCUTUS
x ONYX
x MULE


2021-07-21 09:57
rebooting everything to make sure the mappings persist


2021-07-21 10:54
completed P4 setup on MULE
Getting latest revision to pupulate this machine's workspace


2021-07-21 11:48
I've installed Creative Cloud on MULE
I've Installed After Effects and Rendergarden. This machine should be able to run as a rendering node.


2021-07-21 12:10
Verified rendergarden functionality on MULE
Ran into an error until I realized that the filesequence was referenced by its local drive nomenclature instead of network mappings shared by all machines in the collective.

Instead of referring to an asset on ONYX as D:/Project/asset.txt
Its should be referred to in the AE project as a network mapping: Y:/Project/asset.txt


2021-07-22 09:34
Getting Perforce worked out on MULE yesterday was more time consuming than expected. SOme of it being my inexperience with using and administering that tool. I wpent tiome reorganizing the testenv UE4 project, and when I left it last night, things were a little bit broken.

I'm not sure what the protoocol for moving content into folders is when they're version controlled. Where can I read about it?

I'm not going to push myself to get the loop sequences I want done by Tesday. I definitely want new material along those lines, but I'm a lot more excited about bringing MULE over to Yoanns and figuring out how to work together interactively

- check w Steve if Mondays and Tuesdays are the only available days
- how much more can I have ready to share by Monday evening?
    + how much more can I have ready to share if I dont focus on rendering and packaging cinechamber output?


2021-07-22 13:02
I'm back in the testenv project. It got screwed up when I started deleting things in P4. How can I avoid that in future. I was trying to organize and consolidate the folder structure in content browser. A number of references were broken


2021-07-22 16:38
Verified that everything works on MULE. Looks solid.


2021-07-22 16:40
There are a couple of things I want to do when we work together
P1 use a shot track to sequence level sequences
P1 incorporate audioreactive processing in Niagara module (previously tested)
P1 incorporate audioreactive processing in Blueprint
P2 how to animate niagara parameters in sequencer
P3 how to record takes with interactive camera (game controller)
P3 investigate audioreactive processing with live audio in (Audio Capture component)
P3 investigate reactivity with Abelton Live/OSC


2021-07-23 09:52
There's so much I want to do. So much that can be done. So much I want to refine. So much I want to be part of. Its exhilarating and confusing and how do I capture it in Jira lol. 


2021-07-23 20:06
created a "shot track" without effort
a level sequence containing 2 other level sequences


2021-08-01 13:12
Yoann is coming by in a bit. I want to officially end this chapter and acknowledge how much I've gained and how much its meant to me. I want to propose a new chapter based on a more improvisational approach.

I'll propose installing MULE at his place for a while and see how it works.
However, I'd like to be able to sync Perforce on MULE, as well as access ARCHIVE in general.

I'm reading about different ways to access the NAS from an external network. 


2021-08-01 17:26
Good chat with Yoann. We're going to move forward with the idea of "jamming". He's thinking that the idea of a common production machine will help him reorganize his setup into a production workflow. W also acknowlegded the bigger collective picture. Its not just cinechamber,. i want to go further, and I can tell he does too. I think the onlw way to do so is to reduce the efort and increase the realtiem ritual

NEXT STEP
- setup a day (next week) to install the machine


2021-08-01 17:29
struggling a bit to understand the various terms behind remote access to my LAN. But this:

For clients that support it, WebDAV lets you access your NAS device as though it were a local device.


2021-08-02 09:24
I've gotten the WebDAV server started on ARCHIVE. I've downloaded Cyberduck to mount
