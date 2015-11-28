# Operations Engineering and Automation


Total Sections: 281   Populated Sections: 21
Current Goal: Populate Empty Sections: 260   (Done: 7.5%)


Lines: 920

Words: 15762

# Chapter 1: Preface


What will you get out of this book?  Why read it?



What I hope to impart here is a view into how I see operations, and how I automate operations.



In the case of the book, "operations" means "networked operations", "server operations", "datacenter operations", "production operations", all rolled into one term.  The field is both specific and non-specific, as operations can mean other things, but these fields are what I'm referring to.



What I hope you will gain from my perspective is a new foundation you can use as a point of reference to build your own operations experiences from, whether you are already an experienced operations engineer or new to the field. 



I will be covering a very large arena of information, so I will try to present a coherent picture, even though I cannot go into full details on every aspect, as it covers too many disciplines.



This book's format is meant to be read from start to finish.  It starts off more general, and very philosophical, setting up terminology and scenarios.  Then will become more specific as we get into implementation details.  Finally, it will go back to being more general as we discuss how to implement in your current environment.



This book is more about depth than about breadth, and as such we will continue to come back to examples over and over again, looking at them in different ways, to give a deeper understanding of all the components that make them up.  This is in contrast to many books that are meant to describe an array of information and give you a broader understanding of how to work.



<h2 id=8d921a98a2974ea61b905ce719a9f121><a href="#8d921a98a2974ea61b905ce719a9f121">1.1</a>: Where Ive Been, What Ive Been Doing, Why I Wrote this Book.</h2>
<br>
I've been working in the industry for over 20 years, and have been programming for over 30 years.  I've written over 1000 programs of varying size (the bulk of them being smaller, and operational in nature), but have also written and deployed PC games, end-user productivity tools, accounting software, end-user websites, as well as a lot of operations related monitoring, alerting, log parsing, configuration and automation logic required for operations work.<br>
<br>
Some names of places I've worked, named where you may know them, and grouped as industries where it's unlikely:<br>
<br>
Google, VMWare, Netflix, Cisco, Pacific Telesis, Lawrence Livermore Labs, Mobile Game Companies, PC Game Industry, Mortgage Industry, Financial Security Industry, Internet Startups (SaaS and end-user websites)<br>
<br>
You can see my abbrieviated job history at LinkedIn:<br>
<br>
https://www.linkedin.com/in/ghowland<br>
<h2 id=4135cf6df0e576145b37ff7fe29922a3><a href="#4135cf6df0e576145b37ff7fe29922a3">1.2</a>: The promise of automation is removing classes of work, while you get the desired results</h2>
<br>
At this point, everyone knows that automation is a necessary thing.  It wasn't always this way.  I spent much of my career trying to automate things and getting strong pushback from both management and peers.  <br>
<br>
These days people usually have some aspects of automation, and are comfortable with those, so it is only the areas that they do not yet have experience which are hard to get implemented.  A major impetus in writing this book is to resolve those problems, by making the concepts better publicized and hopefully well understood.<br>
<br>
The issues I find these days are not that people do not want comprehensive automation, but that there is not a clear understanding on what comprehensive automation entails, what it takes to build, how things will change once it is in place, and how the life-cycle of operations changes to modify it.<br>
<br>
With all of these things, it is best to stay results-focused, and look to what you want to achieve out of automation, and in my opinion the ultimate goal should be "removing classes of work".<br>
<br>
What is a "Class of Work"?  We will look at this in many ways over the course of this book, but we can start by summarizing it as "anything that is done".<br>
<br>
This may be a specific thing such as "update a DNS zone file" (text file).  When this "Class of Work" is comprehensively automated, then no one will ever again update the text file relating to DNS zones.<br>
<br>
This could be extended to "configuring DNS", in which case all zone files are automatically generated, the serial numbers are always incremented properly, the configuration files that specify the zones are generated, and all the transfers and tests to ensure that these changes are pushed out into production and contain valid entries are validated and monitored.<br>
<br>
This is a "Class of Work" that requires people to do currently, in some ways if it is already automated.<br>
<br>
If you have a service (SaaS, such as a web-site like "DNS Made Easy") that does this for you, then someone still needs to enter the data.  The data entry is still a manual process, and part of the Class of Work.<br>
<br>
How would you remove this manual work?  It will need to be generated from either a template of hostnames for the type of services being provided, or some other automated mechanism.<br>
<br>
When no one has to think about the life-cycle changes or perform manual labor relating to this area of work, then this Class of Work has been comprehensively automated, and has been removed.  <br>
<br>
Updating the system that manages this Class of Work remains manual labor, as writing logic has not yet been turned into an automatable task, but the regularity of updating the automation logic should happen far less frequently, and is more knowledge-work than data-entry work.<br>
<br>
Knowledge work is more stimulating, and known to be something that needs reviews and tests, whereas manual data-entry work is more prone to mistakes, because it is done so regularly that constant vigilance becomes impossible.  Eventually someone will make a typo or other data-entry mistake, and it will not be caught in review, and will be pushed out to production.<br>
<br>
With automated logic, these kinds of repetitive data changes and verifications can be done as correctly as the logic specifies, and if it is written correctly, it will be done correctly forever.<br>
<h2 id=205420c1274a2b80366e988715cd32f8><a href="#205420c1274a2b80366e988715cd32f8">1.3</a>: Writing in the first-person.  I will try to write as much as possible in the first-person, as I am speaking of my opinions, my experiences, etc.  I also find that this avoids the tone that can be see as "scolding" or "commanding" in write, as in the second-person "you must do this", etc.  When reading speech in the first person, I am more likely to see the information as informative, coming from the writers' perspective, rather than commanding and authoritative, in that this is an instruction or order for you.</h2>
<br>
You may have noticed, but I am writing quiet frequently in the first person, and will try to keep this consistent as much as possible.<br>
<br>
I am speaking of my experiences, perspectives and opinions, and so I think this is best done using "my own" voice, instead of a more factual "voice of authority".<br>
<br>
In my view, all information should be considered as coming from the source of origin, where you discovered it.<br>
<br>
When I say "X is Y", I think this should be read as "Geoff said X is Y", and not that X really is Y.  Whether X is really Y or not should be something that you validate for yourself, in your own experience, in your specific situation.<br>
<br>
The situation I could be using as my example may not match up to the situation you are working in, and my perspective may not be a useful one.<br>
<br>
Moreover, language itself is very flexible in what is what is meant, as many things could be intended by the same word, like the very overloaded word of "operations".  There is frequently a COO, Chief Operations Officer, in large or public companies, and this person's role and department has absolutely nothing to do with "production operations", "network operations", "server operations", "datacenter operations", etc.<br>
<br>
Because of this, it is useful to limit what you take from incoming information to what the speaker was trying to convey to you, as coming from them, from that particular situation, and their particular perspective and experiences.<br>
<br>
This separation from incoming-information to "fact" makes taking in more perspectives easier, as they do not need to be turned into a one-size-fits-all world view of truth.  As I learn more, I find that having such a one-size-fits-all is often a hindrance to communicating with other people, and learning new things.  It is certainly a hindrance to having an open mind to new information which may conflict with your current world view.<br>
<br>
Instead having a "this person said this thing" stance, allows any new information to come in as it arrived.  You experienced getting the information in some way, and that is that.<br>
<br>
Whether you utilize that information, or make it part of how you make decisions is up to you.  Whether it is applicable to your situation is up to you.  Whether it seems logical and grounded in reality as you understand it is up to you.  There is no reason to reject or accept it, as it is simply information.<br>
<br>
There will be quite a bit of this kind of introspection into language and meaning in this book, as it is in part a book on the philosophy of engineering and automation, because this is much more important than common jokes about philosophy majors in college may lead one to believe.<br>
<br>
I also find that when writing in the first person, it is less of a commanding or authoritative approach, rather than writing in the second person ("you will then do this") has more opportunities to throw readers off if they disagree, do not want to do that, or are tired of being lectured to.<br>
<br>
This is a one-way conversation, in that it is a book, but it is meant to be taken as a conversational approach to learning, so that you can grow from it as best is possible, and not merely a display of my knowledge and set of instructions for others to follow.<br>
<h2 id=c0288d74f0dd8cb74fcb23af5ce26a0e><a href="#c0288d74f0dd8cb74fcb23af5ce26a0e">1.4</a>: Hopefully, this will provide you with a set of foundational experiences from my expeirence, in which you can use to form your own opinions, methods, philosophies, procedures, axioms, and systems.</h2>
<br>
The ultimate goal in this book is that it improves your ability to function as an operational engineer, and to write automation that achieves the results that you want.<br>
<br>
If you find any areas difficult to understand, or believe that sections are not explained well or are incorrect, feel free to write me and I will try to get back to you and update the work as best I can.<br>
<br>
My personal email is:  geoff@gmail.com<br>
# Chapter 2: Introduction


One of the major focuses of this book will be to different the real from the virtual.



This may seem like something that is common sense, but I have found wide spread and scale disagreement on in what is real and what is not real, and this creates a lot of communication and planning problems.



If we can't agree on what is real, how can we agree on our priorities?  We will value things differently, because we understand them differently at a very fundamental level, and all communication will be moving past each other, instead of directly engaging.



The results will be poor, and without coming to terms with why this fundamental mis-communication is occurring, we may never be able to see eye-to-eye, and may end up being unable to work to get good results with each other.



Going to the very basics and working up from there will allow us to develop a common method of communicating, starting from terms, and moving to axioms, and then goals, and finally into priorities so that we can come up with plans where we agree on the components and end results.

