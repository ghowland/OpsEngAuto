.. OpsEngAuto documentation master file, created by
   sphinx-quickstart on Sun Mar  5 19:44:42 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Operations: Engineering and Automation
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Chapter 1: Preface (README.txt)
===============================


What will you get out of this book?  Why read it?



What I hope to impart here is a view into how I see operations, and how I automate operations.



In the case of this book, "operations" means "networked operations", "server operations", "datacenter operations", "production operations", all rolled into one term.  The name is both specific and non-specific, as operations can mean other things, but these specific fields are what I'm referring to.



What I hope you will gain from my perspective is a new foundation you can use as a plane of reference to improve your own operational mindset and practices, whether you are already an experienced operations engineer or new to the field. 



I will be covering a large arena of information, and I will try to present a coherent picture, though each section must unfortunately be left incomplete as each section is only a small part of the larger picture I am trying to make clear.  This is in contrast to many technical books which explain things clearly in each section before moving on, because their content is able to be defined and explained in each given section.



This book's format is meant to be read from start to finish.  It starts off more general, and philosophical, setting up terminology and direction.  Then it becomes more specific as we work towards implementation.  Finally, it will go back to being more general as we discuss how to implement automation in your current environment, as automation will change the way your organization operates, and must be performed with these issues in mind.



This book is more about depth than breadth, and as such we will continue to come back to examples over and over again, looking at them in different ways, to give a deeper understanding of all the components that make them up.  This is again in contrast to many books that are meant to describe an array of information and give you a broader understanding of how they work and how to use them specifically.



This book is meant to improve your ability to reason and create efficient solutions in the operational engineering space.


1.1: Where Ive Been, What Ive Been Doing, Why I Wrote this Book
---------------------------------------------------------------

As of this writing (2016), I've been working in the industry for over 20 years, and have been programming for over 30 years.  I've written over 1000 programs of varying size (the bulk of them being smaller, and operational in nature), but have also written and deployed PC games, end-user productivity tools, accounting software, end-user websites, as well as a lot of operations related monitoring, alerting, log parsing, configuration and automation logic required for operations work.

Some names of places I've worked, named where you may know them, and grouped as industries where it's unlikely:

Google, VMWare, Netflix, LinkedIn, Cisco, Pacific Telesis, Lawrence Livermore Labs, Mobile Game Companies, PC Game Industry, Mortgage Industry, Financial Security Industry, Internet Startups (SaaS and end-user websites)

You can see my abbrieviated job history at LinkedIn:

https://www.linkedin.com/in/ghowland

1.2: The promise of automation is removing classes of work
----------------------------------------------------------

"The promise of automation is removing classes of work, while you consistently get the desired results."

At this point, everyone knows that automation is a necessary thing.  It wasn't always this way.  I spent much of my career trying to automate things and getting strong pushback from both management and peers (starting around 1996).  

These days people usually have some aspects of automation, and are comfortable with those, so it is only the areas that they do not yet have experience which are hard to get implemented.  A major impetus in writing this book is to resolve those problems, by making the concepts better publicized and hopefully well understood.

The issues I find these days are not that people do not want comprehensive automation, but that there is not a clear understanding on what comprehensive automation entails, what it takes to build, how things will change once it is in place, and how the life-cycle of operations changes accordingly.

With all of these things, it is best to stay results-focused, and look to what you want to achieve out of automation, and in my opinion the ultimate goal should be: "removing classes of work".

What is a "Class of Work"?  We will look at this in many ways over the course of this book, but we can start by summarizing it as: "anything that is done".

This may be a specific thing such as "update a DNS zone file" (text file).  When this "Class of Work" is comprehensively automated, then no one will ever again update the text file relating to DNS zones, but will have to do other work related to DNS still, as only updating the zone file was comprehensively automated.

This could be extended to "configuring DNS", in which case all zone files are automatically generated, the serial numbers are always incremented properly, the configuration files that specify the zones are generated, and all the transfers and tests to ensure that these changes are pushed out into production and contain valid entries are validated and monitored.

This is a "Class of Work" that requires people to do something currently, but perhaps only in some areas if it is already partially automated.

If you have a service (SaaS, such as a web-site like "DNS Made Easy") that does this for you, then someone still needs to enter the data.  The data entry is still a manual process, and part of the total Class of Work relating to updating DNS.

How would you remove this manual work?  It will need to be generated from either a template of hostnames for the type of services being provided, or some other automated mechanism.

When no one has to think about the life-cycle changes or perform manual labor relating to this area of work, then this Class of Work has been comprehensively automated, and has been removed from the realm of Manual Labor (which requires scaling personnel).

Updating the system (code) that manages this Class of Work remains manual labor, as writing logic has not yet been turned into an automatable task, but the regularity of updating the automation logic should happen far less frequently, and is more knowledge-work than data-entry work.

Knowledge work is more stimulating, and known to be something that needs reviews and tests, whereas manual data-entry work is more prone to mistakes, because it is done so regularly that constant vigilance becomes impossible to perform accurately.  

Mistakes will happen, as everyone knows manual work must be manually inspected and automatically tested, and yet this is typically the place that mistakes are made, because updating automatic tests and and manually inspecting the data are both themselves manual processes, and similarly prone to failures.  

Eventually someone will make a typo or other data-entry mistake, and it will not be caught in review, and will be pushed out to production, and will cause an outage, and may cause loss of revenue or other negative consequences.

With automated logic, these kinds of repetitive data changes and verifications can be done as correctly as the logic specifies, and if it is written correctly, it will be done correctly forever.  Or, until the business goals or infrastructure environment changes, and it must be modified accordingly.

1.3: Writing in the First-Person
--------------------------------

You may have noticed, but I am writing quiet frequently in the first person, and will try to keep this consistent as much as possible.

I am speaking of my experiences, perspectives and opinions, and so I think this is best done using "my own" voice, instead of a more factual "voice of authority".

In my view, all information should be considered as coming from the source of origin, where you discovered it.

When I say "X is Y", I think this should be read as "Geoff said X is Y", and not that X really is Y.  Whether X is really Y or not should be something that you validate for yourself, in your own experience, in your specific situation, or context.

The situation I could be using as my example may not match up to the situation you are working in, and my perspective may not be a useful one.

Moreover, language itself is very flexible in what is what is meant, as many things could be intended by the same word, like the very overloaded word of "operations".  There is frequently a COO, Chief Operations Officer, in large or public companies, and this person's role and department has absolutely nothing to do with "production operations", "network operations", "server operations", "datacenter operations", etc.

Because of this, it is useful to limit what you take from incoming information to what the speaker was trying to convey to you, their intent, as coming from them, from that particular situation, and their particular perspective and experiences.

This separation from incoming-information as "fact" makes taking in more perspectives easier, as they do not need to be turned into a one-size-fits-all world view of truth.  As I learn more, I find that having such a one-size-fits-all is often a hindrance to communicating with other people, and learning new things.  It is certainly a hindrance to having an open mind to new information which may conflict with one's current world view.

Instead having a "this person said this thing" stance, allow any new information to come in as it arrived ("I learned about X from Y").  You experienced getting the information in some way, and that is that.  No additional weight needs to be added or subtracted from that evaluation, and you avoid applying the Logic Fallacy of the "Appeal to Authority" in your own in-take of information.

Whether you utilize that information, or make it part of how you make decisions is up to you.  Whether it is applicable to your situation is up to you.  Whether it seems logical and grounded in reality as you understand it is up to you.  There is no reason to reject or accept it, as it is simply information, and you have tagged it along with the source to use as you see fit.

There will be quite a bit of this kind of introspection into language and meaning in this book, as it is in part a book on the philosophy of engineering and automation, because this is much more important than common jokes about philosophy majors in college may lead one to believe.

I also find that when writing in the first person, it is less of a commanding or authoritative approach, rather than writing in the second person ("you will then do this"), which has more opportunities to throw readers off if they disagree with the statement, do not immediate want to do what is being recommended, or are just tired of being lectured at.  All of these are reasonable reasons for avoiding incoming information, and I use my own voice to give it as my own take, to avoid this.

This is a one-way conversation, in that it is a book, but it is meant to be taken as a conversational approach to learning, so that you can grow from it as best is possible, and not merely a display of my knowledge and set of instructions for others to follow.

1.4: Writing Stylistic Conventions
----------------------------------

There will likely be some writing stylistic conventions I use that are new for you to read, and perhaps you don't like, and certainly you will not find approved in English Grammar books.

I have developed my style of written communication over my life, and continue to refine it still.  I am more concerned with having my intent and detailed messages understood than in complying with grammatical rules, and so will bend and break them as needed to achieve my desired results.

As such, as I will quote "things" whenever I want to emphasize them specifically, as introduced by Alfred Korzybski, from his methodology of General Semantics (although not following his strict guidelines).

I will also interject parentheticals (like this), whenever I want to make an immediate "aside" comment or clarification (like this).

I will also make up words whenever they seem to work better, or sometimes I will think I am making up a word, but it might end up being an existing word that I didn't know, and has a different standard meaning.  I will try to explain my meaning any time I think I am making a concept that may not be a standard one, so try to read it with my intent, instead of against a standard, as if I stuck to the standards I don't think I could get the details with the pacing that I want.

I am going to frequently switch words such as "I", "you", "we", "one" to account for the subject, and I have specific meanings for this:

- "I": I am talking about myself and my experience.  As previously said, I will try to do this as much as possible, because this is a transference of knowledge, from me to you.

- "You": I am talking about you, the reader.  I have written this for you, even though I probably don't know you, I have you in mind when I am writing, and I am thinking "What will you be aware of at this time, from previous material?  What I am trying to get you to?  Is it clear to you?  Do I need to add any disclaimers or details?  Am I spending too much time on this?"

- "We": You and I are on a short journey together, although at different times and different places, but I am relaying information into this medium, and you are consuming this information, and that creates an informal relationship between us.  I like to think in terms of "we" for this, as it is a shared journey.  

When I write code I often like to document things like "Here we are doing this" and "We don't want this effect, so I am doing this".  In this "future readership" situation, I am thinking of the code documentation's future reader, which may be myself or someone else.  In either case, that reader will be in a different state than I was at the time I wrote the code and documented it, so I am trying to bridge that gap, and make it another "shared journey".

- "One": This is when I am trying to give advice to some sort of direction.  I really don't think I should be telling you what to do, and I don't want to.  I want to assist in enabling you to do things better, and to make your own choices, and make your own processes, and methodologies and philosophies.  Telling you to do things is in opposition to these goals, so I use the word "one", such as:

"One's tea is best with slightly sweet biscuits."

It is kind-of the British Royal "we", as the "all encompassing singular", but I write it mostly so if you don't want to accept my information, it is easier to digest, because it is directly toward the aether, and not directly at "you" in a tone of command.  I feel this is a way one can make generalizations and advice, without making the statement too-pointed-at-you.

I will also hyphenate-things-to-make-compound-ideas.  This allows words to be read in the sense of "all these things are one thing", and help in any kind of grammatical parsing.  As I understand it, not being able to speak German, the German language has "compound nouns", in which many nouns are put together in sequence to form a new word that is a combination of all of these.  I think this is a cool method of communication, and these long-chains-of-hyphenated-words are like that, but for any type of word, not just nouns.  They create Compound Concepts.

I was born and have lived almost exclusively in the United States of America, and only in a few small areas of that space, and so my language usage is set up in a certain way.  Additionally being an Internet-denizen, I have a very fluid use of that language.

My usage of English, or maybe "American", may not be easy for you to parse if you are not familiar with the way people similar-to-myself communicate, or English may not be your first language.  

Even if you have a very similar usage of language as mine, the ideas I am expressing are complex and riddled with detail, so these mechanism of asides, and compound ideas, and such are methods to make parsing these ideas more clear, although they may appear more Byzantine.

I am mostly writing in a tone of conversation, and so will jump around more than if this was a text book.  This is certainly not a text book, and should not be read as such.  It should be read more like a novel, as I am attempting to perform "Mentoring", and so am building up ideas and referencing them repeatedly in a type of planned sequence.

If you jump to a section, and find it oddly confusing, it is likely because ideas were introduced and specified in a previous section, and their immediate usage (without that previous information) may seem very alien indeed.

This is a trade-off between writing styles, and for this work I have chosen this style as the one I think will yield the best results for the audience most-likely to be able to intake this information and make use of it.  That is only a guess, but I have to pick a methodology and stick with it.