<h2 id=ff17d94c0d49aab3e372e47b64b96ea7><a href="#ff17d94c0d49aab3e372e47b64b96ea7">2.1</a>: Focus on the virtual/physical management, specifically around internet and network services, but relatable to other industries.  All use cases will be around data centers and networked services.</h2>
<br>
"What is reality?" is a question that is too big and general to be dealt with here, if you want a good introduction on how to understand this from an engineering perspective, you can see Bertrand Russell's book {{ book_russell_reality }}.  It does a good job of describing how reality can be determined from our senses, and is a fairly short read.  You can also take a look on Wikipedia at the philosophical movement, Logical Positivism, which is a useful philosophy for engineers, and is one of the philosophical methodologies I use and reference in this book.<br>
<br>
For our purposes, it is good enough to have a summary of this, and for me to describe on which side of real vs. virtual (un-real) various elements reside in, for our purposes.  Again, this is not meant to be "ultimate truth", but a tool for communication, so that we can come to common terms and understandings, and grow our engineering abilities and get better results.  It is not meant for purposes outside of this endeavor.<br>
<br>
To be brief, I will use Russell's example converted into the experience you are having right now.<br>
<br>
At present, you are somewhere reading this text.  You are real, you exist, because you have tangible properties, such as mass, made of of molecules and atoms, in a certain state that make you you.<br>
<br>
The text you are reading is either in a book form, such as paper, or an electronic form, such as a monitor or e-ink display.<br>
<br>
If you are reading a book, the book is real, because like you, it is made of molecules, and has physical properties.  It resides in a certain position in the world.<br>
<br>
If you are reading from a monitor, then the monitor has similar physical properties.<br>
<br>
These things are all real, for our purposes of reality.<br>
<br>
The way you are able to read is that either ambient light is refracting off of the book, or is being emitted from the monitor, and those photons are striking your eyes, and the rods and cones in your eyes are being stimulated, and sending "signals" into your brain and nervous system.<br>
<br>
These things are all real.  Photons have physical properties, and while different than molecules and atoms, are able to be physically described and interacted with.<br>
<br>
At this point, you are probably affirming why you may have not read more philosophy works in your life, right?  Nothing new here, but lots of words to get to that point.<br>
<br>
Now, we enter into the realm of the un-real, the virtual world.<br>
<br>
How you interpret the words is not real.  It is a virtual type of understanding, though the word "virtual" is usually confined to computer related terms, I am going to use it universally to all things to differentiate from real.  Because we are mostly going to be discussing computer-related un-real concepts, it is easier to just stick to real vs. virtual.<br>
<br>
So, what am I getting at here?<br>
<br>
You are real, the device (book/monitor/device) is real, the photons traveling to your eyes are real, but your understanding and interpretation of the words is virtual.  Your feelings about the words is virtual, and in fact the words themselves are virtual.<br>
<br>
The ink on the paper, or the electrons producing the physical effects are real, but your understanding and interpretations of them are virtual.<br>
<br>
What's the point of this?  It will become clearer as we go on why I am leading with this, and it's not to make myself seem like a fancy-pants smart guy, it's because without this agreement now, there will be many more disagreements in the future, and it will hinder our communication about the more interesting and relevant parts of engineering and automation.  Please, bear with me here.<br>
<br>
So.  We have real books, devices, you are real, I am real, but your understanding and my understanding of things is not real, and even the words I am writing and you are reading are not real.<br>
<br>
How are words not real?  It is because they are symbolic.  They represent an idea, or set of ideas, which are also not real.<br>
<br>
The word for "book" exists separately then the object they describe.  In other languages, the word "book" changes (libre, knega, etc), yet the book itself does not change.  This illustrates how words are different than the things that they describe.<br>
<br>
Words can also be written in different fonts, and I could call this a "manual" instead of a "book", and yet what you are reading would not change.<br>
<br>
Symbolic things are not real, they are virtual, or logical.  I will use virtual instead of logical, as I will be differentiating "Virtual" as un-real, from "Logic" to be used for processes and code, or programming.<br>
<br>
Let's create a quick list of things that are real and virtual, for an immediate reference:<br>
<br>
- Hardware:  Real.  Something you buy, put an OS on, and runs your software, or something similar.<br>
- Software: Virtual.  Electricity (RAM), magnetism (rotating disks) or electro-chemical (SSDs/NAND) stores bits of information that can be executed.<br>
- Data: Virtual.  Same as software, but can't necessarily be executed.<br>
- Operating System:  Virtual.  Collection of software and data to make hardware perform operations.<br>
- Book: Real.<br>
- Words.  Virtual.<br>
- "A network": Virtual.  It's a concept of something that "networks", or more specifically may be an network IP address (data), that describes the network.<br>
- Network cables: Real.  Physical objects, that carry current.<br>
- Ethernet protocol: Virtual.  A collection of data and logic that describes how to communicate over electrical signals.<br>
- Layer 1 Ethernet: Real.  Physical electrical signals<br>
- Layer 1 Ethernet standard:  Virtual.  The description of how the physical Layer 1 ethernet will operatie.<br>
- Layer 2 Ethernet: Virtual.  How the Layer 1 physical (real) is used via the Layer 1 Ethernet standard (virtual), to create a Layer 2 ethernet connectivity effect (virtual).<br>
- IP Address: Virtual.  Data.<br>
- Hostname:  Virtual.  Data.<br>
- My engineering perspectives:  Virtual.  Data.<br>
- My engineering experience:  Virtual.  Data.<br>
- The actual things I have been through in my life:  Real.  Things happened, involving molecules and stuff over time (entropic heat exchange, etc)<br>
- My perspectives and memories of the actual things I have experienced:  Virtual.  Data, and summarized data at that, since I was not aware of the full-state of the physical (real) occurrences around me, and my memory (virtual) of them is a summary of that as well.<br>
<br>
<br>
I hope this short list and hopefully not-too-painful fundamental section has left what I am referring to in a clear state with you.  <br>
<br>
If not, please skim it again.  You don't need to agree with me on these things, you merely need to understand what I am trying to say clearly to get the information I am trying to convey.<br>
<br>
If you ever hit parts that feel wrong to you, or you reject, try to use the mechanism I presented in the preference of: "Geoff says X"<br>
<br>
This means you can take in this information, as "Geoff is saying this to me", without having to update your world-view at this moment to include what I am saying as "the truth", and in fact, I am not asking you to ever do this.  This is a communication to hopefully provide you more insight, which will include my perspectives, not as instructions on how you should see the world once you have finished reading this.<br>
<h2 id=75d62671847424a563ec929a890245c5><a href="#75d62671847424a563ec929a890245c5">2.2</a>: I only really know what I myself have experienced.  Everything else is hear-say, and while there may be a solid model behind it, I do not actually have experience in the matter, so I cannot trust the information to make solid engineering decisions on.  If I have nothing better, I may need to use this as the best course of action, and it may sound like a good thing to try, so I might experiment with it, but I have to recognize that this is an experiment, and so there is a great risk of failure.</h2>
<br>
What do I know?  What do I really know?<br>
<br>
In any situation, this is a relevant question, as it directs where I will go next.<br>
<br>
If I believe I have solid information, that I can take action on, I can begin immediately to take action on that information.<br>
<br>
If I know that I do not have solid information, then I know that the first thing I need to do is to get some solid information I could work on.<br>
<br>
How do I know what I really know is good information?<br>
<br>
It should be sourced from my own experiences, or it should be planned to quickly make checking the information so that it becomes part of my personal experience.<br>
<br>
Things I have personally experienced, I can say I have knowledge of.  Things I have read or heard, or that someone (including myself) just thought up may not be related to the reality of what is going on at the moment.<br>
<br>
Actions based on this kind of information are going to yield extremely unreliable results, because the information was not grounded in the circumstances it is being applied to.<br>
<br>
Let's create an example, a problem for us to solve.  We'll be doing a lot of this during the course of the book, so to get the most out of these I would suggest taking a moment each time one is introduced to try to model it out in your mind, or imagine it.  I will discuss techniques for doing this a bit later on.<br>
<br>
The problem will be a common one:  Alerts are going off on our monitoring system, and tell us that we are having problems with our web servers.<br>
<br>
The monitor alerts are not extremely specific in this case and report something like "HTTP test failure".  More specific alerting would be helpful here, but those tests take time to set up, and in our immediate example environment they don't exist.<br>
<br>
A group of people forms up to deal with the alerts, and immediately several things are suggested as problems:<br>
<br>
- Maybe there was a bad code push?<br>
- Maybe the logs have filled up the disks?<br>
- Maybe There is a DDOS or other hacking attack occurring?<br>
- Maybe someone is doing work on it, and forgot to tell anyone and made a mistake?<br>
<br>
All of these are possible, and while some are more likely than others, and could be used to prioritize where we start looking, the question remains:  What do we know?<br>
<br>
What we have experienced so far, and what we really know, is that we got an alert of "HTTP test failure", and this has something to do with our web server environment returning correct results to the monitor health checks.<br>
<br>
This is all we know in this circumstance.<br>
<br>
Was there a bad code push?  We don't know, because we haven't made it part of our example.  Let's add some data around that.<br>
<br>
We have 2 options:<br>
<br>
- We ask developers or release engineers (or whomever, for this purpose we will say "release engineers") if they have recently pushed any code.<br>
- We go and look to see if the code has been updated.<br>
<br>
Both of these options will yield us new information we can work from, but will each of them give us solid information?<br>
<br>
Asking the release engineers will give us the hear-say information that whoever we asked gives their best current information.  Do they check first before responding, to see if anyone has pushed code lately, or do they use their current information to tell us?<br>
<br>
If they say, "No, no one has pushed any code lately.  We won't be doing that until X time", then we will leave that conversation with information that says no new code was recently pushed, and we will have impetus to de-prioritize the possibility of new-bad code being pushed into production causing the monitoring alert.<br>
<br>
But is this solid information?  They may be the only person who does the code pushes, and so they may be the "definitive" answer on the subject, but what if someone new accidentally did it for some reason?  The "definitive" person would not know this, unless they checked, and their information would not be congruous with reality.<br>
<br>
If we take the second option, and we look for ourselves, then we can see if the timestamps on the files have been updated, or if the log files say that the web or application servers have been reloaded.<br>
<br>
The second option gives us information that we have personal experience with, and this is solid information.  If we do not have access to go look ourselves, then the next best thing would be getting someone who does have access to verify it themselves and preferably show us the result, but they could also provide unique information such as "X was the last time code was pushed", instead of a more vague answer like "No, no code has been pushed lately".<br>
<br>
So we have 2 lessons we can take from this example problem.  One, that information we have personal experience on is better than hear-say information, or information we do not have personal experience with.  Second, that there are degrees to "information solidity", or the reality-based nature of the information.<br>
<br>
Looking ourselves yields the highest relation to reality.  We were there, we looked at the information, and it said "X".  We have very high reliability with this information, as long as we were paying attention to what "X" was, and paid attention to get into the right position to look at the right data (not accidentally looking in a different server or direction, at the wrong files), then we have solid actionable information to work off.<br>
<br>
This would be the same level of information if someone else did this work, but showed us while they did it.  We saw them do it, we saw the results.  It would take some acts of deception to make this data questionable, and since we are referring to working in a work-environment, we will assume that all people are behaving as Good Actors for these examples.  Later, we will also look at how some people act as Bad Actors, and can create bad data, for instance trying to hide a mistake that have made.<br>
<br>
Less reliable is information that someone told us they looked, but did not show us, and gave us exact data, such as "X was the last time code was pushed, I checked the directory timestamps and logs".  This is good data, but we do not have personal experience with it, so it is less-good than data we verify ourselves.<br>
<br>
Next, we have a situation where someone else tells us "No, no code was pushed recently".  This is not data we have verified ourselves, so we have no personal experience with it, and it is not specific as to when the code was actually released.  It is possible that this person did not check, and is just telling us from their own perspective that they don't believe it was pushed recently.  This is beginning to be invalid data.  <br>
<br>
We could still ascribe Good Actor behavior to this person, and take them for their word, however, what will be the result if we do take them at their word, and de-prioritize looking at a bad code release, and start looking at other problems.  We end up exhausting the search on other things, and much down-time has accrued with the "HTTP test failure" alert still going off, and eventually someone looks and see that indeed new code was pushed out, and it contained a bug.<br>
<br>
Rolling back the code resolves the problem, and the HTTP server starts to return correct tests to the monitoring system.<br>
<br>
Much of the downtime accrued because of working with non-verified information could have been avoided by getting personal verification of the exact time of the last code push.  I have seen this exact situation happen many times, and bad-code or bad-configuration changes are one of the most common outages for networked services.<br>
<br>
Even though these are common, the common-ness alone does not mean that it is solid information.  It only means it is something that should be verified quickly to see if it is a contender for causing the problem.<br>
<br>
We will be exploring the idea of what makes good information in detail in this book, and I will change this introductory terminology of "solid information" into a more precise definition of Intelligence, which we can categorize in many ways:  Verified, Unverified, Actionable, Unactionable, etc.<br>
<h2 id=10fc971fd9dc706d141c5ada28fd9ae3><a href="#10fc971fd9dc706d141c5ada28fd9ae3">2.3</a>: What is Operations?</h2>
<br>
Keeping up our short tradition of asking questions that seem pointlessly basic, I will ask:  What is operations?<br>
<br>
Why do we do what we do?  Why does it exist?  What is it?  What are the goals?  What are the priorities?  What are the procedures that makes up an Operations department?<br>
<br>
The more questions that are asked, stemming from the original question, the less the question seems to be pointless, and the more the questions start to become the ones we deal with every day.  But, we skip the first question.  Why?<br>
<br>
We skip it because we already assume that we all know the answer, and that we are already in agreement about the answer.  It is taken as a given, but in my experience, there are many differences of opinions in even the most basic answers to what it is.<br>
<br>
People have different values, and they have different skills and personal experiences, and from these, they have a world-view that is also different.<br>
<br>
Getting to the fundamentals of what we mean by something like "Operations" means that we can start to align our views, and in aligning our views, we will communicate more effectively, and be able to work more effectively together.<br>
<br>
It is really these fundamental issues that make communication so hard and ineffective, because we do not drop down to discussing what we are fundamentally doing, and get buy-in from everyone on the team about each of the layers in the stack of what makes up an environment's operations.<br>
<br>
So, what is operations?<br>
<h3 id=0671652556ae5d62c827e6db8082bab7><a href="#0671652556ae5d62c827e6db8082bab7">2.3.1</a>: Ops is about Control.  Letting everyone do their own thing is not-control.  It is individual control, for them, but the company is not in control as there are too many different types of activities going on for the same task, so the task is constantly done differently, creating cruft and stuff.  You can move faster, but not in an aligned way.</h3>
<br>
I will posit that the primary thing that operations is about is Control.<br>
<br>
Why control?  Why not up-time, availability, responsiveness to business direction, or any other valid priority?<br>
<br>
My reason for this is that without control, you cannot be efficient in any other areas.  You can only be as efficient as your level of control allows you to be.<br>
<br>
You can always make progress in any area by applying resources to it:  people, time, money, hardware, etc.  <br>
<br>
These will make progress on problems you have and want to solve, but the limiting factor to each of them will be your ability to control the environment.<br>
<br>
If you have an up-time failure event, to fix the problem quickly you must be able to determine what is wrong, which takes the ability to gather information, and you must be able to take action to resolve the problem, which takes the ability to change the environment.<br>
<br>
Both of those actions, "gather information" and "change the environment" have Control as a central tenet.  <br>
<br>
How can you gather information without the control of the environment to yield you information?  In the most basic example, if you do not have access to the information, you cannot gather it, and you certainly do not have control over it.<br>
<br>
If you do not have access to change the environment, you cannot change it, and do not have control over it.  <br>
<br>
Like many things, Control can be seen a spectrum.  We can illustrate in on a line segment, such as:<br>
<br>
No Control <-----> Total Control<br>
<br>
This spectrum would represent all possibilities of "Control", having no control, and having total control.<br>
<br>
Control is a tricky subject, in that it is not only un-real (Virtual), but it is even more Virtual than many other things, because it more like a concept than something that is valid data.<br>
<br>
Unlike other Virtual (non-real) things, Control cannot be verified like data can be verified.<br>
<br>
If I have a variable "X" and I set X to 5 (X=5), and then I check if X is 5 (X==5?), I can get a result that is True or False.  X is either 5 or it isn't.<br>
<br>
But with a concept like "Control", there is no way to check that you have control or not.  You can check that you have access to some data, which is an aspect of control, and you can check if you can change data (by changing it, or looking at permissions (less good)), and this tells you more aspects about control, but there are so many other things that go into this that are very difficult to inspect or verify.<br>
<br>
For instance, one aspect of Control is, "Do we have enough time to do the work we need to do?"  This is an aspect of controlling one's schedule, so that good work can be produced.<br>
<br>
If we do not have control over our schedules, and work is required to be done before it can be done to our satisfaction of "good work", then we do not have control over this, and we will see problems arise from this fact.<br>
<br>
There are many other aspects of Control that we will look at, and I will make more cases on why I believe this is the central tenet of Operations and why understanding what you do have good control over, and do not have good control over is very valuable and actionable information.<br>
<p id=126b3100e0bafcd606cdb539413d4ce5><b><a href="#126b3100e0bafcd606cdb539413d4ce5">2.3.1.1</a>: "De facto" ops vs. "planned/controlled" ops</b></p>
<br>
If Control is the central tenet of Operations, what is the opposite side of the spectrum?  Uncontrolled operations?<br>
<br>
I think it's clearer to say that the opposite side of the spectrum from control is "de facto" operations.  What simply happens because there are business goals that need to be solved, and resources were put towards solving them, again and again.<br>
<br>
It is fairly easy, in my experience, to handle every situation in an efficient manner for the problem at hand, and still end up with a total mess of an operations environment, because the actions while individually efficient do not work together as a whole efficiently.<br>
<br>
This is often seen in naming conventions that change frequently, or that you could say there is not really a "convention" to the naming of things.  The same goes with what kind of hardware you purchase, if every time you purchase hardware you pick the "right tool for the job", but you end up with unique hardware configurations for every problem solved that required a purchase, then you have N number of hardware configurations to support and manage.<br>
<br>
The maintenance work to keeping many hardware configurations versus a limited number (say 2-4 unique hardware specifications per generation of hardware purchases), will mean many more problems have to be solved in upgrading software, and many more security and firmware upgrades will need to be tested.  It can easily create a situation that either requires many people to support, or more likely it to not worth the cost of actively supporting everything, and so support is only assigned when a high priority problem arises.<br>
<br>
"De facto" just means "In reality", but in common terms it means "the way things happens", like "this is what we have got from our low-coordinated efforts".<br>
<br>
So a spectrum for Control would look like:<br>
<br>
De Facto <----> Planned<br>
<br>
Planned operations will have strict naming conventions, where all the data required to be derived from a name is embedded in the name, and when new services, products, environments, and other things arrive, they are intelligently inserted into the existing convention and do not create new conventions.<br>
<br>
An example of "de facto" naming of hostnames might be like this:<br>
<br>
- chicken.domain.com<br>
- trex.domain.com<br>
- saturn.domain.com<br>
- monkeyknifefight.domain.com<br>
- web1.prod.domain.com<br>
- web9.prod.domain.com<br>
- web10.prod.domain.com<br>
- redis-01.sf.prod.domain.com<br>
- redis-01.nyc.prod.domain.com<br>
- redisqa-01.nyc.prod.domain.com<br>
- redis-01.nyc.stage.domain.com<br>
- git.corp.domain.com<br>
<br>
And a list of the same names, in a "planned" fashion might be like this (which provide the same services as the above machines, in a 1-1 fashion):<br>
<br>
- ops-001.infra.admin.sjc.domain.com<br>
- ops-002.infra.admin.sjc.domain.com<br>
- ops-003.infra.admin.sjc.domain.com<br>
- monitor-001.infra.admin.sjc.domain.com<br>
- web-001.product.prod.sjc.domain.com<br>
- web-009.product.prod.sjc.domain.com<br>
- web-010.product.prod.sjc.domain.com<br>
- redis-001.product.prod.nyc.domain.com<br>
- redis-001.product.qa.nyc.domain.com<br>
- redis-001.product.stage.nyc.domain.com<br>
- git-001.infra.corp.sjc.domain.com<br>
<br>
A couple of things can be immediately seem from these lists, as you compare the each ordered element against the same position in the other list.<br>
<br>
Some striking differences:<br>
<br>
- No "funny" or special names for machines.  "monkeyknifefight" is great imagery, and fun to say, but it has no business in your operational data.  It does not explain what services are provided, who owns the machine, where it is located, or any other actionable information.  It is essentially dis-information, since you know less about the machine then if it was called "misc" or "general".<br>
<br>
- In a planned naming structure, all names have the same number of elements, and the elements are in the same order, and written in the same sequence and pattern.<br>
<br>
In the list I have just made up, you can tell a number of things about any of the given hostnames' servers:  <br>
<br>
What general function they provide (web, git, redis).  <br>
<br>
What location is the server in?  SJC and NYC seems to be our options.  This is much clearer than "sf", as they are airport codes, and so provide more than city or regional information.<br>
<br>
What environment is this used for?  Production, staging, QA, corporate?<br>
<br>
What instance number of the service is this?  001, 010?  <br>
<br>
In addition, the instance numbers are always written in the same format, providing a standard for where to start a new service:  001 (or 000, if you prefer computer counting)<br>
<br>
The planned naming convention can scale significantly, while keeping a pattern that fits any of the machines, new or old.  Selecting the proper format for naming hosts is so important, because it is a direct factor in Control.<br>
<br>
If you cannot name something accurately, how can you control it?  How can I access a server, if I do not know it's name?  How can I change the state of a server, if I do not know it's name?<br>
<br>
I have worked in environments where naming conventions changed even in the same service.<br>
<br>
Take this for example:<br>
<br>
- redis-01-1.product.prod.domain.com<br>
- redis-02-1.product.prod.domain.com<br>
- redis-2-001.product.prod.domain.com<br>
- redis-2-002.product.prod.domain.com<br>
<br>
These are 4 redis servers, in the same "pool" of servers (used by the same application servers, in the same production data center), but halfway through someone changed the naming convention (out of a much larger pool than 4 machines, more like 40).<br>
<br>
They started out with "shards" as "redis-XX-#", where "#" is the "shard" number (relating to a master-slave set of data), and "XX" was the "shard instance" number, where "01" might be the Master (takes writes) and "02" would be the Slave.<br>
<br>
Then later they or someone else (more likely) created a new set of machines with the shard and shard-instance values flipped, and the shard-instance values now have 3 digits, instead of 2.<br>
<br>
This creates problems every time someone tries to work on these machines.  Logging into any given machine takes either trial-and-error, memorization, or looking it up.  Each of these is inefficient in time and personnel resources, and as the site scales up (more servers, more services), these kinds of time-personnel costs start to become major factors in both how much work can be accomplished in a given period of time, how frequently mistakes are made (not updating all the servers in the same fashion, performing work on the wrong servers), how long it takes to train new employees, and how well any employee really knows the environment.<br>
<br>
We are probably in agreement that planned naming conventions is better than unplanned or de facto naming conventions, but we are engineers, and it is not enough to think something is better, we require being able to dissect the issue to see what the components make it up, so that we can build it better for our specific needs.<br>
<br>
Let's take a look at the original planned naming convention I gave, and see how we can make it more efficient, since we want it to be our one-and-only naming convention.<br>
<br>
- web-001.product.prod.sjc.domain.com<br>
<br>
Let's look at each part of this name:<br>
<br>
- web<br>
- 001<br>
- product<br>
- prod<br>
- sjc<br>
- domain.com<br>
<br>
These are the components that make up this name.  Do we have the right components for our current needs?  What about our future needs?<br>
<br>
One can certainly over-engineer a problem and "prematurely optimize" it against future concerns, but not looking at what is likely to come in the future is on an extreme side of the spectrum for planning for the future.<br>
<br>
Taking each section individually:<br>
<br>
- web<br>
<br>
This seems pretty self-explanatory.  If we call things "web" servers, and they do "web" things, and we don't have other services that also do the same thing in the same environment and could cause confusion, this is good enough.<br>
<br>
If we do have other services that do the same or similar things, we might need some alternative names, such as "app", "webmain", or "webfront" or something similar.  Try to make it what people in your environment call it verbally, and there will be less confusion when switching from discussions to typing in data.<br>
<br>
I will call this first part of a naming convention our "Host Class".  So machines hostnames that start with "web" have a Host Class of "web".<br>
<br>
- 001<br>
<br>
This is our Instance number.  It is the first (or second if starting from 000) machine in in the "web" Host Class.<br>
<br>
This has an obvious limit of stopping at 999, and then the naming convention breaks.  Many organizations will never have more than 999 servers of any type, but this is not a reason to fail to plan for the case of scaling past that point.<br>
<br>
It costs very little to make a good naming convention, and only requires diligence and checking your work to ensure that no one creates names they should not, and it will save much pain in having issues with naming down the line.<br>
<br>
Scripts are written whose logic may not be able to deal with naming conventions that change, and this can cause problems in your environment as you pass these thresholds.  We'll cover how to solve this shortly.<br>
<br>
- product<br>
<br>
This is an example product name for your organization.  This should be a short product or project name that clearly differentiates it's purpose from other products or projects.  Notice in the example I use "product" and "infra" to differentiate the organization's product, which may generate revenue, from the infrastructure servers used to support the product's operational environment.<br>
<br>
- prod<br>
<br>
This is an "environment" description, and differentiates machines in production (being used by end-users, or running financially impacting services), differentiating it from servers performing the same actions, but that run in development, QA, staging, corporate, or other environments which have different users and impact if they go down or degrade.<br>
<br>
- sjc<br>
<br>
This is the location of the datacenter the server is in.  Whether it is a closet, or a Tier-4 Gold data center, you have assigned a location to it, so no one has to guess.  If you are consistent and only put the correct location labels into the hostnames, you will not have confusion over where machines physically reside when this becomes an issue, say for maintenance, repairs, or networking changes.<br>
<br>
- domain.com<br>
<br>
The example domain of our example organization.  The important part here is that it is consistent.<br>
<br>
There is a difference between internal names and external names, in that internal names can be kept consistent with the work of the Operations department, but external names are frequently in control of other departments such as Marketing, Business Development, Sales, etc.<br>
<br>
As such, they should be treated differently.  Internal names should be rigidly controlled, and external names should come with high recommendations for using naming conventions.  You could even provide several different recommendations for external naming conventions, to try to get other departments to constrain themselves and avoiding total naming-anarchy.<br>
<br>
Frequently non-Operations departments do not understand the use of sub-domains like "product.domain.com", and will create new base level domains for every projects.  Sometimes this is required (legal and business reasons) and other times, it is only because they didnt know they could have "newproduct.domain.com".  This is especially a problem for certificates, like for HTTPS, as new domains require new certs and updating them every year or so, while sub-domains may use star-certs (*.domain.com), and roll up hundreds of sub-domains under a single certificate to manage them.<br>
<br>
<br>
Now that we have gone over a bit about the initial planned naming convention, let's make it better.  Here is a proposal:<br>
<br>
- web-1-001.product.prod.sjc1.domain.com<br>
<br>
I have only added 3 characters to this name, but I have made it both significantly more scalable, and provided a new level of control.<br>
<br>
First, how is it more scalable than the previous naming convention of "web-001.product.prod.sjc.domain.com"?<br>
<br>
It is more scalable in 2 ways.<br>
<br>
First, it is more scalable in the location.  Previously we had "sjc", which meant that the server was located near the closest airport code of SJC (San Jose, California), but which data center is this?<br>
<br>
If you only have 1 data center, then you know.  But what if you get a second data center, for redundancy or growth?  What do you name it?  sjc2?  <br>
<br>
If you name the second data center "sjc2" and the first was "sjc", you now have a naming convention error.  You previously had 3 letters, now you have 3 letters and 1 number.  This will create parsing problems in scripts, and is inconsistent when you type names.  As you grow in number of data centers in the SJC area, you will have more problems when "sjc3" and "sjc4" are consistent, but the original "sjc" is not.<br>
<br>
If you know that something is likely to grow in count, then you should start with a numerical indicator from the beginning.<br>
<br>
What about "product", is it likely to grow in count too?  No, there is no necessary requirement for this.  If a new product does come out that is called "product2", then it is still differentiated from "product", and while it shares the same look and feel as the datacenter location scaling problem, it is actually a different type of scaling.<br>
<br>
This is likely to be controversial, as it is difficult to back up with solid data quickly, so we will cover how to differentiate data like this later.<br>
<br>
The second way it is more scalable is that we have a secondary numerical counter for the Host Class.  "001" has now become "1-001".<br>
<br>
This provides 2 methods of scaling.  For Host Classes that merely collect a lot of servers, this means we can use the same naming convention once we pass "999" instances for the "web" Host Class in our production SJC facility for our given product.<br>
<br>
This would look like:  web-2-001.product.prod.sjc1.domain.com<br>
<br>
However, many services have a more interesting use case for this number than simply going rolling over by 1000, which is separating sets of machines that hold related information.  Consider these names:<br>
<br>
- redis-1-001.product.prod.sjc1.domain.com<br>
- redis-1-002.product.prod.sjc1.domain.com<br>
- redis-2-001.product.prod.sjc1.domain.com<br>
- redis-2-002.product.prod.sjc1.domain.com<br>
<br>
These are 4 machines, grouped into 2 sets of 2:  1-001/1-002 and 2-001/2-002<br>
<br>
These can be used in many ways, but one way would be that this represents a Master-Slave relationship of data being written and read to 1-001 and 2-001, until one of those machines goes down, and then the other would take over such as 1-001 going down, it would be: 1-002 and 2-001 which are active for reads and writes.<br>
<br>
What data is sent to each of these machines could be done based on doing a modulus of an index ID (shard = index_id % 2), or another lookup method (rings, partitions, etc).<br>
<br>
In this case I refer to the first number as the "Shard" and the second number as the "Shard Instance", so redis-1-001 is Shard 1, Shard Instance 001.<br>
<br>
This is a very scalable naming convention.  It allows for different Host Classes (web), different Shards of data (-1-), different instances in the shards (-001.), different products (.product.), different environments (.prod., .qa.), different data centers (.sjc1.) and the common domain name for internal server hostnames.<br>
<br>
Separate from being scalable, this also provides a new layer of Control.<br>
<br>
Data in Shard 1 is different than data in Shard 2, and may even have different logic operate against it.  This is more easily handled than differentiating "redis-001, redis-002" from "redis-003, redis-004" for different logic.<br>
<br>
It is generally better still to use the same logic on all Host Classes of type "redis" and merely differentiate the data sets by the Shard, but because you have grouped the Shards as different numbers, you have this additional ability to control them accurately based on this data.<br>
<br>
There are other ways of organizing this data into names, and it depends on what data you need to track, but starting from a naming convention like this when you don't yet have that information is a safer bet than starting with less information planning than this.<br>
<br>
If you know you have additional requirements, be sure that they are implemented into the naming convention, and kept in the standard.<br>
<br>
If you already have a naming convention, it is better to stay with it than to change it, but if you do need to change it, it is better to make a new standard, and make all new machines comply with it (if they are not in existing services with the old naming convention).<br>
<br>
This way you can at least control your naming conventions in a generational sense, and if you are doing planned work, you should have a very limited number of total generations.<br>
<br>
There is a lot more that could be said on just this example, and we will come back to it later, as naming things is, after all, one of the two hard computer problems, along with cache poisoning and off-by-one errors.<br>
<p id=e6f860a586c5005530de3736bbf50109><b><a href="#e6f860a586c5005530de3736bbf50109">2.3.1.2</a>: Alignment takes "vision" and knowledge.  Not someting someone new to the process can understand well, because they are new.</b></p>
<br>
Another important aspect of operational engineering, and engineering in general, is "alignment".<br>
<br>
Things must align with each other for their full efficiency to be able to be used.  This is easy to see in the physical world: all sections of a bridge must align with one another, fence parts must be in alignment to be a good fence, and support beams must align with each other to provide continuous support.  Engines must align with transmissions and so on.<br>
<br>
It is no less important in the virtual world.  The entire field of networking is about aligning physical cables and virtual configuration to move frames and packets from source to destination.  Databases are about aligning data together so that it can be stored and retrieved efficiently.<br>
<br>
Everywhere you look alignment is an important factor on the quality, reliability, resilience, and structure and yet like many fundamental aspects of engineering, this topic itself is not discussed directly, and typically indirectly discussed as in how "everything must match up" given different protocols.<br>
<br>
You may see where I'm starting to go at this point with all of these fundamental questions and inspections:  the are fundamentals of engineering that we are using every day, but not discussing directly in our conversations about our environment, resources, goals, and what we are going to do to achieve our goals.<br>
<br>
This lack of introspection of our process results in a lot of miscommunication, and different visions struggling for the chance of being implemented, but without the necessary alignment between all the points of implementation to give us the kind of efficiencies, resiliency and other effects that we desire.<br>
<br>
Having this vision requires being able to see "the big picture" as well as the details, and it is important to be able to go from detail to big picture, back to details again repeatedly to see what any proposed changes will mean with regard to aligning with the rest of our details, to create the final result which occurs when all of those details are taken in whole.<br>
<br>
This is the methodology I use in designing any solution, and I will try to describe it in enough detail that you can inspect the process for yourself and can hopefully positively supplement your current methods for doing similar activities.<br>
<br>
One thing about "vision" is that it is something that takes a bit of experience to be able to see.  One needs to have had personal experience implementing things to really know what effects will result in the implementation, and across enough areas of the environment so that one can see how things align well or do not align well.<br>
<br>
This experience is less about how many years one has worked in an industry or environment, and more about the experiences one has had in one's lifetime.  <br>
<br>
If you have never worked in the industry before, you will not know how organizations that run production operations, especially internet facing production operations at large scale, will function and what changes will do those organizations and operating environments.<br>
<br>
The more you work in different environments, and complete more areas of implementation, the more experiences you will gain.  You can supplement these by setting up your own virtual environments on any cloud hosting providers, or on your own machines with a series of virtual machines.<br>
<br>
All projects, whether in-industry or outside of it, are limited, and never give complete information, because one's viewpoint is limited and the amount of details one can interact with is limited.  So even if you know one environment from beginning to end, having created all of it, you will find another environment that you didn't create to have many different properties, even if all the software used is the same, due to the alignment choices made in it's creation.<br>
<h3 id=7bdf31941d762810d8c81c360d28d38c><a href="#7bdf31941d762810d8c81c360d28d38c">2.3.2</a>: An Explanation of what Operations.  And why every company is an Operations company (internet or not), and how now almost every company is first and foremost an Ops company, though almost no companies recognize this.</h3>
<br>
This section could be headlines on the front page of any magazine targeted at CIOs, and so may seem a little fluffy and self-serving.<br>
<br>
Sales people think of organizations in terms of their sales generating revenues.<br>
<br>
Developers think of organizations in terms of the software they write, which may be sold to generate revenue.<br>
<br>
Managers think of organizations in terms of the people they manage that do the work.<br>
<br>
Customer Support thinks about organizations in that customers would be completely dissatisfied without their support.<br>
<br>
Finance thinks about organizations in terms of cash flow, as when an organization runs out of money, they can no longer pay their building leases or employees.<br>
<br>
Etc...<br>
<br>
Each department in an organization thinks it is a critical department, and they are all right.  No organization would pay the financial and opportunity costs in maintaining any department that is unnecessary, so they are all critical.  Operations is no different here.<br>
<br>
There was a time that operations was a lot more like Facilities departments, they bought things and maintained them.  Keeping them powered up and plugged in, and keeping people from stealing or damaging them.  This is not really accurate, but from the perspectives of people paying for these employees, it is pretty close to accurate, and we are currently discussing how organizations see themselves and their actions, and organizations act through using money to pay for services.<br>
<br>
What has changed, and what companies have for the most part not caught on to yet, and it will behove operational engineers to start repeating ad nauseam is operations is now the front-line of many companies ability to collect revenue.<br>
<br>
This started changing for many companies in the late 1990s, and started to become normal in the 2000s, and by this current 2010s almost every company's interactions with it's customers are going through a network, to servers, and software and databases that run on those servers.<br>
<br>
The majority of the companies I have worked for have completely downgraded the importance of their operations departments, giving much more staffing and scheduling priority to other departments.<br>
<br>
There are a number of reasons for this, and they are all valid in themselves, as many perspectives are when given in their own context.<br>
<br>
However, in a context that is grounded in the physical world the connection to their revenue might look like this for different companies, starting from the least-technological and moving to the most:<br>
<br>
- Physical good company.  Makes things that are sold in metal cans, etc:<br>
	- Supply chain management has a basis in digital records at every step.  Some steps involve calling people, writing things on paper, but these are recorded in at least Excel type spread sheets, and at any larger organizations something more similar to an Enterprise Resource Planning (ERP) software to coordinate all the steps are required.<br>
<br>
	- Communication with vendors in the chain may have many physical components, but ultimately they are also recorded into digital mediums, at least the low-level of email, if not higher level tracking software.<br>
<br>
	- Employee time and pay records are now kept in a mostly or purely digital form.<br>
<br>
	- End-user support is typically done via electronic medium (emails, customer support) to <br>
<br>
	- The larger the organization for all non-Internet based companies, the more corporate infrastructure that will be needed to provide support to desktops, laptops, servers to manage directory services (AD/LDAP), backups, storage, centralized software, etc.  More of these services are moving into online-only for small-medium companies.<br>
<br>
	- Hold outs will be older (pre-PC age computers) and will need to be small, to maintain operating the manual labor scales<br>
<br>
- Non-Internet Services Company<br>
	- Similar to physical companies, but with more smaller companies that can get by without much technology.  Real estate agents are a famous example of this.  Doctors and lawyers are also slow to adopt technology in tracking their clients and work, but in most medical institutes I have seen recently, all patient visit tracking is being digitally tracked.<br>
<br>
- Physical software companies<br>
	- Software is sold in boxes, in stores or shipped via the mail on DVDs.<br>
<br>
	- All software is written in a networked environment which must remain up for any productivity.  Developers cannot all go home and continue working if the infrastructure going down, and as security levels increase, this is not possible for those reasons as well.<br>
<br>
	- Customer support is usually entirely digital, unless it is for Enterprise level software, and then there is phone call and occasional in-person visits as well, mostly as good-faith efforts, not to solve immediate problems.<br>
<br>
- Internet Service Companies<br>
	- This is where the real change occurs, and many businesses are becoming more Internet service oriented.<br>
<br>
	- Almost every interaction the company has with end-users/customers is over the Internet, and handled by servers that the company manages, and may or may not own/lease.<br>