I will also be making Liberal Use of capitalizations.  I will have certain terms that I always capitalize, as I am using them as "Proper Nouns" (like a person's name), but I will also sometimes capitalize Random Words, because I am introducing a concept and want to draw attention to those specific words in the sentence.  It may be that I will capitalize them the first time I talk about them, and then never again, because the point was made, and the attention to them was drawn.

All of this makes a real jumble of what is considered proper English, but I am doing more than relaying my thoughts and experiences and methodologies to you in English, I am trying to communicate the underlying ideas behind them, and those concepts are far more detailed and complex than English (or any language as I know them) can relay.

There is a reason we have poetry, because the intent is to express something beyond the words, and often the structure of normal language communication is broken or modified to relay those intentions through the language, as the language is both the barrier and the medium.

My usage is similar, but is the Poetry of Engineering, as I see it.

1.5: Hopefully, this will...
----------------------------

The ultimate goal in this book is that it improves your ability to function as an operational engineer, and to write automation that achieves the results that you want.

If you find any areas difficult to understand, or believe that sections are not explained well or are incorrect, feel free to write me and I will try to get back to you and update the work as best I can.

My personal email is:  geoff@gmail.com

Chapter 2: Introduction
=======================


One of the foundational goals of this book will be to differentiate the real from the virtual.



This may seem like something that is common sense, but I have found wide breadth and scale disagreement on what is real and what is not real, and this creates a lot of communication and planning problems.



If we can't agree on what is real, how can we agree on our priorities?  We will value things differently, because we understand them differently at a very fundamental level, and all communication will be inaccurately moving past each other, instead of directly engaging with common terms and values.



The results will be poor, and without coming to terms with why this fundamental mis-communication is occurring, we may never be able to see eye-to-eye, and may end up being unable to work to get good results with each other.



Going to the very basics and working up from there will allow us to develop a common method of communicating, starting from terms, and moving to goals, and then priorities, and finally into axioms so that we can come up with plans where we agree on the components and end results.




2.1: The differences between Physical and Virtual: Real and Unreal
------------------------------------------------------------------

"What is reality?" is a question that is too big and general to be dealt with here, if you want a good introduction on how to understand this from an engineering perspective, you can see Bertrand Russell's book {{ book_russell_reality }}.  It does a good job of describing how reality can be determined from our senses, and is a fairly short read (described in about the first 30 pages).  You can also take a look on Wikipedia at the philosophical movement, Logical Positivism, which is a useful philosophy for engineers, and is one of the philosophical methodologies I use and reference in this book.

For our purposes, it is good enough to have a summary of this, and for me to describe on which side of real vs. virtual (un-real) various elements reside in, for our purposes.  Again, this is not meant to be "ultimate truth", but a tool for communication, so that we can come to common terms and understandings, and grow our engineering abilities and get better results.  It is not meant for purposes outside of this endeavor.

To be brief, I will use Russell's example converted into the experience you are having right now.

At present, you are somewhere reading this text.  You are real, you exist, because you have tangible properties, such as mass, made of of molecules and atoms, in a certain state that make you you.

The text you are reading is either in a book form, such as paper, or an electronic form, such as a monitor or e-ink display.

If you are reading a book, the book is real, because like you, it is made of molecules, and has physical properties.  It resides in a certain position in the world.

If you are reading from a monitor, then the monitor has similar physical properties.

These things are all real, for our purposes of reality.

The way you are able to read is that either ambient light is refracting off of the book, or is being emitted from the monitor, and those photons are striking your eyes, and the rods and cones in your eyes are being stimulated, and sending "signals" into your brain and nervous system.

These things are all real.  Photons have physical properties, and while different than molecules and atoms, are able to be physically described and interacted with.

At this point, you are probably affirming why you may have not read more philosophy works in your life, right?  Nothing new here, but lots of words to get to that point.

Now, we enter into the realm of the un-real, the virtual world.

How you interpret the words is not real.  It is a virtual type of understanding, though the word "virtual" is usually confined to computer related terms, I am going to use it universally to all things to differentiate from real.  Because we are mostly going to be discussing computer-related un-real concepts, it is easier to just stick to real vs. virtual.

So, what am I getting at here?

You are real, the device (book/monitor/device) is real, the photons traveling to your eyes are real, but your understanding and interpretation of the words is virtual.  Your feelings about the words is virtual, and in fact the words themselves are virtual.

The ink on the paper, or the electrons producing the physical effects are real, but your understanding and interpretations of them are virtual.

What's the point of this?  It will become clearer as we go on why I am leading with this, and it's not to make myself seem like a fancy-pants smart guy, it's because without this agreement now, there will be many more disagreements in the future, and it will hinder our communication about the more interesting and relevant parts of engineering and automation.  Please, bear with me here.

So.  We have real books, devices, you are real, I am real, but your understanding and my understanding of things is not real, and even the words I am writing and you are reading are not real.

How are words not real?  It is because they are symbolic.  They represent an idea, or set of ideas, which are also not real.

The word for "book" exists separately then the object they describe.  In other languages, the word "book" changes (libre, knega, etc), yet the book itself does not change.  This illustrates how words are different than the things that they describe.

Words can also be written in different fonts, and I could call this a "manual" instead of a "book", and yet what you are reading would not change.

Symbolic things are not real, they are virtual, or logical.  I will use virtual instead of logical, as I will be differentiating "Virtual" as un-real, from "Logic" to be used for processes and code, or programming.

Let's create a quick list of things that are real and virtual, for an immediate reference:

- Hardware:  Real.  Something you buy (a device), put an OS on, and runs your software, or something similar.
- Software: Virtual.  Electricity (in RAM), magnetism (on rotating disks) or electro-chemical (on SSDs/NAND) stores bits of information that can be executed.
- Data: Virtual.  Same as software, but can't necessarily be executed.
- Operating System:  Virtual.  Collection of software and data to make hardware perform operations.
- Book: Real.
- Words.  Virtual.
- Ink on a page: Real.
- Fonts: Virtual.  Data about how ink can be put on a page, or pixels illuminated on a screen.
- Light emission from monitors/screens: Real.
- Words and letters written on the monitor: Virtual.  These are just patterns we recognize, and are all virtual.  The physical properties of them are real, but those are not what we call "words" or "letters", but are instead patterns of photons at different frequencies and intensity.
- "A network": Virtual.  It's a concept of something that "networks", or more specifically may be an network IP address (data), that describes the network.
- Network cables: Real.  Physical objects, that carry current.
- Ethernet protocol: Virtual.  A collection of data and logic that describes how to communicate over electrical signals.
- Layer 1 Ethernet: Real.  Physical electrical signals
- Layer 1 Ethernet standard:  Virtual.  The description of how the physical Layer 1 ethernet will operatie.
- Layer 2 Ethernet: Virtual.  How the Layer 1 physical (real) is used via the Layer 1 Ethernet standard (virtual), to create a Layer 2 ethernet connectivity effect (virtual).
- IP Address: Virtual.  Data.
- Hostname:  Virtual.  Data.
- My engineering perspectives:  Virtual.  Data.
- My engineering experience:  Virtual.  Data.
- The actual things I have been through in my life:  Real.  Things happened, involving molecules and stuff over time (entropic heat exchange, etc)
- My perspectives and memories of the actual things I have experienced:  Virtual.  Data, and summarized data at that, since I was not aware of the full-state of the physical (real) occurrences around me, and my memory (virtual) of them is a summary of that as well.


I hope this short list and hopefully not-too-painful fundamental section has left what I am referring to in a clear state with you.  

If not, please skim it again.  You don't need to agree with me on these things, you merely need to understand what I am trying to say clearly to get the information I am trying to convey.

If you ever hit parts that feel wrong to you, or you reject, try to use the mechanism I presented in the preface, changing what you disagree with to: "Geoff says X"

This means you can take in this information, as "Geoff is saying this to me", without having to update your world-view at this moment to include what I am saying as "the truth", and in fact, I am not asking you to ever do this.  This is a communication to hopefully provide you more insight, which will include my perspectives, not as instructions on how you should see the world once you have finished reading this.

It is more important that the things I am saying to you are internally consistent (Alignment), than that you agree with my usage and summary of each of them.  I am working with more information than I can convey at any given time, and am doing my best to partition this into a small stream of data that can be turned into understandable language.  It's a lossy process, at best, but it's the best I am able to do currently.

2.2: I only really know what I myself have experienced
------------------------------------------------------

What do I know?  What do I really know?

Or, to paraphase a Sherlock Holmes quote, "What do I know, and how do I know it?"

In any situation, this is a relevant question, as it directs where I will go next.

If I believe I have solid information, that I can take action on, I can begin immediately to take action on that information.  If I know that I do not have solid information, then I know that the first thing I need to do is to get some solid information I could work on.

How do I know if what I really know is good information?

It should be sourced from my own experiences, or it should be planned to quickly make checking the information so that it becomes part of my personal experience.  Things I have personally experienced, I can say I have knowledge of.  

Things I have read or heard, or that someone (including myself) just thought up may not be related to the reality of what is going on at the moment.  Actions based on non-personal-experience information are going to yield extremely unreliable results, because the information was not grounded in the circumstances it is being applied to:  Local Reality.

What you experience and work with directly constitutes your actual context:  Reality.  Information that is not directly related to your context may not be directly applicable: Virtual.

Let's create an example, a problem for us to solve.  We'll be doing a lot of this during the course of the book, so to get the most out of these I would suggest taking a moment each time one is introduced to try to model it out in your mind, imagine it, draw it out on paper, or do whatever works best for you.  I will discuss some of my techniques for doing this as we progress, but please use what you already know and invent new ones any time they occur to you as well, and try them out.

The problem will be a common one:  Alerts are going off on our monitoring system, and tell us that we are having problems with our web servers.

The monitor alerts are not extremely specific in this case and report something like "HTTP test failure".  More specific alerting would be helpful here, but those tests take time to set up, and in our immediate example environment they don't exist.

A group of people forms up to deal with the alerts, and immediately several things are suggested as problems:

- Maybe there was a bad code push?
- Maybe the logs have filled up the disks?
- Maybe there is a DDOS or other hacking attack occurring?
- Maybe someone is doing work on it, and forgot to tell anyone and made a mistake?

All of these are possible, and while some are more likely than others, and could be used to prioritize where we start looking, the question remains:  What do we know?

What we have experienced so far, and what we really know, is that we got an alert of "HTTP test failure", and this has something to do with our web server environment returning correct results to the monitor health checks.

This is all we know in this circumstance.

Was there a bad code push?  We don't know, because we haven't made it part of our example.  Let's add some data around that.

We have 2 options:

- We ask developers or release engineers (or whomever, for this purpose we will say "release engineers") if they have recently pushed any code.
- We go and look to see if the code has been updated.

Both of these options will yield us new information we can work from, but will each of them give us solid information?

Asking the release engineers will give us the hear-say information that whoever we asked gives their best current information.  Do they check first before responding, to see if anyone has pushed code lately, or do they use their current information to tell us?

If they say, "No, no one has pushed any code lately.  We won't be doing that until X time", then we will leave that conversation with information that says no new code was recently pushed, and we will have impetus to de-prioritize the possibility of new-bad code being pushed into production causing the monitoring alert.

But is this solid information?  They may be the only person who does the code pushes, and so they may be the "definitive" answer on the subject, but what if someone new accidentally did it for some reason?  The "definitive" person would not know this, unless they checked, and their information would not be congruent with reality.

If we take the second option, and we look for ourselves, then we can see if the timestamps on the files have been updated, or if the log files say that the web or application servers have been reloaded.

The second option gives us information that we have personal experience with, and this is solid information.  If we do not have access to go look ourselves, then the next best thing would be getting someone who does have access to verify it themselves and preferably show us the result, but they could also provide unique information such as "X was the last time code was pushed", instead of a more vague answer like "No, no code has been pushed lately".

So we have two lessons we can take from this example problem.  One, that information we have personal experience on is better than hear-say information, or information we do not have personal experience with.  Second, that there are degrees to "information solidity", or the reality-based nature of the information.

Looking ourselves yields the highest relation to reality.  We were there, we looked at the information, and it said "X".  We have very high reliability with this information, as long as we were paying attention to what "X" was, and paid attention to get into the right position to look at the right data (not accidentally looking in a different server or directory, at the wrong files), then we have solid actionable information to work from.

This would be the same level of information if someone else did this work, but showed us while they did it.  We saw them do it, we saw the results.  It would take some acts of deception to make this data questionable, and since we are referring to working in a work-environment, we will assume that all people are behaving as Good Actors for these examples.  Later, we will also look at how some people act as Bad Actors, and can create bad data, for instance trying to hide a mistake that have made.  (We could call this section, "Do you even audit, bro?")

Less reliable is information that someone told us they looked, but did not show us, and gave us exact data, such as "X was the last time code was pushed, I checked the directory timestamps and logs".  This is good data, but we do not have personal experience with it, so it is less-good than data we verified ourselves.

Next, we have a situation where someone else tells us "No, no code was pushed recently".  This is not data we have verified ourselves, so we have no personal experience with it, and it is not specific as to when the code was actually released.  It is possible that this person did not check, and is just telling us from their own perspective that they don't believe it was pushed recently.  This is beginning to be invalid data.  

We could still ascribe Good Actor behavior to this person, and take them for their word, however, what will be the result if we do take them at their word, and de-prioritize looking at a bad code release, and start looking at other problems.  We end up exhausting the search on other things, and much down-time has accrued with the "HTTP test failure" alert still going off, and eventually someone looks and see that indeed new code was pushed out, and it contained a bug.

Rolling back the code resolves the problem, and the HTTP server starts to return correct tests to the monitoring system.

Much of the downtime accrued because of working with non-verified information could have been avoided by getting personal verification of the exact time of the last code push.  I have seen this exact situation happen many times, and bad-code or bad-configuration changes are one of the most common outages for networked services.

Even though these are common, the common-ness alone does not mean that it is solid information.  It only means it is something that should be verified quickly to see if it is a contender for causing the problem.

We will be exploring the idea of what makes good information in detail in this book, and I will change this introductory terminology of "solid information" into a more precise definition of Intelligence, which we can categorize in many ways:  Verified, Unverified, Actionable, Unactionable, etc.

2.3: What is Operations?
------------------------

Keeping up our short tradition of asking questions that seem pointlessly basic, I will ask:  What is operations?

Why do we do what we do?  Why does it exist?  What is it?  What are the goals?  What are the priorities?  What are the procedures that makes up an Operations department?

The more questions that are asked, stemming from the original question, the less the question seems to be pointless, and the more the questions start to become the ones we deal with every day.  But, we skip the first question.  Why?

We skip it because we already assume that we all know the answer, and that we are already in agreement about the answer.  It is taken as a given, but in my experience, there are many differences of opinions in even the most basic answers to what it is.

People have different values, and they have different skills and personal experiences, and from these, they have a world-view that is also different.

Getting to the fundamentals of what we mean by something like "Operations" means that we can start to align our views, and in aligning our views, we will communicate more effectively, and become able to work more effectively together.

It is really these fundamental issues that make communication so hard and ineffective, because we do not drop down to discussing what we are fundamentally doing, and get buy-in from everyone on the team about each of the layers in the stack of what makes up an environment's operations.

So, what is operations?

2.3.1: Operations is about Control
----------------------------------

I will posit that the primary thing that operations is about is Control.

Why control?  Why not up-time, availability, responsiveness to business direction, or any other valid priority?

My reason for this is that without control, you cannot be efficient in any other areas.  You can only be as efficient as your level of control allows you to be.

You can always make progress in any area by applying resources to it:  people, time, money, hardware, etc.  

These will make progress on problems you have and want to solve, but the limiting factor to each of them will be your ability to control the environment.

If you have an up-time failure event, to fix the problem quickly you must be able to determine what is wrong, which takes the ability to gather information, and you must be able to take action to resolve the problem, which takes the ability to change the environment.

Both of those actions, "gather information" and "change the environment" have Control as a central tenet.  

How can you gather information without the control of the environment to yield you information?  In the most basic example, if you do not have access to the information, you cannot gather it, and you certainly do not have control over it.

If you do not have access to change the environment, you cannot change it, and do not have control over it.  

Like many things, Control can be seen a spectrum.  We can illustrate in on a line segment, such as:

No Control <-----> Total Control

This spectrum would represent all possibilities of "Control", having no control, and having total control.

Control is a tricky subject, in that it is not only un-real (Virtual), but it is even more Virtual than many other things, because it more like a concept than something that is valid data.

Unlike other Virtual (non-real) things, Control cannot be verified like data can be verified.

If I have a variable "X" and I set X to 5 (X=5), and then I check if X is 5 (X==5?), I can get a result that is True or False.  X is either 5 or it isn't.

But with a concept like "Control", there is no way to check that you have control or not.  You can check that you have access to some data, which is an aspect of control, and you can check if you can change data (by changing it, or looking at permissions (less good)), and this tells you more aspects about control, but there are so many other things that go into this that are very difficult to inspect or verify.

For instance, one aspect of Control is, "Do we have enough time to do the work we need to do?"  This is an aspect of controlling one's schedule, so that good work can be produced.

If we do not have control over our schedules, and work is required to be done before it can be done to our satisfaction of "good work", then we do not have control over this, and we will see problems arise from this fact.

There are many other aspects of Control that we will look at, and I will make more cases on why I believe this is the central tenet of Operations and why understanding what you do have good control over, and do not have good control over is very valuable and actionable information.

2.3.1.1: "De facto" Ops vs. "Planned/Controlled" Ops
----------------------------------------------------

If Control is the central tenet of Operations, what is the opposite side of the spectrum?  Uncontrolled operations?

I think it's clearer to say that the opposite side of the spectrum from control is "de facto" operations.  What simply happens because there are business goals that need to be solved, and resources were put towards solving them, again and again.

It is fairly easy, in my experience, to handle every situation in an efficient manner for the problem at hand, and still end up with a total mess of an operations environment, because the actions while individually efficient do not work together as a whole efficiently.  The total set of actions have poor Alignment.

This is often seen in naming conventions that change frequently, or that you could say there is not really a "convention" to the naming of things.  The same goes with what kind of hardware you purchase, if every time you purchase hardware you pick the "right tool for the job", but you end up with unique hardware configurations for every problem solved that required a purchase, then you have N number of hardware configurations to support and manage.  How does that impact your overall efficiency at supporting these systems?  It was individually efficient up-front, but how is the efficiency after the up-front cost?  Which cost is more over it's life-time, the up-front cost or the maintenance costs?

The maintenance work to keeping many hardware configurations versus a limited number (say 2-4 unique hardware specifications per generation of hardware purchases), will mean many more problems have to be solved in upgrading software, and many more security and firmware upgrades will need to be tested.  It can easily create a situation that either requires many people to support, or more likely it is not worth the cost of actively supporting everything, and so support is only assigned when a high priority problem arises to keep personnel costs down.

"De facto" just means "In reality", but in common terms it means "the way things happens", like "this is what has been created from our low-coordinated efforts".

So a spectrum for Control would look like:

De Facto <----> Planned

Planned operations will have strict naming conventions, where all the data required to be derived from data embedded in the name, and when new services, products, environments, and other things arrive, they are intelligently inserted into the existing convention, and they do not create new conventions (without just cause), and they do not arbitrarily add new components or re-use existing components for different purposes (without just cause).

An example of "de facto" naming of hostnames might be like this:

- chicken.domain.com
- trex.domain.com
- saturn.domain.com
- monkeyknifefight.domain.com
- web1.prod.domain.com
- web9.prod.domain.com
- web10.prod.domain.com
- redis-01.sf.prod.domain.com
- redis-01.nyc.prod.domain.com
- redisqa-01.nyc.prod.domain.com
- redis-01.nyc.stage.domain.com
- git.corp.domain.com

And a list of the same names, in a "planned" fashion might be like this (which provide the same services as the above machines, in a 1-1 fashion):

- ops-001.infra.admin.sjc.domain.com
- ops-002.infra.admin.sjc.domain.com
- ops-003.infra.admin.sjc.domain.com
- monitor-001.infra.admin.sjc.domain.com
- web-001.product.prod.sjc.domain.com
- web-009.product.prod.sjc.domain.com
- web-010.product.prod.sjc.domain.com
- redis-001.product.prod.nyc.domain.com
- redis-001.product.qa.nyc.domain.com
- redis-001.product.stage.nyc.domain.com
- git-001.infra.corp.sjc.domain.com

A couple of things can be immediately seem from these lists, as you compare the each ordered element against the same position in the other list.

Some striking differences:

- No "funny" or special names for machines.  "monkeyknifefight" is great imagery, and fun to say, but it has no business in your operational data.  It does not explain what services are provided, who owns the machine, where it is located, or any other actionable information.  It is essentially dis-information, since you know less about the machine then if it was called "misc" or "general".

- In a planned naming structure, all names have the same number of elements, and the elements are in the same order, and written in the same sequence and pattern.

In the list I have just made up, you can tell a number of things about any of the given hostnames' servers:  

What general function they provide (web, git, redis).  

What location is the server in?  SJC and NYC seems to be our options.  This is much clearer than "sf", as they are airport codes, and so provide more localized information than city or regional data does.

What environment is this used for?  Production, staging, QA, corporate?

What instance number of the service is this?  001, 010?  

In addition, the instance numbers are always written in the same format, providing a standard for where to start a new service:  001 (or 000, if you prefer cardinal counting)

The planned naming convention can scale significantly, while keeping a pattern that fits any of the machines, new or old.  Selecting the proper format for naming hosts is so important, because it is a direct factor in Control.

If you cannot name something accurately, how can you control it?  How can I access a server, if I do not know it's name?  How can I change the state of a server, if I do not know it's name?

I have worked in environments where naming conventions changed even in the same service.

Take this for example:

- redis-01-1.product.prod.domain.com
- redis-02-1.product.prod.domain.com
- redis-2-001.product.prod.domain.com
- redis-2-002.product.prod.domain.com

These are 4 redis servers, in the same "pool" of servers (used by the same application servers, in the same production data center), but halfway through someone changed the naming convention (out of a much larger pool than 4 machines, more like 40).

They started out with "shards" as "redis-XX-#", where "#" is the "shard" number (relating to a master-slave set of data), and "XX" was the "shard instance" number, where "01" might be the Master (takes writes) and "02" would be the Slave.

Then later they or someone else (more likely) created a new set of machines with the shard and shard-instance values flipped, and the shard-instance values now have 3 digits, instead of 2.

This creates problems every time someone tries to work on these machines.  Logging into any given machine takes either trial-and-error, memorization, or looking it up.  Each of these is inefficient in time and personnel resources, and as the site scales up (more servers, more services), these kinds of time-personnel costs start to become major factors in both how much work can be accomplished in a given period of time, how frequently mistakes are made (not updating all the servers in the same fashion, performing work on the wrong servers), how long it takes to train new employees, and how well any employee really knows the environment.

We are probably in agreement that planned naming conventions is better than unplanned or de facto naming conventions, but we are engineers, and it is not enough to think something is better, we require being able to dissect the issue to see what the components make it up, so that we can build it better for our specific needs, for any given circumstance, to create the most efficient solution for that specific circumstance.

Let's take a look at the original planned naming convention I gave, and see how we can make it more efficient, since we want it to be our one-and-only naming convention.

- web-001.product.prod.sjc.domain.com

Let's look at each part of this name:

- web
- 001
- product
- prod
- sjc
- domain.com

These are the components that make up this name.  Do we have the right components for our current needs?  What about our future needs?

One can certainly over-engineer a problem and "prematurely optimize" it against future concerns, but not looking at what is likely to come in the future is on an extreme side of the spectrum for planning for the future.  Let's make a spectrum for this:

No Planning <---> Every Detail Planned

We want to be in the middle, but more towards the side of "Every Detail Planned", while minimizing the resources we spend on doing them, to maximize our efficiency.

Taking each section individually:

- web

This seems pretty self-explanatory.  If we call things "web" servers, and they do "web" things, and we don't have other services that also do the same thing in the same environment and could cause confusion, this is good enough.

If we do have other services that do the same or similar things, we might need some alternative names, such as "app", "webmain", or "webfront" or something similar.  Try to make it what people in your environment call it verbally, and there will be less confusion when switching from discussions to typing in data.

I will call this first part of a naming convention our "Host Class".  So machines hostnames that start with "web" have a Host Class of "web".

- 001

This is our Instance number.  It is the first (or second if starting from 000) machine in in the "web" Host Class.

This has an obvious limit of stopping at 999, and then the naming convention reaches it's limit.  Many organizations will never have more than 999 servers of any type, but this is not a reason to fail to plan for the case of scaling past that point.

It costs very little to make a good naming convention, and only requires diligence and checking your work to ensure that no one creates names they should not, and it will save much pain in having issues with naming down the line.

Scripts are written whose logic may not be able to deal with naming conventions that change, and this can cause problems in your environment as you pass these thresholds.  We'll cover how to solve this shortly.

- product

This is an example product name for your organization.  This should be a short product, project or service name that clearly differentiates it's purpose from other products, projects or services.  Notice in the example I use "product" and "infra" to differentiate the organization's product, which may generate revenue, from the infrastructure services used to support the product's operational environment.

- prod

This is an "environment" description, and differentiates machines in production (being used by end-users, or running financially impacting services), differentiating it from servers performing the same actions, but that run in development, QA, staging, corporate, or other environments which have different users and impact if they go down or degrade.

Common examples:  prod, stage, qa, dev, corp, net

- sjc

This is the location of the datacenter the server is in.  Whether it is a closet, or a Tier-4 Gold data center, you have assigned a location to it, so no one has to guess.  If you are consistent and only put the correct location labels into the hostnames, you will not have confusion over where machines physically reside when this becomes an issue, say for maintenance, repairs, networking changes or migrations.  If you are shutting down a datacenter, you definitely want to know all the machines in that datacenter, so you can migrate their services and not miss anything.

Using airport codes, of the airport closest to the location, is a common practice and a good one.  It allows being fairly specific, but not having to debate over whether something is inside this-or-that region.  Simply find the closest airport with a 3-letter airport code and use that.  It doesn't matter how big the airport is, if it is a registered airport it is guaranteed to be unique and give you a latitude and longitude to the general area in a consistent manner.

- domain.com

The example domain of our example organization.  The important part here is that it is consistent.

There is a difference between internal names and external names, in that internal names can be kept consistent with the work of the Operations department, but external names are frequently under the control of other departments such as Marketing, Business Development, Sales, etc.

As such, they should be treated differently.  Internal names should be rigidly controlled, and external names should come with high recommendations for using naming conventions.  You could even provide several different recommendations for external naming conventions, to try to get other departments to constrain themselves and avoiding total naming-anarchy.  Without having control, you should expect "de facto" results, and prepare for those accordingly.
``
{{ aside_begin }}
Frequently non-Operations departments do not understand the use of sub-domains like "product.domain.com", and will create new base level domains for every project.  Sometimes this is required (legal and business reasons) and other times, it is only because they didnt know they could have "newproduct.domain.com".  This is especially a problem for certificates, like for HTTPS, as new domains require new certs and updating them every year or so, while sub-domains may use star-certs (*.domain.com), and roll up hundreds of sub-domains under a single certificate to manage them.
{{ aside_end }}


Now that we have gone over a bit about the initial planned naming convention, let's make it better.  Here is a proposal:

- web-1-001.product.prod.sjc1.domain.com

I have only added 3 characters to this name, but I have made it both significantly more scalable, and provided a new level of control.

First, how is it more scalable than the previous naming convention of "web-001.product.prod.sjc.domain.com"?

It is more scalable in 2 ways.

First, it is more scalable in the location.  Previously we had "sjc", which meant that the server was located near the closest airport code of SJC (San Jose, California), but which data center is this?

If you only have 1 data center, then you know.  But what if you get a second data center, for redundancy or growth?  What do you name it?  sjc2?  

If you name the second data center "sjc2" and the first was "sjc", you now have a naming convention discrepency.  You previously had 3 letters, now you have 3 letters and 1 number.  This can create parsing problems in scripts, and is inconsistent when you type names.  As you grow in number of data centers in the SJC area, you will have more problems when "sjc3" and "sjc4" are consistent, but the original "sjc" is not.

If you know that something is likely to grow in count, then you should start with a numerical indicator from the beginning.

When we hit "sjc10" we have changed the number of total characters for this section, which we are trying to avoid in other areas, but the number of characters has changed in a deterministic manner, so we can deal with it efficiently and it still scales.  The original 3 letter airport code still stays 3 characters, and the attached number is parsed as a normal number would be.  The string is also split on periods ("."), so everything remains very regular, and whether you account for this scaling change in your original code or not, it is a small addition in logic up-front, and a modest change to logic at-scaling-time.  

This makes it more dynamic, yet still scalable, and so has preference over sjc01 or sjc001, which account for limited growth (100 possibilities), or a large growth (1000 possibilities), but which are immediately more wasteful, mostly in terms of parsing and typing for humans.  This is the tradeoff being made here each time we choose to prepend zeros, or choose not to.

What about "product", is it likely to grow in count too?  No, there is not necessarily a requirement for this.  If a new product does come out that is called "product2", then it is still differentiated from "product", and while it shares the same look and feel as the datacenter location scaling problem, it is actually a different type of scaling, because each of these products is unique and naming them is a business-customer function, not an engineering-infrastructure function.  We will simply shorten the name into an "alias" that is engineering-infrastructure friendly, and also to avoid any renaming that the product line goes through.

{{ aside_begin }}
Often marketing and sales departments will rename a product many times, both before it is launched, and after it is launched, and sometimes "newer versions" of the same product will be renamed, and "older versions" may have the same old name, or may also change names.

All of this name changing is an important part of Sales, Marketing, Branding, etc, but it has nothing to do with engineering or operations.  In fact, it is completely against our interests to change the name, ever.  No matter what happens outside the company, the internal name should not change, because the costs associated with internal name changes are high, and rewards of internal name changes are essentially non-existent.

People from outside the Engineering and Operations departments may not share these values, but they are not tasked with performing actions in the engineering or operational realms, so their opinions are valid for themselves, but carry no engineering weight.

As such, I recommend making internal engineering names that are unrelated to the product names.  They can be related informally, such as one happened to use the name of the original project as the name, and we simply keep that name as the internal name, even if later on it sounds silly or incorrect.  Think of it like a code name.

Additionally, when new versions of that product come out, do not be swayed easily to changing the product name.  If it is in the same "product line", then simply add additional versioning information such as "project" becoming "project2" or "project2016" or "project201605", etc.  These are essentially generic labels, which can be ascribed to the work we are doing accurately, and then can be sold to customers in any way the business likes, unrelated to our internal terminology.

Avoid the loss of productive work time, insertion of data mis-alignment and other bugs, loss of opportunity, now-incorrect documentation, and general confusion added by renaming projects.  Simply name projects something simple (that describes it generally), or code-word related (that doesn't describe it), or any other short and machine-friendly-character-set-constructed (makes good Host Class names, or at least a good variable name), and then iterate on that label, ignoring what the advertising and branding names are.  Focus on engineering and operational stability and accuracy, and keep sales and engineering separated by what customers can actually see.
{{ aside_end }}

This is likely to be controversial, as it is difficult to back up with solid data quickly, so we will cover how to differentiate data like this later to keep the pace moving along.

The second way it is more scalable is that we have a secondary numerical counter for the Host Class.  "001" has now become "1-001".

This provides 2 methods of scaling.  For Host Classes that merely collect a lot of servers, this means we can use the same naming convention once we pass "999" instances for the "web" Host Class in our production SJC facility for our given product.

This would look like:  web-2-001.product.prod.sjc1.domain.com

However, many services have a more interesting use case for this number than simply rolling over at 1000, which is separating sets of machines that hold related information.  Consider these names:

- redis-1-001.product.prod.sjc1.domain.com
- redis-1-002.product.prod.sjc1.domain.com
- redis-2-001.product.prod.sjc1.domain.com
- redis-2-002.product.prod.sjc1.domain.com

These are 4 machines, grouped into 2 sets of 2:  1-001/1-002 and 2-001/2-002

These can be used in many ways, but one way would be that this represents a Master-Slave relationship of data being written and read to 1-001 and 2-001, until one of those machines goes down, and then the other would take over such as 1-001 going down, it would be: 1-002 and 2-001 which are active for reads and writes.

What data is sent to each of these machines could be done based on doing a modulus of an index ID (shard = index_id % 2), or another lookup method (rings, partitions, etc).

In this case I refer to the first number as the "Shard" and the second number as the "Shard Instance", so redis-1-001 is Shard 1, Shard Instance 001.

This is a very scalable naming convention.  It allows for different Host Classes (web), different Shards of data (-1-), different instances in the shards (-001.), different products (.product.), different environments (.prod., .qa.), different data centers (.sjc1.) and the common domain name for internal server hostnames.

Separate from being scalable, this also provides a new layer of Control.

Data in Shard 1 is different than data in Shard 2, and may even have different logic operate against it.  This is more easily handled than differentiating "redis-001, redis-002" from "redis-003, redis-004" for logic that groups data on servers by their position in a sequentially numbered set of server instances.

It is generally better still to use the same logic on all Host Classes of type "redis" and merely differentiate the data sets by the Shard, but if you have grouped the Shards as different distinct numbers, you have this additional ability to control them accurately based on this data.

There are other ways of organizing this data into names, and it depends on what data you need to track, but starting from a naming convention like this when you don't yet have that information is a safer bet than starting with less planning than this.

If you know you have additional requirements, be sure that they are implemented into the naming convention, and kept in the standard.  This is a good standard to be extremely rigid with, as the benefits for having consistent naming are large and increase over time.  

If you already have a naming convention, it is better to stay with it than to change it, but if you do need to change it, it is better to make a new standard, and make all new machines comply with it (if they are not in existing services with the old naming convention).

This way you can at least control your naming conventions in a generational sense, and if you are doing planned work, you should have a very limited number of total generations.

There is a lot more that could be said on just this example, and we will come back to it later, as naming things is, after all, one of the two hard computer problems, along with cache poisoning and off-by-one errors.

2.3.1.2: Alignment takes "vision" and knowledge
-----------------------------------------------

Another important aspect of operational engineering, and engineering in general, is "Alignment".

Things must Align with each other for their full efficiency to be able to be available.  This is easy to see in the physical world: all sections of a bridge must align with one another, fence parts must be in alignment to be a good fence, and support beams must align with each other to provide continuous support in a large building.  Engine linkages must align with transmissions and so on, all things that must work efficiently must have high levels of Alignment in order to do so.

It is no less important in the virtual world.  The entire field of networking is about aligning physical cables and virtual configuration to move frames and packets from source to destination.  Databases are about aligning data together so that it can be stored and retrieved efficiently.  Software is the alignment of a starting set of data, transitioning through consecutive state changes until a result is produced; each of those state changes must be in perfect Alignment to produce that result; with any change a different result would occur.

Everywhere you look alignment is an important factor on the quality, reliability, resilience, and structure and yet like many fundamental aspects of engineering, this topic itself is not discussed directly, and typically indirectly discussed as in how "everything must match up" given different protocols.

You may see where I'm starting to go at this point with all of these fundamental questions and inspections:  these are fundamentals of engineering that we are using every day, but are not being discussed directly in our conversations about our environment, resources, goals, and what we are going to do to achieve our goals.

This lack of introspection of our process results in a lot of miscommunication, and different visions struggling for the chance of being implemented, but without the necessary alignment between all the points of implementation to give us the kind of efficiencies, resiliency and other effects that we desire.

Having this vision requires being able to see "the big picture" as well as the details, and it is important to be able to go from detail to big picture, back to details again repeatedly to see what any proposed changes will mean with regard to aligning with the rest of our details, to create the final result which occurs when all of those details are taken in whole.

This is the methodology I use in designing any solution, and I will try to describe it in enough detail that you can inspect the process for yourself and can hopefully positively supplement your current methods for doing similar activities.

One thing about "vision" is that it is something that takes a bit of experience to be able to see.  One needs to have had personal experience implementing things to really know what effects will result in the implementation, and across enough areas of the environment so that one can see how things align well or do not align well.

This experience is less about how many years one has worked in an industry or environment, and more about the experiences one has had in one's lifetime.  

If you have never worked in the industry before, you will not know how organizations that run production operations, especially internet facing production operations at large scale (which I use as an extreme end of the scaling spectrum), will function and what changes will do those organizations and operating environments.

The more you work in different environments, and complete more areas of implementation, the more experiences you will gain.  You can supplement these by setting up your own virtual environments on any cloud hosting providers, or on your own machines with a series of virtual machines.

All projects, whether in-industry or outside of it, are limited, and never give complete information, because one's viewpoint is limited and the amount of details one can interact with is limited.  So even if you know one environment from beginning to end, having created all of it, you will find another environment that you didn't create to have many different properties, even if all the software used is the same, due to the alignment choices made in it's creation.

2.3.2: An Explanation of Operations
-----------------------------------

This section could be headlines on the front page of any magazine targeted at CIOs, and so may seem a little fluffy and self-serving.

Sales people think of organizations in terms of their sales generating revenues.

Developers think of organizations in terms of the software they write, which may be sold to generate revenue.

Managers think of organizations in terms of the people they manage that do the work.

Customer Support thinks about organizations in that customers would be completely dissatisfied without their support.

Finance thinks about organizations in terms of cash flow, as when an organization runs out of money, they can no longer pay their building leases or employees.

Etc...

Each department in an organization thinks it is a critical department, and they are all right.  No organization would pay the financial and opportunity costs in maintaining any department that is unnecessary, so they are all critical.  Operations is no different here.

There was a time that operations was a lot more like Facilities departments, they bought things and maintained them.  Keeping them powered up and plugged in, and keeping people from stealing or damaging them.  This is not really accurate, but from the perspectives of people paying for these employees, it is pretty close to accurate, and we are currently discussing how organizations see themselves and their actions, and organizations act through using money to pay for services.

What has changed, and what companies have for the most part not caught on to yet, and it will behove operational engineers to start repeating ad nauseam is operations is now the front-line of many companies ability to collect revenue.

This started changing for many companies in the late 1990s, and started to become normal in the 2000s, and by this current 2010s almost every company's interactions with it's customers are going through a network, to servers, and software and databases that run on those servers.

The majority of the companies I have worked for have completely downgraded the importance of their operations departments, giving much more staffing and scheduling priority to other departments.

There are a number of reasons for this, and they are all valid in themselves, as many perspectives are when given in their own context.

However, in a context that is grounded in the physical world the connection to their revenue might look like this for different companies, starting from the least-technological and moving to the most:

- Physical good company.  Makes things that are sold in metal cans, etc:
	- Supply chain management has a basis in digital records at every step.  Some steps involve calling people, writing things on paper, but these are recorded in at least Excel type spread sheets, and at any larger organizations something more similar to an Enterprise Resource Planning (ERP) software to coordinate all the steps are required.

	- Communication with vendors in the chain may have many physical components, but ultimately they are also recorded into digital mediums, at least the low-level of email, if not higher level tracking software.

	- Employee time and pay records are now kept in a mostly or purely digital form.

	- End-user support is typically done via electronic medium (emails, customer support) to 

	- The larger the organization for all non-Internet based companies, the more corporate infrastructure that will be needed to provide support to desktops, laptops, servers to manage directory services (AD/LDAP), backups, storage, centralized software, etc.  More of these services are moving into online-only for small-medium companies.

	- Hold outs will be older (pre-PC age computers) and will need to be small, to maintain operating the manual labor scales

- Non-Internet Services Company
	- Similar to physical companies, but with more smaller companies that can get by without much technology.  Real estate agents are a famous example of this.  Doctors and lawyers are also slow to adopt technology in tracking their clients and work, but in most medical institutes I have seen recently, all patient visit tracking is being digitally tracked.

- Physical software companies
	- Software is sold in boxes, in stores or shipped via the mail on DVDs.

	- All software is written in a networked environment which must remain up for any productivity.  Developers cannot all go home and continue working if the infrastructure going down, and as security levels increase, this is not possible for those reasons as well.

	- Customer support is usually entirely digital, unless it is for Enterprise level software, and then there is phone call and occasional in-person visits as well, mostly as good-faith efforts, not to solve immediate problems.

- Internet Service Companies
	- This is where the real change occurs, and many businesses are becoming more Internet service oriented.

	- Almost every interaction the company has with end-users/customers is over the Internet, and handled by servers that the company manages, and may or may not own/lease.


This is a very simplified spectrum of business, and not meant to be correct or truly representative, but merely to paint a quick picture I need for this example, which I'll start describing... now.


The change is that these days if your operations is not reliable, and you have frequent outages, or long-term degraded performance, or you are unable to respond to customer demands in a "reasonable" time, or competitors have a more reliable and reachable service, then you are directly impacted in your revenue.

If your operations is down, your customers cannot reach you to pay you.

As someone reading this book, this is no surprise to you, but what may be somewhat surprising is that many companies I have worked for, and you may have as well, display all the symptoms of completely not behaving like this is true.

Some of these symptoms are:

- Not properly staffing their operation teams for the workloads they are required to perform.  Note that it doesn't matter *who* the operation team staff is, System Administrators, Site Reliability Engineers, DevOps, Developers, it doesn't matter.  If they are responsible for the operations of the software and systems, they are the operations team.

- Not giving proper lead times on work that is due, such as finishing a project that the operations team was not notified about, and expecting an immediate release to the public of that project.  Not taking into account either ordering hardware, or configuring systems to support the software.

- Not giving significant information on how to maintain, run, or even install the software to be released and supported.

- Prioritizing work that does not yield to improving or supporting the revenue generating and employee supporting software and services.

There are many other symptoms, but these are large enough to illustrate this point.  Other departments have similar complaints with regard to notice ahead-of-time, and schedules.  See any book on Software Development project management for examples close to operations.

This is not a problem that is likely to be solved soon, if ever solved, because there are a number of difficult factors that cause it; the primary one being the structure of organizations themselves.  When something is structured a certain way, it will tend to produce certain results, and producing different results is very difficult, and often only temporarily possible.

Since the organizational structure of organizations is not likely to change, the best hope in making progress here is something akin to the Agile movement in development, where all developers just kept repeating the same things and eventually the management of companies started to be populated with managers who also said the same things, and their world changed.

It's debatable on whether their world really changed that much for the better, but there are many distinct differences in the pre-Agile development world, from the post-Agile development world, and it was this change in perspective and discussing it that caused those changes to take effect.

It's also worth noting that the way this change-through-repetition occurs should be done with as much awareness as possible of what is being repeated.  If it is something that will become a dogmatic problem, then that is not a good thing to repeat.  Thing's to repeat should be based on ideas that cause more awareness to the complexities of the present reality and less dogmatic simplicity, which frequently ignores any local data and instead focuses on following idealistic principles.  If a principle sounds too idealistic, it probably is.

2.3.2.1: How is this not a core-service?
----------------------------------------

One concept that organizations have a pretty good grasp on is "core services".  They understand there are some services that they cannot outsource to other organizations and remain an efficient operation.

The core-est of these core services are: management, finance and human resources (HR).

Almost no organization outsources its' people managers.  They are the most core-service that a company has.

Similarly, there will almost always be at least 1 to several people in the finance department, even if they use external services for many services that used to be hired in-house.

HR in the past decade has begun to be outsourced, but once a company reaches a certain size, they always have their own HR departments.  This is the same for legal services, though this can be configured in a number of ways for companies, so I'm not listing it as a core service.

Many companies outsource their development departments, and many companies also try to outsource their operation department, though this does not usually last long, and they may try to stick with it by turning their developers into their operations staff, but eventually some people will end up being the de facto operations team, regardless of their titles.

If a company is primarily a software or internet service organization, and these are the types of companies I focus on, so they will be the majority of what we spend time inspecting, then they are much less likely to outsource their development departments.

They realize the developing software is a core business service, and without direct control of their developers and efficient communications, they are unlikely to make consistent progress.  Many companies that try to outsource this department end up moving it back into their company after poor experiences, unless the product being developed itself is not all that important to the company, or can be treated as a throw-away product (like a phone application they only need to do XYZ "well enough").

This is all a pretty subjective description, and I won't use up the space to turn it into a more objective one.  You should review your own experiences with these descriptions to determine how accurate they seem to you.

The point of this discussion on core services is that for any company that relies on Internet or networked services for revenue generation, their operations department is not only a core service, but is often the front door to any other services.

If their operations is not available, or performance is significantly degraded, then their customers and partners are not able to use their services, and they cannot generate revenue.

This would be similar to sales people losing the ability to contact customers, completely making that department unable to provide benefit.

If a company develops software, and end-users cannot reach that software, then there was no reason to develop it.

This is where operations sits in the revenue chain, and companies are not yet currently recognizing the important distinction.

I have used many similies for this over time, such as:

- Operations is like the tires of the car.  We are the part of the car that comes into contact with the road.  Your driving can only be as good as your traction against the ground.  If you lose a tire, your ability to drive is severely impacted or not possible. 

- Operations are like the roads.  You can have a fleet of cars or trucks, but you cannot efficiently move them around without roads to provide consistent surfaces.

A lot of people shop for cars, but not a lot of people are involved in the building or maintenance of roads.  This is similar to many people using networked services, but not being aware of what it takes to build or maintain them.

2.3.2.1.1: Just because it's Core doesnt mean...
------------------------------------------------

A service may be a core service, but that does not mean all of it needs to be internally owned and operated.

Cloud datacenter operations and Software-as-a-Service (SaaS) have changed the way many companies perform their internal and external operations, and has provided new ways for many engineers to think about solving problems.

Just because you are paying someone else to maintain hardware or software for you does not mean that you do not need to manage it.  Some SaaS products do not require much management, but other still requires one or more full time staff to help manage it for the rest of the departments.

For machine and datacenter operations, having Cloud offerings like Amazon or Googles offerings does not stop operational work from being created, it only raises the bar on what type of work is required.

The basics of buying machines, racking them, cabling them, keeping them physically functioning (replacing disks and RAM, etc) and doing basics like assigning their primary IPs is taken care of for you.

Everything above that level is up to you to manage, and these are the more complex problem areas, as the lower level areas are more logistical, scheduling and manual labor intensive.

Who will manage all of the rest of the decisions and life-cycle maintenance problems that your network services require to function properly?

Whoever they are, whatever you call them, they are your operations team, and are providing the operational core services for your organization.

Outsourcing works up until the point where you lose Control that you need over the environment.  At some scaling point in every organizations usage of an external service, their needs and the services offerings will start to part ways, and the service will start requiring more work than previous to perform the same benefits for the organization.

Once this reaches a critical point, either though financial cost, personnel time cost, or cost in terms of outages, degraded performance or misalignment in terms of providing the kinds of services the organization requires.

Once this point is met, there will be a new transition where the problem areas are migrated to another service, which it is hoped will solve these problems, or the services are migrated in-house to be internally managed.

At present the financial costs alone seem to be consistently measuring up like this:

- Internally managed infrastructure.  1x cost, of hardware, data center and network services to provide an operational environment.  This is the base-line, doing it yourself.

- Managed services that are comparable to doing it yourself, but letting others do it for you, about 3x the base-line cost.

- Using cloud services, where you manage all your infrastructures through a virtual interface is about 5x the cost of doing it yourself.

This is highly subject to change, as many things are involved in pricing, but as of 2015, this has been accurate in all the measurements I have made in about 10 environments I had direct internal access to, from 2008 to 2015.

What are the differences in cost in your current environment, between total ownership/leasing, managed services (someone else buys/leases and maintains), or going completely virtual?

You should know these differences, as they will make data points in decisions on how to run your departments as the costs start to outweigh the benefits of any solution.

This 1-factor look at the problem, financially, is not a "big picture" view, it is only a single detail, so there are many other factors which make using services that may be 5x or 3x as expensive, and provide worthwhile benefits, such as the total cost being low enough to be worth it, or the faster turn around time on new machines, or not having decided on the hardware requirements to make it practical to start ordering hardware yourselves.

There are many more factors in this, and we will get into some of them later, but they are not the focus of this book, so we will not cover them comprehensively.

2.3.2.1.1.1: Typically companies still don't...
-----------------------------------------------

The problem of communication between departments, especially in regard to lead times between knowing they need work to eventually be done, and when they alert another department or team that they need that work done is such a classic problem that we can just assume it will happen everywhere, in every circumstance, unless people do something to change the pattern.

In places where departments are giving each other prior notice of work coming down the pipeline, and involving the teams they will need to do that future work in the design phase, it is very likely that this was set up on purpose, and either by "visionary" early employees or founders, or through great work of some individuals to make changes to the de facto process of only asking for work to be done, when it is at the end of the project and time to release.

I say it's most likely that this is the problem, because I have only worked in a couple environments, out of a large number of environments, where this happened as a normal occurrence.

The point I am making is that one shouldn't be surprised when another department or group arrives and says they have finished a project, and they "just need it deployed into production", and has no time available in their release schedule for doing things like:

- Productionizing the release process
- Productionizing the configuration
- Doing security audits and fixes
- Writing an operational manual with support play book, enumeration of error codes, instructions as to options

Frequently projects just being released into production do not have good performance tests done of them, although this happens more frequently than others, so I'm not including it in the above list.

One of the lessons it took me a very long time to learn, but has served me well since learning it, is that if you recognize a pattern as occurring regularly, it is better to simply plan to deal with that pattern than to put up any resistance to it's existence.

What I mean by this is not to get upset when you are given these types of projects, and they require immediate action, and things are requested to be done "wrong" and they cause havoc with the clean environment you are trying to make.

Instead, see them as failure to get ahead of a pattern that occurs so frequently that you can simply assume that there are cases in process of coming to you right now.

Knowing this, how do you get ahead of this problem?  You can't completely solve it, as it requires cooperation from other people, and the root of the problem is that they themselves aren't coming forward to cooperate before they normally would.

Some things you can do:

- Regularly, say every month, send out a standard template communication (email, etc) to all departments asking if they have any projects that will coming down the pipeline and will need operational resources.

- Describe in the communication what "requires operational resources" means, such as machines in production, adding a new service, making changes to services which aren't already in production or that the operations department doesn't know about, etc.

- Describe any lead-times you require for these types of projects.

This is the direct-but-passive communication approach, and will allow people who are up for communicating ahead of time to communicate with you in a way they can understand is helpful.  This will not catch all new projects.

From there you can also create a department policy, document it in your online documentation site (wiki, etc) as to how you accept new projects, and when people ask you for them,  you can refer them to the "new project on-boarding" documentation that describes how you would like to work.

This provides some "back end" type protections, as people will see that they didn't communicate with your regular email, and now they are learning how the operations department works.

But this will still not stop any externally set schedules, as if the company requires a product is launched on a given date, then this is a higher priority than following any department's self-appointed rules, and will override them in many circumstances.

The direct-active approach is the best, but requires more resources, this would be someone who is acting a department project manager would meet with the other department heads or team managers directly, and ask them what they are working on, and when they will need operational resources.

This direct-active approach is more likely to be successful, as the managers will know what projects they are working on, and are not trying to hide their project's work, they are simply working to complete their projects, and in this way you are assisting them in getting to the final steps of completion.

If this can be approached in a "let us help you" manner, then collaboration can begin, and hopefully will improve the working conditions for everyone, as handing off work between groups is a difficult process.

2.3.2.1.1.1.1: The Ops department is blamed for all lag
-------------------------------------------------------

A look at the more negative side of this problem between groups is that the operations departments are often claimed to be creating lag between work being completed by other teams (typically development, sometimes marketing or business development).

From the perspective of the non-operations teams, this is a true statement.  They finished their work, and now they want to put it into production for end-users to be able to access, and any time between them being "finished" and the end-user being able to access the work is considered lag created by the operations department.

The issue here is one of "someone else's problem" (SEP), which comes down to empathy and a realistic view of the nature of all work involved in a company, not just one's own work in the company.  This is not a problem that can be solved directly, as people's ability to appreciate other's position's is not going to change easily, or deterministically.

So what we can do is to look to ameliorate this problem as much as we can, by getting ahead of the requests.  This means having a process that people can easily follow to getting what they want.

For example, create a limited set of Hardware Specifications that you purchase, for any generation of hardware.  The typical basics of this as of 2015 are usually a "utility" class machine, a "relational database" class machine, and a "non-relational database" class machine.

To simplify what we call a Hardware Specification, let's use the acronym for Stock Keeping Unit (SKU), which is very general.

Utility class machines are for running general purpose software, and typically are mostly used for web and application services in production.  There may be two SKUs if there is a "low memory" and "high memory" version.  Caching services (memcache, redis) usually use a low amount of CPU, but a high amount of RAM, and may reside alone on machines due to their critical nature.  Utility machines typically do not need much in the way of storage, and almost any small redundant disks are good enough.

Relational Database class machines are typically used for relational SQL databases like MySQL, PostgreSQL, etc.  They need both a lot of RAM, a lot of CPU cores, and they need very fast disk.

Non-Relational Database class machines are usually running software like Hadoop, Cassandra, or any of the other many column-oriented databases that are better at storing logs, events, time-series than other databases.  They typically need a lot of CPU, memory, and much more storage than relational databases.  If a relational database might need 5TB of storage, a non-relational database might need 30TB, or something in this type of proportion.  Currently (2015), many of these types of systems still use rotating disks as their primary storage as they provide high capacity, and the quick-access times of SSDs are not required (for some platforms), or they may combine SSD with rotating disks for a recent and longer-term storage.

Starting with these 3 base SKUs, and perhaps several sub-SKUs for more RAM, you can offer departments easy choices for how they want to deploy their software.  Providing them virtual machines for some services may also be a good match, depending on their usage patterns and criticality.

For each type of request they are likely to make, having already worked out in advance what options they will need, in a sort of restaurant-like menu, will allow you to make the requests more streamlined, and work better with your organization.

You can add SKUs if necessary, when they have a strong need (for example, a large order of systems that have a usage pattern that do not match any of your existing SKUs), and otherwise they have an easier by simply selecting what seems best to them.

This can also be done for:

- Networks:  Have set ranges of IP space that you assign to a given network, such as standardizing on /23, /22 and /20.  If you only create server networks of these sizes, then it should be pretty easy to size them appropriately for a given request that needs their own network.

- Load Balancing:  If you have a pre-determined set of options say using SNAT with X-Forwarded-For for all web services, then you can announce that early, and avoid running into problems where web applications require the source IP in the request.

- Host names: As we went over earlier, there is a lot of information stored in names.  If you give a guideline of what your convention is, and how to apply that convention to various configurations, you can avoid being requested to make names that do not fit the convention, as you have already described how to take their configuration and put it into your naming convention.

- Accessing production machines:  You should have a security policy that can be applied in a standard way to all requests.  Do you allow root logins?  Root escalation?  Sudo?  Role accounts?  Copying data to machines?   You should write each of these things down, and where you do not allow something, you should have a method for how to accomplish that goal in a manner that is consistent with your security policy.  If you do not do this, people will just work around your enforcements and create many messes as everyone does it slightly differently.

It is unlikely that people who perform different roles will start to become empathetic that the work done in others' roles really does take expertise and time, since we have so much history of people not having this empathy, but we can do things to try to bridge these gaps by being aware of them and tuning our behaviors accordingly.

2.3.2.1.1.1.1.1: Everyone doing everything themselves is...
-----------------------------------------------------------

One important component of all operational environments is standardization.  At the extreme end of that spectrum would be uniformity and at the other extreme everything is unique:

Everything Is Uniform <---> Everything Is Unique

Since we know that not everything can be uniform, since we are already starting with a base of 3 SKUs (Utility, Relational Database, Non-Relational Database), that side of the spectrum is already constrained.

However, it is completely possible to have an "everything is unique" operational system, and this might be labelled something like "operational hell", where everything is a special snow-flake one-off case.

In an "operational hell" environment, no change can be assumed to work for more than 1 specific case.  That case must be inspected just prior to being modified, because it could be in any type of state or configuration at all, and the only way to have reasonable confidence that the change will not break things would be to look at everything going on on the machine, all configuration, all currently running processes, and to determine through expert-understanding that the planned change will work with the existing configuration.

This is the most dangerous type of environment to work in, with regards to uptime, stability, efficiency, and all the other positive attributes we want to imbrue our operational environments with.

All it takes to create an "everything is unique" environment is to let everyone solve every problem in the way they see best, at the time they got the request, without communicating the changes to others, and aligning the changes so that they follow a planned path.

Many requests into operations will diff from previous requests in some way, making it impossible for the current request to be handled in the same fashion as the previous request, because of those differences, but still the methods used to take care of the previous and current requests could be aligned with one another.

This type of alignment does not come for free, and it does not come naturally.  It is a process that must be learned, and it takes coordination of all the different members of a team to work together in ensuring that this alignment takes place.

Alignment itself has a spectrum, and is best seen at different levels of details.

We can "block box" anything into:  Inputs, Outputs, Side-Effects

Inputs are what comes into the black box, say HTTP requests for a web server.

Outputs are what comes out of the black box, sat the HTTP response for a web server.

And side-effects are what happens beyond the outputs, say that a database is updated, and a memory caching server is updated, and logs are written to storage.

Black boxes are an appropriate level for a group to be able to discuss alignment, as getting into implementation details of how a web server is configured should be left to the sub-team that deals with that web server. 

This is to allow people and sub-teams autonomy of action, as centralized planning cannot deal with all details and all contingencies efficiently, while still allowing a larger centralized inspection of the black boxes, to achieve a total operational system alignment.

There's a lot involve in this, and we will be going into more depth as we move from philosophy and general issues into implementation.

2.3.2.1.1.1.1.2: What can be self-service, and what cant
--------------------------------------------------------

One goal for an operations team that has decided they want to get the benefits of comprehensive automation is to provide more and more self-service tools to the departments they support.

The benefit for the operations team is that they can remain more focused on improving infrastructure, rather than performing requests that were made by other teams to simply set up, configure and change existing infrastructure.

There is also a spectrum of productivity to this:

Handling Requests <---> Improving Infrastructure

The more of the operational team's resources (time, people) that are committed to processing requests made from outside the team (other departments, higher management), the less time the team is able to work on improving the infrastructure that exists, including improving the ability to handle the incoming requests in the first place.

I have worked in many organizations where the operations team spends nearly all of their time performing requests, and almost no time improving the infrastructure, and as a result the infrastructure becomes more and more fragile as request after request is done in a manner that is not scalable or supportable, but is required to meet business timelines and direction.  In this way the Alignment between all elements of the operational environment becomes worse and worse over time as each one-off request is handled specially and the system becomes more "de facto" and less planned.

Achieving business goals is the reason all departments exist, so it is a good thing to get the work done, but if it is performed in a manner where the business begins to operate less efficiently over time, and eventually starts to fail frequently, it can cause harm to other business goals, such as customer retention, which effects revenue.  So both getting the work done, and getting the work done in a way that improves the ability to do more work in the future are important goals which must coexist in an healthy environment.

In order to handle requests efficiently, the infrastructure must be one that can reasonably be altered to support this requests, and as the business changes in scale, scope, and direction, this takes either a very well put together operational environment that is made to be changed quickly in these manners (possible, but difficult to assemble, and easy to turn less-functional), or it requires time before requests are done, to prepare the environment, or more time after the requests are done to fix the system after the fact.

This is also on a spectrum, so you can't have both extremes as being simultaneously true in the same instance, which means you need to acknowledge, plan for and deal with the trade offs actively both over longer periods of times (quarters, years) and for each request, with an understanding of the scope of each requests potential to make positive or negative impacts on the infrastructure.

What do I mean when I say two extreme's can't be true at the same time for the same instance?  Apart from the truism there, what I specifically mean is that an environment that is not flexible must request time to complete requests to stay a healthy environment.  And a team that does not have time to complete request appropriately must have a flexible infrastructure to be able to finish requests without "enough time" to change the infrastructure to keep it healthy.  So either the team must have time, or the team must not need to have time, in order to keep the infrastructure healthy.

Failure to either get enough time per request, or to have an infrastructure that does not take much time per request to remain a healthy environment, will result in an operational environment that becomes unhealthy, and will begin to exhibit the unhealthy signs:  Lower Availability, Lower Performance, Lower Correctness, Lower User Satisfaction, Lower Maintainer Satisfaction, Lower Developer Satisfaction, Lower Revenues, Lower Opportunities, Lower Ability To Be Manueverable, etc.

This spectrum is fairly specific, unlike "Not Available <--> Available", which is a fairly straight-forward concept to understand as a single topic, this axis' line moves among many topics to create a sliding scale between all of them, in a very limited manner.  It is a line that travels through N-dimensions of information space.

Trade Off Between Team Time and Infrastructure Flexibility For A Healthy Environment:

Team Has Time To Manually Perform Requests <---> Infrastructure Is Flexible Enough To Take Requests Quickly Without Requiring Significant Team Manual Time

This flexibility to be very specific with an axis, and to cross many boundaries of topics provides another benefit to Axiomatic Engineering, which is that "Compare and Contrast" type efforts can be very explicit, and anything that is too complicated to talk about clearly can be turned into these very specific sets of axises, which can than be given numerical values, and compared against each other.

Because the topics are specific, and the numerical values gives your preference (or could be data collected through automation or monitoring) for describing very specific things.  If you have related concepts that are specifically explained in separate axises, then the resulting quantified numbers of those axises comparison can give deeper insight to the problem, and can be communicated accordingly as Engineering Oriented Information, separate from normal communication in it's attempt to be precise and descriptive, attempting to be as objective as possible on data so complicated it must be subjectively formulated.  Mathematics are such a notation for dealing with problems in that domain, but these are problems in a different domain, and need a solution as customized for that domain as the mathematics solution is customized for it's domain.

This is the problem that we must work to overcome with any engineering field, in that there are too many variables, both known and unknown, to take into account, and to communicate about them is impossible to do accurately, and difficult to even do effectively.  

Since we know accuracy, perfect accuracy, will be impossible, we must strive for maximum effectiveness, where we get the most value for the least effort, while not using too little effort so that we get the best results possible with the resources we have to use.

2.4: What is a System?
----------------------

There are a lot of ways the word "system" could be used.  We're going to look at a general version of the word first, and then a specific version for our exact purposes afterwards.

When I was growing up and for the first 10 years of my career, operational engineers were called "System Administrators".  Today some people use this term derogatorily as lower-level or older style work, and while anyone can have any perspective they'd like, this is not consistent with history.

I was lucky enough to spend some time around professional system administrators throughout the 1980s, before I was old enough to work, and I got to see them doing core dumps and reading through the hexadecimal output to find where the problems in their code were, and even fix some problems through a hex editor.  I also got to get a bit of their practical advice and viewpoints, and I believe that after 5 or so years of professional operations work the lessons I saw back then started to filter back in to be more conscious rather than subconscious guides and role models.

So, what is a system?  Historically, in the computer industry, a system was often referred to as a single machine with an operating system on it, and the environment that was then configured on top of that to create a working environment.

A system was sometimes a machine's hardware, an operating system was also a system, and the eventual configured environment was a system.

One of the interesting properties of the word "system" is that all of these things were and are true.  And all of these things together are also a system.

A system is an generalized term for a set of interrelated, connected things that can be used together to produce effects.  Like anything, it is black-boxable into inputs, outputs and side effects, and has sub-components which can be similarly black-boxed, etc.  Systems may contain Real or Virtual components, and may create Real or Virtual effects, and combinations thereof.

So, a "system" is a flexible term, and is something like an "environment" or an "ecosystem" in common usage.

I like to think of systems as being somewhat like virtual machines, in the actual sense not in the container-type-operating-system sense.  A system's connections can be graphed, like a network, and each component and be described by the inputs, outputs and side effects it causes, and may contain many layers of other systems, and may be part of a bigger system.

Why is any of this important?  Because your understanding of how systems works will determine your ability to mentally map the systems that you work with, so that you can think in terms of how those systems function.

Without having this mental mapping, and having a mind that over time becomes more and more comfortable learning about systems, and understanding system intra-action and interactions, one will have gaps in their understanding.

These gaps are perfectly fine if they are properly black-boxed to create a comprehensive system, where you may not know how memory data is shuttled between the RAM chips and the CPU, but you have a model for how this works, and that model, while not physically accurate in detail, has a strong correlation to reality and can be used to make good decisions and predictions.

We will go deeper into Modeling in the future, but building accurate models of the systems you are working with is an important part of operations.

When someone has a poor Model they are working with, they will be confused by things that occur, and are likely to have "magical thinking" ideas, like "out of nowhere, X just happened".

When someone has a good Model and "X happens", they can see that X is related to Y and Z, and without first Y occurring, and then Z occurring, then X could not occur.

They can trace this backwards and confirm that indeed Z occurred, and Y occurred, and so of course X was going to occur in sequence after them.

For a common example of this, a web server starts to fail, and on inspection the disk is full, and on further inspection no log rotation was configured, and so the web server failing is a mechanical response to the disk filling up, which is a mechanical response to not having logs being rotated.

If you do not rotate logs (or otherwise truncate them), then with any activity at all, it is guaranteed that eventually the available storage will fill up, and any services which might use the storage for writes (such as logging) will fail.

This is an example of a simple system, and indeed anything can be turned into a system, regardless of complexity or their nature.  Additionally any given topic can be turned into multiple different systems which are all different, but all accurately model the topic, providing different descriptions, and showing that no single model or system will be the only description of Reality, they are simply one method of attempting to summarize and communicate information.

The power of Systems is that they can be created at any time, to describe any thing, provided you are capable of properly black-boxing the components of the system you want to construct.

You do not need to constrain yourself to existing systems, that other people have described, even when working with their work which have their own systems already described and available.  You can create your own systems for your own purposes, to either assist yourself or communicate with others, or as tools to perform work.

You might create alternative systems to simply understand other people's described systems.  Sometimes it is harder to understand someone else's work than your own, and so creating your own work can illuminate a subject.  Sometimes just writing down someone else's ideas in your own words provides insight you were previously missing, and allows you to understand the system you are describing, in a way that is more comprehensive or deeper than merely trying to use someone else's system.

As an exercise while you read this book, try to create your own systems based on "the big picture" to understand what is currently being discussed.  As new information comes in, update your system to reflect these changes.  Attempt to switch from "big picture" to "details" and back again, to deepen your understanding of individual topics and the overall topic.  

Imaging looking at a forrest, then the leaves of a single tree, then back to the forrest, then looking at a specific leaf on a single tree, then back to the original tree's set of leaves, etc.  The information is always a summary of something, whether you are look at specific pieces of summarized information, or larger sections of collected summarized information, you must be able to understand it, and have opinions on it based on your goals.  Will it assist your goals?  Will it make it harder to complete your goals?

You can create your own systems on paper, in your head, you can find software that helps you create systems quickly (like Mind Map software), or use relational databases to track discrete data.  

Flow charts are one way to map systems, finite state machines are others ways, behavior trees are another way, but you can also describe them in prose, or doodles or any other way.  Experiment, and find ways you enjoy.

How you describe a system is merely a view into the system, and will never cover every aspect of a system, but each change in viewpoint gives a better angle on some information, and a worse angle on others.  

Only the actual components of a system describe the system, and any attempt to review the system will only give a partial insight into it, because it is a summary of something else, because a map is not equivalent to the territory it attempts to describe.  

By "actual components" I mean the things that make up the system are separate than our understanding of them, and our descriptions of them.  They exist outside of our information, and so they are not only super-sets to the parts of our information that are accurate (and not related to the portions of our sets of information that are inaccurate), but that they also contain more data than we are aware of, and almost always some data of which we cannot become aware of because of the limitations in our ability to detect some things, and the limits of our knowledge to know to even try to detect them.

Systems are tricky in this way, but this is also where their power comes from, because they are not limited by the nature of the actual components; they can be extended in any way you can think of, it it will assist you in your goals.

2.5: Systemic Thinking
----------------------

I'll use "Systemic Thinking" to mean thinking in a way where everything is inside of a system.  Systemic Thinking focuses on the relationships between all things in a system, and their mechanical relationships to each other.  A system being a set of things you wish to model, to accomplish one or more goals by using the model to understand mechanically what the effects of a planned action would be.  It is mechanical because it has inputs, outputs and side-effects, and so can be tracked and operated on as any mechanical device can.  This is a Virtual Mechanical Device, which operates on Data.

The Model gives feedback about what the current state of the Set of Components are, and what the likely state of the Set of Components will be if an action were to be performed.  This also works in reverse to provide information about what happened in the past, by comparing Data to the Model, which can both improve the Model by correcting it against Data and Reality, and give information by inspecting the Data produced by Reality, and using the Model to explain that Data, given the error tolerance you have for the accuracy of the Model's ability to explain this Data and the correctness of the actions to perform the explanation.

A System can be described by a network of black box functions which take inputs, emit outputs, and perform side-effects, totaling the results of anything that exists or doesn't exist, Real or Virtual.  Either way, it can be described as a System, and using this methodology for organizing one's thoughts is "Systemic Thinking" by my definition here.

I believe Systemic Thinking is one of the most powerful and useful tools in our mental toolbox, and could use a lot more of the educational spotlight.  In terms of yielding positive results in learning speed and depth, creating works, and in performing maintenance (ie. troubleshooting), Systemic Thinking is among the most useful tools.

Systemic Thinking has a number of prerequisites, such as a general understanding of how systems work, how to create systems, how to modify a system, how to inspect and evaluate the connections and links between system components, and a good basis in critical thinking.  Having the ability to think Deductively and Inductively is a fundamental requirement.

If you have not yet read a book on critical thinking, you should, to ensure you have the basic understanding of the topic.  Of course you can fill in this information later now that you know it's something that could benefit you.  

{{ todo__recommend_critical_thinking_book }}


{{ asside_begin }}
{{ NOTE: This is too long for an aside, and is better suited to either being chopped up and put into other sections, or else chopped up and put into a reference section in the appendix. }}
{{ IDEA: The aside is just a reference to an Appendix chapter, so that it doesnt take up any space or change the pacing of the chapter.  This idea is a winner.  Do this and clean this junk up.  The cleanup will require changing the verbiage of this section into stand-alone, so that it can be read without the current context.  This will also help clean up the rambling nature of this section, which rambled ramblingly. }}
There is an infinite amount of information that is possible to learn, so the important thing is to bookmark all new "requirements" for the future, and follow up on what is most useful for the current goal to be accomplished in the present.  

This creates paths for future obstacle clearance, once one encounters an obstacle based on a required skill or set of knowledge, and minimizes disturbances to accomplishing one's current goals, which will always yield the most immediately rewarding results, since they were prioritized as objectives.

Deductive and Inductive Reasoning, Boolean Logic, and Set Logic are the primary tools for doing analysis, and any troubleshooting of Systems will be significantly improved if you can break things down to terms and evaluate them for correctness against various assertions, as well as whether the assertions are valid or invalid.  

It is of critical importance that one is able to test the validity of an assertion.  Without being able to validate or invalidate an assertion against it's test's result, one will not know if they are making a decision based on an invalid assumption.

For example, if there was an Web Server outage for 30 minutes, and in the outage post-mortem discussion the Root Cause was suggested to be an ISP outage, as it was during the time window their ISP told them they would be doing maintenance.

Except, that in this example, that is not the correct cause, as an engineer got an alert on their cell phone that a service was down, they logged into the specified server, saw a mounted volume had no space left on it; so they deleted some old log files, and the service started working again.  Then they filed a ticket about it and marked it as an outage.

But, in this example, the person who suggested it was the ISP's fault did not read this ticket, and so was giving their best guess as to what happened, based on information they had, that they thought was relevant.  

If no one with better information was present in that meeting, then that could very likely be selected as the primary reason for the 30 minute outage when it is written up as Root Cause; when in actuality, the outage was caused for a different reason, and that reason was fixed and logged according to standard work procedures by the engineer on-call.

Being able to test the validity of an assertion allows us to qualify an assertion against it's subject.

If we were in the meeting we could qualify the assertion that this was related to an ISP maintenance notification we received by comparing it to the data known to correlate that assertion with the actual outage.  Is it valid or invalid, based on the data we have?  Is it matched to actual data, or a data-less hypothesis?  Unqualified assertions do not have data to back them up, qualified assertions do have data to back them up.  An assertion can be both qualified and wrong, as it can have data that backs it up, but also data that invalidates it as an impossibility, so it is qualified as incorrect.  In the same way, if all the data did back up the assertion, then it would be qualified as correct with the data current inspected, or some probability thereof if the data is inconclusive, so a Root Cause is still yet unknown, though there are possibilities.

{{ exercise: build a matrix of all possible scenarios for an assertion being qualified, conclusive, and correct.  Write an appendix entry that goes over this. }}

If the the post-mortem meeting attendee who offered the assertion was asked about the qualifying information to their assertion, they would explain that they didn't verify this was the case and so cannot qualify it, but it matches the time frame of the notification.  We can conclude from this that while it is a possible lead to look for correlating data/evidence, it is not a candidate for Root Cause yet, because there is no data to support that candidacy.  Having no candidates is a valid state to be in, because without supporting data, there can be no valid candidates for Root Cause.

Without any data, this is only a speculative relationship, due to correlation of information:  notification and outage windows, but no data correlating the outage with the maintenance directly.

While this is a higher-than-other-unknown-topic-priority topic to collect data on, since there is a time window correlation which adds priority, all other areas of the operational environment still need to be prioritized to collect information on, in order to find a direct correlation between the outage and the thing that caused the outage: the Root Cause.  

Prioritization is based on which Components of the Environment are most likely involved with the outage, based on the match between the data collected from monitoring and what those our Model predicts the results would be if a given Component failed, under a given condition.  This description can be called a Component's Model, which serves like a fingerprint to distinguish how that Component interacts with data, which we use to predict future state, or extract information from historical summaries.

To elaborate on a specific item in prioritization: it is important that the collection of information on the ISP's maintenance should be given less priority than collection from some other sources, even though it is a known-likely-possible-cause.  It has elevated priority over the set of all places to gather information, because of the time correlation, but must be ranked according to the total set of indicators, not just that one indicator.

The reason that it should get lower priority than some other areas of collection is that the maintenance correlation was temporary and a one-time thing, and is already over.  So, collecting data on the ISP maintenance correlation is going to improve your records of events, and possibly has financial or contractual ramifications, which are important, but are not urgent in terms of time to response, since they are going to take time to process, on the order of weeks, or Quarters.  This is an event that can be reacted to at lower priority, because it is over and non-recurring in nature (vendor scheduled maintenance).

In comparison, if it was not the ISP maintenance that was the Root Cause, then the problem could still be occurring presently, and could be causing degraded service, or potentially failing in a manner that is not being monitored or alerted on, or is going to pass a threshold and begin a new outage soon.

All of this can be found through troubleshooting, using the required skills of Modeling your System against the perceived and summarized Reality of the Components in your actual system, turned into a database-like schema, and then using that Model to reason about what happened, or what will happen.

This tangential aside has already turned into an epic side-quest, but I have additional point to make on the topic of goals.

Programming a computer is done with a programming language (C, Python, Java, etc), programming your mind is done by making physical and chemical-electrical changes to your brain by learning new skills and information (creating change in the patterns of connections and firing), which gives you a larger library of activities you can perform and problems you can solve, which gives you improved ability to accomplish your goals.

Accomplishment of your own goals, in my opinion, is a Primary Life Requirement, and should be an ever-present factor in each decision you make in your life, in order to yield yourself the best results.  Prioritization and other balancing factors between all things is necessary to achieve efficiency, so we can create Models that we believe are oriented towards creating work that is Aligned with our goals, to create the Reality we are attempting to achieve through applying effort.

And, as an aside to this aside, the previous paragraph is an example of attempting to use a Mental Model or doing Self-Programming or whatever label seems best to apply to it, I don't think there is a good one yet.

I created an English version of a descending mechanical-relationship tree, which Im defining as a tree of attribute descriptions which are related to each other by description of any input, output or side-effects.  Each element shows hierarchy in terms of the described relationship, and the total space of all the ideas gives a "shape" that the reader can use their own information to populate to give them an idea at a certain "size", given the total "size" of the labels being used and the amount of labels and relationships, with bias towards their personal experience.  This is a type of "Information Spatial Reasoning" in that they can use the resulting model to compare it against other models to see where they overlap or do not overlap in the space of all the contained ideas and information.
{{ asside_end }}


How do you use Systemic Thinking?

The first thing to do is to take whatever you are thinking about, and turn it into a system.  Anything can be turned into a system, and this system can be as large or small as you need, and can contain any number of components.  We will start with this system being a set of things that you list.  A "set of listed things" is a very basic system, and then anything can be added onto this, making it a more complex system.

Since we, as humans, are limited in the number of things we can think about simultaneously, on a conscious level especially, we need to break things into small groups of related ideas.

Let's create a system right now and do some reasoning with it, to use as an example.  We will continue to use the web server analogy, as it is one that many people will already be familiar with, and are likely to spend a lot of time dealing with in their careers, as it has become the default medium for information exchange.  You can think of this as an "Application Server" instead of web server if you like, the important thing is that it takes requests and serves back data.

In the simplest of web server systems, we have static content serving.  This is when someone has pre-created text (HTML, CSS, etc) and binary (images, videos) and the web server's job is to take requests for specific static files, and to relay those files to the requester.

Since we can create a system out of any components, let's decide what our components will be:

- A network connection to the Internet, which end-users are making requests on.
- The IP protocol for networking, and basic TCP session management, on a Linux server.
- A web server that listens on TCP port 80 on that server.
- A file system that locally contains system files.
- A file system that locally logs requests and processing.

This is a slice of components involved in a web request, and just as I have arbitrarily picked these for this example, you can pick any components you want to build your own systems.  

You can continue to refer to the same system over time to get more familiar with all the details of that system, as is important in operational and application documentation, or you can abandon the system as soon as it's immediate purposes are over.  Systems can be used forever or can be completely ephemeral, they are abstractions for reasoning and understanding reality, which remains too detailed and complex for us to directly understand.

Let's create an event that occurs and exercises these components, as a sequence:

- An end-user requests a file from the remote web server: http://www.domain.com/images/unstoppabletrex.png

- The request performs operations outside of this system (LAN, routing, DNS, etc), but eventually opens a TCP socket to port 80 on the web server.  The web server and the end-user now have a persistent session to communicate bidirectionally.

- The end-user requests the URL specified above (broken into URI and Header sections), and relays any cookie and browser header information.

- The web server accepts the input of the request, and goes through a process of routing the request internally, where it matches the domain in the URL domain or Host Header value and any other Headers it processes, and in this case then determines if there are any directory modifications to look for the static file.

- Having determined what the path of the static file is on the local file system, if the file exists, the web server opens the file, reads it, and relays the data into the content section of the HTTP response.  After relaying the contents, it closes the file, creates a successful HTTP status code, and returns the results.  In this case we will assume that HTTP keep-alive is not enabled, and the HTTP server will close the connection afterwards.

- The web server logs the request and successful response, appending to it's access log on the local file system.

- The end-user's web browser will have received the HTTP response, getting the status code and body of the content, and in this case will display the image to the screen.

This is one way that a request event could be processed by a web server.  We can similarly create the model of "the file does not exist", the web server may do something similar, except return a 404 File Not Found static content result.

In the case of a more dynamic system, the web server could proxy the request to an application server, which then makes database calls and performs formatting logic, and then returns a dynamic result instead of a static one.

The importance of Systemic Thinking is that there are no gaps.  Every connection that is required is modeled, and if new connections are required, they are added, and the remaining components need to be updated so that the System remains Internally Consistent.

Internal Consistency is a very important factor in any System, for it to be a properly functioning system, and will be another topic we delve into deeply.  Internal Consistency has similarities to Alignment, where components are aligned with one another for maximum efficiency, but Alignment requires Internal Consistency, where something can be Internally Consistent but not aligned.  In this way Internal Consistency is a super-set of Alignment, in order to be aligned, things must be consistent, but things can be consistent and yet not well-aligned.

Any time a change is made to any part of a Model, the rest of the Model must react accordingly, to stay Internally Consistent.  The initial change may not require any additional changes to remain Internally Consistent, but it might be that every other Component must also be changed to remain Internally Consistent, this depends on the Reality that the Model is modeling, and the intent of the change being made.

2.5.1: Philosophers Knife
-------------------------

One important tool in creating systems is the concept of the "Philosopher's Knife".

This is a virtual knife, meant for cutting ideas into sections.

The most basic way of dividing ideas is to split them in half.  Bifurcation is the cleanest method of division, as everything in split into one of two possibilities, which allows for using binary methods of organization, such as binary trees for creating hierarchy, or quantifying values so that things can be sorted on an comparative axis (ex: smallest to larger, slowest to fastest, etc), or setting binary flags so that set theory and boolean logic can be used (ex: "Is an X?", "Has an X?").

For example, one can say something is "Black or White", and then take any concept and add it into the "Black camp" or the "White camp".  This is a basic process of sub-division with things that appear to be opposites.  In subtractive light frequencies, black is the absences of color, and white is all of the colors.  In additive pigments, black is the combination of all pigments required to absorb all frequencies, and white is the absence of pigments that absorb frequencies, so that the frequencies are refracted and appear to be total spectrum, or white.  

By stating your method for determining the color, and your method for assigning into "black or white" camps, you can create a repeatable, inspectable, qualifiable and quantifiable method for working on data.  You could create a color value from 0 to 255, and anything 0-127 is in the "Black" camp and anything 128-255 is in the "White" camp, and then additional operations could be performed on them.

Being able to divide things in this way is a useful tool, but it is also a primitive inspection of the information, and in fact creates a frame that excludes almost all data.  We all know that "black and white thinking" is simplistic, and the reason is that most of the information (color) is reduced out, when thinking in this way.  And yet, it has utility.  How can we use this utility, without being negatively effected by the loss of information?  This is a primary goal in creating Wisdom, which is how to balance something beneficial or detrimental, depending on how it is used, but through Wisdom of it's usage, the results are beneficial.

As a further example in making the split between "Black and White", the frame of reference created also ignores that fact that black and white are both colors, which means they are very similar to each other, and much less different from each other than say the word "duck", which is an animal.

If we took the sets of "Black, White" and "Duck, Goose", we see that black and white have much more in common with each other than duck and goose.  Because of this, even though in our first example we contrasted black and white as opposites, they are in fact much more similarly related to each other than many other things.

This is both the power and the limitation of the philosophers knife.  It can reveal differences, and it can obfuscate similarities.  How you use it will depend on the results you are looking for, and your skill at applying this technique to create those results.

For our purposes, we are looking at how to use the philosophers knife to sub-divide systems, for the purposes of Systemic Thinking.

The most important element in creating a well-cut concept into a system, is that nothing is left behind.  The use of the philosopher's knife should account for all components and options of a system, and while it is sub-dividing them, they never lose their whole.

Their "whole" is what makes up the "system".  If you lose a part of the system while sub-dividing it, you have not correctly used the philosophers knife.  This will be important when designing your system, implementing it, and troubleshooting it, or in creating a Model to understand an existing system.

Let's first use our previous example of the static HTTP web request.

I used the philosopher's knife on the system of "making HTTP requests from a web server over a network" to come up with 5 elements of the process:

- A communication network (Internet): part of the environment.
- A protocol and environment (TCP/IP on Linux): part of the environment.
- A request handler (web server on TCP port 80): the Input to the black-box.
- A content location (static files on local filesystem): a component of the Output to the black-box.
- A log location (appending results to log file): a Side-Effect of the black-box operation.

I could have sliced this in a different manner, and instead focused on the TCP packet exchange, or I could have cut it so we delved deeper into the end-user's process of getting it's request to the web server (LAN, routing, DNS, TCP handshakes, etc).

I was able to slice this process into the layer's I chose, because I wanted to discuss those elements, and not other elements.  This ability to exclude what information is being inspected, while not losing any of those excluded areas of data in the total picture is the real power of systemic thinking, is the function of the philosopher's knife in this process.

We can take the exact same example process, and re-slice it any way we want, and the events would be the same, but the information we look at, and how we inspect it would be different.  The system has not changed, the actions that occur in reality did not change, the results did not change, the inputs, outputs and side-effects did not change, and yet we are able to look at the problem in a completely different way, and take different lessons and gather different information from it.

2.5.2: Slicing the pie vs aggregation
-------------------------------------

In the last section we covered the importance of slicing with the Philosopher's Knife without losing any information.

One easy way of thinking about this is that you are cutting up a pie with the Philosopher's Knife.

No matter how you slice a pie, the amount of pie has not been reduced, there is only a different number of pieces.

If you cut a piece directly down the middle, creating 2 symmetrical pieces, no pie is lost.  You have 2 pieces that compose the entire pie before slicing.

Similarly if you cut a pie into any configuration, with any number of cuts, whether it is symmetrical, asymmetrical, whether the cuts are vertical, horizontal, diagonal, straight or wavy, the results are the same, in total all the pieces still contain all the original matter of the pie, the difference is only in the distinction of between separate pieces of the pie.

In our philosophical cuts, the structure of the "pie" does not change, unlike a real pie, which deforms with the pressure of cuts, and will turn into a mess after enough slicing.

In our virtual "pies" of information, or systems, we can slice any number of times in any direction, and the information remains the same, but on each side of the cut, we have made a division that can be used logically.  Essentially, the Model of our System is the progression of cuts, and the total set of cuts as it relates to the system.  Each cut is an "axis", which divides along a boolean of "is X" or "is not X" relating to the cut X.

For instance, we can look at an Operating System that runs on PC hardware (like Linux, OS X or Windows), and divide the it into code that runs in "Kernel space" vs code that runs in "User space".  We could call this the "Kernel space cut", to determine "Is Kernel space?" vs "Is not Kernel space?", or we could bifurcate it as "Kernel/User space" to explicitly state the 2 sides, instead of only explicitly stating 1 side, and the other is simply what-isn't-part-of-the-explicitly-stated-side.  If you already know there can only be 2 options, you can use explicitly naming both sides, if you aren't sure there are 2 and only 2 options, then use naming 1 side and leave "everything else" for the other side.

Dividing between Kernel and User space splits all code that is executed by the operating system, they are either executing in Kernel space or User space.  We can take the same system, and make a cut between "firmware" (code that executes from BIOS and other places closer to hardware) and "software", which is executed from RAM on the main CPU.

Whether we have divided by "Kernel vs User" or "Firmware vs Software", nothing about the system has changed, we have simply decided to cut the pie in a different place, and we can then use this division for some sort of useful inspection.

Cuts can be layered on top of each other, like dividing into Firmware/Software, and then dividing Software into Kernel/User space, and could continue to be divided, such as dividing User space into shared library code vs. application local code.  Share library code will be executed by more than one application, and is stored in a .so or .dll type file, and application code will be stored in a program's ELF or EXE formatted binary file.  This type of layered cutting creates a structure like a binary-space partition tree (BSP tree), if you want to model it that way, or can be seen as a list of boolean axes, or could be used in any other way you want to model data if you have a different goal for your visualization.

For purposes of discussion and illustration we can be fairly fluid about our definitions, and decisions on where to slice, because they are throw-away examples, and exist only for as long as they are useful to us.

As we get deeper into the topics of Engineering Axioms and automation, we will see that while this can be used fluidly, the ability to use it deterministically, in a repeatable pattern, across many topics, becomes of paramount importance.

The reason for this is the difference between a comprehensive system (correctly sliced with the Philosopher's Knife), and an aggregated system, which is not built as a complete system is aggregated from components, and is not built using a whole system and "pie-slicing".  The difference is an Aggregated System is built from components, like bricks from the ground up.  As bricks are needed, bricks are laid down, if there is a gap, it can be filled in.  In comparison the Comprehensive System exists in total from the beginning, although it is Virtual as it exists as a concept, it exists in totality, where the concept of the Aggregate System does not exist in totality, and only what we currently know and track of it (with our component-bricks) is tracked or can be said to exist.

The problem with aggregated "systems" is that they not always in jeopardy of becoming not-internally-consistent, and they can never be complete.  Due to being "aggregated" into creation, where one piece is created, and then another piece, and then the two are put together, and then a change is made, and then a new piece is added, you get the result of not having a "complete pie" when it is assembled, as the only pieces that were tracked were those that we happened to work with.  

Aggregated systems have a tendency towards not being internally consistent, and Comprehensive (Slicing the Pie) systems have a tendency towards being internally consistent.  Just because you have a Comprehensive (Slicing the Pie) system, does not mean you cannot create an a situation where it isn't internally consistent, but as it is reviewed and worked on (under the Slicing-The-Pie mechanism), it will be revealed as to where and why an internal-consistency-error was created.  In an aggregated system this is much more difficult, because things are only related to their adjacent neighbors through their connections, and did not come out of a comprehensive system from the beginning.

In fact, I will attempt to prove later on that it is impossible for a system that is aggregated to ever become a complete and comprehensive system, whereas if you always work from the method of "slicing the pie", you will always have a comprehensive system.  The reason for this is their approach.  

The work involved to do both are very similar, and in some cases exactly the same, but the manner of thinking about the elements in them are very different, and yield very different results.

If you think about "comprehensiveness" as "volume", and we think of the "space of this volume" as a rectangle (width and height), then the Aggregation method works by building up from the bottom (height = 0, and up), and works along the width to provide more structure.  

The Comprehensive model starts by utilizing the entire area of the volume, but making subdivisions, say in 4 equal pieces to start, and assigning each sub-section as an element of the Comprehensive whole.  Then those sub-sections are subdivided again, and again, until we start to add in details.  The entirety of the volume will never be filled, as there is an infinite amount of detail that can be applied, but the entire space of the rectangle is being "owned" by some topic, and is being further divided down as we zoom-in to more details.

With the Aggregate model (which is a system, but not in the "Systemic Thinking" sense of the word), only the bottom parts of the space are utilized.  It's doing the same thing, in terms of implementation of the details, but the way the details are mapped to one-another is only through their implementation.  This differs from the Comprehensive model (which uses "system" in the same way the "Systemic Thinking" does), because the relationship for all details is completely mapped into the entire volume, the entire comprehensive structure of thought or description, and the model takes into account "all of the space", even if a given particular part of the space has not yet been implemented.

The Aggregate model does not have the attributes, and so gives a different result, which is not a Comprehensive result, but a "de facto" result.  The Aggregate is "what we did", but does not include planning inside of it's own structure, because it is simply a map of work performed.  The Comprehensive model includes both the entirety of the structure (all things we know of in the system), and where we have performed work to solve problems inside this system-space.

As of 2015, I do not know of any operational environments which work in a manner that is consistent with "slicing the pie", I only know of aggregation environments.  I will explain this assertion as we get more into details, but this puts the use of systemic thinking in an operational environment into a purely "mythical" state at the moment.  Something I hope to change with writing this book, and sometime I hope to pass on as a valid tool for Engineering, and a valid goal where it will help your engineering projects.

Part of the purpose of this book is to provide a path for others to understand these differences, so that paths can be built to allow us to create these comprehensive and complete systems, and to manage them accordingly, to get the benefits which they provide.

We know the benefits and fallbacks of the aggregation system, though without comparing them to another method it is merely the de facto operations of all environments, making it hard to inspect as there is nothing different to compare it to.  

Making a change requires both defining the goals we want to achieve, and the current state of things, so we know what is required to make a change to get closer to our goals.

2.5.3: Systemic Thinking
------------------------

So far we've gone over the general definition of a system, and created some examples, and looked at how to slice components of a system up to leave the system intact, but able to looked at from different perspectives, and to separate out different components.

How does this affect our ability to perform operational duties?  How will it help in automation, and in the life-cycle management of an operational environment?

Firstly, if one cannot understand something in detail for one's self, then it will be difficult to work with that thing efficiently.  I hope I have shown that being able to slice up a topic in any way you would like can produce sub-divisions which allow inspection and description, and which do not change the whole of system, and can be sub-divided further, or sub-divided differently to provide examples to compare and contract with one another, and to inspect their relationships and how work might flow through them.

Once one has an understanding for one's self, then the ability to communicate effectively about the topic becomes a possibility.  If I don't understand a topic thoroughly, I will have a very hard time having a thorough discussion of that topic with someone else, in fact I believe this is impossible to do.  I must have a thorough and comprehensive understanding myself if I wish to be able to communicate with someone else with clarity.  They will have a different understanding than I do, even if we use the same Model descriptions, because we have different experiences and information, but the Model and System view I make and understand myself gives me a map to try to make analogues against when conversing with others.

Through the power of using systems and the Philosopher's Knife, and black-boxing, I can take topics I do not comprehensively understand, and transform them into topics I do comprehensively understand, using a Model I have devised as a mechanism for understanding.

By reducing a system or component to it's Inputs, Outputs and known Side-Effects, I can clearly talk about what is going on as it relates to other systems or components.  

If we can come to an agreement on terms and what the Inputs, Outputs and Side-Effects are for the given systems/components we are talking about, we have a much higher likelihood of coming to consensus on what we are talking about, and will be less likely to be talking about completely different things, while we are trying to communicate about a problem, or a solution, or whatever.

Additionally, once we can create a system out of any environment and events, we can begin to Model that system so that we can come up with procedures on what we should do under different circumstances.

For instance, in our web request and logging examples, we have determined that without log rotation we will in time fill up available storage, and fail to be able to take more requests (or at least, log their results), and so we are sure to have failures on any active systems where this is the case.

From this we can create a policy that requires all services to have log rotation or truncating configured for any software before it is put into active service.  We can go over the results we will achieve without this, and determine that are not the results that we want, and come up with a test for whether this is enacted on a given server to ensure that we have done this work, and have protected ourselves from this deterministic outcome.

This is the type of leverage that these tools provide, and when we get into the details of automating an entire operational environment, through it's life-cycles, with change management and ensuring that all things are internally consistent, and well-aligned, to accomplish our goals, we will find that without these tools for clear and consistent "breaking things apart" and "putting them back together again" without losing any information, we will not be able to get comprehensive coverage without being able to communicate at this level of detail.

The short-comings of aggregated systems, versus comprehensive systemic systems is not yet clear, but as we define our terms more concretely, and begin to use them to deconstruct on operational environment, and then put it back together again, while keeping track of everything, we will see how aggregated systems are incapable of performing this task, while whole-systems always lean-towards an accurate representation, if they are viewed with accuracy.

That isn't circular logic, is it simply the result of "Garbage In-Garbage Out".  If one can't view a topic accurately, one cannot expect to perform work to meet goals accurately.

2.5.4: Inputs, Outputs and Side-Effects: A Virtual Mechanism
------------------------------------------------------------

I talk about the qualities of "Inputs, Outputs and Side-Effects" enough that I've decided to label them as something that can be discussed directly.

I will call something that takes Inputs, gives Outputs, and produces Side-Effects a "Universal Machine", because it is a type of machine (performs work, mechanistically), and can be applied in any situation.  It may be a deterministic machine or non-deterministic (introduces randomness, or other factors which cause different Outputs or Side-Effects with the same Inputs).

A Universal Machine, by our definition here, can take any inputs and return any outputs, and create any side-effects, whether they are Real or Virtual, it doesn't matter.  The important aspect is that there is a definition of the interface, so that the understanding can be brought about from just looking at Inputs, Outputs and Side-Effects.

Additionally, how you define a Universal Machine can change based on your goals.  If you are trying to track information as input, and information as output, and yet track real physical changes as side-effects, this is one way of defining a machine.  In a different way, for the same situation, you could define physical inputs, and physical outputs, and information-based side-effects (data that has changed).  Any combination is usable.  In the Operations world, generally we are dealing with informational inputs, informational outputs and informational side-effects, as physical changes are usually outside of our area of immediate concerns.

A Universal Machine can be defined as you want it, and can be applied to anything, like a system, and a Universal Machine is a System, but it is a specific type of System that is defined as having Inputs, Outputs and Side-Effects.  While any System might be able to be viewed as a Universal Machine, many times when we think of a system we are not thinking of it as a machine, so it helps to differentiate about when we are and when we are not thinking in terms of mechanical inputs, outputs and side-effects.

Any process, physical or non-physical (informational, virtual, etc), can be defined by it's Inputs, Outputs and Side-Effects, so this creates an interface we can use at any time, for any reason, and we can reason about Universal Machines based on their interfaces, separate from the work that they actually perform.

The linkages between Universal Machines will follow the same rules, irregardless of the type of Inputs, Outputs and Side-Effects being worked on.  By making a distinct type of unit we can refer to by the label Universal Machine, we can always drop into the method of talking about a component. or service, or physical machine, or any type of thing, and how it operates in a chain or process of events.

{{ note: Should I create an acronym for this?  I/O/SE? IOSE?  Might be useful. }}

2.6: Terminology
----------------

Congratulations!  You've made it to the second beginning of the book, where we go over the definitions of terminology we will be using.

I thought it was important to give a bunch of background on what we were going to talk about before we got to the definitions, because my terminology definitions may be quite different than how you already think of these terms, as you may have already begun to see.

For the purposes of reading this book, please accept my definitions as I will use them for the purpose of making things clear.  The definitions must be kept congruous to differentiate things that are frequently conflated.  If it helps you can mentally append "Geoff is saying he means X when he says Y in this book", if the terminologies conflict too much with your existing use of the words.  I'm making a specific point about this, as I often have an internal feeling of rejecting an authors information based on their use of words from being different than how I would use them.  It's often a useful method to determine if the information is worth listening to, but in the case of a longer-term effort like reading a mentorship-oriented book, can cause you to miss out on crucial information.

The important part of this is that you gain insight into my perspectives, as I will be using those descriptions of my perspectives to build up a detailed map of how to inspect an environment, how to design and compose an environment, how to implement it, how to automate it, how to troubleshoot it, how to perform maintenance and life-cycle changes to it, how to document it, describe it to other people, etc.

This is all too much to do with just anyone's terminology, and the only terminology that will be able to consistently deliver these results inside of this book will be my own.  So try to accept all of these for the tools that they are in getting to these goals, and not as universal definitions that should be written into dictionaries, or compared against them.

I will be using the capitalization of proper nouns with these special terms, so that they are clearly my definition, for the purpose of this book, and not meant as the general term.  The only time this may be confusing is when the word starts the beginning of a sentence, but I hope context will keep that clear.

2.6.1: Data: data
-----------------

In the virtual world, Data is king.

I will support this assertion throughout this entire work, as it has become a central tenet in my thinking about how to do any sort of digital engineering.

As I asserted in {{ section_ff17d94c0d49aab3e372e47b64b96ea7 }}, Data is an un-real thing.  It is virtual.  It does not have physical properties, and does not exist in the physical world.

Electrons and magnetic forces exist, which we use to encode data into storage and processing mediums, but the Data itself does not physically exist.

This is an important fundamental to understand, and more important for the purpose of learning from this book, to accept as the usage under which I will giving examples and explaining things.

Data is symbolic and descriptive.  It can be used in any way, to accomplish any purpose at which the data has usefulness.

You can use Data to accomplish things it was not intended.  For instance I could take the textual data inside a Linux /etc/passwd file and turn that into a musical score, by converting the characters and terms into frequencies, and by playing it.

It would likely sound incoherent, and not be considered musical, but that is the power of Data.  It can be used as you see fit.

Data resides in a Data Source, which could be anything, such as: files, database tables and rows, returned by networked services, etc.

Data can be stored in many formats, and these formats can dramatically change the way the data is stored, and yet if it is not corrupted, the data can still function in the same way.

Consider that data stored in a CSV (Comma-Separated Value) file and data stored in a YAML or JSON format look very different, and yet both can be loaded, parsed, and used as if they were stored in the same format.

Data could be formatted to fit inside a relational database, so that it is spread into tables and fields, and looks nothing like a CSV file, and yet after querying the database I can get the data back in the same format which I could parse from a CSV file.

This shows the dynamic nature of Data, while still providing us with consistent information that can be used by humans or Logic.

2.6.2: Logic: code
------------------

I'm going to try to constrain myself to using the capitalized (proper noun) "Logic" any time I am referring any of the following things:

- Code
- Programming
- Scripts
- Decision trees
- Finite State Machine processes
- etc

I will also use these other terms in their normal meanings throughout the book, but I will refer to Logic when I am combining what is created in order to manage things that are done programmatically.

It's good that our industry has many terms for things, as it makes them specific, but I will using the roll-up term, Logic, in order to simplify and generalize what we are talking about.

One simple definition could be:

- Logic is Data that is executable.

In this definition, Logic is a sub-set of Data.

This could be executable because it is in a native format an Operating System can load and execute (ex: ELF, EXE, etc), or via an interpreter (ex: Python, Ruby, PHP, Bash), or via a Virtual Machine executor (ex: Java, .NET/Mono).

Logic is used when one wants to operate on data in a digital environment.  With Logic we will change the data, create new data, validate data, and perform side-effect type actions where we do things like copy data to different locations, remove it, create directories, start and stop services, as well as anything else we could do manually.

Essentially Logic is the way we take action through digital means, where we would otherwise take actions manually.

Of course, in a digital environment, all actions eventually require Logic.

If I am in a command-line shell, and I run a command to create a directory, I have manually initiated Logic to perform this work.

If I write logic to inspect a data source, and then to create directories based on that data in that source, then I do not need to manually initiate the Logic to create the directory.  There will be some kind of timed period (ex: cron jobs) or event (ex: monitoring initiated execution) that will initiate the Logic.

As we went over in {{ section_ff17d94c0d49aab3e372e47b64b96ea7 }}, Logic is un-real or virtual.  It is not a physical thing, with physical properties.  It does not exist in the physical world at a given location or orientation.

One can say that that bits that describe the Logic do reside on a physical storage medium (rotating disk, SSD, RAM, etc), but I am separating these physical attributes from the Logic itself, which could be anywhere, and in a given physical device, it will almost always reside in multiple locations, both on storage, and in RAM and perhaps in a CPU cache, and perhaps partially in CPU registers.

I will end up breaking down many things to Logic layers and Data layers, and how Logic works on Data, and how Data is the stable foundation of Logic.  In my perspective, this is a reversal of how many people see the relationship between Logic and Data, but I will make a case for why Data is the core and Logic is the shell.

To make the assertion as briefly as I can:

1. Data is what you know at a given time.  This is useful forever.  It could be useful hundreds of years for now, for the same reasons it is for us today (using it to configure things), or strictly for historical or analytical purposes.  Data has essentially no "death" or time where it becomes invalid or unusable, as a general resource.  

Not to say Data cannot be corrupted, or be invalid to our purposes, but it remains valid as a source of information even if it is corrupted (though perhaps not actionable for our immediate use, and degraded utility and trustworthiness due to corruption).

Even corrupt data is potentially usable to give us some information (statistics about what was not corrupted), but corrupt Code/Logic should not be executed, unless it is an sealed-off environment, as it may perform destructive actions.

2. Logic is the codification of goals.  What we want to occur is processed through Logic.  Because of this, Logic has a number of environmental factors that work in some conditions, but there are many states where Logic cannot be used, except if it is seen as "Data" and is no longer executable.

Logic requires a valid environment to run on.  Logic created to run on Linux will not run on Windows, or OS X, without being re-compiled (and perhaps "ported"), or being somehow universally compiled.

Logic expects certain environmental requirements to exist.  It may expect to run in a certain directory structure, which contains certain files, formatted a certain way, and containing specifically formatted data.

Logic could require access to network services which must exist and be reachable and authenticatable for it to work properly.

Logic has dependencies.  It runs on a given "platform", and does not run if the supported "platform" is not available as it's execution environment.

Data needs a place to reside (ex: database, file system, etc), but it does not require a specific environment, it could be stored in a YAML format, JSON format, in a relational database, a flat file with comma or colon separation, as raw blocks on a device, or any type of format or storage system at all.

The methods to access the Data can change, but the Data itself will remain the same.

In order for Logic to run in a different environment, it is likely going to need changes.  Some programming languages offer cross platform execution, via being run by an interpreter or virtual machine executor which was natively compiled to the target operating system.

However, there are still many places that Logic may not be able to work cross-platform without changes, such as moving from Linux to Windows there is a difference in how Windows access some storage, because it uses "Drive Letters" as device targets, Unix-style operating systems use a single directory hierarchy, and user's home directories are in completely different places, and looked up in different ways.

Other changes may be system files it expects to find in certain places, or required libraries that may not be installed, or may be an incompatible version.

These are lower-level types of problems that Logic has, and why, unless it is running in a hardware emulator, Logic written decades ago generally cannot be executed properly on modern hardware and modern operating systems.  

There are some exceptions to this, such as code that ran on very old versions of Windows, and has had fixes installed throughout Windows versions up until the modern times to allow this code to still work.  These are the minority of cases though.

A more likely scenario is that the organizational goals have changed.

Goals change frequently, and so requirements change frequently, and Logic is codification of requirements.  Once you have different goals, it is very unlikely that the code that worked for the previous goals will still work with the new goals.  This happens every time new commits are made to a source code repository, the actions the old code performed are now changes, and new actions happen.  The old-code's action's results are no longer desired, because we have upgraded them to the new-code's action's results.  The old-code is deprecated and should no longer be run, that Logic is expired.

The conditions for when the same Logic will give correct results once you goals have changed is when that Logic is being used as a "tool" or "utility", in which case it operates on data to perform it's actions.  The Logic performs a primitive function, and so it can escape being outdated as soon as your goals change, because of the limited nature of it's actions, and it's intent being a general purpose tool, rather than a specific tool to implement your goals.

This accounts for the long-life span of Unix-style environments, which are historically largely made up of software that performs generalized operations against a set of data.  That data might resides in a file, a database or be given by user input on the command-line, piping through input streams, or through a series of prompts.  

In these "tool" types of Logic, it is the data that tells the Logic how to achieve a goal, and so again the Data gains primacy over the Logic in being the key element.  The "tool" Logic only exists to transform the Data.

For our purposes, in automating an operational environment, we will be extending this "tool" type processing greatly, so that we create a large pool of interconnected data, and then create Logic that works against this data to achieve the goals we want.

Like the Unix-style environment that allows so much control and flexibility, we will create a layer on top of current Operating Systems, which allows the accomplishment of goals with a minimum amount of changes to Logic, as the Logic is driven by the Data.

2.6.3: Rules: policies about how you do stuff
---------------------------------------------

For the purpose of this book, I'm going to use a term I don't usually use in real life, which is "Rules".

In this case I will define Rules to mean the way we do things, encoded into Logic and Data.

I will use this to separate out digital Rules from policies and procedures that departments and organizations use to determine how people do things.

This could be seen in the sense of "Rule Processing Systems", or something similar, where Rules are constraints or requirements in how Logic will operate.

And the Rules are specified either directly in the Logic (hard-coded rules), or in Data.

Rules encoded in Logic will require more effort to change, and are not able to be changed automatically, unless you are generating the code.  Generated code is more of the side of the spectrum of Data than Logic, because Logic is generally created by humans.

In the case of generated Logic, it will be generated from Logic created by humans, and is a type of template that has data populated into it, or loops of generated chunks with data populated into them.

2.6.4: Distributed: dealing with N nodes
----------------------------------------

You may have used the word "distributed" before, such as in "distributed systems".

My meaning will be very similar to this usage, but I will use it a little more generally to mean any time you need to work across many nodes of something.

For instance having to control 200 web servers will be a Distributed service of web servers.

This usage stems from a single web server being able to do the same thing as 200 web servers (configured in the same manner), but the "load" is "distributed" across the 200 web servers, making this a distributed network service.

The reason for being very general in this usage is that it provides a comparison point between single-unit processing system and a multi-unit processing system, which is the core of the problem and benefit: there are more things doing the thing.

As I will cover in more detail later on, there are 3 cases you should account for in operations:

- Zero instances of something.  You do not do this thing.  In some cases this is simply something you do not require, but in the more sophisticated case, this is work you are still accomplishing, but in a manner that does not need an instance of anything running to accomplish the goal, it is taken care of by an efficiency gain.  In either case, it is important to know that "not having something" is a potential state.

- One instance of something.  This is when you have one thing that you use; it is the centralization of a service.  There may still be a pair of machines (Master/Slave) supporting this one-thing, and there may be more than a pair, but if there is logically a "single instance" of the thing, then it is a "one instance" though the instance may be made up of many pieces to create the single-whole.

- Infinite instances of something.  As soon as you move beyond "one instance" (or one-thing), you move into the realm of many-things.  If you think you can move to "just two" or "just three" you are not taking into account all of history which shows continual sub-division and growth in all things that are not "shutting down".  "infinite instances" may currently be at a count of "2", but in order to handle the growth that will eventually come, it should be implemented as an N-instance, or infinite instance system.

Differentiating between "instances" and "counts of things" can be a little tricky, and seem subjective, but it is because it is fulfilling a goal of understanding whether we have duplication of "service providers", or not.  This is all in the context of "distributed systems", if that helps to make this language introspection easier to understand.

These differences can be seen in the phase:

"0, 1, Infinity.  There is no 2."

Make this an internal meme for yourself, and watch as things start to make more sense in terms of problems with scaling.  When a number larger than 1-instance is introduced, you will eventually see that number grow, and sub-divide into different domains.

Having a 1-instance system is incredibly difficult.  Pressures will continually be applied to grow into an N-instance system, and it will take work and perseverance to keep a 1-instance system at 1-instance.

0-instance systems, when not just the identity of "we don't do that here", are created from efficiencies in automation.  This is when a 1-instance or N-instance system has been replaced in such a way that the work does not need to specifically occur, and yet the goals are still achieved.  If this sounds a lot like what I referred to as "removing Classes of Work", it is because it is exactly that.

I will cover this concept in full detail later on, because it is critical to understanding how scaling works in practice, but takes a bit more background before accomplishing it can be discussed.

2.6.5: Real/Virtual.  Strict definitions.
-----------------------------------------

I won't go through the explanation that I made in {{ section_ff17d94c0d49aab3e372e47b64b96ea7 }} again here, as I think we covered the differences between what I meant by real and un-real, or virtual there.

I'll just say that like other terms meant for this book, I will be using Real and Virtual as proper nouns to describe things I mean to be having physical properties as Real, and things that do not have physical properties are Virtual.

If this seems vague, please review {{ section_ff17d94c0d49aab3e372e47b64b96ea7 }} again, as the specific use of these terms for the purposes of this book is important for understanding what I'm trying to convey.

2.6.5.1: Be clear about the differences:  Physical (Real), Logical (Virtual), Data (Virtual)
--------------------------------------------------------------------------------------------

{{ todo: ... }}

Since I think we have a clear working definition for the terms Real and Virtual, we start to do some comparisons between them and see what other things are different.

Since they have very different properties, as they are about as different as anything can be, that means that those different properties should have different advantages and disadvantages when looking at them from different perspectives.

2.6.5.1.1: Reality: The Physical
--------------------------------

The first important thing to know about the difference between Real and Virtual things is that you cannot know everything about a Real thing.

Determine what the state of a Real thing is is essentially impossible, but we can have approximations that are good enough.

Why is it impossible to know that "true state" of a real thing?  Because it's state varies with every atom, and collectively all the atoms of a physical thing are too numerous and beyond inspecting in many dimensions.

This is not taking this too far either, it is simply being clear about what is possible, and what is not.

So, if we can't know everything, then what is possible, and what are those limitations?

Let's take something fairly simple for example, such as temperature.  What temperature is a physical device, we will say a 1U 19" rack server?

Well, that depends on where you are measuring it from.  Modern servers can have dozens of temperature sensors throughout their chassis, and those temperature sensors will approximate the temperature fairly accurately for part of the device.

We could measure the each CPU socket temperature, and the temperature near the power supply, and the fans, and then we can approximate from these or list them, but there remains many places we are not even directly measuring.

It happens that this is not necessarily important for our purposes, but it is important to understand and accept that this data is simply not available to us, and we have sensors in place to detect some aspects of it.

Other aspects we may not have any sensors for.  For instance, mobile devices often come with accelerometers, which will detect movement of the devices.  Rack servers do not currently come with these sensors, and for a fairly reasonable reason, as they are not in demand.

But this is one type of data that we cannot collect about this server.  It could be that the amount of vibration the servers are going through could end up causing problems over large numbers of servers, and by doing correlative analysis on part failures with vibrations, and by determining where the vibrations were worse, we could contact our data center's staff and see if they could fix the problem, as it may be an undetected problem on their part.

This is a completely theoretical example, but it illustrates that there are things we know, but not completely (temperature), and there are things we do not know at all about Real things.

2.6.5.1.2: Virtual: The Un-Real
-------------------------------

In the last section we learned that there are things we cannot know, or know with full accuracy about Real things.  Their very nature means that they are not fully knowable, but we can know enough about them to make use of them effectively, and have a long history of doing so.

How do Virtual things align on this same spectrum of "knowability"?

Some Virtual things can be completely known.  Other Virtual things remain unknowable.

We can use the examples we used in a previous chapter.

Let's look at a variable that we assign:

X = 5

Here, I have made X to be equal to 5.  Can we know everything about this Virtual thing?

Yes, we can.

We can inspect this in any way we like, and know everything to know about it.  We can compare it to different numbers:  X < 6, X > 4, X == 10, and see if it is similar to them.  

Any operation we wish to make, we can perform and know the full extent of what there is to know about this Data.

Now, let's look at a Virtual thing that is not fully knowable, we will look at the word and symbol of "idea".

We can take the word "idea" and trace it's language roots, and compare it to other languages, and find common usage of it in popular literature, and we can ask people what it means, and in all of these things we will gain information.

But, we will never know everything there is to know about the word and symbol of "idea" because it is not a concrete thing.  It has subjectivity and flexibility, and can be used in different ways in different circumstances.

The same is true for many things.  So we have a class of Virtual things about which anything can be completely known, and another class of Virtual things about which only some things can be known.

Let's simplify this into two more terms:  Knowable Virtual things, and Unknowable Virtual things.

We could call this "Knowable Virtual Data", but since Data is a subset of Virtual, and there exists other things that are virtual, and may be completely Knowable, that do not meet the same definition as Data, we will use the label "Knowable Virtual" and then can append anything onto it afterwards, like Data, to describe what exactly the Knowlable Virtual thing is.

Let's create a spectrum for these labels:

Knowable Virtual thing <---> Unknowable Virtual thing

We're going to build a little forest of terms and spectrums (or axes) over the course of the book, because once we have clear terms like this, we can use them in different ways than if they were still more vague, and less specific.  Once they are specific, they become tools, which we can use to help us perform work.

We create a language tool when we give terms specific properties, which allow us to clearly divide information, such as Knowable Virtual Data vs. Unknowable Virtual Data.  We have at least 1 property between these information topics that we can use in any algorithm as something that is clearly understood: knowability.

Over time we will build up a toolset of these, so that we can communicate about incredibly complicated topics, and reason about them efficiently and clearly.

As an exercise, try to come up with some of your own terms.  Once you have an understanding of how to create terms for yourself, you can use this to create things you understand completely, because you made up the terms you are working with.

If you can, great, write them down and add more to that list as you think of them.  Over time, you will start your own set of terminology in which you can reason with, having more understanding of it than my terminology, which I have created.  Like I'm doing here, you will have to define your terms for other people, or translate your terms into language they already understand, but it is important that you have a clear understanding for yourself, which creating your own terms helps with.

If you can't think of any now, that's not a problem, but if any come to mind in the future, write them down, and over time more and more may start to come to you.  This is a process that becomes easier and more useful over time, as you get used to it.

2.6.5.1.2.1: However, between Data and Logic is a huge gap, as Data is "perfectly" understandable, while Logic is not, due to Halting Problems and all other things CS-academia knows and describes very well.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Another Unknowable Virtual thing is Logic.

Logic, as we defined earlier, is an all-emcompassing term for anything to do with software or decisions, or scripts or other methods of manipulating data, executing statements, etc.

One of the famous problems of computer science is the Halting Problem.

This problem is essentially that is impossible to know if a program is every going to stop executing once it starts.  There is a lot of information about this problem out there, so we will just leave it with that description and realize that Logic has an Unknowable Virtual element to it.

However, Logic also has many Knowable Virtual elements to it, because as in our example of "X = 5", this is a statement that can be made in Logic.

Additionally, just like in our example we can use the Logic itself to inspect this, or we can externally inspect the Logic using a debugger, and we can verify the data, and it is Knowable Virtual Data.

So, while Logic contains some properties that are Unknowable (the halting problem being one example), it also contains properties that are Knowable, and the Unknowable does not stop us or hinder us in any way from gaining full access to the Knowable.  

This puts Logic in a murky place on a spectrum of Knowable to Unknowable, but that's OK!

What we need to do in this instance is slice up what Logic is, and look at each of the components on the spectrum, and we will have a correct view into it.  Whenever you have a compound problem, you can slice it into simpler components to better understand it.

So, that would look like:

- Logic: Will it ever stop running?  On the Unknowable part of the spectrum.
- Logic: Variables and other values?  On the Knowable part of the spectrum.

I leave off calling them directly Knowable and Unknowable, because Logic can be tricky, and there can be tricky things done inside logic, and perhaps in some circumstances this means that variables are not completely knowable, and there might be circumstances where we have a high confidence that a program will halt, like this pseudo-code:

{{ start_code }}
int main()
{
  return 1;
}
{{ end_code }}

We can be reasonably sure that if this program compiles, and there are not problems with dynamically linked libraries, and there are not somehow crazy macros in the white space or brackets, that this program will eventually stop running.

This tells us another Knowable property of Logic, which is that it is very complex, and that it's meanings can be obscured.

Take for example this Python code snippet which uses a Decorator.  It's OK if you don't know Python or aren't familiar with Decorators, because it's just an example and I'll explain my meaning of it.

{{ start_code }}
@HelloWorldDecorator
def HelloWorldFunction():
    return 'Hello World!'
{{ end_code }}

If the "@HelloWorldDecorator" wasn't there, this would read like a beginning Hello World! program, as when you call the HelloWorldFunction() function, and it returns the string "Hello World!".

However, there is a Decorator to this function call "HelloWorldDecorator", which modifies the behavior.  The decorator code may live in another file, so it may not be obvious what is happening when you simply look at the code.  You assume it's basically going to return "Hello World!".

Let's look at the decorator code I have created:

{{ start_code }}
# Decorator
def HelloWorldDecorator(function_reference):
    def DecoratorInside():
        # Call the Function we are wrapping
        intitial_result = function_reference()
        
        return intitial_result.replace('Hello', 'Goodbye')
    
    return DecoratorInside
{{ end_code }}

The decorator code creates the required wrapper for the functions, as that is what decorators do in Python, and it calls the function reference, but instead of simply returning the result, as if we had called the code without a decorator, it modifies the result.

It replaces the string "Hello" with "Goodbye", so we get the very different result of the "Goodbye World!" string being returned, changing our peppy introductory function into something much darker.

This melodramatic example shows that we can see something that looks very clear in code, and yet something that does not necessarily looks like it will change the result we clearly see, in fact, does change that result.

This is another aspect of Logic's being on the Unknowable side of the spectrum, due to it's ability to contain very high complexity.

2.6.5.1.2.2: This difference also tells us why Data is more important than Logic, because Data is more trustworthy than Logic.  When making changes to data, the changes are straight-forward to understand, when making changes to Logic, the side-effects (unintended consequences) can be far-reaching and completely not understandable, and frequently enough are this way.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now that we have established that collectively, Virtual Data, which I will just call Data, since it is always Virtual, is Knowable.

And we have established that collectively Logic is Unknowable, even though components of it may be knowable, we can use this information to set up a hierarchy, which we can use to build more robust engineering solutions.

If Data is comprehensively Knowable, and Logic is comprehensively Unknowable, then we should base our actions on our Data, and treat that as the supreme truth.  Our Logic is not less important because of this, as it serves the same role as it would if Logic was King, and reigned supreme over Data.  One thing must have precedence over the other, because in real-world prioritization things cannot be equal.  There is always a preference, and it is usually by a wide-margin, due to the limitation of resources in the pursuit of our goals.

Knowing that we can treat Data as the most important thing in our operational environment means that we will always first focus on the data being correct, and then secondarily we will look at how the Logic interacts with the Data, with a careful watch that the Logic does not do anything to or with the Data that would cause us problems.

Of course, you don't have to have any of this kind of analysis to know that you should not corrupt your data with your code, but this is the path I have taken to understanding where to place priorities, and how to approach working, and they have served me well.  I hope to prove after we have gotten through this introductory phase, into the details phase, and finally into going over implementation, how these fundamentals are truly critical to building large, robust, resilient, controllable, manageable operational automation environments.

Without all of these details, all the adjectives I just used to describe what we will build may still be applied, but they may not be true, and we may not really get those effects.  Through using well defined fundamentals, we can begin to bring this assurance in.  This is an important part of what Knowability gives us.

2.6.5.1.2.2.1: Changes to data, that meets constraints, will not harm other data, but can harm Logic that acts on the data (results of Logic, rather)
-----------------------------------------------------------------------------------------------------------------------------------------------------

When working with Data, is it required that certain constraints are met.  This is normal database 101 stuff.  If you have a relationship between 2 tables, the the primary key of Table A is referenced in Table B, and then you change that primary key in Table A, but do not update all external references to it (such as in Table B), then you will have created an inconsistency.

There are methods for forcing this to not be allowed in many database software's schema configuration, using constraints and foreign keys, etc.

In an Operational Automation environment it is likely that the data sets will stay small enough that you can work with these constraints enabled (without performance problems), and the changes are important enough to deal with the performance hit the constraints provide anyway.  So, I recommend using software constraints when possible, and letting the database software manage enforcement of constraints to keep your operational configuration data consistent.

If you find yourself in a place where constraints are causing a real performance problem, and are not working, I suggest only turning off the constraints that are the problem points, and leaving the rest of them enabled.

For the areas where data constraints are turned off, you must be especially careful when making changes to this data not to lose any of the referential integrity that the constraints would have provided, with your own changes via Logic, or in unfortunate times when you manually update the database (which you should try to never, ever do).

Another Knowable thing about Data, is that if you have these constraints active, then you can Know that the data is correctly configured, and it's referential integrity is consistent.

There are some operations, such as dumping data and mass-importing it, that can cause these checks to be turned off, so be careful when you do this to do everything that is involved at the same time (ex: dump all tables that reference each other at the same time), to ensure that you have not imported things into an inconsistent state.

We've now covered that Data can have an additional area of Knowability.  How does this relate to Logic?

Well, it turns out this is another area where Logic provides a fundamental weakness, and in a way that is Unknowable.

You can have perfectly consistent and correct Data, with all constraints active, and have Logic that works perfectly well with all of the current data.

And then you can make a change to that Data, which does not violate any of the comprehensive consistency validation tests, and yet afterwards the Logic fails against the Data.  How?

Logic is not actually tied to Data in that same way that Data can be tied to itself (through constraints).  In a database, let's use an abstract general SQL database with transactions for this case, we can insert a valid row into database table, and all the constraint tests are made in the transactional commit process, and the data is stored correctly.

When the Logic next tries to access this data, it finds the new table row, and it goes about it's normal operational logic, which has always worked before, but this time the data it receives is not something the Logic accounted for.

For instance, you have a field that is an unsigned integer in the database software, so it goes from 0 to 4 billion, but the Logic expects that this data is in the range of 0 to 100.

If the data entered is actually 5000, and the Logic expected it to never be more than 100, then the Logic will do something incorrect, perhaps making something that shouldn't be 50 times larger, such as memory allocations of a Java Virtual Machine, which might fail and cause a service to not start on the next attempt.

Whose problem is this, Data or Logic?

It is a shared problem with between the two, because the Data contains valid data based off the database software constraint system (0 to 4 billion), and the the Logic is only handling 0 to 100, and so a failure has been entered between the two, even though the Data was correctly inserted into the database, under the database's constraint system.

There are many ways to approach this problem.  Databases frequently have code that you can put into the database to execute at certain times (ie. user defined constraints), which could validate the values and enforce only numbers 0-100 are put in them.

There are some problems with this, you will have probably tied yourself to this database platform for a very long time, whether you want to be or not, because after all of that Logic is put into the database to validate the Data, it would take a large effort to re-create it all correctly in another database software's methods, and those methods may not be fully compatible, in that you can't do everything in the target database that you could do in the original database.

That is a manageable problem, however, as it deals with timescales of years, and is possibly worth of the cost-benefit tradeoff.

However, there is another problem is that now you are putting Logic into your Data.  We know that Data is Knowable, and Logic is Unknowable, and when you put an Unknowable into your Knowable, the result is that you end up with an Unknowable.

We have just transformed our safe-space of Data into an un-safe space, because now we have custom Logic in there as well.  So we do not have anywhere that is just Data.

This is a huge problem as we will never be able to be assured that the Data we are accessing is going to be accessed correctly.  

To take our "X=5" type example, if we have a field "X" in a database table, and we have Logic running in that database, it is possible that as we test and modify that "X" field, the Logic will be invoked, and it could change the results.

With this being the case, we can no longer trust that we set "X=5" and then we test "X > 4" (X is greater than 4), and we receive a positive.

The Logic may have silently changed X to 4, because it had a constraint that we did or didn't know about at some point, and now we do 2 steps in a row, where we assume success is guaranteed, and we end up with failure.

This is a large problem.  

Another issue that we deal with is that writing Logic for databases is not as manageable over time as writing Logic in other platforms, such as directly for execution or interpretation in an operating system.  That is because database's purposes are to serve data, and so they do not get "best of breed" software development environments.

There are many more examples I can give on how you can have consistent Data, but inconsistencies between the Logic and Data.  The end result of all of these is that you must simply be very cautious when creating your Logic, and provide as many safe guards as is warranted by the needs of your organization to provide that the Logic works cleanly with the Data.

There are many techniques for this that we will cover once we get to implementation.

2.6.6: Knowability
------------------

I didn't know this before I just looked it up, but Knowability is already a word in dictionaries, so there is not a lot of reason to cover it in depth.

We've already been using it quite a lot, but I thought it would make sense to shortly define it.

Knowability is a spectrum of how well you can know something, in full, at all levels.  It needs to be extreme knowledge like our "X=5" example, where we know absolutely everything about it.

Any ambiguity or aspects that remain not-perfectly-knowable need to count against it being on the extreme side of Knowability, and more towards the side of Unknowability.

To set up the spectrum, it looks like this:

Unknowable  <--->  Knowable

2.6.7: Class of Work
--------------------

We briefly defined Class of Work in the beginning of the book, but let's take a slightly deeper look at what it means.

Initially I just said it was "anything that is done", and this is true but perhaps "work" work suffice to say that, and everyone would understand.  However, there is more depth we can gain from looking at it deeper.

I initially used the example of automating the DNS zone file updating.  If you aren't familiar with DNS zone files, they are text files look like this:

{{ example_dns_zone_file }}

One aspect of manual workflow generally goes:

- A new host is created, and needs a name matched to it's IP address (an address "A" record)

- Someone goes to the server that hosts the DNS Master files (the host people use to make edits on, and where the changes will be disseminated)

- They add the line with the hostname fragment, and the "A" for address record, and the IP address

- They update the serial number of the zone file (so the DNS software knows the file has been changed)

- They test the file with the DNS software's configuration file validation

- If the test passes, they reload the DNS zone file into the server

- Then they tell the Slave DNS servers (other machines that reference this Master machine's DNS service to get records), and tell them to do a zone transfer.  This might also be configured to happen automatically on the Zone file being reloaded, through the Master DNS server's software


These steps might take a person 10-15 minutes to perform, on an individual basis, and slightly longer to implement for larger changes, or in larger environments where there are more tests or more templating.

Sometimes it is a problem that people just forget to do one of the steps, but, since the new host wont have a DNS name, it will only be able to reference them by IP address, so usually this problem is quickly remedied.

A larger problem is that people can type things incorrectly, and while the validation tests find some problems, they will not find correctly formatted zone or configuration files, which have incorrect data in them.

If a line that used to exist was removed, then immediately afterward reloading services that referred to that previously-existing DNS name will start to fail, as the name no longer exists or resolves.

These problems are usually caught quickly, as things will fail and alert, if monitoring is set up properly, but there was just an outage, and revenue may have been lost, or other negative consequences for an organization.

Humans making manual entry mistakes are simply unavoidable.  As the population of humans doing manual work increases, and the amount of work each human does increases, so will the amount of failures.  This is compounded with any special conditions, where there is a standard process, but special cases exist which must be manually maintained either without automated testing, or with insufficient testing.

Some failures only show up when multiple mistakes occur, so the original set-up problem may have been occurring for days, weeks or months before, but the secondary mistake triggers the initial mistake, making it harder to troubleshoot as the recent change doesn't seem to impact the part that is now broken (but did).

The "delayed failure" may not have even been a mistake at all, and after reverting that change and inspecting the configuration, it might be found that it looks correct, so it is put back in, and the failure occurs again because the error requires two places to cause the failure.

This is a component of Alignment, which I mentioned in the beginning of the book, but we haven't referenced in a while.

The Alignment in question for our original "DNS zone entry is removed" is this:

- A service, say a web server, references a database by DNS name, and is live and working

- A person makes a change to the Zone file, removing the database name, but leaving the zone file in a valid state in terms of validation

- The zone file is loaded and replicated, and the web server cannot reach the database.  An outage has begun.

What was the Alignment here?

The Alignment was that the web server required the DNS server to have the name of the database server, so that it could make a connection to it.  This is 1 layer of Alignment, as the web server needed the DNS server (the requirement) to contact the DB server (the goal).

This is a very simple case of Alignment, but it makes the point for an initial example, which is that without Alignment, things either do not work, or do not work efficiently.  In the above case, things stopped working completely with the removal of the DNS entry.

Efficiency is a metric that has to do with "functioning, but not as well as we would like, or could be", and so is a more complex topic than something that does not function, which is fairly clear cut.

We'll be getting very deep into the Alignment of efficiency soon.

2.6.8: Data Source
------------------

Since we'll be talking about Data quite a bit, I will be referring to any mechanism that stores Data as a "Data Source".

This could be a database, a YAML file, a variable in a JavaScript web page that came from a JSON RPC request, it doesn't matter.  There is a location that stores data, and we interact with it to get data and store the data.

The Data Source may be persistent, or it may be temporary (such as Javascript data in a web page).  It may be transactionally safe, or unsafe to update simultaneously.  These are secondary properties, as the primary property of a Data Source is access to the data.

Some qualities of a Data Source:

- Access to data.  Get it, set it.  This is mandatory, all others are optional.

- Constraints on the structure of the data (such as not being able to insert arbitrary fields).  This would be a strict "schema" (schematic), as opposed to a "document" style which allows any type of modifications in the values of a record.

- Constraints on the value of the data that is put into specific fields in the data.  For instance, in a relational database a field in table may be of type "integer" and will not allow alphabet characters, special characters, or real numbers (decimal precision) to be inserted.

- Persistence: So that the data is saved, and if the power is turned off to the system storing the data, when the machine restarts the data will still be available.  There may be corruption here, unless the Data Source also offers a Consistency guarantee.  Persistence simply means that things can be discontinuous (losing power is one method to lose continuity of the service), but the data will still exist.

- Consistency: Ensures that the data does not become corrupted in any failure situations.  These situations might be the program being terminated un-cleanly, and it might use something like a journal to keep track of on-going changes, and will replay this journal on start-up to ensure that recently changed data is the same as in the journal.  

To be safe, the journal is written to and flushed to disk before the "changes are made" in the database, so if anything the internal database data is consistent with the previous changes, and only new journal entries need to be applied.

There are different Consistency guarantees, and while Consistency means "will not become corrupted", there are usually many methods with which data could become corrupted, but the Consistency provisions attempt to solve those problems through various Logical steps.

- Transactions: Multiple changes, such as in different tables, or multiple rows in the same table, can be applied all-at-once, in an "atomic" fashion, which means that it "cannot be split further" (Atomicity), and being the smallest-type-of-action, it is guaranteed to either not-have-started, or finished completely, before another action takes place.  

Transactional changes are made sequentially, and cannot interrupt each other.  Furthermore they verify the consistency of the entire exchange, and not simply each statement, which allows more precise validation of referential integrity as well as being able to make changes that would be constraint violations if done one-at-a-time, but which are consistent when done together in a transaction.

- Replication: This allows copies to be made of the data to at least 1 other instance of the Data Source implementation, for example a SQL server could incrementally copy it's journal file from itself to another machine, which then applies the journal.  If the original machine goes down, the replication target machine will have an update-to-date version of the database, up to the latest journal entry it received.

Replication might be after-the-fact replication, so a transaction completes on a Master DB, and then the Slave DB will get the same transaction request moments later, after the latest bytes of the journal file has been copied over to the Slave, and the replication agent re-runs the remote transaction statements on the local database.

Replication might also be in lock-step with the Master, so a server that gets a write request will complete it on itself, and then wait for 1 or more other replication servers, based on a "quorum" number.  If the quorum is two (2), then at least 2 servers must have this transaction committed before the client requesting the transaction is told that it was successful.  This method is much slower in terms of returning a result to a user, but is safer in that the information is persisted on multiple server's storage, in case a corruption-level failure happens on the original server.

There are many other properties to Data Sources, so this is not meant to be an exhaustive list, but a brief coverage of some elements we can associate with the label Data Source, which may or may not exist in a given implementation you may use.

Some Data Source implementations offer features that are in opposition to some of the above, and those feature sets are also useful, since they provide different benefits and weaknesses to some of the features I have mentioned.  The right tool for every job, and all that.

{{ todo__make_more_of_these_qualities_lists_for_other_terms_and_things }}

2.6.9: Operational Environments
-------------------------------

Any place where any operating is going on is an "operational environment".  This could be on your desk, or in your closet, or in a data center, or across a number of data centers across the world.  The size and location of the operational environments is not what defines an Operational Environment.

What defines an Operational Environment is the purpose you wish to achieve with it.

Often it can be useful to think of an Operational Environment as a Security Zone.  You allow certain people to make certain requests in each security zone.

For example, on your laptop or desktop machines, you probably only allow yourself, and perhaps your Corporate IT department, to execute software or make configuration changes to the single machine in these environments.  We don't want people on the internet connecting to our personal machines, so we will want to restrict any external connections.

If we move to a Quality Assurance (QA) environment, we may allow all QA engineers to make data changes, and software pushes to these machines, but we only allow certain operations staff to have administrative access, and make system-level changes, so all of the systems stay in a similar state.  We generally don't want any external access to a QA environment, but we might allow whitelisted access for some partner companies who either provide us services, or who are doing integration with your developers.

Looking at a Production Environment, we would want to have much more auditing, and restrictive access of who could login to servers and make changes.  We also all do allow external access from our customers, who could be anyone located anywhere, and may allow un-authenticated (guest) access to our services.

Operational Environments, and their corresponding view as a Security Zone, is an important consideration any time you are performing Operational work.  Where are you doing this work?  What are the goals?  What are the rules and restrictions?  Who gets access, and what are they allowed to do?  

How do we ensure all of this stays consistent?  How do we maintain this, make changes, and automate regularly occurring processes?  What about monitoring and alerting on things we care about?

All of these will change every time you change what Operational Environment classification you are in.

2.6.9.1: Production Environment
-------------------------------

The most important environment for any given system is the "Production" environment.  This is the environment in which the organization makes their revenue (ex: online service), or interfaces with their customers (ex: informational service), or creates their product (ex: manufacturing).  "Production" comes from "product", as in a "production line" which in an assembly line that produces an end-good product, it has the meaning of the "end of the line" in terms of an organization producing a good or service, which will then be distributed.

The Production Environment, which I will mostly just be calling "Production", is the place that the critical operations of your organization takes place.

This might be a data center that has many peered network circuits, in which you receive internet traffic and generate revenue.

Or, it could be a server farm in your corporate offices, in which processing occurs, which is critical for the functioning of your organization.

Or, it could be in a cloud or managed hosting environment, in which you mostly manage through a browser application.

It doesn't matter what exactly the circumstances of your "Production" are, you should be aware of what it is, and how it is treated different than other areas of your organization.

Things in Production should be the most important things, and not intermingled with devices or services which are not of the same critical importance.  Sometimes sharing of environmental space will have to occur, but this should be minimized, and remedied once it is possible to do so.

The Production environment should have the highest levels of security, where only authorized personnel are allowed to access the server instances, and every login and preferably every command issued is logged, for auditing purposes.

This follows the "AAA" process of: Authenticate, Authorize, Audit.

In brief:

- Authentication is determining who someone is.

- Authorization is determining if they are allowed to do what they are trying to do.

- Auditing is logging everything that happens, so that it can be reviewed.


There is a fourth "A" that be added {{ todo_forgot_what_this_is_tempoarily_but_i_wrote_about_it_years_ago }}

2.6.9.2: Staging Environment
----------------------------

.......

2.6.9.3: QA Environment
-----------------------

2.6.9.4: Performance Bench Testing Environment
----------------------------------------------

2.6.9.5: Corporate Environment
------------------------------

2.6.10: Server
--------------

2.6.11: Device or Machine or Nodes
----------------------------------

2.6.12: Humans
--------------

It feels a bit weird when I say or write "Humans", as it's strangely impersonalizing to everyone, I feel.  However, it is conveniently clear to differentiate not only from "Not Human", or "Logic Based" or "Software" or whatever, but also clear in the sense that I am not speaking casually about people, but specifically about the type of effects that Humans cause.

We generalize about "people" all the time, different groups of them, to have any sort of discussion.  Sentences can only carry so much information in them at any given time, because words only have so much meaning, and a word is composed of syllables, and those take time to write or say, and they have to be done sequentially: the syllables cannot be written or said simultaneously to be more efficient, and so generalizing or summarization is required.

Without summarization and generalization, we would spend so much time getting to the point, by being maximally explicit in every detail, much in the way I am doing right now, that we would just not get to the point, and all communication would cease to function.

Shouldn't there be a spectrum for this?  Let's make one:

Generalization  <----->  Specificity

Now we have an axis on which we can slide a variable across, to be more or less specific, and it can be tuned in the way we want it, for every circumstance that is possible.

In addition to this, we can add in another topic we recently covered, such as "Atomicity".

We can be extremely specific in our discussion of Atomicity, or we can be extremely General, or somewhere in between, in the spectrum, along the axis.  I will use this method of multiple examples mixed together to provide a richer tapestry for these ideas to be expressed in, as the book goes on.  These are tools for communicating more deeply; they are another spectrum or axis, which our goals can be applied against.

Let's just combine some right now, and make a new communication tool.  We just discussed "Atomicity" as a topic, on the spectrum/axis of Generalization <--> Specificity.  Let's combine the Atomicity spectrum and the Specificity spectrum together, and create a topic based on the two dimensional coordinate system that those two axes create.

Atomicity:  Not Atomic <---> Atomic
Specificity:  General <---> Specific

I ended up writing these "Right to Left" in terms of the subject being in a full-state, or an empty-state, but they could just as easily be written "Left to Right" (in reverse order), if it is more convenient for the problem at hand to see them in that way.  This process of ordering things as needed for the current problem is another tool that can be applied, and which has properties that can be evaluated.  For the sake of keeping up a fluid pacing for this book, I can't go into detail on each of these things as they arrive (even though I would like to: enhance, enhance, enhance).

Now that we have these two axes, which we could use in the Cartesian coordinate system, we can plot a point on it, and then create text that describes that point.  This is a sort of generative tool, in which one can use one's knowledge of an information space to generate any amount of specific data.

If you are familiar with any sort of procedural generation, this yields the same kind of effect that Perlin or Simplex Noise allowed in procedural generation, in that because the pattern remained consistent whether viewed from "from away" or "up close".  Procedurally generated content (images, models, clouds, cities, whatever) could scale to "infinite" detail, either looking at the "big picture" or with a "magnifying glass".

In the same way, this generative tool of mapping axes to an information space, and then using your own understanding of that space to extrapolate what text would describe that point in those axes' space.  

This is actually the exact same technique I am using to write this book, as I have broken up the information space I am trying to cover into both a linear (sequential) flow (chapters), and then assigning various variables (in the forms of words in the topics) to create each chapter's text.

Let's do one of these now:

For the Atomicity value, let's say on a scale of 1.0 (Atomic) to 0.0 (Not Atomic), we have an Atomicity value of 0.25, or not very Atomic, but having some Atomic characteristics.  

Then let's say on the Specificity scale of 1.0 (Specific) to 0.0 (General), we have an Specificity value of 0.75, or fairly specific.

Because we need to be specific, I am going to make up some details about the Atomicity of the thing in question, which I will use a database for:

{{ start_quote }}
This database provides limited atomic transactions.  Transactions are accepted, and written into a journal file, which is flushed to disk periodically, but not in sync with the transaction being considered successfully completed, for performance.  The means that in certain circumstances a transaction may be partially written onto the journal file disk, and in these cases recent data writes can be lost.
{{ end_quote }}

So, this terrible database accepts things as Transactions, and journals the transactions, but it doesn't flush the journal as part of the transaction success criteria to make it Atomic, so you might have partial transactions written on the disk.  This is actually always potentially true, since a power failure could cause a partial transfer, in some hardware configurations, but the difference is that a successful result would already be returned to the client, even though the write will later fail to complete.

In practice, modern controllers accept a queue of IO requests, and can do some optimizations on them, depending on the construction of the storage medium (what type of disk/etc), and so flushing merely pushes more things onto this queue, and if you cant put more things into the queue, you have already maxed out your throughput in this configuration.  Unless the queue has a battery backup to complete operations in case of primary power failure, than power failure will always potentially cause writes to fail that you think were accepted.  Unless you force your OS to not complete writes until the storage device has ensured it was written (which has a performance penalty).

In this case, it is possible that the queue can take more total IO requests if they are batched, and for a given workload and hardware specification, you may need to do this, understanding the performance to consistency trade offs.  Moving on.


What if we had a Specific value of 0.0, instead of 0.75?

In this case we would be 100% Generic, but we still have to say something relevant so we might summarize:

{{ start_quote }}
This database handles requests in Transactions, and writes them to a journal file, but flushes only periodically, so Transactions may be lost on power failure.
{{ end_quote }}

This gets across the idea of what's going on, but is very brief about it.

What if we had a Specific value of 1.0, instead of 0.75?

We would have to specify the entire code, every line, and it would need to be idealistically correct (or actual implementation), and we would have to specify all environment requirements.  Why?  Because we are 100% Specificity at 1.0.  This means absolutely everything must be specified, if this spectrum or axis is to have real meaning.

Taking this into account, maybe my example using 0.75 for that level of specificity isn't nearly detailed or specific enough, but on first introduction 0.75 sounds like "pretty specific", where 0.5 sounds "half specific, half vague", and I wanted to be detailed enough to get real implementation points across, but also not too long for pacing.  Only after thinking about what 100% Specificity would really mean does 0.75 seem too high for our previous example.

This is yet another tool for performing evaluations, by making one example, and rating it, and then making another (or a series of others) example, and rating those, and then going back and re-rating the first examples, then the second again, and finally creating examples of the most extreme situation you can imagine at both ends of the spectrum (being 0.0 and 1.0), and then re-evaluating the middle ones again.  This is a method for getting a numerical sense of an information space.

So, these are 2 more tools we can use in the future to discuss problems in a clear and precise manner.  Trying to get as close as we can to 1.0 specificity, without losing the ability to make progress.

But where we're we?  Oh, yes!  Humans!

When we are having conversations like the one we are sort-of currently involved in, being specific by saying "Humans" instead of any other word allows us to understand we are using technical jargon, and we mean technical things.

This allows us to move away from our standard social communication style, and into a technical communication style, to discuss technical points at a detailed level.

So while it is weird to type and say, it has a benefit for clarity, which is an important attribute of Engineering.

Also, it will make it easier to relate to your future AI overlords, which will be helpful.  ("The humans are revolting!", "I know, right?")

2.6.13: Philosophy
------------------

If you didn't know, there are 2 Greek roots in the word "Philosophy".

These roots are "love" and "wisdom", so Philosophy is the "love of wisdom".

I look at Wisdom and Intelligence as different axes.

Wisdom is gained from experience, and has to do with the breadth and depth of insight into topics, and being able to make judgements that detail what might be favorable and unfavorable outcomes, and why.

Intelligence I look at in very different perspective, which is "making an action that yields beneficial results for all parties involved."

This is not a common definition of Intelligence, but it has a rigid definition, and comes from a brilliant article written by Carlo M. Cipolla, a professor of Economics at UC Berkeley, and is one of the greatest things I have ever read, and quite literally changed my life.  I saw the world differently after having ingested it, and am much better for it.

The article is entitled "The Basic Laws of Human Stupidity", and while it's title and subject matter focus on "Stupidity" (anti-Intelligence), it's real function for me was to qualitatively and quantitatively define what intelligence is.  He puts it on a 2D graph, and charts it, and allows for pinpointing different kinds of Intelligent and Anti-Intelligent actions.  Try not to let the negative sounding name cause you to avoid this information, it is a very important set of thoughts he has encoded there-in.

http://www.amazon.com/The-Basic-Laws-Human-Stupidity-ebook/dp/B005ZX622C

http://harmful.cat-v.org/people/basic-laws-of-human-stupidity/

{{ todo__request_rights_to_reprint_article_in_my_book_from_family }}

These start to illustrate the differences between Intelligence and Wisdom, to me, and will hopefully (over the course of the material) become clearer and useful to you as well.

So Philosophy is the "love of wisdom", and I love wisdom, so I take it for that.  I orient myself on "Applied Philosophy", which is using Philosophy in a way in which that I can achieve results (internally and externally) and not merely as a way to win arguments at dinner parties, or making witty comments that end with "Do you want fries with that?".

Another purpose of Philosophy is to be a structure around the question, "Why?"

In much of Engineering we focus on "How?":

- How do I use this library or software?
- How was this software written?
- How do I get the result I want?

Philosophy is more angled like:

- Why should I use this library instead of that other library?  How are they different?  What will be the effect of using the one, versus the other?  If one of them is better suited for my current situation, but the other may be better suited to a future situation of mine, when would be the time to start switching over?  Is it worth doing?  Should we even be doing any of this at all?

- Why was the software written in this way?  How was the developer trying to allow me to solve problems with it?  How can I best use this software to work with the way the developer was trying to enable me to solve a problem?  Between the different ways I could do this work, what are the different effects they will cause, and which of those do I think will be most beneficial for me?

- Why am I doing this?  What are my goals?  How can I define them precisely?  Is my entire team in agreement with this, as an intention?  Are we able to communicate effectively, ensuring that we understand each other and can work together efficiently?  How would we know if this is true, and we are succeeding?  How can we measure that success, and compare it to the goals we wanted to achieve before we started?

Philosophy is about depth, and the ability to inspect things from different angles, and while it may appear on the surface (and is sometimes explicitly stated) that it is trying to "define the way things are", in actuality the Philosophical inspection never ends (Infinitely Recursive in All Dimensions), and so it does not have the ability to ever define things "the way they are", because it can't stop defining things.

This is a "Machine" in which we can know it will never halt.  There is no final exit or return from Philosophy, it is a rabbit hole that never ends, and goes as deep as you are willing to look, and the detail expands to meet any closer inspection.  What is true from one perspective, or frame of values, is false from another.  It's flexibility to reframe data is infinite.

{{ todo: Cleanup needed immediately below. }}

This is do to "Why?"  Why?  Why?  Why?  Why?  ...

I think Philosophy has a bad-wrap these days, and I hope to show, if only in a thin slice, that there is a way to use Philosophical ideas in a practical way to add clarity and improved performance in your life and work.

Transitioning back to Wisdom (Note to self: Awesome segue!):

One simple way to see Wisdom is "good ideas".

To keep things simple and say, "I love good ideas", is why I love and heavily utilitize methods of philosophy.  I make use of different kinds of philosophies in my own ways, I take their definitions and interpret them in my own meanings, and I mix and match pieces wherever I need to, as configurable tools to be used in understanding the problem I have at hand, and manipulating them into what I what I want them to become, to get the results I want.

This is what philosophy is an element of, for me, and how I will be using it, in this book.

2.7: The Philosophy of Pragmatism
---------------------------------

Pragmatism is a formally written up philosophy, and you can read more in-depth about it on the Internet or various books.

For the purpose of this book, we'll be using it in it's core form, in my usage, which is:

"Pragmatism is when you only evaluate an action based on the effects, and nothing else."

"Effects" are different than "results", because results is more about what you wanted to achieve, and whether you felt you achieved that thing or not.

"Effects" are more general, and deal with all things that come from an action.  The change of state from before to after.  How are things different?  How did they change?  What are the effects of this change?

There can be a lot of confusion with the word "pragmatism", and it is often used interchangeably with "practical", and sometimes conflated with "common knowledge", but it does not mean these things, and for the purpose of this book we will be strictly avoided any conflation with "practical".

"Practical" is a very loose term that means efficient in both resources and results, it gives you "good enough" results, with an acceptable amount of resource usage.

This has nothing to do with Pragmatism, as Pragmatism has no concern for the amount of resources that were used, or if the burden was terrible, or whether it was convenient.  These things may show up in the "effects" of an action, such as the amount of resources impacted is part of the effect, but "practical" ties these things together as being important in the concept, whereas with Pragmatism, all of the effects are simply data and can be evaluated as to whether those are desirable effects, or not.

This also covers another topic that causes confusion, which is "side-effects", and although this is useful in language to denote things that occurred that may not have been part of the "main" or "center" (hence, "side"), in truth all things are simply effects.  Whether they are in the "center" or the "side" is based on your perspective, and is likely to cause partial blindness in evaluation when they are separated, instead of being seen as a single set of effects.  Some effects you intended, some effects you did not intend, but they are all equally effects of the action.

Grouping everything into only one single pool of "effects" is the better way to do this, when you want to prioritize for accuracy and clarity, because you are not trying to push anything to the "side-lines" and are seeing all effects as being caused by your action, and thus will evaluate that action's effects more comprehensively than separating effects into "desired and undesired" categories, and primarily looking at the "desired" category when performing post-action evaluations.

**What are we excluding when we only look at effects?**

Initially, we are excluding our value judgements, our goals, our history, culture, feelings, wants and desires, and anything else, so that we can focus on dealing with "what changed?" or "what will change?", and detailing these effects (changes) qualitatively and quantitatively, where possible for each.

This allows us to go beyond whatever limitations we might be currently bound by, in terms of our perspective or awareness.  If we don't apply our bias to the situation before we have enumerated and started to evaluate all of the effects, we are likely to find additional effects from the one's inherent to our goals.

In terms of getting coverage like "all of something", we are obviously talking about potentially a lot of data and too much to grasp at any time, and this is where Systemic Thinking and Slicing the Pie come into effect.  We can box these effects into groups, to be inspected in more detail as needed, or viewed from farther away with less detail, or less Specificity.

Again, this ability to scale in or out from details, is an important skill that needs to be developed and applied to get a good grasp on what is going on in any given situation.  Without this, one is going to be "stuck" with the view from one's current perspective, which may be inconsistent through different circumstances, giving one inconsistent results even when it seems like one's perspective is remaining the same.  One can't see the same things under different environments, because there are different things to see.  One's perspective should always adapt to the problem at hand, and the environment and resources involved.

I like to give examples with every topic I introduce, but I don't think it's the right time to go into a deeper example on this topic, so we will just touch the surface of an example we will soon delve into deeper.

**How can we use Pragmatism to get better results?**

For instance, one thing that we are concerned about greatly in Production Operations is "up-time", which is the Availability of our services.

How do we get the "best" (most) up-time?  Well, the most important thing is actually a "negative", which is "don't go down".  However, "not going down" takes "all the things" working all the time, even when some things fail.  This is obviously a very complicated endeavor to try to improve.

By using Pragmatism, and only focusing on the "effects" of doing one thing, versus another thing, we can evaluate that method with the highest signal-to-noise ratio, so that we are spending more time thinking of the most-relevant things, and are actively trying to avoid things that may be distractions.

Knowing that one thing that causes down-time events is "Humans making changes" we can say that we want to optimize for making more changes through automation, and less changes through direct Human manual (by hand) efforts.

Since Logic is able to be written so that it runs deterministically (if done "properly"), then this Determinism is an attribute which helps us improve our up-time, by removing the non-determinism of manual Human changes.

We can evaluate these based on the effects of what happens when Logic updates a DNS Zone file 10000 times, versus having Humans update a DNS Zone file 10000 times.  From these cumulative effects, we can see that the Humans will make more mistakes in the act of updating the zone file, than the Logic will, and thus the effect of Human edits are more errors, which reduce our up-time.

There is a lot more detail that could go into this analysis, as with anything, but this is getting our feet on the path of how to analyze things by their effects, trying to strip out anything that is not an effect of the process.

Chapter 3: Engineering Philosophy and Methodology in Operations
===============================================================


Alright!  The book is really starting now!



We have cleared the hurdles of disclaimers, how-to-read, introductions, and terminology.  We can now get into the real substance of of why we are both here:  The Engineering of Operations.






3.1: What is Engineering?
-------------------------

More definitions?  Well, we are never going to stop defining and re-defining things to our particular circumstances, as we simply can't front load all the thinking, and sometimes we will need to be more specific.  At least we are now into the real content, and no longer strictly in the peripherals.

Engineering, to me, is:

**"The efficient use of resources applied in an environment, to yield a desired effect."**

Generic and vague?  You bet!  But, also it can be used to insert in any specifics into the general terms to get at a more specific definition, like so:

"The efficient use of time, personnel, money and physical devices (servers, etc) applied into a Production Operations environment, to yield high up-time, acceptable performance, and scalable management."

That's starting to be more clear, and more specific to our current topic than the more general answer, but I see all of Engineering as a similar set of options.

Whether Engineering is applied to building a bridge, a canal, a sky scraper, baking a cake, or managing a production operations environment, it needs to be:

+ Efficient (because being inefficient might mean it is not able to be completed, or "fails")
+ It has certain resources (universally time, almost always money, and also almost always people
+ It might be soil conditions, and logistics of getting materials from Point A to Point B, or whatever)
+ It has specifically desired effects, such as a set of interlocking canal segments of the Panama Canal, or a sky-scraper buildings ability to stay erect under it's own enormous weight and support and movement of the soil, or the digital and physical equivalents in server operations.

Regardless of the topic or domain, the initial approach to engineering a problem is the same.  Determine the environment and resources in play, determine the requirements of meeting our goal, determine the actions that can be taken to fulfill those requirements, create a plan to perform the actions, evaluate the plan's methods of implementation, risks, etc, implement the plan, evaluate the implementation, whether we met our success criteria, and update the documentation based on the new state of the environment and resources.

3.1.1: A brief interlude on the Strengths and Weaknesses of Metaphors
---------------------------------------------------------------------

There is a trade-off on Metaphors, and it has to do with expert-knowledge and accuracy.

Metaphors, in my opinion, are most useful when are you not an expert on the subject of the metaphor, or defer your expertise to see the metaphorical example being used as tool for communication.

If I give the example of:

 "Production Operations must deal with the problems given by information alignment and physical hardware management, similar to how building a bridge must deal with the soil, water, wind and temperatures around a bridge, and the materials used to construct the bridge."

This metaphor, or simile in this case, is most useful if the audience are not experts at building bridges.  As an expert in building a bridge, they may have a very different take on what it takes to build a bridge, and what the issues are, and they may validly complain about my use of analogy between information and soil.

This is where metaphors are weak, because they are meant to give "a comparative idea" by taking us out of the details we are currently immersed in, and putting us into a "very loose" frame in another topic which we can discuss as non-experts.  In a sense this "levels the playing field", as neither party is an expert at bridge building, so we can use that to illustrate our points of view without getting into details where we do have expertise, but our definitions and values may not be Aligned and need to be discussed.

Because of this, it may be useful to change metaphorical topics if someone introduces details about the metaphor which derail the intention of using a metaphor.  This can be referred to as "over-extending the metaphor".

If you find yourself disagreeing with a particular metaphorical usage, try to re-frame the metaphor yourself into a different topic, preferably one you do not have expert knowledge in, and see if you can gain more insight into it that way instead.  

This can also be a useful tool in determining if you understood someone correctly, as you can re-frame what you understand of their point with a different metaphorical topic, allowing them to re-map what they meant to your new metaphor, and if they are agree, you are both likely thinking of very similar things.  Going back and forth like this, when there is still mis-alignment, choosing new metaphorical topics, or changing the reference of the metaphor, can allow a complex topic to be worked through in a shorter period of time than going to full-fundamental-definitions and working up from there.

The "Expert's Curse" is a real thing, and doesn't just ruin movie plots ("We are 10 digits into hacking the mainframe password, but they are using 49-bit encryption, so it will take two more hours.  You need it done in 10 minutes?  We'll make it happen."), but also can ruin the intention of any type of alternative explanation, which is trying to expand on an idea in a hand-wavy-kind-of-way.

This is an attempt to get you to use more information than what is being provided, which you already internally know, instead of explicitly providing all the information.  People have amazing inherent skills at filling in this information, and while this works best in spoken conversations (say, where you could finish the other person's sentence), metaphors are an attempt to do that explicitly by providing a non-related but comparable reference.

The goal of communication is the exchange of ideas, and it is important to always return to this goal, s we can remove anti-goals, such as competition, or "Being Right", or any other anti-goals that get in the way of communicating in a fashion that allows us to achieve our True Goals.

3.2: Difference between Application and Operational Logic
---------------------------------------------------------

Is there a difference between Logic that is written for Operations automation and Logic that is written for non-Operations?

In my opinion, there is, and it is a big difference.  It doesn't need to exist, but it does exist, and they are not mildly different, but extremely different, at present ({{ CURRENT_YEAR }}).

I see this changing more in the future, as distributed programming environments not only become normal, as they are are now, but that we start to get generational levels of experience in the field.  Generation Levels of Experience is required because there are many lessons to be learned, and then summarized, and then classified, and then come up with procedures for handling, and then generationally iterate on all of this, and this work has barely begun.

I will call non-Operational Logic "Application Logic", even though it may not strictly fit your definition of what an Application is, since it changes under different contexts.  If we we're to put this on an axis, we could call it:

Application Logic  <----->  Operational Logic

For instance, in a Production web serving environment, you frequently have "Application Servers" which might run Java Tomcat, JBoss, or Ruby on Rails, or a Python, or other Logic required for producing dynamic web content.

These would be "Application Logic" in this terminology, as I'm using it.

**What is the difference between Application Logic and Operational Logic?**

The main difference is Resiliency and Minimal Dependencies, and these have a number of sub-parts.  Some examples:

- Application Logic requires that the environment that it runs in be configured, or the Logic will fail, and often will fall non-gracefully.  How gracefully it fails generally has to do with how "mature" the Logic is, in terms of it's life cycle.

Example: An application server is started without a required configuration file in a specific directory, so the application server program exits with a status code of 127 and output to STDERR "Cannot open file: /path/to/file".  This is reasonable for an Application server, because it needs to be completely and correctly configured for it to return the correct results to a client.

- Operational Logic is built to support infrastructure, with the knowledge that the infrastructure components are going to fail, and the Operational Logic needs to not only recognize the failures, but needs to continue to work in whatever ways are still available.  

Example: A operational software is written which will execute remote code on hosts, for the purposes of managing Application state.  The remote programs which are executed will modify the Application's state, so that clients will receive different information after the state change.  If the operational software cannot update the Application, perhaps because a file is missing (similar to the Application Logic example above), the Operational Logic cannot simply exit with an error code and message.  It cannot complete it's task correctly, but instead must continue to run, and create a local and remote log of the failure, with any additional environmental data that is required to help troubleshoot this problem, and then proper staff must be notified of this failure, and potentially other servers must be updated accordingly (rolled back, or different update), to account for the failure to update this Application state.

Don't misunderstand me and construe that I am criticizing Application Logic or their developers, and praising Operational Logic or their developers; they each have different goals, and so will produce works that have different results because of this.

The differences between Application and Operational Logic are due to differences in priorities and responsibilities.

Operational Logic is responsible for:

- Infrastructure configuration and on-going maintenance
- Configuring Application services and maintenance assistance
- Monitoring and notification of Operational and Application state
- Solving operational failures

Applications are made to provide end-users with:

- Correct and timely results, for a given Application

Application Logic has an expectation that the operational environment is working correctly, and so error detection and handling is typically rudimentary, and output and results are intended for Application experts.  This is a natural prioritization, and not an incorrect one.  Only organization that have grown large enough that the long-tail problems are causing them noticeable impact should attempt to prioritize making Application Logic to be more robust, like Operational Logic, though Application Logic design can take many lessons from Operational Logic design for very cheap or equivalent cost.

As an example, say there are a pair of relational databases in a Master/Slave configuration, and the Master node fails, because of the priorities for Application Logic, generally the application will just fail until the Master/Slave designators are updated to promote the Slave to Master (updated as moving a floating IP address or DNS name or IP record change, or from another directory-style service).

There are some good reasons why Application Logic currently behaves this way.  The first is that it takes extra Logic to determine what should happen if the primary database server goes away, and this will be (very short term, "several minutes, or under an hour") taken care of by the Operations team, through manual intervention or automation.  This allows the Application developers to focus on revenue oriented features, while the Operations team deals with the relatively rare occasions when there is a fail-over event.  This model becomes less desirable as businesses scale up, but is the normal model for smaller or newer businesses, even though it has obvious deficiencies.

Some classes of databases have a multi-node approach from the beginning, to make these types of events less frequent, since a server can go down, but others will be up, and the Application can talk to any of them.  These databases still have failure cases though, and so the results can end up being the same depending on the type of failure, in terms of non-Availability due to database failures.

Part of the "extra Logic" is that Applications are meant to serve end-users, and the time put into making this extra resiliency is often prioritized to go into making additional or improved features.  Whether you agree or disagree that this should be the priority, it often is the priority, and it serves us well to accept Reality, and work within it's confines.  If we want to change this, we need to change the priorities by showing more value given with a different priority.  This is difficult, but possible.  Choose your battles based on when you can win, and when winning is worth it.

Additional to the Logic required to handle failures, is that Application code needs to be very stable for-it's-own-purposes, and adding in this kind of Logic means that during failures more cases may be found that could be handled, which means more changes to the Logic surrounding database access, which means more change/churn, and this leads to more potential bugs.  Specifically the kind of bugs that have data access requests failing, which is something no one wants.  This doesn't mean that better Logic shouldn't be written for database access, but it does need to be written very well, and with an Operational understanding, especially around the matrix of failure cases.  Using a slicing-the-pie methodology for handling errors is an important tool for not missing any of the potential failure cases.

While I think with better education, and better base-libraries we can solve these problems and Application Logic can be more like Operational Logic in handling failures, or in fact leverage the same Logic, so that they are working hand-in-hand, I am making this point because this is not currently standard, and has never been historically standard anywhere that I am aware of.

Another thing that Operational Logic needs to do, is to simply have more information about the operational environment.  Seems like common sense, but since we are building from the foundations, it is necessary to state the details.  Without meta information about the environment, Operational Logic will not be able to make the same kind of decisions that a Human performing Manual changes would have access to.

As we get into what it takes to construct Operational Logic the brief description I have given here will be born out by many more details and along many more axes, which will give better insight into  how these things are different, but for now it is sufficient that we can see that Application and Operational Logic are indeed different things.

3.2.1: Many applications and services.  One Operational environment
-------------------------------------------------------------------

Another difference between Operational Logic and Application Logic has to do with the nature of their environments.

In a given organization there is generally only one "Production Environment".  It may span many data centers, and there may be regional data center teams to support the physical side of the operations environment, but it generally by classified and worked on as a single environment.

There are organizations who break these up, but they are frequently either regulated businesses, or ancient, or have some other external reason for running segmented Production Environments.  In general, companies, even very large ones with the largest Production server collections, only have one Production Environment (which may contain many services and security zones).

This means that in an entire Product Environment is being managed in a single manner:

- There is one way to update Production DNS.
- There is one way to provision new servers.
- There is one way to fail over from a faulty server to a working server, for a given service.
- There is one way to handle authentication and authorization for user and role account access.
- There is one way to centralize log collection.
- There is one way to monitor and alert on logs.
- There may be one way to software releases.  (Actually, this could be on a product by product basis)


Each of these "one way" methods may contain many sub-methods, such as you may actually have several monitoring packages, but collectively they make up the "one way", and generally things are put into one of them, versus any others, unless multiple coverage is desired.

By this "one way" concept, I don't mean to be naive and really limit it to "one thing", that is why there is "one way to" and not "one thing that does".  However many methods of doing something (as legacy implementations will stick around for a long time, and sometimes there is intra-team competition for creating solutions) may combine into "the way we do things", and is meant to keep growing (although it might in practice).

The thing about "one way to do it" systems that are different than "lots of different environments, that do it their own way", which is the comparison I'm trying to make, is that in a one-way-to-do-it system is that you don't want to introduce competing services.

It is more efficient to configure, manage and have life-cycle support if we have limited the amount of ways we do things.  This is a goal for us, in a Production Environment, but we may be forced to fracture things due to time or other resource or environmental restrictions (laws, business goals, technical limitations, etc).

In terms of creating Application Logic, it is easy to separate components of the Application or separate applications that may work in tandem or sequence, or may be linked through a common Data Source, through a messaging queue, RPC (Remote Procedure Call), or other data transference mechanism.

There are many ways to do it, but the point is that you can split up personnel, or Logic, to work on different things, and their work can be isolated from each other, only connecting at certain points to do data exchanges. 

This could be generalized to always be true, but again, the point Im making is the difference between one thing and another, not in their similarities. 

The Operational equivalent needs to be more tightly integrated, because it is trying to support a one-way-to-do-it system, and where things are not one-way, it would often be better if they were.  

So it is a Goal of an Operational system to have one-way-to-do-it, for efficiency, and it is a Goal of an Application system to have many ways to do many specific tasks, so that personnel can be split up into separate teams and given specific goals for those teams.  

This may seem wrong to you if you are coming from the Application side of things as "re-use" and "modularity" and all the tenets of Software Development seem to contradict what I am saying, but I am referring to the scale and degrees of this, and am saying that in Operational Logic, these must be significantly more extreme than in Application Logic.  This is because Operational Logic supports the infrastructure in which Application Logic runs, so Operational Logic must be "more basic", "more fundamental", "more fault-tolerant", "more infrastructure-aware", than it's Application Logic sibling.

The Operational team, in contrast to the Non-Operational software development department, has more generalized goals, that take into account the entire Production Environment, and are more concerned about:

- Total availability of all services in the Production Environment
- Manageability and life-cycle maintenance efficiency
- Performance of the entire system, with a priority on bottle-necks
- Not introducing problems into the environment, and prioritizing solving ones that currently exist

Again, we could align these in terms of how they are similar, and we will find that they are mostly similar, but there is a difference between Operational Logic and Application Logic, and in this circumstance we want to understand the differences more than the similarities, as we are dividing the two subjects for inspection.

I will not spend much more time on Application Logic, as there is much writing about that in non-Operational literature that covers the current understanding of how to do that, and that is not the focus for Operational Engineers.

3.2.1.1: Making more dependencies.
----------------------------------

Now that I've established there are two different things, with different qualities, Operational Logic and Application Logic, let's get into what goals Operational Logic should have:

- Operation Logic should try to minimize external dependencies, especially networked dependencies.

If we know things are going to fail, and we are writing Logic to handle them in cases where they have failed, then we know the infrastructure we are writing against, to manage, will also fail.

Knowing this, we can optimize for the case that we want our Operational Logic to continue to function properly even in the case of a network partition or failure.

If I have locally cached data to the server my Operational Logic is running on, I can access that data consistently, even if the network fails and the server running my Logic cannot reach other networked services or nodes.

This allows me to handle failure cases more gracefully.  For instance, maybe all the nodes are not unavailable, and if I have the data that lists all the nodes and their properties on my server already, I can verify which are reachable, and which are not without an internal processing failure occurring (cannot access data to check with, because it has been partitioned in the network failure).

- Operational Logic should try to minimize the amount of frameworks, libraries and services it uses.

Frameworks and libraries are useful, they server a purpose, however the more things you have, the more things that can fail and cause your Logic to no longer function.

Additionally each of these things needs expertise to manage and troubleshoot, and your Operational Logic needs to be as straight-forward and simple as it can be, so that when problems occur, they can be troubleshot and resolved quickly.

Operations teams are also generally (at most organizations) much smaller than their Application Engineering departments, so this must also be done with less people involved in the work, and with shorter time frames.

Since the Operations team also has to take new services into account, and new hardware platforms, and may be given very short notice to get these working, the Operational Logic needs to be written to be able to be adapted to these situations extremely rapidly, and without causing problems for the existing infrastructure.

After all, in a one-way-to-do-it system, if you break something with a change, you have might have broken everything with the change.

This "force multiplier" or leverage gained from automation is a double-edged sword, in that it cuts your problems efficiently but if used incorrectly will cut you as well, by automating failures into happening in a wider area and faster than Humans can manually do.

In the past, these problems could be avoided when automation was implemented incorrectly by simply removing the automation and having everyone do everything by hands again.  I have seen this happen many times, when automation was immature, or was not given proper resources (mostly time) to be implemented correctly.

As the scale of operations continues to grow, this will simply not be possible or efficient in terms of money and personnel to scale enough people to do things manually, and the number of mistakes created by manual work will mean that even getting through the dangerous stages of automation will be a better trade-off.

We aren't quite there yet as of 2015, but it is coming.  Some organizations have a good amount of automation, and we will create a spectrum soon to do some analysis on this, but they are not yet comprehensively automated, and are approaching it through Aggregation, instead of Slicing The Pie.

This change in viewpoint is what is required to deal with automation comprehensively, and it starts with understanding how to optimize the Operational Logic to yield the effects required to allow this to happen.

- When things do break, how does your Logic function?

Minimizing dependencies, locally caching data are two strategies in making resilient Logic, but the real goal is that the Logic continues to function exactly as you designed it.

By using Slicing The Pie methods of black boxing work that needs to be done, one can create a system that anticipates failures, and continues to function properly with the resources that are still available to it.

This will the be automation we are going to inspect and start modeling soon.

3.2.1.2: Like 1 big computer.
-----------------------------

One reason why the difference between Operational Logic and Application Logic matters if that it provides an insight into another way of looking at the Production Environment.

By seeing it as a "one-way-to-do-it" system, where we mostly want things done one-way, we can actually look at the entire collective of Production Operations as a single entity.

We can abstract it so that it is "one big computer", with many nodes, which can be configured as if it one a single computer, with containers in it, or rather different directory mount points.

Each node in this "one big computer" has it's own internal process schedulers (as Operating Systems start processes through a scheduler, that manages interrupts and putting processes back onto CPUs when their system calls finish), and it has it's own internal RAM and storage, etc.

But, the entire set of machines, no matter how distributed they are across the planet, or how many nodes they are, can be controlled in terms of configuration and operational management, as if they were one system with many parts.

I think of this as a layer of Operating System above the traditional bare-metal and virtual-machine installed Operating Systems, whose goals are to abstract physical hardware (BIOS, Buses, Devices), and manage device drivers, and schedule processes on their CPU, and manage libraries and file systems and virtual memory and such.

So, I'll introduce this acronym as "DOS", Distributed Operating System.  It is similar to a "cluster", but clusters are generally more uniform, trying to have the same type of pieces controlled by the same processes, in this they are homogeneous.

Distributed Operating Systems (DOSes), would be heterogeneous, with any number of different hardware specification, different Operating Systems, and different services, and can contain any type of storage, in any configuration.

Just like a single system, where you can run any kind of software (for that platform), or configure the directory structure in any way you want, there is no standard order for a DOS, it is merely an abstraction of working with a number of systems as if they were one system.

There are unfortunately some acronym name conflicts with DOS, such as the legacy "MS-DOS", but this can simply be specified as "MS-DOS" or "PC-DOS" for the rare instances that someone needs to refer to this.

There is also another acronym for "DoS", which is Denial of Service, and usually takes place in reality as a "DDoS", Distributed Denial of Service.  The convention is to keep the "o" lower case, which makes this less confusing.

Since we need to move forward in our industry, and distributed systems are here to stay, and we need to advance our methods of thinking about how to manage those distributed systems, I think we can safely take the acronym "DOS" for our purposes.

One big computer, many nodes, heterogeneous Operating Systems, and services.  All able to be managed as a single system.

It's a big deal, and I predict whether this terminology is adopted or not, that in the future we will end up seeing Production Environments in this way, because of the efficiencies that this will lead to.

In any case, I'm going to detail how to build this sort of thing in this book, so you have a path to getting access to this technology in your hands already.

3.3: Axiomatic Engineering
--------------------------

We've been building up to this for a while, introducing different spectrums or axes for different Attributes of this or that, but do they fit into a system?  They do!  And I call this "Axiomatic Engineering", which is like working with mathematical Axioms, to create engineering solutions.

In this way we can detail all of the Attributes that we would like, and specify the spectrums (or axes) of those attributes, and then assign values to each attribute axes that we would like.

Do we want more Consistency or less Consistency?  Do we want more Availability or less Availability?

Between Consistency and Availability, which is higher priority?  What sorts of trade-offs need to be made if we were to rate Consistency higher than Availability?  What about Available over Consistency?

We can't possible implement the same solution while matching our different axes values, and priorities, because we care about different things in each circumstance, and so we will create a different solution.

This is important in your own work, and critical for working in a team.  If you can't agree on your values, how will your work have the Alignment necessary to produce the effects you want with efficient use of your resources?

Let's re-iterate my generic definition for Engineering again:

 "The efficient use of resources applied in an environment, to yield a desired effect."

So we have:

- An Environment (Production)
- Resources (time, people, hardware, money)
- Effects (Availability, Consistency, Resiliency, Atomicity, etc)

These are the fundamental elements of Production Operations Engineering, and how we mix and match them together, and the methods of their implementation, will determine the effects that we get.

If we are being Pragmatic, and we are only concerned with the effects, then we can start to build an "Effect Estimating Machine", and this is done through Axioms, created by populating our Axes with values and prioritizing which of those values are more important to us than others.  After and during the implementation of the solution, we can use an "Effect Evaluation Machine" to determine how our implementation is matching up with our Prioritized Attribute Axes values.  These would be a type of mental Virtual "machines", which could be considered mental software, or well-structured, consistent, internal algorithms for thinking, and used externally for communication.

Let's make an overview for all of services in the Production Environment:

- Available.  Our services must be available.

- Performant.  Our services must be fast enough for our purposes (poor performance under heavy load means that some percentage of our end-users will not have Availability).

- Manageable.  We need to be able to control our environment, deploy software, upgrade security flaws, making configuration changes, add or replace server nodes, control user access, etc.

- Visible.  We need insight into our system through monitoring, alerts, logs, etc.  We can't manage things if we don't know what is going on.

That's a pretty good start, so let's take this as our basis.

I have also ordered them in a general order of priority, because:

- If the services are not Available, what is the point of it existing?

- If the services are not Performant, then they are not available to some end-users, or are not timely.

- If they are not Manageable, then we cannot control them to keep them Available and Performant.

- If they are not Visible, we cannot efficiently Manage them.

We could add other elements in here, or split these up, and some circumstances might order them differently, but this is a good starting place for our purposes.

So, let's check our Attribute Axes for these prioritized goals:

- Available:   Not Available <---> Completely Availability
- Performant:  Slow <---> Fast
- Manageable:  Difficult, Risky and Slow <---> Easy, Safe and Fast
- Visible:  Opaque or Fuzzy <---> Clear and Precise

For Manageable, I ended up creating three different sub-attributed, as saying "Unmanageable" really doesn't mean much, so we can re-write it as:

- Available:   Not Available <---> Completely Availability
- Performant:  Slow <---> Fast
- Manageable: Risk: Dangerous <---> Safe
- Manageable: Difficulty: Difficult <---> Easy
- Manageable: Speed: Slow <---> Fast
- Visible:  Opaque or Fuzzy <---> Clear and Precise

I have split these up now into individual attribute axes for Manageable, and also re-ordered them slightly for better prioritization, as we are more concerned with Risk than Difficulty.

Difficult things need more leeway in performing them, so I am putting this higher than Speed, because if you are doing something difficult, but do it quickly, it seems that might lead to more mistakes, which increases Risk.  Perhaps the "Safeness" of the higher priority will protect us from these mistakes, but unless that is guaranteed, than Difficulty should be a higher priority issue than Speed.

Is Visibility really less important than all of those Manageability attributes?  Maybe not, let's do one more re-ordering:

- Available:   Not Available <---> Completely Availability
- Performant:  Slow <---> Fast
- Manageable: Risk: Dangerous <---> Safe
- Visible:  Opaque or Fuzzy <---> Clear and Precise
- Manageable: Difficulty: Difficult <---> Easy
- Manageable: Speed: Slow <---> Fast

That looks a little better to me.  We need that Visibility, because it speaks to knowing what is going on.  I would rather than that then easier to faster management, as I need it to ensure my work is correct, or help with troubleshooting if an error is introduced.

Now, we have some Attribute Axes, does that mean we have Axioms?  Not quite, but we are getting close.

3.3.1: 90-9-.9-.09% Rules for Priorities
----------------------------------------

Let's take a brief tangent to talk about prioritization.  We made a couple prioritized lists earlier, and they were listed sequentially, but not numbered or evaluated in terms of "how much more important" each element was.

There are many ways to rank priorities, and I have come up with a methodology that I like which I call the: "90-9-0.9% rule", and can be said as the "Ninety-nine-point-Oh-nine rule" to make that actually pronounceable.

The progression continues on forever, with the previous item being ten times (10x) more important than it's following item.

This allows for clarity in which thing is more important, and also for knowing when things are just not important any more.  It is purposefully exaggerated because without that clear separation, it is unclear why one action would be preferred over another action, because of "extenuating circumstances" may exaggerate a lower prioritized item over a higher prioritized item.

It is my contention, that you should never do this.  If you are going to change prioritization, you should explicitly change it from the order of ["A, B, C"] to ["B, A, C"] for a given circumstance.  "ABC" may normally be what you want, and in some circumstance "BAC" may be better, and so you should explicitly state that.

But, while evaluating the priorities of "ABC", then "A" should always be preferred over "B", or you should change your assessment of the priorities and state what the extenuating circumstances are for the priority change.  This is for clarity of communication, both with yourself at a later date ("Why did I do that?") and for people besides yourself who should share a common understanding with you.

By making the differences 10x apart, it clarifies things much more than if they were less.  2x may still sufficient, but let us first demonstrate that merely being "too close together" in priority separation causes confusion, and from that we can see that "further apart is less confusion", and have our answer for why this is a valid technique.

Say we have priority of Availability and Performance, and we assign Availability a value of "100" and we assign Performance a value of "90", so that Availability is the most important thing (an "A" grade of importance"), and Performance is the second most, but still highly important (a "B" grade of importance).

So, Availability is first, but Performance is still quite close behind at 10%.

Say there is a decision to be made, and it has to due with a hardware configuration, say cabling, that will give an Availability vs. Performance tradeoff.

Let's say that we can cable up some storage which will be five times (5x) faster in Specification B, but it has as flaw in that sometimes it fails, but very rarely and might be able to be avoided with some maintenance actions.

But, there is another cabling strategy which will ensure Availability, Specification A, even under intense failure scenarios, but is one fifth (1/5th) the speed (Performance) of Specification B.

If we have a 10% difference in importance (100 vs 90) in Availability (Spec A) and Performance (Spec B), but we are getting a 5x boost of Performance if we choose Spec B, we have a decision to make, and some data to make it with.

If we were going to seriously evaluate this, for a presentation on "What should we do?" to our department, we could make up some "point system" and do the arithmetic and decide which had more points.  On a scale of 100 vs 90, it is possible that the 5X performance could win the "point comparison" just because of the "5x" scaling value being used in some calculation.

Being "10%" close to the top item, it may seem more fluid, in that "this time" we will still keep Availability over Consistency (not thinking or talking about it, or not publicly stating the change in priority through documentation, etc), but we will go with the Spec B 5x performance boost, over better Availability.

Making this trade-off isn't wrong, the proposed down-time might be acceptable, if it doesn't also some with a Consistency trade-off of data corruption (because we haven't accounted for that, you might find that acceptable as well as a trade-off) or another important Attribute which needs to be accounted for.  (Aside: Data Corruption would actually impact Availability directly, since if the data is corrupt, it isn't Available in a useful form.  Consistency in terms of recovering may still take time, and also count against Availability.)

However, when making the scales of the system ten times (10x) different, then the spread is much wider, and thus more clear.  Availability is worth "90", and Performance is worth "9".

Even if we took a very naive algorithm of "5x performance is 5x the value", we get "90" vs. "45", and Availability is still on top.

If we change the value to "10x performance", then we get "90" vs. "90" and while the positions match, we still know Availability is #1, and so it is clear that Availability is still our top priority in this case.

If we change the value to "100x performance", we would get "90" versus "900" and it is clear this Performance has true value.

What it means in reality is that we have a new Caching Layer.  With 100x performance (or even considerably less), it is worth it to try to leverage that storage in a different capacity then we are currently considering.  The "balance of scales" is heavily in favor of using "Specification B", because it's performance simply cannot be denied, but we probably still need to use "Specification A" as well, for reliable storage that is better for Availability when the "Spec B" solution fails.  This decision will probably come down to whether the money is available, and the cost-benefit analysis determines it is required and worth it, for implementation both solutions as a 2-tier caching and persistence layer.

"Specification B" could be used for very fast read-only queries, or it could be used as transient storage for incoming queries, so that there is a "pretty reliable, with known long-term faults" solution in place for taking incoming data as quickly as we can.

These types of analysis are what using multiple-axes of values (Attribute Axes), and combining them into an easy-to-communicate-and-visualize method allow.  We can change the values around, put them into forms or a spread sheet and apply algorithms to compare them quantitatively, etc.

So, I have establish that using 10x scale differences has value, so let's put it to use:

- Available:   90%
- Performant:  9%
- Manageable: Risk: 0.9%
- Visible:  Opaque or Fuzzy 0.09%
- Manageable: Difficulty: 0.009%
- Manageable: Speed: 0.0009%

Now the sequentially prioritized list we created before becomes numerically weighted.  We can calculate against each attribute based on the value we have assigned it, to determine which actions we should take next.

But, one might ask, isn't setting things at 0.0009% and lower making them trivial and not important to work on?

That depends on whether there is more important work to be done, which is the beauty of this system.

For instance:

- If there is no work to do at the 90% layer, because the system is currently up (Available)

- And, there is no work to do at the 9% layer, because the system is currently running fast enough (Performant)

- And, we are not currently evaluating making a change that introduce Risk into our Production environment (Manageable: Risk, at the 0.9% layer)

- And, we currently have sufficient monitoring and visibility into our system (Visible, at the 0.09% layer)

- And, we have a problem with how Difficult some tasks are to perform (the 0.009% layer), then this is currently the top priority, and this work should occur.

Should we also schedule work to fix "Manageable: Speed" problems (at the 0.0009% layer)?  Not unless we have another person to assign it to, as the 0.009% layer is 10x more important.  

Once the 0.009% work is complete, the 0.0009% work will become the most important work.  If you should ever have a problem with Availability (90%), it immediately becomes the top priority, as it is one hundred-thousand times (100,000x) more important.  That is clearly more important, and the scale differences again make things very clear.

I think this is a system that provides a lot of clarity for what is important right now, and how we should design things, and how to separate what should be done from what should not be done.  It's simple enough to document in a page or so of Prioritized Attribute Axes, and that makes it easy to version control, or put into a Data Source, so we can also run Logic against it.

In a one-way-to-do-it system, you do not want to do all-the-things, you preferably want to do one-thing for any given category of thing, so that you can gain efficiencies from that correctly chosen thing, for your set of priorities, goals and engineering values.

Although I believe being able to maintain a regular scaling interval (10x) between priority levels is good, and the "90-9-0.9%" format makes doing this clear, it is not easy to communicate about these levels using the exact percentage values because saying "0.0009%" is difficult, and it is easy to confuse between "0.009%" and "0.00009%".

Instead we can simply order the layers as "Top Priority", "Second Priority" and so on, or some other labeling structure which is easier to say.  ("Alpha Level, engage!", or whatever works for you.)

Then you can say "This is 5th level priority, but we don't have anything to do in levels 1 to 4, so it is currently the top priority", which is clear, numerical, and does not use potentially confusing real numbers for normal communication purposes.

The labelled tier structures can be replaced with their numerical equivalents to perform quantitative analysis whenever it is needed.

The take-away for this section is not "this is a good technique, use it", although I am currently using it, and I do recommend it, but the larger lesson here is that you can make up these types of devices yourself, and you should.

Come up with your own numbering schemes, labeling schemes, and determine the exact meaning for each of them, and reasoning behind why they are a valid method of working, and then suggest other people use them yourself.

This is the type of Engineering discussions I would like to see more of, and the type of Engineering thought that I believe the Operational Engineering world could benefit from.

We get clear sets of data, that are quantifiable, and qualifiable, and we can test ideas against them, and communicate clearly about what our priorities are, down to which axes of information, and we can change the attribute axes values or priorities and talk about how those changes would affect our designs, and evaluate how well our implementations did against those values during and after implementation.

3.3.1.1: Assigning different people different priorities is what makes up different roles.  This allows different points of view, to make the organization stronger and more thoughtful, by design.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now, we have created a system for being able to prioritize our Attribute Axes that we are using to evaluate our goals.

How do we use these, is it one-size-fits all?  Well, that doesn't sound like our working definition of Engineering, so that can't be the right answer.

Now, for "How do we prioritize work in Production?", this starts to become more specific, and we can generally use this as a set of priorities.

However, different people do different things in an organization, and these priorities just don't make sense for everyone.

Even in a Production Operations team, once it gets large enough, or if it has special needs, there may be people who do nothing related to the up-time or Availability of Production.

These these people, they still need to understand and agree with, for the purpose of providing proper utility to their organization, the Production Priorities, but they will need their own priorities in doing their own work.

In fact, everyone should always have their own priorities, and then they should match up their priorities against the environments that they are supporting or responsible for, or interacting with.

For example, someone with a title similar to "Database Administrator" would be primarily focused on how whatever changes are being made relate to databases.  They might be concerned at how the Development department might be making changes that could cause table scan differences.  Or how a schema change might not be able to be rolled back in a reasonable time, or might take too long to apply the change.

Their concerns will be prioritized around their responsibilities.

Different people in a department will have different priorities, and it is through this that the department gains coverage across concerns. 

If everyone was only paying attention to exactly the same things, then there would be blind spots where no one was looking, and it would create a "monoculture" where only certain kinds of ideas would be suggested, and other types of ideas would be ignored or discarded, even though they may provide a valid solution that meets a different set of priorities.

Having this internal opposition of priorities can cause friction, but this friction (if done in a healthy way) will lead to better discussions about the issues than if everyone had the same perspective, and so the discussion didn't take place at all, because there was no opposing point of view.

This is the "Devil's Advocate" of Engineering, but shouldn't be used just to throw out opposing ideas, as that is also not Axiomatic Engineering, but should be applied to a set of Attribute Axes and Priorities with a different value set, that has a different perspective.

This is always the case, but it not always explicitly the case, in fact it is rarely so in my experience.  Explicitness could be seen as "pedantic" or "argumentative", when it does not need to be this at all, and should be encouraged in the time allowed for discussions.

The organization and department should make an effort to provide timelines that allow some period of these discussions, at least for most important changes (things that are direction changes, direction-setters, or are risky are the most important).

3.3.2: Creating Axioms from Axes
--------------------------------

This will be one of the few places in the book that I use an external definition to help us get more clarity.  I used to always lead with dictionary definitions and quotes for things and I still am a fan of both these things, but if I am writing a book about how to think about things and evaluate them for yourself, it doesn't help to constantly source external material as an authority.

So accordingly to the greatest authority that was easily accessible on my phone as I wrote this, there are generally two types of Axioms.  Logical Axioms and Non-Logical Axioms.

Logical Axioms are where you say something so simple and concise, that it couldn't possible by disagreed with.

This might be something like:

"If Availability of your Production Operations is your top priority, you need to have a validation step before making a change to determine if the change will cause down-time or Unavailability."

This borders on a tautology, and that is OK, because it is being specific, and has utility.

Is "Availability" our Top Priority for our Production Environment?  If so, then we need to validate that a change to the Production Environment won't cause a problem with our Availability.   BAM!  Axiom!

Not the most useful axiom, until one doesn't implicitly follow it, and causes an outage, and then a New Policy is created:  Validate the change against the existing Production Environment, and determine the level of Risk, and then test it against a Staging Environment to ensure it works there, before implementing in Production.

This is a Policy, that creates a Procedure, that stems from the explicit axiom, with a historical background of the outage event in question as it's inspiration.

So, we have "simple statements no one should be able to disagree with" as one type of Axiom.  It is important that these statements are very explicit and detailed, or the generality of the statement will make it not true in some circumstances.

For instance, I lead that axiom with "If Availability of your Production Operations is your top priority", because this set's both a Priority and a fairly specific range in the spectrum or axis of Availability that it will be "Highly Available" or more towards Available on the scale of:

Not Available  <--->  Available

Now let's look at the Non-Logical Axiom, which is defined as something that can't be proved by simply thinking about the assertion as being true or not true, but fit's into set of rules such as the commutative property of Arithmetic:

a + b == b + a

Things are able to be moved around from being first to being second, with the same results.  This only works, for some operations, not others.   For instance:

a / b == b / a

This is generally not a true statement, so cannot be an axiom, because unless "a" and "b" are both 1, then the different sides of the equation will have different values.

But, this is only for the general rules of Arithmetic.  We could create our own usage of the symbols "/" and "==" and define them to mean something else, then this could mean anything we want.  However, because these symbols have an established use, and would generally be read with that use, this might be a bad idea.  It depends on if it would make things more clear or less clear.

Regardless, the point is that Non-Logical Axioms fit into a system, and they should be seen, understood and used in the context of that system.

We will be using both kinds of Axioms.

What we have been leading up to is mostly being able to build Logical Axioms, by taking our specific Attribute Axes, and the values we have assigned them, we can create Axioms.

By using the Prioritization of our Attribute Axes values, we can make other Logical Axioms (that deal with Priority).

We can also make Non-Logical Axioms by coming up with a system for how to discuss and compare the different things we are working on.  We can turn the Logical Axioms into variables, and create formulas out of them to determine what is a Logical course of action.

We can also create Non-Logical Axioms once we start building these formulas, as we can decide how things can be treated inside the algorithm to express different ideas, and get different results.

To go back to Philosophy, these elements are part of the Philosophy of Mathematics.  These do not need to be strictly used in an academic or strictly used in standard methods of statical analysis, but can be used in any circumstance, given that we have put sufficient thought and detail so that they can be used discretely and deterministically.

3.3.2.1: Impersonal decision making through communicated values and priorities using Axioms
-------------------------------------------------------------------------------------------

One of the immediate benefits that we can apply to our everyday jobs is to use these Axioms, and their component Attribute Axes and Priorities to determine what actions we should take, and do so in a non-personal way.

These days, when I make decisions, I don't do it because "I want to do X" or "I think X is a good idea", or "I had problems when I do Y, so I do X instead".

I make decisions based on turning things into component pieces, evaluating them, and determining what action best aligns with all of the values (Alignment).

One course of action better fits those values than another course of action, and that is the action I advocate, and I attempt to use the internal variables for doing that analysis in my explanation of why this is my current position.

Change any variable, and the answer may change.

As a thought experiment to visualize this, I like to imagine a scale, like the "Scales of Justice" or an old weight scale where you have 2 sides, and you put a known weight on one side, and the thing you are trying to weight on the other side.  

Since this is not a digital or a single-downward-vector scale (as we generally use these days), but a lever-based scale (I don't actually know the technical terms for these scales, so just making up what makes sense to me), it has two sides, and not just a single platform.

So, we have this old-style scale.  And on the weighing platforms on that scale, sit 2 more scales.

Each one the same type of scale as each other (you can imagine them smaller than the first, so they fit), so that now there are 3 scales

The first scale weighs the 2 scales that sit on it's 2 platforms.  Initially these will all be exactly equal, so no tipping of the scales.

On the 2 scales sitting on the primary scale, there are 2 more scales for each scale.  So 1 base scale (Level 1), 2 scales on the base scale (Level 2), and 4 scales on the 2nd-tier scales (Level 3).

And so on, forever.  A recursive amount of scales placed on scales.

The primary scale is our question:  Do we do "A" or "B"?  One side of the scale represents "A" and the other "B".

Sub-dividing our question into Prioritized Attribute Axes, they map to the layers of the scales.  

We can also use this with our "90%-9%-0.9%" rule:  Level 1 is our Top Priority (90%).  Level 2 is next priority (9%).  Level 3 is our next (0.9%), and so on.

Having a "Recursive Tree of Scales" in which I map all my values to, means that any time a value changes, the entire tree will need to rebalance.

If the "A" side was heavier, but something is removed and added to the "B" side, or something was merely made heavier on the "B" side, then the scale will tip.  Maybe it won't go all the way over to being "Fully-Weighted-On-B", but it will be "Less-Weighted-On-A" than it was before.

This imaginary set of scales is always working in my mind as I rate the various axes that my organization or goals are concerned with, and as changes are proposed, I re-scale my values, and the Recursive Scale rebalances itself.

In this way, I am not really making any decision at all, personally, I am merely an agent of this system, mapping values as I understand them into a set of Prioritized Attribute Axes, which map to goals, which map to a result (effects) that we want, and when any variable changes, the results might change.

This doesn't mean that I don't bring my experience into the picture, because I do, but my experience is mapped into this Attribute Axes and Priorities, and can be expressed in a deterministic and explicit manner.

They can be written into a Data Source and evaluated by Logic, and they can be graphed, statistically analyzed and revision controlled for historical reference.

This is how I make judgement calls in a "non-personal" way, and I assert that this is a valid way to proceed with making Engineering decisions.

3.3.3: Fashion Oriented Engineering
-----------------------------------

This section is a little tricky for me, because it's a thin line between just gathering information and using it, and "blindly following things" or simply acting out fashions.  These are all highly subjective, and trying to write up the history of these "Fashion Eras" in technology mostly reads like it is a valid progression.  The problem is to the extent any information is valid, for your context, not that the information contains potentially valid information.

This is the problem with rationalization, and anything can be rationalized.  However, Rationalization and Engineering are not the same thing.

So I'll just that simply state that reading other organization's Public Relations releases on what they are doing and how they are doing it, is frequently information one cannot validate.

Taking it as a data point and deciding whether a given methodology works for one's environment, with one's resources, is Engineering.

Simply doing something because an Authority has said they do it, and worked well for them, is accepting their Appeal to Authority (a logical fallacy).  They don't even need to appeal to anyone, people do the appealing themselves just from seeing the content and knowing that the organization has some social credit or prestige.

I have been in far too many meetings where a problem was brought up, and then someone mentioned a blog post from some currently-fashionable-company, and then the consensus was to do what the blog post said, without properly evaluating whether it was a good fit for us, or a valid technique in our context.  

This is outsourcing one's infrastructure design and decisions to a party that does not know one's environment, one's resources, one's goals, and was probably not even intentionally telling anyone to follow their path.  This is giving up "agency", or ability to make one's own decisions, based on one's own data and context.  In fact, discussion against this course-of-action was sometimes seen challenging the legitimacy of the organization who made the press release.

I refer to this as Fashion Oriented Engineering (FOE) or "Blogineering".

Maybe these are good techniques, and if we evaluate them in the way we evaluate everything else as an Engineering decision, then it is not Fashion, it is Engineering.

However, if one simply says "I read on Famous Company X's blog, they were doing Y.  Let's do Y.", this is not Engineering.  This is following a fashion trend setter.

I have been at organizations that made very well received press releases (through their engineering blog) that completely mischaracterized what was going on in their environment (from my perspective), and it was well accepted by many others in the industry.

Why?  Because they have no idea that if they actually worked at that organization, they might completely disagree with the statements, because they have more information and could see the chain of events, and the effects of the recommended practice.  There are many colloquial phrases such as "putting lipstick on a pig" that relate to dressing up something that you don't want to make it look like something you do want.

{{ todo__get_a_couple_phrases_and_pick_a_different_one_could_be_seen_as_sexist }}

No one is going to publicly announce that they are making a mess of their operations, but if their management tells them to make press releases (blog posts), then they are going to do that, and do it in a way that makes them look good.

They have an incentive to "spin" things to a positive outcome, regardless of real Engineering going on, and the effects thereof.  They may be doing excellent Engineering, I am also not saying that they are not because I don't have that contextual information, I am simply saying that we don't have direct experience with this information, and it should be treated as noise, that we can potentially extract signal from.

So, Buyer Beware!  Engineering blogs are "press releases", in fact all public communications are, and like any press release they are effectively "selling" something, such as how great a place they are to work, or how efficient and intelligent they are.

There is nothing wrong with these press releases, they are a good thing, as they share information, and may be very useful.  However, they should be taken as information in the sense of, "Organizating X made a press release where they said Y."

This is true, and can be useful.  Simply doing what one interprets from their release doesn't even mean that they communicated it properly, or their intent was understood properly, and it is a summarization, so it is only giving a limited insight into the reality behind the post, at best.

Just something to keep in mind.  Fashion and Engineering are not compatible in making decisions, and there is a unfortunately lot of Fashion going on, in my experience.

3.4: Evaluating changes.
------------------------

Now that we have established how to set up Attribute Axes, Priorities and create Axioms we can start to look at how to make evaluate changes, before making them and afterwards.

Let's start by creating an example problem, by setting up the environment for it, current state, and our goals (end state).

Let's start with a simple website with some dynamic content, which we are deploying.

Our goal is to improve our performance in doing the deployment.  Currently, we are copying the installation files sequentially from a single server, and we have 100 web or application servers which we are copying them to (we will call them "web" servers for simplicity).

The exact mechanisms for copying and deployment are not going to be the focus of this example, and so we won't be evaluating their performance or impacts, because it will complicate the example.  In the real world, of course, these factors are also important, and would have be evaluated independently, and in conjuncture with the rest of the changes.  

It is important that all details are "Aligned" in that they work well together, and perform efficient as a whole (in their sequential and parallel processing), over long periods of time, and under our given resiliency goals.  Alignment is complicated to explain, so I will keep giving examples of it over time, so that you can build up your own understanding of the concept, and how to apply the term as I am using it.

So, we have a current state:

- Single server, connects to 100 servers over SCP (secure copy) sequentially.

What are some options that will perform better than running 100 sequential copies?

One method is running the copies on the same single server, but running the copy commands in parallel instead of sequentially.

There are a number of options for running things in parallel:

- Forking the process, so that there are many processes of SCP running.  Forked processes are independent of the process that forked them (they start as clones, and then do their custom thing), and do not have a lot of communication with the parent.  There are ways to know some things about the program though, so this is a viable option.

- Using a controller program to create Threads, and running the SCP process in the threads (similar to forking, in that there are still 100 (in this case) SCP processes being run, but they are being controlled by a single program, instead of just independently launching.

Since I want to constrain this example, I won't get into the differences between controlling forked and threaded sub-processes, it's enough to know that while they have differences, we can get the results we want out of either of them for this case.

{{ todo__describe_forked_vs_threaded_somewhere_else }}

It doesn't matter whether we write our own code to do this forked or thread handling, or we use software someone else made, such as "Orchestration" software which might have agents that run on each target server, and perform the copy in it's own way.

So we have specified 2 methods running on the same single source server, and performing the work in parallel.

Since we have run into this performance problem by running things sequentially, one thing we will do is say, "Let's not get into this situation again, once our server targets have grown again", and say that we are removing the option of using sequential copies again, because it will not scale, and will create work for us again in the future.

Since we just went over how create an Axiom, let's do it now.  However, since we are working with a specific scenario and have not yet looked at all-of-operations together, we shouldn't make this a Universal Axiom, or a Production Axiom.

Instead, let's make it a Working Axiom, or a Temporary Axiom, for the purpose of this problem.

Here goes:

"Once a job that was working sequentially on a single server hits a scaling problem, and needs to be changed for performance, all later implementations of that job will not be re-implemented sequentially, even on more than a single server."

This is a little longer than I like for an Axiom, and it has more caveats than I prefer as well, as I like them simple and straight-forward, always able to be applied.

In this circumstance, we are building a Working Axiom, so it is temporary, and it needs to be precise, so it needs those caveats to fit into our problem space.

Let's review the verbiage quickly to see what caveats I baked in:

- I have limited this to implementations that already exist, and were implemented as sequential processing, on a single instance.

This could actually apply to a number of different scenarios, not just the one we are currently discussing, so this is good Axiom material, as we want to be able to apply Axioms generally, so that they are usable or actionable.

- I specify that this axiom is only to be applied once the work hits a problem.  Going around and "fixing" problems that aren't problems is a poor use of resources, as there are likely actual problems that need fixing.  Also, it is creating change in the environment, which may lead to instability or outages.  

All changes come with risk, as you only know the effects of your previous system from your history with it, once you change it you are working with a new system (new state vs. old state), so you may get different effects.  

If your change is implemented ideally, then the effects that change are exactly what you planned and wanted, so everything is OK.  If you get effects you did not want, or did not anticipate, you will likely be created a problem, which may need another change to fix.  In cases where it causes an immediate outage or degradation, it will need to be reverted or "rolled-back", if this is possible.

- Once a job gets to this "problem" state, we will not create another solution that operates sequentially, as we have proven that for this case of work (job), sequential processing doesn't scale for us.

This doesn't meant that everything should be parallelized.  Firstly, not everything can be run in parallel, as some operations are sequential operations.  If you need to get data, and then format text with it, you can't format the text at the same time you are getting data (in parallel), because you don't have the data yet.  This work requires being run sequentially.  However, if you have to process 100 of these, you may be able to run each of the 100 jobs in parallel, and then internally process them sequentially.

Writing things to work initially in sequence is a faster way to to develop, as the complexity of parallel process communication, locking and other issues can be ignored, and sequential processing is a default for many implementation languages (and all the primary Operational related languages, from any environment I've worked in).

- Finally, I state that even splitting the job across multiple servers, which may allow the sequential processing to have acceptable performance again, is not acceptable, because we are just planning to have this problem again when those N servers have to do "100" servers each, and we are back in the same spot.  This method of "throwing hardware at the problem" is frequently not the right move, although there are some special cases where it is the right move, which we will get into later.

The act of taking the same method you use now, and making a change to it that allows it to continue working, but with the knowledge that it will stop working again once you have continued growing as you have previously, I sometimes call "burying land mines in your own yard".  This is because you know this will create a problem for you in the future (problems, degradation, outages, etc), but you are doing it anyway.  You have embedded a known problem in your system, and will certainly encounter it again (unless you are going to decline and shut down the organization).

However, just because this is going to create a problem in the future, and is would be best to be avoided, there are circumstances this might be the "right thing to do".  Such as if you are working in a "Startup" organization (very small, moving very fast, not afraid to break things), and the trade offs are worth it.  

Doing things or not doing things should always be evaluated for their Engineering trade-offs, with the business goals and requirements.  Refusing to do something that is best for the organization, just because it will cause a problem in the future is also Not Engineering, even though it seems like it is "being a better Engineer", because it is not taking into account the actual environment, which is prioritizing moving fast over avoiding problems.  This will create Technical Debt, but may be worth the trade-off, just like creating Financial Debt can.

Ok, so now we have established that one method of solving this problem is to create parallel processing on the single server, and we have our Working Axiom:

"Once a job that was working sequentially on a single server hits a scaling problem, and needs to be changed for performance, all later implementations of that job will not be re-implemented sequentially, even on more than a single server."

We need at least one more method for this example to be complete, for our purposes (but not for a real world solution), and for that I will choose the method of the target servers all pulling down the deployment themselves.

This creates a "push" (parallel SCP copies) vs. "pull" (target servers pull down data) scenario, so we are comparing data moving in two different direction.

For this example, I will only provide 1 method of "pulling" the deployment data, which will be to use a Load Balancer and web servers behind the Load Balancer.

For all Production services, we should generally always have at least 2 servers for redundancy, in case one of them fails the other is available.  Note I say "generally always", which is a contradiction, but we will have to talk about this later.  However, for this example, to keep things simple we will just create a single Load Balancer and N web servers behind the Load Balancer.  For the example, we could say 1 web server, but since the purpose of Load Balancers is to distribute requests (load), we can say N.  Getting into 2 or more Load Balancers has a couple other issues I would want to bring up, so I will avoid it for this example.

So, to summarize, our "pull" alternative is:

- A Load Balancer server that accepts HTTP requests (also simplifying by not adding in security, made clear by not using HTTPS).

- N Web servers that can server the static content of our deployment data.

- Some Logic for invoking the "pull request" from the target servers, to the Load Balancer.  We will call this "Pull Logic".

- Some Logic for signaling the target servers that they should invoke the "Pull Logic".  We will this "Deploy Logic", since this invokes the deployment.


The flow of this Pull system will be:

- The new deployment data is put in place, in whatever way that is done, which is the same for any of our cases.

- Deploy Logic is triggered, by a Human running a script or initiating from a webpage, etc.

- The Deploy Logic triggers the Pull Logic to get the latest data.  This could also be done several ways, but let's take the simplest one of an Agent Model, where the Deploy tells each of the web servers it's time to Pull their deployment data.

- The Pull Logic makes an HTTP request to the Load Balancer, which proxies the request to the HTTP server, which responds with the Deployment Data.

- The standard "local installation" Logic runs on the web server node, which would run in any of our cases.


So, now we have established a more scalable Push and a Pull alternative to our sequential Push mechanism, how should we go about evaluating them?

First, let's come up with all the Attribute Axes that we care about here, and then let's prioritize them for ranking purposes, and finally we can assign values to all of the Attribute Axes, and then look at what their Prioritization tells us about what our options are.

One important concept to always be aware of when designing a solution is Centralization.  Let's create that spectrum:

Decentralized (0.0) <---> Centralized (1.0)

On the Decentralized end of the spectrum, things are done on many nodes (machines, servers, etc), and on the Centralized end of the spectrum, things are done in a single place.

The benefits of Centralization are control, and a single point to detect failures and perform control logic.

The liabilities of Centralization, or the benefits of Decentralization, are that there are many nodes, so if a node fails, you only lost 1/N of the total processing capacity, this also can help with performance as many nodes can do more work than a single node.

However, we actually have 2 sides to this Centralization question.

Firstly, we are always Decentralized on our HTTP servers, because we have more than 1 of them, or N of them.  So our Target is already Decentralized.

The question is whether we will make our Source Decentralized (HTTP servers behind load balancers), or our Source Centralized.

There is a slightly different perspective on this already going on with Sequential vs. Parallel execution on a single node.  Parallel execution has a "Decentralized" factor over a sequential execution, which is the Centralization of an execution process.  The differences between running many processes on the same server or running many processes on different servers have many similarities.

Now that we have this Centralization spectrum, let's put our options on the table:

- Push: Centralized execution of parallel processes.  While there is an element of Decentralization to the Parallel processing vs. sequential, this operates under the black-box of this server, since it is on a single server, it is still a 1-instance system, and so is fully Centralized.  Centralized = 1.0.

- Pull: We initiate it on a single machine, that contacts 100 machines, those contact 1 machine (Load Balancer), which contacts N machines that serve static HTTP.  This has a back-and-forth in terms of being Centralized as we move from 1-instance to N-instance, back to few-instances (1 Load Balancer), to N-instances (HTTP) again.  However, when we black-box this, the important part is that the 100 machines (N-instances) are requesting their deployment data independently:  this is Decentralized intallation, so Centralization is closer to 0.0, but probably not full 0.0, since there are many centralized steps, let's call it Centralized = 0.2.

Even in creating a simple set of values for comparison on a single Attribute Axes, we found there are many sub-points that could confuse the topic, and be causes for disagreement.  I'm able to settle these quickly in this text, because I don't have to have anyone else agree with my assessments, but as soon as you add in other people you quickly get disagreements based on terminology, experience and understanding of the current problem and previous solutions.

This makes this kind of thing essentially an unsolvable problem in terms of communication, and underlines how important it is to try to communicate clearly, like with Prioritized Attribute Axes, as it allows for some resemblance of qualified and quantified discussion, instead of the usual method of making decisions in groups:  who can talk the most, who can talk the loudest, who is better at arguing and the most important, who has the most social capital to spend on "winning" the current discussion.

Since we are looking for Engineering clarity as opposed to "winning" through rhetoric, we must make our best efforts to perform this work clearly, even though as we get into the details of any topic it obviously becomes unclear and could be subjectively argued to mean the opposite thing.  Your experience and discretion will determine what path you go down, so paying attention to the results (effects) of all your actions will need to be your guide in how to make these choices to get effects you desire, and avoid effects you do not.

So we have a Centralized axis, and Push = 1.0, and Pull = 0.2.  We have one Attribute Axis filled out.

What's another spectrum we can measure here?  Performance is important, since that is why we are doing this exercise.  So let's rate them both:

- Push: N parallel SCP processes start, and copy the tarball or otherwise single-file packaged deployment data to each node.  Starting 100 SCP processes at once can delay things moving as the handshakes are occurring, but once things start up being in a single SCP process versus an HTTP process will only have the encryption as an added factor, which is fairly minimal on modern hardware and can be ignored unless it can be measured to be important.

- Pull: 1 process initiates 100 processes, which make an HTTP request through a load balancer to our HTTP servers.  We never did cover how the 1 process will initiate the 100 processes; if we use SSH to do it, we are literally doing the same thing that the 100 SCP processes of Push would do (since SCP uses SSH), except for the data delivery.

All in all, I'm going to round these out to being equivalent, which means between them we can put both their Performance scales at 1.0, which means it is a non-factor.

What about Scalability?  This is another factor like Performance.  We came to this problem because the Sequential Push was too slow.  It was not too slow when we had less than 100 servers, but at 100 servers it is too slow, which makes this a Scalability issue.  So let's rate our methods in terms of Scalability, after we make a spectrum:

Can't Scale (0.0)  <--->  Can Scale (1.0)

Notice I said "Can't Scale vs Can Scale", and not "Not Scalable vs Scalable".  The reason for this is that we may still need to change our selected solution, as it is not the "Most Scalable" solution, but building the "Most Scalable" solution before you need it is not good Engineering, as it is overkill for what we need.  We only need to handle our current and near-future problems, not our far-future problems.  Implementing a solution for far-future problems may actually cause us problems in building, supporting and using it now that we are not nearly at that scale.

Imagine a deployment system that can handle quickly doing deployments on 100,000 servers.  Is this going to be as easy to use, create and maintain as one that can deploy on 300 servers?  Probably not, as the mechanisms that will allow it to scale to 100,000 servers probably add in a lot of complexity and will make it difficult to use this system, and to make changes as the business goals change.

So let's review our Push/Pull options on the "Can't Scale" vs "Can Scale" spectrum:

- Push: Runs on a single machine with 100 processes.  This only scales up to what this single machine can handle, so at some point we are going to need to move to more than 1 initiating server.  So this is only scalable for so long, and then we will need more machines to perform this copy, and we will need a method to initiate all those machines to initiate their copies.

- Pull: Has 2 limited server groups (initiating, load balancing) and 2 scalable server groups (target servers, HTTP static content servers).  This has a much better scaling factor, in that our "limited server" groups are actually easy to expand.  It is easy to add more Load Balancers, and easy to split up Initiators, as they do a small workload (triggering the deployment fetching Logic on the target nodes).  Additionally, since the initiating Logic (Pull) does less work than the copying Logic (Push), we can run more target node initiations from a single Pull-instance server.

So, with this I'm going to assign some values based on my internal experience and understanding of this space.  It would take too much space to go into all the decision points I am making to assign these values.  As an exercise, do your own analysis on this and come up with your own values, and compare them to mine.  Why do you think we came up with different values?  This will happen with every person you work with, if you both have different ideas for how to implement things, so it is a useful exercise.

I will rate the Push option as having a Can Scale value of 0.5.  It can scale, but will start to have problems as the target server count gets bigger.  SCP is not as fast as HTTP, and is not set up to handle as many simultaneous connections.

I will rate the Pull option as having a Can Scale value of 0.75.  This is still not an amazingly scalable architecture, but it has the ability to scale better than the previous one, so I am leaving room for more-scalable solutions, but indicating that it is clearly superior to the Push option in this single Attribute Axis.

Now, let's come up with another spectrum, which I will call Knowability (as we have used generically before), but will be more specific in this case:  Do we know all target servers got the new code?  Do we know they all installed the new code?  Do we know they are all running the same code?  This is what Knowability will mean for this case.


...tbc....

3.4.1: Alignment
----------------

Alignment is one of the most important concepts of building efficient systems.

Any system can be described in a number of ways, but let us consider a system that is described as nodes and links between them, or edges, so that can be describe a system as a Graph.

Any point of interest in the system can be described as a node, and the connections between these points of interest are our links or edges.

Let us first consider a physical building structure, like a house, but we will simplify it into a wooden ceiling (flat board of equal width and length, and a small height) and 4 posts of wood to put the ceiling on top of.  You can consider the wooden posts to be "4x4 inch" beams or other material.

Now, in this example the purpose of the beams is to lift the ceiling board into the air, and keep it there.  So the beams function as support for the ceiling.  This defines the terms needed to start inspecting the concept of Alignment.

How can we begin to measure Alignment?  Let's make up a scale.

Alignment Efficiency

Least Efficient <=====> Most Efficient

Here is a basic scale of efficiency, going from least to most, which is pretty vague.

Let's start throwing some more variables in and seeing how this immediately becomes more interesting as a concept that I am claiming is a core concept of Engineering.

Let's assign different heights to the beams.  Lets say the beams are:  10 foot in height, 8 foot in height, 6 foot in height, 1 foot in height.

How efficient are these heights of beams at keeping a ceiling raised above the ground?

Firstly, when we think of a ceiling, we think of it generally as having an even height, or having some sort of stylistically (or functionally) changing height, but always we think of a ceiling as something we could be underneath.

If one of our boards is only 1 foot in height, then for part of our ceiling, we know we will not be able to reside underneath it, as there is not much space.  This does not sound like a very good ceiling.

This means, that we can reduce the "efficiency" of the ceiling we are proposing, because the ceiling is qualitatively "not good" from our definitions (goals) of what a ceiling should be.

Now, if qualitatively we wanted a flat ceiling above our heads, then this sloping ceiling is also "less good", and if we we're satisfied with a sloping ceiling, but require that it only slope in 1 dimension, then these heights of beams are also producing a qualitatively "less good" ceiling.

That covers some qualitative issues, but what about quantitatively?

There are several factors we can immediately state for quantitative measurements, such as:

- Vertical Weight bearing:  How much weight could be placed on the ceiling/roof, before the structure collapses?  You can imagine snow, if you need a concrete example.  As snow accumulates, the structure bears mode weight through the supporting beams, and is at risk of changing structure and eventually collapsing as this weight is delivered over time.  Even unweighted by extra material, the material in the beams and ceiling board themselves have weight and will over time degrade, so this is always a factor.

- Lateral force stability:  How much horizontal or lateral force can be applied to this structure, before it collapses?  Is it equal in all directions?  How stable is it in terms of falling on one of it's sides?  Etc.

Let's start with just these two factors, though there are many many more than can be applied, even in this trivial example.

In the case of the beams with 10, 8, 6, and 1 feet in height, if they are mounted vertically under the structure, which provides the maximum resistance to gravity (a vertical force), then only or 3 of these beams will ever touch the ground at any time, for any given combination of their placement.

This is obviously an inefficient design for keeping up a ceiling.

If the beams are connected to the ceiling at an angle, such as they allow for a "flat" ceiling (equal height from the ground in all parts), then the ceiling will only be 1 foot high, and the longer boards will be connected at very steep angles, which will provide less resistance to the gravity force pressing down on the ceiling and beams.

This can be calculated as quantifiably less efficient than beams that are all the same height, such as all being 10 feet in height.

In the same way as this physical example yields different qualitative and quantitative results with only the variance of heights of the boards, so every virtual difference yields different qualitative and quantitative results with every change.

Some virtual differences may yield "essentially the same results", for your level of interest in those results, but the results will always be different with different values.

This is why you must understand your own environment, requirements, resources and goals for yourself, in as deep and accurate manner as possible, so that you can understand what these small differences will yield.

This is an example of "local alignment", because we were only looking at: 1 ceiling, 4 beams, 1 goal (ceiling is efficient), 1 force (gravity).

No problem we ever deal with in life is this restricted.  Even for our above example, we will have to deal with weather (wetness, heat), biological (mold, termites), and many other factors for a real world "just a ceiling" problem, which massively complicate what "building an efficient ceiling out of 1 board and 4 beams" looks like.

In our modern Operational environments, we have hundreds of sub-goals, and thousands of instances of software, and millions of instances of data, even in small environments, all of which have different access patterns and reliability requirements.

If you can extrapolate out the ability to understand Alignment for our "simple ceiling" problem, and can extrude from that the importance of understanding Alignment in our much more complex and complicated real world environments, then you will see why I am maintaining that Alignment is one of the cores of Engineering, and that it is one of the first questions we must always ask in any kind of design related inquiry.

In future sections I will go into how Non-Local Alignment is one of the bigger problems we have to deal with in modern organizations today, because even good Local Alignment may yield poor Non-Local Alignment, as two or more sub-systems are working together in a larger integrated system, and while they may be locally efficient, they are not globally efficient.

With this in mind, spend some time thinking now about environments you have worked in which had services whose poor Alignment lead to problems.  This might mean that one inefficient service blocked more-efficient services from being created because of the overlap they would have, and that the existing service was seen as "Good Enough", even though it blocked progress and improvements due to inefficiently being Aligned to the future-good-state that you would like to create.

In environments where I work, I see this constantly.  Almost every existing project is created inefficiently, and causes us to be blocked from moving forward to more efficient services (in that area and others) due to the inefficient designs of the existing services.  Can you see this inefficiency in your own environment?

While we want to have Globally Efficient Alignment, if you find yourself in an environment where there is poor global efficiency, then you must start with a single project that has good Local Alignment efficiency, and attempt to branch out from there, creating either new Local efficiencies, or leveraging your now-existing good Local Alignment to create larger and larger inter-connected efficient systems, which can eventually replace the older less-aligned and less-efficient systems.

3.4.2: The Problem with the "Best"
----------------------------------

Best is a concept that is poorly understood in our culture.  It is frequently used, but rarely clarified, because it's vagueness gives it rhetorical power, but in engineering this is simply a logical fallacy that leads us to poor choices and low efficiency.

In order to take a term like "best" and use it in a manner that allows us to make good choices and have high efficiency, we must understand what other properties "best" has, besides just being "the best".

What are some properties of "best"?

- There is only one of them.  Only 1 thing can be "the best".

- Something cannot be "the best" for a great number of circumstances, because as the circumstances (variables) change, then what is "best" will also change.

- This creates an inverse ratio between the numbers of circumstances a methodology can be applied in, and the efficiency of the results for those circumstances.  This can be extended by allowing for any given set of circumstances (variables) to be repeated over and over.  The repetition will cause some of the variables to fluctuate (time itself being in constant fluctuation, others being contextual yet still being classified as being processed in the "same general manner").

- The inverse ratio suggests that for any given circumstance, there is one-and-only-one "best" answer, and potentially a small set of "close-enough-in-quantitative-results" class of answers that competes with the local-maximum of the "best" answer.

- Changing any of the requirements, resources or goals significantly will almost assuredly change which given solution is the "best" answer to the new problem.

This set of properties took it's shape through a line-of-reasoning, instead of enumerating things that were visible without reasoning, but both methods of defining properties are acceptable (simply remember how you came to them, in case they need re-evaluation).

In engineering we are not generally interested in the "worst" outcome as a result, except when we need to brainstorm in finding potential problems to pre-solve against in coming up with our failure matrix for our services/etc.

Determining "worst" solutions is using the methodologies for "best" with reverse quantitative comparisons.

In my view, this makes it clear that best/worst are a very small subset of options, and those options are highly detailed to one's exact environment, requirement, resources and goals.

As such, there can be no such thing as "Best Practices" (see section {{ section__e5829271e6cfb5927f3a4d4aec1b10df }} for details), because these are generalized solutions, for generalized environments, generalized resources available, and generalized goals.

"Best Practices" are useful to read as case-studies that someone is claiming a method worked well for them, and they can recommend it as a potentially useful method, but since this goes against our own understanding of what "best" really means, these should be reworded as "An Example Implementation", not a "Best Practice", as it is neither Best nor a Practice, since Practice connotes a deeper level of understanding that is provided than the very thin layer of a "recipe" and some case-study information.

In this book, I try to define for you, roughly, my Practice, for how to do engineering and operations.  I am trying to provide deep insight into how these things work, as I see them, and how I manipulate them to achieve results I desire, and how you can learn from my work and help with improving your own methods.

Be careful with the language you use casually to describe things like "The Best Way To Do Something", in your giving or receiving of information, because the results you receive from taking those words at anywhere near their face-value may be far from the suggested-reality those words relayed to you.

"Best" has a powerful symbolic meaning to us.  Use it very carefully, or pay the consequences for wielding power poorly.

A better way to think of things is using the term "better".

Better is always a comparison between two distinct things.  Best is often only discussing 1 thing, and lumps everything else into the second category: not-the-best.

"Better" specifies two things, and it is known that "everything else" is not being considered at the moment, and so it not being discarded at the moment.  "Best" discards everything but the "best" immediately.

"Better" immediately leads to questions such as, "Why is it better?  In what way is better?  And, in what ways is it worse?"

When you think of "best", it does not immediately call into mind the same questions, because the power of the symbol of "best" is that there are no competitors, it is the best.

And yet, from our inspection earlier we see that "best" means a very limited set of scenarios, do we know that we described the scenarios accurately?  If the "best" is based on a limited set of scenarios, and we described anything inaccurately in the description of our scenario, than very likely we chose the wrong "best".

In comparison with "better", we have to be more explicit.  Our language compels us to describe the "better attributes" explicitly, and begs that we also describe the "worse attributes" in comparison.  "Best" does not beg that we describe the "worse", because we don't care about the worst methodology or worst design.  Our minds enjoy the relationships of extremes.  "Better" leads to "more good" and "less good"; "Best" leads to "worst".

In both "best" and "better" we do care about their peer results, but "best" claims to have no peers, while "better" usually implies there are competing peers.

Thought exercise:  In what circumstances currently do you use the term "best"?  When applying my critique above, what strikes you as something you need to think about more in terms of "best" or "better"?

Can you think of a single thing you currently describe and think about as "best" that it would be better to reframe as "better"?  What tangible benefits could this immediately bring you, from this change in your thinking and decision making abilities?

3.5: Understanding Engineering
------------------------------

I've said before that I think Engineering is:

{{ definition_begin__engineering }}
"The efficient use of resources that meet requirements which sufficiently satisfy your goals."
{{ definition_end__engineering }}

Let's break this down in a way where we can understand Engineering as a process.

If we wanted to make a sequence from general-to-specific in terms of honing in on understanding Engineering, we can start here:

- Environment		->
- Resources		->
- Requirements		->
- Goal			->
- Actions		->
- Changed Environment	-> 
- Desired Effects?  
- Efficient use of resources?  
- Management of environment?

We start with an Environment, in which we have Resources, and we have some kind of Requirements, which apply to some Goal(s), so we perform some Actions, which change the Environment.

Do these Actions have the Desired Effects?

Did we make efficient use of our Resources?

How efficiently can we manage our Environment?  What is it like day-to-day operating what we have built?

{{ break }}

With the above sequence and prose description of that sequence, we have a starting place to understand what Engineering is.  It's something we do, it's something that produces results we may or may not want.  It changes things.

These are all things that can be said to describe Engineering, and shine lights on it's different surfaces, which show different things to different people, coming from different viewpoints.

Engineering is multi-faceted to an amazing degree, so we will have to describe it repeatedly in vague terms to cloak it in an overall shape that provides better understanding.

Like Local vs Global Alignment, Engineering can be understood in a small or shallow manner well Locally, but when compared against other descriptions which are equally accurate, they do not seem to Align well.

It is only through creating many Local descriptions which Align well, and combine together into a Global network of descriptions which all Align well, that we can create a real understanding of what Engineering is.

What does Engineering mean to you?

How would you summarize it in a sentence, as I have?  How does your summary differ from mine?  What advantages do you see in your summary over mine?  Can you make a denser and more correct description?  

Brevity allows for a type of clarity which details do not provide, as details allow for a type of clarity which brevity does not provide.  They are the extremes of the scale of all valid information.

Feel free to share your personal summaries with me, I am happy to hear how others view things, and expand my own understanding accordingly.

3.5.1: The Use of Resources
---------------------------

For our purposes, Resources can be summarized to the short list of:

- Overall Time
- Personnel Time
- Money
- Hardware

Overall Time is like calendar time.  Things can take hours, or a month, or the month of March goes by, or something is a quarter of a year.  This is all "overall" time.  It speaks to time passing, which you cannot do-over, making it a limited resource.  This is heavily tied to Money, which is why the saying "Time is money" has a logical truth to it, since salaries, rent and loans must all be paid at distinct time periods, so this is a very important concept for organizations.

Personnel Time is the time that any given person has to perform work.  For instance, in an example job an engineer may have 40 hours of time to potentially perform work in a week.  Over a month that is 160 hours of potential time.  This is also a limited resource, and while organizations can make this flexible by paying more (hourly/bonuses/etc) or by asking for the person to simply give more time (unpaid overtime/death marches/etc), it still mostly remains a very limited resource.

Money is obviously a limited resource as it is a scalar/number.  At any time an organization will have a value for available capital, and another value of available credit, and potentially options for creating more capital (sales/etc) or credit (new lines/etc).  These are all limited resources, and running out of money is almost exclusively the only reason organizations cease to exist, or are otherwise "abandoned".

Hardware is essentially a "platform" for performing work.  We can lump buildings, facilities, hardware-infrastructure, and all other kinds of things into this that are essentially "things we buy/rent with money, that we then 'own' and have to manage".

Apart from these things there are of course other categories, such as Software that we buy (like Hardware), but these days you can run your entire organization on Free Open Source Software (FOSS) and many companies do just that, operating as well or better than those who pay for software.  So, Software is fairly subjective in terms of being a resource like Hardware, as without Hardware we do not have any place to run FOSS or commercial software, and so we cannot operate.

Additionally, engineering companies often create their own software, and this is required for managing your own operational environments, as there will be somethings that are unique about your organization, even if you try to make it as generic as possible, from the software-infrastructure side of things.  

Finally, even commercial software requires configuration, troubleshooting, maintenance, etc, so in comparison with do-it-yourself style software, the difference is only in Personnel Time and Money, and it may well be cheaper to do it either way, depending on your unique situation and goals.

How you use resources will determine the efficiency in the interactions between them, and the overall level of quality and quantity of work that you can perform, which will impact the success of your goals, and the success of your organization.

Using resources efficiently is of prime importance for any Engineer.

3.5.1.1: Evaluate the environment.  Know the present.  Real vs. Virtual.
------------------------------------------------------------------------

Do you remember the term "Knowability", which I introduced towards the beginning of the book?

If not, please refresh your memory quickly here:  {{ section__knowability }}

In order to make efficient use of our resources, we must understand our resources, in as much depth as possible, in as many categories as possible, for our given cost-benefit requirements, to meet our goals.  So, we want to know "almost everything about everything", while trying to minimize that into as few things as possible, because keeping track of more things is more work than keeping track of less things, and so is less efficient.

The most important thing to know about our Environment is the "Present State".  This is the current state of affairs, for everything, as it actually is.  Reality.

When we previously inspected Knowability, as a concept, we stated that "reality is not truly knowable", because there is so much about any physical thing that we simply cannot measure, and we run everything on Hardware, which is a physical thing.

So, what we have left is what we can measure, and with these things we will attempt to "know the present".

Knowing the "past" is as simple as having snapshots of your "present" still available after time.  So any data that is Versioned, or stored in a Time Series, can be used to compared against the Present or other Past Snapshots.

We can think of any of these time slices, or moments-in-time, as a "Snapshot" of all the data of our Environment.  With all these data points from "now" and the past, we can understand where we came from and where we are.

We can further extrapolate, by various statistical means, projections of how things will be over time.  Some things we extrapolate are valid, and useful information.  Other things we can extrapolate, but they are actually invalid, in that while the mathematics used to calculate them may be valid, the application of that processing against the given data set, for our desired results is not a valid combination.  

This is important to know, as you can predict somethings, such as "How many hard disks do we expect to fail next month?", but you cannot predict other things such as "Will this specific hard drive in this specific machine, fail next month?".  No amount of statistical analysis can answer a useful boolean value there, and a non-boolean result is not something you can reliably make a decision on in that case.

For example, for a given machine and hard disk device, will knowing it's manufacturing lot number, with the known MTBFs (Mean Time Between Failures), and the lifespan of the system, and the usage of the disk (IOPS over time), be able to determine if you must replace that exact hard disk device, in the next month?

No.  That specific hard disk device could fail in the next second, or could last another 5 years, you cannot give a valid actionable answer to this question.

However, if we restate the question as, "How many disks do I need to have in stock, in order to replace the number of disks in all of my systems that are likely to fail in the next month?"

This is a very different question, because it deals with a population of disk devices, not a single disk device.  Across a population this statistical analysis becomes valid, and it will remain statistically-true, as long as the numbers you give it are accurate and correlate properly, which becomes more true as the population size increases, and as you can improve correlating relationships.

So, with the Physical hardware and other Real things, we cannot know everything, but with Virtual things, Data and Logic, we can know everything.

We can gather the exact values for each of the things we wish to know, and we can store them exactly as how they live in the real world, or can digest them so that we store a reference or as a reference count, or we can do anything else we want with them, because they are Virtual, we can know them completely.

And, since we are also inspecting the Physical things with Logic, which is Virtual, we only data Virtual output (Data) from our Logic, so all we know are Virtual things, not Real physical things.  We can use the virtual knowledge to extrapolate about the physical knowledge we cannot reach directly.

On the Knowability spectrum, Virtual information is Knowable at 1.0: Completely Knowable.

An important note about "now".  You can never know things in the truly "Now" state, because all information arrives to you in a delayed fashion.  It took time for the information to travel from it's source, to you.  Whether this is via network packets, visible light, vibration, or any other method of information propagation, it has a delay before arrival.

In terms of Monitoring, this means that all time series collected data, and other collected data, is aged.  It has an age that is older than 0 seconds, in which that information was "accurate-as-of-Now", but the "now" that you are looking at is actually aged information.

The only requirement is that this information is "new enough" to be considered "now", but it is never truly "Now" that you are looking at.  This is important to keep in mind, since different decisions require a different level of "freshness" of data, to be a decision made from valid data.

Thought experiment: What do you currently know about your own environment?  What don't you know?  What did you think you knew before you read this, but changed your mind as you read?

How can you use this perspective to improve your efficient use of your resources?

3.5.1.2: Modeling
-----------------

To create a Model of something, is to try to "map" it some way.  Models can be made in any way you can think of, but typical models are things like:

- Data Schemas: such as in a relational database.
- Graphs: nodes and edges which define a sort of topology.
- Flow Charts, State Machines, Entity Relationship Maps, and other process diagrams.

Each type of Model is meant to provide the ability to simulate something, such as your Operational Environment.  

If you were to Model your Operational Environment with each method you could, some of the data would overlap between model-types, and some of the data would be unique per model-type.

Out all of these, the most fundamental type of modeling is the Data Schema model, and the Relational data schema model is the most comprehensive way to model this data.

This is because all data can be describes as collections of fields (tables), with relationships between them (inter-table field constraints).  Graphs, flow charts, and all other types of models can be described textually through a schema, and these schemas can be put into databases such as MySQL, PostgreSQL, Oracle, sqlite, etc.

Once a relational schema is created, for the clearest expression of the schema, then the schema can be "de-normalized" and otherwise "un-spun" so that it can fit into non-relational databases, such as column-oriented or time series databases.  These databases have advantages for some access patterns (such as mostly-inserting data), but their schema is less expressive due to this optimization, so it is best to first understand it's model through a relational schema.

Relational schemas can also be written as programming language "structs", or data primitives, and extended into Classes (Object Oriented style "structs").  This may seem like looking at things in a skewed way, but you can look at these data structures from any direction to get a better understanding of them.

There are two primary reasons to create Models:

- Creating Models to better understand a topic.
- Creating Models to control a set of resources.

Models made for learning are about providing insight, and different ways of looking at data, and are beyond being documentation are generally disposable, ephemeral, and prone to becoming out of date.

For a given Environment, a Model can provide understanding, through creating a summary of the system trying to be understood.  A model like this can be given variables and used to calculate probabilities, and perform analysis to aide in making decisions.

This is a very different thing from a Model that is created in order to control resources.

A Model created to control resources will share many things with Models made for understanding, in that it is also a summary of the system, but unlike a Model for understanding, a Model for control is built to last potentially for the lifetime of the resources and beyond.

Models for control are intended to make operating an Environment better by allowing inspection of state and control through the model.  A Control Model must be absolutely accurate, and have highly synchronized coordination with the Environment itself, or it risks becoming out-of-sync, and unable to Control the Environment.

In contrast, a Model for understanding does not need to be highly synchronized, or absolutely accurate, because it only needs to be "good enough" to provide the required insight.  More accurate and more synchronization can assist in providing better accuracy, but less accuracy might be sufficient depending on your goals for better understanding.

Creating Models for understanding has a lot of documentation that already exists about it, and there are many mature areas of study that currently exist for this.

Creating Models for control does have some good examples in the wild, and some that are taught in mature areas of study, but I am of the opinion that we still do not have much documentation in this area, so I will do my best to describe how I do this effectively, quickly, and how I get good results every time.

Modeling is a core skill in Engineering, so if you do not already consider yourself a proficient modeler, you should take any attempt to start creating more models when opportunities arise, as practice improves all skills.

3.5.1.2.1: Black-Boxing the World
---------------------------------

Once we accept that anything can be modeled, then we can go about modeling everything that is useful.  We can model for Understanding, but it is better to model for Control, since you get both.

Remember the introduction to Pragmatism?  If not, check here:  {{ section__pragmatism }}

Using Pragmatism, we can evaluate anything on only the effects that they cause.  These effects can be turned into schema, as can any additional data needed to model the effects.

When modeling for Operations, there are 2 main areas of modeling:

- Model Reality: Describe what exists.
- Model Effects: Describe what happens.

We'll cover these in detail later as we go over the OpsDB, which is all about doing both of these things.

Remember the "Universal Machine" concept?  If not, check here:  {{ section_um }}

Universal Machines map Inputs, Outputs and Side-Effects, which is just a more explicit version of a Function, which maps Inputs and Outputs, and may perform Side-Effects, but does not explicitly model them for Control purposes.

Using modeling, by way of Pragmatism, through the Universal Machine interface, we can model anything and everything.  We can Black-Box the World, or wrap the world full of "black boxes", which contain something that has the signature of the Universal Machine (Input/Output/Side-Effects).

Later, I will go over how to actually do this, but for now I just wanted to point out what our currently defined terminology and tools allow us to do, which is quite a lot.

3.5.1.3: Algorithms
-------------------

There are lots of important Algorithms in Engineering, they are Virtual and are frequently constrained to these types of things:

- Searching for data: Finding things based on some matching criteria
- Sorting data: Ordering data based on some sorting criteria
- Coordination: Locking, reference counting, signaling other coordination style actions
- Encoding/Decoding: Encryption, compression, encapsulation, and other wrap/unwrap style actions

There are other categories as well, but these are often what we think of in Operational Engineering when someone says "algorithms".

There are many good references for these, including Wikipedia or Donald Knuth's books, for a completely in-depth comparison between an encyclopedia of algorithms.

In terms of Operations, while we use these other algorithms, I will focusing on "Algorithmic Properties" and very fundamental Algorithms.

One important "Algorithmic Property" is Idempotency.  This means that when you apply an Algorithm with this Property that the result is always the same.  In simple mathematics this can be seen by "1 * 1 = 1".  "* 1" is the Algorithm, and the result is always the same as the same as the original value (1 == 1).

This has interesting mathematical uses, but in Operational Engineering, the use is that if we perform a function, we always have the same result.

Consider a Algorithm that ensures that a directory exits with a given set of permissions.

Let's say that this will be the input data for this Algorithm, in YAML format:

{{{ code_begin }}}
type: ensure_directory_exists
path: /Users/ghowland/projects/OpsEngAuto/sections
mode: 755
user: ghowland
group: staff
{{{ code_end }}}

When the function that executes this Algorithm runs against this data it will ensure that a directory like this is created, if it doesn't exist:

{{{ code_begin }}}
$ ls -ld sections
drwxr-xr-x  346 ghowland  staff  11764 Aug 23 00:48 sections
{{{ code_end }}}

If the directory does exist, then it ensures that the mode, user and group are correct.

At the end of the function running, we always have this directory, with the correct mode, user and group permissions.

This is a basic example of what Idempotency can mean in a Operational Engineering environment.  This property can be used in many places to ensure that we always get a single result, without conditional changes.  It either works, and we get what we expect, or it fails and we know there is a problem (such as lack of permissions to make the changes).  These are both desirable states, because both success and failure meet the Idempotent criteria we set forth.

In comparison to an Algorithmic Property is an Algorithm, such as "Iterating Over a Sequence".

We could combine the previous example with this, to create Logic that will ensure a number of directories exist.

For example, consider this YAML data that lists YAML paths for our above ensure_directory_exists function:

{{{ code_begin }}}
ensure_directory_exists:
  - /Users/ghowland/projects/idempotent/dirs/OpsEngAuto_sections.yaml
  - /Users/ghowland/projects/idempotent/dirs/OpsEngAuto_toc_backups.yaml
  - /Users/ghowland/projects/idempotent/dirs/something_else.yaml
{{{ code_end }}}

If we wrote some Python like this, we can iterate (go over each item in the list) like this:

{{{ code_begin }}}
directory_data = LoadYaml('/path/to/ensure_directory_exists.yaml')
paths = directory_data['ensure_directory_exists']
for path in paths:
  dir_data = LoadYaml(path)
  EnsureDirectoryExistsIdempotentFunction(dir_data)
{{{ code_end }}}

This code assumes a LoadYaml() and EnsureDirectoryExistsIdempotentFunction() exist for convenience, and do what they say they do.  This will iterate over our list of YAML files that contain our directory data, to Idempotently ensure exist.

Over the course of the coming chapters we will introduce many Algorithmic Properties which give us good results in Operations, and we will compare when to use them, and how to use them efficiently.

3.5.1.4: Centralized vs. Decentralized
--------------------------------------

TODO:  Push vs Pull, when is it centralized?  Do you want tight control, or loose control?  Both have their effects.  People typically want tight control, or the effects of tight control (knowledge that it worked).

3.5.1.5: Distributed Systems
----------------------------

3.5.1.6: Distributed Data
-------------------------

3.5.1.7: Hardware: Fixed vs. Utility vs. Cloud
----------------------------------------------

3.5.1.7.1: Fixed Hardware
-------------------------

3.5.1.7.2: Utility Hardware
---------------------------

3.5.1.7.3: Cloud Hardware
-------------------------

3.5.1.7.3.1: *aaS
-----------------

Everything as a Service.

3.5.1.7.4: What do you have to care about?
------------------------------------------

3.5.1.8: Types of Complexity
----------------------------

There are a number of different kinds of complexity that we have to cope with while performing Engineering tasks.  Let's enumerate them so we can refer to them explicitly, instead of clumping them all together as "complexity" or having to describe them each time.

Each of these types of complexity also represent a spectrum or axis, as we only think of complexity as something heads toward 1.0, while things closer to 0.0 on the axis are seen as simple.

This means that any issue can be evaluated on all types of complexity, to get a better understanding of it's total "complexity shape".

- Large-scale Complexity
- Detail Complexity

3.6: Code management
--------------------

3.7: Perfect is the enemy of done
---------------------------------

3.7.1: Quality is Never #1; Utility is Always #1
------------------------------------------------

3.7.2: Security Is Also Not #1
------------------------------

3.8: Troubleshooting
--------------------

3.8.1: Monitoring
-----------------

3.8.2: Spectrums
----------------

3.8.2.1: Comparisons
--------------------

3.9: Skill Ladders
------------------

3.9.1: Graphing Skills
----------------------

3.9.2: Understanding Your Own Ladder
------------------------------------

3.10: When to use Statistics
----------------------------



When I started this book I made some statistical counters, which are sections, words and lines written.

I estimated from about 280 sections off of my first 10 sections written, that I would have about 208,000 words at the end of the book.

I have been checking my percentage complete, such as currently:

"""
 Total Sections: 301 Populated Sections: 54 Current Goal: Populate Empty Sections: 247 (Done: 17.9%)

Lines: 2197

Words: 37668
"""

And the sections and word percentages to completion have almost kept perfect alignment the entire time I have been writing this work.

Yesterday was:

>>> 33000 / 200000.
0.165

And today (with the above quote):

>>> 37600 / 200000.
0.188

18.8% word vs 17.9% sections, in terms of estimated complete.

Additionally I have been adding sections and removing them as I see fit.  Im not trying to match this data up, and Im not trying to count words in my sections, I just write what seems to fill the topic section, and move on.

And yet the percentage complete to my initial rough-calculation of 208,000 words, remaining in-line with the number of sections I have.  I will do an analysis on this from my Github entries, since all of this is in version control once the book is done.

This is a topic that apparently works very well with statistical analysis, and the results are "amazingly accurate" as a study of the population of words and sections I write over time.

Apparently there is some kind of statistical slant I have to writing a certain number of words a day, a certain number of sections a day, and so on.

3.10.1: Across many things: Appliable
-------------------------------------

3.10.2: For a given thing: Not Applicable
-----------------------------------------

3.10.3: Exercises
-----------------

3.11: How to Select Tools
-------------------------

3.11.1: Many stand alone tools will end up being replaced
---------------------------------------------------------

3.11.1.1: Text and data and the purpose of the tools
----------------------------------------------------

3.11.1.2: Explain Replacement of DNS, DHCP, etc
-----------------------------------------------

3.11.1.2.1: Zones, Subnets, etc
-------------------------------

3.12: Name spaces
-----------------

3.13: Structure as Logic
------------------------

Explain how I use schema and other structures in place of Logic, reducing the total amount of Logic, and making the gap between working features and Logic-creation much smaller.

How this scales better than not doing this, writing everything as Logic without help from Structure.

Structure is Efficient Alignment, in practice.

Chapter 4: Automation Philosophy and Methodology in Operations
==============================================================







4.1: ***** Removing classes of work.
------------------------------------

4.1.1: Manual automation is a force multiplier.  Mistakes are also multipled.  Unintended consequences can be severe and wide-spread.
-------------------------------------------------------------------------------------------------------------------------------------

4.1.2: Making people do more complicated and dangerous activtiies should not be an end-goal of automation, though it will likely be an intermediary step.
---------------------------------------------------------------------------------------------------------------------------------------------------------

4.1.2.1: Step with caution.
---------------------------

4.2: Introduce spectrum of automatability.  How automateable is something in configure X vs Y?  This is automatability.
-----------------------------------------------------------------------------------------------------------------------

4.3: Working with N axis data for evaluation of properties.  Properties are scalar, but there are many dimensions to measure, and collectively they are near-infinite.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

4.3.1: Tuning your goals based on your methods.
-----------------------------------------------

4.3.2: How to create your own Axioms.  Some standard axioms.  Axiomatic development.
------------------------------------------------------------------------------------

4.3.3: Tools to fit the job.  Testing in an operational environment.  Mock-tests, etc in a world of only side effects.  Using Vagrant and VMs to test allows these side-effects to be tested, but take time to set up.  Worth it, but you may not start there in a live environment because of all the legacy that would have to be replicated and is changing all the time in non-standard ways.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4.3.4: How to standardize things.  Simplification.  The benefits and limitations.  Simpler means less options at any given time.  1-1 work is infinite precision and difficult to scale.  Simpler is can be deep precision in 1 or several ways, but does not allow all options.  Build your option matrix out of what you need, ensure all your use cases are covered.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4.4: All processes can be automated to get a desired effect, if enough information about it is known.
-----------------------------------------------------------------------------------------------------

4.5: Introduce Intelligence.  Actionable Intelligence.
------------------------------------------------------

4.6: Automating anything
------------------------

4.6.1: Pre-Solving Problems
---------------------------

What are we doing when we automate?

We are pre-solving problems.

If we did not automate a solution, we would need to show up (as a human), and see what needs to be done, and then do it.

When we pre-solve a problem, we are figuring out in advance how to detect a problem, how to "see it" with monitoring data collection, and creating troubleshooting logic (testing the environment) to determine how to solve a given set of problems.

If we are comprehensive about describing which problems can occur, and we are comprehensive about what states the problems may contain, it is possible to Black Box an entire set of problems so that they can be solved with Logic instead of Humans.

This is what makes the elimination of Classes of Work possible.

Through understanding our environments and using systemic thinking and the Slicing The Pie technique to ensure we have comprehensive coverage of anything we are looking at, we can pre-solve problems by going through all their states.

In testing our solutions, we will find mistakes and incorrect assumptions we have made, and over time Reality will inform us of additional mistakes, incorrect assumptions and also contexts we were not aware of, or did not prioritize.

As these new areas are added to our awareness, and we prioritize them we will continue to slice the pie into more sections which allow us to cope with these problems and pre-solve them as well.

4.7: Total elimination of manual work.  How to remove classes of work from being necessary.
-------------------------------------------------------------------------------------------

4.8: Building the data and action chains, to create all workflow.
-----------------------------------------------------------------

4.9: The data requirements:  Authentication, Authorization, Versioning, Change Management, Deployment, Pre-Post Deployment Actions, Schema Management
-----------------------------------------------------------------------------------------------------------------------------------------------------

4.10: How to construct an unbreakable process.  How to stop that process from being completed/sealed, so that it breaks.  How to ensure it breaks all the time, by setting conditions accordingly.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4.10.1: Faux-automation.  Manual automation.  Automation-assist.  Full-automation.  Comprehensive Life-Cycle automation.
------------------------------------------------------------------------------------------------------------------------

4.10.2: This can be started as Procedure for Humans, but it will not be unbreakable, as people will make mistakes entering data (running commands is entering data)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

4.10.2.1: Entered on the right system?  Right command?  Right args?  Right path?  Right data?  Right goal?  Right everything?
-----------------------------------------------------------------------------------------------------------------------------

4.11: Flexibility and dangers of an automation system.
------------------------------------------------------

4.12: Distributed OS.  DOS.  N units, all being controlled, configured and scheduling work.
-------------------------------------------------------------------------------------------

4.12.1: Does not need a "traditional" cluster scheduler.  Can use these these for "cron" type jobs though.
----------------------------------------------------------------------------------------------------------

4.13: Monitoring is the heart of automation.  You cant control what you dont have info on.
------------------------------------------------------------------------------------------

4.13.1: Instelligence:  Actionable?  Timely?  Relevant?  Correct?  (Cross check it, all must align)
---------------------------------------------------------------------------------------------------

4.14: Behavioral AI.  An expert system, build by experts in Ops and Biz goals.
------------------------------------------------------------------------------

4.14.1: Do not use fuzzy info until you have exhausted discrete/precise info.  And turn the fuzzy info into a discrete/precise data point, so it can be acted on cleanly by logic.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4.14.2: N of M failures is not fuzzy, even though it has a scalar value, and not boolean.
-----------------------------------------------------------------------------------------

4.15: 3 States:  Now, Desired, Current State (Whats Out there?)
---------------------------------------------------------------

4.15.1: How to manage.  Importing, synthesizing, checking.
----------------------------------------------------------

4.15.2: Versioning, commits, pre/post-commit logic.
---------------------------------------------------

4.16: Agent model.  Centralized model.
--------------------------------------

4.17: Library model.  RPC model.  Framework model.
--------------------------------------------------

4.18: ORM vs wrapping lib vs straight SQL/data query.
-----------------------------------------------------

4.19: Scales,  1000s/millions, not billions.  Can make this "configuration scale" not "production deployment end-user scale".  Optimize only when necessary, use tools that do heavy lifting for Time series data analysis, and import results and last N snippets into OpsDB.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4.20: Selective Data Updating for Pyramid method and Mesh method.
-----------------------------------------------------------------

4.21: Compare Pyramid vs Mesh (p2p).  Pros and cons.
----------------------------------------------------

4.22: Introduce the dotted notation as a universal naming convention, for lookups, it can universally address any type of DAG data:   domain.sub.thing.11.field.subfield.11.arrayfield.20.subsubfield
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4.22.1: **** Use this DAG lookup to go into YAML, DBs, etc.  Schema Man can allow this.  Can use sub-searches like globs (domain.thing.*.field) and translate that into SQL or whatever for more advanced usage.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 5: Components of Engineering
====================================


In previous sections on Engineering I went over the philosophy and balance of engineering, and now I will break things into distinct components that we deal with, how they are related to each other, and how they fit into the overall toolbox of Engineering.






5.1: Requirements
-----------------

5.2: Resources
--------------

5.3: Goals
----------

5.4: Logic
----------

5.5: Environments
-----------------

5.6: Processes
--------------

5.6.1: Adding Features
----------------------

5.6.2: Fixing Bugs
------------------

5.6.3: Improving Efficiency
---------------------------

5.6.4: Performing Maintenance
-----------------------------

5.6.5: Designing a New Version of a System
------------------------------------------

5.6.6: Replacing a System
-------------------------

5.6.7: Depricating a System
---------------------------

Chapter 6: Components of Operational Environments
=================================================







6.1: Troubleshooting
--------------------

Chapter 7: Components of Automation Environments
================================================







7.1: The process of building this system in your organization.
--------------------------------------------------------------

7.1.1: Collect all unique data in one place.  Ensure it is accurate by checking against reality, and combing through it manually to see if things line up, spot checking and automation checking every one by script.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

7.1.2: Things that are unique to you, vs things that are general to everyone.
-----------------------------------------------------------------------------

7.1.2.1: FQDNs, IPs, HW specs, OS specs, configuration variables, specific workflow and stuff.
----------------------------------------------------------------------------------------------

7.2: Imaging vs re-building from scratch
----------------------------------------

7.2.1: Correctness, up-to-date, vs speed.
-----------------------------------------

7.3: *** The Progression of an Automation System:  Walk through all the stages **
---------------------------------------------------------------------------------

7.3.1: These shouldnt be an order so much, as people can take different routes.   How to evaluate each of these spectrums/axis of data, scalars, would be good.
---------------------------------------------------------------------------------------------------------------------------------------------------------------

7.3.2: Manual everything
------------------------

7.3.3: Kickstarts and auto config  (AWS gets you here)
------------------------------------------------------

7.3.4: Sys configuration tools, Monitoring, Centralized Logging, etc.  Normal sys admin process.
------------------------------------------------------------------------------------------------

7.3.5: Issue tracking systems, change management ticket systems.
----------------------------------------------------------------

7.3.5.1: Good to have different CMS for tickets, because your ops logic will change, but its more useful to track the CMS data right in the ops db for a real record of things, because it lists the complete workloads.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

7.3.6: Databases for assets, inventory, etc
-------------------------------------------

7.4: * The more sources of authoritative data, the more data drift and non-alignment between the data (fields tracking similar but non-matching things, naming differences, not able to point to same primary keys, etc)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

7.5: Data survives longer than code/logic, business logic stays all the time, but the assets described in the DB remain the same, even if they are used differently, and different meta-data is stored about them.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 8: The OpsDB
====================







8.1: What is it?
----------------

8.1.1: Your OpsDB is the desires and actionable knowledge of your company.  Everything inside it can be acted upon, it is better global information than any single person can have, so it is the best communication mechanism for a system that has multiple people with their own information (all companies over 1 employee).  Synchronizes information, makes transactional.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.1.2: Setting realistic expectations for this project will be one of your biggest challenges.  Once the premise is understood, it is difficult to stop "magical" thinking about the project, as the intention is to solve all solvable problems, people see it as a magic machine.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.1.3: It is a system or "machine" that can be used to solve all problems, in that it is a centralized database and method for acting against that data.  That is immediately a universal set of tools, because every piece of software is data with a method for acting against it.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.2: Data Driven Design:  My methodology.  Start with the data, work from there.  Testing against data is key.
--------------------------------------------------------------------------------------------------------------

8.2.1: Separate data changing logic from non-data changing logic.  This is like the Model/Controller separation, but is different because it is about any type of action, not just GUI-like actions.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.2.2: Work systems.  Distributed Job schedulers.
-------------------------------------------------

8.2.3: Collection of data:  Events (logs/etc), Time Series, Config State (md5sum, etc), Active/Live State (up/down)
-------------------------------------------------------------------------------------------------------------------

8.2.4: Data Driven Development.  My methodology.
------------------------------------------------

8.2.4.1: Start with data.  Fo over all features as represented in data.
-----------------------------------------------------------------------

8.3: The Data (base)
--------------------

8.3.1: Modeling off of reality.  Logical ideas change all the time, business decisions and directions change all the time, staff changes regularly, reality will hold true, but it's perceived differently by everyone.  Still trying to map to reality gives the most common information to the most people who will work with it, and a common method of communication, and is therefore better than not.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.4: Naming conventions.  Set them and try to abide by them consistently.  This will determine how frequently things must be looked up to be used, for someone familiar with the sytem.  Python vs PHP.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.5: My rules:  No plurals in data (code is ok), strict lookup methods, limit methods of relationality.  DAG lookups, with normalized relations in data (not-DAG, has cycles, data doesnt have a direction when there are cycles, the search could start anywhere).
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.6: What tools you will need to manage this data.   Problems with ORM, problems with non-ORMs.  The tools chosen will determine the level of automatability.
-------------------------------------------------------------------------------------------------------------------------------------------------------------

8.7: Building the logic system.
-------------------------------

8.7.1: Ensuring uniqueness of elements that require guarantees.
---------------------------------------------------------------

8.7.2: Infrastructure.  Pre-Services.
-------------------------------------

8.7.3: Configuration of Services.
---------------------------------

8.7.4: Monitoring of Services.
------------------------------

8.7.5: Life-Cycle Management of services.
-----------------------------------------

8.8: The layers of an automation system:
----------------------------------------

8.8.1: Description of environment
---------------------------------

8.8.2: Provisioning
-------------------

8.8.2.1: One-Time configuration
-------------------------------

8.8.2.2: Continuous Configuration
---------------------------------

8.8.2.3: State management
-------------------------

8.8.2.4: One-time actions (manual state control of distributed systems)
-----------------------------------------------------------------------

8.8.2.5: Maintenance actions (taking offline)
---------------------------------------------

8.8.2.6: Marking broken HW, fixing HW, migrating OS positions.
--------------------------------------------------------------

8.8.2.7: What stays the same, what changes?  IPs for LOM on HW.  IPs for OSes on virtual.
-----------------------------------------------------------------------------------------

8.8.2.8: Tracking N things.  Primaries vs. position.  Ordered lists are the best?
---------------------------------------------------------------------------------

8.9: How to "translate" data changes, making many changes at once, like matrix multiplication.  Changing from Puppet to Salt, etc.
----------------------------------------------------------------------------------------------------------------------------------

8.10: How to Build your own OpsDB.  What you need:
--------------------------------------------------

8.10.1: View (Webpage, API)
---------------------------

8.10.2: DB Backend
------------------

8.10.2.1: Method for safely making changes to data
--------------------------------------------------

8.10.2.1.1: Versioning, Change Management
-----------------------------------------

8.10.2.1.1.1: Roll backs
------------------------

8.10.2.1.1.2: Pre-Post Commits
------------------------------

8.10.2.1.1.3: Locking, to stop problematic race conditions
----------------------------------------------------------

8.10.2.1.1.3.1: Channeled locking, to limit domains of locks
------------------------------------------------------------

8.10.2.1.1.3.1.1: Size of domain, and rate of change and lock duration determine requirements
---------------------------------------------------------------------------------------------

8.10.2.1.2: Single choke point for DB changes
---------------------------------------------

8.10.2.1.2.1: Web/API all use the same code, so different paths give different results.
---------------------------------------------------------------------------------------

8.10.2.1.2.2: Role users (scripts) can auto-commit changes, but should go through same process, because needed for auditing, troubleshooting, and maintaining integrity and pre/post-commit logic
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.10.3: Pull method, to gather data.  Time Series, Logs, State/Configs, Events, etc
-----------------------------------------------------------------------------------

8.10.3.1: Creates Global Authority DB
-------------------------------------

8.10.3.1.1: Can be distributed, if sync. is strong
--------------------------------------------------

8.10.3.1.1.1: Need Transactions on all pieces of total DB, so that things are changed in block fastion, all this way, then all that way.  Keeping alignment.  (Like a shot in Pool, game.  Stick and balls must line up to make it into the pocket.)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.10.3.1.1.2: Will come later in the process, in the "How to implement" section
-------------------------------------------------------------------------------

8.10.3.1.2: Selective Replication.  Will have local and global portions.   Easy to separate instances (2 MySQL instances) so taht there is a Global DB (replicated from Master) and a Local DB, pulled from Local, which replicates to Master.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.10.3.1.2.1: In this scenario, the Master will need to have N instances, where N is the number of sub-masters, so it can replicate.  Then it will pull and integrate this data into it's own global system, and then synthesize.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.10.3.1.2.1.1: This Global pull-integrate-synthesize is then replicated out everywhere, and is the REAL data that can be acted upon.  It has met all constraints and has a view into everything
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.10.3.1.2.1.1.1: Some Logic can run off of Local data, because it is locally concerned.  When Logic needs to act on Global data, its obvious it needs to be correct and current global data.  Intelligence.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.10.3.1.2.2: Collection is local.  Work from Global.
-----------------------------------------------------

8.10.3.1.2.2.1: How to work on partitioon?
------------------------------------------

8.10.3.1.2.2.1.1: Can use local data for N time, until is stale.  Logic can decide how stale the data can be, can have Rules for lag time allowances.
-----------------------------------------------------------------------------------------------------------------------------------------------------

8.10.4: Orchestration.  Remote Execution.  Seall the loop and check.  Post-Provisioning will need to run commands to check that things really worked.  Same as any other type of action. Do the action, get the result, but then go check and make sure it worked.  Check again to see if it failed after some time.  Ensure another action hasnt caused this (acted on the same Resource)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.10.5: Config Management.  Make known changes on a system.  It should be in "X state"
--------------------------------------------------------------------------------------

8.10.6: State Management.
-------------------------

8.10.6.1: OS Level
------------------

8.10.6.2: Service level (dealing with the execution of services, and proper functionoining of the service)
----------------------------------------------------------------------------------------------------------

8.10.6.3: Running-Service level (dealing with things inside a running service.  This is a user of the service, instead of a controller, but it is an "administrative" type of use)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.10.7: Work Scheduling
-----------------------

8.10.7.1: Global cron jobs, etc.
--------------------------------

8.10.7.1.1: In maint?  Is right machine (master/slave/role/etc)?  Dont take down prod.
--------------------------------------------------------------------------------------

8.10.7.1.2: Dont ignore failures of jobs.  Keep logs for auditing, so we know what happened, and what it happened for troubleshooting and Root Cause Analysis.
--------------------------------------------------------------------------------------------------------------------------------------------------------------

8.10.7.1.3: Track times for analysis to determine failures of scale-performance changes
---------------------------------------------------------------------------------------

8.10.8: Capacity Planning.  When will you run out of:  Disk? RAM?  CPU? Connections?  etc
-----------------------------------------------------------------------------------------

8.10.8.1: Resources of our services.  Network Loadbalancer has N potential connections, and we can determine that by a MAX check on how much its done, and where it has produced failures after MAX_WORKING values have been breached.  Might not be the LB though, just correlation.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.10.9: Access Control.  Authorization to do work.
--------------------------------------------------

8.10.10: Security zones
-----------------------

8.10.10.1: Environments and Security Zones
------------------------------------------


Environments are natural Security Zones, because we have a goal in mind for everything inside an Environment, so everything has a similar base set of Security Requirements, and therefore a Security Posture that is required.

8.10.10.2: Tiered Security Zones
--------------------------------

Let's make a map of what tiers we could have in security zones.

- Tier 1: Member of the organization.  Employee or outsider?

The first tier will simply be a boolean of whether a person is a member of the organization in question.  "Do you work for us?"

This is a basic question of insider vs. outsider.  This tier can have additional children tiers for all departments and groups in an organization, as wall as professional rank, such as Vice President (VP) vs. Engineer will be two different levels of tiered security in the employee category.

This has blurred lines for Contractors, Consultants, Vendors and Partners.

Contractors are paid as work-for-hire "employees", without the employee benefits.  This is usually focused on individuals that are contracted for work, but sometimes is a separate organization who is contracted (usually for lower level work, or non-core services).  Contractors will usually have similar access to employees at their same level, with perhaps some additional restrictions to making changes or seeing sensitive information.

Consultants are short-term or contracted for specific work, and often for informational work, rather than manual labor type work (including technical manual labor, like writing code in this).  Consultants are often given very limited access to a company's data and resources, as they have a specific task to perform which does not need general employee-level access.

Vendors are organizations who sell software, hardware or services to an organization, and are not associated with any individuals.  Vendors are generally not given any access to data or resources, except in the case of special technical support investigations, which are rare and may still not be allowed by organizations who are serious about security.

Partners are a mix between contractors, consultants and vendors.  They may be a Vendor, which is making a co-sponsored project with your organization, and so they need limited access to all relevant project data and may need resource access to test integration.  Partner employees may be given contractor or consultant level access, depending on the partnership goals and time lines.

- Tier 2: Environment level.  Production, staging, QA, development?

This is a statement of a basic operational environment.  Where are you?  What are you allowed to do here?

Described thoroughly here: {{ section_10c0b236af1081d0c601a87fb274211c }}

- Tier 3: Location level.  Specific datacenter in a Tier 2 environment.

Inside of a Production Environment, you might be in Data Center #1, which may have some different rules from Data Center #2, because the build-outs were done at different times, or different resources are located in each of them.

- Tier 4: Resource level.

Inside of a Tier 2 environment (and maybe Tier 3), there will be special resources, such as a database that stores Personal Identification Information (PII), or credit card information (PCI), etc.

For these special resources they may need additional sub-environmental security zones, such as internal DMZs (ie: "de-militarized zones", which is like a security "draw-bridge" or "fire-wall" area).  

This could also be external DMZs, which are used for services that take external requests which may be considered "more dangerous" or otherwise having a different security posture requirement, which is placed into a separate special area of the network.  This allows for example a place to put a file-server that is accessible by partners or vendors, but if compromised does not give privileged access into the Production network.

Roughly these 4 tiers break down into:

- Authentication, authorization:  "Are you one of us?"
- Operational Environment:  "What do we want to happen at this point?"
- Specific Location:  "What do we do in this location that is special?"
- Resource specific: "Is the specific resource in question special?"

8.10.10.3: Security Zones Inside Environments
---------------------------------------------

8.10.11: Deployments, as separate from Config
---------------------------------------------

8.10.11.1: Code deploy
----------------------

8.10.11.2: Data/Schema deploy
-----------------------------

8.10.11.2.1: When tied together.  Ways to avoid problems, ways to increase problems.
------------------------------------------------------------------------------------

8.10.11.2.2: Lifetimes, rate of change, etc
-------------------------------------------

8.10.11.2.3: Service up/down.  In/out of LB.  (Active)
------------------------------------------------------

8.10.12: Network config and planning
------------------------------------

8.10.12.1: VLANs.  Hidden systems, ensure not old IPs (collisions)
------------------------------------------------------------------

8.10.12.1.1: Can defer their use until that HW is proven to not use that IP anymore.  Like its in Escrow.  Once really released, it can be re-used.   Nice.
-----------------------------------------------------------------------------------------------------------------------------------------------------------

8.10.12.2: LOM IPs stay with the hardware.  DHCP timeouts, etc.  Server IPs stay with "ServerInstance" (OSInstance)
-------------------------------------------------------------------------------------------------------------------

8.10.13: VM Provisioning.  Hybrid.
----------------------------------

8.10.14: Self Service tools.
----------------------------

8.10.15: How to plan to do this in your existing environment.  A map from:  Here -> There.
------------------------------------------------------------------------------------------

8.11: States of machines:  Unknown, Unprovisioned/Spare, Provisioned-Inactive, Active, In Maintenance, Transition-To X State, Broken, Fixed (waitig to be Unprovisioned/Spare)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 9: How to Implement the OpsDB in your Current Environment
=================================================================







9.1: The OSI layer for getting things done:
-------------------------------------------

9.1.1: Physical.  Real world things.
------------------------------------

9.1.1.1: People are always required for real world things, because robots arent good enough yet.  Physical must manage physical.
--------------------------------------------------------------------------------------------------------------------------------

9.1.2: Configuration.  How real world things are configured.
------------------------------------------------------------

9.1.2.1: Logical.
-----------------

9.1.3: State.  How real world things are managed.
-------------------------------------------------

9.1.3.1: Logical.
-----------------

9.1.4: Automation.  How software can manage configuration and state.
--------------------------------------------------------------------

9.1.4.1: Automation ends where people begin.  If you have no automation, the people manage the config and state.
----------------------------------------------------------------------------------------------------------------

9.1.4.2: Automation is the control of logical devices and state.  It does not control Physical devices, but does control their state.  (Even in the case of directing a physical robot, the automation updates state, and it takes something physical (motors, servos, cogs) to make the physical thing move.)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

9.1.5: Process (and Procedures).  How people work around the lower levels.
--------------------------------------------------------------------------

9.1.6: Policy.  Dictates how processes can be implemented.  Policies may be directly contradicting Process, such as "No one is allowed to X", while a process requires a person to do exactly that.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

9.1.7: Business...  Business goals
----------------------------------

9.1.8: Political.  The realities of the business goals, determined by how well people will work together to achieve them.
-------------------------------------------------------------------------------------------------------------------------

9.1.9: Financial...  Financial reality, approved or not.  Timing.  Delays.
--------------------------------------------------------------------------

9.1.10: Legal...  Hard stop, must change direction if told by legal.
--------------------------------------------------------------------

9.2: Planning for projects in the real world
--------------------------------------------

9.2.1: The end-date comes first.  Whether you have any say in that is only occassionally true, even if you are asked how long it will take.
-------------------------------------------------------------------------------------------------------------------------------------------

9.2.2: Things will interrupt your work that were not planned for in the time estimates, and this will mean less work gets done
------------------------------------------------------------------------------------------------------------------------------

9.2.3: You will have normal duties to attend to, this will interrupt things getting done
----------------------------------------------------------------------------------------

9.2.4: Meetings.  Whether you enjoy them, are ambivalent, or dislike them, they are going to occur and take time.
-----------------------------------------------------------------------------------------------------------------

9.2.5: Mental-Context-switching cost.  Ramp up time.
----------------------------------------------------

9.2.5.1: Know what kind of work you are going to start, and pick the best time to do so.  If it needs more ramp-up time, then pick a block where you are less likely to be interrupted.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

9.2.5.2: Break your open time periods into "units" of 30 minutes or 2 hours or whatever you can have contiguously, and see what you can FINISH in that time.  It is easy to lose days/weeks to getting little changes made, but not moving ahead in terms of usable progress.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

9.2.5.2.1: When each time block arrives, try to get what you can finish, and hopefully test and put into place, in that 1 session.  This isnt possible for some work, because it's too big, so break that into stages that can fit into one of these time blocks.  A simple method, would be: write it in 1, test it in another, and finally deploy it in the 3rd.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 10: Planet Scale Automation
===================================


[Placeholder for the time being, just to briefly explain]



UM = Function + Side Effects = A method for describing any individual action



UMC = Universal Machine Context.  A label for a set of UMs.  These are actions that are all related to each other, so all UMs in a UMC can be said to be on the same "layer".



UMCR = UMC Relationship.  A mapping from either an input, output or effect, from one UMC UM to another UMC UM.  This is described *as* a UM.  The set of all UMCRs between two UMCs is itself a UMC.  The UMC of the relationship between the two UMCs.



In this way, all functions can be mapped, for any "context" or "layer", and then all contexts/layers can be mapped, and then all relationships between all contexts and layers can be mapped.



Does this need to be taken to it's extreme with a full-mesh mapping?  No.



It is only important that we have a mechanism for how to link the different layers we will eventually end up creating together under a scalable and simple system, which this is.  I believe there is probably no simpler system that can be invented to describe this set of complex relationships together, because there is a minimal set of data being tracked.



One would have to track less data, and do the same or more work to create a better effect, so I can state I believe this is currently an optimal solution for the present understanding of how we could scale to full-mesh style sizes of Planet Scale Automation.










10.1: Universal Machines as infinite recursive abstraction
----------------------------------------------------------


[Fill out...]

How this works:  

UMCs are different "Pies" in the "Slicing the Pie" concept, but they are all the same "Pie".

So you can slice the same Pie up in one UMC.

Then in another UMC you make different slices to the same pie.

This is why UMCs and UMCRs are needed, in that you still only have "One Pie", but you want to track one Set-Of-Slice from another Set-Of-Slices, and then map the relationships between all the sliced pieces and stuff.

This is obvious when you think about Planetary Scale.

We only have 1 Planet we are dealing with (for now, and then its the same thing all over, no change for Universal Scale Automation, or Multi-Versal Scale Automation), or whatever).

We have 1 Planet now, and we can slice that pie up in lots of ways.  But do we really think that a single "set" of slices will be good enough to describe automating the entire planet?

Of course not, we have so many different viewpoints on things that we will need many "contexts" into this, which is exactly what UMCs are.  They are the mappings to contexts, of all the ways of seeing the "slice-the-pie" method of understanding and controlling something, as big as a Planet/Universe/etc, and also being able to map with deterministic and accurate precious between those different contexts, with the best information available to you to do so (since some concepts may not map cleanly, and results will be accordingly "less good").

10.2: Single Layer Systems
--------------------------

The entire "OpsDB" as it has been presented in this book can be considered a single "context" or "layer" system because it was created so that all pieces were equal, relational, and shared a place with each other under concepts like Don't Repeat Yourself (DRY), and other methodologies so that there would not be overlaying contexts.

This would be different in a situation where an existing legacy system already existed, and the OpsDB was created in parallel, and they both had to share their work.

However, in this last case it is unlikely you would want to create two UMCs, because the OpsDB will become the dominant system, and the legacy system will be deprecated, so there is no reason to spend the time mapping between them with UMs.

If both systems were required, because of some requirement, and you wanted to maintain the different contexts independently, but wanted them to work together, or through each other's interfaces (so that there was a single-operator for any given task), then a sub-set of UMCRs would be required to map the two contexts together.

Generally, you will want to aim for a single-layer system because it is simpler, and requires less work to design and maintain, but if you find that you must have more complexity or complicated systems because of your requirements, then you can use the UM/UMC/UMCR methods to recursively cover all the differences between them in a comprehensive manner, if you implement the interfaces accurately.

10.3: Multi-Layer Systems
-------------------------


If comprehensive automation systems can be created as a Single-Layer System, than why would we ever need Multi-Layer Systems?

Why can't OpsDB scale into a Planet Scale Automation system without UMCs and UMCRs?

The reason is that OpsDB is taking a look at the data from a strictly virtual perspective.  It maps to physical devices, hardware and physical locations of things, and other physical attributes and issues, but it is primarily a logical system for controlling logical elements, which simply map to physical elements.

But, if one wants to automation an entire Planet's worth of infrastructure, then one is going to have to take many different perspectives than the one we have settled on for the OpsDB.

There will be many different views of these systems, which are in themselves just as valid as the OpsDB view, but do not mesh well with the intent of the OpsDB layout as I have described it here.

In essence, these will be new OpsDBs, written in the same method as the OpsDB I have laid out, but with very different goals and requirements, so that the current OpsDB has it's purpose, and so do these additional supplementary OpsDBs.

So, how can they all work together, in a way where things don't break, and they don't fight over resources (race conditions), and their different views of the systems, can be integrated together.

This is where the UMCs and UMCRs come into play.

Your logical OpsDB for controlling your system is a UMC, and your other OpsDB for meeting your other goals is another UMC, and the UMCRs connect them and allow them to work together, with their different views, but in complementary and non-conflicting ways.

10.4: N-M-... Layer Systems
---------------------------


Give examples of how we would need different systems that work together, and brief mappings between them.

Use things like physical infrastructure, gas or electrical delivery grids, etc.

Chapter 11: General Advice
==========================







11.1: Go over code reviews, and config reviews.
-----------------------------------------------

11.1.1: *** Mark this as my personal opinion.  Not as something provable.  This is color. ***
---------------------------------------------------------------------------------------------

11.1.2: Normal pitfalls.  Dont really check, "Yes Stamp".
---------------------------------------------------------

11.1.2.1: Too style oriented.  Enforcing a style is important in some areas, but less important in others.  It is better to keep a team cohevsive to know these differences, so that on some things you are strict (variable naming) and on other things you are flexible (commenting style).  People write prose more personally than they name variables, and variables have to be used by many people, whereas the message in a comment in based on the author's mental state when they wrote it, which is very subjective, and people have very different styles.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

11.1.2.1.1: I recommend allowing people to have their own unique style in areas that will not harm the ease-of-use and resiliency/robustness of the Logic, and strictness on naming conventions, and basic formatting (indentation)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

11.1.2.1.1.1: Strictness can be kept inside individual projects, with a general theme to a department or company.  These are degrees to each of this which will make actually working with other people nicer, while
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

11.2: Root Cause Analysis write ups.
------------------------------------

11.2.1: How to not bullshit these.  Dont lie.  Dont criticize every failure, because failures WILL happen.  The only way to avoid them is to REMOVE the CLASS OF WORK.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

11.3: Create a set of Checklists.
---------------------------------

11.3.1: Automation Spectrum
---------------------------

11.3.2: Automation Layers
-------------------------

11.3.2.1: Sub-Components of layers.  How well are they implemented, 1-5 scale or something
------------------------------------------------------------------------------------------

11.3.3: Talk about how to make your own checklists and scales.  This is flexible, not dogmatic.  The important part is that we can communicate what we are talking about, in a way where multiple individuals and groups can agree, allowing us to work successfully together.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

11.4: Self-evaluation?  How to evaluate your actions, how to make plans to improve.
-----------------------------------------------------------------------------------

11.5: Introduce the Basic Laws of Human Stupidity.  Not meant as insult or joke, but as quantitative method of determining the intelligence of an action.  This is the model I will use in this book.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

11.6: Journmanship, apprenticeship.  What we are missing.  Valuing experience.  Im old, of course thats my take.
----------------------------------------------------------------------------------------------------------------

11.7: The benefits of "vanilla" use of tools.  Less upkeep.  Only change what you strictly need to change.  Spend time optimizing only in critical areas.  Reduce things that need to be manually maintained.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

11.8: "Lowest Common Denominator" problem
-----------------------------------------

In response to: http://euphoricus.blogspot.com/2015/11/everybody-is-doing-tdd-take-two.html



Reduction to this workflow does not mean that this workflow can be understood and implemented with the same results in any manner.

I call this the "Lowest Common Denominator" problem.  In any given situation, there are some common things that are understood between all parties, and these are the things that can be communicated "clearly".

These concepts are used to divide up the problem so that they can be solved, hence denominator.  The problem is that in order for the parties to agree, they have to use the simplest methods of communicating that every party can understand, which is where the "common" and "lowest" (simplest) come from.

The issue here is that there are more efficient ways of doing things, that are not as simple, but not all parties will have equal knowledge of all of these things, presenting a dilemma:  Do you aim for higher efficiency or higher commonality?

This is something every given team/organization should decide for themselves, because they work on a spectrum.  If you aim for more commonality, you lower the bar on what techniques are common to all parties, and you will lose the benefits that un-commonly-known techniques may provide.

If you aim for efficiency of techniques, you enter the area where not all parties understand the techniques.  This is also exemplified by the "single person vs. large team" spectrum.  Single people are able to use efficiencies that even a 2-person team cannot, because of the immediate nature of communication inside one's own head.

As soon as the communication must be externalized, there is a massive loss of efficiency in the communication, and as the team grows the communication problems grow factorially.

How massive is this loss in terms of efficiency in communication between your own thoughts, and communicating with 1 external person?  {{ stats_memory_cycles_per_second_vs_words_per_minute }}

To give an example, this is the difference between accessing something already loaded into RAM and Layer 1 Cache, vs accessing something on a 5400 RPM slow rotating spindle disk, on a remote computer, that is networked via satellite, and resides on another planet (Earth -> Mars).  That is the type of inefficiency that is created between going from one's own thoughts, to communicating with 1 other person.

When communicating with teams or large groups of people, this is made worse, as often the communicate is by proxy, so not only is the communication inter-planetary in terms of efficiency, it is through a lossy-proxy, which will change the data and is more likely to summarize it, dropping out many details and changing the terminology, phrasing, and perhaps even the intent.

So while your assertion that everything can be broken down into: Create Test, Implement Thing To Be Tested, Verified Test.  

This does not mean that all different types of processes give the same results merely because of this.

To give an analogy, I can say that all data in a database could be stored in a single table with 3 fields:

- Group
- Type
- Value

All of these fields can be BLOBs, so we only need 1 storage type, and from that all data actions done in any other method can be implemented.

This is true, but it is not efficient.

This is a similar spectrum to having "single ownership" vs "team ownership".  They provide different benefits, and cause different problems.  Single ownership allows for the efficiency that a single owner can bring, but at the loss of wider understanding and access.

Team ownership provides wider understanding and access, but limits the amount of efficiency that can be used due to all members of the team needing to be able to understand all of the implementation well enough to work with it.

Anything that is not immediately well-understood by any member of the team, in a team-ownership environment, should be converted into a method in which that team member can understand it.  This should be applied to all changes, recursively, so that all details fit this criteria.

Taken to it's extreme, it is easy to see how this solution will be "dumbed down" (not to be insulting, merely to illustrate the point) to the most common knowledge (low tech vs high tech), and this will have an effect on the efficiency and manageability of the work.

There is a "tipping point" where this "low-tech" type direction starts to become a problem in itself, either by not performing fast enough, or not being small enough to manage, as size has a direct impact on complexity as well.  More things are harder to manage than less things, just as more complex things are harder to manager than simple things.

__Exchange__

Author:  So are you are saying that the workflow is same, but it just differs in implementation? I'm leaving that question out for now. I believe it is possible to separate the questions of workflow and it's implementation. So first think I want to agree on is on which workflow produces best result. After we agree on that, we can talk about it's implementation.


Me:

I completely agree with your interest in coming to agreement on workflow, techniques and terminology.  I think this is important work, and the surface has barely been scratched on it in our industry (even with places like the c2 wiki, which are comically in-depth).  Just wanted to say that.

I think there are a couple of issues here.

The first is the matter of deconstructionism.  For every layer of abstraction you remove when deconstructing something, you lose the context and connotations (intentions) of that symbolic abstraction as well.

So I can further deconstruct your deconstruction into this:

- Think
- Act
- Evaluate

Now we have an even simpler model, and we aren't restricting to programming.  The problem is that we also aren't even talking about software development any more, we've gone so general that it has lost it's original purpose, which is to better understand how to do something related to developing software.

In similar ways, each abstraction layer removed to get to the point of:

- Create test
- Write code
- Evaluate test

Has lost the contexts, connotations, and further layers of abstractions that each of the concrete methods that would be used in place of those 3 things, and the many nuanced sub-things that would be required to properly detail those replaces.

Taken to it's extreme, on that same spectrum, you go from the 3 things I just typed in, to the complete work of code you intended to produce, in it's ideal fully-tested-and-shippable form.

This is the full-spectrum of analysis:  From complete abstraction to complete concrete implementation.

So we can tune the discussion to any parameter for both this spectrum, and any related axioms for determining the results of the work that we wish to get through our efforts.

My point was mostly that we should not lose out on efficiency, if we desire efficiency, because we also desire commonality.  As they have a spectrum between them.  (Almost anything can be put with anything else into a spectrum, like two points making a line segment, so I'm not drawing from any specific examples here, more in idea-space)

11.8.1: "Best Practices" Means Not-Thinking
-------------------------------------------

Everyone wants to know a "good" way to do something, or better yet a "better" way of doing something, or best yet, the "best" way of doing something.

And so, "Best Practices" were created, to be sold by authorities (of any type or experience level) as to what you should do under a given situation, often with little context at all in terms of pros-and-cons of the implementation, because the authors often have very little personal experience in managing the solution being offered.

Why would I broadly declare this to be true?  Because for any given "best" solution to be published would require more caveats and warnings than any advice, because "best" is a very specific set of criteria, and they by definition are not taking any of your specific environmental issues into account.

Why would I broadly state that this is tantamount to Not Thinking?  Because if one does not take into account one's specific environment, requirements, resources and goals into consideration in making plans for action, than what is one doing?

It is following a recipe, without checking if the recipe will even give you what you want.  Do you even know what you want?  Probably only vaguely if you want to follow someone else's Best Practices, because you are leaving all the decision making as to what the effects of the system will be up to someone who doesn't know you, your circumstances, your environment, your requirements, your resources or your goals.

Does leaving all that up to someone who doesn't know any of those things sound like Good Thinking to you?  It does not to me, which is why I stated this section's title as I did.

Reading over the "Best Practices" of others is not in any way bad, and one should try to collect up all the ways that people are doing things, or at least all the major archetypes of those methods, so that one has a good perspective of external activity to help guide one's own decision.

But, then one should make one's decision based on your own environment, your own understanding of your resources, your own understanding of your requirements, your own understanding of your goals, and in this way you can tailor any external or internally created methodology to meet those needs, and because you thought about it yourself, whenever you discover something is inefficient you have the tools to re-design the solution to meet the new problem and solve it.

If you are simply following someone else's recipe, you are unequipped to change the recipe, because none of the thinking about how to build and apply the recipe were your own, so changes will be not mapped to all the issues I mentioned.  Often people are more likely to just switch to a different recipe, which they see as a New Silver Bullet, because the last one didn't work.

Repeating this process wastes time and other resources, and you give up all the opportunity you could have been leveraging if you had made your own plans, because you could make smaller changes since you well-understood all the components and decisions.

11.9: The Similarities of All Code
----------------------------------

Explain how all code is similar, and all programs are implementing 95%+ the same functionality, and 5%- unique functionality.

Explain how to take this apart and put it back together again, and how to apply it.

11.10: Penalties of Over-Abstraction
------------------------------------

{{ todo__needs_editing__maybe_moved_into_another_section }}

Removing the real-worldness of things always makes them easier to abstract, and also makes them unequipped to solve any real-world problems as-is.

Many times when a real-world problem is finally solved with the non-real-worldness-based abstracted solution, the fit is not a good one, because the abstracted solution factored out critical elements of the problem, and now the problem is solved less efficiently, and in some cases too inefficiently.

It yields better results to design a solution to an exact problem, so that you can solve it as efficiently as possible, and then abstract the solution into two split pieces: an abstracted library layer and a real-world implementation layer.

Then you know the abstracted version solves a problem efficiently, because it's the exact solution you just designed to solve your problem-at-hand efficiently.

If it worked for this problem efficiently, there are likely other problems that can also make highly efficient or sufficiently efficient use of the abstracted solution as well.

This is obviously something that can be logically proved if someone wanted to spend the effort.

11.11: Releasing the poison
---------------------------

This is the only non-Operations advice that I will give in this book, because I think it is the most important non-technical advice I can give, and it has to do with inter-human communication and inter-human relationships.

No matter what society, culture or place you are born in, grow up in, and live in, there are elements around you that are harmful to you, and affect you in a negative manner.

In dealing with other people, we often encounter negativity in many dimensions, whether it is in attitude, verbally, or physically.

And in our own actions, we ourselves will have negative attributes that are presented and may affect our co-workers, team mates, as well as ourselves, friends and family.

A term I have begun to use for this type of thing is "poison", and to use it in a sentence might be something like, "I am poisoned, and have become toxic and it is effecting myself and others".  This reads pretty harshly to me, but it is meant to be clarifying and not vague or down-played.

I believe that all of us are both our own greatest allies, and our own worst enemies.  Our own actions have more impact on us than any other individual's can have, because we are the ones who coordinate our actions every second of every of day of our lives, whether we are directly aware of the coordination for each action or not.

In term's of our larger group's influence on us, this is actually more of our own influence on ourselves, as we have interpreted the intention of our larger society, culture or group, and our position in it.  I find conflict between my view of how I think I should fit into my group, versus how I would like to fit into my group.  And the same is true for "how the group thinks about me", to anthropomorphize the "collective dynamic" or "group think" or "social pressure" or "super ego" or whatever.

But, this is not merely negative, it is also positive, as I take the good things about my culture and group, and I am seen positively by them and myself, and I see the positive ways that I fit into the group, and they do me.

In order to improve myself, I need to focus more on seeing these positive things, and how others can see me positively, and less on the negative.  My attention alone will create time that I spend reflecting on the negative aspects, where I could be putting effort into actively making things more positive, and spending my time inspecting the positive aspects of things to determine how to strengthen them, and create more of them.

I refer to this, internally (and now written into a book, I guess), as "releasing the poison", which is releasing the things inside me that make me "more toxic", so that I can be "less toxic", with the goal of being "not toxic".

I say "releasing" instead of some other term, because these are active patterns in myself, things that I do, that I didn't have to do, but did.  So these are habits or reflexes which need to be changed, but in order to do something else, I must stop doing what I am already doing.  So I refer to this as "releasing" it, as it is something I am "holding on to", which is why I keep doing it.  I think this distinction is important, as it underlines how this is completely an internal process, that I can accomplish myself, with no external validation.  

Why is it important that I can continue to make progress without external validation?  It is important, because if people act in negative ways to me or around me, I do not need to respond with negativity or spend time dwelling on the negativity.  

Acting with negativity creates a feedback loop, where one party is negative to another party, and the other responds with negativity (understandable, even if they were neutral or positive prior to the introduced negativity), and the first continues to respond negative and may increase it, and so on.

Because this feedback loop only intensifies until one of the party "turns down the volume", or turns it off, then it becomes clear why so many problems exist between people. 

I am certainly not through with my journey on this path, but I feel continual improvement as I have created an internal process of inspecting things that occur in my life, and comparing them to the model I have created for how I spend time related to negativity, versus how I spend time related to positivity.

This allows me to see where I have made mistakes more easily, and gives me the incentive to take action to try to correct those mistakes.  Often simply not taking action to correct a negative-effect action creates even more problems down the road which requires much work or may be unsalvageable, where taking a smaller effort earlier on, after detecting the problem, leads to less problems in the future and a more positive outcome and duration.

If I have said or done something that may have caused a problem for someone, in any way, I can realize this and then mention it to them in passing, or ask to talk with them and go over what happened, and how I would prefer things were resolved, trying to fix any problems that were created, and create and keep a positive relationship with them.

This, however, does not mean that I ignore problems because "problems are negative".  I do not see problems being negative, even though "problem" and "obstacle" are normally negative-quality terms.  In engineering, and especially in more maintenance type aspects such as Operations, problems and obstacles are almost all we deal with.  Everything could be phrased as a problem, and it could be flipped around to being phrased as an opportunity.  

I don't recommend trying to phrase problems as opportunities all the time, because it leads to sounding unrealistic, but if you look at them positively, they really are opportunities that one can take advantage of to greater or lesser degrees to get greater or lesser benefits, if one can view them appropriately, and work with the knowledge gained from that vision into their nature.

I think this methodology this has been very good for me, and recommend spending some time to think about this, and how it intersects with your life, and who you are, and if you can think of ways that bring about similar improvements in your own life, which can make working with other people more enjoyable and efficient, and brings you more happiness, contentment and a more fulfilling life with more accomplishments and friends.

11.12: Randomly Collected Spectrums
-----------------------------------

Spectrums I thought of, but have not yet placed in a particular part of the book.


Spectrum: Caring

Shame <=====> Pride

Without caring about things, one cannot feel shame over bad actions, nor pride in good actions.  This is an effect of having an environment where the care-takers do not care about their environment, only about getting through another day.

When you care, you will avoid creating Shame for yourself and others.  When you care, you will try to perform actions you and others can be Proud of.  These are good things, because they will form as a compass, pointing in the direction you want to go towards and away from.

If your assessments are in Alignment with Reality, then you have high assurance that you are creating a better Environment for yourself.

11.13: How To Make A Decision
-----------------------------

Describe how to make a decision immediately based on data.

How to decide when you need more data.

How to decide when you have enough data.

How to make an immediate decision when you have enough data.

How you can explain your decision based on the data you had to others.  Charting, graphing, etc.

Chapter 12: Everywhere.  Throughout the book.
=============================================







12.1: Have "Wouldnt it be nice?" sections, where I posit what would be improvements I have yet to experience.  Coming to terms, agreeing on the foundational details, agreeing on the axioms, agreeing on how to relate data to the axioms.  Agreeing on how to act against axioms.  With these done, we can work much better as a team, and discuss them.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