<br>
<br>
This is a very simplified spectrum of business, and not meant to be correct or truly representative, but merely to paint a quick picture I need for this example, which I'll start describing... now.<br>
<br>
<br>
The change is that these days if your operations is not reliable, and you have frequent outages, or long-term degraded performance, or you are unable to respond to customer demands in a "reasonable" time, or competitors have a more reliable and reachable service, then you are directly impacted in your revenue.<br>
<br>
If your operations is down, your customers cannot reach you to pay you.<br>
<br>
As someone reading this book, this is no surprise to you, but what may be somewhat surprising is that many companies I have worked for, and you may have as well, display all the symptoms of completely not behaving like this is true.<br>
<br>
Some of these symptoms are:<br>
<br>
- Not properly staffing their operation teams for the workloads they are required to perform.<br>
<br>
- Not giving proper lead times on work that is due, such as finishing a project that the operations team was not notified about, and expecting an immediate release to the public of that project.  Not taking into account either ordering hardware, or configuring systems to support the software.<br>
<br>
- Not giving significant information on how to maintain, run, or even install the software to be released and supported.<br>
<br>
- Prioritizing work that does not yield to improving or supporting the revenue generating and employee supporting software and services.<br>
<br>
There are many other symptoms, but these are large enough to illustrate this point.  Other departments have similar complaints with regard to notice ahead-of-time, and schedules.  See any book on Software Development project management for examples close to operations.<br>
<br>
This is not a problem that is likely to be solved soon, if every solved, because there are a number of difficult factors that cause it, the primary one being the structure of organizations themselves.  When something is structure a certain way, it will tend to produce certain results, and producing different results is very difficult, and often only temporarily possible.<br>
<br>
Since the organizational structure of organizations is not likely to change, the best hope in making progress here is something akin to the Agile movement in development, where all developers just kept repeating the same things and eventually the management of companies started to be populated with managers who also said the same things, and their world changed.<br>
<br>
It's debatable on whether their world really changed that much for the better, but there are many distinct differences in the pre-Agile development world, from the post-Agile development world, and it was this change in perspective and discussing it that caused those changes to take effect.<br>
<p id=5bc4c817bd8491f2de4fcd4fa234cca9><b><a href="#5bc4c817bd8491f2de4fcd4fa234cca9">2.3.2.1</a>: Their ability to stay online and available and provide their service is what keeps them making money.  How is this not a core-service?</b></p>
<br>
One concept that organizations have a pretty good grasp on is "core services".  They understand there are some services that they cannot outsource to other organizations and remain an efficient operation.<br>
<br>
The core-est of these core services are: management, finance and human resources (HR).<br>
<br>
Almost no organization outsources its' people managers.  They are the most core-service that a company has.<br>
<br>
Similarly, there will almost always be at least 1 to several people in the finance department, even if they use external services for many services that used to be hired in-house.<br>
<br>
HR in the past decade has begun to be outsourced, but once a company reaches a certain size, they always have their own HR departments.  This is the same for legal services, though this can be configured in a number of ways for companies, so I'm not listing it as a core service.<br>
<br>
Many companies outsource their development departments, and many companies also try to outsource their operation department, though this does not usually last long, and they may try to stick with it by turning their developers into their operations staff, but eventually some people will end up being the de facto operations team, regardless of their titles.<br>
<br>
If a company is primarily a software or internet service organization, and these are the types of companies I focus on, so they will be the majority of what we spend time inspecting, then they are much less likely to outsource their development departments.<br>
<br>
They realize the developing software is a core business service, and without direct control of their developers and efficient communications, they are unlikely to make consistent progress.  Many companies that try to outsource this department end up moving it back into their company after poor experiences, unless the product being developed itself is not all that important to the company, or can be treated as a throw-away product (like a phone application they only need to do XYZ "well enough").<br>
<br>
This is all a pretty subjective description, and I won't use up the space to turn it into a more objective one.  You should review your own experiences with these descriptions to determine how accurate they seem to you.<br>
<br>
The point of this discussion on core services is that for any company that relies on Internet or networked services for revenue generation, their operations department is not only a core service, but is often the front door to any other services.<br>
<br>
If their operations is not available, or performance is significantly degraded, then their customers and partners are not able to use their services, and they cannot generate revenue.<br>
<br>
This would be similar to sales people losing the ability to contact customers, completely making that department unable to provide benefit.<br>
<br>
If a company develops software, and end-users cannot reach that software, then there was no reason to develop it.<br>
<br>
This is where operations sits in the revenue chain, and companies are not yet currently recognizing the important distinction.<br>
<br>
I have used many similies for this over time, such as:<br>
<br>
- Operations is like the tires of the car.  We are the part of the car that comes into contact with the road.  Your driving can only be as good as your traction against the ground.  If you lose a tire, your ability to drive is severely impacted or not possible. <br>
<br>
- Operations are like the roads.  You can have a fleet of cars or trucks, but you cannot efficiently move them around without roads to provide consistent surfaces.<br>
<br>
A lot of people shop for cars, but not a lot of people are involved in the building or maintenance of roads.  This is similar to many people using networked services, but not being aware of what it takes to build or maintain them.<br>
<p id=109a7a222581029b6b3ed44aeb36acbc><b><a href="#109a7a222581029b6b3ed44aeb36acbc">2.3.2.1.1</a>: Just because its Core doesnt mean they need to own all of it, but as they grow they will pay more and more for what they do not control, and control well.</b></p>
<br>
A service may be a core service, but that does not mean all of it needs to be internally owned and operated.<br>
<br>
Cloud datacenter operations and Software-as-a-Service (SaaS) have changed the way many companies perform their internal and external operations, and has provided new ways for many engineers to think about solving problems.<br>
<br>
Just because you are paying someone else to maintain hardware or software for you does not mean that you do not need to manage it.  Some SaaS products do not require much management, but other still requires one or more full time staff to help manage it for the rest of the departments.<br>
<br>
For machine and datacenter operations, having Cloud offerings like Amazon or Googles offerings does not stop operational work from being created, it only raises the bar on what type of work is required.<br>
<br>
The basics of buying machines, racking them, cabling them, keeping them physically functioning (replacing disks and RAM, etc) and doing basics like assigning their primary IPs is taken care of for you.<br>
<br>
Everything above that level is up to you to manage, and these are the more complex problem areas, as the lower level areas are more logistical, scheduling and manual labor intensive.<br>
<br>
Who will manage all of the rest of the decisions and life-cycle maintenance problems that your network services require to function properly?<br>
<br>
Whoever they are, whatever you call them, they are your operations team, and are providing the operational core services for your organization.<br>
<br>
Outsourcing works up until the point where you lose Control that you need over the environment.  At some scaling point in every organizations usage of an external service, their needs and the services offerings will start to part ways, and the service will start requiring more work than previous to perform the same benefits for the organization.<br>
<br>
Once this reaches a critical point, either though financial cost, personnel time cost, or cost in terms of outages, degraded performance or misalignment in terms of providing the kinds of services the organization requires.<br>
<br>
Once this point is met, there will be a new transition where the problem areas are migrated to another service, which it is hoped will solve these problems, or the services are migrated in-house to be internally managed.<br>
<br>
At present the financial costs alone seem to be consistently measuring up like this:<br>
<br>
- Internally managed infrastructure.  1x cost, of hardware, data center and network services to provide an operational environment.  This is the base-line, doing it yourself.<br>
<br>
- Managed services that are comparable to doing it yourself, but letting others do it for you, about 3x the base-line cost.<br>
<br>
- Using cloud services, where you manage all your infrastructures through a virtual interface is about 5x the cost of doing it yourself.<br>
<br>
This is highly subject to change, as many things are involved in pricing, but as of 2015, this has been accurate in all the measurements I have made in about 10 environments I had direct internal access to, from 2008 to 2015.<br>
<br>
What are the differences in cost in your current environment, between total ownership/leasing, managed services (someone else buys/leases and maintains), or going completely virtual?<br>
<br>
You should know these differences, as they will make data points in decisions on how to run your departments as the costs start to outweigh the benefits of any solution.<br>
<br>
This 1-factor look at the problem, finance, is not a "big picture" view, it is only a single detail, so there are many other factors which make using services that may be 5x or 3x as expensive, and provide worthwhile benefits, such as the total cost being low enough to be worth it, or the faster turn around time on new machines, or not having decided on the hardware requirements to make it practical to start ordering hardware yourselves.<br>
<br>
There are many more factors in this, and we will get into some of them later, but they are not the focus of this book, so we will not cover them comprehensively.<br>
<p id=0932b206900bdd69c2b6cc7a46dfee68><b><a href="#0932b206900bdd69c2b6cc7a46dfee68">2.3.2.1.1.1</a>: Typically companies still dont tell ops departments that they need anything, until its due, all decisions are done, and its time to roll out.</b></p>
<br>
The problem of communication between departments, especially in regard to lead times between knowing they need work to eventually be done, and when they alert another department or team that they need that work done is such a classic problem that we can just assume it will happen everywhere, in every circumstance, unless people do something to change the pattern.<br>
<br>
In places where departments are giving each other prior notice of work coming down the pipeline, and involving the teams they will need to do that future work in the design phase, it is very likely that this was set up on purpose, and either by "visionary" early employees or founders, or through great work of some individuals to make changes to the de facto process of only asking for work to be done, when it is at the end of the project and time to release.<br>
<br>
I say it's most likely that this is the problem, because I have only worked in a couple environments, out of a large number of environments, where this happened as a normal occurrence.<br>
<br>
The point I am making is that one shouldn't be surprised when another department or group arrives and says they have finished a project, and they "just need it deployed into production", and has no time available in their release schedule for doing things like:<br>
<br>
- Productionizing the release process<br>
- Productionizing the configuration<br>
- Doing security audits and fixes<br>
- Writing an operational manual with support play book, enumeration of error codes, instructions as to options<br>
<br>
Frequently projects just being released into production do not have good performance tests done of them, although this happens more frequently than others, so I'm not including it in the above list.<br>
<br>
One of the lessons it took me a very long time to learn, but has served me well since learning it, is that if you recognize a pattern as occurring regularly, it is better to simply plan to deal with that pattern than to put up any resistance to it's existence.<br>
<br>
What I mean by this is not to get upset when you are given these types of projects, and they require immediate action, and things are requested to be done "wrong" and they cause havoc with the clean environment you are trying to make.<br>
<br>
Instead, see them as failure to get ahead of a pattern that occurs so frequently that you can simply assume that there are cases in process of coming to you right now.<br>
<br>
Knowing this, how do you get ahead of this problem?  You can't completely solve it, as it requires cooperation from other people, and the root of the problem is that they themselves aren't coming forward to cooperate before they normally would.<br>
<br>
Some things you can do:<br>
<br>
- Regularly, say every month, send out a standard template communication (email, etc) to all departments asking if they have any projects that will coming down the pipeline and will need operational resources.<br>
<br>
- Describe in the communication what "requires operational resources" means, such as machines in production, adding a new service, making changes to services which aren't already in production or that the operations department doesn't know about, etc.<br>
<br>
- Describe any lead-times you require for these types of projects.<br>
<br>
This is the direct-but-passive communication approach, and will allow people who are up for communicating ahead of time to communicate with you in a way they can understand is helpful.  This will not catch all new projects.<br>
<br>
From there you can also create a department policy, document it in your online documentation site (wiki, etc) as to how you accept new projects, and when people ask you for them,  you can refer them to the "new project on-boarding" documentation that describes how you would like to work.<br>
<br>
This provides some "back end" type protections, as people will see that they didn't communicate with your regular email, and now they are learning how the operations department works.<br>
<br>
But this will still not stop any externally set schedules, as if the company requires a product is launched on a given date, then this is a higher priority than following any department's self-appointed rules, and will override them in many circumstances.<br>
<br>
The direct-active approach is the best, but requires more resources, this would be someone who is acting a department project manager would meet with the other department heads or team managers directly, and ask them what they are working on, and when they will need operational resources.<br>
<br>
This direct-active approach is more likely to be successful, as the managers will know what projects they are working on, and are not trying to hide their project's work, they are simply working to complete their projects, and in this way you are assisting them in getting to the final steps of completion.<br>
<br>
If this can be approached in a "let us help you" manner, then collaboration can begin, and hopefully will improve the working conditions for everyone, as handing off work between groups is a difficult process.<br>
<p id=d05edb2ae926b6b3071c2d16497f5721><b><a href="#d05edb2ae926b6b3071c2d16497f5721">2.3.2.1.1.1.1</a>: The ops department is blamed for all lag.  Developers are blocked, legitimately and not-legitimately.</b></p>
<br>
A look at the more negative side of this problem between groups is that the operations departments are often claimed to be creating lag between work being completed by other teams (typically development, sometimes marketing or business development).<br>
<br>
From the perspective of the non-operations teams, this is a true statement.  They finished their work, and now they want to put it into production for end-users to be able to access, and any time between them being "finished" and the end-user being able to access the work is considered lag created by the operations department.<br>
<br>
The issue here is one of "someone else's problem", which comes down to empathy and a realistic view of the nature of all work involved in a company, not just one's own work in the company.  This is not a problem that can be solved directly, as people's ability to appreciate other's positions is not going to change easily, or deterministically.<br>
<br>
So what we can do is to look to ameliorate this problem as much as we can, by getting ahead of the requests.  This means having a process that people can easily follow to getting what they want.<br>
<br>
For example, create a limited set of Hardware Specifications that you purchase, for any generation of hardware.  The typical basics of this as of 2015 are usually a "utility" class machine, a "relational database" class machine, and a "non-relational database" class machines.<br>
<br>
To simplify what we call a Hardware Specification, let's use the acronym for Stock Keeping Unit (SKU), which is very general.<br>
<br>
Utility class machines are for running general purpose software, and typically are mostly used for web and application services in production.  There may be two SKUs if there is a "low memory" and "high memory" version.  Caching services (memcache, redis) usually use a low amount of CPU, but a high amount of RAM, and may reside alone on machines due to their critical nature.  Utility machines typically do not need much in the way of storage, and almost any small redundant disks are good enough.<br>
<br>
Relational Database class machines are typically used for relational SQL databases like MySQL, PostgreSQL, etc.  They need both a lot of RAM, a lot of cores, and they need very fast disk.<br>
<br>
Non-Relational Database class machines are usually running software like Hadoop, Cassandra, or any of the other many column-oriented databases that are better at storing logs, events, time-series and other databases.  They typically need a lot of CPU, memory, and much more storage than relational databases.  If a relational database might need 5TB of storage, a non-relational database might need 30TB, or something in this type of proportion.<br>
<br>
Starting with these 3 base SKUs, and perhaps several sub-SKUs for more RAM, you can offer departments easy choices for how they want to deploy their software.  Providing them virtual machines for some services may also be a good match, depending on their usage patterns and criticality.<br>
<br>
For each type of request they are likely to make, having already worked out in advance what options they will need, in a sort of restaurant-like menu, will allow you to make the requests more streamlined, and work better with your organization.<br>
<br>
You can add SKUs if necessary, when they have a strong need (for example, a large order of systems that have a usage pattern that do not match any of your existing SKUs), and otherwise they have an easier by simply selecting what seems best to them.<br>
<br>
This can also be done for:<br>
<br>
- Networks:  Have set ranges of IP space that you assign to a given network, such as standardizing on /23, /22 and /20.  If you only create server networks of these sizes, then it should be pretty easy to size them appropriately for a given request that needs their own network.<br>
<br>
- Load Balancing:  If you have a pre-determined set of options say using SNAT with X-Forwarded-For for all web services, then you can announce that early, and avoid running into problems where web applications require the source IP in the request.<br>
<br>
- Host names: As we went over earlier, there is a lot of information stored in names.  If you give a guideline of what your convention is, and how to apply that convention to various configurations, you can avoid being requested to make names that do not fit the convention, as you have already described how to take their configuration and put it into your naming convention.<br>
<br>
- Accessing production machines:  You should have a security policy that can be applied in a standard way to all requests.  Do you allow root logins?  Root escalation?  Sudo?  Role accounts?  Copying data to machines?   You should write each of these things down, and where you do not allow something, you should have a method for how to accomplish that goal in a manner that is consistent with your security policy.  If you do not do this, people will just work around your enforcements and create many messes as everyone does it slightly differently.<br>
<br>
It is unlikely that people who perform different roles will start to become empathetic that the work done in others' roles really does take expertise and time, since we have so much history of people not having this empathy, but we can do things to try to bridge these gaps by being aware of them and tuning our behaviors accordingly.<br>
<p id=565cd0fce08c8934484649d6a9f5b105><b><a href="#565cd0fce08c8934484649d6a9f5b105">2.3.2.1.1.1.1.1</a>: Everyone doing everything themselves is great for a boot-strap project, but just does not work in a Mission-Critical environment.  Launch NASA rocket with newbies running things?  No, experience is needed for precision and taking into account All The Things.</b></p>
<br>
One important component of all operational environments is standardization.  At the extreme end of that spectrum would be uniformity and at the other extreme everything is unique:<br>
<br>
Everything Is Uniform <---> Everything Is Unique<br>
<br>
Since we know that not everything can be uniform, since we are already starting with a base of 3 SKUs (Utility, Relational Database, Non-Relational Database), that side of the spectrum is already constrained.<br>
<br>
However, it is completely possible to have an "everything is unique" operational system, and this might be labelled something like "operational hell", where everything is a special snow-flake one-off case.<br>
<br>
In an "operational hell" environment, no change can be assumed to work for more than 1 specific case.  That case must be inspected just prior to being modified, because it could be in any type of state or configuration at all, and the only way to have reasonable confidence that the change will not break things would be to look at everything going on on the machine, all configuration, all currently running processes, and to determine through expert-understanding that the planned change will work with the existing configuration.<br>
<br>
This is the most dangerous type of environment to work in, with regards to uptime, stability, efficiency, and all the other positive attributes we want to imbrue our operational environments with.<br>
<br>
All it takes to create an "everything is unique" environment is to let everyone solve every problem in the way they see best, at the time they got the request, without communicating the changes to others, and aligning the changes so that they follow a planned path.<br>
<br>
Many requests into operations will diff from previous requests in some way, making it impossible for the current request to be handled in the same fashion as the previous request, because of those differences, but still the methods used to take care of the previous and current requests could be aligned with one another.<br>
<br>
This type of alignment does not come for free, and it does not come naturally.  It is a process that must be learned, and it takes coordination of all the different members of a team to work together in ensuring that this alignment takes place.<br>
<br>
Alignment itself has a spectrum, and is best seen at different levels of details.<br>
<br>
We can "block box" anything into:  Inputs, Outputs, Side-Effects<br>
<br>
Inputs are what comes into the black box, say HTTP requests for a web server.<br>
<br>
Outputs are what comes out of the black box, sat the HTTP response for a web server.<br>
<br>
And side-effects are what happens beyond the outputs, say that a database is updated, and a memory caching server is updated, and logs are written to storage.<br>
<br>
Black boxes are an appropriate level for a group to be able to discuss alignment, as getting into implementation details of how a web server is configured should be left to the sub-team that deals with that web server. <br>
<br>
This is to allow people and sub-teams autonomy of action, as centralized planning cannot deal with all details and all contingencies efficiently, while still allowing a larger centralized inspection of the black boxes, to achieve a total operational system alignment.<br>
<br>
There's a lot involve in this, and we will be going into more depth as we move from philosophy and general issues into implementation.<br>
<p id=e08a32902b4d3960b8ee560f8851f34f><b><a href="#e08a32902b4d3960b8ee560f8851f34f">2.3.2.1.1.1.1.2</a>: Balance to this.  What can be self-service, and what cant.  PaaS for production, IaaS for development and Ops usage.</b></p>
<br>
One goal for an operations team that has decided they want to get the benefits of comprehensive automation is to provide more and more self-service tools to the departments they support.<br>
<br>
The benefit for the operations team is that they can remain more focused on improving infrastructure, rather than performing requests that were made by other teams to simply set up, configure and change existing infrastructure.<br>
<br>
There is also a spectrum of productivity to this:<br>
<br>
Handling Requests <---> Improving Infrastructure<br>
<br>
The more of the operational team's resources (time, people) that are committed to processing requests made from outside the team (other departments, higher management), the less time the team is able to work on improving the infrastructure that exists, including improving the ability to handle the incoming requests in the first place.<br>
<br>
I have worked in many organizations where the operations team spends nearly all of their time performing requests, and almost no time improving the infrastructure, and as a result the infrastructure becomes more and more fragile as request after request is done in a manner that is not scalable or supportable, but is required to meet business timelines and direction.<br>
<br>
Achieving business goals is the reason all departments exist, so this is a good thing, in itself, but it can be performed in a manner where the business begins to not operate efficiently, and eventually starts to fail frequently, causing harm to other business goals, such as customer retention, which effects revenue.<br>
<br>
In order to handle requests efficiently, the infrastructure must be one that can reasonably be altered to support this requests, and as the business changes in scale, scope, and direction, this takes either a very well put together operational environment that is made to be changed quickly in these manners (possible, but difficult to assemble, and easy to turn less-functional), or it requires time before requests are done, to prepare the environment, or more time after the requests are done to fix the system after the fact.<br>
<h2 id=7ef5e6c23b6cb4359f88aea566c255fb><a href="#7ef5e6c23b6cb4359f88aea566c255fb">2.4</a>: What is a System?</h2>
<br>
There are a lot of ways the word "system" could be used.  We're going to look at a general version of the word first, and then a specific version for our exact purposes afterwards.<br>
<br>
When I was growing up and for the first 10 years of my career, operational engineers were called "System Administrators".  Today some people use this term derogatorily as lower-level or older style work, and while anyone can have any perspective they'd like, this is not consistent with history.<br>
<br>
I was lucky enough to spend some around professional system administrators throughout the 1980s, before I was old enough to work, and I got to see them doing core dumps and reading through the hexadecimal output to find where the problems in their code were, and even fix some problems through a hex editor.  I also got to get a bit of their practical advice and viewpoints, and I believe that after 5 or so years of professional operations work the lessons I saw back then started to filter back in to be more conscious rather than subconscious guides and role models.<br>
<br>
So what is a system?  Historically, in the computer industry, a system was often referred to as a single machine with an operating system on it, and the environment that was then configured on top of that to create a working environment.<br>
<br>
So a system was sometimes a machine's hardware, an operating system was also a system, and the eventual configured environment was a system.<br>
<br>
One of the interesting properties of the word "system" is that all of these things were and are true.  And all of these things together are also a system.<br>
<br>
A system is an generalized term for a set of interrelated, connected things that work together to produce effects.  Like anything, it is black-boxable into inputs, outputs and side effects, and has sub-components which can be similarly black-boxed, etc.<br>
<br>
So a system is a flexible term, and is something like an "environment" or an "ecosystem" in common usage.<br>
<br>
I like to think of systems as being somewhat like virtual machines, in the actual sense not in the container operating system sense.  A system's connections can be graphed, like a network, and each component and be described by the inputs, outputs and side effects it causes, and may contain many layers of other systems, and may be part of a bigger system.<br>
<br>
Why is any of this important?  Because your understanding of how systems works will determine your ability to mentally map the systems that you work with, so that you can think in terms of how those systems function.<br>
<br>
Without having this mental mapping, and having a mind that over time becomes more and more comfortable learning about systems, and understanding system intra-action and interactions, one will have gaps in their understanding.<br>
<br>
These gaps are perfectly fine if they are properly black-boxed to create a comprehensive system, where you may not know how memory data is shuttled between the RAM chips and the CPU, but you have a model for how this works, and that model, while not physically accurate in detail, has a strong correlation to reality and can be used to make good decisions and predictions.<br>
<br>
We will go deeper into Modeling in the future, but building accurate models of the systems you are working with is an important part of operations.<br>
<br>
When someone has a poor Model they are working with, they will be confused by things that occur, and are likely to have "magical thinking" ideas, like "out of nowhere, X just happened".<br>
<br>
When someone has a good Model and "X happens", they can see that X is related to Y and Z, and without first Y occurring, and then Z occurring, then X could not occur.<br>
<br>
They can trace this backwards and confirm that indeed Z occurred, and Y occurred, and so of course X was going to occur in sequence after them.<br>
<br>
For a common example of this, a web server starts to fail, and on inspection the disk is full, and on further inspection no log rotation was configured, and so the web server failing is a mechanical response to the disk filling up, which is a mechanical response to not having logs being rotated.<br>
<br>
If you do not rotate logs (or truncate them), then with any activity at all, it is guaranteed that eventually the disk will fill up, and any services which might use the disk for writes (such as logging) will fail.<br>
<br>
This is a simple system, and indeed anything can be turned into a system.<br>
<br>
The power of Systems is that they can be created at any time, to describe any thing, provided you are capable of properly black-boxing the components of the system you want to construct.<br>
<br>
You do not need to constrain yourself to existing systems, that other people have described, even when working with their work which have their own systems already described.  You can create your own systems for your own purposes.<br>
<br>
You might create alternative systems to simply understand other people's described systems.  Sometimes it is harder to understand someone else's work than your own, and so creating your own work can illuminate a subject.  <br>
<br>
As an exercise while you read this book, try to create your own systems based on "the big picture" to understand what is currently being discussed.  As new information comes in, update your system to reflect these changes.<br>
<br>
You can do this on paper, in your head, you can find software that helps you create systems quickly (like Mind Map software), or use relational databases to track discrete data.  Flow charts are one way to map systems, finite state machines are others ways, behavior trees are another way, but you can also describe them in prose, or doodles or any other way.<br>
<br>
How you describe a system is merely a view into the system, and will never cover every aspect of a system.  Only the actual components of a system describe the system, and any attempt to review the system will only give a partial insight into it.  Systems are tricky in this way, but this is also where their power comes from, because they are not limited by them either.<br>
<h2 id=61fc96e11d2dd57966d2b5b014f1a2dc><a href="#61fc96e11d2dd57966d2b5b014f1a2dc">2.5</a>: Systemic Thinking</h2>
<br>
System Thinking is one of the tools that I believe is the most powerful, and could use a lot more of the educational spotlight.  In terms of yielding positive results in learning, creating things, and in performing maintenance (in a very general sense), system thinking is one of the most useful tools.<br>
<br>
System Thinking has a number of prerequisites, such as a general understanding of how systems work, how to create systems, how to modify a system, how to inspect and evaluate the connections and links between system components, and a good basis in critical thinking.  Having the ability to thinking deductive is critical.<br>
<br>
If you have not yet read a book on critical thinking, you should to ensure you have down the basics of the topic.  Deductive and inductive thinking, boolean logic, and set logic are primary tools for doing analysis, and any troubleshooting of systems will be significantly improved if you can break things down to terms and evaluate them.<br>
<br>
How do you use System Thinking?<br>
<br>
The first thing to do is to take whatever you are thinking about, and turn it into a system.  Anything can be turned into a system, and this system can be as large or small as you need, and can contain any number of components.<br>
<br>
Since we, as humans, are limited in the number of things we can think about simultaneously, on a conscious level especially, we need to break things into small groups of related ideas.<br>
<br>
Let's create a system right now and do some reasoning with it, to use as an example.  We will continue to use the web server analogy, as it is one that many people will already be familiar with, or will probably spend a lot of time dealing with in their careers.  You can think of this as an "Application Server" instead of web server if you like, the important thing is that it takes requests and servers back data.<br>
<br>
In the simplest of web server systems, we have static content serving.  This is when someone has pre-created text (HTML, CSS, etc) and binary (images, videos) and the web server's job is to take requests for specific static files, and to relay those files to the requester.<br>
<br>
Since we can create a system out of any components, let's decide what our components will be:<br>
<br>
- A network connection to the Internet, which end-users are making requests on.<br>
- The IP protocol for networking, and basic TCP session management, on a Linux server.<br>
- A web server that listens on TCP port 80 on that server.<br>
- A file system that locally contains system files.<br>
- A file system that locally logs requests and processing.<br>
<br>
This is a slice of components involve in web process, and just as I have arbitrarily picked these for this example, you can pick any components you want to build your own systems.  You can continue to refer to the same system over time to get more familiar with all the details of that system, as is important in operational and application documentation, or you can abandon the system as soon as it's immediate purposes are over.  Systems can be used forever or can be completely ephemeral, they are abstractions for reasoning and understanding reality, which remains too detailed and complex for us to directly understand.<br>
<br>
Let's create an event that occurs and exercises these components, as a sequence:<br>
<br>
- An end-user requests a file from the remote web server: http://www.domain.com/images/unstoppabletrex.png<br>
<br>
- The request performs operations outside of this system (LAN, routing, DNS, etc), but eventually opens a TCP socket to port 80 on the web server.  The web server and the end-user now have a persistent session to communicate bidirectionally.<br>
<br>
- The end-user requests the URL specified above (broken into URI and Host Header sections), and relays any cookie and browser header information.<br>
<br>
- The web server accepts the input of the request, and goes through a process of routing the request internally, where it matches the domain in the Host Header value to any Host Headers it processes, and then determines if there are any directory modifications to look for the static file.<br>
<br>
- Having determined what the path of the static file is on the local file system, if the file exists, the web server opens the file, reads it, and relays the data into the content section of the HTTP response.  After relaying the contents, it closes the file, creates a successful HTTP status code, and returns the results.  In this case we will assume that HTTP keep-alive is not enabled, and the HTTP server will close the connection afterwards.<br>
<br>
- The end-user's web browser will have received the HTTP response, getting the status code and body of the content, and in this case will display the image to the screen.<br>
<br>
This is one way that a request event could be processed by a web server.  We can similarly model of the file does not exist, the web server may do something similar, except return a 404 File Not Found static content.<br>
<br>
In the case of a more dynamic system, the web server could proxy the request to an application server, which then makes database calls and performs formatting logic, and then returns a dynamic result instead of a static one.<br>
<br>
The important of systemic thinking in this is that there are no gaps.  Every connection that is required is modeled, and if new connections are required, they are added, and the remaining components need to be updated so that the system remains<br>
<h3 id=03071c27c692b17c5d7f95b9d4f021a4><a href="#03071c27c692b17c5d7f95b9d4f021a4">2.5.1</a>: Philosophers Knife</h3>
<h3 id=1f4b194d8569136439831f483c38a264><a href="#1f4b194d8569136439831f483c38a264">2.5.2</a>: Slicing the pie vs aggregation</h3>
<h3 id=f32b593542b3562df78d89693543c0fe><a href="#f32b593542b3562df78d89693543c0fe">2.5.3</a>: Systemic Thinking.  Philosophers Knife.  Slicing the pie vs Aggregation.  Completeness, ease of understanding, ease of building, life-cycle maintenance.  Where do you spend your time?</h3>
<h2 id=da54e5ab11aae5fc49994945cb3bc9a8><a href="#da54e5ab11aae5fc49994945cb3bc9a8">2.6</a>: Terminology</h2>
<h3 id=69371f3e438e2ed281f525ac57e65e3c><a href="#69371f3e438e2ed281f525ac57e65e3c">2.6.1</a>: Logic: code</h3>
<h3 id=9b48a00c792d88dfa31f203429758f84><a href="#9b48a00c792d88dfa31f203429758f84">2.6.2</a>: Data: data</h3>
<h3 id=aa2640c210126a47b684283980210b76><a href="#aa2640c210126a47b684283980210b76">2.6.3</a>: Rules: policies about how you do stuff</h3>
<h3 id=3393e40f9f65bba3ee24fc4f744c792b><a href="#3393e40f9f65bba3ee24fc4f744c792b">2.6.4</a>: Distributed: dealing with N nodes</h3>
<h3 id=a709b239027a030b1a2dc4d500e49a24><a href="#a709b239027a030b1a2dc4d500e49a24">2.6.5</a>: Real/Virtual.  Strict definitions.</h3>
<p id=d997d62bdfc3a11ce132fe5aade05eaa><b><a href="#d997d62bdfc3a11ce132fe5aade05eaa">2.6.5.1</a>: Physical</b></p>
<p id=90c9825a0f594625107fd59419c3f079><b><a href="#90c9825a0f594625107fd59419c3f079">2.6.5.1.1</a>: Matter, Eletricity</b></p>
<p id=f94e13d4b8fcbb599dc285bff7bdb543><b><a href="#f94e13d4b8fcbb599dc285bff7bdb543">2.6.5.2</a>: Virtual:</b></p>
<p id=41d56db0a27604bc57fe7a0b5bfe58d0><b><a href="#41d56db0a27604bc57fe7a0b5bfe58d0">2.6.5.2.1</a>: Data, Logic</b></p>
<p id=031f037060d88ef98ae42ae359b42dd0><b><a href="#031f037060d88ef98ae42ae359b42dd0">2.6.5.3</a>: Be clear about the differences:  Physical (Real), Logical (Virtual), Data (Virtual)</b></p>
<p id=5a2ee645ef74425ffa093976096dee18><b><a href="#5a2ee645ef74425ffa093976096dee18">2.6.5.3.1</a>: Can never know everything about something Real (physical), because of limited insight into what is going on with it</b></p>
<p id=e529c9c5431e0acff31b16484c63dfad><b><a href="#e529c9c5431e0acff31b16484c63dfad">2.6.5.3.2</a>: Can know everything about Virtual (Logic/Data), because they are limited, and they are fully contained and inspectable.</b></p>
<p id=dd889cf6d887f391188383b428c7ebfc><b><a href="#dd889cf6d887f391188383b428c7ebfc">2.6.5.3.2.1</a>: However, between Data and Logic is a huge gap, as Data is "perfectly" understandable, while Logic is not, due to Halting Problems and all other things CS-academia knows and describes very well.</b></p>
<p id=99b45325e58458c65965de974e2f7dc2><b><a href="#99b45325e58458c65965de974e2f7dc2">2.6.5.3.2.2</a>: This difference also tells us why Data is more important than Logic, because Data is more trustworthy than Logic.  When making changes to data, the changes are straight-forward to understand, when making changes to Logic, the side-effects (unintended consequences) can be far-reaching and completely not understandable, and frequently enough are this way.</b></p>
<p id=3b9a062658c7f15e53b7601de12d3857><b><a href="#3b9a062658c7f15e53b7601de12d3857">2.6.5.3.2.2.1</a>: Changes to data, that meets constraints, will not harm other data, but can harm Logic that acts on the data (results of Logic, rather)</b></p>
<h3 id=e2a0bb61f2d74d70b31bf533e2b1c260><a href="#e2a0bb61f2d74d70b31bf533e2b1c260">2.6.6</a>: Class of Work: a specific type of work that is done, may be domain specific or general across the company</h3>
<h2 id=af1f8c9950e296d130a668076e4ba88b><a href="#af1f8c9950e296d130a668076e4ba88b">2.7</a>: The Philosophy of Pragmatism</h2>
<h3 id=ecb2f6533d02864a3355571f4e7d17b7><a href="#ecb2f6533d02864a3355571f4e7d17b7">2.7.1</a>: It doens't mean practical, or common sense.  It is specific to the effects, and nothing else.</h3>
<p id=c88a8c2a472464982c2f1601901f744d><b><a href="#c88a8c2a472464982c2f1601901f744d">2.7.1.1</a>: Deal with ONLY effecs.  No side effects.</b></p>
<p id=c225c5097c5fbffad5f9b2d6d5fb3d43><b><a href="#c225c5097c5fbffad5f9b2d6d5fb3d43">2.7.1.1.1</a>: Show positives, not negatives.</b></p>
<p id=435b1da00f2fe0352e54a0887ca8e461><b><a href="#435b1da00f2fe0352e54a0887ca8e461">2.7.1.1.1.1</a>: How to produce low-downtime.  How to produce high-downtime.  Functinally positive or negative on our Axiom spectrums.  As prioritized by the 90-9-.9-.09... rules.</b></p>
# Chapter 3: Engineering Philosophy and Methodology in Operations






<h2 id=b313ae83a593ebeebefbf3e427c23f35><a href="#b313ae83a593ebeebefbf3e427c23f35">3.1</a>: What is Engineering?</h2>
<h2 id=a941939e629b2be25c1ba265cbd9aaed><a href="#a941939e629b2be25c1ba265cbd9aaed">3.2</a>: Difference between Application and Operational code</h2>
<h3 id=1e13f344d1ae44173a1f9532c809f6b1><a href="#1e13f344d1ae44173a1f9532c809f6b1">3.2.1</a>: Many applications and services.  One Operational environment</h3>
<p id=8eb74e570e995c459a430857793ad69f><b><a href="#8eb74e570e995c459a430857793ad69f">3.2.1.1</a>: Like 1 big computer.</b></p>
<h2 id=432075b2196c9716df5bcc2d7c070b2e><a href="#432075b2196c9716df5bcc2d7c070b2e">3.3</a>: The difference between App software dev, and Operational dev.  Robust, resilient, correct, handles failures, assumes failures will occur, is designed around failures occuring, instead of App designed around all functions being available (for the most part).</h2>
<h2 id=53ee284612b4d4678a26814fc2442067><a href="#53ee284612b4d4678a26814fc2442067">3.4</a>: Troubleshooting.  Cencentric circles.  Locality.  Intermittent vs. sustained.  The attributes of failures.</h2>
<h3 id=222b0da1a677c8319df0b5742703e46f><a href="#222b0da1a677c8319df0b5742703e46f">3.4.1</a>: Determines monitoring.</h3>
<h3 id=5e9a4e088d8a4899a4a8579fec56b098><a href="#5e9a4e088d8a4899a4a8579fec56b098">3.4.2</a>: This can be represented in a spectrum.  Ops  <---->  Application.    Backend  <--->  Front End</h3>
<p id=2cda0e85947b37088449bf5d24291155><b><a href="#2cda0e85947b37088449bf5d24291155">3.4.2.1</a>: HTML pages are very front end, web servers are less front end, DBs are less front end more back end, and OpsDB is most backend.</b></p>
<h2 id=4410772cb808c71ea7621428281fa35c><a href="#4410772cb808c71ea7621428281fa35c">3.5</a>: Evaluating changes.</h2>
<h2 id=44e191e4a8799ec4d8239c53a915b728><a href="#44e191e4a8799ec4d8239c53a915b728">3.6</a>: Perfect is the enemy of done.  Worse is better.  How much safety can you afford?</h2>
<h3 id=d98cb46eb6a0d64a68131fa80be27a81><a href="#d98cb46eb6a0d64a68131fa80be27a81">3.6.1</a>: Quality is never #1, utility is.  Once it's "good enough", it is abandoned for higher priority things.</h3>
<h2 id=ac39699dc841781b49de6156b7d47f07><a href="#ac39699dc841781b49de6156b7d47f07">3.7</a>: Explain the skill ladders.  Infinitely many ladder, infinity tall ladders.  In each area you need to advance and learn, and as you do more ladders are climbed</h2>
<h3 id=8c334623a47643e18e33479feebf5bed><a href="#8c334623a47643e18e33479feebf5bed">3.7.1</a>: Show it like a Graph:  mwMmwnUvMMm, ups and downs in different areas.  How to test yourself, understanding your skills.  Completition of projects as proof of skill, etc.</h3>
<h3 id=5e25a809a807106b545adb208a4fa99d><a href="#5e25a809a807106b545adb208a4fa99d">3.7.2</a>: Know that no one else can know your ladder positions, though they can attempt to estimate, and people are always trying to determine pecking order between themselves and other people, and often to change the pecking order by politics and power.</h3>
<h2 id=92dfc6ded926f3d44bd483b43e658db3><a href="#92dfc6ded926f3d44bd483b43e658db3">3.8</a>: Axiomatic Engineering.  My method for making decisions that are not personal, even though of course they are my personal understand and information matching to the algorithm.  Present a method for discussing engineering in this manner..</h2>
<h3 id=66087a8256206e268b334c49bc0ba5ef><a href="#66087a8256206e268b334c49bc0ba5ef">3.8.1</a>: 90-9-.9-.09% rules for priorities.  Make up your own rules if this doesnt work for you.  How to present them to people, a plan on improvining presentation.  A plan on requested for improving presentation.    If you dont come to common terms, you arent really communicating, talking past each other.</h3>
<h3 id=5c1f069a25780e9d9aff8574624089fc><a href="#5c1f069a25780e9d9aff8574624089fc">3.8.2</a>: Fashion Based Engineering.  "Blogineering".  real evaluations of the environment, agreement between team on details, moving forward.  How to do it quickly.   Honesty in public relations, be skeptical of the claims of others.  No one will state they are fuckups, but that doesnt mean they arent asked to blog about their operational endeavours anyway.  What works for them may not work for you, apply Axiomatic Engineering principles, decided by you and your team.  Use everyone for source information, but nothing as universally applicable.  It's just another idea, including this one.  In-take, evaluate, match to your environment (synthesize), iterate, evaluate, repeat.</h3>
<h2 id=291d5132845ea58ade7ea580866bf0f6><a href="#291d5132845ea58ade7ea580866bf0f6">3.9</a>: When to use statistics.  When they are applicable, when they are not.</h2>
<h3 id=18ddda391b891bf36f9b2387380f5e67><a href="#18ddda391b891bf36f9b2387380f5e67">3.9.1</a>: Across many things: appliable</h3>
<h3 id=967dc75f17be743f5b44485436fceff2><a href="#967dc75f17be743f5b44485436fceff2">3.9.2</a>: For a given thing: not applicable.</h3>
<h3 id=feb605a9dd85dcc6e0d371d023dea881><a href="#feb605a9dd85dcc6e0d371d023dea881">3.9.3</a>: Give mental exercises to prove this.</h3>
<h2 id=9b893b40e08934229116cacf12764a11><a href="#9b893b40e08934229116cacf12764a11">3.10</a>: Understanding Engineering:  Environment -> Resources -> Goal -> Actions -> Changed Environment -> Desired Effects?  Efficient use of resources?  Management of environment?</h2>
<h3 id=dd4d43fb90d90e89b351e98d3788a97c><a href="#dd4d43fb90d90e89b351e98d3788a97c">3.10.1</a>: The use of resources (overall time, people time, money, hardware, etc) to create desired effects, for a given environment.</h3>
<p id=9ed589a4467b296c2ea9dbb09ae0f49d><b><a href="#9ed589a4467b296c2ea9dbb09ae0f49d">3.10.1.1</a>: Evaluate the environment.  Know the present.  Real vs. virtual/logical.</b></p>
<p id=6f4678a0c1cc447ce97cf330abb63e6d><b><a href="#6f4678a0c1cc447ce97cf330abb63e6d">3.10.1.2</a>: Modeling.  Creating models to understand.  Creating models to control.  Not the same.</b></p>
<p id=1e2f1485f11d72e7cc37ce72c7de6775><b><a href="#1e2f1485f11d72e7cc37ce72c7de6775">3.10.1.2.1</a>: Black boxing the world.  Pragmatism and effect driven models.  Input, Output, Side-Effects.</b></p>
<p id=86a667264372ca24826a809f97ed36b8><b><a href="#86a667264372ca24826a809f97ed36b8">3.10.1.3</a>: Algorithms: Idempotency, Sequence,</b></p>
<p id=c5cff688b2a25a6cc5ab3c0301d86a54><b><a href="#c5cff688b2a25a6cc5ab3c0301d86a54">3.10.1.4</a>: Centralized vs. Decentralized.  Push vs Pull, when is it centralized?  Do you want tight control, or loose control?  Both have their effects.  People typically want tight control, or the effects of tight control (knowledge that it worked).</b></p>
<p id=5fa11c75ac5e5ee842071b89611bd9ac><b><a href="#5fa11c75ac5e5ee842071b89611bd9ac">3.10.1.5</a>: Distribute Systems.  Many node problems.</b></p>
<p id=1a38d9aa40613994ccbc55d3bd80aac3><b><a href="#1a38d9aa40613994ccbc55d3bd80aac3">3.10.1.6</a>: Distributed Data.  Where is the good data?  Where is the active data?  Are they the same?</b></p>
<p id=4f692dac9d4a18060c7ed7ab3c560bea><b><a href="#4f692dac9d4a18060c7ed7ab3c560bea">3.10.1.7</a>: Utility vs. Cloud vs. Old-School:  On Demand vs. Full Anonymous vs One-Off.</b></p>
<p id=cd0b3e19dbeb9aa7495f50e8b3698932><b><a href="#cd0b3e19dbeb9aa7495f50e8b3698932">3.10.1.7.1</a>: Named servers (1-1), position and datacenter are known.  Utilty is anonymous server, not anonymous location, position unknown, location known.  Cloud is anonymous name and location.  You dont care what server in a DC it is, or what DC it is in.</b></p>
<p id=cc126bbb155f6cf8bd48d01908206040><b><a href="#cc126bbb155f6cf8bd48d01908206040">3.10.1.7.1.1</a>: What do you have to care about?  The exact machine?  The DC in general?  Nothing, only that the service is reachable, and it can be reachable from anywhere?</b></p>
<h2 id=b897d8c3f141f288841664b42ade8068><a href="#b897d8c3f141f288841664b42ade8068">3.11</a>: Code management.  How to canary.  How to test.  Vagrant and virtual testing.</h2>
<h2 id=2d543cb2a0bfd85b80eacbcb10cf77b2><a href="#2d543cb2a0bfd85b80eacbcb10cf77b2">3.12</a>: How to select:  Frameworks, Libs, Software Tools</h2>
<h3 id=17c8887cbd04084bc3b75f577132b78e><a href="#17c8887cbd04084bc3b75f577132b78e">3.12.1</a>: Many stand alone tools will end up being replaced.</h3>
<p id=9362cba32d5a5c9dd234aecef27564d4><b><a href="#9362cba32d5a5c9dd234aecef27564d4">3.12.1.1</a>: Text and data and the purpose of the tools.</b></p>
<p id=e122b3c42185ad60077b1cc58c7f1f22><b><a href="#e122b3c42185ad60077b1cc58c7f1f22">3.12.1.2</a>: Explain DNS, DHCP, etc replacement</b></p>
<p id=957ddd798c6271497229ea774b39e478><b><a href="#957ddd798c6271497229ea774b39e478">3.12.1.2.1</a>: zones, subnets, etc</b></p>
<h2 id=27893ca25e6be2dd440c59fcc7aa321e><a href="#27893ca25e6be2dd440c59fcc7aa321e">3.13</a>: Name spaces.  Different kinds, diff uses, diff formats.  One of the 2 hard problems (+ off by 1)</h2>
<h2 id=2a00c5d80b8c51101939d282ffea333c><a href="#2a00c5d80b8c51101939d282ffea333c">3.14</a>: Differences between Ops vs Non-Ops code.</h2>
<h3 id=ae00bdb9200029912abd5c942058cf26><a href="#ae00bdb9200029912abd5c942058cf26">3.14.1</a>: Making more depencies.  Networked dependencies.  When things are broken, how will your system function?  Will it fail?  Will it make it worse?  Will it make a mess?  Will it corrupt and destroy?</h3>
# Chapter 4: Automation Philosophy and Methodology in Operations






<h2 id=92fb73bc7b038ce1ccda5ff2fbfdbd56><a href="#92fb73bc7b038ce1ccda5ff2fbfdbd56">4.1</a>: ***** Removing classes of work.</h2>
<h3 id=b7ed43cb9d71411713c556599a83a068><a href="#b7ed43cb9d71411713c556599a83a068">4.1.1</a>: Manual automation is a force multiplier.  Mistakes are also multipled.  Unintended consequences can be severe and wide-spread.</h3>
<h3 id=6715d22e2b900a354a2308f0a78af63e><a href="#6715d22e2b900a354a2308f0a78af63e">4.1.2</a>: Making people do more complicated and dangerous activtiies should not be an end-goal of automation, though it will likely be an intermediary step.</h3>
<p id=5530d1c5607e5f60f382ea9e52ce84d2><b><a href="#5530d1c5607e5f60f382ea9e52ce84d2">4.1.2.1</a>: Step with caution.</b></p>
<h2 id=80ef8721e561c4cedf7d5e7c71ded573><a href="#80ef8721e561c4cedf7d5e7c71ded573">4.2</a>: Introduce spectrum of automatability.  How automateable is something in configure X vs Y?  This is automatability.</h2>
<h2 id=24e3b555ee6f249c33c40b79fce7e744><a href="#24e3b555ee6f249c33c40b79fce7e744">4.3</a>: Working with N axis data for evaluation of properties.  Properties are scalar, but there are many dimensions to measure, and collectively they are near-infinite.</h2>
<h3 id=5b9d7b060f1397403be31640db9326c5><a href="#5b9d7b060f1397403be31640db9326c5">4.3.1</a>: Tuning your goals based on your methods.</h3>
<h3 id=45ba9f44240bd3d8eb4785969cda5301><a href="#45ba9f44240bd3d8eb4785969cda5301">4.3.2</a>: How to create your own Axioms.  Some standard axioms.  Axiomatic development.</h3>
<h3 id=ee01dd35dc1f46d2db9f2bb0383055da><a href="#ee01dd35dc1f46d2db9f2bb0383055da">4.3.3</a>: Tools to fit the job.  Testing in an operational environment.  Mock-tests, etc in a world of only side effects.  Using Vagrant and VMs to test allows these side-effects to be tested, but take time to set up.  Worth it, but you may not start there in a live environment because of all the legacy that would have to be replicated and is changing all the time in non-standard ways.</h3>
<h3 id=2694eafa373f1024fd47adf1fc0878be><a href="#2694eafa373f1024fd47adf1fc0878be">4.3.4</a>: How to standardize things.  Simplification.  The benefits and limitations.  Simpler means less options at any given time.  1-1 work is infinite precision and difficult to scale.  Simpler is can be deep precision in 1 or several ways, but does not allow all options.  Build your option matrix out of what you need, ensure all your use cases are covered.</h3>
<h2 id=024280ac08d372e795de22ac03f8aec5><a href="#024280ac08d372e795de22ac03f8aec5">4.4</a>: All processes can be automated to get a desired effect, if enough information about it is known.</h2>
<h2 id=a562892f336213a7fd2005780a71e6b4><a href="#a562892f336213a7fd2005780a71e6b4">4.5</a>: Introduce Intelligence.  Actionable Intelligence.</h2>
<h2 id=3c09a1e29d529b0e7e64d4c2cf6e026f><a href="#3c09a1e29d529b0e7e64d4c2cf6e026f">4.6</a>: Automating anything</h2>
<h2 id=18279c1b25b35838b531d26379bf8feb><a href="#18279c1b25b35838b531d26379bf8feb">4.7</a>: Total elimination of manual work.  How to remove classes of work from being necessary.</h2>
<h2 id=5ddef01855119bd34e5ea45dc320de43><a href="#5ddef01855119bd34e5ea45dc320de43">4.8</a>: Building the data and action chains, to create all workflow.</h2>
<h2 id=bab4fcb00ea2749653c2a43573413ce6><a href="#bab4fcb00ea2749653c2a43573413ce6">4.9</a>: The data requirements:  Authentication, Authorization, Versioning, Change Management, Deployment, Pre-Post Deployment Actions, Schema Management</h2>
<h2 id=08a271c1b1d52b0b22293cc0aa24981f><a href="#08a271c1b1d52b0b22293cc0aa24981f">4.10</a>: How to construct an unbreakable process.  How to stop that process from being completed/sealed, so that it breaks.  How to ensure it breaks all the time, by setting conditions accordingly.</h2>
<h3 id=0667659ec138ba985e276e32c2c874a5><a href="#0667659ec138ba985e276e32c2c874a5">4.10.1</a>: Faux-automation.  Manual automation.  Automation-assist.  Full-automation.  Comprehensive Life-Cycle automation.</h3>
<h3 id=cc4e2b2b382a5b8203afd5f7c286d1e7><a href="#cc4e2b2b382a5b8203afd5f7c286d1e7">4.10.2</a>: This can be started as Procedure for Humans, but it will not be unbreakable, as people will make mistakes entering data (running commands is entering data)</h3>
<p id=4952dddaa19b91207fda5e21b66cb544><b><a href="#4952dddaa19b91207fda5e21b66cb544">4.10.2.1</a>: Entered on the right system?  Right command?  Right args?  Right path?  Right data?  Right goal?  Right everything?</b></p>
<h2 id=55fc6a2fc3929e32f3e6aa8c650e52c3><a href="#55fc6a2fc3929e32f3e6aa8c650e52c3">4.11</a>: Flexibility and dangers of an automation system.</h2>
<h2 id=9d7a7dfb8deeb7338094c604cb4d6853><a href="#9d7a7dfb8deeb7338094c604cb4d6853">4.12</a>: Distributed OS.  DOS.  N units, all being controlled, configured and scheduling work.</h2>
<h3 id=10b09a38df50bfa7e5a5c390d4cfffad><a href="#10b09a38df50bfa7e5a5c390d4cfffad">4.12.1</a>: Does not need a "traditional" cluster scheduler.  Can use these these for "cron" type jobs though.</h3>
<h2 id=9fbbf8329fb60dc10037a5af19f31002><a href="#9fbbf8329fb60dc10037a5af19f31002">4.13</a>: Monitoring is the heart of automation.  You cant control what you dont have info on.</h2>
<h3 id=e52665a326340a943354050c831ed263><a href="#e52665a326340a943354050c831ed263">4.13.1</a>: Instelligence:  Actionable?  Timely?  Relevant?  Correct?  (Cross check it, all must align)</h3>
<h2 id=8ffdb0c910c1a74549d0d30d43ee3420><a href="#8ffdb0c910c1a74549d0d30d43ee3420">4.14</a>: Behavioral AI.  An expert system, build by experts in Ops and Biz goals.</h2>
<h3 id=3fa9092174f6aa792fa739418160f025><a href="#3fa9092174f6aa792fa739418160f025">4.14.1</a>: Do not use fuzzy info until you have exhausted discrete/precise info.  And turn the fuzzy info into a discrete/precise data point, so it can be acted on cleanly by logic.</h3>
<h3 id=102b1d39363d43827086af170dbc6c22><a href="#102b1d39363d43827086af170dbc6c22">4.14.2</a>: N of M failures is not fuzzy, even though it has a scalar value, and not boolean.</h3>
<h2 id=ab57d26b3045a6b20cffdd14faba910c><a href="#ab57d26b3045a6b20cffdd14faba910c">4.15</a>: 3 States:  Now, Desired, Current State (Whats Out there?)</h2>
<h3 id=734e804607130b865c31b46d6cfbafb8><a href="#734e804607130b865c31b46d6cfbafb8">4.15.1</a>: How to manage.  Importing, synthesizing, checking.</h3>
<h3 id=2c53820f8696b9c71bf7779bf141f713><a href="#2c53820f8696b9c71bf7779bf141f713">4.15.2</a>: Versioning, commits, pre/post-commit logic.</h3>
<h2 id=c8d4ceee72c4e9bec9a140aab31af0a7><a href="#c8d4ceee72c4e9bec9a140aab31af0a7">4.16</a>: Agent model.  Centralized model.</h2>
<h2 id=8df33f2e3ab42652f8dbc974a55ade69><a href="#8df33f2e3ab42652f8dbc974a55ade69">4.17</a>: Library model.  RPC model.  Framework model.</h2>
<h2 id=8f3dc2bb1b918f96ed62f145545bf67d><a href="#8f3dc2bb1b918f96ed62f145545bf67d">4.18</a>: ORM vs wrapping lib vs straight SQL/data query.</h2>
<h2 id=a287441fde41b224c7f9d96589d445b0><a href="#a287441fde41b224c7f9d96589d445b0">4.19</a>: Scales,  1000s/millions, not billions.  Can make this "configuration scale" not "production deployment end-user scale".  Optimize only when necessary, use tools that do heavy lifting for Time series data analysis, and import results and last N snippets into OpsDB.</h2>
<h2 id=e75b67627fcd0302ecae6162320e7b36><a href="#e75b67627fcd0302ecae6162320e7b36">4.20</a>: Selective Data Updating for Pyramid method and Mesh method.</h2>
<h2 id=8e5a823181660693663ac9171ea437f7><a href="#8e5a823181660693663ac9171ea437f7">4.21</a>: Compare Pyramid vs Mesh (p2p).  Pros and cons.</h2>
<h2 id=52c5a2714542df457a2f43133a312847><a href="#52c5a2714542df457a2f43133a312847">4.22</a>: Introduce the dotted notation as a universal naming convention, for lookups, it can universally address any type of DAG data:   domain.sub.thing.11.field.subfield.11.arrayfield.20.subsubfield</h2>
<h3 id=9d4135ad596f06c4521954e1f4b1e02f><a href="#9d4135ad596f06c4521954e1f4b1e02f">4.22.1</a>: **** Use this DAG lookup to go into YAML, DBs, etc.  Schema Man can allow this.  Can use sub-searches like globs (domain.thing.*.field) and translate that into SQL or whatever for more advanced usage.</h3>
# Chapter 5: Components of Operational Environments






<h2 id=e0456dfc4344813c454b2832f721d7cc><a href="#e0456dfc4344813c454b2832f721d7cc">5.1</a>: Troubleshooting</h2>
# Chapter 6: Components of Automation Environments






<h2 id=a26d014573a051d21bf35b17d0eda041><a href="#a26d014573a051d21bf35b17d0eda041">6.1</a>: The process of building this system in your organization.</h2>
<h3 id=87e63ce8f2071f53f8805c0cd6fc706e><a href="#87e63ce8f2071f53f8805c0cd6fc706e">6.1.1</a>: Collect all unique data in one place.  Ensure it is accurate by checking against reality, and combing through it manually to see if things line up, spot checking and automation checking every one by script.</h3>
<h3 id=f36abc40f33f81d73b6b8fd94bc37ff3><a href="#f36abc40f33f81d73b6b8fd94bc37ff3">6.1.2</a>: Things that are unique to you, vs things that are general to everyone.</h3>
<p id=0623d9b6199fbeb9e183439df55431b9><b><a href="#0623d9b6199fbeb9e183439df55431b9">6.1.2.1</a>: FQDNs, IPs, HW specs, OS specs, configuration variables, specific workflow and stuff.</b></p>
<h2 id=7007cad30eb5ca34743dbc74ecb214d6><a href="#7007cad30eb5ca34743dbc74ecb214d6">6.2</a>: Imaging vs re-building from scratch</h2>
<h3 id=5016b7b3143e119640e94393d4b76590><a href="#5016b7b3143e119640e94393d4b76590">6.2.1</a>: Correctness, up-to-date, vs speed.</h3>
<h2 id=206e9c61bb5ef53bbded00a8c8964b9e><a href="#206e9c61bb5ef53bbded00a8c8964b9e">6.3</a>: *** The Progression of an Automation System:  Walk through all the stages **</h2>
<h3 id=6dab388a16ed3d77edcd61d24e22f562><a href="#6dab388a16ed3d77edcd61d24e22f562">6.3.1</a>: These shouldnt be an order so much, as people can take different routes.   How to evaluate each of these spectrums/axis of data, scalars, would be good.</h3>
<h3 id=d7b7edd2b384d2fb2aa8ae8da1767599><a href="#d7b7edd2b384d2fb2aa8ae8da1767599">6.3.2</a>: Manual everything</h3>
<h3 id=1451f4580715a78839eb3ada548626a9><a href="#1451f4580715a78839eb3ada548626a9">6.3.3</a>: Kickstarts and auto config  (AWS gets you here)</h3>
<h3 id=1c20fb798339d70263c0b78365f27f78><a href="#1c20fb798339d70263c0b78365f27f78">6.3.4</a>: Sys configuration tools, Monitoring, Centralized Logging, etc.  Normal sys admin process.</h3>
<h3 id=8744736462545259d69fc1e0eacdc78a><a href="#8744736462545259d69fc1e0eacdc78a">6.3.5</a>: Issue tracking systems, change management ticket systems.</h3>
<p id=611430f5641a791eec9fda109deaecde><b><a href="#611430f5641a791eec9fda109deaecde">6.3.5.1</a>: Good to have different CMS for tickets, because your ops logic will change, but its more useful to track the CMS data right in the ops db for a real record of things, because it lists the complete workloads.</b></p>
<h3 id=1fc55849153c719e757bb6cba8124d73><a href="#1fc55849153c719e757bb6cba8124d73">6.3.6</a>: Databases for assets, inventory, etc</h3>
<h2 id=4f78d48397b0d75399cddbac6661aa4f><a href="#4f78d48397b0d75399cddbac6661aa4f">6.4</a>: * The more sources of authoritative data, the more data drift and non-alignment between the data (fields tracking similar but non-matching things, naming differences, not able to point to same primary keys, etc)</h2>
<h2 id=c60e4b0680418499aa5840cafca907a5><a href="#c60e4b0680418499aa5840cafca907a5">6.5</a>: Data survives longer than code/logic, business logic stays all the time, but the assets described in the DB remain the same, even if they are used differently, and different meta-data is stored about them.</h2>
# Chapter 7: The OpsDB






<h2 id=64bbdc8ed0e1e42739b42a4fc419e08e><a href="#64bbdc8ed0e1e42739b42a4fc419e08e">7.1</a>: What is it?</h2>
<h3 id=6d85b906bd9d454887125ebb31840c17><a href="#6d85b906bd9d454887125ebb31840c17">7.1.1</a>: Your OpsDB is the desires and actionable knowledge of your company.  Everything inside it can be acted upon, it is better global information than any single person can have, so it is the best communication mechanism for a system that has multiple people with their own information (all companies over 1 employee).  Synchronizes information, makes transactional.</h3>
<h3 id=f9918b64d4f419d98d2f8342088bea27><a href="#f9918b64d4f419d98d2f8342088bea27">7.1.2</a>: Setting realistic expectations for this project will be one of your biggest challenges.  Once the premise is understood, it is difficult to stop "magical" thinking about the project, as the intention is to solve all solvable problems, people see it as a magic machine.</h3>
<h3 id=3140a4b8520344ef6af72c4b6709e379><a href="#3140a4b8520344ef6af72c4b6709e379">7.1.3</a>: It is a system or "machine" that can be used to solve all problems, in that it is a centralized database and method for acting against that data.  That is immediately a universal set of tools, because every piece of software is data with a method for acting against it.</h3>
<h2 id=febf95c8835573c89a43474f25043f21><a href="#febf95c8835573c89a43474f25043f21">7.2</a>: Data Driven Design:  My methodology.  Start with the data, work from there.  Testing against data is key.</h2>
<h3 id=addcf00c3304307ee3ec5717fab5c768><a href="#addcf00c3304307ee3ec5717fab5c768">7.2.1</a>: Separate data changing logic from non-data changing logic.  This is like the Model/Controller separation, but is different because it is about any type of action, not just GUI-like actions.</h3>
<h3 id=63ca29ecfdbd33f8b82529d48bf7e2f6><a href="#63ca29ecfdbd33f8b82529d48bf7e2f6">7.2.2</a>: Work systems.  Distributed Job schedulers.</h3>
<h3 id=b9188413cc8c6606506e014873b6b930><a href="#b9188413cc8c6606506e014873b6b930">7.2.3</a>: Collection of data:  Events (logs/etc), Time Series, Config State (md5sum, etc), Active/Live State (up/down)</h3>
<h3 id=727550ddb6653e016e1496f196e288ac><a href="#727550ddb6653e016e1496f196e288ac">7.2.4</a>: Data Driven Development.  My methodology.</h3>
<p id=c2f8690440b17c7c50567db20222ffe1><b><a href="#c2f8690440b17c7c50567db20222ffe1">7.2.4.1</a>: Start with data.  Fo over all features as represented in data.</b></p>
<h2 id=f233ed09310a458264d313be344b885a><a href="#f233ed09310a458264d313be344b885a">7.3</a>: The Data (base)</h2>
<h3 id=b81585e0fda170c7250649704866ac0a><a href="#b81585e0fda170c7250649704866ac0a">7.3.1</a>: Modeling off of reality.  Logical ideas change all the time, business decisions and directions change all the time, staff changes regularly, reality will hold true, but it's perceived differently by everyone.  Still trying to map to reality gives the most common information to the most people who will work with it, and a common method of communication, and is therefore better than not.</h3>
<h2 id=eb0781821183170b505cc3d53ed8f810><a href="#eb0781821183170b505cc3d53ed8f810">7.4</a>: Naming conventions.  Set them and try to abide by them consistently.  This will determine how frequently things must be looked up to be used, for someone familiar with the sytem.  Python vs PHP.</h2>
<h2 id=88eefb88d8bdddb29a06e49470b741b5><a href="#88eefb88d8bdddb29a06e49470b741b5">7.5</a>: My rules:  No plurals in data (code is ok), strict lookup methods, limit methods of relationality.  DAG lookups, with normalized relations in data (not-DAG, has cycles, data doesnt have a direction when there are cycles, the search could start anywhere).</h2>
<h2 id=580a184d5471cd2ae0aa2951fafffcee><a href="#580a184d5471cd2ae0aa2951fafffcee">7.6</a>: What tools you will need to manage this data.   Problems with ORM, problems with non-ORMs.  The tools chosen will determine the level of automatability.</h2>
<h2 id=af2c0408d1a232656d0845019e4790ef><a href="#af2c0408d1a232656d0845019e4790ef">7.7</a>: Building the logic system.</h2>
<h3 id=c587a72562db2e142ed7bce6ba82c2fb><a href="#c587a72562db2e142ed7bce6ba82c2fb">7.7.1</a>: Ensuring uniqueness of elements that require guarantees.</h3>
<h3 id=d02f1a4ff1c843265bfaa4d20accf4d0><a href="#d02f1a4ff1c843265bfaa4d20accf4d0">7.7.2</a>: Infrastructure.  Pre-Services.</h3>
<h3 id=37233edbc6bbf446d6353f066766b5d4><a href="#37233edbc6bbf446d6353f066766b5d4">7.7.3</a>: Configuration of Services.</h3>
<h3 id=06bfc3797691d54fdd6e34c13c4e2ec3><a href="#06bfc3797691d54fdd6e34c13c4e2ec3">7.7.4</a>: Monitoring of Services.</h3>
<h3 id=e01a2cff836d04f498744d984298c363><a href="#e01a2cff836d04f498744d984298c363">7.7.5</a>: Life-Cycle Management of services.</h3>
<h2 id=2e7bd70786c580dcfbd4a9115bf0bb8f><a href="#2e7bd70786c580dcfbd4a9115bf0bb8f">7.8</a>: The layers of an automation system:</h2>
<h3 id=63b722744987837de93cab18cb980051><a href="#63b722744987837de93cab18cb980051">7.8.1</a>: Description of environment</h3>
<h3 id=cd394f4051b52bbe62e5ebb2cd8310ff><a href="#cd394f4051b52bbe62e5ebb2cd8310ff">7.8.2</a>: Provisioning</h3>
<p id=3ccd753ebf4dc31d41da2ddd58d657d6><b><a href="#3ccd753ebf4dc31d41da2ddd58d657d6">7.8.2.1</a>: One-Time configuration</b></p>
<p id=2ea0777930172d51b11974c4b9870340><b><a href="#2ea0777930172d51b11974c4b9870340">7.8.2.2</a>: Continuous Configuration</b></p>
<p id=60fee5b4808b14ad3b519f3642b92ba9><b><a href="#60fee5b4808b14ad3b519f3642b92ba9">7.8.2.3</a>: State management</b></p>
<p id=8959758dbd6b6f3cf8506033ed26a74e><b><a href="#8959758dbd6b6f3cf8506033ed26a74e">7.8.2.4</a>: One-time actions (manual state control of distributed systems)</b></p>
<p id=b7738190443498e5389dd4bb606b3213><b><a href="#b7738190443498e5389dd4bb606b3213">7.8.2.5</a>: Maintenance actions (taking offline)</b></p>
<p id=dc1141d3dbdaed262a31451319e4a0d6><b><a href="#dc1141d3dbdaed262a31451319e4a0d6">7.8.2.6</a>: Marking broken HW, fixing HW, migrating OS positions.</b></p>
<p id=dadcbabed40306c7ac679c0ce0715aca><b><a href="#dadcbabed40306c7ac679c0ce0715aca">7.8.2.7</a>: What stays the same, what changes?  IPs for LOM on HW.  IPs for OSes on virtual.</b></p>
<p id=47628abed8e1db8e9ed815f84bb4d116><b><a href="#47628abed8e1db8e9ed815f84bb4d116">7.8.2.8</a>: Tracking N things.  Primaries vs. position.  Ordered lists are the best?</b></p>
<h2 id=c5e3fc0965c2fdd764070ce7089ab03e><a href="#c5e3fc0965c2fdd764070ce7089ab03e">7.9</a>: How to "translate" data changes, making many changes at once, like matrix multiplication.  Changing from Puppet to Salt, etc.</h2>
<h2 id=1431f5a1f11b9fb451cc24ff2fee85c5><a href="#1431f5a1f11b9fb451cc24ff2fee85c5">7.10</a>: How to Build your own OpsDB.  What you need:</h2>
<h3 id=9853534dc81b1e9e41d72d4363f0a542><a href="#9853534dc81b1e9e41d72d4363f0a542">7.10.1</a>: View (Webpage, API)</h3>
<h3 id=276746c8ba1e2809eb7df2308d002381><a href="#276746c8ba1e2809eb7df2308d002381">7.10.2</a>: DB Backend</h3>
<p id=ff326af388f41f4924ffad21eb1dfed3><b><a href="#ff326af388f41f4924ffad21eb1dfed3">7.10.2.1</a>: Method for safely making changes to data</b></p>
<p id=036106589f472c34b5d06d007dea3f2b><b><a href="#036106589f472c34b5d06d007dea3f2b">7.10.2.1.1</a>: Versioning, Change Management</b></p>
<p id=1cdc99a3dfdde59fb854db0175cb63c4><b><a href="#1cdc99a3dfdde59fb854db0175cb63c4">7.10.2.1.1.1</a>: Roll backs</b></p>
<p id=c49dd8f1c6c2c694c834e61f716fb0fa><b><a href="#c49dd8f1c6c2c694c834e61f716fb0fa">7.10.2.1.1.2</a>: Pre-Post Commits</b></p>
<p id=0e83ef919a005decfa42731ac7f54b07><b><a href="#0e83ef919a005decfa42731ac7f54b07">7.10.2.1.1.3</a>: Locking, to stop problematic race conditions</b></p>
<p id=019b9ff6745a81e4c068d893c7f13852><b><a href="#019b9ff6745a81e4c068d893c7f13852">7.10.2.1.1.3.1</a>: Channeled locking, to limit domains of locks</b></p>
<p id=80bc1f096de2420328753be58a57dceb><b><a href="#80bc1f096de2420328753be58a57dceb">7.10.2.1.1.3.1.1</a>: Size of domain, and rate of change and lock duration determine requirements</b></p>
<p id=5d14c394196a168616acd71cd98b3e1d><b><a href="#5d14c394196a168616acd71cd98b3e1d">7.10.2.1.2</a>: Single choke point for DB changes</b></p>
<p id=b0cb8e8e7ef02730d62e746be34c4735><b><a href="#b0cb8e8e7ef02730d62e746be34c4735">7.10.2.1.2.1</a>: Web/API all use the same code, so different paths give different results.</b></p>
<p id=f17e11f935b8c1a4aa11102e9f73223e><b><a href="#f17e11f935b8c1a4aa11102e9f73223e">7.10.2.1.2.2</a>: Role users (scripts) can auto-commit changes, but should go through same process, because needed for auditing, troubleshooting, and maintaining integrity and pre/post-commit logic</b></p>
<h3 id=540cf17fe6e0e04bd037e55d7ce2f5ce><a href="#540cf17fe6e0e04bd037e55d7ce2f5ce">7.10.3</a>: Pull method, to gather data.  Time Series, Logs, State/Configs, Events, etc</h3>
<p id=c4337517e5ddb7098a69ab9ea06a54fe><b><a href="#c4337517e5ddb7098a69ab9ea06a54fe">7.10.3.1</a>: Creates Global Authority DB</b></p>
<p id=a12e034abf7648e012dba8f6624f26f3><b><a href="#a12e034abf7648e012dba8f6624f26f3">7.10.3.1.1</a>: Can be distributed, if sync. is strong</b></p>
<p id=462d69372dfef02a563fa6444c55cd24><b><a href="#462d69372dfef02a563fa6444c55cd24">7.10.3.1.1.1</a>: Need Transactions on all pieces of total DB, so that things are changed in block fastion, all this way, then all that way.  Keeping alignment.  (Like a shot in Pool, game.  Stick and balls must line up to make it into the pocket.)</b></p>
<p id=277518558b3f7c13c97da337398a3239><b><a href="#277518558b3f7c13c97da337398a3239">7.10.3.1.1.2</a>: Will come later in the process, in the "How to implement" section</b></p>
<p id=dc439f9efa60e2ef3a3b7a76233e90b4><b><a href="#dc439f9efa60e2ef3a3b7a76233e90b4">7.10.3.1.2</a>: Selective Replication.  Will have local and global portions.   Easy to separate instances (2 MySQL instances) so taht there is a Global DB (replicated from Master) and a Local DB, pulled from Local, which replicates to Master.</b></p>
<p id=36da14c0258aed53bb129e50b7540c0b><b><a href="#36da14c0258aed53bb129e50b7540c0b">7.10.3.1.2.1</a>: In this scenario, the Master will need to have N instances, where N is the number of sub-masters, so it can replicate.  Then it will pull and integrate this data into it's own global system, and then synthesize.</b></p>
<p id=8a7a7c7b2388bd544de92c5e305fac1b><b><a href="#8a7a7c7b2388bd544de92c5e305fac1b">7.10.3.1.2.1.1</a>: This Global pull-integrate-synthesize is then replicated out everywhere, and is the REAL data that can be acted upon.  It has met all constraints and has a view into everything</b></p>
<p id=acd4663d59d1c72e97ec62dfc8144a85><b><a href="#acd4663d59d1c72e97ec62dfc8144a85">7.10.3.1.2.1.1.1</a>: Some Logic can run off of Local data, because it is locally concerned.  When Logic needs to act on Global data, its obvious it needs to be correct and current global data.  Intelligence.</b></p>
<p id=bed7228195793a630892b855fc99a256><b><a href="#bed7228195793a630892b855fc99a256">7.10.3.1.2.2</a>: Collection is local.  Work from Global.</b></p>
<p id=87f7c87b586607ad6a5f02b42dbc6fd9><b><a href="#87f7c87b586607ad6a5f02b42dbc6fd9">7.10.3.1.2.2.1</a>: How to work on partitioon?</b></p>
<p id=d7f9ae8a09db2ce495f7b9c3de1765c2><b><a href="#d7f9ae8a09db2ce495f7b9c3de1765c2">7.10.3.1.2.2.1.1</a>: Can use local data for N time, until is stale.  Logic can decide how stale the data can be, can have Rules for lag time allowances.</b></p>
<h3 id=a00ef370998cbb3006289af9b995a5b9><a href="#a00ef370998cbb3006289af9b995a5b9">7.10.4</a>: Orchestration.  Remote Execution.  Seall the loop and check.  Post-Provisioning will need to run commands to check that things really worked.  Same as any other type of action. Do the action, get the result, but then go check and make sure it worked.  Check again to see if it failed after some time.  Ensure another action hasnt caused this (acted on the same Resource)</h3>
<h3 id=db268b9d5648f3cf17247aa4466aca44><a href="#db268b9d5648f3cf17247aa4466aca44">7.10.5</a>: Config Management.  Make known changes on a system.  It should be in "X state"</h3>
<h3 id=0a8618fa5985ed1fdc24f110dc27c026><a href="#0a8618fa5985ed1fdc24f110dc27c026">7.10.6</a>: State Management.</h3>
<p id=8b695cbf41a4ec0c65cc346d3f4ec397><b><a href="#8b695cbf41a4ec0c65cc346d3f4ec397">7.10.6.1</a>: OS Level</b></p>
<p id=13c2c758c5deddeef82f376abc18fd9d><b><a href="#13c2c758c5deddeef82f376abc18fd9d">7.10.6.2</a>: Service level (dealing with the execution of services, and proper functionoining of the service)</b></p>
<p id=c4dcd142e927de912d9547bc2fdc0b04><b><a href="#c4dcd142e927de912d9547bc2fdc0b04">7.10.6.3</a>: Running-Service level (dealing with things inside a running service.  This is a user of the service, instead of a controller, but it is an "administrative" type of use)</b></p>
<h3 id=dd58ffaa4ecbdac2411f233050464747><a href="#dd58ffaa4ecbdac2411f233050464747">7.10.7</a>: Work Scheduling</h3>
<p id=a70b03745f8075613c39c401fa6ebb3c><b><a href="#a70b03745f8075613c39c401fa6ebb3c">7.10.7.1</a>: Global cron jobs, etc.</b></p>
<p id=1ba95b39f638a0a938fe583f13451394><b><a href="#1ba95b39f638a0a938fe583f13451394">7.10.7.1.1</a>: In maint?  Is right machine (master/slave/role/etc)?  Dont take down prod.</b></p>
<p id=b0daa3658be541aa293ab0b9ded206da><b><a href="#b0daa3658be541aa293ab0b9ded206da">7.10.7.1.2</a>: Dont ignore failures of jobs.  Keep logs for auditing, so we know what happened, and what it happened for troubleshooting and Root Cause Analysis.</b></p>
<p id=0044ef67424877e39c1ba3c6053e8c31><b><a href="#0044ef67424877e39c1ba3c6053e8c31">7.10.7.1.3</a>: Track times for analysis to determine failures of scale-performance changes</b></p>
<h3 id=fb473bfadfe142c63f22f088a56d5977><a href="#fb473bfadfe142c63f22f088a56d5977">7.10.8</a>: Capacity Planning.  When will you run out of:  Disk? RAM?  CPU? Connections?  etc</h3>
<p id=0c6c6113cb02a2a1ff6e897237e5402b><b><a href="#0c6c6113cb02a2a1ff6e897237e5402b">7.10.8.1</a>: Resources of our services.  Network Loadbalancer has N potential connections, and we can determine that by a MAX check on how much its done, and where it has produced failures after MAX_WORKING values have been breached.  Might not be the LB though, just correlation.</b></p>
<h3 id=a6e21acd13a2849ee9c611451ba8b30a><a href="#a6e21acd13a2849ee9c611451ba8b30a">7.10.9</a>: Access Control.  Authorization to do work.</h3>
<h3 id=e3cba7be54f69ef1b2d51192e0ef633e><a href="#e3cba7be54f69ef1b2d51192e0ef633e">7.10.10</a>: Deployments, as separate from Config</h3>
<p id=f05b48f95386109c5c79cfc128fc44e3><b><a href="#f05b48f95386109c5c79cfc128fc44e3">7.10.10.1</a>: Code deploy</b></p>
<p id=1d1be487a8a4d497425c60ca93d25285><b><a href="#1d1be487a8a4d497425c60ca93d25285">7.10.10.2</a>: Data/Schema deploy</b></p>
<p id=f08b1ca1ab0f2290f2a2c3b8b8b97ffc><b><a href="#f08b1ca1ab0f2290f2a2c3b8b8b97ffc">7.10.10.2.1</a>: When tied together.  Ways to avoid problems, ways to increase problems.</b></p>
<p id=ed24cd5011374fb609ff91ea5d18cc17><b><a href="#ed24cd5011374fb609ff91ea5d18cc17">7.10.10.2.2</a>: Lifetimes, rate of change, etc</b></p>
<p id=88ff2ffdc4b027db0a400a53602c0063><b><a href="#88ff2ffdc4b027db0a400a53602c0063">7.10.10.2.3</a>: Service up/down.  In/out of LB.  (Active)</b></p>
<h3 id=938f106673899a434d955e75ed15a20a><a href="#938f106673899a434d955e75ed15a20a">7.10.11</a>: Network config and planning</h3>
<p id=95c64ed20fa4a1dbb04c67f0aea42b82><b><a href="#95c64ed20fa4a1dbb04c67f0aea42b82">7.10.11.1</a>: VLANs.  Hidden systems, ensure not old IPs (collisions)</b></p>
<p id=19579404710a661869e4eea32f5e1c96><b><a href="#19579404710a661869e4eea32f5e1c96">7.10.11.1.1</a>: Can defer their use until that HW is proven to not use that IP anymore.  Like its in Escrow.  Once really released, it can be re-used.   Nice.</b></p>
<p id=8307c8ed240946f143913fa06d1021f4><b><a href="#8307c8ed240946f143913fa06d1021f4">7.10.11.2</a>: LOM IPs stay with the hardware.  DHCP timeouts, etc.  Server IPs stay with "ServerInstance" (OSInstance)</b></p>
<h3 id=203ffd1d4778494bd7a2556c2a0ac90e><a href="#203ffd1d4778494bd7a2556c2a0ac90e">7.10.12</a>: VM Provisioning.  Hybrid.</h3>
<h3 id=f7ae4f5ab54c3927652049bdcf35e555><a href="#f7ae4f5ab54c3927652049bdcf35e555">7.10.13</a>: Self Service tools.</h3>
<h3 id=276b07fae87391ca794e8587e972cf4e><a href="#276b07fae87391ca794e8587e972cf4e">7.10.14</a>: How to plan to do this in your existing environment.  A map from:  Here -> There.</h3>
<h2 id=dc9b1c51ebd041941929fe8845a2c78e><a href="#dc9b1c51ebd041941929fe8845a2c78e">7.11</a>: States of machines:  Unknown, Unprovisioned/Spare, Provisioned-Inactive, Active, In Maintenance, Transition-To X State, Broken, Fixed (waitig to be Unprovisioned/Spare)</h2>
# Chapter 8: How to Implement the OpsDB in your Current Environment






<h2 id=4e188beb6a9e453253679bb857ac7767><a href="#4e188beb6a9e453253679bb857ac7767">8.1</a>: The OSI layer for getting things done:</h2>
<h3 id=458b9365b935744307dce791d0f73ea6><a href="#458b9365b935744307dce791d0f73ea6">8.1.1</a>: Physical.  Real world things.</h3>
<p id=7543ac663d8be861d64b607357cbc148><b><a href="#7543ac663d8be861d64b607357cbc148">8.1.1.1</a>: People are always required for real world things, because robots arent good enough yet.  Physical must manage physical.</b></p>
<h3 id=a782fd2d1471fc65afd9abcdc78c14ed><a href="#a782fd2d1471fc65afd9abcdc78c14ed">8.1.2</a>: Configuration.  How real world things are configured.</h3>
<p id=719bc5f15fa7d54e8a67977bf0901094><b><a href="#719bc5f15fa7d54e8a67977bf0901094">8.1.2.1</a>: Logical.</b></p>
<h3 id=6331cb83195fd5b2bd738c89abc4ec84><a href="#6331cb83195fd5b2bd738c89abc4ec84">8.1.3</a>: State.  How real world things are managed.</h3>
<p id=719bc5f15fa7d54e8a67977bf0901094><b><a href="#719bc5f15fa7d54e8a67977bf0901094">8.1.3.1</a>: Logical.</b></p>
<h3 id=b53ddf4dc4025191a641f212d24e1be3><a href="#b53ddf4dc4025191a641f212d24e1be3">8.1.4</a>: Automation.  How software can manage configuration and state.</h3>
<p id=32f7e1e930dc786f657dc6a88b1bbde3><b><a href="#32f7e1e930dc786f657dc6a88b1bbde3">8.1.4.1</a>: Automation ends where people begin.  If you have no automation, the people manage the config and state.</b></p>
<p id=95e40183969996603b8e5e3425a932c4><b><a href="#95e40183969996603b8e5e3425a932c4">8.1.4.2</a>: Automation is the control of logical devices and state.  It does not control Physical devices, but does control their state.  (Even in the case of directing a physical robot, the automation updates state, and it takes something physical (motors, servos, cogs) to make the physical thing move.)</b></p>
<h3 id=173c2bec1142197f6757fcb7d4a8dbbf><a href="#173c2bec1142197f6757fcb7d4a8dbbf">8.1.5</a>: Process (and Procedures).  How people work around the lower levels.</h3>
<h3 id=8e203f62002cbf6f27b191f991da6f30><a href="#8e203f62002cbf6f27b191f991da6f30">8.1.6</a>: Policy.  Dictates how processes can be implemented.  Policies may be directly contradicting Process, such as "No one is allowed to X", while a process requires a person to do exactly that.</h3>
<h3 id=7fdcde9fe4218f5aa5a0a40cc5501fbd><a href="#7fdcde9fe4218f5aa5a0a40cc5501fbd">8.1.7</a>: Business...  Business goals</h3>
<h3 id=9fe2a787f3e54166e4252165680a59d2><a href="#9fe2a787f3e54166e4252165680a59d2">8.1.8</a>: Political.  The realities of the business goals, determined by how well people will work together to achieve them.</h3>
<h3 id=3ff1735de8bc414c4f645abe641ad297><a href="#3ff1735de8bc414c4f645abe641ad297">8.1.9</a>: Financial...  Financial reality, approved or not.  Timing.  Delays.</h3>
<h3 id=b982d3de81bba13dd46914991650f426><a href="#b982d3de81bba13dd46914991650f426">8.1.10</a>: Legal...  Hard stop, must change direction if told by legal.</h3>
<h2 id=3f2cc3566a84cad0a234647ab1300021><a href="#3f2cc3566a84cad0a234647ab1300021">8.2</a>: Planning for projects in the real world</h2>
<h3 id=236e9bb833a610161cfbaaba9e6bb6fe><a href="#236e9bb833a610161cfbaaba9e6bb6fe">8.2.1</a>: The end-date comes first.  Whether you have any say in that is only occassionally true, even if you are asked how long it will take.</h3>
<h3 id=cba0d1f4cdd7b395395d6b34e6523e97><a href="#cba0d1f4cdd7b395395d6b34e6523e97">8.2.2</a>: Things will interrupt your work that were not planned for in the time estimates, and this will mean less work gets done</h3>
<h3 id=c7eec3bac3f711b65028b49170529559><a href="#c7eec3bac3f711b65028b49170529559">8.2.3</a>: You will have normal duties to attend to, this will interrupt things getting done</h3>
<h3 id=c2a0b4944f0d52aaec4ba066f1860790><a href="#c2a0b4944f0d52aaec4ba066f1860790">8.2.4</a>: Meetings.  Whether you enjoy them, are ambivalent, or dislike them, they are going to occur and take time.</h3>
<h3 id=05c0e353e04741273d56999b7e33a595><a href="#05c0e353e04741273d56999b7e33a595">8.2.5</a>: Mental-Context-switching cost.  Ramp up time.</h3>
<p id=d14a0f795ad0930b2ab59e40ff6742b4><b><a href="#d14a0f795ad0930b2ab59e40ff6742b4">8.2.5.1</a>: Know what kind of work you are going to start, and pick the best time to do so.  If it needs more ramp-up time, then pick a block where you are less likely to be interrupted.</b></p>
<p id=ca064b32d34547ac269d1b85fa693e6d><b><a href="#ca064b32d34547ac269d1b85fa693e6d">8.2.5.2</a>: Break your open time periods into "units" of 30 minutes or 2 hours or whatever you can have contiguously, and see what you can FINISH in that time.  It is easy to lose days/weeks to getting little changes made, but not moving ahead in terms of usable progress.</b></p>
<p id=ae9af424cff9e20bb4d775d699db9e81><b><a href="#ae9af424cff9e20bb4d775d699db9e81">8.2.5.2.1</a>: When each time block arrives, try to get what you can finish, and hopefully test and put into place, in that 1 session.  This isnt possible for some work, because it's too big, so break that into stages that can fit into one of these time blocks.  A simple method, would be: write it in 1, test it in another, and finally deploy it in the 3rd.</b></p>
# Chapter 9: General Advice






<h2 id=0a605e177cdf62b2e4fd820e73cbecf7><a href="#0a605e177cdf62b2e4fd820e73cbecf7">9.1</a>: Go over code reviews, and config reviews.</h2>
<h3 id=a720022abaff2d1c9e31daf42dc94dee><a href="#a720022abaff2d1c9e31daf42dc94dee">9.1.1</a>: *** Mark this as my personal opinion.  Not as something provable.  This is color. ***</h3>
<h3 id=3519e134dd26a81e963ccf09964c8a88><a href="#3519e134dd26a81e963ccf09964c8a88">9.1.2</a>: Normal pitfalls.  Dont really check, "Yes Stamp".</h3>
<p id=7cfef0cbf3e4fb479b3309647eb17ca6><b><a href="#7cfef0cbf3e4fb479b3309647eb17ca6">9.1.2.1</a>: Too style oriented.  Enforcing a style is important in some areas, but less important in others.  It is better to keep a team cohevsive to know these differences, so that on some things you are strict (variable naming) and on other things you are flexible (commenting style).  People write prose more personally than they name variables, and variables have to be used by many people, whereas the message in a comment in based on the author's mental state when they wrote it, which is very subjective, and people have very different styles.</b></p>
<p id=3caece8edc80e43f05cec661ae0cf2f7><b><a href="#3caece8edc80e43f05cec661ae0cf2f7">9.1.2.1.1</a>: I recommend allowing people to have their own unique style in areas that will not harm the ease-of-use and resiliency/robustness of the Logic, and strictness on naming conventions, and basic formatting (indentation)</b></p>
<p id=8923934b9a6ece208968c72ceb0460c4><b><a href="#8923934b9a6ece208968c72ceb0460c4">9.1.2.1.1.1</a>: Strictness can be kept inside individual projects, with a general theme to a department or company.  These are degrees to each of this which will make actually working with other people nicer, while</b></p>
<h2 id=fa154a30257b81d67d9e7c7114d4c549><a href="#fa154a30257b81d67d9e7c7114d4c549">9.2</a>: Root Cause Analysis write ups.</h2>
<h3 id=57a8fb171628609c4f4a074359da7864><a href="#57a8fb171628609c4f4a074359da7864">9.2.1</a>: How to not bullshit these.  Dont lie.  Dont criticize every failure, because failures WILL happen.  The only way to avoid them is to REMOVE the CLASS OF WORK.</h3>
<h2 id=676e5f44878bdde31c3379f2c69b98ae><a href="#676e5f44878bdde31c3379f2c69b98ae">9.3</a>: Create a set of Checklists.</h2>
<h3 id=508068aefcdc803e5f88092d9cafbbf5><a href="#508068aefcdc803e5f88092d9cafbbf5">9.3.1</a>: Automation Spectrum</h3>
<h3 id=47245b1f66b268d9bf3e915e19d7106e><a href="#47245b1f66b268d9bf3e915e19d7106e">9.3.2</a>: Automation Layers</h3>
<p id=4d89acb0c6cf7d6c14c7c9925ffee864><b><a href="#4d89acb0c6cf7d6c14c7c9925ffee864">9.3.2.1</a>: Sub-Components of layers.  How well are they implemented, 1-5 scale or something</b></p>
<h3 id=10909577585a58647fbb1902112b6ab3><a href="#10909577585a58647fbb1902112b6ab3">9.3.3</a>: Talk about how to make your own checklists and scales.  This is flexible, not dogmatic.  The important part is that we can communicate what we are talking about, in a way where multiple individuals and groups can agree, allowing us to work successfully together.</h3>
<h2 id=0109e0d4643177fefe7ccc3fe1c7a872><a href="#0109e0d4643177fefe7ccc3fe1c7a872">9.4</a>: Self-evaluation?  How to evaluate your actions, how to make plans to improve.</h2>
<h2 id=90ee09235d729b6403260561482812a7><a href="#90ee09235d729b6403260561482812a7">9.5</a>: Introduce the Basic Laws of Human Stupidity.  Not meant as insult or joke, but as quantitative method of determining the intelligence of an action.  This is the model I will use in this book.</h2>
<h2 id=7f0428bc4e8fd20bc8ddd31b00ea1d75><a href="#7f0428bc4e8fd20bc8ddd31b00ea1d75">9.6</a>: Journmanship, apprenticeship.  What we are missing.  Valuing experience.  Im old, of course thats my take.</h2>
<h2 id=5ca3d14cd4988a84227bb91b9f59650b><a href="#5ca3d14cd4988a84227bb91b9f59650b">9.7</a>: The benefits of "vanilla" use of tools.  Less upkeep.  Only change what you strictly need to change.  Spend time optimizing only in critical areas.  Reduce things that need to be manually maintained.</h2>
# Chapter 10: Everywhere.  Throughout the book.






<h2 id=a7df76e3e33c3832af992a160d248f3b><a href="#a7df76e3e33c3832af992a160d248f3b">10.1</a>: Have "Wouldnt it be nice?" sections, where I posit what would be improvements I have yet to experience.  Coming to terms, agreeing on the foundational details, agreeing on the axioms, agreeing on how to relate data to the axioms.  Agreeing on how to act against axioms.  With these done, we can work much better as a team, and discuss them.</h2>
