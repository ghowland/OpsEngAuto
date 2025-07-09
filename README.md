# Old School Operations: 25 years of System Administration and SRE


Total Sections: 348   Populated Sections: 92
Current Goal: Populate Empty Sections: 256   (Done: 26.4%)


<br><br><b>NOTE: This is still an early Work-In-Progress.  It is being written linearly as a First Rough Draft without editing at the moment.  There are many typos and grammatical errors presently.</b>

Lines: 3490

Words: 63944


# Chapter 1: Preface (README.txt)


What will you get out of this book?  Why read it?



What I hope to impart here is a view into how I see operations, and how I automate operations.



In the case of this book, "operations" means "networked operations", "server operations", "datacenter operations", "production operations", all rolled into one term.  The name is both specific and non-specific, as operations can mean other things, but these specific fields are what I'm referring to.



What I hope you will gain from my perspective is a new foundation you can use as a plane of reference to improve your own operational mindset and practices, whether you are already an experienced operations engineer or new to the field. 



I will be covering a large arena of information, and I will try to present a coherent picture, though each section must unfortunately be left incomplete as each section is only a small part of the larger picture I am trying to make clear.  This is in contrast to many technical books which explain things clearly in each section before moving on, because their content is able to be defined and explained in each given section.



This book's format is meant to be read from start to finish.  It starts off more general, and philosophical, setting up terminology and direction.  Then it becomes more specific as we work towards implementation.  Finally, it will go back to being more general as we discuss how to implement automation in your current environment, as automation will change the way your organization operates, and must be performed with these issues in mind.



This book is more about depth than breadth, and as such we will continue to come back to examples over and over again, looking at them in different ways, to give a deeper understanding of all the components that make them up.  This is again in contrast to many books that are meant to describe an array of information and give you a broader understanding of how they work and how to use them specifically.



This book is meant to improve your ability to reason and create efficient solutions in the operational engineering space.

<h2 id=8d921a98a2974ea61b905ce719a9f121><a href="#8d921a98a2974ea61b905ce719a9f121">1.1</a>: Where Ive Been, What Ive Been Doing, Why I Wrote this Book</h2>
<br>
As of this writing (2016), I've been working in the industry for over 20 years, and have been programming for over 30 years.&nbsp;&nbsp;I've written over 1000 programs of varying size (the bulk of them being smaller, and operational in nature), but have also written and deployed PC games, end-user productivity tools, accounting software, end-user websites, as well as a lot of operations related monitoring, alerting, log parsing, configuration and automation logic required for operations work.<br>
<br>
Some names of places I've worked, named where you may know them, and grouped as industries where it's unlikely:<br>
<br>
Google, VMWare, Netflix, LinkedIn, Cisco, Pacific Telesis, Lawrence Livermore Labs, Mobile Game Companies, PC Game Industry, Mortgage Industry, Financial Security Industry, Internet Startups (SaaS and end-user websites)<br>
<br>
You can see my abbrieviated job history at LinkedIn:<br>
<br>
https://www.linkedin.com/in/ghowland<br>
<h2 id=4135cf6df0e576145b37ff7fe29922a3><a href="#4135cf6df0e576145b37ff7fe29922a3">1.2</a>: The promise of automation is removing classes of work</h2>
<br>
"The promise of automation is removing classes of work, while you consistently get the desired results."<br>
<br>
At this point, everyone knows that automation is a necessary thing.&nbsp;&nbsp;It wasn't always this way.&nbsp;&nbsp;I spent much of my career trying to automate things and getting strong pushback from both management and peers (starting around 1996).&nbsp;&nbsp;<br>
<br>
These days people usually have some aspects of automation, and are comfortable with those, so it is only the areas that they do not yet have experience which are hard to get implemented.&nbsp;&nbsp;A major impetus in writing this book is to resolve those problems, by making the concepts better publicized and hopefully well understood.<br>
<br>
The issues I find these days are not that people do not want comprehensive automation, but that there is not a clear understanding on what comprehensive automation entails, what it takes to build, how things will change once it is in place, and how the life-cycle of operations changes accordingly.<br>
<br>
With all of these things, it is best to stay results-focused, and look to what you want to achieve out of automation, and in my opinion the ultimate goal should be: "removing classes of work".<br>
<br>
What is a "Class of Work"?&nbsp;&nbsp;We will look at this in many ways over the course of this book, but we can start by summarizing it as: "anything that is done".<br>
<br>
This may be a specific thing such as "update a DNS zone file" (text file).&nbsp;&nbsp;When this "Class of Work" is comprehensively automated, then no one will ever again update the text file relating to DNS zones, but will have to do other work related to DNS still, as only updating the zone file was comprehensively automated.<br>
<br>
This could be extended to "configuring DNS", in which case all zone files are automatically generated, the serial numbers are always incremented properly, the configuration files that specify the zones are generated, and all the transfers and tests to ensure that these changes are pushed out into production and contain valid entries are validated and monitored.<br>
<br>
This is a "Class of Work" that requires people to do something currently, but perhaps only in some areas if it is already partially automated.<br>
<br>
If you have a service (SaaS, such as a web-site like "DNS Made Easy") that does this for you, then someone still needs to enter the data.&nbsp;&nbsp;The data entry is still a manual process, and part of the total Class of Work relating to updating DNS.<br>
<br>
How would you remove this manual work?&nbsp;&nbsp;It will need to be generated from either a template of hostnames for the type of services being provided, or some other automated mechanism.<br>
<br>
When no one has to think about the life-cycle changes or perform manual labor relating to this area of work, then this Class of Work has been comprehensively automated, and has been removed from the realm of Manual Labor (which requires scaling personnel).<br>
<br>
Updating the system (code) that manages this Class of Work remains manual labor, as writing logic has not yet been turned into an automatable task, but the regularity of updating the automation logic should happen far less frequently, and is more knowledge-work than data-entry work.<br>
<br>
Knowledge work is more stimulating, and known to be something that needs reviews and tests, whereas manual data-entry work is more prone to mistakes, because it is done so regularly that constant vigilance becomes impossible to perform accurately.&nbsp;&nbsp;<br>
<br>
Mistakes will happen, as everyone knows manual work must be manually inspected and automatically tested, and yet this is typically the place that mistakes are made, because updating automatic tests and and manually inspecting the data are both themselves manual processes, and similarly prone to failures.&nbsp;&nbsp;<br>
<br>
Eventually someone will make a typo or other data-entry mistake, and it will not be caught in review, and will be pushed out to production, and will cause an outage, and may cause loss of revenue or other negative consequences.<br>
<br>
With automated logic, these kinds of repetitive data changes and verifications can be done as correctly as the logic specifies, and if it is written correctly, it will be done correctly forever.&nbsp;&nbsp;Or, until the business goals or infrastructure environment changes, and it must be modified accordingly.<br>
<h2 id=205420c1274a2b80366e988715cd32f8><a href="#205420c1274a2b80366e988715cd32f8">1.3</a>: Writing in the First-Person</h2>
<br>
You may have noticed, but I am writing quiet frequently in the first person, and will try to keep this consistent as much as possible.<br>
<br>
I am speaking of my experiences, perspectives and opinions, and so I think this is best done using "my own" voice, instead of a more factual "voice of authority".<br>
<br>
In my view, all information should be considered as coming from the source of origin, where you discovered it.<br>
<br>
When I say "X is Y", I think this should be read as "Geoff said X is Y", and not that X really is Y.&nbsp;&nbsp;Whether X is really Y or not should be something that you validate for yourself, in your own experience, in your specific situation, or context.<br>
<br>
The situation I could be using as my example may not match up to the situation you are working in, and my perspective may not be a useful one.<br>
<br>
Moreover, language itself is very flexible in what is what is meant, as many things could be intended by the same word, like the very overloaded word of "operations".&nbsp;&nbsp;There is frequently a COO, Chief Operations Officer, in large or public companies, and this person's role and department has absolutely nothing to do with "production operations", "network operations", "server operations", "datacenter operations", etc.<br>
<br>
Because of this, it is useful to limit what you take from incoming information to what the speaker was trying to convey to you, their intent, as coming from them, from that particular situation, and their particular perspective and experiences.<br>
<br>
This separation from incoming-information as "fact" makes taking in more perspectives easier, as they do not need to be turned into a one-size-fits-all world view of truth.&nbsp;&nbsp;As I learn more, I find that having such a one-size-fits-all is often a hindrance to communicating with other people, and learning new things.&nbsp;&nbsp;It is certainly a hindrance to having an open mind to new information which may conflict with one's current world view.<br>
<br>
Instead having a "this person said this thing" stance, allow any new information to come in as it arrived ("I learned about X from Y").&nbsp;&nbsp;You experienced getting the information in some way, and that is that.&nbsp;&nbsp;No additional weight needs to be added or subtracted from that evaluation, and you avoid applying the Logic Fallacy of the "Appeal to Authority" in your own in-take of information.<br>
<br>
Whether you utilize that information, or make it part of how you make decisions is up to you.&nbsp;&nbsp;Whether it is applicable to your situation is up to you.&nbsp;&nbsp;Whether it seems logical and grounded in reality as you understand it is up to you.&nbsp;&nbsp;There is no reason to reject or accept it, as it is simply information, and you have tagged it along with the source to use as you see fit.<br>
<br>
There will be quite a bit of this kind of introspection into language and meaning in this book, as it is in part a book on the philosophy of engineering and automation, because this is much more important than common jokes about philosophy majors in college may lead one to believe.<br>
<br>
I also find that when writing in the first person, it is less of a commanding or authoritative approach, rather than writing in the second person ("you will then do this"), which has more opportunities to throw readers off if they disagree with the statement, do not immediate want to do what is being recommended, or are just tired of being lectured at.&nbsp;&nbsp;All of these are reasonable reasons for avoiding incoming information, and I use my own voice to give it as my own take, to avoid this.<br>
<br>
This is a one-way conversation, in that it is a book, but it is meant to be taken as a conversational approach to learning, so that you can grow from it as best is possible, and not merely a display of my knowledge and set of instructions for others to follow.<br>
<h2 id=8c769f9c732b984ba19311c211e281ab><a href="#8c769f9c732b984ba19311c211e281ab">1.4</a>: Writing Stylistic Conventions</h2>
<br>
There will likely be some writing stylistic conventions I use that are new for you to read, and perhaps you don't like, and certainly you will not find approved in English Grammar books.<br>
<br>
I have developed my style of written communication over my life, and continue to refine it still.&nbsp;&nbsp;I am more concerned with having my intent and detailed messages understood than in complying with grammatical rules, and so will bend and break them as needed to achieve my desired results.<br>
<br>
As such, as I will quote "things" whenever I want to emphasize them specifically, as introduced by Alfred Korzybski, from his methodology of General Semantics (although not following his strict guidelines).<br>
<br>
I will also interject parentheticals (like this), whenever I want to make an immediate "aside" comment or clarification (like this).<br>
<br>
I will also make up words whenever they seem to work better, or sometimes I will think I am making up a word, but it might end up being an existing word that I didn't know, and has a different standard meaning.&nbsp;&nbsp;I will try to explain my meaning any time I think I am making a concept that may not be a standard one, so try to read it with my intent, instead of against a standard, as if I stuck to the standards I don't think I could get the details with the pacing that I want.<br>
<br>
I am going to frequently switch words such as "I", "you", "we", "one" to account for the subject, and I have specific meanings for this:<br>
<br>
- "I": I am talking about myself and my experience.&nbsp;&nbsp;As previously said, I will try to do this as much as possible, because this is a transference of knowledge, from me to you.<br>
<br>
- "You": I am talking about you, the reader.&nbsp;&nbsp;I have written this for you, even though I probably don't know you, I have you in mind when I am writing, and I am thinking "What will you be aware of at this time, from previous material?&nbsp;&nbsp;What I am trying to get you to?&nbsp;&nbsp;Is it clear to you?&nbsp;&nbsp;Do I need to add any disclaimers or details?&nbsp;&nbsp;Am I spending too much time on this?"<br>
<br>
- "We": You and I are on a short journey together, although at different times and different places, but I am relaying information into this medium, and you are consuming this information, and that creates an informal relationship between us.&nbsp;&nbsp;I like to think in terms of "we" for this, as it is a shared journey.&nbsp;&nbsp;<br>
<br>
When I write code I often like to document things like "Here we are doing this" and "We don't want this effect, so I am doing this".&nbsp;&nbsp;In this "future readership" situation, I am thinking of the code documentation's future reader, which may be myself or someone else.&nbsp;&nbsp;In either case, that reader will be in a different state than I was at the time I wrote the code and documented it, so I am trying to bridge that gap, and make it another "shared journey".<br>
<br>
- "One": This is when I am trying to give advice to some sort of direction.&nbsp;&nbsp;I really don't think I should be telling you what to do, and I don't want to.&nbsp;&nbsp;I want to assist in enabling you to do things better, and to make your own choices, and make your own processes, and methodologies and philosophies.&nbsp;&nbsp;Telling you to do things is in opposition to these goals, so I use the word "one", such as:<br>
<br>
"One's tea is best with slightly sweet biscuits."<br>
<br>
It is kind-of the British Royal "we", as the "all encompassing singular", but I write it mostly so if you don't want to accept my information, it is easier to digest, because it is directly toward the aether, and not directly at "you" in a tone of command.&nbsp;&nbsp;I feel this is a way one can make generalizations and advice, without making the statement too-pointed-at-you.<br>
<br>
I will also hyphenate-things-to-make-compound-ideas.&nbsp;&nbsp;This allows words to be read in the sense of "all these things are one thing", and help in any kind of grammatical parsing.&nbsp;&nbsp;As I understand it, not being able to speak German, the German language has "compound nouns", in which many nouns are put together in sequence to form a new word that is a combination of all of these.&nbsp;&nbsp;I think this is a cool method of communication, and these long-chains-of-hyphenated-words are like that, but for any type of word, not just nouns.&nbsp;&nbsp;They create Compound Concepts.<br>
<br>
I was born and have lived almost exclusively in the United States of America, and only in a few small areas of that space, and so my language usage is set up in a certain way.&nbsp;&nbsp;Additionally being an Internet-denizen, I have a very fluid use of that language.<br>
<br>
My usage of English, or maybe "American", may not be easy for you to parse if you are not familiar with the way people similar-to-myself communicate, or English may not be your first language.&nbsp;&nbsp;<br>
<br>
Even if you have a very similar usage of language as mine, the ideas I am expressing are complex and riddled with detail, so these mechanism of asides, and compound ideas, and such are methods to make parsing these ideas more clear, although they may appear more Byzantine.<br>
<br>
I am mostly writing in a tone of conversation, and so will jump around more than if this was a text book.&nbsp;&nbsp;This is certainly not a text book, and should not be read as such.&nbsp;&nbsp;It should be read more like a novel, as I am attempting to perform "Mentoring", and so am building up ideas and referencing them repeatedly in a type of planned sequence.<br>
<br>
If you jump to a section, and find it oddly confusing, it is likely because ideas were introduced and specified in a previous section, and their immediate usage (without that previous information) may seem very alien indeed.<br>
<br>
This is a trade-off between writing styles, and for this work I have chosen this style as the one I think will yield the best results for the audience most-likely to be able to intake this information and make use of it.&nbsp;&nbsp;That is only a guess, but I have to pick a methodology and stick with it.<br>
<br>
I will also be making Liberal Use of capitalizations.&nbsp;&nbsp;I will have certain terms that I always capitalize, as I am using them as "Proper Nouns" (like a person's name), but I will also sometimes capitalize Random Words, because I am introducing a concept and want to draw attention to those specific words in the sentence.&nbsp;&nbsp;It may be that I will capitalize them the first time I talk about them, and then never again, because the point was made, and the attention to them was drawn.<br>
<br>
All of this makes a real jumble of what is considered proper English, but I am doing more than relaying my thoughts and experiences and methodologies to you in English, I am trying to communicate the underlying ideas behind them, and those concepts are far more detailed and complex than English (or any language as I know them) can relay.<br>
<br>
There is a reason we have poetry, because the intent is to express something beyond the words, and often the structure of normal language communication is broken or modified to relay those intentions through the language, as the language is both the barrier and the medium.<br>
<br>
My usage is similar, but is the Poetry of Engineering, as I see it.<br>
<h2 id=c0288d74f0dd8cb74fcb23af5ce26a0e><a href="#c0288d74f0dd8cb74fcb23af5ce26a0e">1.5</a>: Hopefully, this will...</h2>
<br>
The ultimate goal in this book is that it improves your ability to function as an operational engineer, and to write automation that achieves the results that you want.<br>
<br>
If you find any areas difficult to understand, or believe that sections are not explained well or are incorrect, feel free to write me and I will try to get back to you and update the work as best I can.<br>
<br>
My personal email is:&nbsp;&nbsp;geoff@gmail.com<br>

# Chapter 2: Introduction


One of the foundational goals of this book will be to differentiate the real from the virtual.



This may seem like something that is common sense, but I have found wide breadth and scale disagreement on what is real and what is not real, and this creates a lot of communication and planning problems.



If we can't agree on what is real, how can we agree on our priorities?  We will value things differently, because we understand them differently at a very fundamental level, and all communication will be inaccurately moving past each other, instead of directly engaging with common terms and values.



The results will be poor, and without coming to terms with why this fundamental mis-communication is occurring, we may never be able to see eye-to-eye, and may end up being unable to work to get good results with each other.



Going to the very basics and working up from there will allow us to develop a common method of communicating, starting from terms, and moving to goals, and then priorities, and finally into axioms so that we can come up with plans where we agree on the components and end results.



<h2 id=ff17d94c0d49aab3e372e47b64b96ea7><a href="#ff17d94c0d49aab3e372e47b64b96ea7">2.1</a>: The differences between Physical and Virtual: Real and Unreal</h2>
<br>
"What is reality?" is a question that is too big and general to be dealt with here, if you want a good introduction on how to understand this from an engineering perspective, you can see Bertrand Russell's book {{ book_russell_reality }}.&nbsp;&nbsp;It does a good job of describing how reality can be determined from our senses, and is a fairly short read (described in about the first 30 pages).&nbsp;&nbsp;You can also take a look on Wikipedia at the philosophical movement, Logical Positivism, which is a useful philosophy for engineers, and is one of the philosophical methodologies I use and reference in this book.<br>
<br>
For our purposes, it is good enough to have a summary of this, and for me to describe on which side of real vs. virtual (un-real) various elements reside in, for our purposes.&nbsp;&nbsp;Again, this is not meant to be "ultimate truth", but a tool for communication, so that we can come to common terms and understandings, and grow our engineering abilities and get better results.&nbsp;&nbsp;It is not meant for purposes outside of this endeavor.<br>
<br>
To be brief, I will use Russell's example converted into the experience you are having right now.<br>
<br>
At present, you are somewhere reading this text.&nbsp;&nbsp;You are real, you exist, because you have tangible properties, such as mass, made of of molecules and atoms, in a certain state that make you you.<br>
<br>
The text you are reading is either in a book form, such as paper, or an electronic form, such as a monitor or e-ink display.<br>
<br>
If you are reading a book, the book is real, because like you, it is made of molecules, and has physical properties.&nbsp;&nbsp;It resides in a certain position in the world.<br>
<br>
If you are reading from a monitor, then the monitor has similar physical properties.<br>
<br>
These things are all real, for our purposes of reality.<br>
<br>
The way you are able to read is that either ambient light is refracting off of the book, or is being emitted from the monitor, and those photons are striking your eyes, and the rods and cones in your eyes are being stimulated, and sending "signals" into your brain and nervous system.<br>
<br>
These things are all real.&nbsp;&nbsp;Photons have physical properties, and while different than molecules and atoms, are able to be physically described and interacted with.<br>
<br>
At this point, you are probably affirming why you may have not read more philosophy works in your life, right?&nbsp;&nbsp;Nothing new here, but lots of words to get to that point.<br>
<br>
Now, we enter into the realm of the un-real, the virtual world.<br>
<br>
How you interpret the words is not real.&nbsp;&nbsp;It is a virtual type of understanding, though the word "virtual" is usually confined to computer related terms, I am going to use it universally to all things to differentiate from real.&nbsp;&nbsp;Because we are mostly going to be discussing computer-related un-real concepts, it is easier to just stick to real vs. virtual.<br>
<br>
So, what am I getting at here?<br>
<br>
You are real, the device (book/monitor/device) is real, the photons traveling to your eyes are real, but your understanding and interpretation of the words is virtual.&nbsp;&nbsp;Your feelings about the words is virtual, and in fact the words themselves are virtual.<br>
<br>
The ink on the paper, or the electrons producing the physical effects are real, but your understanding and interpretations of them are virtual.<br>
<br>
What's the point of this?&nbsp;&nbsp;It will become clearer as we go on why I am leading with this, and it's not to make myself seem like a fancy-pants smart guy, it's because without this agreement now, there will be many more disagreements in the future, and it will hinder our communication about the more interesting and relevant parts of engineering and automation.&nbsp;&nbsp;Please, bear with me here.<br>
<br>
So.&nbsp;&nbsp;We have real books, devices, you are real, I am real, but your understanding and my understanding of things is not real, and even the words I am writing and you are reading are not real.<br>
<br>
How are words not real?&nbsp;&nbsp;It is because they are symbolic.&nbsp;&nbsp;They represent an idea, or set of ideas, which are also not real.<br>
<br>
The word for "book" exists separately then the object they describe.&nbsp;&nbsp;In other languages, the word "book" changes (libre, knega, etc), yet the book itself does not change.&nbsp;&nbsp;This illustrates how words are different than the things that they describe.<br>
<br>
Words can also be written in different fonts, and I could call this a "manual" instead of a "book", and yet what you are reading would not change.<br>
<br>
Symbolic things are not real, they are virtual, or logical.&nbsp;&nbsp;I will use virtual instead of logical, as I will be differentiating "Virtual" as un-real, from "Logic" to be used for processes and code, or programming.<br>
<br>
Let's create a quick list of things that are real and virtual, for an immediate reference:<br>
<br>
- Hardware:&nbsp;&nbsp;Real.&nbsp;&nbsp;Something you buy (a device), put an OS on, and runs your software, or something similar.<br>
- Software: Virtual.&nbsp;&nbsp;Electricity (in RAM), magnetism (on rotating disks) or electro-chemical (on SSDs/NAND) stores bits of information that can be executed.<br>
- Data: Virtual.&nbsp;&nbsp;Same as software, but can't necessarily be executed.<br>
- Operating System:&nbsp;&nbsp;Virtual.&nbsp;&nbsp;Collection of software and data to make hardware perform operations.<br>
- Book: Real.<br>
- Words.&nbsp;&nbsp;Virtual.<br>
- Ink on a page: Real.<br>
- Fonts: Virtual.&nbsp;&nbsp;Data about how ink can be put on a page, or pixels illuminated on a screen.<br>
- Light emission from monitors/screens: Real.<br>
- Words and letters written on the monitor: Virtual.&nbsp;&nbsp;These are just patterns we recognize, and are all virtual.&nbsp;&nbsp;The physical properties of them are real, but those are not what we call "words" or "letters", but are instead patterns of photons at different frequencies and intensity.<br>
- "A network": Virtual.&nbsp;&nbsp;It's a concept of something that "networks", or more specifically may be an network IP address (data), that describes the network.<br>
- Network cables: Real.&nbsp;&nbsp;Physical objects, that carry current.<br>
- Ethernet protocol: Virtual.&nbsp;&nbsp;A collection of data and logic that describes how to communicate over electrical signals.<br>
- Layer 1 Ethernet: Real.&nbsp;&nbsp;Physical electrical signals<br>
- Layer 1 Ethernet standard:&nbsp;&nbsp;Virtual.&nbsp;&nbsp;The description of how the physical Layer 1 ethernet will operatie.<br>
- Layer 2 Ethernet: Virtual.&nbsp;&nbsp;How the Layer 1 physical (real) is used via the Layer 1 Ethernet standard (virtual), to create a Layer 2 ethernet connectivity effect (virtual).<br>
- IP Address: Virtual.&nbsp;&nbsp;Data.<br>
- Hostname:&nbsp;&nbsp;Virtual.&nbsp;&nbsp;Data.<br>
- My engineering perspectives:&nbsp;&nbsp;Virtual.&nbsp;&nbsp;Data.<br>
- My engineering experience:&nbsp;&nbsp;Virtual.&nbsp;&nbsp;Data.<br>
- The actual things I have been through in my life:&nbsp;&nbsp;Real.&nbsp;&nbsp;Things happened, involving molecules and stuff over time (entropic heat exchange, etc)<br>
- My perspectives and memories of the actual things I have experienced:&nbsp;&nbsp;Virtual.&nbsp;&nbsp;Data, and summarized data at that, since I was not aware of the full-state of the physical (real) occurrences around me, and my memory (virtual) of them is a summary of that as well.<br>
<br>
<br>
I hope this short list and hopefully not-too-painful fundamental section has left what I am referring to in a clear state with you.&nbsp;&nbsp;<br>
<br>
If not, please skim it again.&nbsp;&nbsp;You don't need to agree with me on these things, you merely need to understand what I am trying to say clearly to get the information I am trying to convey.<br>
<br>
If you ever hit parts that feel wrong to you, or you reject, try to use the mechanism I presented in the preface, changing what you disagree with to: "Geoff says X"<br>
<br>
This means you can take in this information, as "Geoff is saying this to me", without having to update your world-view at this moment to include what I am saying as "the truth", and in fact, I am not asking you to ever do this.&nbsp;&nbsp;This is a communication to hopefully provide you more insight, which will include my perspectives, not as instructions on how you should see the world once you have finished reading this.<br>
<br>
It is more important that the things I am saying to you are internally consistent (Alignment), than that you agree with my usage and summary of each of them.&nbsp;&nbsp;I am working with more information than I can convey at any given time, and am doing my best to partition this into a small stream of data that can be turned into understandable language.&nbsp;&nbsp;It's a lossy process, at best, but it's the best I am able to do currently.<br>
<h2 id=75d62671847424a563ec929a890245c5><a href="#75d62671847424a563ec929a890245c5">2.2</a>: I only really know what I myself have experienced</h2>
<br>
What do I know?&nbsp;&nbsp;What do I really know?<br>
<br>
Or, to paraphase a Sherlock Holmes quote, "What do I know, and how do I know it?"<br>
<br>
In any situation, this is a relevant question, as it directs where I will go next.<br>
<br>
If I believe I have solid information, that I can take action on, I can begin immediately to take action on that information.&nbsp;&nbsp;If I know that I do not have solid information, then I know that the first thing I need to do is to get some solid information I could work on.<br>
<br>
How do I know if what I really know is good information?<br>
<br>
It should be sourced from my own experiences, or it should be planned to quickly make checking the information so that it becomes part of my personal experience.&nbsp;&nbsp;Things I have personally experienced, I can say I have knowledge of.&nbsp;&nbsp;<br>
<br>
Things I have read or heard, or that someone (including myself) just thought up may not be related to the reality of what is going on at the moment.&nbsp;&nbsp;Actions based on non-personal-experience information are going to yield extremely unreliable results, because the information was not grounded in the circumstances it is being applied to:&nbsp;&nbsp;Local Reality.<br>
<br>
What you experience and work with directly constitutes your actual context:&nbsp;&nbsp;Reality.&nbsp;&nbsp;Information that is not directly related to your context may not be directly applicable: Virtual.<br>
<br>
Let's create an example, a problem for us to solve.&nbsp;&nbsp;We'll be doing a lot of this during the course of the book, so to get the most out of these I would suggest taking a moment each time one is introduced to try to model it out in your mind, imagine it, draw it out on paper, or do whatever works best for you.&nbsp;&nbsp;I will discuss some of my techniques for doing this as we progress, but please use what you already know and invent new ones any time they occur to you as well, and try them out.<br>
<br>
The problem will be a common one:&nbsp;&nbsp;Alerts are going off on our monitoring system, and tell us that we are having problems with our web servers.<br>
<br>
The monitor alerts are not extremely specific in this case and report something like "HTTP test failure".&nbsp;&nbsp;More specific alerting would be helpful here, but those tests take time to set up, and in our immediate example environment they don't exist.<br>
<br>
A group of people forms up to deal with the alerts, and immediately several things are suggested as problems:<br>
<br>
- Maybe there was a bad code push?<br>
- Maybe the logs have filled up the disks?<br>
- Maybe there is a DDOS or other hacking attack occurring?<br>
- Maybe someone is doing work on it, and forgot to tell anyone and made a mistake?<br>
<br>
All of these are possible, and while some are more likely than others, and could be used to prioritize where we start looking, the question remains:&nbsp;&nbsp;What do we know?<br>
<br>
What we have experienced so far, and what we really know, is that we got an alert of "HTTP test failure", and this has something to do with our web server environment returning correct results to the monitor health checks.<br>
<br>
This is all we know in this circumstance.<br>
<br>
Was there a bad code push?&nbsp;&nbsp;We don't know, because we haven't made it part of our example.&nbsp;&nbsp;Let's add some data around that.<br>
<br>
We have 2 options:<br>
<br>
- We ask developers or release engineers (or whomever, for this purpose we will say "release engineers") if they have recently pushed any code.<br>
- We go and look to see if the code has been updated.<br>
<br>
Both of these options will yield us new information we can work from, but will each of them give us solid information?<br>
<br>
Asking the release engineers will give us the hear-say information that whoever we asked gives their best current information.&nbsp;&nbsp;Do they check first before responding, to see if anyone has pushed code lately, or do they use their current information to tell us?<br>
<br>
If they say, "No, no one has pushed any code lately.&nbsp;&nbsp;We won't be doing that until X time", then we will leave that conversation with information that says no new code was recently pushed, and we will have impetus to de-prioritize the possibility of new-bad code being pushed into production causing the monitoring alert.<br>
<br>
But is this solid information?&nbsp;&nbsp;They may be the only person who does the code pushes, and so they may be the "definitive" answer on the subject, but what if someone new accidentally did it for some reason?&nbsp;&nbsp;The "definitive" person would not know this, unless they checked, and their information would not be congruent with reality.<br>
<br>
If we take the second option, and we look for ourselves, then we can see if the timestamps on the files have been updated, or if the log files say that the web or application servers have been reloaded.<br>
<br>
The second option gives us information that we have personal experience with, and this is solid information.&nbsp;&nbsp;If we do not have access to go look ourselves, then the next best thing would be getting someone who does have access to verify it themselves and preferably show us the result, but they could also provide unique information such as "X was the last time code was pushed", instead of a more vague answer like "No, no code has been pushed lately".<br>
<br>
So we have two lessons we can take from this example problem.&nbsp;&nbsp;One, that information we have personal experience on is better than hear-say information, or information we do not have personal experience with.&nbsp;&nbsp;Second, that there are degrees to "information solidity", or the reality-based nature of the information.<br>
<br>
Looking ourselves yields the highest relation to reality.&nbsp;&nbsp;We were there, we looked at the information, and it said "X".&nbsp;&nbsp;We have very high reliability with this information, as long as we were paying attention to what "X" was, and paid attention to get into the right position to look at the right data (not accidentally looking in a different server or directory, at the wrong files), then we have solid actionable information to work from.<br>
<br>
This would be the same level of information if someone else did this work, but showed us while they did it.&nbsp;&nbsp;We saw them do it, we saw the results.&nbsp;&nbsp;It would take some acts of deception to make this data questionable, and since we are referring to working in a work-environment, we will assume that all people are behaving as Good Actors for these examples.&nbsp;&nbsp;Later, we will also look at how some people act as Bad Actors, and can create bad data, for instance trying to hide a mistake that have made.&nbsp;&nbsp;(We could call this section, "Do you even audit, bro?")<br>
<br>
Less reliable is information that someone told us they looked, but did not show us, and gave us exact data, such as "X was the last time code was pushed, I checked the directory timestamps and logs".&nbsp;&nbsp;This is good data, but we do not have personal experience with it, so it is less-good than data we verified ourselves.<br>
<br>
Next, we have a situation where someone else tells us "No, no code was pushed recently".&nbsp;&nbsp;This is not data we have verified ourselves, so we have no personal experience with it, and it is not specific as to when the code was actually released.&nbsp;&nbsp;It is possible that this person did not check, and is just telling us from their own perspective that they don't believe it was pushed recently.&nbsp;&nbsp;This is beginning to be invalid data.&nbsp;&nbsp;<br>
<br>
We could still ascribe Good Actor behavior to this person, and take them for their word, however, what will be the result if we do take them at their word, and de-prioritize looking at a bad code release, and start looking at other problems.&nbsp;&nbsp;We end up exhausting the search on other things, and much down-time has accrued with the "HTTP test failure" alert still going off, and eventually someone looks and see that indeed new code was pushed out, and it contained a bug.<br>
<br>
Rolling back the code resolves the problem, and the HTTP server starts to return correct tests to the monitoring system.<br>
<br>
Much of the downtime accrued because of working with non-verified information could have been avoided by getting personal verification of the exact time of the last code push.&nbsp;&nbsp;I have seen this exact situation happen many times, and bad-code or bad-configuration changes are one of the most common outages for networked services.<br>
<br>
Even though these are common, the common-ness alone does not mean that it is solid information.&nbsp;&nbsp;It only means it is something that should be verified quickly to see if it is a contender for causing the problem.<br>
<br>
We will be exploring the idea of what makes good information in detail in this book, and I will change this introductory terminology of "solid information" into a more precise definition of Intelligence, which we can categorize in many ways:&nbsp;&nbsp;Verified, Unverified, Actionable, Unactionable, etc.<br>
<h2 id=10fc971fd9dc706d141c5ada28fd9ae3><a href="#10fc971fd9dc706d141c5ada28fd9ae3">2.3</a>: What is Operations?</h2>
<br>
Keeping up our short tradition of asking questions that seem pointlessly basic, I will ask:&nbsp;&nbsp;What is operations?<br>
<br>
Why do we do what we do?&nbsp;&nbsp;Why does it exist?&nbsp;&nbsp;What is it?&nbsp;&nbsp;What are the goals?&nbsp;&nbsp;What are the priorities?&nbsp;&nbsp;What are the procedures that makes up an Operations department?<br>
<br>
The more questions that are asked, stemming from the original question, the less the question seems to be pointless, and the more the questions start to become the ones we deal with every day.&nbsp;&nbsp;But, we skip the first question.&nbsp;&nbsp;Why?<br>
<br>
We skip it because we already assume that we all know the answer, and that we are already in agreement about the answer.&nbsp;&nbsp;It is taken as a given, but in my experience, there are many differences of opinions in even the most basic answers to what it is.<br>
<br>
People have different values, and they have different skills and personal experiences, and from these, they have a world-view that is also different.<br>
<br>
Getting to the fundamentals of what we mean by something like "Operations" means that we can start to align our views, and in aligning our views, we will communicate more effectively, and become able to work more effectively together.<br>
<br>
It is really these fundamental issues that make communication so hard and ineffective, because we do not drop down to discussing what we are fundamentally doing, and get buy-in from everyone on the team about each of the layers in the stack of what makes up an environment's operations.<br>
<br>
So, what is operations?<br>
<h3 id=0671652556ae5d62c827e6db8082bab7><a href="#0671652556ae5d62c827e6db8082bab7">2.3.1</a>: Operations is about Control</h3>
<br>
I will posit that the primary thing that operations is about is Control.<br>
<br>
Why control?&nbsp;&nbsp;Why not up-time, availability, responsiveness to business direction, or any other valid priority?<br>
<br>
My reason for this is that without control, you cannot be efficient in any other areas.&nbsp;&nbsp;You can only be as efficient as your level of control allows you to be.<br>
<br>
You can always make progress in any area by applying resources to it:&nbsp;&nbsp;people, time, money, hardware, etc.&nbsp;&nbsp;<br>
<br>
These will make progress on problems you have and want to solve, but the limiting factor to each of them will be your ability to control the environment.<br>
<br>
If you have an up-time failure event, to fix the problem quickly you must be able to determine what is wrong, which takes the ability to gather information, and you must be able to take action to resolve the problem, which takes the ability to change the environment.<br>
<br>
Both of those actions, "gather information" and "change the environment" have Control as a central tenet.&nbsp;&nbsp;<br>
<br>
How can you gather information without the control of the environment to yield you information?&nbsp;&nbsp;In the most basic example, if you do not have access to the information, you cannot gather it, and you certainly do not have control over it.<br>
<br>
If you do not have access to change the environment, you cannot change it, and do not have control over it.&nbsp;&nbsp;<br>
<br>
Like many things, Control can be seen a spectrum.&nbsp;&nbsp;We can illustrate in on a line segment, such as:<br>
<br>
No Control <-----> Total Control<br>
<br>
This spectrum would represent all possibilities of "Control", having no control, and having total control.<br>
<br>
Control is a tricky subject, in that it is not only un-real (Virtual), but it is even more Virtual than many other things, because it more like a concept than something that is valid data.<br>
<br>
Unlike other Virtual (non-real) things, Control cannot be verified like data can be verified.<br>
<br>
If I have a variable "X" and I set X to 5 (X=5), and then I check if X is 5 (X==5?), I can get a result that is True or False.&nbsp;&nbsp;X is either 5 or it isn't.<br>
<br>
But with a concept like "Control", there is no way to check that you have control or not.&nbsp;&nbsp;You can check that you have access to some data, which is an aspect of control, and you can check if you can change data (by changing it, or looking at permissions (less good)), and this tells you more aspects about control, but there are so many other things that go into this that are very difficult to inspect or verify.<br>
<br>
For instance, one aspect of Control is, "Do we have enough time to do the work we need to do?"&nbsp;&nbsp;This is an aspect of controlling one's schedule, so that good work can be produced.<br>
<br>
If we do not have control over our schedules, and work is required to be done before it can be done to our satisfaction of "good work", then we do not have control over this, and we will see problems arise from this fact.<br>
<br>
There are many other aspects of Control that we will look at, and I will make more cases on why I believe this is the central tenet of Operations and why understanding what you do have good control over, and do not have good control over is very valuable and actionable information.<br>
<p id=126b3100e0bafcd606cdb539413d4ce5><b><a href="#126b3100e0bafcd606cdb539413d4ce5">2.3.1.1</a>: "De facto" Ops vs. "Planned/Controlled" Ops</b></p>
<br>
If Control is the central tenet of Operations, what is the opposite side of the spectrum?&nbsp;&nbsp;Uncontrolled operations?<br>
<br>
I think it's clearer to say that the opposite side of the spectrum from control is "de facto" operations.&nbsp;&nbsp;What simply happens because there are business goals that need to be solved, and resources were put towards solving them, again and again.<br>
<br>
It is fairly easy, in my experience, to handle every situation in an efficient manner for the problem at hand, and still end up with a total mess of an operations environment, because the actions while individually efficient do not work together as a whole efficiently.&nbsp;&nbsp;The total set of actions have poor Alignment.<br>
<br>
This is often seen in naming conventions that change frequently, or that you could say there is not really a "convention" to the naming of things.&nbsp;&nbsp;The same goes with what kind of hardware you purchase, if every time you purchase hardware you pick the "right tool for the job", but you end up with unique hardware configurations for every problem solved that required a purchase, then you have N number of hardware configurations to support and manage.&nbsp;&nbsp;How does that impact your overall efficiency at supporting these systems?&nbsp;&nbsp;It was individually efficient up-front, but how is the efficiency after the up-front cost?&nbsp;&nbsp;Which cost is more over it's life-time, the up-front cost or the maintenance costs?<br>
<br>
The maintenance work to keeping many hardware configurations versus a limited number (say 2-4 unique hardware specifications per generation of hardware purchases), will mean many more problems have to be solved in upgrading software, and many more security and firmware upgrades will need to be tested.&nbsp;&nbsp;It can easily create a situation that either requires many people to support, or more likely it is not worth the cost of actively supporting everything, and so support is only assigned when a high priority problem arises to keep personnel costs down.<br>
<br>
"De facto" just means "In reality", but in common terms it means "the way things happens", like "this is what has been created from our low-coordinated efforts".<br>
<br>
So a spectrum for Control would look like:<br>
<br>
De Facto <----> Planned<br>
<br>
Planned operations will have strict naming conventions, where all the data required to be derived from data embedded in the name, and when new services, products, environments, and other things arrive, they are intelligently inserted into the existing convention, and they do not create new conventions (without just cause), and they do not arbitrarily add new components or re-use existing components for different purposes (without just cause).<br>
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
- No "funny" or special names for machines.&nbsp;&nbsp;"monkeyknifefight" is great imagery, and fun to say, but it has no business in your operational data.&nbsp;&nbsp;It does not explain what services are provided, who owns the machine, where it is located, or any other actionable information.&nbsp;&nbsp;It is essentially dis-information, since you know less about the machine then if it was called "misc" or "general".<br>
<br>
- In a planned naming structure, all names have the same number of elements, and the elements are in the same order, and written in the same sequence and pattern.<br>
<br>
In the list I have just made up, you can tell a number of things about any of the given hostnames' servers:&nbsp;&nbsp;<br>
<br>
What general function they provide (web, git, redis).&nbsp;&nbsp;<br>
<br>
What location is the server in?&nbsp;&nbsp;SJC and NYC seems to be our options.&nbsp;&nbsp;This is much clearer than "sf", as they are airport codes, and so provide more localized information than city or regional data does.<br>
<br>
What environment is this used for?&nbsp;&nbsp;Production, staging, QA, corporate?<br>
<br>
What instance number of the service is this?&nbsp;&nbsp;001, 010?&nbsp;&nbsp;<br>
<br>
In addition, the instance numbers are always written in the same format, providing a standard for where to start a new service:&nbsp;&nbsp;001 (or 000, if you prefer cardinal counting)<br>
<br>
The planned naming convention can scale significantly, while keeping a pattern that fits any of the machines, new or old.&nbsp;&nbsp;Selecting the proper format for naming hosts is so important, because it is a direct factor in Control.<br>
<br>
If you cannot name something accurately, how can you control it?&nbsp;&nbsp;How can I access a server, if I do not know it's name?&nbsp;&nbsp;How can I change the state of a server, if I do not know it's name?<br>
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
This creates problems every time someone tries to work on these machines.&nbsp;&nbsp;Logging into any given machine takes either trial-and-error, memorization, or looking it up.&nbsp;&nbsp;Each of these is inefficient in time and personnel resources, and as the site scales up (more servers, more services), these kinds of time-personnel costs start to become major factors in both how much work can be accomplished in a given period of time, how frequently mistakes are made (not updating all the servers in the same fashion, performing work on the wrong servers), how long it takes to train new employees, and how well any employee really knows the environment.<br>
<br>
We are probably in agreement that planned naming conventions is better than unplanned or de facto naming conventions, but we are engineers, and it is not enough to think something is better, we require being able to dissect the issue to see what the components make it up, so that we can build it better for our specific needs, for any given circumstance, to create the most efficient solution for that specific circumstance.<br>
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
These are the components that make up this name.&nbsp;&nbsp;Do we have the right components for our current needs?&nbsp;&nbsp;What about our future needs?<br>
<br>
One can certainly over-engineer a problem and "prematurely optimize" it against future concerns, but not looking at what is likely to come in the future is on an extreme side of the spectrum for planning for the future.&nbsp;&nbsp;Let's make a spectrum for this:<br>
<br>
No Planning <---> Every Detail Planned<br>
<br>
We want to be in the middle, but more towards the side of "Every Detail Planned", while minimizing the resources we spend on doing them, to maximize our efficiency.<br>
<br>
Taking each section individually:<br>
<br>
- web<br>
<br>
This seems pretty self-explanatory.&nbsp;&nbsp;If we call things "web" servers, and they do "web" things, and we don't have other services that also do the same thing in the same environment and could cause confusion, this is good enough.<br>
<br>
If we do have other services that do the same or similar things, we might need some alternative names, such as "app", "webmain", or "webfront" or something similar.&nbsp;&nbsp;Try to make it what people in your environment call it verbally, and there will be less confusion when switching from discussions to typing in data.<br>
<br>
I will call this first part of a naming convention our "Host Class".&nbsp;&nbsp;So machines hostnames that start with "web" have a Host Class of "web".<br>
<br>
- 001<br>
<br>
This is our Instance number.&nbsp;&nbsp;It is the first (or second if starting from 000) machine in in the "web" Host Class.<br>
<br>
This has an obvious limit of stopping at 999, and then the naming convention reaches it's limit.&nbsp;&nbsp;Many organizations will never have more than 999 servers of any type, but this is not a reason to fail to plan for the case of scaling past that point.<br>
<br>
It costs very little to make a good naming convention, and only requires diligence and checking your work to ensure that no one creates names they should not, and it will save much pain in having issues with naming down the line.<br>
<br>
Scripts are written whose logic may not be able to deal with naming conventions that change, and this can cause problems in your environment as you pass these thresholds.&nbsp;&nbsp;We'll cover how to solve this shortly.<br>
<br>
- product<br>
<br>
This is an example product name for your organization.&nbsp;&nbsp;This should be a short product, project or service name that clearly differentiates it's purpose from other products, projects or services.&nbsp;&nbsp;Notice in the example I use "product" and "infra" to differentiate the organization's product, which may generate revenue, from the infrastructure services used to support the product's operational environment.<br>
<br>
- prod<br>
<br>
This is an "environment" description, and differentiates machines in production (being used by end-users, or running financially impacting services), differentiating it from servers performing the same actions, but that run in development, QA, staging, corporate, or other environments which have different users and impact if they go down or degrade.<br>
<br>
Common examples:&nbsp;&nbsp;prod, stage, qa, dev, corp, net<br>
<br>
- sjc<br>
<br>
This is the location of the datacenter the server is in.&nbsp;&nbsp;Whether it is a closet, or a Tier-4 Gold data center, you have assigned a location to it, so no one has to guess.&nbsp;&nbsp;If you are consistent and only put the correct location labels into the hostnames, you will not have confusion over where machines physically reside when this becomes an issue, say for maintenance, repairs, networking changes or migrations.&nbsp;&nbsp;If you are shutting down a datacenter, you definitely want to know all the machines in that datacenter, so you can migrate their services and not miss anything.<br>
<br>
Using airport codes, of the airport closest to the location, is a common practice and a good one.&nbsp;&nbsp;It allows being fairly specific, but not having to debate over whether something is inside this-or-that region.&nbsp;&nbsp;Simply find the closest airport with a 3-letter airport code and use that.&nbsp;&nbsp;It doesn't matter how big the airport is, if it is a registered airport it is guaranteed to be unique and give you a latitude and longitude to the general area in a consistent manner.<br>
<br>
- domain.com<br>
<br>
The example domain of our example organization.&nbsp;&nbsp;The important part here is that it is consistent.<br>
<br>
There is a difference between internal names and external names, in that internal names can be kept consistent with the work of the Operations department, but external names are frequently under the control of other departments such as Marketing, Business Development, Sales, etc.<br>
<br>
As such, they should be treated differently.&nbsp;&nbsp;Internal names should be rigidly controlled, and external names should come with high recommendations for using naming conventions.&nbsp;&nbsp;You could even provide several different recommendations for external naming conventions, to try to get other departments to constrain themselves and avoiding total naming-anarchy.&nbsp;&nbsp;Without having control, you should expect "de facto" results, and prepare for those accordingly.<br>
``<br>
{{ aside_begin }}<br>
Frequently non-Operations departments do not understand the use of sub-domains like "product.domain.com", and will create new base level domains for every project.&nbsp;&nbsp;Sometimes this is required (legal and business reasons) and other times, it is only because they didnt know they could have "newproduct.domain.com".&nbsp;&nbsp;This is especially a problem for certificates, like for HTTPS, as new domains require new certs and updating them every year or so, while sub-domains may use star-certs (*.domain.com), and roll up hundreds of sub-domains under a single certificate to manage them.<br>
{{ aside_end }}<br>
<br>
<br>
Now that we have gone over a bit about the initial planned naming convention, let's make it better.&nbsp;&nbsp;Here is a proposal:<br>
<br>
- web-1-001.product.prod.sjc1.domain.com<br>
<br>
I have only added 3 characters to this name, but I have made it both significantly more scalable, and provided a new level of control.<br>
<br>
First, how is it more scalable than the previous naming convention of "web-001.product.prod.sjc.domain.com"?<br>
<br>
It is more scalable in 2 ways.<br>
<br>
First, it is more scalable in the location.&nbsp;&nbsp;Previously we had "sjc", which meant that the server was located near the closest airport code of SJC (San Jose, California), but which data center is this?<br>
<br>
If you only have 1 data center, then you know.&nbsp;&nbsp;But what if you get a second data center, for redundancy or growth?&nbsp;&nbsp;What do you name it?&nbsp;&nbsp;sjc2?&nbsp;&nbsp;<br>
<br>
If you name the second data center "sjc2" and the first was "sjc", you now have a naming convention discrepency.&nbsp;&nbsp;You previously had 3 letters, now you have 3 letters and 1 number.&nbsp;&nbsp;This can create parsing problems in scripts, and is inconsistent when you type names.&nbsp;&nbsp;As you grow in number of data centers in the SJC area, you will have more problems when "sjc3" and "sjc4" are consistent, but the original "sjc" is not.<br>
<br>
If you know that something is likely to grow in count, then you should start with a numerical indicator from the beginning.<br>
<br>
When we hit "sjc10" we have changed the number of total characters for this section, which we are trying to avoid in other areas, but the number of characters has changed in a deterministic manner, so we can deal with it efficiently and it still scales.&nbsp;&nbsp;The original 3 letter airport code still stays 3 characters, and the attached number is parsed as a normal number would be.&nbsp;&nbsp;The string is also split on periods ("."), so everything remains very regular, and whether you account for this scaling change in your original code or not, it is a small addition in logic up-front, and a modest change to logic at-scaling-time.&nbsp;&nbsp;<br>
<br>
This makes it more dynamic, yet still scalable, and so has preference over sjc01 or sjc001, which account for limited growth (100 possibilities), or a large growth (1000 possibilities), but which are immediately more wasteful, mostly in terms of parsing and typing for humans.&nbsp;&nbsp;This is the tradeoff being made here each time we choose to prepend zeros, or choose not to.<br>
<br>
What about "product", is it likely to grow in count too?&nbsp;&nbsp;No, there is not necessarily a requirement for this.&nbsp;&nbsp;If a new product does come out that is called "product2", then it is still differentiated from "product", and while it shares the same look and feel as the datacenter location scaling problem, it is actually a different type of scaling, because each of these products is unique and naming them is a business-customer function, not an engineering-infrastructure function.&nbsp;&nbsp;We will simply shorten the name into an "alias" that is engineering-infrastructure friendly, and also to avoid any renaming that the product line goes through.<br>
<br>
{{ aside_begin }}<br>
Often marketing and sales departments will rename a product many times, both before it is launched, and after it is launched, and sometimes "newer versions" of the same product will be renamed, and "older versions" may have the same old name, or may also change names.<br>
<br>
All of this name changing is an important part of Sales, Marketing, Branding, etc, but it has nothing to do with engineering or operations.&nbsp;&nbsp;In fact, it is completely against our interests to change the name, ever.&nbsp;&nbsp;No matter what happens outside the company, the internal name should not change, because the costs associated with internal name changes are high, and rewards of internal name changes are essentially non-existent.<br>
<br>
People from outside the Engineering and Operations departments may not share these values, but they are not tasked with performing actions in the engineering or operational realms, so their opinions are valid for themselves, but carry no engineering weight.<br>
<br>
As such, I recommend making internal engineering names that are unrelated to the product names.&nbsp;&nbsp;They can be related informally, such as one happened to use the name of the original project as the name, and we simply keep that name as the internal name, even if later on it sounds silly or incorrect.&nbsp;&nbsp;Think of it like a code name.<br>
<br>
Additionally, when new versions of that product come out, do not be swayed easily to changing the product name.&nbsp;&nbsp;If it is in the same "product line", then simply add additional versioning information such as "project" becoming "project2" or "project2016" or "project201605", etc.&nbsp;&nbsp;These are essentially generic labels, which can be ascribed to the work we are doing accurately, and then can be sold to customers in any way the business likes, unrelated to our internal terminology.<br>
<br>
Avoid the loss of productive work time, insertion of data mis-alignment and other bugs, loss of opportunity, now-incorrect documentation, and general confusion added by renaming projects.&nbsp;&nbsp;Simply name projects something simple (that describes it generally), or code-word related (that doesn't describe it), or any other short and machine-friendly-character-set-constructed (makes good Host Class names, or at least a good variable name), and then iterate on that label, ignoring what the advertising and branding names are.&nbsp;&nbsp;Focus on engineering and operational stability and accuracy, and keep sales and engineering separated by what customers can actually see.<br>
{{ aside_end }}<br>
<br>
This is likely to be controversial, as it is difficult to back up with solid data quickly, so we will cover how to differentiate data like this later to keep the pace moving along.<br>
<br>
The second way it is more scalable is that we have a secondary numerical counter for the Host Class.&nbsp;&nbsp;"001" has now become "1-001".<br>
<br>
This provides 2 methods of scaling.&nbsp;&nbsp;For Host Classes that merely collect a lot of servers, this means we can use the same naming convention once we pass "999" instances for the "web" Host Class in our production SJC facility for our given product.<br>
<br>
This would look like:&nbsp;&nbsp;web-2-001.product.prod.sjc1.domain.com<br>
<br>
However, many services have a more interesting use case for this number than simply rolling over at 1000, which is separating sets of machines that hold related information.&nbsp;&nbsp;Consider these names:<br>
<br>
- redis-1-001.product.prod.sjc1.domain.com<br>
- redis-1-002.product.prod.sjc1.domain.com<br>
- redis-2-001.product.prod.sjc1.domain.com<br>
- redis-2-002.product.prod.sjc1.domain.com<br>
<br>
These are 4 machines, grouped into 2 sets of 2:&nbsp;&nbsp;1-001/1-002 and 2-001/2-002<br>
<br>
These can be used in many ways, but one way would be that this represents a Master-Slave relationship of data being written and read to 1-001 and 2-001, until one of those machines goes down, and then the other would take over such as 1-001 going down, it would be: 1-002 and 2-001 which are active for reads and writes.<br>
<br>
What data is sent to each of these machines could be done based on doing a modulus of an index ID (shard = index_id % 2), or another lookup method (rings, partitions, etc).<br>
<br>
In this case I refer to the first number as the "Shard" and the second number as the "Shard Instance", so redis-1-001 is Shard 1, Shard Instance 001.<br>
<br>
This is a very scalable naming convention.&nbsp;&nbsp;It allows for different Host Classes (web), different Shards of data (-1-), different instances in the shards (-001.), different products (.product.), different environments (.prod., .qa.), different data centers (.sjc1.) and the common domain name for internal server hostnames.<br>
<br>
Separate from being scalable, this also provides a new layer of Control.<br>
<br>
Data in Shard 1 is different than data in Shard 2, and may even have different logic operate against it.&nbsp;&nbsp;This is more easily handled than differentiating "redis-001, redis-002" from "redis-003, redis-004" for logic that groups data on servers by their position in a sequentially numbered set of server instances.<br>
<br>
It is generally better still to use the same logic on all Host Classes of type "redis" and merely differentiate the data sets by the Shard, but if you have grouped the Shards as different distinct numbers, you have this additional ability to control them accurately based on this data.<br>
<br>
There are other ways of organizing this data into names, and it depends on what data you need to track, but starting from a naming convention like this when you don't yet have that information is a safer bet than starting with less planning than this.<br>
<br>
If you know you have additional requirements, be sure that they are implemented into the naming convention, and kept in the standard.&nbsp;&nbsp;This is a good standard to be extremely rigid with, as the benefits for having consistent naming are large and increase over time.&nbsp;&nbsp;<br>
<br>
If you already have a naming convention, it is better to stay with it than to change it, but if you do need to change it, it is better to make a new standard, and make all new machines comply with it (if they are not in existing services with the old naming convention).<br>
<br>
This way you can at least control your naming conventions in a generational sense, and if you are doing planned work, you should have a very limited number of total generations.<br>
<br>
There is a lot more that could be said on just this example, and we will come back to it later, as naming things is, after all, one of the two hard computer problems, along with cache poisoning and off-by-one errors.<br>
<p id=e6f860a586c5005530de3736bbf50109><b><a href="#e6f860a586c5005530de3736bbf50109">2.3.1.2</a>: Alignment takes "vision" and knowledge</b></p>
<br>
Another important aspect of operational engineering, and engineering in general, is "Alignment".<br>
<br>
Things must Align with each other for their full efficiency to be able to be available.&nbsp;&nbsp;This is easy to see in the physical world: all sections of a bridge must align with one another, fence parts must be in alignment to be a good fence, and support beams must align with each other to provide continuous support in a large building.&nbsp;&nbsp;Engine linkages must align with transmissions and so on, all things that must work efficiently must have high levels of Alignment in order to do so.<br>
<br>
It is no less important in the virtual world.&nbsp;&nbsp;The entire field of networking is about aligning physical cables and virtual configuration to move frames and packets from source to destination.&nbsp;&nbsp;Databases are about aligning data together so that it can be stored and retrieved efficiently.&nbsp;&nbsp;Software is the alignment of a starting set of data, transitioning through consecutive state changes until a result is produced; each of those state changes must be in perfect Alignment to produce that result; with any change a different result would occur.<br>
<br>
Everywhere you look alignment is an important factor on the quality, reliability, resilience, and structure and yet like many fundamental aspects of engineering, this topic itself is not discussed directly, and typically indirectly discussed as in how "everything must match up" given different protocols.<br>
<br>
You may see where I'm starting to go at this point with all of these fundamental questions and inspections:&nbsp;&nbsp;these are fundamentals of engineering that we are using every day, but are not being discussed directly in our conversations about our environment, resources, goals, and what we are going to do to achieve our goals.<br>
<br>
This lack of introspection of our process results in a lot of miscommunication, and different visions struggling for the chance of being implemented, but without the necessary alignment between all the points of implementation to give us the kind of efficiencies, resiliency and other effects that we desire.<br>
<br>
Having this vision requires being able to see "the big picture" as well as the details, and it is important to be able to go from detail to big picture, back to details again repeatedly to see what any proposed changes will mean with regard to aligning with the rest of our details, to create the final result which occurs when all of those details are taken in whole.<br>
<br>
This is the methodology I use in designing any solution, and I will try to describe it in enough detail that you can inspect the process for yourself and can hopefully positively supplement your current methods for doing similar activities.<br>
<br>
One thing about "vision" is that it is something that takes a bit of experience to be able to see.&nbsp;&nbsp;One needs to have had personal experience implementing things to really know what effects will result in the implementation, and across enough areas of the environment so that one can see how things align well or do not align well.<br>
<br>
This experience is less about how many years one has worked in an industry or environment, and more about the experiences one has had in one's lifetime.&nbsp;&nbsp;<br>
<br>
If you have never worked in the industry before, you will not know how organizations that run production operations, especially internet facing production operations at large scale (which I use as an extreme end of the scaling spectrum), will function and what changes will do those organizations and operating environments.<br>
<br>
The more you work in different environments, and complete more areas of implementation, the more experiences you will gain.&nbsp;&nbsp;You can supplement these by setting up your own virtual environments on any cloud hosting providers, or on your own machines with a series of virtual machines.<br>
<br>
All projects, whether in-industry or outside of it, are limited, and never give complete information, because one's viewpoint is limited and the amount of details one can interact with is limited.&nbsp;&nbsp;So even if you know one environment from beginning to end, having created all of it, you will find another environment that you didn't create to have many different properties, even if all the software used is the same, due to the alignment choices made in it's creation.<br>
<h3 id=7bdf31941d762810d8c81c360d28d38c><a href="#7bdf31941d762810d8c81c360d28d38c">2.3.2</a>: An Explanation of Operations</h3>
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
Each department in an organization thinks it is a critical department, and they are all right.&nbsp;&nbsp;No organization would pay the financial and opportunity costs in maintaining any department that is unnecessary, so they are all critical.&nbsp;&nbsp;Operations is no different here.<br>
<br>
There was a time that operations was a lot more like Facilities departments, they bought things and maintained them.&nbsp;&nbsp;Keeping them powered up and plugged in, and keeping people from stealing or damaging them.&nbsp;&nbsp;This is not really accurate, but from the perspectives of people paying for these employees, it is pretty close to accurate, and we are currently discussing how organizations see themselves and their actions, and organizations act through using money to pay for services.<br>
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
- Physical good company.&nbsp;&nbsp;Makes things that are sold in metal cans, etc:<br>
	- Supply chain management has a basis in digital records at every step.&nbsp;&nbsp;Some steps involve calling people, writing things on paper, but these are recorded in at least Excel type spread sheets, and at any larger organizations something more similar to an Enterprise Resource Planning (ERP) software to coordinate all the steps are required.<br>
<br>
	- Communication with vendors in the chain may have many physical components, but ultimately they are also recorded into digital mediums, at least the low-level of email, if not higher level tracking software.<br>
<br>
	- Employee time and pay records are now kept in a mostly or purely digital form.<br>
<br>
	- End-user support is typically done via electronic medium (emails, customer support) to <br>
<br>
	- The larger the organization for all non-Internet based companies, the more corporate infrastructure that will be needed to provide support to desktops, laptops, servers to manage directory services (AD/LDAP), backups, storage, centralized software, etc.&nbsp;&nbsp;More of these services are moving into online-only for small-medium companies.<br>
<br>
	- Hold outs will be older (pre-PC age computers) and will need to be small, to maintain operating the manual labor scales<br>
<br>
- Non-Internet Services Company<br>
	- Similar to physical companies, but with more smaller companies that can get by without much technology.&nbsp;&nbsp;Real estate agents are a famous example of this.&nbsp;&nbsp;Doctors and lawyers are also slow to adopt technology in tracking their clients and work, but in most medical institutes I have seen recently, all patient visit tracking is being digitally tracked.<br>
<br>
- Physical software companies<br>
	- Software is sold in boxes, in stores or shipped via the mail on DVDs.<br>
<br>
	- All software is written in a networked environment which must remain up for any productivity.&nbsp;&nbsp;Developers cannot all go home and continue working if the infrastructure going down, and as security levels increase, this is not possible for those reasons as well.<br>
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
- Not properly staffing their operation teams for the workloads they are required to perform.&nbsp;&nbsp;Note that it doesn't matter *who* the operation team staff is, System Administrators, Site Reliability Engineers, DevOps, Developers, it doesn't matter.&nbsp;&nbsp;If they are responsible for the operations of the software and systems, they are the operations team.<br>
<br>
- Not giving proper lead times on work that is due, such as finishing a project that the operations team was not notified about, and expecting an immediate release to the public of that project.&nbsp;&nbsp;Not taking into account either ordering hardware, or configuring systems to support the software.<br>
<br>
- Not giving significant information on how to maintain, run, or even install the software to be released and supported.<br>
<br>
- Prioritizing work that does not yield to improving or supporting the revenue generating and employee supporting software and services.<br>
<br>
There are many other symptoms, but these are large enough to illustrate this point.&nbsp;&nbsp;Other departments have similar complaints with regard to notice ahead-of-time, and schedules.&nbsp;&nbsp;See any book on Software Development project management for examples close to operations.<br>
<br>
This is not a problem that is likely to be solved soon, if ever solved, because there are a number of difficult factors that cause it; the primary one being the structure of organizations themselves.&nbsp;&nbsp;When something is structured a certain way, it will tend to produce certain results, and producing different results is very difficult, and often only temporarily possible.<br>
<br>
Since the organizational structure of organizations is not likely to change, the best hope in making progress here is something akin to the Agile movement in development, where all developers just kept repeating the same things and eventually the management of companies started to be populated with managers who also said the same things, and their world changed.<br>
<br>
It's debatable on whether their world really changed that much for the better, but there are many distinct differences in the pre-Agile development world, from the post-Agile development world, and it was this change in perspective and discussing it that caused those changes to take effect.<br>
<br>
It's also worth noting that the way this change-through-repetition occurs should be done with as much awareness as possible of what is being repeated.&nbsp;&nbsp;If it is something that will become a dogmatic problem, then that is not a good thing to repeat.&nbsp;&nbsp;Thing's to repeat should be based on ideas that cause more awareness to the complexities of the present reality and less dogmatic simplicity, which frequently ignores any local data and instead focuses on following idealistic principles.&nbsp;&nbsp;If a principle sounds too idealistic, it probably is.<br>
<p id=5bc4c817bd8491f2de4fcd4fa234cca9><b><a href="#5bc4c817bd8491f2de4fcd4fa234cca9">2.3.2.1</a>: How is this not a core-service?</b></p>
<br>
One concept that organizations have a pretty good grasp on is "core services".&nbsp;&nbsp;They understand there are some services that they cannot outsource to other organizations and remain an efficient operation.<br>
<br>
The core-est of these core services are: management, finance and human resources (HR).<br>
<br>
Almost no organization outsources its' people managers.&nbsp;&nbsp;They are the most core-service that a company has.<br>
<br>
Similarly, there will almost always be at least 1 to several people in the finance department, even if they use external services for many services that used to be hired in-house.<br>
<br>
HR in the past decade has begun to be outsourced, but once a company reaches a certain size, they always have their own HR departments.&nbsp;&nbsp;This is the same for legal services, though this can be configured in a number of ways for companies, so I'm not listing it as a core service.<br>
<br>
Many companies outsource their development departments, and many companies also try to outsource their operation department, though this does not usually last long, and they may try to stick with it by turning their developers into their operations staff, but eventually some people will end up being the de facto operations team, regardless of their titles.<br>
<br>
If a company is primarily a software or internet service organization, and these are the types of companies I focus on, so they will be the majority of what we spend time inspecting, then they are much less likely to outsource their development departments.<br>
<br>
They realize the developing software is a core business service, and without direct control of their developers and efficient communications, they are unlikely to make consistent progress.&nbsp;&nbsp;Many companies that try to outsource this department end up moving it back into their company after poor experiences, unless the product being developed itself is not all that important to the company, or can be treated as a throw-away product (like a phone application they only need to do XYZ "well enough").<br>
<br>
This is all a pretty subjective description, and I won't use up the space to turn it into a more objective one.&nbsp;&nbsp;You should review your own experiences with these descriptions to determine how accurate they seem to you.<br>
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
- Operations is like the tires of the car.&nbsp;&nbsp;We are the part of the car that comes into contact with the road.&nbsp;&nbsp;Your driving can only be as good as your traction against the ground.&nbsp;&nbsp;If you lose a tire, your ability to drive is severely impacted or not possible. <br>
<br>
- Operations are like the roads.&nbsp;&nbsp;You can have a fleet of cars or trucks, but you cannot efficiently move them around without roads to provide consistent surfaces.<br>
<br>
A lot of people shop for cars, but not a lot of people are involved in the building or maintenance of roads.&nbsp;&nbsp;This is similar to many people using networked services, but not being aware of what it takes to build or maintain them.<br>
<p id=109a7a222581029b6b3ed44aeb36acbc><b><a href="#109a7a222581029b6b3ed44aeb36acbc">2.3.2.1.1</a>: Just because it's Core doesnt mean...</b></p>
<br>
A service may be a core service, but that does not mean all of it needs to be internally owned and operated.<br>
<br>
Cloud datacenter operations and Software-as-a-Service (SaaS) have changed the way many companies perform their internal and external operations, and has provided new ways for many engineers to think about solving problems.<br>
<br>
Just because you are paying someone else to maintain hardware or software for you does not mean that you do not need to manage it.&nbsp;&nbsp;Some SaaS products do not require much management, but other still requires one or more full time staff to help manage it for the rest of the departments.<br>
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
Outsourcing works up until the point where you lose Control that you need over the environment.&nbsp;&nbsp;At some scaling point in every organizations usage of an external service, their needs and the services offerings will start to part ways, and the service will start requiring more work than previous to perform the same benefits for the organization.<br>
<br>
Once this reaches a critical point, either though financial cost, personnel time cost, or cost in terms of outages, degraded performance or misalignment in terms of providing the kinds of services the organization requires.<br>
<br>
Once this point is met, there will be a new transition where the problem areas are migrated to another service, which it is hoped will solve these problems, or the services are migrated in-house to be internally managed.<br>
<br>
At present the financial costs alone seem to be consistently measuring up like this:<br>
<br>
- Internally managed infrastructure.&nbsp;&nbsp;1x cost, of hardware, data center and network services to provide an operational environment.&nbsp;&nbsp;This is the base-line, doing it yourself.<br>
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
This 1-factor look at the problem, financially, is not a "big picture" view, it is only a single detail, so there are many other factors which make using services that may be 5x or 3x as expensive, and provide worthwhile benefits, such as the total cost being low enough to be worth it, or the faster turn around time on new machines, or not having decided on the hardware requirements to make it practical to start ordering hardware yourselves.<br>
<br>
There are many more factors in this, and we will get into some of them later, but they are not the focus of this book, so we will not cover them comprehensively.<br>
<p id=0932b206900bdd69c2b6cc7a46dfee68><b><a href="#0932b206900bdd69c2b6cc7a46dfee68">2.3.2.1.1.1</a>: Typically companies still don't...</b></p>
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
Knowing this, how do you get ahead of this problem?&nbsp;&nbsp;You can't completely solve it, as it requires cooperation from other people, and the root of the problem is that they themselves aren't coming forward to cooperate before they normally would.<br>
<br>
Some things you can do:<br>
<br>
- Regularly, say every month, send out a standard template communication (email, etc) to all departments asking if they have any projects that will coming down the pipeline and will need operational resources.<br>
<br>
- Describe in the communication what "requires operational resources" means, such as machines in production, adding a new service, making changes to services which aren't already in production or that the operations department doesn't know about, etc.<br>
<br>
- Describe any lead-times you require for these types of projects.<br>
<br>
This is the direct-but-passive communication approach, and will allow people who are up for communicating ahead of time to communicate with you in a way they can understand is helpful.&nbsp;&nbsp;This will not catch all new projects.<br>
<br>
From there you can also create a department policy, document it in your online documentation site (wiki, etc) as to how you accept new projects, and when people ask you for them,&nbsp;&nbsp;you can refer them to the "new project on-boarding" documentation that describes how you would like to work.<br>
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
<p id=d05edb2ae926b6b3071c2d16497f5721><b><a href="#d05edb2ae926b6b3071c2d16497f5721">2.3.2.1.1.1.1</a>: The Ops department is blamed for all lag</b></p>
<br>
A look at the more negative side of this problem between groups is that the operations departments are often claimed to be creating lag between work being completed by other teams (typically development, sometimes marketing or business development).<br>
<br>
From the perspective of the non-operations teams, this is a true statement.&nbsp;&nbsp;They finished their work, and now they want to put it into production for end-users to be able to access, and any time between them being "finished" and the end-user being able to access the work is considered lag created by the operations department.<br>
<br>
The issue here is one of "someone else's problem" (SEP), which comes down to empathy and a realistic view of the nature of all work involved in a company, not just one's own work in the company.&nbsp;&nbsp;This is not a problem that can be solved directly, as people's ability to appreciate other's position's is not going to change easily, or deterministically.<br>
<br>
So what we can do is to look to ameliorate this problem as much as we can, by getting ahead of the requests.&nbsp;&nbsp;This means having a process that people can easily follow to getting what they want.<br>
<br>
For example, create a limited set of Hardware Specifications that you purchase, for any generation of hardware.&nbsp;&nbsp;The typical basics of this as of 2015 are usually a "utility" class machine, a "relational database" class machine, and a "non-relational database" class machine.<br>
<br>
To simplify what we call a Hardware Specification, let's use the acronym for Stock Keeping Unit (SKU), which is very general.<br>
<br>
Utility class machines are for running general purpose software, and typically are mostly used for web and application services in production.&nbsp;&nbsp;There may be two SKUs if there is a "low memory" and "high memory" version.&nbsp;&nbsp;Caching services (memcache, redis) usually use a low amount of CPU, but a high amount of RAM, and may reside alone on machines due to their critical nature.&nbsp;&nbsp;Utility machines typically do not need much in the way of storage, and almost any small redundant disks are good enough.<br>
<br>
Relational Database class machines are typically used for relational SQL databases like MySQL, PostgreSQL, etc.&nbsp;&nbsp;They need both a lot of RAM, a lot of CPU cores, and they need very fast disk.<br>
<br>
Non-Relational Database class machines are usually running software like Hadoop, Cassandra, or any of the other many column-oriented databases that are better at storing logs, events, time-series than other databases.&nbsp;&nbsp;They typically need a lot of CPU, memory, and much more storage than relational databases.&nbsp;&nbsp;If a relational database might need 5TB of storage, a non-relational database might need 30TB, or something in this type of proportion.&nbsp;&nbsp;Currently (2015), many of these types of systems still use rotating disks as their primary storage as they provide high capacity, and the quick-access times of SSDs are not required (for some platforms), or they may combine SSD with rotating disks for a recent and longer-term storage.<br>
<br>
Starting with these 3 base SKUs, and perhaps several sub-SKUs for more RAM, you can offer departments easy choices for how they want to deploy their software.&nbsp;&nbsp;Providing them virtual machines for some services may also be a good match, depending on their usage patterns and criticality.<br>
<br>
For each type of request they are likely to make, having already worked out in advance what options they will need, in a sort of restaurant-like menu, will allow you to make the requests more streamlined, and work better with your organization.<br>
<br>
You can add SKUs if necessary, when they have a strong need (for example, a large order of systems that have a usage pattern that do not match any of your existing SKUs), and otherwise they have an easier by simply selecting what seems best to them.<br>
<br>
This can also be done for:<br>
<br>
- Networks:&nbsp;&nbsp;Have set ranges of IP space that you assign to a given network, such as standardizing on /23, /22 and /20.&nbsp;&nbsp;If you only create server networks of these sizes, then it should be pretty easy to size them appropriately for a given request that needs their own network.<br>
<br>
- Load Balancing:&nbsp;&nbsp;If you have a pre-determined set of options say using SNAT with X-Forwarded-For for all web services, then you can announce that early, and avoid running into problems where web applications require the source IP in the request.<br>
<br>
- Host names: As we went over earlier, there is a lot of information stored in names.&nbsp;&nbsp;If you give a guideline of what your convention is, and how to apply that convention to various configurations, you can avoid being requested to make names that do not fit the convention, as you have already described how to take their configuration and put it into your naming convention.<br>
<br>
- Accessing production machines:&nbsp;&nbsp;You should have a security policy that can be applied in a standard way to all requests.&nbsp;&nbsp;Do you allow root logins?&nbsp;&nbsp;Root escalation?&nbsp;&nbsp;Sudo?&nbsp;&nbsp;Role accounts?&nbsp;&nbsp;Copying data to machines?&nbsp;&nbsp; You should write each of these things down, and where you do not allow something, you should have a method for how to accomplish that goal in a manner that is consistent with your security policy.&nbsp;&nbsp;If you do not do this, people will just work around your enforcements and create many messes as everyone does it slightly differently.<br>
<br>
It is unlikely that people who perform different roles will start to become empathetic that the work done in others' roles really does take expertise and time, since we have so much history of people not having this empathy, but we can do things to try to bridge these gaps by being aware of them and tuning our behaviors accordingly.<br>
<p id=565cd0fce08c8934484649d6a9f5b105><b><a href="#565cd0fce08c8934484649d6a9f5b105">2.3.2.1.1.1.1.1</a>: Everyone doing everything themselves is...</b></p>
<br>
One important component of all operational environments is standardization.&nbsp;&nbsp;At the extreme end of that spectrum would be uniformity and at the other extreme everything is unique:<br>
<br>
Everything Is Uniform <---> Everything Is Unique<br>
<br>
Since we know that not everything can be uniform, since we are already starting with a base of 3 SKUs (Utility, Relational Database, Non-Relational Database), that side of the spectrum is already constrained.<br>
<br>
However, it is completely possible to have an "everything is unique" operational system, and this might be labelled something like "operational hell", where everything is a special snow-flake one-off case.<br>
<br>
In an "operational hell" environment, no change can be assumed to work for more than 1 specific case.&nbsp;&nbsp;That case must be inspected just prior to being modified, because it could be in any type of state or configuration at all, and the only way to have reasonable confidence that the change will not break things would be to look at everything going on on the machine, all configuration, all currently running processes, and to determine through expert-understanding that the planned change will work with the existing configuration.<br>
<br>
This is the most dangerous type of environment to work in, with regards to uptime, stability, efficiency, and all the other positive attributes we want to imbrue our operational environments with.<br>
<br>
All it takes to create an "everything is unique" environment is to let everyone solve every problem in the way they see best, at the time they got the request, without communicating the changes to others, and aligning the changes so that they follow a planned path.<br>
<br>
Many requests into operations will diff from previous requests in some way, making it impossible for the current request to be handled in the same fashion as the previous request, because of those differences, but still the methods used to take care of the previous and current requests could be aligned with one another.<br>
<br>
This type of alignment does not come for free, and it does not come naturally.&nbsp;&nbsp;It is a process that must be learned, and it takes coordination of all the different members of a team to work together in ensuring that this alignment takes place.<br>
<br>
Alignment itself has a spectrum, and is best seen at different levels of details.<br>
<br>
We can "block box" anything into:&nbsp;&nbsp;Inputs, Outputs, Side-Effects<br>
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
<p id=e08a32902b4d3960b8ee560f8851f34f><b><a href="#e08a32902b4d3960b8ee560f8851f34f">2.3.2.1.1.1.1.2</a>: What can be self-service, and what cant</b></p>
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
I have worked in many organizations where the operations team spends nearly all of their time performing requests, and almost no time improving the infrastructure, and as a result the infrastructure becomes more and more fragile as request after request is done in a manner that is not scalable or supportable, but is required to meet business timelines and direction.&nbsp;&nbsp;In this way the Alignment between all elements of the operational environment becomes worse and worse over time as each one-off request is handled specially and the system becomes more "de facto" and less planned.<br>
<br>
Achieving business goals is the reason all departments exist, so it is a good thing to get the work done, but if it is performed in a manner where the business begins to operate less efficiently over time, and eventually starts to fail frequently, it can cause harm to other business goals, such as customer retention, which effects revenue.&nbsp;&nbsp;So both getting the work done, and getting the work done in a way that improves the ability to do more work in the future are important goals which must coexist in an healthy environment.<br>
<br>
In order to handle requests efficiently, the infrastructure must be one that can reasonably be altered to support this requests, and as the business changes in scale, scope, and direction, this takes either a very well put together operational environment that is made to be changed quickly in these manners (possible, but difficult to assemble, and easy to turn less-functional), or it requires time before requests are done, to prepare the environment, or more time after the requests are done to fix the system after the fact.<br>
<br>
This is also on a spectrum, so you can't have both extremes as being simultaneously true in the same instance, which means you need to acknowledge, plan for and deal with the trade offs actively both over longer periods of times (quarters, years) and for each request, with an understanding of the scope of each requests potential to make positive or negative impacts on the infrastructure.<br>
<br>
What do I mean when I say two extreme's can't be true at the same time for the same instance?&nbsp;&nbsp;Apart from the truism there, what I specifically mean is that an environment that is not flexible must request time to complete requests to stay a healthy environment.&nbsp;&nbsp;And a team that does not have time to complete request appropriately must have a flexible infrastructure to be able to finish requests without "enough time" to change the infrastructure to keep it healthy.&nbsp;&nbsp;So either the team must have time, or the team must not need to have time, in order to keep the infrastructure healthy.<br>
<br>
Failure to either get enough time per request, or to have an infrastructure that does not take much time per request to remain a healthy environment, will result in an operational environment that becomes unhealthy, and will begin to exhibit the unhealthy signs:&nbsp;&nbsp;Lower Availability, Lower Performance, Lower Correctness, Lower User Satisfaction, Lower Maintainer Satisfaction, Lower Developer Satisfaction, Lower Revenues, Lower Opportunities, Lower Ability To Be Manueverable, etc.<br>
<br>
This spectrum is fairly specific, unlike "Not Available <--> Available", which is a fairly straight-forward concept to understand as a single topic, this axis' line moves among many topics to create a sliding scale between all of them, in a very limited manner.&nbsp;&nbsp;It is a line that travels through N-dimensions of information space.<br>
<br>
Trade Off Between Team Time and Infrastructure Flexibility For A Healthy Environment:<br>
<br>
Team Has Time To Manually Perform Requests <---> Infrastructure Is Flexible Enough To Take Requests Quickly Without Requiring Significant Team Manual Time<br>
<br>
This flexibility to be very specific with an axis, and to cross many boundaries of topics provides another benefit to Axiomatic Engineering, which is that "Compare and Contrast" type efforts can be very explicit, and anything that is too complicated to talk about clearly can be turned into these very specific sets of axises, which can than be given numerical values, and compared against each other.<br>
<br>
Because the topics are specific, and the numerical values gives your preference (or could be data collected through automation or monitoring) for describing very specific things.&nbsp;&nbsp;If you have related concepts that are specifically explained in separate axises, then the resulting quantified numbers of those axises comparison can give deeper insight to the problem, and can be communicated accordingly as Engineering Oriented Information, separate from normal communication in it's attempt to be precise and descriptive, attempting to be as objective as possible on data so complicated it must be subjectively formulated.&nbsp;&nbsp;Mathematics are such a notation for dealing with problems in that domain, but these are problems in a different domain, and need a solution as customized for that domain as the mathematics solution is customized for it's domain.<br>
<br>
This is the problem that we must work to overcome with any engineering field, in that there are too many variables, both known and unknown, to take into account, and to communicate about them is impossible to do accurately, and difficult to even do effectively.&nbsp;&nbsp;<br>
<br>
Since we know accuracy, perfect accuracy, will be impossible, we must strive for maximum effectiveness, where we get the most value for the least effort, while not using too little effort so that we get the best results possible with the resources we have to use.<br>
<h2 id=7ef5e6c23b6cb4359f88aea566c255fb><a href="#7ef5e6c23b6cb4359f88aea566c255fb">2.4</a>: What is a System?</h2>
<br>
There are a lot of ways the word "system" could be used.&nbsp;&nbsp;We're going to look at a general version of the word first, and then a specific version for our exact purposes afterwards.<br>
<br>
When I was growing up and for the first 10 years of my career, operational engineers were called "System Administrators".&nbsp;&nbsp;Today some people use this term derogatorily as lower-level or older style work, and while anyone can have any perspective they'd like, this is not consistent with history.<br>
<br>
I was lucky enough to spend some time around professional system administrators throughout the 1980s, before I was old enough to work, and I got to see them doing core dumps and reading through the hexadecimal output to find where the problems in their code were, and even fix some problems through a hex editor.&nbsp;&nbsp;I also got to get a bit of their practical advice and viewpoints, and I believe that after 5 or so years of professional operations work the lessons I saw back then started to filter back in to be more conscious rather than subconscious guides and role models.<br>
<br>
So, what is a system?&nbsp;&nbsp;Historically, in the computer industry, a system was often referred to as a single machine with an operating system on it, and the environment that was then configured on top of that to create a working environment.<br>
<br>
A system was sometimes a machine's hardware, an operating system was also a system, and the eventual configured environment was a system.<br>
<br>
One of the interesting properties of the word "system" is that all of these things were and are true.&nbsp;&nbsp;And all of these things together are also a system.<br>
<br>
A system is an generalized term for a set of interrelated, connected things that can be used together to produce effects.&nbsp;&nbsp;Like anything, it is black-boxable into inputs, outputs and side effects, and has sub-components which can be similarly black-boxed, etc.&nbsp;&nbsp;Systems may contain Real or Virtual components, and may create Real or Virtual effects, and combinations thereof.<br>
<br>
So, a "system" is a flexible term, and is something like an "environment" or an "ecosystem" in common usage.<br>
<br>
I like to think of systems as being somewhat like virtual machines, in the actual sense not in the container-type-operating-system sense.&nbsp;&nbsp;A system's connections can be graphed, like a network, and each component and be described by the inputs, outputs and side effects it causes, and may contain many layers of other systems, and may be part of a bigger system.<br>
<br>
Why is any of this important?&nbsp;&nbsp;Because your understanding of how systems works will determine your ability to mentally map the systems that you work with, so that you can think in terms of how those systems function.<br>
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
If you do not rotate logs (or otherwise truncate them), then with any activity at all, it is guaranteed that eventually the available storage will fill up, and any services which might use the storage for writes (such as logging) will fail.<br>
<br>
This is an example of a simple system, and indeed anything can be turned into a system, regardless of complexity or their nature.&nbsp;&nbsp;Additionally any given topic can be turned into multiple different systems which are all different, but all accurately model the topic, providing different descriptions, and showing that no single model or system will be the only description of Reality, they are simply one method of attempting to summarize and communicate information.<br>
<br>
The power of Systems is that they can be created at any time, to describe any thing, provided you are capable of properly black-boxing the components of the system you want to construct.<br>
<br>
You do not need to constrain yourself to existing systems, that other people have described, even when working with their work which have their own systems already described and available.&nbsp;&nbsp;You can create your own systems for your own purposes, to either assist yourself or communicate with others, or as tools to perform work.<br>
<br>
You might create alternative systems to simply understand other people's described systems.&nbsp;&nbsp;Sometimes it is harder to understand someone else's work than your own, and so creating your own work can illuminate a subject.&nbsp;&nbsp;Sometimes just writing down someone else's ideas in your own words provides insight you were previously missing, and allows you to understand the system you are describing, in a way that is more comprehensive or deeper than merely trying to use someone else's system.<br>
<br>
As an exercise while you read this book, try to create your own systems based on "the big picture" to understand what is currently being discussed.&nbsp;&nbsp;As new information comes in, update your system to reflect these changes.&nbsp;&nbsp;Attempt to switch from "big picture" to "details" and back again, to deepen your understanding of individual topics and the overall topic.&nbsp;&nbsp;<br>
<br>
Imaging looking at a forrest, then the leaves of a single tree, then back to the forrest, then looking at a specific leaf on a single tree, then back to the original tree's set of leaves, etc.&nbsp;&nbsp;The information is always a summary of something, whether you are look at specific pieces of summarized information, or larger sections of collected summarized information, you must be able to understand it, and have opinions on it based on your goals.&nbsp;&nbsp;Will it assist your goals?&nbsp;&nbsp;Will it make it harder to complete your goals?<br>
<br>
You can create your own systems on paper, in your head, you can find software that helps you create systems quickly (like Mind Map software), or use relational databases to track discrete data.&nbsp;&nbsp;<br>
<br>
Flow charts are one way to map systems, finite state machines are others ways, behavior trees are another way, but you can also describe them in prose, or doodles or any other way.&nbsp;&nbsp;Experiment, and find ways you enjoy.<br>
<br>
How you describe a system is merely a view into the system, and will never cover every aspect of a system, but each change in viewpoint gives a better angle on some information, and a worse angle on others.&nbsp;&nbsp;<br>
<br>
Only the actual components of a system describe the system, and any attempt to review the system will only give a partial insight into it, because it is a summary of something else, because a map is not equivalent to the territory it attempts to describe.&nbsp;&nbsp;<br>
<br>
By "actual components" I mean the things that make up the system are separate than our understanding of them, and our descriptions of them.&nbsp;&nbsp;They exist outside of our information, and so they are not only super-sets to the parts of our information that are accurate (and not related to the portions of our sets of information that are inaccurate), but that they also contain more data than we are aware of, and almost always some data of which we cannot become aware of because of the limitations in our ability to detect some things, and the limits of our knowledge to know to even try to detect them.<br>
<br>
Systems are tricky in this way, but this is also where their power comes from, because they are not limited by the nature of the actual components; they can be extended in any way you can think of, it it will assist you in your goals.<br>
<h2 id=61fc96e11d2dd57966d2b5b014f1a2dc><a href="#61fc96e11d2dd57966d2b5b014f1a2dc">2.5</a>: Systemic Thinking</h2>
<br>
I'll use "Systemic Thinking" to mean thinking in a way where everything is inside of a system.&nbsp;&nbsp;Systemic Thinking focuses on the relationships between all things in a system, and their mechanical relationships to each other.&nbsp;&nbsp;A system being a set of things you wish to model, to accomplish one or more goals by using the model to understand mechanically what the effects of a planned action would be.&nbsp;&nbsp;It is mechanical because it has inputs, outputs and side-effects, and so can be tracked and operated on as any mechanical device can.&nbsp;&nbsp;This is a Virtual Mechanical Device, which operates on Data.<br>
<br>
The Model gives feedback about what the current state of the Set of Components are, and what the likely state of the Set of Components will be if an action were to be performed.&nbsp;&nbsp;This also works in reverse to provide information about what happened in the past, by comparing Data to the Model, which can both improve the Model by correcting it against Data and Reality, and give information by inspecting the Data produced by Reality, and using the Model to explain that Data, given the error tolerance you have for the accuracy of the Model's ability to explain this Data and the correctness of the actions to perform the explanation.<br>
<br>
A System can be described by a network of black box functions which take inputs, emit outputs, and perform side-effects, totaling the results of anything that exists or doesn't exist, Real or Virtual.&nbsp;&nbsp;Either way, it can be described as a System, and using this methodology for organizing one's thoughts is "Systemic Thinking" by my definition here.<br>
<br>
I believe Systemic Thinking is one of the most powerful and useful tools in our mental toolbox, and could use a lot more of the educational spotlight.&nbsp;&nbsp;In terms of yielding positive results in learning speed and depth, creating works, and in performing maintenance (ie. troubleshooting), Systemic Thinking is among the most useful tools.<br>
<br>
Systemic Thinking has a number of prerequisites, such as a general understanding of how systems work, how to create systems, how to modify a system, how to inspect and evaluate the connections and links between system components, and a good basis in critical thinking.&nbsp;&nbsp;Having the ability to think Deductively and Inductively is a fundamental requirement.<br>
<br>
If you have not yet read a book on critical thinking, you should, to ensure you have the basic understanding of the topic.&nbsp;&nbsp;Of course you can fill in this information later now that you know it's something that could benefit you.&nbsp;&nbsp;<br>
<br>
{{ todo__recommend_critical_thinking_book }}<br>
<br>
<br>
{{ asside_begin }}<br>
{{ NOTE: This is too long for an aside, and is better suited to either being chopped up and put into other sections, or else chopped up and put into a reference section in the appendix. }}<br>
{{ IDEA: The aside is just a reference to an Appendix chapter, so that it doesnt take up any space or change the pacing of the chapter.&nbsp;&nbsp;This idea is a winner.&nbsp;&nbsp;Do this and clean this junk up.&nbsp;&nbsp;The cleanup will require changing the verbiage of this section into stand-alone, so that it can be read without the current context.&nbsp;&nbsp;This will also help clean up the rambling nature of this section, which rambled ramblingly. }}<br>
There is an infinite amount of information that is possible to learn, so the important thing is to bookmark all new "requirements" for the future, and follow up on what is most useful for the current goal to be accomplished in the present.&nbsp;&nbsp;<br>
<br>
This creates paths for future obstacle clearance, once one encounters an obstacle based on a required skill or set of knowledge, and minimizes disturbances to accomplishing one's current goals, which will always yield the most immediately rewarding results, since they were prioritized as objectives.<br>
<br>
Deductive and Inductive Reasoning, Boolean Logic, and Set Logic are the primary tools for doing analysis, and any troubleshooting of Systems will be significantly improved if you can break things down to terms and evaluate them for correctness against various assertions, as well as whether the assertions are valid or invalid.&nbsp;&nbsp;<br>
<br>
It is of critical importance that one is able to test the validity of an assertion.&nbsp;&nbsp;Without being able to validate or invalidate an assertion against it's test's result, one will not know if they are making a decision based on an invalid assumption.<br>
<br>
For example, if there was an Web Server outage for 30 minutes, and in the outage post-mortem discussion the Root Cause was suggested to be an ISP outage, as it was during the time window their ISP told them they would be doing maintenance.<br>
<br>
Except, that in this example, that is not the correct cause, as an engineer got an alert on their cell phone that a service was down, they logged into the specified server, saw a mounted volume had no space left on it; so they deleted some old log files, and the service started working again.&nbsp;&nbsp;Then they filed a ticket about it and marked it as an outage.<br>
<br>
But, in this example, the person who suggested it was the ISP's fault did not read this ticket, and so was giving their best guess as to what happened, based on information they had, that they thought was relevant.&nbsp;&nbsp;<br>
<br>
If no one with better information was present in that meeting, then that could very likely be selected as the primary reason for the 30 minute outage when it is written up as Root Cause; when in actuality, the outage was caused for a different reason, and that reason was fixed and logged according to standard work procedures by the engineer on-call.<br>
<br>
Being able to test the validity of an assertion allows us to qualify an assertion against it's subject.<br>
<br>
If we were in the meeting we could qualify the assertion that this was related to an ISP maintenance notification we received by comparing it to the data known to correlate that assertion with the actual outage.&nbsp;&nbsp;Is it valid or invalid, based on the data we have?&nbsp;&nbsp;Is it matched to actual data, or a data-less hypothesis?&nbsp;&nbsp;Unqualified assertions do not have data to back them up, qualified assertions do have data to back them up.&nbsp;&nbsp;An assertion can be both qualified and wrong, as it can have data that backs it up, but also data that invalidates it as an impossibility, so it is qualified as incorrect.&nbsp;&nbsp;In the same way, if all the data did back up the assertion, then it would be qualified as correct with the data current inspected, or some probability thereof if the data is inconclusive, so a Root Cause is still yet unknown, though there are possibilities.<br>
<br>
{{ exercise: build a matrix of all possible scenarios for an assertion being qualified, conclusive, and correct.&nbsp;&nbsp;Write an appendix entry that goes over this. }}<br>
<br>
If the the post-mortem meeting attendee who offered the assertion was asked about the qualifying information to their assertion, they would explain that they didn't verify this was the case and so cannot qualify it, but it matches the time frame of the notification.&nbsp;&nbsp;We can conclude from this that while it is a possible lead to look for correlating data/evidence, it is not a candidate for Root Cause yet, because there is no data to support that candidacy.&nbsp;&nbsp;Having no candidates is a valid state to be in, because without supporting data, there can be no valid candidates for Root Cause.<br>
<br>
Without any data, this is only a speculative relationship, due to correlation of information:&nbsp;&nbsp;notification and outage windows, but no data correlating the outage with the maintenance directly.<br>
<br>
While this is a higher-than-other-unknown-topic-priority topic to collect data on, since there is a time window correlation which adds priority, all other areas of the operational environment still need to be prioritized to collect information on, in order to find a direct correlation between the outage and the thing that caused the outage: the Root Cause.&nbsp;&nbsp;<br>
<br>
Prioritization is based on which Components of the Environment are most likely involved with the outage, based on the match between the data collected from monitoring and what those our Model predicts the results would be if a given Component failed, under a given condition.&nbsp;&nbsp;This description can be called a Component's Model, which serves like a fingerprint to distinguish how that Component interacts with data, which we use to predict future state, or extract information from historical summaries.<br>
<br>
To elaborate on a specific item in prioritization: it is important that the collection of information on the ISP's maintenance should be given less priority than collection from some other sources, even though it is a known-likely-possible-cause.&nbsp;&nbsp;It has elevated priority over the set of all places to gather information, because of the time correlation, but must be ranked according to the total set of indicators, not just that one indicator.<br>
<br>
The reason that it should get lower priority than some other areas of collection is that the maintenance correlation was temporary and a one-time thing, and is already over.&nbsp;&nbsp;So, collecting data on the ISP maintenance correlation is going to improve your records of events, and possibly has financial or contractual ramifications, which are important, but are not urgent in terms of time to response, since they are going to take time to process, on the order of weeks, or Quarters.&nbsp;&nbsp;This is an event that can be reacted to at lower priority, because it is over and non-recurring in nature (vendor scheduled maintenance).<br>
<br>
In comparison, if it was not the ISP maintenance that was the Root Cause, then the problem could still be occurring presently, and could be causing degraded service, or potentially failing in a manner that is not being monitored or alerted on, or is going to pass a threshold and begin a new outage soon.<br>
<br>
All of this can be found through troubleshooting, using the required skills of Modeling your System against the perceived and summarized Reality of the Components in your actual system, turned into a database-like schema, and then using that Model to reason about what happened, or what will happen.<br>
<br>
This tangential aside has already turned into an epic side-quest, but I have additional point to make on the topic of goals.<br>
<br>
Programming a computer is done with a programming language (C, Python, Java, etc), programming your mind is done by making physical and chemical-electrical changes to your brain by learning new skills and information (creating change in the patterns of connections and firing), which gives you a larger library of activities you can perform and problems you can solve, which gives you improved ability to accomplish your goals.<br>
<br>
Accomplishment of your own goals, in my opinion, is a Primary Life Requirement, and should be an ever-present factor in each decision you make in your life, in order to yield yourself the best results.&nbsp;&nbsp;Prioritization and other balancing factors between all things is necessary to achieve efficiency, so we can create Models that we believe are oriented towards creating work that is Aligned with our goals, to create the Reality we are attempting to achieve through applying effort.<br>
<br>
And, as an aside to this aside, the previous paragraph is an example of attempting to use a Mental Model or doing Self-Programming or whatever label seems best to apply to it, I don't think there is a good one yet.<br>
<br>
I created an English version of a descending mechanical-relationship tree, which Im defining as a tree of attribute descriptions which are related to each other by description of any input, output or side-effects.&nbsp;&nbsp;Each element shows hierarchy in terms of the described relationship, and the total space of all the ideas gives a "shape" that the reader can use their own information to populate to give them an idea at a certain "size", given the total "size" of the labels being used and the amount of labels and relationships, with bias towards their personal experience.&nbsp;&nbsp;This is a type of "Information Spatial Reasoning" in that they can use the resulting model to compare it against other models to see where they overlap or do not overlap in the space of all the contained ideas and information.<br>
{{ asside_end }}<br>
<br>
<br>
How do you use Systemic Thinking?<br>
<br>
The first thing to do is to take whatever you are thinking about, and turn it into a system.&nbsp;&nbsp;Anything can be turned into a system, and this system can be as large or small as you need, and can contain any number of components.&nbsp;&nbsp;We will start with this system being a set of things that you list.&nbsp;&nbsp;A "set of listed things" is a very basic system, and then anything can be added onto this, making it a more complex system.<br>
<br>
Since we, as humans, are limited in the number of things we can think about simultaneously, on a conscious level especially, we need to break things into small groups of related ideas.<br>
<br>
Let's create a system right now and do some reasoning with it, to use as an example.&nbsp;&nbsp;We will continue to use the web server analogy, as it is one that many people will already be familiar with, and are likely to spend a lot of time dealing with in their careers, as it has become the default medium for information exchange.&nbsp;&nbsp;You can think of this as an "Application Server" instead of web server if you like, the important thing is that it takes requests and serves back data.<br>
<br>
In the simplest of web server systems, we have static content serving.&nbsp;&nbsp;This is when someone has pre-created text (HTML, CSS, etc) and binary (images, videos) and the web server's job is to take requests for specific static files, and to relay those files to the requester.<br>
<br>
Since we can create a system out of any components, let's decide what our components will be:<br>
<br>
- A network connection to the Internet, which end-users are making requests on.<br>
- The IP protocol for networking, and basic TCP session management, on a Linux server.<br>
- A web server that listens on TCP port 80 on that server.<br>
- A file system that locally contains system files.<br>
- A file system that locally logs requests and processing.<br>
<br>
This is a slice of components involved in a web request, and just as I have arbitrarily picked these for this example, you can pick any components you want to build your own systems.&nbsp;&nbsp;<br>
<br>
You can continue to refer to the same system over time to get more familiar with all the details of that system, as is important in operational and application documentation, or you can abandon the system as soon as it's immediate purposes are over.&nbsp;&nbsp;Systems can be used forever or can be completely ephemeral, they are abstractions for reasoning and understanding reality, which remains too detailed and complex for us to directly understand.<br>
<br>
Let's create an event that occurs and exercises these components, as a sequence:<br>
<br>
- An end-user requests a file from the remote web server: http://www.domain.com/images/unstoppabletrex.png<br>
<br>
- The request performs operations outside of this system (LAN, routing, DNS, etc), but eventually opens a TCP socket to port 80 on the web server.&nbsp;&nbsp;The web server and the end-user now have a persistent session to communicate bidirectionally.<br>
<br>
- The end-user requests the URL specified above (broken into URI and Header sections), and relays any cookie and browser header information.<br>
<br>
- The web server accepts the input of the request, and goes through a process of routing the request internally, where it matches the domain in the URL domain or Host Header value and any other Headers it processes, and in this case then determines if there are any directory modifications to look for the static file.<br>
<br>
- Having determined what the path of the static file is on the local file system, if the file exists, the web server opens the file, reads it, and relays the data into the content section of the HTTP response.&nbsp;&nbsp;After relaying the contents, it closes the file, creates a successful HTTP status code, and returns the results.&nbsp;&nbsp;In this case we will assume that HTTP keep-alive is not enabled, and the HTTP server will close the connection afterwards.<br>
<br>
- The web server logs the request and successful response, appending to it's access log on the local file system.<br>
<br>
- The end-user's web browser will have received the HTTP response, getting the status code and body of the content, and in this case will display the image to the screen.<br>
<br>
This is one way that a request event could be processed by a web server.&nbsp;&nbsp;We can similarly create the model of "the file does not exist", the web server may do something similar, except return a 404 File Not Found static content result.<br>
<br>
In the case of a more dynamic system, the web server could proxy the request to an application server, which then makes database calls and performs formatting logic, and then returns a dynamic result instead of a static one.<br>
<br>
The importance of Systemic Thinking is that there are no gaps.&nbsp;&nbsp;Every connection that is required is modeled, and if new connections are required, they are added, and the remaining components need to be updated so that the System remains Internally Consistent.<br>
<br>
Internal Consistency is a very important factor in any System, for it to be a properly functioning system, and will be another topic we delve into deeply.&nbsp;&nbsp;Internal Consistency has similarities to Alignment, where components are aligned with one another for maximum efficiency, but Alignment requires Internal Consistency, where something can be Internally Consistent but not aligned.&nbsp;&nbsp;In this way Internal Consistency is a super-set of Alignment, in order to be aligned, things must be consistent, but things can be consistent and yet not well-aligned.<br>
<br>
Any time a change is made to any part of a Model, the rest of the Model must react accordingly, to stay Internally Consistent.&nbsp;&nbsp;The initial change may not require any additional changes to remain Internally Consistent, but it might be that every other Component must also be changed to remain Internally Consistent, this depends on the Reality that the Model is modeling, and the intent of the change being made.<br>
<h3 id=03071c27c692b17c5d7f95b9d4f021a4><a href="#03071c27c692b17c5d7f95b9d4f021a4">2.5.1</a>: Philosophers Knife</h3>
<br>
One important tool in creating systems is the concept of the "Philosopher's Knife".<br>
<br>
This is a virtual knife, meant for cutting ideas into sections.<br>
<br>
The most basic way of dividing ideas is to split them in half.&nbsp;&nbsp;Bifurcation is the cleanest method of division, as everything in split into one of two possibilities, which allows for using binary methods of organization, such as binary trees for creating hierarchy, or quantifying values so that things can be sorted on an comparative axis (ex: smallest to larger, slowest to fastest, etc), or setting binary flags so that set theory and boolean logic can be used (ex: "Is an X?", "Has an X?").<br>
<br>
For example, one can say something is "Black or White", and then take any concept and add it into the "Black camp" or the "White camp".&nbsp;&nbsp;This is a basic process of sub-division with things that appear to be opposites.&nbsp;&nbsp;In subtractive light frequencies, black is the absences of color, and white is all of the colors.&nbsp;&nbsp;In additive pigments, black is the combination of all pigments required to absorb all frequencies, and white is the absence of pigments that absorb frequencies, so that the frequencies are refracted and appear to be total spectrum, or white.&nbsp;&nbsp;<br>
<br>
By stating your method for determining the color, and your method for assigning into "black or white" camps, you can create a repeatable, inspectable, qualifiable and quantifiable method for working on data.&nbsp;&nbsp;You could create a color value from 0 to 255, and anything 0-127 is in the "Black" camp and anything 128-255 is in the "White" camp, and then additional operations could be performed on them.<br>
<br>
Being able to divide things in this way is a useful tool, but it is also a primitive inspection of the information, and in fact creates a frame that excludes almost all data.&nbsp;&nbsp;We all know that "black and white thinking" is simplistic, and the reason is that most of the information (color) is reduced out, when thinking in this way.&nbsp;&nbsp;And yet, it has utility.&nbsp;&nbsp;How can we use this utility, without being negatively effected by the loss of information?&nbsp;&nbsp;This is a primary goal in creating Wisdom, which is how to balance something beneficial or detrimental, depending on how it is used, but through Wisdom of it's usage, the results are beneficial.<br>
<br>
As a further example in making the split between "Black and White", the frame of reference created also ignores that fact that black and white are both colors, which means they are very similar to each other, and much less different from each other than say the word "duck", which is an animal.<br>
<br>
If we took the sets of "Black, White" and "Duck, Goose", we see that black and white have much more in common with each other than duck and goose.&nbsp;&nbsp;Because of this, even though in our first example we contrasted black and white as opposites, they are in fact much more similarly related to each other than many other things.<br>
<br>
This is both the power and the limitation of the philosophers knife.&nbsp;&nbsp;It can reveal differences, and it can obfuscate similarities.&nbsp;&nbsp;How you use it will depend on the results you are looking for, and your skill at applying this technique to create those results.<br>
<br>
For our purposes, we are looking at how to use the philosophers knife to sub-divide systems, for the purposes of Systemic Thinking.<br>
<br>
The most important element in creating a well-cut concept into a system, is that nothing is left behind.&nbsp;&nbsp;The use of the philosopher's knife should account for all components and options of a system, and while it is sub-dividing them, they never lose their whole.<br>
<br>
Their "whole" is what makes up the "system".&nbsp;&nbsp;If you lose a part of the system while sub-dividing it, you have not correctly used the philosophers knife.&nbsp;&nbsp;This will be important when designing your system, implementing it, and troubleshooting it, or in creating a Model to understand an existing system.<br>
<br>
Let's first use our previous example of the static HTTP web request.<br>
<br>
I used the philosopher's knife on the system of "making HTTP requests from a web server over a network" to come up with 5 elements of the process:<br>
<br>
- A communication network (Internet): part of the environment.<br>
- A protocol and environment (TCP/IP on Linux): part of the environment.<br>
- A request handler (web server on TCP port 80): the Input to the black-box.<br>
- A content location (static files on local filesystem): a component of the Output to the black-box.<br>
- A log location (appending results to log file): a Side-Effect of the black-box operation.<br>
<br>
I could have sliced this in a different manner, and instead focused on the TCP packet exchange, or I could have cut it so we delved deeper into the end-user's process of getting it's request to the web server (LAN, routing, DNS, TCP handshakes, etc).<br>
<br>
I was able to slice this process into the layer's I chose, because I wanted to discuss those elements, and not other elements.&nbsp;&nbsp;This ability to exclude what information is being inspected, while not losing any of those excluded areas of data in the total picture is the real power of systemic thinking, is the function of the philosopher's knife in this process.<br>
<br>
We can take the exact same example process, and re-slice it any way we want, and the events would be the same, but the information we look at, and how we inspect it would be different.&nbsp;&nbsp;The system has not changed, the actions that occur in reality did not change, the results did not change, the inputs, outputs and side-effects did not change, and yet we are able to look at the problem in a completely different way, and take different lessons and gather different information from it.<br>
<h3 id=1f4b194d8569136439831f483c38a264><a href="#1f4b194d8569136439831f483c38a264">2.5.2</a>: Slicing the pie vs aggregation</h3>
<br>
In the last section we covered the importance of slicing with the Philosopher's Knife without losing any information.<br>
<br>
One easy way of thinking about this is that you are cutting up a pie with the Philosopher's Knife.<br>
<br>
No matter how you slice a pie, the amount of pie has not been reduced, there is only a different number of pieces.<br>
<br>
If you cut a piece directly down the middle, creating 2 symmetrical pieces, no pie is lost.&nbsp;&nbsp;You have 2 pieces that compose the entire pie before slicing.<br>
<br>
Similarly if you cut a pie into any configuration, with any number of cuts, whether it is symmetrical, asymmetrical, whether the cuts are vertical, horizontal, diagonal, straight or wavy, the results are the same, in total all the pieces still contain all the original matter of the pie, the difference is only in the distinction of between separate pieces of the pie.<br>
<br>
In our philosophical cuts, the structure of the "pie" does not change, unlike a real pie, which deforms with the pressure of cuts, and will turn into a mess after enough slicing.<br>
<br>
In our virtual "pies" of information, or systems, we can slice any number of times in any direction, and the information remains the same, but on each side of the cut, we have made a division that can be used logically.&nbsp;&nbsp;Essentially, the Model of our System is the progression of cuts, and the total set of cuts as it relates to the system.&nbsp;&nbsp;Each cut is an "axis", which divides along a boolean of "is X" or "is not X" relating to the cut X.<br>
<br>
For instance, we can look at an Operating System that runs on PC hardware (like Linux, OS X or Windows), and divide the it into code that runs in "Kernel space" vs code that runs in "User space".&nbsp;&nbsp;We could call this the "Kernel space cut", to determine "Is Kernel space?" vs "Is not Kernel space?", or we could bifurcate it as "Kernel/User space" to explicitly state the 2 sides, instead of only explicitly stating 1 side, and the other is simply what-isn't-part-of-the-explicitly-stated-side.&nbsp;&nbsp;If you already know there can only be 2 options, you can use explicitly naming both sides, if you aren't sure there are 2 and only 2 options, then use naming 1 side and leave "everything else" for the other side.<br>
<br>
Dividing between Kernel and User space splits all code that is executed by the operating system, they are either executing in Kernel space or User space.&nbsp;&nbsp;We can take the same system, and make a cut between "firmware" (code that executes from BIOS and other places closer to hardware) and "software", which is executed from RAM on the main CPU.<br>
<br>
Whether we have divided by "Kernel vs User" or "Firmware vs Software", nothing about the system has changed, we have simply decided to cut the pie in a different place, and we can then use this division for some sort of useful inspection.<br>
<br>
Cuts can be layered on top of each other, like dividing into Firmware/Software, and then dividing Software into Kernel/User space, and could continue to be divided, such as dividing User space into shared library code vs. application local code.&nbsp;&nbsp;Share library code will be executed by more than one application, and is stored in a .so or .dll type file, and application code will be stored in a program's ELF or EXE formatted binary file.&nbsp;&nbsp;This type of layered cutting creates a structure like a binary-space partition tree (BSP tree), if you want to model it that way, or can be seen as a list of boolean axes, or could be used in any other way you want to model data if you have a different goal for your visualization.<br>
<br>
For purposes of discussion and illustration we can be fairly fluid about our definitions, and decisions on where to slice, because they are throw-away examples, and exist only for as long as they are useful to us.<br>
<br>
As we get deeper into the topics of Engineering Axioms and automation, we will see that while this can be used fluidly, the ability to use it deterministically, in a repeatable pattern, across many topics, becomes of paramount importance.<br>
<br>
The reason for this is the difference between a comprehensive system (correctly sliced with the Philosopher's Knife), and an aggregated system, which is not built as a complete system is aggregated from components, and is not built using a whole system and "pie-slicing".&nbsp;&nbsp;The difference is an Aggregated System is built from components, like bricks from the ground up.&nbsp;&nbsp;As bricks are needed, bricks are laid down, if there is a gap, it can be filled in.&nbsp;&nbsp;In comparison the Comprehensive System exists in total from the beginning, although it is Virtual as it exists as a concept, it exists in totality, where the concept of the Aggregate System does not exist in totality, and only what we currently know and track of it (with our component-bricks) is tracked or can be said to exist.<br>
<br>
The problem with aggregated "systems" is that they not always in jeopardy of becoming not-internally-consistent, and they can never be complete.&nbsp;&nbsp;Due to being "aggregated" into creation, where one piece is created, and then another piece, and then the two are put together, and then a change is made, and then a new piece is added, you get the result of not having a "complete pie" when it is assembled, as the only pieces that were tracked were those that we happened to work with.&nbsp;&nbsp;<br>
<br>
Aggregated systems have a tendency towards not being internally consistent, and Comprehensive (Slicing the Pie) systems have a tendency towards being internally consistent.&nbsp;&nbsp;Just because you have a Comprehensive (Slicing the Pie) system, does not mean you cannot create an a situation where it isn't internally consistent, but as it is reviewed and worked on (under the Slicing-The-Pie mechanism), it will be revealed as to where and why an internal-consistency-error was created.&nbsp;&nbsp;In an aggregated system this is much more difficult, because things are only related to their adjacent neighbors through their connections, and did not come out of a comprehensive system from the beginning.<br>
<br>
In fact, I will attempt to prove later on that it is impossible for a system that is aggregated to ever become a complete and comprehensive system, whereas if you always work from the method of "slicing the pie", you will always have a comprehensive system.&nbsp;&nbsp;The reason for this is their approach.&nbsp;&nbsp;<br>
<br>
The work involved to do both are very similar, and in some cases exactly the same, but the manner of thinking about the elements in them are very different, and yield very different results.<br>
<br>
If you think about "comprehensiveness" as "volume", and we think of the "space of this volume" as a rectangle (width and height), then the Aggregation method works by building up from the bottom (height = 0, and up), and works along the width to provide more structure.&nbsp;&nbsp;<br>
<br>
The Comprehensive model starts by utilizing the entire area of the volume, but making subdivisions, say in 4 equal pieces to start, and assigning each sub-section as an element of the Comprehensive whole.&nbsp;&nbsp;Then those sub-sections are subdivided again, and again, until we start to add in details.&nbsp;&nbsp;The entirety of the volume will never be filled, as there is an infinite amount of detail that can be applied, but the entire space of the rectangle is being "owned" by some topic, and is being further divided down as we zoom-in to more details.<br>
<br>
With the Aggregate model (which is a system, but not in the "Systemic Thinking" sense of the word), only the bottom parts of the space are utilized.&nbsp;&nbsp;It's doing the same thing, in terms of implementation of the details, but the way the details are mapped to one-another is only through their implementation.&nbsp;&nbsp;This differs from the Comprehensive model (which uses "system" in the same way the "Systemic Thinking" does), because the relationship for all details is completely mapped into the entire volume, the entire comprehensive structure of thought or description, and the model takes into account "all of the space", even if a given particular part of the space has not yet been implemented.<br>
<br>
The Aggregate model does not have the attributes, and so gives a different result, which is not a Comprehensive result, but a "de facto" result.&nbsp;&nbsp;The Aggregate is "what we did", but does not include planning inside of it's own structure, because it is simply a map of work performed.&nbsp;&nbsp;The Comprehensive model includes both the entirety of the structure (all things we know of in the system), and where we have performed work to solve problems inside this system-space.<br>
<br>
As of 2015, I do not know of any operational environments which work in a manner that is consistent with "slicing the pie", I only know of aggregation environments.&nbsp;&nbsp;I will explain this assertion as we get more into details, but this puts the use of systemic thinking in an operational environment into a purely "mythical" state at the moment.&nbsp;&nbsp;Something I hope to change with writing this book, and sometime I hope to pass on as a valid tool for Engineering, and a valid goal where it will help your engineering projects.<br>
<br>
Part of the purpose of this book is to provide a path for others to understand these differences, so that paths can be built to allow us to create these comprehensive and complete systems, and to manage them accordingly, to get the benefits which they provide.<br>
<br>
We know the benefits and fallbacks of the aggregation system, though without comparing them to another method it is merely the de facto operations of all environments, making it hard to inspect as there is nothing different to compare it to.&nbsp;&nbsp;<br>
<br>
Making a change requires both defining the goals we want to achieve, and the current state of things, so we know what is required to make a change to get closer to our goals.<br>
<h3 id=f32b593542b3562df78d89693543c0fe><a href="#f32b593542b3562df78d89693543c0fe">2.5.3</a>: Systemic Thinking</h3>
<br>
So far we've gone over the general definition of a system, and created some examples, and looked at how to slice components of a system up to leave the system intact, but able to looked at from different perspectives, and to separate out different components.<br>
<br>
How does this affect our ability to perform operational duties?&nbsp;&nbsp;How will it help in automation, and in the life-cycle management of an operational environment?<br>
<br>
Firstly, if one cannot understand something in detail for one's self, then it will be difficult to work with that thing efficiently.&nbsp;&nbsp;I hope I have shown that being able to slice up a topic in any way you would like can produce sub-divisions which allow inspection and description, and which do not change the whole of system, and can be sub-divided further, or sub-divided differently to provide examples to compare and contract with one another, and to inspect their relationships and how work might flow through them.<br>
<br>
Once one has an understanding for one's self, then the ability to communicate effectively about the topic becomes a possibility.&nbsp;&nbsp;If I don't understand a topic thoroughly, I will have a very hard time having a thorough discussion of that topic with someone else, in fact I believe this is impossible to do.&nbsp;&nbsp;I must have a thorough and comprehensive understanding myself if I wish to be able to communicate with someone else with clarity.&nbsp;&nbsp;They will have a different understanding than I do, even if we use the same Model descriptions, because we have different experiences and information, but the Model and System view I make and understand myself gives me a map to try to make analogues against when conversing with others.<br>
<br>
Through the power of using systems and the Philosopher's Knife, and black-boxing, I can take topics I do not comprehensively understand, and transform them into topics I do comprehensively understand, using a Model I have devised as a mechanism for understanding.<br>
<br>
By reducing a system or component to it's Inputs, Outputs and known Side-Effects, I can clearly talk about what is going on as it relates to other systems or components.&nbsp;&nbsp;<br>
<br>
If we can come to an agreement on terms and what the Inputs, Outputs and Side-Effects are for the given systems/components we are talking about, we have a much higher likelihood of coming to consensus on what we are talking about, and will be less likely to be talking about completely different things, while we are trying to communicate about a problem, or a solution, or whatever.<br>
<br>
Additionally, once we can create a system out of any environment and events, we can begin to Model that system so that we can come up with procedures on what we should do under different circumstances.<br>
<br>
For instance, in our web request and logging examples, we have determined that without log rotation we will in time fill up available storage, and fail to be able to take more requests (or at least, log their results), and so we are sure to have failures on any active systems where this is the case.<br>
<br>
From this we can create a policy that requires all services to have log rotation or truncating configured for any software before it is put into active service.&nbsp;&nbsp;We can go over the results we will achieve without this, and determine that are not the results that we want, and come up with a test for whether this is enacted on a given server to ensure that we have done this work, and have protected ourselves from this deterministic outcome.<br>
<br>
This is the type of leverage that these tools provide, and when we get into the details of automating an entire operational environment, through it's life-cycles, with change management and ensuring that all things are internally consistent, and well-aligned, to accomplish our goals, we will find that without these tools for clear and consistent "breaking things apart" and "putting them back together again" without losing any information, we will not be able to get comprehensive coverage without being able to communicate at this level of detail.<br>
<br>
The short-comings of aggregated systems, versus comprehensive systemic systems is not yet clear, but as we define our terms more concretely, and begin to use them to deconstruct on operational environment, and then put it back together again, while keeping track of everything, we will see how aggregated systems are incapable of performing this task, while whole-systems always lean-towards an accurate representation, if they are viewed with accuracy.<br>
<br>
That isn't circular logic, is it simply the result of "Garbage In-Garbage Out".&nbsp;&nbsp;If one can't view a topic accurately, one cannot expect to perform work to meet goals accurately.<br>
<h3 id=dadc2661d50f3cdb6efb0378f9c6803d><a href="#dadc2661d50f3cdb6efb0378f9c6803d">2.5.4</a>: Inputs, Outputs and Side-Effects: A Virtual Mechanism</h3>
<br>
I talk about the qualities of "Inputs, Outputs and Side-Effects" enough that I've decided to label them as something that can be discussed directly.<br>
<br>
I will call something that takes Inputs, gives Outputs, and produces Side-Effects a "Universal Machine", because it is a type of machine (performs work, mechanistically), and can be applied in any situation.&nbsp;&nbsp;It may be a deterministic machine or non-deterministic (introduces randomness, or other factors which cause different Outputs or Side-Effects with the same Inputs).<br>
<br>
A Universal Machine, by our definition here, can take any inputs and return any outputs, and create any side-effects, whether they are Real or Virtual, it doesn't matter.&nbsp;&nbsp;The important aspect is that there is a definition of the interface, so that the understanding can be brought about from just looking at Inputs, Outputs and Side-Effects.<br>
<br>
Additionally, how you define a Universal Machine can change based on your goals.&nbsp;&nbsp;If you are trying to track information as input, and information as output, and yet track real physical changes as side-effects, this is one way of defining a machine.&nbsp;&nbsp;In a different way, for the same situation, you could define physical inputs, and physical outputs, and information-based side-effects (data that has changed).&nbsp;&nbsp;Any combination is usable.&nbsp;&nbsp;In the Operations world, generally we are dealing with informational inputs, informational outputs and informational side-effects, as physical changes are usually outside of our area of immediate concerns.<br>
<br>
A Universal Machine can be defined as you want it, and can be applied to anything, like a system, and a Universal Machine is a System, but it is a specific type of System that is defined as having Inputs, Outputs and Side-Effects.&nbsp;&nbsp;While any System might be able to be viewed as a Universal Machine, many times when we think of a system we are not thinking of it as a machine, so it helps to differentiate about when we are and when we are not thinking in terms of mechanical inputs, outputs and side-effects.<br>
<br>
Any process, physical or non-physical (informational, virtual, etc), can be defined by it's Inputs, Outputs and Side-Effects, so this creates an interface we can use at any time, for any reason, and we can reason about Universal Machines based on their interfaces, separate from the work that they actually perform.<br>
<br>
The linkages between Universal Machines will follow the same rules, irregardless of the type of Inputs, Outputs and Side-Effects being worked on.&nbsp;&nbsp;By making a distinct type of unit we can refer to by the label Universal Machine, we can always drop into the method of talking about a component. or service, or physical machine, or any type of thing, and how it operates in a chain or process of events.<br>
<br>
{{ note: Should I create an acronym for this?&nbsp;&nbsp;I/O/SE? IOSE?&nbsp;&nbsp;Might be useful. }}<br>
<h2 id=da54e5ab11aae5fc49994945cb3bc9a8><a href="#da54e5ab11aae5fc49994945cb3bc9a8">2.6</a>: Terminology</h2>
<br>
Congratulations!&nbsp;&nbsp;You've made it to the second beginning of the book, where we go over the definitions of terminology we will be using.<br>
<br>
I thought it was important to give a bunch of background on what we were going to talk about before we got to the definitions, because my terminology definitions may be quite different than how you already think of these terms, as you may have already begun to see.<br>
<br>
For the purposes of reading this book, please accept my definitions as I will use them for the purpose of making things clear.&nbsp;&nbsp;The definitions must be kept congruous to differentiate things that are frequently conflated.&nbsp;&nbsp;If it helps you can mentally append "Geoff is saying he means X when he says Y in this book", if the terminologies conflict too much with your existing use of the words.&nbsp;&nbsp;I'm making a specific point about this, as I often have an internal feeling of rejecting an authors information based on their use of words from being different than how I would use them.&nbsp;&nbsp;It's often a useful method to determine if the information is worth listening to, but in the case of a longer-term effort like reading a mentorship-oriented book, can cause you to miss out on crucial information.<br>
<br>
The important part of this is that you gain insight into my perspectives, as I will be using those descriptions of my perspectives to build up a detailed map of how to inspect an environment, how to design and compose an environment, how to implement it, how to automate it, how to troubleshoot it, how to perform maintenance and life-cycle changes to it, how to document it, describe it to other people, etc.<br>
<br>
This is all too much to do with just anyone's terminology, and the only terminology that will be able to consistently deliver these results inside of this book will be my own.&nbsp;&nbsp;So try to accept all of these for the tools that they are in getting to these goals, and not as universal definitions that should be written into dictionaries, or compared against them.<br>
<br>
I will be using the capitalization of proper nouns with these special terms, so that they are clearly my definition, for the purpose of this book, and not meant as the general term.&nbsp;&nbsp;The only time this may be confusing is when the word starts the beginning of a sentence, but I hope context will keep that clear.<br>
<h3 id=9b48a00c792d88dfa31f203429758f84><a href="#9b48a00c792d88dfa31f203429758f84">2.6.1</a>: Data: data</h3>
<br>
In the virtual world, Data is king.<br>
<br>
I will support this assertion throughout this entire work, as it has become a central tenet in my thinking about how to do any sort of digital engineering.<br>
<br>
As I asserted in {{ section_ff17d94c0d49aab3e372e47b64b96ea7 }}, Data is an un-real thing.&nbsp;&nbsp;It is virtual.&nbsp;&nbsp;It does not have physical properties, and does not exist in the physical world.<br>
<br>
Electrons and magnetic forces exist, which we use to encode data into storage and processing mediums, but the Data itself does not physically exist.<br>
<br>
This is an important fundamental to understand, and more important for the purpose of learning from this book, to accept as the usage under which I will giving examples and explaining things.<br>
<br>
Data is symbolic and descriptive.&nbsp;&nbsp;It can be used in any way, to accomplish any purpose at which the data has usefulness.<br>
<br>
You can use Data to accomplish things it was not intended.&nbsp;&nbsp;For instance I could take the textual data inside a Linux /etc/passwd file and turn that into a musical score, by converting the characters and terms into frequencies, and by playing it.<br>
<br>
It would likely sound incoherent, and not be considered musical, but that is the power of Data.&nbsp;&nbsp;It can be used as you see fit.<br>
<br>
Data resides in a Data Source, which could be anything, such as: files, database tables and rows, returned by networked services, etc.<br>
<br>
Data can be stored in many formats, and these formats can dramatically change the way the data is stored, and yet if it is not corrupted, the data can still function in the same way.<br>
<br>
Consider that data stored in a CSV (Comma-Separated Value) file and data stored in a YAML or JSON format look very different, and yet both can be loaded, parsed, and used as if they were stored in the same format.<br>
<br>
Data could be formatted to fit inside a relational database, so that it is spread into tables and fields, and looks nothing like a CSV file, and yet after querying the database I can get the data back in the same format which I could parse from a CSV file.<br>
<br>
This shows the dynamic nature of Data, while still providing us with consistent information that can be used by humans or Logic.<br>
<h3 id=69371f3e438e2ed281f525ac57e65e3c><a href="#69371f3e438e2ed281f525ac57e65e3c">2.6.2</a>: Logic: code</h3>
<br>
I'm going to try to constrain myself to using the capitalized (proper noun) "Logic" any time I am referring any of the following things:<br>
<br>
- Code<br>
- Programming<br>
- Scripts<br>
- Decision trees<br>
- Finite State Machine processes<br>
- etc<br>
<br>
I will also use these other terms in their normal meanings throughout the book, but I will refer to Logic when I am combining what is created in order to manage things that are done programmatically.<br>
<br>
It's good that our industry has many terms for things, as it makes them specific, but I will using the roll-up term, Logic, in order to simplify and generalize what we are talking about.<br>
<br>
One simple definition could be:<br>
<br>
- Logic is Data that is executable.<br>
<br>
In this definition, Logic is a sub-set of Data.<br>
<br>
This could be executable because it is in a native format an Operating System can load and execute (ex: ELF, EXE, etc), or via an interpreter (ex: Python, Ruby, PHP, Bash), or via a Virtual Machine executor (ex: Java, .NET/Mono).<br>
<br>
Logic is used when one wants to operate on data in a digital environment.&nbsp;&nbsp;With Logic we will change the data, create new data, validate data, and perform side-effect type actions where we do things like copy data to different locations, remove it, create directories, start and stop services, as well as anything else we could do manually.<br>
<br>
Essentially Logic is the way we take action through digital means, where we would otherwise take actions manually.<br>
<br>
Of course, in a digital environment, all actions eventually require Logic.<br>
<br>
If I am in a command-line shell, and I run a command to create a directory, I have manually initiated Logic to perform this work.<br>
<br>
If I write logic to inspect a data source, and then to create directories based on that data in that source, then I do not need to manually initiate the Logic to create the directory.&nbsp;&nbsp;There will be some kind of timed period (ex: cron jobs) or event (ex: monitoring initiated execution) that will initiate the Logic.<br>
<br>
As we went over in {{ section_ff17d94c0d49aab3e372e47b64b96ea7 }}, Logic is un-real or virtual.&nbsp;&nbsp;It is not a physical thing, with physical properties.&nbsp;&nbsp;It does not exist in the physical world at a given location or orientation.<br>
<br>
One can say that that bits that describe the Logic do reside on a physical storage medium (rotating disk, SSD, RAM, etc), but I am separating these physical attributes from the Logic itself, which could be anywhere, and in a given physical device, it will almost always reside in multiple locations, both on storage, and in RAM and perhaps in a CPU cache, and perhaps partially in CPU registers.<br>
<br>
I will end up breaking down many things to Logic layers and Data layers, and how Logic works on Data, and how Data is the stable foundation of Logic.&nbsp;&nbsp;In my perspective, this is a reversal of how many people see the relationship between Logic and Data, but I will make a case for why Data is the core and Logic is the shell.<br>
<br>
To make the assertion as briefly as I can:<br>
<br>
1. Data is what you know at a given time.&nbsp;&nbsp;This is useful forever.&nbsp;&nbsp;It could be useful hundreds of years for now, for the same reasons it is for us today (using it to configure things), or strictly for historical or analytical purposes.&nbsp;&nbsp;Data has essentially no "death" or time where it becomes invalid or unusable, as a general resource.&nbsp;&nbsp;<br>
<br>
Not to say Data cannot be corrupted, or be invalid to our purposes, but it remains valid as a source of information even if it is corrupted (though perhaps not actionable for our immediate use, and degraded utility and trustworthiness due to corruption).<br>
<br>
Even corrupt data is potentially usable to give us some information (statistics about what was not corrupted), but corrupt Code/Logic should not be executed, unless it is an sealed-off environment, as it may perform destructive actions.<br>
<br>
2. Logic is the codification of goals.&nbsp;&nbsp;What we want to occur is processed through Logic.&nbsp;&nbsp;Because of this, Logic has a number of environmental factors that work in some conditions, but there are many states where Logic cannot be used, except if it is seen as "Data" and is no longer executable.<br>
<br>
Logic requires a valid environment to run on.&nbsp;&nbsp;Logic created to run on Linux will not run on Windows, or OS X, without being re-compiled (and perhaps "ported"), or being somehow universally compiled.<br>
<br>
Logic expects certain environmental requirements to exist.&nbsp;&nbsp;It may expect to run in a certain directory structure, which contains certain files, formatted a certain way, and containing specifically formatted data.<br>
<br>
Logic could require access to network services which must exist and be reachable and authenticatable for it to work properly.<br>
<br>
Logic has dependencies.&nbsp;&nbsp;It runs on a given "platform", and does not run if the supported "platform" is not available as it's execution environment.<br>
<br>
Data needs a place to reside (ex: database, file system, etc), but it does not require a specific environment, it could be stored in a YAML format, JSON format, in a relational database, a flat file with comma or colon separation, as raw blocks on a device, or any type of format or storage system at all.<br>
<br>
The methods to access the Data can change, but the Data itself will remain the same.<br>
<br>
In order for Logic to run in a different environment, it is likely going to need changes.&nbsp;&nbsp;Some programming languages offer cross platform execution, via being run by an interpreter or virtual machine executor which was natively compiled to the target operating system.<br>
<br>
However, there are still many places that Logic may not be able to work cross-platform without changes, such as moving from Linux to Windows there is a difference in how Windows access some storage, because it uses "Drive Letters" as device targets, Unix-style operating systems use a single directory hierarchy, and user's home directories are in completely different places, and looked up in different ways.<br>
<br>
Other changes may be system files it expects to find in certain places, or required libraries that may not be installed, or may be an incompatible version.<br>
<br>
These are lower-level types of problems that Logic has, and why, unless it is running in a hardware emulator, Logic written decades ago generally cannot be executed properly on modern hardware and modern operating systems.&nbsp;&nbsp;<br>
<br>
There are some exceptions to this, such as code that ran on very old versions of Windows, and has had fixes installed throughout Windows versions up until the modern times to allow this code to still work.&nbsp;&nbsp;These are the minority of cases though.<br>
<br>
A more likely scenario is that the organizational goals have changed.<br>
<br>
Goals change frequently, and so requirements change frequently, and Logic is codification of requirements.&nbsp;&nbsp;Once you have different goals, it is very unlikely that the code that worked for the previous goals will still work with the new goals.&nbsp;&nbsp;This happens every time new commits are made to a source code repository, the actions the old code performed are now changes, and new actions happen.&nbsp;&nbsp;The old-code's action's results are no longer desired, because we have upgraded them to the new-code's action's results.&nbsp;&nbsp;The old-code is deprecated and should no longer be run, that Logic is expired.<br>
<br>
The conditions for when the same Logic will give correct results once you goals have changed is when that Logic is being used as a "tool" or "utility", in which case it operates on data to perform it's actions.&nbsp;&nbsp;The Logic performs a primitive function, and so it can escape being outdated as soon as your goals change, because of the limited nature of it's actions, and it's intent being a general purpose tool, rather than a specific tool to implement your goals.<br>
<br>
This accounts for the long-life span of Unix-style environments, which are historically largely made up of software that performs generalized operations against a set of data.&nbsp;&nbsp;That data might resides in a file, a database or be given by user input on the command-line, piping through input streams, or through a series of prompts.&nbsp;&nbsp;<br>
<br>
In these "tool" types of Logic, it is the data that tells the Logic how to achieve a goal, and so again the Data gains primacy over the Logic in being the key element.&nbsp;&nbsp;The "tool" Logic only exists to transform the Data.<br>
<br>
For our purposes, in automating an operational environment, we will be extending this "tool" type processing greatly, so that we create a large pool of interconnected data, and then create Logic that works against this data to achieve the goals we want.<br>
<br>
Like the Unix-style environment that allows so much control and flexibility, we will create a layer on top of current Operating Systems, which allows the accomplishment of goals with a minimum amount of changes to Logic, as the Logic is driven by the Data.<br>
<h3 id=aa2640c210126a47b684283980210b76><a href="#aa2640c210126a47b684283980210b76">2.6.3</a>: Rules: policies about how you do stuff</h3>
<br>
For the purpose of this book, I'm going to use a term I don't usually use in real life, which is "Rules".<br>
<br>
In this case I will define Rules to mean the way we do things, encoded into Logic and Data.<br>
<br>
I will use this to separate out digital Rules from policies and procedures that departments and organizations use to determine how people do things.<br>
<br>
This could be seen in the sense of "Rule Processing Systems", or something similar, where Rules are constraints or requirements in how Logic will operate.<br>
<br>
And the Rules are specified either directly in the Logic (hard-coded rules), or in Data.<br>
<br>
Rules encoded in Logic will require more effort to change, and are not able to be changed automatically, unless you are generating the code.&nbsp;&nbsp;Generated code is more of the side of the spectrum of Data than Logic, because Logic is generally created by humans.<br>
<br>
In the case of generated Logic, it will be generated from Logic created by humans, and is a type of template that has data populated into it, or loops of generated chunks with data populated into them.<br>
<h3 id=3393e40f9f65bba3ee24fc4f744c792b><a href="#3393e40f9f65bba3ee24fc4f744c792b">2.6.4</a>: Distributed: dealing with N nodes</h3>
<br>
You may have used the word "distributed" before, such as in "distributed systems".<br>
<br>
My meaning will be very similar to this usage, but I will use it a little more generally to mean any time you need to work across many nodes of something.<br>
<br>
For instance having to control 200 web servers will be a Distributed service of web servers.<br>
<br>
This usage stems from a single web server being able to do the same thing as 200 web servers (configured in the same manner), but the "load" is "distributed" across the 200 web servers, making this a distributed network service.<br>
<br>
The reason for being very general in this usage is that it provides a comparison point between single-unit processing system and a multi-unit processing system, which is the core of the problem and benefit: there are more things doing the thing.<br>
<br>
As I will cover in more detail later on, there are 3 cases you should account for in operations:<br>
<br>
- Zero instances of something.&nbsp;&nbsp;You do not do this thing.&nbsp;&nbsp;In some cases this is simply something you do not require, but in the more sophisticated case, this is work you are still accomplishing, but in a manner that does not need an instance of anything running to accomplish the goal, it is taken care of by an efficiency gain.&nbsp;&nbsp;In either case, it is important to know that "not having something" is a potential state.<br>
<br>
- One instance of something.&nbsp;&nbsp;This is when you have one thing that you use; it is the centralization of a service.&nbsp;&nbsp;There may still be a pair of machines (Master/Slave) supporting this one-thing, and there may be more than a pair, but if there is logically a "single instance" of the thing, then it is a "one instance" though the instance may be made up of many pieces to create the single-whole.<br>
<br>
- Infinite instances of something.&nbsp;&nbsp;As soon as you move beyond "one instance" (or one-thing), you move into the realm of many-things.&nbsp;&nbsp;If you think you can move to "just two" or "just three" you are not taking into account all of history which shows continual sub-division and growth in all things that are not "shutting down".&nbsp;&nbsp;"infinite instances" may currently be at a count of "2", but in order to handle the growth that will eventually come, it should be implemented as an N-instance, or infinite instance system.<br>
<br>
Differentiating between "instances" and "counts of things" can be a little tricky, and seem subjective, but it is because it is fulfilling a goal of understanding whether we have duplication of "service providers", or not.&nbsp;&nbsp;This is all in the context of "distributed systems", if that helps to make this language introspection easier to understand.<br>
<br>
These differences can be seen in the phase:<br>
<br>
"0, 1, Infinity.&nbsp;&nbsp;There is no 2."<br>
<br>
Make this an internal meme for yourself, and watch as things start to make more sense in terms of problems with scaling.&nbsp;&nbsp;When a number larger than 1-instance is introduced, you will eventually see that number grow, and sub-divide into different domains.<br>
<br>
Having a 1-instance system is incredibly difficult.&nbsp;&nbsp;Pressures will continually be applied to grow into an N-instance system, and it will take work and perseverance to keep a 1-instance system at 1-instance.<br>
<br>
0-instance systems, when not just the identity of "we don't do that here", are created from efficiencies in automation.&nbsp;&nbsp;This is when a 1-instance or N-instance system has been replaced in such a way that the work does not need to specifically occur, and yet the goals are still achieved.&nbsp;&nbsp;If this sounds a lot like what I referred to as "removing Classes of Work", it is because it is exactly that.<br>
<br>
I will cover this concept in full detail later on, because it is critical to understanding how scaling works in practice, but takes a bit more background before accomplishing it can be discussed.<br>
<h3 id=a709b239027a030b1a2dc4d500e49a24><a href="#a709b239027a030b1a2dc4d500e49a24">2.6.5</a>: Real/Virtual.&nbsp;&nbsp;Strict definitions.</h3>
<br>
I won't go through the explanation that I made in {{ section_ff17d94c0d49aab3e372e47b64b96ea7 }} again here, as I think we covered the differences between what I meant by real and un-real, or virtual there.<br>
<br>
I'll just say that like other terms meant for this book, I will be using Real and Virtual as proper nouns to describe things I mean to be having physical properties as Real, and things that do not have physical properties are Virtual.<br>
<br>
If this seems vague, please review {{ section_ff17d94c0d49aab3e372e47b64b96ea7 }} again, as the specific use of these terms for the purposes of this book is important for understanding what I'm trying to convey.<br>
<p id=031f037060d88ef98ae42ae359b42dd0><b><a href="#031f037060d88ef98ae42ae359b42dd0">2.6.5.1</a>: Be clear about the differences:&nbsp;&nbsp;Physical (Real), Logical (Virtual), Data (Virtual)</b></p>
<br>
{{ todo: ... }}<br>
<br>
Since I think we have a clear working definition for the terms Real and Virtual, we start to do some comparisons between them and see what other things are different.<br>
<br>
Since they have very different properties, as they are about as different as anything can be, that means that those different properties should have different advantages and disadvantages when looking at them from different perspectives.<br>
<p id=5a2ee645ef74425ffa093976096dee18><b><a href="#5a2ee645ef74425ffa093976096dee18">2.6.5.1.1</a>: Reality: The Physical</b></p>
<br>
The first important thing to know about the difference between Real and Virtual things is that you cannot know everything about a Real thing.<br>
<br>
Determine what the state of a Real thing is is essentially impossible, but we can have approximations that are good enough.<br>
<br>
Why is it impossible to know that "true state" of a real thing?&nbsp;&nbsp;Because it's state varies with every atom, and collectively all the atoms of a physical thing are too numerous and beyond inspecting in many dimensions.<br>
<br>
This is not taking this too far either, it is simply being clear about what is possible, and what is not.<br>
<br>
So, if we can't know everything, then what is possible, and what are those limitations?<br>
<br>
Let's take something fairly simple for example, such as temperature.&nbsp;&nbsp;What temperature is a physical device, we will say a 1U 19" rack server?<br>
<br>
Well, that depends on where you are measuring it from.&nbsp;&nbsp;Modern servers can have dozens of temperature sensors throughout their chassis, and those temperature sensors will approximate the temperature fairly accurately for part of the device.<br>
<br>
We could measure the each CPU socket temperature, and the temperature near the power supply, and the fans, and then we can approximate from these or list them, but there remains many places we are not even directly measuring.<br>
<br>
It happens that this is not necessarily important for our purposes, but it is important to understand and accept that this data is simply not available to us, and we have sensors in place to detect some aspects of it.<br>
<br>
Other aspects we may not have any sensors for.&nbsp;&nbsp;For instance, mobile devices often come with accelerometers, which will detect movement of the devices.&nbsp;&nbsp;Rack servers do not currently come with these sensors, and for a fairly reasonable reason, as they are not in demand.<br>
<br>
But this is one type of data that we cannot collect about this server.&nbsp;&nbsp;It could be that the amount of vibration the servers are going through could end up causing problems over large numbers of servers, and by doing correlative analysis on part failures with vibrations, and by determining where the vibrations were worse, we could contact our data center's staff and see if they could fix the problem, as it may be an undetected problem on their part.<br>
<br>
This is a completely theoretical example, but it illustrates that there are things we know, but not completely (temperature), and there are things we do not know at all about Real things.<br>
<p id=e529c9c5431e0acff31b16484c63dfad><b><a href="#e529c9c5431e0acff31b16484c63dfad">2.6.5.1.2</a>: Virtual: The Un-Real</b></p>
<br>
In the last section we learned that there are things we cannot know, or know with full accuracy about Real things.&nbsp;&nbsp;Their very nature means that they are not fully knowable, but we can know enough about them to make use of them effectively, and have a long history of doing so.<br>
<br>
How do Virtual things align on this same spectrum of "knowability"?<br>
<br>
Some Virtual things can be completely known.&nbsp;&nbsp;Other Virtual things remain unknowable.<br>
<br>
We can use the examples we used in a previous chapter.<br>
<br>
Let's look at a variable that we assign:<br>
<br>
X = 5<br>
<br>
Here, I have made X to be equal to 5.&nbsp;&nbsp;Can we know everything about this Virtual thing?<br>
<br>
Yes, we can.<br>
<br>
We can inspect this in any way we like, and know everything to know about it.&nbsp;&nbsp;We can compare it to different numbers:&nbsp;&nbsp;X < 6, X > 4, X == 10, and see if it is similar to them.&nbsp;&nbsp;<br>
<br>
Any operation we wish to make, we can perform and know the full extent of what there is to know about this Data.<br>
<br>
Now, let's look at a Virtual thing that is not fully knowable, we will look at the word and symbol of "idea".<br>
<br>
We can take the word "idea" and trace it's language roots, and compare it to other languages, and find common usage of it in popular literature, and we can ask people what it means, and in all of these things we will gain information.<br>
<br>
But, we will never know everything there is to know about the word and symbol of "idea" because it is not a concrete thing.&nbsp;&nbsp;It has subjectivity and flexibility, and can be used in different ways in different circumstances.<br>
<br>
The same is true for many things.&nbsp;&nbsp;So we have a class of Virtual things about which anything can be completely known, and another class of Virtual things about which only some things can be known.<br>
<br>
Let's simplify this into two more terms:&nbsp;&nbsp;Knowable Virtual things, and Unknowable Virtual things.<br>
<br>
We could call this "Knowable Virtual Data", but since Data is a subset of Virtual, and there exists other things that are virtual, and may be completely Knowable, that do not meet the same definition as Data, we will use the label "Knowable Virtual" and then can append anything onto it afterwards, like Data, to describe what exactly the Knowlable Virtual thing is.<br>
<br>
Let's create a spectrum for these labels:<br>
<br>
Knowable Virtual thing <---> Unknowable Virtual thing<br>
<br>
We're going to build a little forest of terms and spectrums (or axes) over the course of the book, because once we have clear terms like this, we can use them in different ways than if they were still more vague, and less specific.&nbsp;&nbsp;Once they are specific, they become tools, which we can use to help us perform work.<br>
<br>
We create a language tool when we give terms specific properties, which allow us to clearly divide information, such as Knowable Virtual Data vs. Unknowable Virtual Data.&nbsp;&nbsp;We have at least 1 property between these information topics that we can use in any algorithm as something that is clearly understood: knowability.<br>
<br>
Over time we will build up a toolset of these, so that we can communicate about incredibly complicated topics, and reason about them efficiently and clearly.<br>
<br>
As an exercise, try to come up with some of your own terms.&nbsp;&nbsp;Once you have an understanding of how to create terms for yourself, you can use this to create things you understand completely, because you made up the terms you are working with.<br>
<br>
If you can, great, write them down and add more to that list as you think of them.&nbsp;&nbsp;Over time, you will start your own set of terminology in which you can reason with, having more understanding of it than my terminology, which I have created.&nbsp;&nbsp;Like I'm doing here, you will have to define your terms for other people, or translate your terms into language they already understand, but it is important that you have a clear understanding for yourself, which creating your own terms helps with.<br>
<br>
If you can't think of any now, that's not a problem, but if any come to mind in the future, write them down, and over time more and more may start to come to you.&nbsp;&nbsp;This is a process that becomes easier and more useful over time, as you get used to it.<br>
<p id=dd889cf6d887f391188383b428c7ebfc><b><a href="#dd889cf6d887f391188383b428c7ebfc">2.6.5.1.2.1</a>: However, between Data and Logic is a huge gap, as Data is "perfectly" understandable, while Logic is not, due to Halting Problems and all other things CS-academia knows and describes very well.</b></p>
<br>
Another Unknowable Virtual thing is Logic.<br>
<br>
Logic, as we defined earlier, is an all-emcompassing term for anything to do with software or decisions, or scripts or other methods of manipulating data, executing statements, etc.<br>
<br>
One of the famous problems of computer science is the Halting Problem.<br>
<br>
This problem is essentially that is impossible to know if a program is every going to stop executing once it starts.&nbsp;&nbsp;There is a lot of information about this problem out there, so we will just leave it with that description and realize that Logic has an Unknowable Virtual element to it.<br>
<br>
However, Logic also has many Knowable Virtual elements to it, because as in our example of "X = 5", this is a statement that can be made in Logic.<br>
<br>
Additionally, just like in our example we can use the Logic itself to inspect this, or we can externally inspect the Logic using a debugger, and we can verify the data, and it is Knowable Virtual Data.<br>
<br>
So, while Logic contains some properties that are Unknowable (the halting problem being one example), it also contains properties that are Knowable, and the Unknowable does not stop us or hinder us in any way from gaining full access to the Knowable.&nbsp;&nbsp;<br>
<br>
This puts Logic in a murky place on a spectrum of Knowable to Unknowable, but that's OK!<br>
<br>
What we need to do in this instance is slice up what Logic is, and look at each of the components on the spectrum, and we will have a correct view into it.&nbsp;&nbsp;Whenever you have a compound problem, you can slice it into simpler components to better understand it.<br>
<br>
So, that would look like:<br>
<br>
- Logic: Will it ever stop running?&nbsp;&nbsp;On the Unknowable part of the spectrum.<br>
- Logic: Variables and other values?&nbsp;&nbsp;On the Knowable part of the spectrum.<br>
<br>
I leave off calling them directly Knowable and Unknowable, because Logic can be tricky, and there can be tricky things done inside logic, and perhaps in some circumstances this means that variables are not completely knowable, and there might be circumstances where we have a high confidence that a program will halt, like this pseudo-code:<br>
<br>
{{ start_code }}<br>
int main()<br>
{<br>
&nbsp;&nbsp;return 1;<br>
}<br>
{{ end_code }}<br>
<br>
We can be reasonably sure that if this program compiles, and there are not problems with dynamically linked libraries, and there are not somehow crazy macros in the white space or brackets, that this program will eventually stop running.<br>
<br>
This tells us another Knowable property of Logic, which is that it is very complex, and that it's meanings can be obscured.<br>
<br>
Take for example this Python code snippet which uses a Decorator.&nbsp;&nbsp;It's OK if you don't know Python or aren't familiar with Decorators, because it's just an example and I'll explain my meaning of it.<br>
<br>
{{ start_code }}<br>
@HelloWorldDecorator<br>
def HelloWorldFunction():<br>
&nbsp;&nbsp;&nbsp;&nbsp;return 'Hello World!'<br>
{{ end_code }}<br>
<br>
If the "@HelloWorldDecorator" wasn't there, this would read like a beginning Hello World! program, as when you call the HelloWorldFunction() function, and it returns the string "Hello World!".<br>
<br>
However, there is a Decorator to this function call "HelloWorldDecorator", which modifies the behavior.&nbsp;&nbsp;The decorator code may live in another file, so it may not be obvious what is happening when you simply look at the code.&nbsp;&nbsp;You assume it's basically going to return "Hello World!".<br>
<br>
Let's look at the decorator code I have created:<br>
<br>
{{ start_code }}<br>
# Decorator<br>
def HelloWorldDecorator(function_reference):<br>
&nbsp;&nbsp;&nbsp;&nbsp;def DecoratorInside():<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Call the Function we are wrapping<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intitial_result = function_reference()<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return intitial_result.replace('Hello', 'Goodbye')<br>
&nbsp;&nbsp;&nbsp;&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;return DecoratorInside<br>
{{ end_code }}<br>
<br>
The decorator code creates the required wrapper for the functions, as that is what decorators do in Python, and it calls the function reference, but instead of simply returning the result, as if we had called the code without a decorator, it modifies the result.<br>
<br>
It replaces the string "Hello" with "Goodbye", so we get the very different result of the "Goodbye World!" string being returned, changing our peppy introductory function into something much darker.<br>
<br>
This melodramatic example shows that we can see something that looks very clear in code, and yet something that does not necessarily looks like it will change the result we clearly see, in fact, does change that result.<br>
<br>
This is another aspect of Logic's being on the Unknowable side of the spectrum, due to it's ability to contain very high complexity.<br>
<p id=99b45325e58458c65965de974e2f7dc2><b><a href="#99b45325e58458c65965de974e2f7dc2">2.6.5.1.2.2</a>: This difference also tells us why Data is more important than Logic, because Data is more trustworthy than Logic.&nbsp;&nbsp;When making changes to data, the changes are straight-forward to understand, when making changes to Logic, the side-effects (unintended consequences) can be far-reaching and completely not understandable, and frequently enough are this way.</b></p>
<br>
Now that we have established that collectively, Virtual Data, which I will just call Data, since it is always Virtual, is Knowable.<br>
<br>
And we have established that collectively Logic is Unknowable, even though components of it may be knowable, we can use this information to set up a hierarchy, which we can use to build more robust engineering solutions.<br>
<br>
If Data is comprehensively Knowable, and Logic is comprehensively Unknowable, then we should base our actions on our Data, and treat that as the supreme truth.&nbsp;&nbsp;Our Logic is not less important because of this, as it serves the same role as it would if Logic was King, and reigned supreme over Data.&nbsp;&nbsp;One thing must have precedence over the other, because in real-world prioritization things cannot be equal.&nbsp;&nbsp;There is always a preference, and it is usually by a wide-margin, due to the limitation of resources in the pursuit of our goals.<br>
<br>
Knowing that we can treat Data as the most important thing in our operational environment means that we will always first focus on the data being correct, and then secondarily we will look at how the Logic interacts with the Data, with a careful watch that the Logic does not do anything to or with the Data that would cause us problems.<br>
<br>
Of course, you don't have to have any of this kind of analysis to know that you should not corrupt your data with your code, but this is the path I have taken to understanding where to place priorities, and how to approach working, and they have served me well.&nbsp;&nbsp;I hope to prove after we have gotten through this introductory phase, into the details phase, and finally into going over implementation, how these fundamentals are truly critical to building large, robust, resilient, controllable, manageable operational automation environments.<br>
<br>
Without all of these details, all the adjectives I just used to describe what we will build may still be applied, but they may not be true, and we may not really get those effects.&nbsp;&nbsp;Through using well defined fundamentals, we can begin to bring this assurance in.&nbsp;&nbsp;This is an important part of what Knowability gives us.<br>
<p id=3b9a062658c7f15e53b7601de12d3857><b><a href="#3b9a062658c7f15e53b7601de12d3857">2.6.5.1.2.2.1</a>: Changes to data, that meets constraints, will not harm other data, but can harm Logic that acts on the data (results of Logic, rather)</b></p>
<br>
When working with Data, is it required that certain constraints are met.&nbsp;&nbsp;This is normal database 101 stuff.&nbsp;&nbsp;If you have a relationship between 2 tables, the the primary key of Table A is referenced in Table B, and then you change that primary key in Table A, but do not update all external references to it (such as in Table B), then you will have created an inconsistency.<br>
<br>
There are methods for forcing this to not be allowed in many database software's schema configuration, using constraints and foreign keys, etc.<br>
<br>
In an Operational Automation environment it is likely that the data sets will stay small enough that you can work with these constraints enabled (without performance problems), and the changes are important enough to deal with the performance hit the constraints provide anyway.&nbsp;&nbsp;So, I recommend using software constraints when possible, and letting the database software manage enforcement of constraints to keep your operational configuration data consistent.<br>
<br>
If you find yourself in a place where constraints are causing a real performance problem, and are not working, I suggest only turning off the constraints that are the problem points, and leaving the rest of them enabled.<br>
<br>
For the areas where data constraints are turned off, you must be especially careful when making changes to this data not to lose any of the referential integrity that the constraints would have provided, with your own changes via Logic, or in unfortunate times when you manually update the database (which you should try to never, ever do).<br>
<br>
Another Knowable thing about Data, is that if you have these constraints active, then you can Know that the data is correctly configured, and it's referential integrity is consistent.<br>
<br>
There are some operations, such as dumping data and mass-importing it, that can cause these checks to be turned off, so be careful when you do this to do everything that is involved at the same time (ex: dump all tables that reference each other at the same time), to ensure that you have not imported things into an inconsistent state.<br>
<br>
We've now covered that Data can have an additional area of Knowability.&nbsp;&nbsp;How does this relate to Logic?<br>
<br>
Well, it turns out this is another area where Logic provides a fundamental weakness, and in a way that is Unknowable.<br>
<br>
You can have perfectly consistent and correct Data, with all constraints active, and have Logic that works perfectly well with all of the current data.<br>
<br>
And then you can make a change to that Data, which does not violate any of the comprehensive consistency validation tests, and yet afterwards the Logic fails against the Data.&nbsp;&nbsp;How?<br>
<br>
Logic is not actually tied to Data in that same way that Data can be tied to itself (through constraints).&nbsp;&nbsp;In a database, let's use an abstract general SQL database with transactions for this case, we can insert a valid row into database table, and all the constraint tests are made in the transactional commit process, and the data is stored correctly.<br>
<br>
When the Logic next tries to access this data, it finds the new table row, and it goes about it's normal operational logic, which has always worked before, but this time the data it receives is not something the Logic accounted for.<br>
<br>
For instance, you have a field that is an unsigned integer in the database software, so it goes from 0 to 4 billion, but the Logic expects that this data is in the range of 0 to 100.<br>
<br>
If the data entered is actually 5000, and the Logic expected it to never be more than 100, then the Logic will do something incorrect, perhaps making something that shouldn't be 50 times larger, such as memory allocations of a Java Virtual Machine, which might fail and cause a service to not start on the next attempt.<br>
<br>
Whose problem is this, Data or Logic?<br>
<br>
It is a shared problem with between the two, because the Data contains valid data based off the database software constraint system (0 to 4 billion), and the the Logic is only handling 0 to 100, and so a failure has been entered between the two, even though the Data was correctly inserted into the database, under the database's constraint system.<br>
<br>
There are many ways to approach this problem.&nbsp;&nbsp;Databases frequently have code that you can put into the database to execute at certain times (ie. user defined constraints), which could validate the values and enforce only numbers 0-100 are put in them.<br>
<br>
There are some problems with this, you will have probably tied yourself to this database platform for a very long time, whether you want to be or not, because after all of that Logic is put into the database to validate the Data, it would take a large effort to re-create it all correctly in another database software's methods, and those methods may not be fully compatible, in that you can't do everything in the target database that you could do in the original database.<br>
<br>
That is a manageable problem, however, as it deals with timescales of years, and is possibly worth of the cost-benefit tradeoff.<br>
<br>
However, there is another problem is that now you are putting Logic into your Data.&nbsp;&nbsp;We know that Data is Knowable, and Logic is Unknowable, and when you put an Unknowable into your Knowable, the result is that you end up with an Unknowable.<br>
<br>
We have just transformed our safe-space of Data into an un-safe space, because now we have custom Logic in there as well.&nbsp;&nbsp;So we do not have anywhere that is just Data.<br>
<br>
This is a huge problem as we will never be able to be assured that the Data we are accessing is going to be accessed correctly.&nbsp;&nbsp;<br>
<br>
To take our "X=5" type example, if we have a field "X" in a database table, and we have Logic running in that database, it is possible that as we test and modify that "X" field, the Logic will be invoked, and it could change the results.<br>
<br>
With this being the case, we can no longer trust that we set "X=5" and then we test "X > 4" (X is greater than 4), and we receive a positive.<br>
<br>
The Logic may have silently changed X to 4, because it had a constraint that we did or didn't know about at some point, and now we do 2 steps in a row, where we assume success is guaranteed, and we end up with failure.<br>
<br>
This is a large problem.&nbsp;&nbsp;<br>
<br>
Another issue that we deal with is that writing Logic for databases is not as manageable over time as writing Logic in other platforms, such as directly for execution or interpretation in an operating system.&nbsp;&nbsp;That is because database's purposes are to serve data, and so they do not get "best of breed" software development environments.<br>
<br>
There are many more examples I can give on how you can have consistent Data, but inconsistencies between the Logic and Data.&nbsp;&nbsp;The end result of all of these is that you must simply be very cautious when creating your Logic, and provide as many safe guards as is warranted by the needs of your organization to provide that the Logic works cleanly with the Data.<br>
<br>
There are many techniques for this that we will cover once we get to implementation.<br>
<h3 id=9ea896216c817034b6d3858d8f934e34><a href="#9ea896216c817034b6d3858d8f934e34">2.6.6</a>: Knowability</h3>
<br>
I didn't know this before I just looked it up, but Knowability is already a word in dictionaries, so there is not a lot of reason to cover it in depth.<br>
<br>
We've already been using it quite a lot, but I thought it would make sense to shortly define it.<br>
<br>
Knowability is a spectrum of how well you can know something, in full, at all levels.&nbsp;&nbsp;It needs to be extreme knowledge like our "X=5" example, where we know absolutely everything about it.<br>
<br>
Any ambiguity or aspects that remain not-perfectly-knowable need to count against it being on the extreme side of Knowability, and more towards the side of Unknowability.<br>
<br>
To set up the spectrum, it looks like this:<br>
<br>
Unknowable&nbsp;&nbsp;<--->&nbsp;&nbsp;Knowable<br>
<h3 id=e2a0bb61f2d74d70b31bf533e2b1c260><a href="#e2a0bb61f2d74d70b31bf533e2b1c260">2.6.7</a>: Class of Work</h3>
<br>
We briefly defined Class of Work in the beginning of the book, but let's take a slightly deeper look at what it means.<br>
<br>
Initially I just said it was "anything that is done", and this is true but perhaps "work" work suffice to say that, and everyone would understand.&nbsp;&nbsp;However, there is more depth we can gain from looking at it deeper.<br>
<br>
I initially used the example of automating the DNS zone file updating.&nbsp;&nbsp;If you aren't familiar with DNS zone files, they are text files look like this:<br>
<br>
{{ example_dns_zone_file }}<br>
<br>
One aspect of manual workflow generally goes:<br>
<br>
- A new host is created, and needs a name matched to it's IP address (an address "A" record)<br>
<br>
- Someone goes to the server that hosts the DNS Master files (the host people use to make edits on, and where the changes will be disseminated)<br>
<br>
- They add the line with the hostname fragment, and the "A" for address record, and the IP address<br>
<br>
- They update the serial number of the zone file (so the DNS software knows the file has been changed)<br>
<br>
- They test the file with the DNS software's configuration file validation<br>
<br>
- If the test passes, they reload the DNS zone file into the server<br>
<br>
- Then they tell the Slave DNS servers (other machines that reference this Master machine's DNS service to get records), and tell them to do a zone transfer.&nbsp;&nbsp;This might also be configured to happen automatically on the Zone file being reloaded, through the Master DNS server's software<br>
<br>
<br>
These steps might take a person 10-15 minutes to perform, on an individual basis, and slightly longer to implement for larger changes, or in larger environments where there are more tests or more templating.<br>
<br>
Sometimes it is a problem that people just forget to do one of the steps, but, since the new host wont have a DNS name, it will only be able to reference them by IP address, so usually this problem is quickly remedied.<br>
<br>
A larger problem is that people can type things incorrectly, and while the validation tests find some problems, they will not find correctly formatted zone or configuration files, which have incorrect data in them.<br>
<br>
If a line that used to exist was removed, then immediately afterward reloading services that referred to that previously-existing DNS name will start to fail, as the name no longer exists or resolves.<br>
<br>
These problems are usually caught quickly, as things will fail and alert, if monitoring is set up properly, but there was just an outage, and revenue may have been lost, or other negative consequences for an organization.<br>
<br>
Humans making manual entry mistakes are simply unavoidable.&nbsp;&nbsp;As the population of humans doing manual work increases, and the amount of work each human does increases, so will the amount of failures.&nbsp;&nbsp;This is compounded with any special conditions, where there is a standard process, but special cases exist which must be manually maintained either without automated testing, or with insufficient testing.<br>
<br>
Some failures only show up when multiple mistakes occur, so the original set-up problem may have been occurring for days, weeks or months before, but the secondary mistake triggers the initial mistake, making it harder to troubleshoot as the recent change doesn't seem to impact the part that is now broken (but did).<br>
<br>
The "delayed failure" may not have even been a mistake at all, and after reverting that change and inspecting the configuration, it might be found that it looks correct, so it is put back in, and the failure occurs again because the error requires two places to cause the failure.<br>
<br>
This is a component of Alignment, which I mentioned in the beginning of the book, but we haven't referenced in a while.<br>
<br>
The Alignment in question for our original "DNS zone entry is removed" is this:<br>
<br>
- A service, say a web server, references a database by DNS name, and is live and working<br>
<br>
- A person makes a change to the Zone file, removing the database name, but leaving the zone file in a valid state in terms of validation<br>
<br>
- The zone file is loaded and replicated, and the web server cannot reach the database.&nbsp;&nbsp;An outage has begun.<br>
<br>
What was the Alignment here?<br>
<br>
The Alignment was that the web server required the DNS server to have the name of the database server, so that it could make a connection to it.&nbsp;&nbsp;This is 1 layer of Alignment, as the web server needed the DNS server (the requirement) to contact the DB server (the goal).<br>
<br>
This is a very simple case of Alignment, but it makes the point for an initial example, which is that without Alignment, things either do not work, or do not work efficiently.&nbsp;&nbsp;In the above case, things stopped working completely with the removal of the DNS entry.<br>
<br>
Efficiency is a metric that has to do with "functioning, but not as well as we would like, or could be", and so is a more complex topic than something that does not function, which is fairly clear cut.<br>
<br>
We'll be getting very deep into the Alignment of efficiency soon.<br>
<h3 id=e51fd2df5fa27c89dbb16625df6ec6b6><a href="#e51fd2df5fa27c89dbb16625df6ec6b6">2.6.8</a>: Data Source</h3>
<br>
Since we'll be talking about Data quite a bit, I will be referring to any mechanism that stores Data as a "Data Source".<br>
<br>
This could be a database, a YAML file, a variable in a JavaScript web page that came from a JSON RPC request, it doesn't matter.&nbsp;&nbsp;There is a location that stores data, and we interact with it to get data and store the data.<br>
<br>
The Data Source may be persistent, or it may be temporary (such as Javascript data in a web page).&nbsp;&nbsp;It may be transactionally safe, or unsafe to update simultaneously.&nbsp;&nbsp;These are secondary properties, as the primary property of a Data Source is access to the data.<br>
<br>
Some qualities of a Data Source:<br>
<br>
- Access to data.&nbsp;&nbsp;Get it, set it.&nbsp;&nbsp;This is mandatory, all others are optional.<br>
<br>
- Constraints on the structure of the data (such as not being able to insert arbitrary fields).&nbsp;&nbsp;This would be a strict "schema" (schematic), as opposed to a "document" style which allows any type of modifications in the values of a record.<br>
<br>
- Constraints on the value of the data that is put into specific fields in the data.&nbsp;&nbsp;For instance, in a relational database a field in table may be of type "integer" and will not allow alphabet characters, special characters, or real numbers (decimal precision) to be inserted.<br>
<br>
- Persistence: So that the data is saved, and if the power is turned off to the system storing the data, when the machine restarts the data will still be available.&nbsp;&nbsp;There may be corruption here, unless the Data Source also offers a Consistency guarantee.&nbsp;&nbsp;Persistence simply means that things can be discontinuous (losing power is one method to lose continuity of the service), but the data will still exist.<br>
<br>
- Consistency: Ensures that the data does not become corrupted in any failure situations.&nbsp;&nbsp;These situations might be the program being terminated un-cleanly, and it might use something like a journal to keep track of on-going changes, and will replay this journal on start-up to ensure that recently changed data is the same as in the journal.&nbsp;&nbsp;<br>
<br>
To be safe, the journal is written to and flushed to disk before the "changes are made" in the database, so if anything the internal database data is consistent with the previous changes, and only new journal entries need to be applied.<br>
<br>
There are different Consistency guarantees, and while Consistency means "will not become corrupted", there are usually many methods with which data could become corrupted, but the Consistency provisions attempt to solve those problems through various Logical steps.<br>
<br>
- Transactions: Multiple changes, such as in different tables, or multiple rows in the same table, can be applied all-at-once, in an "atomic" fashion, which means that it "cannot be split further" (Atomicity), and being the smallest-type-of-action, it is guaranteed to either not-have-started, or finished completely, before another action takes place.&nbsp;&nbsp;<br>
<br>
Transactional changes are made sequentially, and cannot interrupt each other.&nbsp;&nbsp;Furthermore they verify the consistency of the entire exchange, and not simply each statement, which allows more precise validation of referential integrity as well as being able to make changes that would be constraint violations if done one-at-a-time, but which are consistent when done together in a transaction.<br>
<br>
- Replication: This allows copies to be made of the data to at least 1 other instance of the Data Source implementation, for example a SQL server could incrementally copy it's journal file from itself to another machine, which then applies the journal.&nbsp;&nbsp;If the original machine goes down, the replication target machine will have an update-to-date version of the database, up to the latest journal entry it received.<br>
<br>
Replication might be after-the-fact replication, so a transaction completes on a Master DB, and then the Slave DB will get the same transaction request moments later, after the latest bytes of the journal file has been copied over to the Slave, and the replication agent re-runs the remote transaction statements on the local database.<br>
<br>
Replication might also be in lock-step with the Master, so a server that gets a write request will complete it on itself, and then wait for 1 or more other replication servers, based on a "quorum" number.&nbsp;&nbsp;If the quorum is two (2), then at least 2 servers must have this transaction committed before the client requesting the transaction is told that it was successful.&nbsp;&nbsp;This method is much slower in terms of returning a result to a user, but is safer in that the information is persisted on multiple server's storage, in case a corruption-level failure happens on the original server.<br>
<br>
There are many other properties to Data Sources, so this is not meant to be an exhaustive list, but a brief coverage of some elements we can associate with the label Data Source, which may or may not exist in a given implementation you may use.<br>
<br>
Some Data Source implementations offer features that are in opposition to some of the above, and those feature sets are also useful, since they provide different benefits and weaknesses to some of the features I have mentioned.&nbsp;&nbsp;The right tool for every job, and all that.<br>
<br>
{{ todo__make_more_of_these_qualities_lists_for_other_terms_and_things }}<br>
<h3 id=10c0b236af1081d0c601a87fb274211c><a href="#10c0b236af1081d0c601a87fb274211c">2.6.9</a>: Operational Environments</h3>
<br>
Any place where any operating is going on is an "operational environment".&nbsp;&nbsp;This could be on your desk, or in your closet, or in a data center, or across a number of data centers across the world.&nbsp;&nbsp;The size and location of the operational environments is not what defines an Operational Environment.<br>
<br>
What defines an Operational Environment is the purpose you wish to achieve with it.<br>
<br>
Often it can be useful to think of an Operational Environment as a Security Zone.&nbsp;&nbsp;You allow certain people to make certain requests in each security zone.<br>
<br>
For example, on your laptop or desktop machines, you probably only allow yourself, and perhaps your Corporate IT department, to execute software or make configuration changes to the single machine in these environments.&nbsp;&nbsp;We don't want people on the internet connecting to our personal machines, so we will want to restrict any external connections.<br>
<br>
If we move to a Quality Assurance (QA) environment, we may allow all QA engineers to make data changes, and software pushes to these machines, but we only allow certain operations staff to have administrative access, and make system-level changes, so all of the systems stay in a similar state.&nbsp;&nbsp;We generally don't want any external access to a QA environment, but we might allow whitelisted access for some partner companies who either provide us services, or who are doing integration with your developers.<br>
<br>
Looking at a Production Environment, we would want to have much more auditing, and restrictive access of who could login to servers and make changes.&nbsp;&nbsp;We also all do allow external access from our customers, who could be anyone located anywhere, and may allow un-authenticated (guest) access to our services.<br>
<br>
Operational Environments, and their corresponding view as a Security Zone, is an important consideration any time you are performing Operational work.&nbsp;&nbsp;Where are you doing this work?&nbsp;&nbsp;What are the goals?&nbsp;&nbsp;What are the rules and restrictions?&nbsp;&nbsp;Who gets access, and what are they allowed to do?&nbsp;&nbsp;<br>
<br>
How do we ensure all of this stays consistent?&nbsp;&nbsp;How do we maintain this, make changes, and automate regularly occurring processes?&nbsp;&nbsp;What about monitoring and alerting on things we care about?<br>
<br>
All of these will change every time you change what Operational Environment classification you are in.<br>
<p id=2880d6cb6fe0e0528df63476d031e45e><b><a href="#2880d6cb6fe0e0528df63476d031e45e">2.6.9.1</a>: Production Environment</b></p>
<br>
The most important environment for any given system is the "Production" environment.&nbsp;&nbsp;This is the environment in which the organization makes their revenue (ex: online service), or interfaces with their customers (ex: informational service), or creates their product (ex: manufacturing).&nbsp;&nbsp;"Production" comes from "product", as in a "production line" which in an assembly line that produces an end-good product, it has the meaning of the "end of the line" in terms of an organization producing a good or service, which will then be distributed.<br>
<br>
The Production Environment, which I will mostly just be calling "Production", is the place that the critical operations of your organization takes place.<br>
<br>
This might be a data center that has many peered network circuits, in which you receive internet traffic and generate revenue.<br>
<br>
Or, it could be a server farm in your corporate offices, in which processing occurs, which is critical for the functioning of your organization.<br>
<br>
Or, it could be in a cloud or managed hosting environment, in which you mostly manage through a browser application.<br>
<br>
It doesn't matter what exactly the circumstances of your "Production" are, you should be aware of what it is, and how it is treated different than other areas of your organization.<br>
<br>
Things in Production should be the most important things, and not intermingled with devices or services which are not of the same critical importance.&nbsp;&nbsp;Sometimes sharing of environmental space will have to occur, but this should be minimized, and remedied once it is possible to do so.<br>
<br>
The Production environment should have the highest levels of security, where only authorized personnel are allowed to access the server instances, and every login and preferably every command issued is logged, for auditing purposes.<br>
<br>
This follows the "AAA" process of: Authenticate, Authorize, Audit.<br>
<br>
In brief:<br>
<br>
- Authentication is determining who someone is.<br>
<br>
- Authorization is determining if they are allowed to do what they are trying to do.<br>
<br>
- Auditing is logging everything that happens, so that it can be reviewed.<br>
<br>
<br>
There is a fourth "A" that be added {{ todo_forgot_what_this_is_tempoarily_but_i_wrote_about_it_years_ago }}<br>
<p id=85f5ad95d9e4d6cd51f782e15b9a380d><b><a href="#85f5ad95d9e4d6cd51f782e15b9a380d">2.6.9.2</a>: Staging Environment</b></p>
<br>
.......<br>
<p id=42913fa225b25b38eee2478890c7cdc9><b><a href="#42913fa225b25b38eee2478890c7cdc9">2.6.9.3</a>: QA Environment</b></p>
<p id=e51f755569b88937197a5286a282bf76><b><a href="#e51f755569b88937197a5286a282bf76">2.6.9.4</a>: Performance Bench Testing Environment</b></p>
<p id=d1a4f057af493912852ac12fc03ca9b3><b><a href="#d1a4f057af493912852ac12fc03ca9b3">2.6.9.5</a>: Corporate Environment</b></p>
<h3 id=13670fd1278efaec64988e5172bfe5a2><a href="#13670fd1278efaec64988e5172bfe5a2">2.6.10</a>: Server</h3>
<h3 id=0f75446224bba09c030dd81e3e0fa4ac><a href="#0f75446224bba09c030dd81e3e0fa4ac">2.6.11</a>: Device or Machine or Nodes</h3>
<h3 id=3d2ece14db911afb11e032b9c3c646b7><a href="#3d2ece14db911afb11e032b9c3c646b7">2.6.12</a>: Humans</h3>
<br>
It feels a bit weird when I say or write "Humans", as it's strangely impersonalizing to everyone, I feel.&nbsp;&nbsp;However, it is conveniently clear to differentiate not only from "Not Human", or "Logic Based" or "Software" or whatever, but also clear in the sense that I am not speaking casually about people, but specifically about the type of effects that Humans cause.<br>
<br>
We generalize about "people" all the time, different groups of them, to have any sort of discussion.&nbsp;&nbsp;Sentences can only carry so much information in them at any given time, because words only have so much meaning, and a word is composed of syllables, and those take time to write or say, and they have to be done sequentially: the syllables cannot be written or said simultaneously to be more efficient, and so generalizing or summarization is required.<br>
<br>
Without summarization and generalization, we would spend so much time getting to the point, by being maximally explicit in every detail, much in the way I am doing right now, that we would just not get to the point, and all communication would cease to function.<br>
<br>
Shouldn't there be a spectrum for this?&nbsp;&nbsp;Let's make one:<br>
<br>
Generalization&nbsp;&nbsp;<----->&nbsp;&nbsp;Specificity<br>
<br>
Now we have an axis on which we can slide a variable across, to be more or less specific, and it can be tuned in the way we want it, for every circumstance that is possible.<br>
<br>
In addition to this, we can add in another topic we recently covered, such as "Atomicity".<br>
<br>
We can be extremely specific in our discussion of Atomicity, or we can be extremely General, or somewhere in between, in the spectrum, along the axis.&nbsp;&nbsp;I will use this method of multiple examples mixed together to provide a richer tapestry for these ideas to be expressed in, as the book goes on.&nbsp;&nbsp;These are tools for communicating more deeply; they are another spectrum or axis, which our goals can be applied against.<br>
<br>
Let's just combine some right now, and make a new communication tool.&nbsp;&nbsp;We just discussed "Atomicity" as a topic, on the spectrum/axis of Generalization <--> Specificity.&nbsp;&nbsp;Let's combine the Atomicity spectrum and the Specificity spectrum together, and create a topic based on the two dimensional coordinate system that those two axes create.<br>
<br>
Atomicity:&nbsp;&nbsp;Not Atomic <---> Atomic<br>
Specificity:&nbsp;&nbsp;General <---> Specific<br>
<br>
I ended up writing these "Right to Left" in terms of the subject being in a full-state, or an empty-state, but they could just as easily be written "Left to Right" (in reverse order), if it is more convenient for the problem at hand to see them in that way.&nbsp;&nbsp;This process of ordering things as needed for the current problem is another tool that can be applied, and which has properties that can be evaluated.&nbsp;&nbsp;For the sake of keeping up a fluid pacing for this book, I can't go into detail on each of these things as they arrive (even though I would like to: enhance, enhance, enhance).<br>
<br>
Now that we have these two axes, which we could use in the Cartesian coordinate system, we can plot a point on it, and then create text that describes that point.&nbsp;&nbsp;This is a sort of generative tool, in which one can use one's knowledge of an information space to generate any amount of specific data.<br>
<br>
If you are familiar with any sort of procedural generation, this yields the same kind of effect that Perlin or Simplex Noise allowed in procedural generation, in that because the pattern remained consistent whether viewed from "from away" or "up close".&nbsp;&nbsp;Procedurally generated content (images, models, clouds, cities, whatever) could scale to "infinite" detail, either looking at the "big picture" or with a "magnifying glass".<br>
<br>
In the same way, this generative tool of mapping axes to an information space, and then using your own understanding of that space to extrapolate what text would describe that point in those axes' space.&nbsp;&nbsp;<br>
<br>
This is actually the exact same technique I am using to write this book, as I have broken up the information space I am trying to cover into both a linear (sequential) flow (chapters), and then assigning various variables (in the forms of words in the topics) to create each chapter's text.<br>
<br>
Let's do one of these now:<br>
<br>
For the Atomicity value, let's say on a scale of 1.0 (Atomic) to 0.0 (Not Atomic), we have an Atomicity value of 0.25, or not very Atomic, but having some Atomic characteristics.&nbsp;&nbsp;<br>
<br>
Then let's say on the Specificity scale of 1.0 (Specific) to 0.0 (General), we have an Specificity value of 0.75, or fairly specific.<br>
<br>
Because we need to be specific, I am going to make up some details about the Atomicity of the thing in question, which I will use a database for:<br>
<br>
{{ start_quote }}<br>
This database provides limited atomic transactions.&nbsp;&nbsp;Transactions are accepted, and written into a journal file, which is flushed to disk periodically, but not in sync with the transaction being considered successfully completed, for performance.&nbsp;&nbsp;The means that in certain circumstances a transaction may be partially written onto the journal file disk, and in these cases recent data writes can be lost.<br>
{{ end_quote }}<br>
<br>
So, this terrible database accepts things as Transactions, and journals the transactions, but it doesn't flush the journal as part of the transaction success criteria to make it Atomic, so you might have partial transactions written on the disk.&nbsp;&nbsp;This is actually always potentially true, since a power failure could cause a partial transfer, in some hardware configurations, but the difference is that a successful result would already be returned to the client, even though the write will later fail to complete.<br>
<br>
In practice, modern controllers accept a queue of IO requests, and can do some optimizations on them, depending on the construction of the storage medium (what type of disk/etc), and so flushing merely pushes more things onto this queue, and if you cant put more things into the queue, you have already maxed out your throughput in this configuration.&nbsp;&nbsp;Unless the queue has a battery backup to complete operations in case of primary power failure, than power failure will always potentially cause writes to fail that you think were accepted.&nbsp;&nbsp;Unless you force your OS to not complete writes until the storage device has ensured it was written (which has a performance penalty).<br>
<br>
In this case, it is possible that the queue can take more total IO requests if they are batched, and for a given workload and hardware specification, you may need to do this, understanding the performance to consistency trade offs.&nbsp;&nbsp;Moving on.<br>
<br>
<br>
What if we had a Specific value of 0.0, instead of 0.75?<br>
<br>
In this case we would be 100% Generic, but we still have to say something relevant so we might summarize:<br>
<br>
{{ start_quote }}<br>
This database handles requests in Transactions, and writes them to a journal file, but flushes only periodically, so Transactions may be lost on power failure.<br>
{{ end_quote }}<br>
<br>
This gets across the idea of what's going on, but is very brief about it.<br>
<br>
What if we had a Specific value of 1.0, instead of 0.75?<br>
<br>
We would have to specify the entire code, every line, and it would need to be idealistically correct (or actual implementation), and we would have to specify all environment requirements.&nbsp;&nbsp;Why?&nbsp;&nbsp;Because we are 100% Specificity at 1.0.&nbsp;&nbsp;This means absolutely everything must be specified, if this spectrum or axis is to have real meaning.<br>
<br>
Taking this into account, maybe my example using 0.75 for that level of specificity isn't nearly detailed or specific enough, but on first introduction 0.75 sounds like "pretty specific", where 0.5 sounds "half specific, half vague", and I wanted to be detailed enough to get real implementation points across, but also not too long for pacing.&nbsp;&nbsp;Only after thinking about what 100% Specificity would really mean does 0.75 seem too high for our previous example.<br>
<br>
This is yet another tool for performing evaluations, by making one example, and rating it, and then making another (or a series of others) example, and rating those, and then going back and re-rating the first examples, then the second again, and finally creating examples of the most extreme situation you can imagine at both ends of the spectrum (being 0.0 and 1.0), and then re-evaluating the middle ones again.&nbsp;&nbsp;This is a method for getting a numerical sense of an information space.<br>
<br>
So, these are 2 more tools we can use in the future to discuss problems in a clear and precise manner.&nbsp;&nbsp;Trying to get as close as we can to 1.0 specificity, without losing the ability to make progress.<br>
<br>
But where we're we?&nbsp;&nbsp;Oh, yes!&nbsp;&nbsp;Humans!<br>
<br>
When we are having conversations like the one we are sort-of currently involved in, being specific by saying "Humans" instead of any other word allows us to understand we are using technical jargon, and we mean technical things.<br>
<br>
This allows us to move away from our standard social communication style, and into a technical communication style, to discuss technical points at a detailed level.<br>
<br>
So while it is weird to type and say, it has a benefit for clarity, which is an important attribute of Engineering.<br>
<br>
Also, it will make it easier to relate to your future AI overlords, which will be helpful.&nbsp;&nbsp;("The humans are revolting!", "I know, right?")<br>
<h3 id=eb72cfe6249ca80ac02d25c50109a4da><a href="#eb72cfe6249ca80ac02d25c50109a4da">2.6.13</a>: Philosophy</h3>
<br>
If you didn't know, there are 2 Greek roots in the word "Philosophy".<br>
<br>
These roots are "love" and "wisdom", so Philosophy is the "love of wisdom".<br>
<br>
I look at Wisdom and Intelligence as different axes.<br>
<br>
Wisdom is gained from experience, and has to do with the breadth and depth of insight into topics, and being able to make judgements that detail what might be favorable and unfavorable outcomes, and why.<br>
<br>
Intelligence I look at in very different perspective, which is "making an action that yields beneficial results for all parties involved."<br>
<br>
This is not a common definition of Intelligence, but it has a rigid definition, and comes from a brilliant article written by Carlo M. Cipolla, a professor of Economics at UC Berkeley, and is one of the greatest things I have ever read, and quite literally changed my life.&nbsp;&nbsp;I saw the world differently after having ingested it, and am much better for it.<br>
<br>
The article is entitled "The Basic Laws of Human Stupidity", and while it's title and subject matter focus on "Stupidity" (anti-Intelligence), it's real function for me was to qualitatively and quantitatively define what intelligence is.&nbsp;&nbsp;He puts it on a 2D graph, and charts it, and allows for pinpointing different kinds of Intelligent and Anti-Intelligent actions.&nbsp;&nbsp;Try not to let the negative sounding name cause you to avoid this information, it is a very important set of thoughts he has encoded there-in.<br>
<br>
http://www.amazon.com/The-Basic-Laws-Human-Stupidity-ebook/dp/B005ZX622C<br>
<br>
http://harmful.cat-v.org/people/basic-laws-of-human-stupidity/<br>
<br>
{{ todo__request_rights_to_reprint_article_in_my_book_from_family }}<br>
<br>
These start to illustrate the differences between Intelligence and Wisdom, to me, and will hopefully (over the course of the material) become clearer and useful to you as well.<br>
<br>
So Philosophy is the "love of wisdom", and I love wisdom, so I take it for that.&nbsp;&nbsp;I orient myself on "Applied Philosophy", which is using Philosophy in a way in which that I can achieve results (internally and externally) and not merely as a way to win arguments at dinner parties, or making witty comments that end with "Do you want fries with that?".<br>
<br>
Another purpose of Philosophy is to be a structure around the question, "Why?"<br>
<br>
In much of Engineering we focus on "How?":<br>
<br>
- How do I use this library or software?<br>
- How was this software written?<br>
- How do I get the result I want?<br>
<br>
Philosophy is more angled like:<br>
<br>
- Why should I use this library instead of that other library?&nbsp;&nbsp;How are they different?&nbsp;&nbsp;What will be the effect of using the one, versus the other?&nbsp;&nbsp;If one of them is better suited for my current situation, but the other may be better suited to a future situation of mine, when would be the time to start switching over?&nbsp;&nbsp;Is it worth doing?&nbsp;&nbsp;Should we even be doing any of this at all?<br>
<br>
- Why was the software written in this way?&nbsp;&nbsp;How was the developer trying to allow me to solve problems with it?&nbsp;&nbsp;How can I best use this software to work with the way the developer was trying to enable me to solve a problem?&nbsp;&nbsp;Between the different ways I could do this work, what are the different effects they will cause, and which of those do I think will be most beneficial for me?<br>
<br>
- Why am I doing this?&nbsp;&nbsp;What are my goals?&nbsp;&nbsp;How can I define them precisely?&nbsp;&nbsp;Is my entire team in agreement with this, as an intention?&nbsp;&nbsp;Are we able to communicate effectively, ensuring that we understand each other and can work together efficiently?&nbsp;&nbsp;How would we know if this is true, and we are succeeding?&nbsp;&nbsp;How can we measure that success, and compare it to the goals we wanted to achieve before we started?<br>
<br>
Philosophy is about depth, and the ability to inspect things from different angles, and while it may appear on the surface (and is sometimes explicitly stated) that it is trying to "define the way things are", in actuality the Philosophical inspection never ends (Infinitely Recursive in All Dimensions), and so it does not have the ability to ever define things "the way they are", because it can't stop defining things.<br>
<br>
This is a "Machine" in which we can know it will never halt.&nbsp;&nbsp;There is no final exit or return from Philosophy, it is a rabbit hole that never ends, and goes as deep as you are willing to look, and the detail expands to meet any closer inspection.&nbsp;&nbsp;What is true from one perspective, or frame of values, is false from another.&nbsp;&nbsp;It's flexibility to reframe data is infinite.<br>
<br>
{{ todo: Cleanup needed immediately below. }}<br>
<br>
This is do to "Why?"&nbsp;&nbsp;Why?&nbsp;&nbsp;Why?&nbsp;&nbsp;Why?&nbsp;&nbsp;Why?&nbsp;&nbsp;...<br>
<br>
I think Philosophy has a bad-wrap these days, and I hope to show, if only in a thin slice, that there is a way to use Philosophical ideas in a practical way to add clarity and improved performance in your life and work.<br>
<br>
Transitioning back to Wisdom (Note to self: Awesome segue!):<br>
<br>
One simple way to see Wisdom is "good ideas".<br>
<br>
To keep things simple and say, "I love good ideas", is why I love and heavily utilitize methods of philosophy.&nbsp;&nbsp;I make use of different kinds of philosophies in my own ways, I take their definitions and interpret them in my own meanings, and I mix and match pieces wherever I need to, as configurable tools to be used in understanding the problem I have at hand, and manipulating them into what I what I want them to become, to get the results I want.<br>
<br>
This is what philosophy is an element of, for me, and how I will be using it, in this book.<br>
<h2 id=af1f8c9950e296d130a668076e4ba88b><a href="#af1f8c9950e296d130a668076e4ba88b">2.7</a>: The Philosophy of Pragmatism</h2>
<br>
Pragmatism is a formally written up philosophy, and you can read more in-depth about it on the Internet or various books.<br>
<br>
For the purpose of this book, we'll be using it in it's core form, in my usage, which is:<br>
<br>
"Pragmatism is when you only evaluate an action based on the effects, and nothing else."<br>
<br>
"Effects" are different than "results", because results is more about what you wanted to achieve, and whether you felt you achieved that thing or not.<br>
<br>
"Effects" are more general, and deal with all things that come from an action.&nbsp;&nbsp;The change of state from before to after.&nbsp;&nbsp;How are things different?&nbsp;&nbsp;How did they change?&nbsp;&nbsp;What are the effects of this change?<br>
<br>
There can be a lot of confusion with the word "pragmatism", and it is often used interchangeably with "practical", and sometimes conflated with "common knowledge", but it does not mean these things, and for the purpose of this book we will be strictly avoided any conflation with "practical".<br>
<br>
"Practical" is a very loose term that means efficient in both resources and results, it gives you "good enough" results, with an acceptable amount of resource usage.<br>
<br>
This has nothing to do with Pragmatism, as Pragmatism has no concern for the amount of resources that were used, or if the burden was terrible, or whether it was convenient.&nbsp;&nbsp;These things may show up in the "effects" of an action, such as the amount of resources impacted is part of the effect, but "practical" ties these things together as being important in the concept, whereas with Pragmatism, all of the effects are simply data and can be evaluated as to whether those are desirable effects, or not.<br>
<br>
This also covers another topic that causes confusion, which is "side-effects", and although this is useful in language to denote things that occurred that may not have been part of the "main" or "center" (hence, "side"), in truth all things are simply effects.&nbsp;&nbsp;Whether they are in the "center" or the "side" is based on your perspective, and is likely to cause partial blindness in evaluation when they are separated, instead of being seen as a single set of effects.&nbsp;&nbsp;Some effects you intended, some effects you did not intend, but they are all equally effects of the action.<br>
<br>
Grouping everything into only one single pool of "effects" is the better way to do this, when you want to prioritize for accuracy and clarity, because you are not trying to push anything to the "side-lines" and are seeing all effects as being caused by your action, and thus will evaluate that action's effects more comprehensively than separating effects into "desired and undesired" categories, and primarily looking at the "desired" category when performing post-action evaluations.<br>
<br>
**What are we excluding when we only look at effects?**<br>
<br>
Initially, we are excluding our value judgements, our goals, our history, culture, feelings, wants and desires, and anything else, so that we can focus on dealing with "what changed?" or "what will change?", and detailing these effects (changes) qualitatively and quantitatively, where possible for each.<br>
<br>
This allows us to go beyond whatever limitations we might be currently bound by, in terms of our perspective or awareness.&nbsp;&nbsp;If we don't apply our bias to the situation before we have enumerated and started to evaluate all of the effects, we are likely to find additional effects from the one's inherent to our goals.<br>
<br>
In terms of getting coverage like "all of something", we are obviously talking about potentially a lot of data and too much to grasp at any time, and this is where Systemic Thinking and Slicing the Pie come into effect.&nbsp;&nbsp;We can box these effects into groups, to be inspected in more detail as needed, or viewed from farther away with less detail, or less Specificity.<br>
<br>
Again, this ability to scale in or out from details, is an important skill that needs to be developed and applied to get a good grasp on what is going on in any given situation.&nbsp;&nbsp;Without this, one is going to be "stuck" with the view from one's current perspective, which may be inconsistent through different circumstances, giving one inconsistent results even when it seems like one's perspective is remaining the same.&nbsp;&nbsp;One can't see the same things under different environments, because there are different things to see.&nbsp;&nbsp;One's perspective should always adapt to the problem at hand, and the environment and resources involved.<br>
<br>
I like to give examples with every topic I introduce, but I don't think it's the right time to go into a deeper example on this topic, so we will just touch the surface of an example we will soon delve into deeper.<br>
<br>
**How can we use Pragmatism to get better results?**<br>
<br>
For instance, one thing that we are concerned about greatly in Production Operations is "up-time", which is the Availability of our services.<br>
<br>
How do we get the "best" (most) up-time?&nbsp;&nbsp;Well, the most important thing is actually a "negative", which is "don't go down".&nbsp;&nbsp;However, "not going down" takes "all the things" working all the time, even when some things fail.&nbsp;&nbsp;This is obviously a very complicated endeavor to try to improve.<br>
<br>
By using Pragmatism, and only focusing on the "effects" of doing one thing, versus another thing, we can evaluate that method with the highest signal-to-noise ratio, so that we are spending more time thinking of the most-relevant things, and are actively trying to avoid things that may be distractions.<br>
<br>
Knowing that one thing that causes down-time events is "Humans making changes" we can say that we want to optimize for making more changes through automation, and less changes through direct Human manual (by hand) efforts.<br>
<br>
Since Logic is able to be written so that it runs deterministically (if done "properly"), then this Determinism is an attribute which helps us improve our up-time, by removing the non-determinism of manual Human changes.<br>
<br>
We can evaluate these based on the effects of what happens when Logic updates a DNS Zone file 10000 times, versus having Humans update a DNS Zone file 10000 times.&nbsp;&nbsp;From these cumulative effects, we can see that the Humans will make more mistakes in the act of updating the zone file, than the Logic will, and thus the effect of Human edits are more errors, which reduce our up-time.<br>
<br>
There is a lot more detail that could go into this analysis, as with anything, but this is getting our feet on the path of how to analyze things by their effects, trying to strip out anything that is not an effect of the process.<br>

# Chapter 3: Engineering Philosophy and Methodology in Operations


Alright!  The book is really starting now!



We have cleared the hurdles of disclaimers, how-to-read, introductions, and terminology.  We can now get into the real substance of of why we are both here:  The Engineering of Operations.





<h2 id=b313ae83a593ebeebefbf3e427c23f35><a href="#b313ae83a593ebeebefbf3e427c23f35">3.1</a>: What is Engineering?</h2>
<br>
More definitions?&nbsp;&nbsp;Well, we are never going to stop defining and re-defining things to our particular circumstances, as we simply can't front load all the thinking, and sometimes we will need to be more specific.&nbsp;&nbsp;At least we are now into the real content, and no longer strictly in the peripherals.<br>
<br>
Engineering, to me, is:<br>
<br>
**"The efficient use of resources applied in an environment, to yield a desired effect."**<br>
<br>
Generic and vague?&nbsp;&nbsp;You bet!&nbsp;&nbsp;But, also it can be used to insert in any specifics into the general terms to get at a more specific definition, like so:<br>
<br>
"The efficient use of time, personnel, money and physical devices (servers, etc) applied into a Production Operations environment, to yield high up-time, acceptable performance, and scalable management."<br>
<br>
That's starting to be more clear, and more specific to our current topic than the more general answer, but I see all of Engineering as a similar set of options.<br>
<br>
Whether Engineering is applied to building a bridge, a canal, a sky scraper, baking a cake, or managing a production operations environment, it needs to be:<br>
<br>
+ Efficient (because being inefficient might mean it is not able to be completed, or "fails")<br>
+ It has certain resources (universally time, almost always money, and also almost always people<br>
+ It might be soil conditions, and logistics of getting materials from Point A to Point B, or whatever)<br>
+ It has specifically desired effects, such as a set of interlocking canal segments of the Panama Canal, or a sky-scraper buildings ability to stay erect under it's own enormous weight and support and movement of the soil, or the digital and physical equivalents in server operations.<br>
<br>
Regardless of the topic or domain, the initial approach to engineering a problem is the same.&nbsp;&nbsp;Determine the environment and resources in play, determine the requirements of meeting our goal, determine the actions that can be taken to fulfill those requirements, create a plan to perform the actions, evaluate the plan's methods of implementation, risks, etc, implement the plan, evaluate the implementation, whether we met our success criteria, and update the documentation based on the new state of the environment and resources.<br>
<h3 id=2ee66e2e591f559bcad84f3a294d732a><a href="#2ee66e2e591f559bcad84f3a294d732a">3.1.1</a>: A brief interlude on the Strengths and Weaknesses of Metaphors</h3>
<br>
There is a trade-off on Metaphors, and it has to do with expert-knowledge and accuracy.<br>
<br>
Metaphors, in my opinion, are most useful when are you not an expert on the subject of the metaphor, or defer your expertise to see the metaphorical example being used as tool for communication.<br>
<br>
If I give the example of:<br>
<br>
 "Production Operations must deal with the problems given by information alignment and physical hardware management, similar to how building a bridge must deal with the soil, water, wind and temperatures around a bridge, and the materials used to construct the bridge."<br>
<br>
This metaphor, or simile in this case, is most useful if the audience are not experts at building bridges.&nbsp;&nbsp;As an expert in building a bridge, they may have a very different take on what it takes to build a bridge, and what the issues are, and they may validly complain about my use of analogy between information and soil.<br>
<br>
This is where metaphors are weak, because they are meant to give "a comparative idea" by taking us out of the details we are currently immersed in, and putting us into a "very loose" frame in another topic which we can discuss as non-experts.&nbsp;&nbsp;In a sense this "levels the playing field", as neither party is an expert at bridge building, so we can use that to illustrate our points of view without getting into details where we do have expertise, but our definitions and values may not be Aligned and need to be discussed.<br>
<br>
Because of this, it may be useful to change metaphorical topics if someone introduces details about the metaphor which derail the intention of using a metaphor.&nbsp;&nbsp;This can be referred to as "over-extending the metaphor".<br>
<br>
If you find yourself disagreeing with a particular metaphorical usage, try to re-frame the metaphor yourself into a different topic, preferably one you do not have expert knowledge in, and see if you can gain more insight into it that way instead.&nbsp;&nbsp;<br>
<br>
This can also be a useful tool in determining if you understood someone correctly, as you can re-frame what you understand of their point with a different metaphorical topic, allowing them to re-map what they meant to your new metaphor, and if they are agree, you are both likely thinking of very similar things.&nbsp;&nbsp;Going back and forth like this, when there is still mis-alignment, choosing new metaphorical topics, or changing the reference of the metaphor, can allow a complex topic to be worked through in a shorter period of time than going to full-fundamental-definitions and working up from there.<br>
<br>
The "Expert's Curse" is a real thing, and doesn't just ruin movie plots ("We are 10 digits into hacking the mainframe password, but they are using 49-bit encryption, so it will take two more hours.&nbsp;&nbsp;You need it done in 10 minutes?&nbsp;&nbsp;We'll make it happen."), but also can ruin the intention of any type of alternative explanation, which is trying to expand on an idea in a hand-wavy-kind-of-way.<br>
<br>
This is an attempt to get you to use more information than what is being provided, which you already internally know, instead of explicitly providing all the information.&nbsp;&nbsp;People have amazing inherent skills at filling in this information, and while this works best in spoken conversations (say, where you could finish the other person's sentence), metaphors are an attempt to do that explicitly by providing a non-related but comparable reference.<br>
<br>
The goal of communication is the exchange of ideas, and it is important to always return to this goal, s we can remove anti-goals, such as competition, or "Being Right", or any other anti-goals that get in the way of communicating in a fashion that allows us to achieve our True Goals.<br>
<h2 id=a941939e629b2be25c1ba265cbd9aaed><a href="#a941939e629b2be25c1ba265cbd9aaed">3.2</a>: Difference between Application and Operational Logic</h2>
<br>
Is there a difference between Logic that is written for Operations automation and Logic that is written for non-Operations?<br>
<br>
In my opinion, there is, and it is a big difference.&nbsp;&nbsp;It doesn't need to exist, but it does exist, and they are not mildly different, but extremely different, at present ({{ CURRENT_YEAR }}).<br>
<br>
I see this changing more in the future, as distributed programming environments not only become normal, as they are are now, but that we start to get generational levels of experience in the field.&nbsp;&nbsp;Generation Levels of Experience is required because there are many lessons to be learned, and then summarized, and then classified, and then come up with procedures for handling, and then generationally iterate on all of this, and this work has barely begun.<br>
<br>
I will call non-Operational Logic "Application Logic", even though it may not strictly fit your definition of what an Application is, since it changes under different contexts.&nbsp;&nbsp;If we we're to put this on an axis, we could call it:<br>
<br>
Application Logic&nbsp;&nbsp;<----->&nbsp;&nbsp;Operational Logic<br>
<br>
For instance, in a Production web serving environment, you frequently have "Application Servers" which might run Java Tomcat, JBoss, or Ruby on Rails, or a Python, or other Logic required for producing dynamic web content.<br>
<br>
These would be "Application Logic" in this terminology, as I'm using it.<br>
<br>
**What is the difference between Application Logic and Operational Logic?**<br>
<br>
The main difference is Resiliency and Minimal Dependencies, and these have a number of sub-parts.&nbsp;&nbsp;Some examples:<br>
<br>
- Application Logic requires that the environment that it runs in be configured, or the Logic will fail, and often will fall non-gracefully.&nbsp;&nbsp;How gracefully it fails generally has to do with how "mature" the Logic is, in terms of it's life cycle.<br>
<br>
Example: An application server is started without a required configuration file in a specific directory, so the application server program exits with a status code of 127 and output to STDERR "Cannot open file: /path/to/file".&nbsp;&nbsp;This is reasonable for an Application server, because it needs to be completely and correctly configured for it to return the correct results to a client.<br>
<br>
- Operational Logic is built to support infrastructure, with the knowledge that the infrastructure components are going to fail, and the Operational Logic needs to not only recognize the failures, but needs to continue to work in whatever ways are still available.&nbsp;&nbsp;<br>
<br>
Example: A operational software is written which will execute remote code on hosts, for the purposes of managing Application state.&nbsp;&nbsp;The remote programs which are executed will modify the Application's state, so that clients will receive different information after the state change.&nbsp;&nbsp;If the operational software cannot update the Application, perhaps because a file is missing (similar to the Application Logic example above), the Operational Logic cannot simply exit with an error code and message.&nbsp;&nbsp;It cannot complete it's task correctly, but instead must continue to run, and create a local and remote log of the failure, with any additional environmental data that is required to help troubleshoot this problem, and then proper staff must be notified of this failure, and potentially other servers must be updated accordingly (rolled back, or different update), to account for the failure to update this Application state.<br>
<br>
Don't misunderstand me and construe that I am criticizing Application Logic or their developers, and praising Operational Logic or their developers; they each have different goals, and so will produce works that have different results because of this.<br>
<br>
The differences between Application and Operational Logic are due to differences in priorities and responsibilities.<br>
<br>
Operational Logic is responsible for:<br>
<br>
- Infrastructure configuration and on-going maintenance<br>
- Configuring Application services and maintenance assistance<br>
- Monitoring and notification of Operational and Application state<br>
- Solving operational failures<br>
<br>
Applications are made to provide end-users with:<br>
<br>
- Correct and timely results, for a given Application<br>
<br>
Application Logic has an expectation that the operational environment is working correctly, and so error detection and handling is typically rudimentary, and output and results are intended for Application experts.&nbsp;&nbsp;This is a natural prioritization, and not an incorrect one.&nbsp;&nbsp;Only organization that have grown large enough that the long-tail problems are causing them noticeable impact should attempt to prioritize making Application Logic to be more robust, like Operational Logic, though Application Logic design can take many lessons from Operational Logic design for very cheap or equivalent cost.<br>
<br>
As an example, say there are a pair of relational databases in a Master/Slave configuration, and the Master node fails, because of the priorities for Application Logic, generally the application will just fail until the Master/Slave designators are updated to promote the Slave to Master (updated as moving a floating IP address or DNS name or IP record change, or from another directory-style service).<br>
<br>
There are some good reasons why Application Logic currently behaves this way.&nbsp;&nbsp;The first is that it takes extra Logic to determine what should happen if the primary database server goes away, and this will be (very short term, "several minutes, or under an hour") taken care of by the Operations team, through manual intervention or automation.&nbsp;&nbsp;This allows the Application developers to focus on revenue oriented features, while the Operations team deals with the relatively rare occasions when there is a fail-over event.&nbsp;&nbsp;This model becomes less desirable as businesses scale up, but is the normal model for smaller or newer businesses, even though it has obvious deficiencies.<br>
<br>
Some classes of databases have a multi-node approach from the beginning, to make these types of events less frequent, since a server can go down, but others will be up, and the Application can talk to any of them.&nbsp;&nbsp;These databases still have failure cases though, and so the results can end up being the same depending on the type of failure, in terms of non-Availability due to database failures.<br>
<br>
Part of the "extra Logic" is that Applications are meant to serve end-users, and the time put into making this extra resiliency is often prioritized to go into making additional or improved features.&nbsp;&nbsp;Whether you agree or disagree that this should be the priority, it often is the priority, and it serves us well to accept Reality, and work within it's confines.&nbsp;&nbsp;If we want to change this, we need to change the priorities by showing more value given with a different priority.&nbsp;&nbsp;This is difficult, but possible.&nbsp;&nbsp;Choose your battles based on when you can win, and when winning is worth it.<br>
<br>
Additional to the Logic required to handle failures, is that Application code needs to be very stable for-it's-own-purposes, and adding in this kind of Logic means that during failures more cases may be found that could be handled, which means more changes to the Logic surrounding database access, which means more change/churn, and this leads to more potential bugs.&nbsp;&nbsp;Specifically the kind of bugs that have data access requests failing, which is something no one wants.&nbsp;&nbsp;This doesn't mean that better Logic shouldn't be written for database access, but it does need to be written very well, and with an Operational understanding, especially around the matrix of failure cases.&nbsp;&nbsp;Using a slicing-the-pie methodology for handling errors is an important tool for not missing any of the potential failure cases.<br>
<br>
While I think with better education, and better base-libraries we can solve these problems and Application Logic can be more like Operational Logic in handling failures, or in fact leverage the same Logic, so that they are working hand-in-hand, I am making this point because this is not currently standard, and has never been historically standard anywhere that I am aware of.<br>
<br>
Another thing that Operational Logic needs to do, is to simply have more information about the operational environment.&nbsp;&nbsp;Seems like common sense, but since we are building from the foundations, it is necessary to state the details.&nbsp;&nbsp;Without meta information about the environment, Operational Logic will not be able to make the same kind of decisions that a Human performing Manual changes would have access to.<br>
<br>
As we get into what it takes to construct Operational Logic the brief description I have given here will be born out by many more details and along many more axes, which will give better insight into&nbsp;&nbsp;how these things are different, but for now it is sufficient that we can see that Application and Operational Logic are indeed different things.<br>
<h3 id=1e13f344d1ae44173a1f9532c809f6b1><a href="#1e13f344d1ae44173a1f9532c809f6b1">3.2.1</a>: Many applications and services.&nbsp;&nbsp;One Operational environment</h3>
<br>
Another difference between Operational Logic and Application Logic has to do with the nature of their environments.<br>
<br>
In a given organization there is generally only one "Production Environment".&nbsp;&nbsp;It may span many data centers, and there may be regional data center teams to support the physical side of the operations environment, but it generally by classified and worked on as a single environment.<br>
<br>
There are organizations who break these up, but they are frequently either regulated businesses, or ancient, or have some other external reason for running segmented Production Environments.&nbsp;&nbsp;In general, companies, even very large ones with the largest Production server collections, only have one Production Environment (which may contain many services and security zones).<br>
<br>
This means that in an entire Product Environment is being managed in a single manner:<br>
<br>
- There is one way to update Production DNS.<br>
- There is one way to provision new servers.<br>
- There is one way to fail over from a faulty server to a working server, for a given service.<br>
- There is one way to handle authentication and authorization for user and role account access.<br>
- There is one way to centralize log collection.<br>
- There is one way to monitor and alert on logs.<br>
- There may be one way to software releases.&nbsp;&nbsp;(Actually, this could be on a product by product basis)<br>
<br>
<br>
Each of these "one way" methods may contain many sub-methods, such as you may actually have several monitoring packages, but collectively they make up the "one way", and generally things are put into one of them, versus any others, unless multiple coverage is desired.<br>
<br>
By this "one way" concept, I don't mean to be naive and really limit it to "one thing", that is why there is "one way to" and not "one thing that does".&nbsp;&nbsp;However many methods of doing something (as legacy implementations will stick around for a long time, and sometimes there is intra-team competition for creating solutions) may combine into "the way we do things", and is meant to keep growing (although it might in practice).<br>
<br>
The thing about "one way to do it" systems that are different than "lots of different environments, that do it their own way", which is the comparison I'm trying to make, is that in a one-way-to-do-it system is that you don't want to introduce competing services.<br>
<br>
It is more efficient to configure, manage and have life-cycle support if we have limited the amount of ways we do things.&nbsp;&nbsp;This is a goal for us, in a Production Environment, but we may be forced to fracture things due to time or other resource or environmental restrictions (laws, business goals, technical limitations, etc).<br>
<br>
In terms of creating Application Logic, it is easy to separate components of the Application or separate applications that may work in tandem or sequence, or may be linked through a common Data Source, through a messaging queue, RPC (Remote Procedure Call), or other data transference mechanism.<br>
<br>
There are many ways to do it, but the point is that you can split up personnel, or Logic, to work on different things, and their work can be isolated from each other, only connecting at certain points to do data exchanges. <br>
<br>
This could be generalized to always be true, but again, the point Im making is the difference between one thing and another, not in their similarities. <br>
<br>
The Operational equivalent needs to be more tightly integrated, because it is trying to support a one-way-to-do-it system, and where things are not one-way, it would often be better if they were.&nbsp;&nbsp;<br>
<br>
So it is a Goal of an Operational system to have one-way-to-do-it, for efficiency, and it is a Goal of an Application system to have many ways to do many specific tasks, so that personnel can be split up into separate teams and given specific goals for those teams.&nbsp;&nbsp;<br>
<br>
This may seem wrong to you if you are coming from the Application side of things as "re-use" and "modularity" and all the tenets of Software Development seem to contradict what I am saying, but I am referring to the scale and degrees of this, and am saying that in Operational Logic, these must be significantly more extreme than in Application Logic.&nbsp;&nbsp;This is because Operational Logic supports the infrastructure in which Application Logic runs, so Operational Logic must be "more basic", "more fundamental", "more fault-tolerant", "more infrastructure-aware", than it's Application Logic sibling.<br>
<br>
The Operational team, in contrast to the Non-Operational software development department, has more generalized goals, that take into account the entire Production Environment, and are more concerned about:<br>
<br>
- Total availability of all services in the Production Environment<br>
- Manageability and life-cycle maintenance efficiency<br>
- Performance of the entire system, with a priority on bottle-necks<br>
- Not introducing problems into the environment, and prioritizing solving ones that currently exist<br>
<br>
Again, we could align these in terms of how they are similar, and we will find that they are mostly similar, but there is a difference between Operational Logic and Application Logic, and in this circumstance we want to understand the differences more than the similarities, as we are dividing the two subjects for inspection.<br>
<br>
I will not spend much more time on Application Logic, as there is much writing about that in non-Operational literature that covers the current understanding of how to do that, and that is not the focus for Operational Engineers.<br>
<p id=ae00bdb9200029912abd5c942058cf26><b><a href="#ae00bdb9200029912abd5c942058cf26">3.2.1.1</a>: Making more dependencies.</b></p>
<br>
Now that I've established there are two different things, with different qualities, Operational Logic and Application Logic, let's get into what goals Operational Logic should have:<br>
<br>
- Operation Logic should try to minimize external dependencies, especially networked dependencies.<br>
<br>
If we know things are going to fail, and we are writing Logic to handle them in cases where they have failed, then we know the infrastructure we are writing against, to manage, will also fail.<br>
<br>
Knowing this, we can optimize for the case that we want our Operational Logic to continue to function properly even in the case of a network partition or failure.<br>
<br>
If I have locally cached data to the server my Operational Logic is running on, I can access that data consistently, even if the network fails and the server running my Logic cannot reach other networked services or nodes.<br>
<br>
This allows me to handle failure cases more gracefully.&nbsp;&nbsp;For instance, maybe all the nodes are not unavailable, and if I have the data that lists all the nodes and their properties on my server already, I can verify which are reachable, and which are not without an internal processing failure occurring (cannot access data to check with, because it has been partitioned in the network failure).<br>
<br>
- Operational Logic should try to minimize the amount of frameworks, libraries and services it uses.<br>
<br>
Frameworks and libraries are useful, they server a purpose, however the more things you have, the more things that can fail and cause your Logic to no longer function.<br>
<br>
Additionally each of these things needs expertise to manage and troubleshoot, and your Operational Logic needs to be as straight-forward and simple as it can be, so that when problems occur, they can be troubleshot and resolved quickly.<br>
<br>
Operations teams are also generally (at most organizations) much smaller than their Application Engineering departments, so this must also be done with less people involved in the work, and with shorter time frames.<br>
<br>
Since the Operations team also has to take new services into account, and new hardware platforms, and may be given very short notice to get these working, the Operational Logic needs to be written to be able to be adapted to these situations extremely rapidly, and without causing problems for the existing infrastructure.<br>
<br>
After all, in a one-way-to-do-it system, if you break something with a change, you have might have broken everything with the change.<br>
<br>
This "force multiplier" or leverage gained from automation is a double-edged sword, in that it cuts your problems efficiently but if used incorrectly will cut you as well, by automating failures into happening in a wider area and faster than Humans can manually do.<br>
<br>
In the past, these problems could be avoided when automation was implemented incorrectly by simply removing the automation and having everyone do everything by hands again.&nbsp;&nbsp;I have seen this happen many times, when automation was immature, or was not given proper resources (mostly time) to be implemented correctly.<br>
<br>
As the scale of operations continues to grow, this will simply not be possible or efficient in terms of money and personnel to scale enough people to do things manually, and the number of mistakes created by manual work will mean that even getting through the dangerous stages of automation will be a better trade-off.<br>
<br>
We aren't quite there yet as of 2015, but it is coming.&nbsp;&nbsp;Some organizations have a good amount of automation, and we will create a spectrum soon to do some analysis on this, but they are not yet comprehensively automated, and are approaching it through Aggregation, instead of Slicing The Pie.<br>
<br>
This change in viewpoint is what is required to deal with automation comprehensively, and it starts with understanding how to optimize the Operational Logic to yield the effects required to allow this to happen.<br>
<br>
- When things do break, how does your Logic function?<br>
<br>
Minimizing dependencies, locally caching data are two strategies in making resilient Logic, but the real goal is that the Logic continues to function exactly as you designed it.<br>
<br>
By using Slicing The Pie methods of black boxing work that needs to be done, one can create a system that anticipates failures, and continues to function properly with the resources that are still available to it.<br>
<br>
This will the be automation we are going to inspect and start modeling soon.<br>
<p id=8eb74e570e995c459a430857793ad69f><b><a href="#8eb74e570e995c459a430857793ad69f">3.2.1.2</a>: Like 1 big computer.</b></p>
<br>
One reason why the difference between Operational Logic and Application Logic matters if that it provides an insight into another way of looking at the Production Environment.<br>
<br>
By seeing it as a "one-way-to-do-it" system, where we mostly want things done one-way, we can actually look at the entire collective of Production Operations as a single entity.<br>
<br>
We can abstract it so that it is "one big computer", with many nodes, which can be configured as if it one a single computer, with containers in it, or rather different directory mount points.<br>
<br>
Each node in this "one big computer" has it's own internal process schedulers (as Operating Systems start processes through a scheduler, that manages interrupts and putting processes back onto CPUs when their system calls finish), and it has it's own internal RAM and storage, etc.<br>
<br>
But, the entire set of machines, no matter how distributed they are across the planet, or how many nodes they are, can be controlled in terms of configuration and operational management, as if they were one system with many parts.<br>
<br>
I think of this as a layer of Operating System above the traditional bare-metal and virtual-machine installed Operating Systems, whose goals are to abstract physical hardware (BIOS, Buses, Devices), and manage device drivers, and schedule processes on their CPU, and manage libraries and file systems and virtual memory and such.<br>
<br>
So, I'll introduce this acronym as "DOS", Distributed Operating System.&nbsp;&nbsp;It is similar to a "cluster", but clusters are generally more uniform, trying to have the same type of pieces controlled by the same processes, in this they are homogeneous.<br>
<br>
Distributed Operating Systems (DOSes), would be heterogeneous, with any number of different hardware specification, different Operating Systems, and different services, and can contain any type of storage, in any configuration.<br>
<br>
Just like a single system, where you can run any kind of software (for that platform), or configure the directory structure in any way you want, there is no standard order for a DOS, it is merely an abstraction of working with a number of systems as if they were one system.<br>
<br>
There are unfortunately some acronym name conflicts with DOS, such as the legacy "MS-DOS", but this can simply be specified as "MS-DOS" or "PC-DOS" for the rare instances that someone needs to refer to this.<br>
<br>
There is also another acronym for "DoS", which is Denial of Service, and usually takes place in reality as a "DDoS", Distributed Denial of Service.&nbsp;&nbsp;The convention is to keep the "o" lower case, which makes this less confusing.<br>
<br>
Since we need to move forward in our industry, and distributed systems are here to stay, and we need to advance our methods of thinking about how to manage those distributed systems, I think we can safely take the acronym "DOS" for our purposes.<br>
<br>
One big computer, many nodes, heterogeneous Operating Systems, and services.&nbsp;&nbsp;All able to be managed as a single system.<br>
<br>
It's a big deal, and I predict whether this terminology is adopted or not, that in the future we will end up seeing Production Environments in this way, because of the efficiencies that this will lead to.<br>
<br>
In any case, I'm going to detail how to build this sort of thing in this book, so you have a path to getting access to this technology in your hands already.<br>
<h2 id=92dfc6ded926f3d44bd483b43e658db3><a href="#92dfc6ded926f3d44bd483b43e658db3">3.3</a>: Axiomatic Engineering</h2>
<br>
We've been building up to this for a while, introducing different spectrums or axes for different Attributes of this or that, but do they fit into a system?&nbsp;&nbsp;They do!&nbsp;&nbsp;And I call this "Axiomatic Engineering", which is like working with mathematical Axioms, to create engineering solutions.<br>
<br>
In this way we can detail all of the Attributes that we would like, and specify the spectrums (or axes) of those attributes, and then assign values to each attribute axes that we would like.<br>
<br>
Do we want more Consistency or less Consistency?&nbsp;&nbsp;Do we want more Availability or less Availability?<br>
<br>
Between Consistency and Availability, which is higher priority?&nbsp;&nbsp;What sorts of trade-offs need to be made if we were to rate Consistency higher than Availability?&nbsp;&nbsp;What about Available over Consistency?<br>
<br>
We can't possible implement the same solution while matching our different axes values, and priorities, because we care about different things in each circumstance, and so we will create a different solution.<br>
<br>
This is important in your own work, and critical for working in a team.&nbsp;&nbsp;If you can't agree on your values, how will your work have the Alignment necessary to produce the effects you want with efficient use of your resources?<br>
<br>
Let's re-iterate my generic definition for Engineering again:<br>
<br>
 "The efficient use of resources applied in an environment, to yield a desired effect."<br>
<br>
So we have:<br>
<br>
- An Environment (Production)<br>
- Resources (time, people, hardware, money)<br>
- Effects (Availability, Consistency, Resiliency, Atomicity, etc)<br>
<br>
These are the fundamental elements of Production Operations Engineering, and how we mix and match them together, and the methods of their implementation, will determine the effects that we get.<br>
<br>
If we are being Pragmatic, and we are only concerned with the effects, then we can start to build an "Effect Estimating Machine", and this is done through Axioms, created by populating our Axes with values and prioritizing which of those values are more important to us than others.&nbsp;&nbsp;After and during the implementation of the solution, we can use an "Effect Evaluation Machine" to determine how our implementation is matching up with our Prioritized Attribute Axes values.&nbsp;&nbsp;These would be a type of mental Virtual "machines", which could be considered mental software, or well-structured, consistent, internal algorithms for thinking, and used externally for communication.<br>
<br>
Let's make an overview for all of services in the Production Environment:<br>
<br>
- Available.&nbsp;&nbsp;Our services must be available.<br>
<br>
- Performant.&nbsp;&nbsp;Our services must be fast enough for our purposes (poor performance under heavy load means that some percentage of our end-users will not have Availability).<br>
<br>
- Manageable.&nbsp;&nbsp;We need to be able to control our environment, deploy software, upgrade security flaws, making configuration changes, add or replace server nodes, control user access, etc.<br>
<br>
- Visible.&nbsp;&nbsp;We need insight into our system through monitoring, alerts, logs, etc.&nbsp;&nbsp;We can't manage things if we don't know what is going on.<br>
<br>
That's a pretty good start, so let's take this as our basis.<br>
<br>
I have also ordered them in a general order of priority, because:<br>
<br>
- If the services are not Available, what is the point of it existing?<br>
<br>
- If the services are not Performant, then they are not available to some end-users, or are not timely.<br>
<br>
- If they are not Manageable, then we cannot control them to keep them Available and Performant.<br>
<br>
- If they are not Visible, we cannot efficiently Manage them.<br>
<br>
We could add other elements in here, or split these up, and some circumstances might order them differently, but this is a good starting place for our purposes.<br>
<br>
So, let's check our Attribute Axes for these prioritized goals:<br>
<br>
- Available:&nbsp;&nbsp; Not Available <---> Completely Availability<br>
- Performant:&nbsp;&nbsp;Slow <---> Fast<br>
- Manageable:&nbsp;&nbsp;Difficult, Risky and Slow <---> Easy, Safe and Fast<br>
- Visible:&nbsp;&nbsp;Opaque or Fuzzy <---> Clear and Precise<br>
<br>
For Manageable, I ended up creating three different sub-attributed, as saying "Unmanageable" really doesn't mean much, so we can re-write it as:<br>
<br>
- Available:&nbsp;&nbsp; Not Available <---> Completely Availability<br>
- Performant:&nbsp;&nbsp;Slow <---> Fast<br>
- Manageable: Risk: Dangerous <---> Safe<br>
- Manageable: Difficulty: Difficult <---> Easy<br>
- Manageable: Speed: Slow <---> Fast<br>
- Visible:&nbsp;&nbsp;Opaque or Fuzzy <---> Clear and Precise<br>
<br>
I have split these up now into individual attribute axes for Manageable, and also re-ordered them slightly for better prioritization, as we are more concerned with Risk than Difficulty.<br>
<br>
Difficult things need more leeway in performing them, so I am putting this higher than Speed, because if you are doing something difficult, but do it quickly, it seems that might lead to more mistakes, which increases Risk.&nbsp;&nbsp;Perhaps the "Safeness" of the higher priority will protect us from these mistakes, but unless that is guaranteed, than Difficulty should be a higher priority issue than Speed.<br>
<br>
Is Visibility really less important than all of those Manageability attributes?&nbsp;&nbsp;Maybe not, let's do one more re-ordering:<br>
<br>
- Available:&nbsp;&nbsp; Not Available <---> Completely Availability<br>
- Performant:&nbsp;&nbsp;Slow <---> Fast<br>
- Manageable: Risk: Dangerous <---> Safe<br>
- Visible:&nbsp;&nbsp;Opaque or Fuzzy <---> Clear and Precise<br>
- Manageable: Difficulty: Difficult <---> Easy<br>
- Manageable: Speed: Slow <---> Fast<br>
<br>
That looks a little better to me.&nbsp;&nbsp;We need that Visibility, because it speaks to knowing what is going on.&nbsp;&nbsp;I would rather than that then easier to faster management, as I need it to ensure my work is correct, or help with troubleshooting if an error is introduced.<br>
<br>
Now, we have some Attribute Axes, does that mean we have Axioms?&nbsp;&nbsp;Not quite, but we are getting close.<br>
<h3 id=66087a8256206e268b334c49bc0ba5ef><a href="#66087a8256206e268b334c49bc0ba5ef">3.3.1</a>: 90-9-.9-.09% Rules for Priorities</h3>
<br>
Let's take a brief tangent to talk about prioritization.&nbsp;&nbsp;We made a couple prioritized lists earlier, and they were listed sequentially, but not numbered or evaluated in terms of "how much more important" each element was.<br>
<br>
There are many ways to rank priorities, and I have come up with a methodology that I like which I call the: "90-9-0.9% rule", and can be said as the "Ninety-nine-point-Oh-nine rule" to make that actually pronounceable.<br>
<br>
The progression continues on forever, with the previous item being ten times (10x) more important than it's following item.<br>
<br>
This allows for clarity in which thing is more important, and also for knowing when things are just not important any more.&nbsp;&nbsp;It is purposefully exaggerated because without that clear separation, it is unclear why one action would be preferred over another action, because of "extenuating circumstances" may exaggerate a lower prioritized item over a higher prioritized item.<br>
<br>
It is my contention, that you should never do this.&nbsp;&nbsp;If you are going to change prioritization, you should explicitly change it from the order of ["A, B, C"] to ["B, A, C"] for a given circumstance.&nbsp;&nbsp;"ABC" may normally be what you want, and in some circumstance "BAC" may be better, and so you should explicitly state that.<br>
<br>
But, while evaluating the priorities of "ABC", then "A" should always be preferred over "B", or you should change your assessment of the priorities and state what the extenuating circumstances are for the priority change.&nbsp;&nbsp;This is for clarity of communication, both with yourself at a later date ("Why did I do that?") and for people besides yourself who should share a common understanding with you.<br>
<br>
By making the differences 10x apart, it clarifies things much more than if they were less.&nbsp;&nbsp;2x may still sufficient, but let us first demonstrate that merely being "too close together" in priority separation causes confusion, and from that we can see that "further apart is less confusion", and have our answer for why this is a valid technique.<br>
<br>
Say we have priority of Availability and Performance, and we assign Availability a value of "100" and we assign Performance a value of "90", so that Availability is the most important thing (an "A" grade of importance"), and Performance is the second most, but still highly important (a "B" grade of importance).<br>
<br>
So, Availability is first, but Performance is still quite close behind at 10%.<br>
<br>
Say there is a decision to be made, and it has to due with a hardware configuration, say cabling, that will give an Availability vs. Performance tradeoff.<br>
<br>
Let's say that we can cable up some storage which will be five times (5x) faster in Specification B, but it has as flaw in that sometimes it fails, but very rarely and might be able to be avoided with some maintenance actions.<br>
<br>
But, there is another cabling strategy which will ensure Availability, Specification A, even under intense failure scenarios, but is one fifth (1/5th) the speed (Performance) of Specification B.<br>
<br>
If we have a 10% difference in importance (100 vs 90) in Availability (Spec A) and Performance (Spec B), but we are getting a 5x boost of Performance if we choose Spec B, we have a decision to make, and some data to make it with.<br>
<br>
If we were going to seriously evaluate this, for a presentation on "What should we do?" to our department, we could make up some "point system" and do the arithmetic and decide which had more points.&nbsp;&nbsp;On a scale of 100 vs 90, it is possible that the 5X performance could win the "point comparison" just because of the "5x" scaling value being used in some calculation.<br>
<br>
Being "10%" close to the top item, it may seem more fluid, in that "this time" we will still keep Availability over Consistency (not thinking or talking about it, or not publicly stating the change in priority through documentation, etc), but we will go with the Spec B 5x performance boost, over better Availability.<br>
<br>
Making this trade-off isn't wrong, the proposed down-time might be acceptable, if it doesn't also some with a Consistency trade-off of data corruption (because we haven't accounted for that, you might find that acceptable as well as a trade-off) or another important Attribute which needs to be accounted for.&nbsp;&nbsp;(Aside: Data Corruption would actually impact Availability directly, since if the data is corrupt, it isn't Available in a useful form.&nbsp;&nbsp;Consistency in terms of recovering may still take time, and also count against Availability.)<br>
<br>
However, when making the scales of the system ten times (10x) different, then the spread is much wider, and thus more clear.&nbsp;&nbsp;Availability is worth "90", and Performance is worth "9".<br>
<br>
Even if we took a very naive algorithm of "5x performance is 5x the value", we get "90" vs. "45", and Availability is still on top.<br>
<br>
If we change the value to "10x performance", then we get "90" vs. "90" and while the positions match, we still know Availability is #1, and so it is clear that Availability is still our top priority in this case.<br>
<br>
If we change the value to "100x performance", we would get "90" versus "900" and it is clear this Performance has true value.<br>
<br>
What it means in reality is that we have a new Caching Layer.&nbsp;&nbsp;With 100x performance (or even considerably less), it is worth it to try to leverage that storage in a different capacity then we are currently considering.&nbsp;&nbsp;The "balance of scales" is heavily in favor of using "Specification B", because it's performance simply cannot be denied, but we probably still need to use "Specification A" as well, for reliable storage that is better for Availability when the "Spec B" solution fails.&nbsp;&nbsp;This decision will probably come down to whether the money is available, and the cost-benefit analysis determines it is required and worth it, for implementation both solutions as a 2-tier caching and persistence layer.<br>
<br>
"Specification B" could be used for very fast read-only queries, or it could be used as transient storage for incoming queries, so that there is a "pretty reliable, with known long-term faults" solution in place for taking incoming data as quickly as we can.<br>
<br>
These types of analysis are what using multiple-axes of values (Attribute Axes), and combining them into an easy-to-communicate-and-visualize method allow.&nbsp;&nbsp;We can change the values around, put them into forms or a spread sheet and apply algorithms to compare them quantitatively, etc.<br>
<br>
So, I have establish that using 10x scale differences has value, so let's put it to use:<br>
<br>
- Available:&nbsp;&nbsp; 90%<br>
- Performant:&nbsp;&nbsp;9%<br>
- Manageable: Risk: 0.9%<br>
- Visible:&nbsp;&nbsp;Opaque or Fuzzy 0.09%<br>
- Manageable: Difficulty: 0.009%<br>
- Manageable: Speed: 0.0009%<br>
<br>
Now the sequentially prioritized list we created before becomes numerically weighted.&nbsp;&nbsp;We can calculate against each attribute based on the value we have assigned it, to determine which actions we should take next.<br>
<br>
But, one might ask, isn't setting things at 0.0009% and lower making them trivial and not important to work on?<br>
<br>
That depends on whether there is more important work to be done, which is the beauty of this system.<br>
<br>
For instance:<br>
<br>
- If there is no work to do at the 90% layer, because the system is currently up (Available)<br>
<br>
- And, there is no work to do at the 9% layer, because the system is currently running fast enough (Performant)<br>
<br>
- And, we are not currently evaluating making a change that introduce Risk into our Production environment (Manageable: Risk, at the 0.9% layer)<br>
<br>
- And, we currently have sufficient monitoring and visibility into our system (Visible, at the 0.09% layer)<br>
<br>
- And, we have a problem with how Difficult some tasks are to perform (the 0.009% layer), then this is currently the top priority, and this work should occur.<br>
<br>
Should we also schedule work to fix "Manageable: Speed" problems (at the 0.0009% layer)?&nbsp;&nbsp;Not unless we have another person to assign it to, as the 0.009% layer is 10x more important.&nbsp;&nbsp;<br>
<br>
Once the 0.009% work is complete, the 0.0009% work will become the most important work.&nbsp;&nbsp;If you should ever have a problem with Availability (90%), it immediately becomes the top priority, as it is one hundred-thousand times (100,000x) more important.&nbsp;&nbsp;That is clearly more important, and the scale differences again make things very clear.<br>
<br>
I think this is a system that provides a lot of clarity for what is important right now, and how we should design things, and how to separate what should be done from what should not be done.&nbsp;&nbsp;It's simple enough to document in a page or so of Prioritized Attribute Axes, and that makes it easy to version control, or put into a Data Source, so we can also run Logic against it.<br>
<br>
In a one-way-to-do-it system, you do not want to do all-the-things, you preferably want to do one-thing for any given category of thing, so that you can gain efficiencies from that correctly chosen thing, for your set of priorities, goals and engineering values.<br>
<br>
Although I believe being able to maintain a regular scaling interval (10x) between priority levels is good, and the "90-9-0.9%" format makes doing this clear, it is not easy to communicate about these levels using the exact percentage values because saying "0.0009%" is difficult, and it is easy to confuse between "0.009%" and "0.00009%".<br>
<br>
Instead we can simply order the layers as "Top Priority", "Second Priority" and so on, or some other labeling structure which is easier to say.&nbsp;&nbsp;("Alpha Level, engage!", or whatever works for you.)<br>
<br>
Then you can say "This is 5th level priority, but we don't have anything to do in levels 1 to 4, so it is currently the top priority", which is clear, numerical, and does not use potentially confusing real numbers for normal communication purposes.<br>
<br>
The labelled tier structures can be replaced with their numerical equivalents to perform quantitative analysis whenever it is needed.<br>
<br>
The take-away for this section is not "this is a good technique, use it", although I am currently using it, and I do recommend it, but the larger lesson here is that you can make up these types of devices yourself, and you should.<br>
<br>
Come up with your own numbering schemes, labeling schemes, and determine the exact meaning for each of them, and reasoning behind why they are a valid method of working, and then suggest other people use them yourself.<br>
<br>
This is the type of Engineering discussions I would like to see more of, and the type of Engineering thought that I believe the Operational Engineering world could benefit from.<br>
<br>
We get clear sets of data, that are quantifiable, and qualifiable, and we can test ideas against them, and communicate clearly about what our priorities are, down to which axes of information, and we can change the attribute axes values or priorities and talk about how those changes would affect our designs, and evaluate how well our implementations did against those values during and after implementation.<br>
<p id=e4f58bc454dce4b3362881399d9ca4fd><b><a href="#e4f58bc454dce4b3362881399d9ca4fd">3.3.1.1</a>: Assigning different people different priorities is what makes up different roles.&nbsp;&nbsp;This allows different points of view, to make the organization stronger and more thoughtful, by design.</b></p>
<br>
Now, we have created a system for being able to prioritize our Attribute Axes that we are using to evaluate our goals.<br>
<br>
How do we use these, is it one-size-fits all?&nbsp;&nbsp;Well, that doesn't sound like our working definition of Engineering, so that can't be the right answer.<br>
<br>
Now, for "How do we prioritize work in Production?", this starts to become more specific, and we can generally use this as a set of priorities.<br>
<br>
However, different people do different things in an organization, and these priorities just don't make sense for everyone.<br>
<br>
Even in a Production Operations team, once it gets large enough, or if it has special needs, there may be people who do nothing related to the up-time or Availability of Production.<br>
<br>
These these people, they still need to understand and agree with, for the purpose of providing proper utility to their organization, the Production Priorities, but they will need their own priorities in doing their own work.<br>
<br>
In fact, everyone should always have their own priorities, and then they should match up their priorities against the environments that they are supporting or responsible for, or interacting with.<br>
<br>
For example, someone with a title similar to "Database Administrator" would be primarily focused on how whatever changes are being made relate to databases.&nbsp;&nbsp;They might be concerned at how the Development department might be making changes that could cause table scan differences.&nbsp;&nbsp;Or how a schema change might not be able to be rolled back in a reasonable time, or might take too long to apply the change.<br>
<br>
Their concerns will be prioritized around their responsibilities.<br>
<br>
Different people in a department will have different priorities, and it is through this that the department gains coverage across concerns. <br>
<br>
If everyone was only paying attention to exactly the same things, then there would be blind spots where no one was looking, and it would create a "monoculture" where only certain kinds of ideas would be suggested, and other types of ideas would be ignored or discarded, even though they may provide a valid solution that meets a different set of priorities.<br>
<br>
Having this internal opposition of priorities can cause friction, but this friction (if done in a healthy way) will lead to better discussions about the issues than if everyone had the same perspective, and so the discussion didn't take place at all, because there was no opposing point of view.<br>
<br>
This is the "Devil's Advocate" of Engineering, but shouldn't be used just to throw out opposing ideas, as that is also not Axiomatic Engineering, but should be applied to a set of Attribute Axes and Priorities with a different value set, that has a different perspective.<br>
<br>
This is always the case, but it not always explicitly the case, in fact it is rarely so in my experience.&nbsp;&nbsp;Explicitness could be seen as "pedantic" or "argumentative", when it does not need to be this at all, and should be encouraged in the time allowed for discussions.<br>
<br>
The organization and department should make an effort to provide timelines that allow some period of these discussions, at least for most important changes (things that are direction changes, direction-setters, or are risky are the most important).<br>
<h3 id=d2c6e14bfa28136f85c785a79fcfc39d><a href="#d2c6e14bfa28136f85c785a79fcfc39d">3.3.2</a>: Creating Axioms from Axes</h3>
<br>
This will be one of the few places in the book that I use an external definition to help us get more clarity.&nbsp;&nbsp;I used to always lead with dictionary definitions and quotes for things and I still am a fan of both these things, but if I am writing a book about how to think about things and evaluate them for yourself, it doesn't help to constantly source external material as an authority.<br>
<br>
So accordingly to the greatest authority that was easily accessible on my phone as I wrote this, there are generally two types of Axioms.&nbsp;&nbsp;Logical Axioms and Non-Logical Axioms.<br>
<br>
Logical Axioms are where you say something so simple and concise, that it couldn't possible by disagreed with.<br>
<br>
This might be something like:<br>
<br>
"If Availability of your Production Operations is your top priority, you need to have a validation step before making a change to determine if the change will cause down-time or Unavailability."<br>
<br>
This borders on a tautology, and that is OK, because it is being specific, and has utility.<br>
<br>
Is "Availability" our Top Priority for our Production Environment?&nbsp;&nbsp;If so, then we need to validate that a change to the Production Environment won't cause a problem with our Availability.&nbsp;&nbsp; BAM!&nbsp;&nbsp;Axiom!<br>
<br>
Not the most useful axiom, until one doesn't implicitly follow it, and causes an outage, and then a New Policy is created:&nbsp;&nbsp;Validate the change against the existing Production Environment, and determine the level of Risk, and then test it against a Staging Environment to ensure it works there, before implementing in Production.<br>
<br>
This is a Policy, that creates a Procedure, that stems from the explicit axiom, with a historical background of the outage event in question as it's inspiration.<br>
<br>
So, we have "simple statements no one should be able to disagree with" as one type of Axiom.&nbsp;&nbsp;It is important that these statements are very explicit and detailed, or the generality of the statement will make it not true in some circumstances.<br>
<br>
For instance, I lead that axiom with "If Availability of your Production Operations is your top priority", because this set's both a Priority and a fairly specific range in the spectrum or axis of Availability that it will be "Highly Available" or more towards Available on the scale of:<br>
<br>
Not Available&nbsp;&nbsp;<--->&nbsp;&nbsp;Available<br>
<br>
Now let's look at the Non-Logical Axiom, which is defined as something that can't be proved by simply thinking about the assertion as being true or not true, but fit's into set of rules such as the commutative property of Arithmetic:<br>
<br>
a + b == b + a<br>
<br>
Things are able to be moved around from being first to being second, with the same results.&nbsp;&nbsp;This only works, for some operations, not others.&nbsp;&nbsp; For instance:<br>
<br>
a / b == b / a<br>
<br>
This is generally not a true statement, so cannot be an axiom, because unless "a" and "b" are both 1, then the different sides of the equation will have different values.<br>
<br>
But, this is only for the general rules of Arithmetic.&nbsp;&nbsp;We could create our own usage of the symbols "/" and "==" and define them to mean something else, then this could mean anything we want.&nbsp;&nbsp;However, because these symbols have an established use, and would generally be read with that use, this might be a bad idea.&nbsp;&nbsp;It depends on if it would make things more clear or less clear.<br>
<br>
Regardless, the point is that Non-Logical Axioms fit into a system, and they should be seen, understood and used in the context of that system.<br>
<br>
We will be using both kinds of Axioms.<br>
<br>
What we have been leading up to is mostly being able to build Logical Axioms, by taking our specific Attribute Axes, and the values we have assigned them, we can create Axioms.<br>
<br>
By using the Prioritization of our Attribute Axes values, we can make other Logical Axioms (that deal with Priority).<br>
<br>
We can also make Non-Logical Axioms by coming up with a system for how to discuss and compare the different things we are working on.&nbsp;&nbsp;We can turn the Logical Axioms into variables, and create formulas out of them to determine what is a Logical course of action.<br>
<br>
We can also create Non-Logical Axioms once we start building these formulas, as we can decide how things can be treated inside the algorithm to express different ideas, and get different results.<br>
<br>
To go back to Philosophy, these elements are part of the Philosophy of Mathematics.&nbsp;&nbsp;These do not need to be strictly used in an academic or strictly used in standard methods of statical analysis, but can be used in any circumstance, given that we have put sufficient thought and detail so that they can be used discretely and deterministically.<br>
<p id=9daefd3b7edab6a712ab778906fedc9f><b><a href="#9daefd3b7edab6a712ab778906fedc9f">3.3.2.1</a>: Impersonal decision making through communicated values and priorities using Axioms</b></p>
<br>
One of the immediate benefits that we can apply to our everyday jobs is to use these Axioms, and their component Attribute Axes and Priorities to determine what actions we should take, and do so in a non-personal way.<br>
<br>
These days, when I make decisions, I don't do it because "I want to do X" or "I think X is a good idea", or "I had problems when I do Y, so I do X instead".<br>
<br>
I make decisions based on turning things into component pieces, evaluating them, and determining what action best aligns with all of the values (Alignment).<br>
<br>
One course of action better fits those values than another course of action, and that is the action I advocate, and I attempt to use the internal variables for doing that analysis in my explanation of why this is my current position.<br>
<br>
Change any variable, and the answer may change.<br>
<br>
As a thought experiment to visualize this, I like to imagine a scale, like the "Scales of Justice" or an old weight scale where you have 2 sides, and you put a known weight on one side, and the thing you are trying to weight on the other side.&nbsp;&nbsp;<br>
<br>
Since this is not a digital or a single-downward-vector scale (as we generally use these days), but a lever-based scale (I don't actually know the technical terms for these scales, so just making up what makes sense to me), it has two sides, and not just a single platform.<br>
<br>
So, we have this old-style scale.&nbsp;&nbsp;And on the weighing platforms on that scale, sit 2 more scales.<br>
<br>
Each one the same type of scale as each other (you can imagine them smaller than the first, so they fit), so that now there are 3 scales<br>
<br>
The first scale weighs the 2 scales that sit on it's 2 platforms.&nbsp;&nbsp;Initially these will all be exactly equal, so no tipping of the scales.<br>
<br>
On the 2 scales sitting on the primary scale, there are 2 more scales for each scale.&nbsp;&nbsp;So 1 base scale (Level 1), 2 scales on the base scale (Level 2), and 4 scales on the 2nd-tier scales (Level 3).<br>
<br>
And so on, forever.&nbsp;&nbsp;A recursive amount of scales placed on scales.<br>
<br>
The primary scale is our question:&nbsp;&nbsp;Do we do "A" or "B"?&nbsp;&nbsp;One side of the scale represents "A" and the other "B".<br>
<br>
Sub-dividing our question into Prioritized Attribute Axes, they map to the layers of the scales.&nbsp;&nbsp;<br>
<br>
We can also use this with our "90%-9%-0.9%" rule:&nbsp;&nbsp;Level 1 is our Top Priority (90%).&nbsp;&nbsp;Level 2 is next priority (9%).&nbsp;&nbsp;Level 3 is our next (0.9%), and so on.<br>
<br>
Having a "Recursive Tree of Scales" in which I map all my values to, means that any time a value changes, the entire tree will need to rebalance.<br>
<br>
If the "A" side was heavier, but something is removed and added to the "B" side, or something was merely made heavier on the "B" side, then the scale will tip.&nbsp;&nbsp;Maybe it won't go all the way over to being "Fully-Weighted-On-B", but it will be "Less-Weighted-On-A" than it was before.<br>
<br>
This imaginary set of scales is always working in my mind as I rate the various axes that my organization or goals are concerned with, and as changes are proposed, I re-scale my values, and the Recursive Scale rebalances itself.<br>
<br>
In this way, I am not really making any decision at all, personally, I am merely an agent of this system, mapping values as I understand them into a set of Prioritized Attribute Axes, which map to goals, which map to a result (effects) that we want, and when any variable changes, the results might change.<br>
<br>
This doesn't mean that I don't bring my experience into the picture, because I do, but my experience is mapped into this Attribute Axes and Priorities, and can be expressed in a deterministic and explicit manner.<br>
<br>
They can be written into a Data Source and evaluated by Logic, and they can be graphed, statistically analyzed and revision controlled for historical reference.<br>
<br>
This is how I make judgement calls in a "non-personal" way, and I assert that this is a valid way to proceed with making Engineering decisions.<br>
<h3 id=5c1f069a25780e9d9aff8574624089fc><a href="#5c1f069a25780e9d9aff8574624089fc">3.3.3</a>: Fashion Oriented Engineering</h3>
<br>
This section is a little tricky for me, because it's a thin line between just gathering information and using it, and "blindly following things" or simply acting out fashions.&nbsp;&nbsp;These are all highly subjective, and trying to write up the history of these "Fashion Eras" in technology mostly reads like it is a valid progression.&nbsp;&nbsp;The problem is to the extent any information is valid, for your context, not that the information contains potentially valid information.<br>
<br>
This is the problem with rationalization, and anything can be rationalized.&nbsp;&nbsp;However, Rationalization and Engineering are not the same thing.<br>
<br>
So I'll just that simply state that reading other organization's Public Relations releases on what they are doing and how they are doing it, is frequently information one cannot validate.<br>
<br>
Taking it as a data point and deciding whether a given methodology works for one's environment, with one's resources, is Engineering.<br>
<br>
Simply doing something because an Authority has said they do it, and worked well for them, is accepting their Appeal to Authority (a logical fallacy).&nbsp;&nbsp;They don't even need to appeal to anyone, people do the appealing themselves just from seeing the content and knowing that the organization has some social credit or prestige.<br>
<br>
I have been in far too many meetings where a problem was brought up, and then someone mentioned a blog post from some currently-fashionable-company, and then the consensus was to do what the blog post said, without properly evaluating whether it was a good fit for us, or a valid technique in our context.&nbsp;&nbsp;<br>
<br>
This is outsourcing one's infrastructure design and decisions to a party that does not know one's environment, one's resources, one's goals, and was probably not even intentionally telling anyone to follow their path.&nbsp;&nbsp;This is giving up "agency", or ability to make one's own decisions, based on one's own data and context.&nbsp;&nbsp;In fact, discussion against this course-of-action was sometimes seen challenging the legitimacy of the organization who made the press release.<br>
<br>
I refer to this as Fashion Oriented Engineering (FOE) or "Blogineering".<br>
<br>
Maybe these are good techniques, and if we evaluate them in the way we evaluate everything else as an Engineering decision, then it is not Fashion, it is Engineering.<br>
<br>
However, if one simply says "I read on Famous Company X's blog, they were doing Y.&nbsp;&nbsp;Let's do Y.", this is not Engineering.&nbsp;&nbsp;This is following a fashion trend setter.<br>
<br>
I have been at organizations that made very well received press releases (through their engineering blog) that completely mischaracterized what was going on in their environment (from my perspective), and it was well accepted by many others in the industry.<br>
<br>
Why?&nbsp;&nbsp;Because they have no idea that if they actually worked at that organization, they might completely disagree with the statements, because they have more information and could see the chain of events, and the effects of the recommended practice.&nbsp;&nbsp;There are many colloquial phrases such as "putting lipstick on a pig" that relate to dressing up something that you don't want to make it look like something you do want.<br>
<br>
{{ todo__get_a_couple_phrases_and_pick_a_different_one_could_be_seen_as_sexist }}<br>
<br>
No one is going to publicly announce that they are making a mess of their operations, but if their management tells them to make press releases (blog posts), then they are going to do that, and do it in a way that makes them look good.<br>
<br>
They have an incentive to "spin" things to a positive outcome, regardless of real Engineering going on, and the effects thereof.&nbsp;&nbsp;They may be doing excellent Engineering, I am also not saying that they are not because I don't have that contextual information, I am simply saying that we don't have direct experience with this information, and it should be treated as noise, that we can potentially extract signal from.<br>
<br>
So, Buyer Beware!&nbsp;&nbsp;Engineering blogs are "press releases", in fact all public communications are, and like any press release they are effectively "selling" something, such as how great a place they are to work, or how efficient and intelligent they are.<br>
<br>
There is nothing wrong with these press releases, they are a good thing, as they share information, and may be very useful.&nbsp;&nbsp;However, they should be taken as information in the sense of, "Organizating X made a press release where they said Y."<br>
<br>
This is true, and can be useful.&nbsp;&nbsp;Simply doing what one interprets from their release doesn't even mean that they communicated it properly, or their intent was understood properly, and it is a summarization, so it is only giving a limited insight into the reality behind the post, at best.<br>
<br>
Just something to keep in mind.&nbsp;&nbsp;Fashion and Engineering are not compatible in making decisions, and there is a unfortunately lot of Fashion going on, in my experience.<br>
<h2 id=4410772cb808c71ea7621428281fa35c><a href="#4410772cb808c71ea7621428281fa35c">3.4</a>: Evaluating changes.</h2>
<br>
Now that we have established how to set up Attribute Axes, Priorities and create Axioms we can start to look at how to make evaluate changes, before making them and afterwards.<br>
<br>
Let's start by creating an example problem, by setting up the environment for it, current state, and our goals (end state).<br>
<br>
Let's start with a simple website with some dynamic content, which we are deploying.<br>
<br>
Our goal is to improve our performance in doing the deployment.&nbsp;&nbsp;Currently, we are copying the installation files sequentially from a single server, and we have 100 web or application servers which we are copying them to (we will call them "web" servers for simplicity).<br>
<br>
The exact mechanisms for copying and deployment are not going to be the focus of this example, and so we won't be evaluating their performance or impacts, because it will complicate the example.&nbsp;&nbsp;In the real world, of course, these factors are also important, and would have be evaluated independently, and in conjuncture with the rest of the changes.&nbsp;&nbsp;<br>
<br>
It is important that all details are "Aligned" in that they work well together, and perform efficient as a whole (in their sequential and parallel processing), over long periods of time, and under our given resiliency goals.&nbsp;&nbsp;Alignment is complicated to explain, so I will keep giving examples of it over time, so that you can build up your own understanding of the concept, and how to apply the term as I am using it.<br>
<br>
So, we have a current state:<br>
<br>
- Single server, connects to 100 servers over SCP (secure copy) sequentially.<br>
<br>
What are some options that will perform better than running 100 sequential copies?<br>
<br>
One method is running the copies on the same single server, but running the copy commands in parallel instead of sequentially.<br>
<br>
There are a number of options for running things in parallel:<br>
<br>
- Forking the process, so that there are many processes of SCP running.&nbsp;&nbsp;Forked processes are independent of the process that forked them (they start as clones, and then do their custom thing), and do not have a lot of communication with the parent.&nbsp;&nbsp;There are ways to know some things about the program though, so this is a viable option.<br>
<br>
- Using a controller program to create Threads, and running the SCP process in the threads (similar to forking, in that there are still 100 (in this case) SCP processes being run, but they are being controlled by a single program, instead of just independently launching.<br>
<br>
Since I want to constrain this example, I won't get into the differences between controlling forked and threaded sub-processes, it's enough to know that while they have differences, we can get the results we want out of either of them for this case.<br>
<br>
{{ todo__describe_forked_vs_threaded_somewhere_else }}<br>
<br>
It doesn't matter whether we write our own code to do this forked or thread handling, or we use software someone else made, such as "Orchestration" software which might have agents that run on each target server, and perform the copy in it's own way.<br>
<br>
So we have specified 2 methods running on the same single source server, and performing the work in parallel.<br>
<br>
Since we have run into this performance problem by running things sequentially, one thing we will do is say, "Let's not get into this situation again, once our server targets have grown again", and say that we are removing the option of using sequential copies again, because it will not scale, and will create work for us again in the future.<br>
<br>
Since we just went over how create an Axiom, let's do it now.&nbsp;&nbsp;However, since we are working with a specific scenario and have not yet looked at all-of-operations together, we shouldn't make this a Universal Axiom, or a Production Axiom.<br>
<br>
Instead, let's make it a Working Axiom, or a Temporary Axiom, for the purpose of this problem.<br>
<br>
Here goes:<br>
<br>
"Once a job that was working sequentially on a single server hits a scaling problem, and needs to be changed for performance, all later implementations of that job will not be re-implemented sequentially, even on more than a single server."<br>
<br>
This is a little longer than I like for an Axiom, and it has more caveats than I prefer as well, as I like them simple and straight-forward, always able to be applied.<br>
<br>
In this circumstance, we are building a Working Axiom, so it is temporary, and it needs to be precise, so it needs those caveats to fit into our problem space.<br>
<br>
Let's review the verbiage quickly to see what caveats I baked in:<br>
<br>
- I have limited this to implementations that already exist, and were implemented as sequential processing, on a single instance.<br>
<br>
This could actually apply to a number of different scenarios, not just the one we are currently discussing, so this is good Axiom material, as we want to be able to apply Axioms generally, so that they are usable or actionable.<br>
<br>
- I specify that this axiom is only to be applied once the work hits a problem.&nbsp;&nbsp;Going around and "fixing" problems that aren't problems is a poor use of resources, as there are likely actual problems that need fixing.&nbsp;&nbsp;Also, it is creating change in the environment, which may lead to instability or outages.&nbsp;&nbsp;<br>
<br>
All changes come with risk, as you only know the effects of your previous system from your history with it, once you change it you are working with a new system (new state vs. old state), so you may get different effects.&nbsp;&nbsp;<br>
<br>
If your change is implemented ideally, then the effects that change are exactly what you planned and wanted, so everything is OK.&nbsp;&nbsp;If you get effects you did not want, or did not anticipate, you will likely be created a problem, which may need another change to fix.&nbsp;&nbsp;In cases where it causes an immediate outage or degradation, it will need to be reverted or "rolled-back", if this is possible.<br>
<br>
- Once a job gets to this "problem" state, we will not create another solution that operates sequentially, as we have proven that for this case of work (job), sequential processing doesn't scale for us.<br>
<br>
This doesn't meant that everything should be parallelized.&nbsp;&nbsp;Firstly, not everything can be run in parallel, as some operations are sequential operations.&nbsp;&nbsp;If you need to get data, and then format text with it, you can't format the text at the same time you are getting data (in parallel), because you don't have the data yet.&nbsp;&nbsp;This work requires being run sequentially.&nbsp;&nbsp;However, if you have to process 100 of these, you may be able to run each of the 100 jobs in parallel, and then internally process them sequentially.<br>
<br>
Writing things to work initially in sequence is a faster way to to develop, as the complexity of parallel process communication, locking and other issues can be ignored, and sequential processing is a default for many implementation languages (and all the primary Operational related languages, from any environment I've worked in).<br>
<br>
- Finally, I state that even splitting the job across multiple servers, which may allow the sequential processing to have acceptable performance again, is not acceptable, because we are just planning to have this problem again when those N servers have to do "100" servers each, and we are back in the same spot.&nbsp;&nbsp;This method of "throwing hardware at the problem" is frequently not the right move, although there are some special cases where it is the right move, which we will get into later.<br>
<br>
The act of taking the same method you use now, and making a change to it that allows it to continue working, but with the knowledge that it will stop working again once you have continued growing as you have previously, I sometimes call "burying land mines in your own yard".&nbsp;&nbsp;This is because you know this will create a problem for you in the future (problems, degradation, outages, etc), but you are doing it anyway.&nbsp;&nbsp;You have embedded a known problem in your system, and will certainly encounter it again (unless you are going to decline and shut down the organization).<br>
<br>
However, just because this is going to create a problem in the future, and is would be best to be avoided, there are circumstances this might be the "right thing to do".&nbsp;&nbsp;Such as if you are working in a "Startup" organization (very small, moving very fast, not afraid to break things), and the trade offs are worth it.&nbsp;&nbsp;<br>
<br>
Doing things or not doing things should always be evaluated for their Engineering trade-offs, with the business goals and requirements.&nbsp;&nbsp;Refusing to do something that is best for the organization, just because it will cause a problem in the future is also Not Engineering, even though it seems like it is "being a better Engineer", because it is not taking into account the actual environment, which is prioritizing moving fast over avoiding problems.&nbsp;&nbsp;This will create Technical Debt, but may be worth the trade-off, just like creating Financial Debt can.<br>
<br>
Ok, so now we have established that one method of solving this problem is to create parallel processing on the single server, and we have our Working Axiom:<br>
<br>
"Once a job that was working sequentially on a single server hits a scaling problem, and needs to be changed for performance, all later implementations of that job will not be re-implemented sequentially, even on more than a single server."<br>
<br>
We need at least one more method for this example to be complete, for our purposes (but not for a real world solution), and for that I will choose the method of the target servers all pulling down the deployment themselves.<br>
<br>
This creates a "push" (parallel SCP copies) vs. "pull" (target servers pull down data) scenario, so we are comparing data moving in two different direction.<br>
<br>
For this example, I will only provide 1 method of "pulling" the deployment data, which will be to use a Load Balancer and web servers behind the Load Balancer.<br>
<br>
For all Production services, we should generally always have at least 2 servers for redundancy, in case one of them fails the other is available.&nbsp;&nbsp;Note I say "generally always", which is a contradiction, but we will have to talk about this later.&nbsp;&nbsp;However, for this example, to keep things simple we will just create a single Load Balancer and N web servers behind the Load Balancer.&nbsp;&nbsp;For the example, we could say 1 web server, but since the purpose of Load Balancers is to distribute requests (load), we can say N.&nbsp;&nbsp;Getting into 2 or more Load Balancers has a couple other issues I would want to bring up, so I will avoid it for this example.<br>
<br>
So, to summarize, our "pull" alternative is:<br>
<br>
- A Load Balancer server that accepts HTTP requests (also simplifying by not adding in security, made clear by not using HTTPS).<br>
<br>
- N Web servers that can server the static content of our deployment data.<br>
<br>
- Some Logic for invoking the "pull request" from the target servers, to the Load Balancer.&nbsp;&nbsp;We will call this "Pull Logic".<br>
<br>
- Some Logic for signaling the target servers that they should invoke the "Pull Logic".&nbsp;&nbsp;We will this "Deploy Logic", since this invokes the deployment.<br>
<br>
<br>
The flow of this Pull system will be:<br>
<br>
- The new deployment data is put in place, in whatever way that is done, which is the same for any of our cases.<br>
<br>
- Deploy Logic is triggered, by a Human running a script or initiating from a webpage, etc.<br>
<br>
- The Deploy Logic triggers the Pull Logic to get the latest data.&nbsp;&nbsp;This could also be done several ways, but let's take the simplest one of an Agent Model, where the Deploy tells each of the web servers it's time to Pull their deployment data.<br>
<br>
- The Pull Logic makes an HTTP request to the Load Balancer, which proxies the request to the HTTP server, which responds with the Deployment Data.<br>
<br>
- The standard "local installation" Logic runs on the web server node, which would run in any of our cases.<br>
<br>
<br>
So, now we have established a more scalable Push and a Pull alternative to our sequential Push mechanism, how should we go about evaluating them?<br>
<br>
First, let's come up with all the Attribute Axes that we care about here, and then let's prioritize them for ranking purposes, and finally we can assign values to all of the Attribute Axes, and then look at what their Prioritization tells us about what our options are.<br>
<br>
One important concept to always be aware of when designing a solution is Centralization.&nbsp;&nbsp;Let's create that spectrum:<br>
<br>
Decentralized (0.0) <---> Centralized (1.0)<br>
<br>
On the Decentralized end of the spectrum, things are done on many nodes (machines, servers, etc), and on the Centralized end of the spectrum, things are done in a single place.<br>
<br>
The benefits of Centralization are control, and a single point to detect failures and perform control logic.<br>
<br>
The liabilities of Centralization, or the benefits of Decentralization, are that there are many nodes, so if a node fails, you only lost 1/N of the total processing capacity, this also can help with performance as many nodes can do more work than a single node.<br>
<br>
However, we actually have 2 sides to this Centralization question.<br>
<br>
Firstly, we are always Decentralized on our HTTP servers, because we have more than 1 of them, or N of them.&nbsp;&nbsp;So our Target is already Decentralized.<br>
<br>
The question is whether we will make our Source Decentralized (HTTP servers behind load balancers), or our Source Centralized.<br>
<br>
There is a slightly different perspective on this already going on with Sequential vs. Parallel execution on a single node.&nbsp;&nbsp;Parallel execution has a "Decentralized" factor over a sequential execution, which is the Centralization of an execution process.&nbsp;&nbsp;The differences between running many processes on the same server or running many processes on different servers have many similarities.<br>
<br>
Now that we have this Centralization spectrum, let's put our options on the table:<br>
<br>
- Push: Centralized execution of parallel processes.&nbsp;&nbsp;While there is an element of Decentralization to the Parallel processing vs. sequential, this operates under the black-box of this server, since it is on a single server, it is still a 1-instance system, and so is fully Centralized.&nbsp;&nbsp;Centralized = 1.0.<br>
<br>
- Pull: We initiate it on a single machine, that contacts 100 machines, those contact 1 machine (Load Balancer), which contacts N machines that serve static HTTP.&nbsp;&nbsp;This has a back-and-forth in terms of being Centralized as we move from 1-instance to N-instance, back to few-instances (1 Load Balancer), to N-instances (HTTP) again.&nbsp;&nbsp;However, when we black-box this, the important part is that the 100 machines (N-instances) are requesting their deployment data independently:&nbsp;&nbsp;this is Decentralized intallation, so Centralization is closer to 0.0, but probably not full 0.0, since there are many centralized steps, let's call it Centralized = 0.2.<br>
<br>
Even in creating a simple set of values for comparison on a single Attribute Axes, we found there are many sub-points that could confuse the topic, and be causes for disagreement.&nbsp;&nbsp;I'm able to settle these quickly in this text, because I don't have to have anyone else agree with my assessments, but as soon as you add in other people you quickly get disagreements based on terminology, experience and understanding of the current problem and previous solutions.<br>
<br>
This makes this kind of thing essentially an unsolvable problem in terms of communication, and underlines how important it is to try to communicate clearly, like with Prioritized Attribute Axes, as it allows for some resemblance of qualified and quantified discussion, instead of the usual method of making decisions in groups:&nbsp;&nbsp;who can talk the most, who can talk the loudest, who is better at arguing and the most important, who has the most social capital to spend on "winning" the current discussion.<br>
<br>
Since we are looking for Engineering clarity as opposed to "winning" through rhetoric, we must make our best efforts to perform this work clearly, even though as we get into the details of any topic it obviously becomes unclear and could be subjectively argued to mean the opposite thing.&nbsp;&nbsp;Your experience and discretion will determine what path you go down, so paying attention to the results (effects) of all your actions will need to be your guide in how to make these choices to get effects you desire, and avoid effects you do not.<br>
<br>
So we have a Centralized axis, and Push = 1.0, and Pull = 0.2.&nbsp;&nbsp;We have one Attribute Axis filled out.<br>
<br>
What's another spectrum we can measure here?&nbsp;&nbsp;Performance is important, since that is why we are doing this exercise.&nbsp;&nbsp;So let's rate them both:<br>
<br>
- Push: N parallel SCP processes start, and copy the tarball or otherwise single-file packaged deployment data to each node.&nbsp;&nbsp;Starting 100 SCP processes at once can delay things moving as the handshakes are occurring, but once things start up being in a single SCP process versus an HTTP process will only have the encryption as an added factor, which is fairly minimal on modern hardware and can be ignored unless it can be measured to be important.<br>
<br>
- Pull: 1 process initiates 100 processes, which make an HTTP request through a load balancer to our HTTP servers.&nbsp;&nbsp;We never did cover how the 1 process will initiate the 100 processes; if we use SSH to do it, we are literally doing the same thing that the 100 SCP processes of Push would do (since SCP uses SSH), except for the data delivery.<br>
<br>
All in all, I'm going to round these out to being equivalent, which means between them we can put both their Performance scales at 1.0, which means it is a non-factor.<br>
<br>
What about Scalability?&nbsp;&nbsp;This is another factor like Performance.&nbsp;&nbsp;We came to this problem because the Sequential Push was too slow.&nbsp;&nbsp;It was not too slow when we had less than 100 servers, but at 100 servers it is too slow, which makes this a Scalability issue.&nbsp;&nbsp;So let's rate our methods in terms of Scalability, after we make a spectrum:<br>
<br>
Can't Scale (0.0)&nbsp;&nbsp;<--->&nbsp;&nbsp;Can Scale (1.0)<br>
<br>
Notice I said "Can't Scale vs Can Scale", and not "Not Scalable vs Scalable".&nbsp;&nbsp;The reason for this is that we may still need to change our selected solution, as it is not the "Most Scalable" solution, but building the "Most Scalable" solution before you need it is not good Engineering, as it is overkill for what we need.&nbsp;&nbsp;We only need to handle our current and near-future problems, not our far-future problems.&nbsp;&nbsp;Implementing a solution for far-future problems may actually cause us problems in building, supporting and using it now that we are not nearly at that scale.<br>
<br>
Imagine a deployment system that can handle quickly doing deployments on 100,000 servers.&nbsp;&nbsp;Is this going to be as easy to use, create and maintain as one that can deploy on 300 servers?&nbsp;&nbsp;Probably not, as the mechanisms that will allow it to scale to 100,000 servers probably add in a lot of complexity and will make it difficult to use this system, and to make changes as the business goals change.<br>
<br>
So let's review our Push/Pull options on the "Can't Scale" vs "Can Scale" spectrum:<br>
<br>
- Push: Runs on a single machine with 100 processes.&nbsp;&nbsp;This only scales up to what this single machine can handle, so at some point we are going to need to move to more than 1 initiating server.&nbsp;&nbsp;So this is only scalable for so long, and then we will need more machines to perform this copy, and we will need a method to initiate all those machines to initiate their copies.<br>
<br>
- Pull: Has 2 limited server groups (initiating, load balancing) and 2 scalable server groups (target servers, HTTP static content servers).&nbsp;&nbsp;This has a much better scaling factor, in that our "limited server" groups are actually easy to expand.&nbsp;&nbsp;It is easy to add more Load Balancers, and easy to split up Initiators, as they do a small workload (triggering the deployment fetching Logic on the target nodes).&nbsp;&nbsp;Additionally, since the initiating Logic (Pull) does less work than the copying Logic (Push), we can run more target node initiations from a single Pull-instance server.<br>
<br>
So, with this I'm going to assign some values based on my internal experience and understanding of this space.&nbsp;&nbsp;It would take too much space to go into all the decision points I am making to assign these values.&nbsp;&nbsp;As an exercise, do your own analysis on this and come up with your own values, and compare them to mine.&nbsp;&nbsp;Why do you think we came up with different values?&nbsp;&nbsp;This will happen with every person you work with, if you both have different ideas for how to implement things, so it is a useful exercise.<br>
<br>
I will rate the Push option as having a Can Scale value of 0.5.&nbsp;&nbsp;It can scale, but will start to have problems as the target server count gets bigger.&nbsp;&nbsp;SCP is not as fast as HTTP, and is not set up to handle as many simultaneous connections.<br>
<br>
I will rate the Pull option as having a Can Scale value of 0.75.&nbsp;&nbsp;This is still not an amazingly scalable architecture, but it has the ability to scale better than the previous one, so I am leaving room for more-scalable solutions, but indicating that it is clearly superior to the Push option in this single Attribute Axis.<br>
<br>
Now, let's come up with another spectrum, which I will call Knowability (as we have used generically before), but will be more specific in this case:&nbsp;&nbsp;Do we know all target servers got the new code?&nbsp;&nbsp;Do we know they all installed the new code?&nbsp;&nbsp;Do we know they are all running the same code?&nbsp;&nbsp;This is what Knowability will mean for this case.<br>
<br>
<br>
...tbc....<br>
<h3 id=72e6204dcea6d95203e9c1a3e0b946d8><a href="#72e6204dcea6d95203e9c1a3e0b946d8">3.4.1</a>: Alignment</h3>
<br>
Alignment is one of the most important concepts of building efficient systems.<br>
<br>
Any system can be described in a number of ways, but let us consider a system that is described as nodes and links between them, or edges, so that can be describe a system as a Graph.<br>
<br>
Any point of interest in the system can be described as a node, and the connections between these points of interest are our links or edges.<br>
<br>
Let us first consider a physical building structure, like a house, but we will simplify it into a wooden ceiling (flat board of equal width and length, and a small height) and 4 posts of wood to put the ceiling on top of.&nbsp;&nbsp;You can consider the wooden posts to be "4x4 inch" beams or other material.<br>
<br>
Now, in this example the purpose of the beams is to lift the ceiling board into the air, and keep it there.&nbsp;&nbsp;So the beams function as support for the ceiling.&nbsp;&nbsp;This defines the terms needed to start inspecting the concept of Alignment.<br>
<br>
How can we begin to measure Alignment?&nbsp;&nbsp;Let's make up a scale.<br>
<br>
Alignment Efficiency<br>
<br>
Least Efficient <=====> Most Efficient<br>
<br>
Here is a basic scale of efficiency, going from least to most, which is pretty vague.<br>
<br>
Let's start throwing some more variables in and seeing how this immediately becomes more interesting as a concept that I am claiming is a core concept of Engineering.<br>
<br>
Let's assign different heights to the beams.&nbsp;&nbsp;Lets say the beams are:&nbsp;&nbsp;10 foot in height, 8 foot in height, 6 foot in height, 1 foot in height.<br>
<br>
How efficient are these heights of beams at keeping a ceiling raised above the ground?<br>
<br>
Firstly, when we think of a ceiling, we think of it generally as having an even height, or having some sort of stylistically (or functionally) changing height, but always we think of a ceiling as something we could be underneath.<br>
<br>
If one of our boards is only 1 foot in height, then for part of our ceiling, we know we will not be able to reside underneath it, as there is not much space.&nbsp;&nbsp;This does not sound like a very good ceiling.<br>
<br>
This means, that we can reduce the "efficiency" of the ceiling we are proposing, because the ceiling is qualitatively "not good" from our definitions (goals) of what a ceiling should be.<br>
<br>
Now, if qualitatively we wanted a flat ceiling above our heads, then this sloping ceiling is also "less good", and if we we're satisfied with a sloping ceiling, but require that it only slope in 1 dimension, then these heights of beams are also producing a qualitatively "less good" ceiling.<br>
<br>
That covers some qualitative issues, but what about quantitatively?<br>
<br>
There are several factors we can immediately state for quantitative measurements, such as:<br>
<br>
- Vertical Weight bearing:&nbsp;&nbsp;How much weight could be placed on the ceiling/roof, before the structure collapses?&nbsp;&nbsp;You can imagine snow, if you need a concrete example.&nbsp;&nbsp;As snow accumulates, the structure bears mode weight through the supporting beams, and is at risk of changing structure and eventually collapsing as this weight is delivered over time.&nbsp;&nbsp;Even unweighted by extra material, the material in the beams and ceiling board themselves have weight and will over time degrade, so this is always a factor.<br>
<br>
- Lateral force stability:&nbsp;&nbsp;How much horizontal or lateral force can be applied to this structure, before it collapses?&nbsp;&nbsp;Is it equal in all directions?&nbsp;&nbsp;How stable is it in terms of falling on one of it's sides?&nbsp;&nbsp;Etc.<br>
<br>
Let's start with just these two factors, though there are many many more than can be applied, even in this trivial example.<br>
<br>
In the case of the beams with 10, 8, 6, and 1 feet in height, if they are mounted vertically under the structure, which provides the maximum resistance to gravity (a vertical force), then only or 3 of these beams will ever touch the ground at any time, for any given combination of their placement.<br>
<br>
This is obviously an inefficient design for keeping up a ceiling.<br>
<br>
If the beams are connected to the ceiling at an angle, such as they allow for a "flat" ceiling (equal height from the ground in all parts), then the ceiling will only be 1 foot high, and the longer boards will be connected at very steep angles, which will provide less resistance to the gravity force pressing down on the ceiling and beams.<br>
<br>
This can be calculated as quantifiably less efficient than beams that are all the same height, such as all being 10 feet in height.<br>
<br>
In the same way as this physical example yields different qualitative and quantitative results with only the variance of heights of the boards, so every virtual difference yields different qualitative and quantitative results with every change.<br>
<br>
Some virtual differences may yield "essentially the same results", for your level of interest in those results, but the results will always be different with different values.<br>
<br>
This is why you must understand your own environment, requirements, resources and goals for yourself, in as deep and accurate manner as possible, so that you can understand what these small differences will yield.<br>
<br>
This is an example of "local alignment", because we were only looking at: 1 ceiling, 4 beams, 1 goal (ceiling is efficient), 1 force (gravity).<br>
<br>
No problem we ever deal with in life is this restricted.&nbsp;&nbsp;Even for our above example, we will have to deal with weather (wetness, heat), biological (mold, termites), and many other factors for a real world "just a ceiling" problem, which massively complicate what "building an efficient ceiling out of 1 board and 4 beams" looks like.<br>
<br>
In our modern Operational environments, we have hundreds of sub-goals, and thousands of instances of software, and millions of instances of data, even in small environments, all of which have different access patterns and reliability requirements.<br>
<br>
If you can extrapolate out the ability to understand Alignment for our "simple ceiling" problem, and can extrude from that the importance of understanding Alignment in our much more complex and complicated real world environments, then you will see why I am maintaining that Alignment is one of the cores of Engineering, and that it is one of the first questions we must always ask in any kind of design related inquiry.<br>
<br>
In future sections I will go into how Non-Local Alignment is one of the bigger problems we have to deal with in modern organizations today, because even good Local Alignment may yield poor Non-Local Alignment, as two or more sub-systems are working together in a larger integrated system, and while they may be locally efficient, they are not globally efficient.<br>
<br>
With this in mind, spend some time thinking now about environments you have worked in which had services whose poor Alignment lead to problems.&nbsp;&nbsp;This might mean that one inefficient service blocked more-efficient services from being created because of the overlap they would have, and that the existing service was seen as "Good Enough", even though it blocked progress and improvements due to inefficiently being Aligned to the future-good-state that you would like to create.<br>
<br>
In environments where I work, I see this constantly.&nbsp;&nbsp;Almost every existing project is created inefficiently, and causes us to be blocked from moving forward to more efficient services (in that area and others) due to the inefficient designs of the existing services.&nbsp;&nbsp;Can you see this inefficiency in your own environment?<br>
<br>
While we want to have Globally Efficient Alignment, if you find yourself in an environment where there is poor global efficiency, then you must start with a single project that has good Local Alignment efficiency, and attempt to branch out from there, creating either new Local efficiencies, or leveraging your now-existing good Local Alignment to create larger and larger inter-connected efficient systems, which can eventually replace the older less-aligned and less-efficient systems.<br>
<h3 id=26ab897a0841f617abc1175707de81dd><a href="#26ab897a0841f617abc1175707de81dd">3.4.2</a>: The Problem with the "Best"</h3>
<br>
Best is a concept that is poorly understood in our culture.&nbsp;&nbsp;It is frequently used, but rarely clarified, because it's vagueness gives it rhetorical power, but in engineering this is simply a logical fallacy that leads us to poor choices and low efficiency.<br>
<br>
In order to take a term like "best" and use it in a manner that allows us to make good choices and have high efficiency, we must understand what other properties "best" has, besides just being "the best".<br>
<br>
What are some properties of "best"?<br>
<br>
- There is only one of them.&nbsp;&nbsp;Only 1 thing can be "the best".<br>
<br>
- Something cannot be "the best" for a great number of circumstances, because as the circumstances (variables) change, then what is "best" will also change.<br>
<br>
- This creates an inverse ratio between the numbers of circumstances a methodology can be applied in, and the efficiency of the results for those circumstances.&nbsp;&nbsp;This can be extended by allowing for any given set of circumstances (variables) to be repeated over and over.&nbsp;&nbsp;The repetition will cause some of the variables to fluctuate (time itself being in constant fluctuation, others being contextual yet still being classified as being processed in the "same general manner").<br>
<br>
- The inverse ratio suggests that for any given circumstance, there is one-and-only-one "best" answer, and potentially a small set of "close-enough-in-quantitative-results" class of answers that competes with the local-maximum of the "best" answer.<br>
<br>
- Changing any of the requirements, resources or goals significantly will almost assuredly change which given solution is the "best" answer to the new problem.<br>
<br>
This set of properties took it's shape through a line-of-reasoning, instead of enumerating things that were visible without reasoning, but both methods of defining properties are acceptable (simply remember how you came to them, in case they need re-evaluation).<br>
<br>
In engineering we are not generally interested in the "worst" outcome as a result, except when we need to brainstorm in finding potential problems to pre-solve against in coming up with our failure matrix for our services/etc.<br>
<br>
Determining "worst" solutions is using the methodologies for "best" with reverse quantitative comparisons.<br>
<br>
In my view, this makes it clear that best/worst are a very small subset of options, and those options are highly detailed to one's exact environment, requirement, resources and goals.<br>
<br>
As such, there can be no such thing as "Best Practices" (see section {{ section__e5829271e6cfb5927f3a4d4aec1b10df }} for details), because these are generalized solutions, for generalized environments, generalized resources available, and generalized goals.<br>
<br>
"Best Practices" are useful to read as case-studies that someone is claiming a method worked well for them, and they can recommend it as a potentially useful method, but since this goes against our own understanding of what "best" really means, these should be reworded as "An Example Implementation", not a "Best Practice", as it is neither Best nor a Practice, since Practice connotes a deeper level of understanding that is provided than the very thin layer of a "recipe" and some case-study information.<br>
<br>
In this book, I try to define for you, roughly, my Practice, for how to do engineering and operations.&nbsp;&nbsp;I am trying to provide deep insight into how these things work, as I see them, and how I manipulate them to achieve results I desire, and how you can learn from my work and help with improving your own methods.<br>
<br>
Be careful with the language you use casually to describe things like "The Best Way To Do Something", in your giving or receiving of information, because the results you receive from taking those words at anywhere near their face-value may be far from the suggested-reality those words relayed to you.<br>
<br>
"Best" has a powerful symbolic meaning to us.&nbsp;&nbsp;Use it very carefully, or pay the consequences for wielding power poorly.<br>
<br>
A better way to think of things is using the term "better".<br>
<br>
Better is always a comparison between two distinct things.&nbsp;&nbsp;Best is often only discussing 1 thing, and lumps everything else into the second category: not-the-best.<br>
<br>
"Better" specifies two things, and it is known that "everything else" is not being considered at the moment, and so it not being discarded at the moment.&nbsp;&nbsp;"Best" discards everything but the "best" immediately.<br>
<br>
"Better" immediately leads to questions such as, "Why is it better?&nbsp;&nbsp;In what way is better?&nbsp;&nbsp;And, in what ways is it worse?"<br>
<br>
When you think of "best", it does not immediately call into mind the same questions, because the power of the symbol of "best" is that there are no competitors, it is the best.<br>
<br>
And yet, from our inspection earlier we see that "best" means a very limited set of scenarios, do we know that we described the scenarios accurately?&nbsp;&nbsp;If the "best" is based on a limited set of scenarios, and we described anything inaccurately in the description of our scenario, than very likely we chose the wrong "best".<br>
<br>
In comparison with "better", we have to be more explicit.&nbsp;&nbsp;Our language compels us to describe the "better attributes" explicitly, and begs that we also describe the "worse attributes" in comparison.&nbsp;&nbsp;"Best" does not beg that we describe the "worse", because we don't care about the worst methodology or worst design.&nbsp;&nbsp;Our minds enjoy the relationships of extremes.&nbsp;&nbsp;"Better" leads to "more good" and "less good"; "Best" leads to "worst".<br>
<br>
In both "best" and "better" we do care about their peer results, but "best" claims to have no peers, while "better" usually implies there are competing peers.<br>
<br>
Thought exercise:&nbsp;&nbsp;In what circumstances currently do you use the term "best"?&nbsp;&nbsp;When applying my critique above, what strikes you as something you need to think about more in terms of "best" or "better"?<br>
<br>
Can you think of a single thing you currently describe and think about as "best" that it would be better to reframe as "better"?&nbsp;&nbsp;What tangible benefits could this immediately bring you, from this change in your thinking and decision making abilities?<br>
<h2 id=9b893b40e08934229116cacf12764a11><a href="#9b893b40e08934229116cacf12764a11">3.5</a>: Understanding Engineering</h2>
<br>
I've said before that I think Engineering is:<br>
<br>
{{ definition_begin__engineering }}<br>
"The efficient use of resources that meet requirements which sufficiently satisfy your goals."<br>
{{ definition_end__engineering }}<br>
<br>
Let's break this down in a way where we can understand Engineering as a process.<br>
<br>
If we wanted to make a sequence from general-to-specific in terms of honing in on understanding Engineering, we can start here:<br>
<br>
- Environment		-><br>
- Resources		-><br>
- Requirements		-><br>
- Goal			-><br>
- Actions		-><br>
- Changed Environment	-> <br>
- Desired Effects?&nbsp;&nbsp;<br>
- Efficient use of resources?&nbsp;&nbsp;<br>
- Management of environment?<br>
<br>
We start with an Environment, in which we have Resources, and we have some kind of Requirements, which apply to some Goal(s), so we perform some Actions, which change the Environment.<br>
<br>
Do these Actions have the Desired Effects?<br>
<br>
Did we make efficient use of our Resources?<br>
<br>
How efficiently can we manage our Environment?&nbsp;&nbsp;What is it like day-to-day operating what we have built?<br>
<br>
{{ break }}<br>
<br>
With the above sequence and prose description of that sequence, we have a starting place to understand what Engineering is.&nbsp;&nbsp;It's something we do, it's something that produces results we may or may not want.&nbsp;&nbsp;It changes things.<br>
<br>
These are all things that can be said to describe Engineering, and shine lights on it's different surfaces, which show different things to different people, coming from different viewpoints.<br>
<br>
Engineering is multi-faceted to an amazing degree, so we will have to describe it repeatedly in vague terms to cloak it in an overall shape that provides better understanding.<br>
<br>
Like Local vs Global Alignment, Engineering can be understood in a small or shallow manner well Locally, but when compared against other descriptions which are equally accurate, they do not seem to Align well.<br>
<br>
It is only through creating many Local descriptions which Align well, and combine together into a Global network of descriptions which all Align well, that we can create a real understanding of what Engineering is.<br>
<br>
What does Engineering mean to you?<br>
<br>
How would you summarize it in a sentence, as I have?&nbsp;&nbsp;How does your summary differ from mine?&nbsp;&nbsp;What advantages do you see in your summary over mine?&nbsp;&nbsp;Can you make a denser and more correct description?&nbsp;&nbsp;<br>
<br>
Brevity allows for a type of clarity which details do not provide, as details allow for a type of clarity which brevity does not provide.&nbsp;&nbsp;They are the extremes of the scale of all valid information.<br>
<br>
Feel free to share your personal summaries with me, I am happy to hear how others view things, and expand my own understanding accordingly.<br>
<h3 id=dd4d43fb90d90e89b351e98d3788a97c><a href="#dd4d43fb90d90e89b351e98d3788a97c">3.5.1</a>: The Use of Resources</h3>
<br>
For our purposes, Resources can be summarized to the short list of:<br>
<br>
- Overall Time<br>
- Personnel Time<br>
- Money<br>
- Hardware<br>
<br>
Overall Time is like calendar time.&nbsp;&nbsp;Things can take hours, or a month, or the month of March goes by, or something is a quarter of a year.&nbsp;&nbsp;This is all "overall" time.&nbsp;&nbsp;It speaks to time passing, which you cannot do-over, making it a limited resource.&nbsp;&nbsp;This is heavily tied to Money, which is why the saying "Time is money" has a logical truth to it, since salaries, rent and loans must all be paid at distinct time periods, so this is a very important concept for organizations.<br>
<br>
Personnel Time is the time that any given person has to perform work.&nbsp;&nbsp;For instance, in an example job an engineer may have 40 hours of time to potentially perform work in a week.&nbsp;&nbsp;Over a month that is 160 hours of potential time.&nbsp;&nbsp;This is also a limited resource, and while organizations can make this flexible by paying more (hourly/bonuses/etc) or by asking for the person to simply give more time (unpaid overtime/death marches/etc), it still mostly remains a very limited resource.<br>
<br>
Money is obviously a limited resource as it is a scalar/number.&nbsp;&nbsp;At any time an organization will have a value for available capital, and another value of available credit, and potentially options for creating more capital (sales/etc) or credit (new lines/etc).&nbsp;&nbsp;These are all limited resources, and running out of money is almost exclusively the only reason organizations cease to exist, or are otherwise "abandoned".<br>
<br>
Hardware is essentially a "platform" for performing work.&nbsp;&nbsp;We can lump buildings, facilities, hardware-infrastructure, and all other kinds of things into this that are essentially "things we buy/rent with money, that we then 'own' and have to manage".<br>
<br>
Apart from these things there are of course other categories, such as Software that we buy (like Hardware), but these days you can run your entire organization on Free Open Source Software (FOSS) and many companies do just that, operating as well or better than those who pay for software.&nbsp;&nbsp;So, Software is fairly subjective in terms of being a resource like Hardware, as without Hardware we do not have any place to run FOSS or commercial software, and so we cannot operate.<br>
<br>
Additionally, engineering companies often create their own software, and this is required for managing your own operational environments, as there will be somethings that are unique about your organization, even if you try to make it as generic as possible, from the software-infrastructure side of things.&nbsp;&nbsp;<br>
<br>
Finally, even commercial software requires configuration, troubleshooting, maintenance, etc, so in comparison with do-it-yourself style software, the difference is only in Personnel Time and Money, and it may well be cheaper to do it either way, depending on your unique situation and goals.<br>
<br>
How you use resources will determine the efficiency in the interactions between them, and the overall level of quality and quantity of work that you can perform, which will impact the success of your goals, and the success of your organization.<br>
<br>
Using resources efficiently is of prime importance for any Engineer.<br>
<p id=9ed589a4467b296c2ea9dbb09ae0f49d><b><a href="#9ed589a4467b296c2ea9dbb09ae0f49d">3.5.1.1</a>: Evaluate the environment.&nbsp;&nbsp;Know the present.&nbsp;&nbsp;Real vs. Virtual.</b></p>
<br>
Do you remember the term "Knowability", which I introduced towards the beginning of the book?<br>
<br>
If not, please refresh your memory quickly here:&nbsp;&nbsp;{{ section__knowability }}<br>
<br>
In order to make efficient use of our resources, we must understand our resources, in as much depth as possible, in as many categories as possible, for our given cost-benefit requirements, to meet our goals.&nbsp;&nbsp;So, we want to know "almost everything about everything", while trying to minimize that into as few things as possible, because keeping track of more things is more work than keeping track of less things, and so is less efficient.<br>
<br>
The most important thing to know about our Environment is the "Present State".&nbsp;&nbsp;This is the current state of affairs, for everything, as it actually is.&nbsp;&nbsp;Reality.<br>
<br>
When we previously inspected Knowability, as a concept, we stated that "reality is not truly knowable", because there is so much about any physical thing that we simply cannot measure, and we run everything on Hardware, which is a physical thing.<br>
<br>
So, what we have left is what we can measure, and with these things we will attempt to "know the present".<br>
<br>
Knowing the "past" is as simple as having snapshots of your "present" still available after time.&nbsp;&nbsp;So any data that is Versioned, or stored in a Time Series, can be used to compared against the Present or other Past Snapshots.<br>
<br>
We can think of any of these time slices, or moments-in-time, as a "Snapshot" of all the data of our Environment.&nbsp;&nbsp;With all these data points from "now" and the past, we can understand where we came from and where we are.<br>
<br>
We can further extrapolate, by various statistical means, projections of how things will be over time.&nbsp;&nbsp;Some things we extrapolate are valid, and useful information.&nbsp;&nbsp;Other things we can extrapolate, but they are actually invalid, in that while the mathematics used to calculate them may be valid, the application of that processing against the given data set, for our desired results is not a valid combination.&nbsp;&nbsp;<br>
<br>
This is important to know, as you can predict somethings, such as "How many hard disks do we expect to fail next month?", but you cannot predict other things such as "Will this specific hard drive in this specific machine, fail next month?".&nbsp;&nbsp;No amount of statistical analysis can answer a useful boolean value there, and a non-boolean result is not something you can reliably make a decision on in that case.<br>
<br>
For example, for a given machine and hard disk device, will knowing it's manufacturing lot number, with the known MTBFs (Mean Time Between Failures), and the lifespan of the system, and the usage of the disk (IOPS over time), be able to determine if you must replace that exact hard disk device, in the next month?<br>
<br>
No.&nbsp;&nbsp;That specific hard disk device could fail in the next second, or could last another 5 years, you cannot give a valid actionable answer to this question.<br>
<br>
However, if we restate the question as, "How many disks do I need to have in stock, in order to replace the number of disks in all of my systems that are likely to fail in the next month?"<br>
<br>
This is a very different question, because it deals with a population of disk devices, not a single disk device.&nbsp;&nbsp;Across a population this statistical analysis becomes valid, and it will remain statistically-true, as long as the numbers you give it are accurate and correlate properly, which becomes more true as the population size increases, and as you can improve correlating relationships.<br>
<br>
So, with the Physical hardware and other Real things, we cannot know everything, but with Virtual things, Data and Logic, we can know everything.<br>
<br>
We can gather the exact values for each of the things we wish to know, and we can store them exactly as how they live in the real world, or can digest them so that we store a reference or as a reference count, or we can do anything else we want with them, because they are Virtual, we can know them completely.<br>
<br>
And, since we are also inspecting the Physical things with Logic, which is Virtual, we only data Virtual output (Data) from our Logic, so all we know are Virtual things, not Real physical things.&nbsp;&nbsp;We can use the virtual knowledge to extrapolate about the physical knowledge we cannot reach directly.<br>
<br>
On the Knowability spectrum, Virtual information is Knowable at 1.0: Completely Knowable.<br>
<br>
An important note about "now".&nbsp;&nbsp;You can never know things in the truly "Now" state, because all information arrives to you in a delayed fashion.&nbsp;&nbsp;It took time for the information to travel from it's source, to you.&nbsp;&nbsp;Whether this is via network packets, visible light, vibration, or any other method of information propagation, it has a delay before arrival.<br>
<br>
In terms of Monitoring, this means that all time series collected data, and other collected data, is aged.&nbsp;&nbsp;It has an age that is older than 0 seconds, in which that information was "accurate-as-of-Now", but the "now" that you are looking at is actually aged information.<br>
<br>
The only requirement is that this information is "new enough" to be considered "now", but it is never truly "Now" that you are looking at.&nbsp;&nbsp;This is important to keep in mind, since different decisions require a different level of "freshness" of data, to be a decision made from valid data.<br>
<br>
Thought experiment: What do you currently know about your own environment?&nbsp;&nbsp;What don't you know?&nbsp;&nbsp;What did you think you knew before you read this, but changed your mind as you read?<br>
<br>
How can you use this perspective to improve your efficient use of your resources?<br>
<p id=6f4678a0c1cc447ce97cf330abb63e6d><b><a href="#6f4678a0c1cc447ce97cf330abb63e6d">3.5.1.2</a>: Modeling</b></p>
<br>
To create a Model of something, is to try to "map" it some way.&nbsp;&nbsp;Models can be made in any way you can think of, but typical models are things like:<br>
<br>
- Data Schemas: such as in a relational database.<br>
- Graphs: nodes and edges which define a sort of topology.<br>
- Flow Charts, State Machines, Entity Relationship Maps, and other process diagrams.<br>
<br>
Each type of Model is meant to provide the ability to simulate something, such as your Operational Environment.&nbsp;&nbsp;<br>
<br>
If you were to Model your Operational Environment with each method you could, some of the data would overlap between model-types, and some of the data would be unique per model-type.<br>
<br>
Out all of these, the most fundamental type of modeling is the Data Schema model, and the Relational data schema model is the most comprehensive way to model this data.<br>
<br>
This is because all data can be describes as collections of fields (tables), with relationships between them (inter-table field constraints).&nbsp;&nbsp;Graphs, flow charts, and all other types of models can be described textually through a schema, and these schemas can be put into databases such as MySQL, PostgreSQL, Oracle, sqlite, etc.<br>
<br>
Once a relational schema is created, for the clearest expression of the schema, then the schema can be "de-normalized" and otherwise "un-spun" so that it can fit into non-relational databases, such as column-oriented or time series databases.&nbsp;&nbsp;These databases have advantages for some access patterns (such as mostly-inserting data), but their schema is less expressive due to this optimization, so it is best to first understand it's model through a relational schema.<br>
<br>
Relational schemas can also be written as programming language "structs", or data primitives, and extended into Classes (Object Oriented style "structs").&nbsp;&nbsp;This may seem like looking at things in a skewed way, but you can look at these data structures from any direction to get a better understanding of them.<br>
<br>
There are two primary reasons to create Models:<br>
<br>
- Creating Models to better understand a topic.<br>
- Creating Models to control a set of resources.<br>
<br>
Models made for learning are about providing insight, and different ways of looking at data, and are beyond being documentation are generally disposable, ephemeral, and prone to becoming out of date.<br>
<br>
For a given Environment, a Model can provide understanding, through creating a summary of the system trying to be understood.&nbsp;&nbsp;A model like this can be given variables and used to calculate probabilities, and perform analysis to aide in making decisions.<br>
<br>
This is a very different thing from a Model that is created in order to control resources.<br>
<br>
A Model created to control resources will share many things with Models made for understanding, in that it is also a summary of the system, but unlike a Model for understanding, a Model for control is built to last potentially for the lifetime of the resources and beyond.<br>
<br>
Models for control are intended to make operating an Environment better by allowing inspection of state and control through the model.&nbsp;&nbsp;A Control Model must be absolutely accurate, and have highly synchronized coordination with the Environment itself, or it risks becoming out-of-sync, and unable to Control the Environment.<br>
<br>
In contrast, a Model for understanding does not need to be highly synchronized, or absolutely accurate, because it only needs to be "good enough" to provide the required insight.&nbsp;&nbsp;More accurate and more synchronization can assist in providing better accuracy, but less accuracy might be sufficient depending on your goals for better understanding.<br>
<br>
Creating Models for understanding has a lot of documentation that already exists about it, and there are many mature areas of study that currently exist for this.<br>
<br>
Creating Models for control does have some good examples in the wild, and some that are taught in mature areas of study, but I am of the opinion that we still do not have much documentation in this area, so I will do my best to describe how I do this effectively, quickly, and how I get good results every time.<br>
<br>
Modeling is a core skill in Engineering, so if you do not already consider yourself a proficient modeler, you should take any attempt to start creating more models when opportunities arise, as practice improves all skills.<br>
<p id=1e2f1485f11d72e7cc37ce72c7de6775><b><a href="#1e2f1485f11d72e7cc37ce72c7de6775">3.5.1.2.1</a>: Black-Boxing the World</b></p>
<br>
Once we accept that anything can be modeled, then we can go about modeling everything that is useful.&nbsp;&nbsp;We can model for Understanding, but it is better to model for Control, since you get both.<br>
<br>
Remember the introduction to Pragmatism?&nbsp;&nbsp;If not, check here:&nbsp;&nbsp;{{ section__pragmatism }}<br>
<br>
Using Pragmatism, we can evaluate anything on only the effects that they cause.&nbsp;&nbsp;These effects can be turned into schema, as can any additional data needed to model the effects.<br>
<br>
When modeling for Operations, there are 2 main areas of modeling:<br>
<br>
- Model Reality: Describe what exists.<br>
- Model Effects: Describe what happens.<br>
<br>
We'll cover these in detail later as we go over the OpsDB, which is all about doing both of these things.<br>
<br>
Remember the "Universal Machine" concept?&nbsp;&nbsp;If not, check here:&nbsp;&nbsp;{{ section_um }}<br>
<br>
Universal Machines map Inputs, Outputs and Side-Effects, which is just a more explicit version of a Function, which maps Inputs and Outputs, and may perform Side-Effects, but does not explicitly model them for Control purposes.<br>
<br>
Using modeling, by way of Pragmatism, through the Universal Machine interface, we can model anything and everything.&nbsp;&nbsp;We can Black-Box the World, or wrap the world full of "black boxes", which contain something that has the signature of the Universal Machine (Input/Output/Side-Effects).<br>
<br>
Later, I will go over how to actually do this, but for now I just wanted to point out what our currently defined terminology and tools allow us to do, which is quite a lot.<br>
<p id=86a667264372ca24826a809f97ed36b8><b><a href="#86a667264372ca24826a809f97ed36b8">3.5.1.3</a>: Algorithms</b></p>
<br>
There are lots of important Algorithms in Engineering, they are Virtual and are frequently constrained to these types of things:<br>
<br>
- Searching for data: Finding things based on some matching criteria<br>
- Sorting data: Ordering data based on some sorting criteria<br>
- Coordination: Locking, reference counting, signaling other coordination style actions<br>
- Encoding/Decoding: Encryption, compression, encapsulation, and other wrap/unwrap style actions<br>
<br>
There are other categories as well, but these are often what we think of in Operational Engineering when someone says "algorithms".<br>
<br>
There are many good references for these, including Wikipedia or Donald Knuth's books, for a completely in-depth comparison between an encyclopedia of algorithms.<br>
<br>
In terms of Operations, while we use these other algorithms, I will focusing on "Algorithmic Properties" and very fundamental Algorithms.<br>
<br>
One important "Algorithmic Property" is Idempotency.&nbsp;&nbsp;This means that when you apply an Algorithm with this Property that the result is always the same.&nbsp;&nbsp;In simple mathematics this can be seen by "1 * 1 = 1".&nbsp;&nbsp;"* 1" is the Algorithm, and the result is always the same as the same as the original value (1 == 1).<br>
<br>
This has interesting mathematical uses, but in Operational Engineering, the use is that if we perform a function, we always have the same result.<br>
<br>
Consider a Algorithm that ensures that a directory exits with a given set of permissions.<br>
<br>
Let's say that this will be the input data for this Algorithm, in YAML format:<br>
<br>
{{{ code_begin }}}<br>
type: ensure_directory_exists<br>
path: /Users/ghowland/projects/OpsEngAuto/sections<br>
mode: 755<br>
user: ghowland<br>
group: staff<br>
{{{ code_end }}}<br>
<br>
When the function that executes this Algorithm runs against this data it will ensure that a directory like this is created, if it doesn't exist:<br>
<br>
{{{ code_begin }}}<br>
$ ls -ld sections<br>
drwxr-xr-x&nbsp;&nbsp;346 ghowland&nbsp;&nbsp;staff&nbsp;&nbsp;11764 Aug 23 00:48 sections<br>
{{{ code_end }}}<br>
<br>
If the directory does exist, then it ensures that the mode, user and group are correct.<br>
<br>
At the end of the function running, we always have this directory, with the correct mode, user and group permissions.<br>
<br>
This is a basic example of what Idempotency can mean in a Operational Engineering environment.&nbsp;&nbsp;This property can be used in many places to ensure that we always get a single result, without conditional changes.&nbsp;&nbsp;It either works, and we get what we expect, or it fails and we know there is a problem (such as lack of permissions to make the changes).&nbsp;&nbsp;These are both desirable states, because both success and failure meet the Idempotent criteria we set forth.<br>
<br>
In comparison to an Algorithmic Property is an Algorithm, such as "Iterating Over a Sequence".<br>
<br>
We could combine the previous example with this, to create Logic that will ensure a number of directories exist.<br>
<br>
For example, consider this YAML data that lists YAML paths for our above ensure_directory_exists function:<br>
<br>
{{{ code_begin }}}<br>
ensure_directory_exists:<br>
&nbsp;&nbsp;- /Users/ghowland/projects/idempotent/dirs/OpsEngAuto_sections.yaml<br>
&nbsp;&nbsp;- /Users/ghowland/projects/idempotent/dirs/OpsEngAuto_toc_backups.yaml<br>
&nbsp;&nbsp;- /Users/ghowland/projects/idempotent/dirs/something_else.yaml<br>
{{{ code_end }}}<br>
<br>
If we wrote some Python like this, we can iterate (go over each item in the list) like this:<br>
<br>
{{{ code_begin }}}<br>
directory_data = LoadYaml('/path/to/ensure_directory_exists.yaml')<br>
paths = directory_data['ensure_directory_exists']<br>
for path in paths:<br>
&nbsp;&nbsp;dir_data = LoadYaml(path)<br>
&nbsp;&nbsp;EnsureDirectoryExistsIdempotentFunction(dir_data)<br>
{{{ code_end }}}<br>
<br>
This code assumes a LoadYaml() and EnsureDirectoryExistsIdempotentFunction() exist for convenience, and do what they say they do.&nbsp;&nbsp;This will iterate over our list of YAML files that contain our directory data, to Idempotently ensure exist.<br>
<br>
Over the course of the coming chapters we will introduce many Algorithmic Properties which give us good results in Operations, and we will compare when to use them, and how to use them efficiently.<br>
<p id=c5cff688b2a25a6cc5ab3c0301d86a54><b><a href="#c5cff688b2a25a6cc5ab3c0301d86a54">3.5.1.4</a>: Centralized vs. Decentralized</b></p>
<br>
TODO:&nbsp;&nbsp;Push vs Pull, when is it centralized?&nbsp;&nbsp;Do you want tight control, or loose control?&nbsp;&nbsp;Both have their effects.&nbsp;&nbsp;People typically want tight control, or the effects of tight control (knowledge that it worked).<br>
<p id=5fa11c75ac5e5ee842071b89611bd9ac><b><a href="#5fa11c75ac5e5ee842071b89611bd9ac">3.5.1.5</a>: Distributed Systems</b></p>
<p id=1a38d9aa40613994ccbc55d3bd80aac3><b><a href="#1a38d9aa40613994ccbc55d3bd80aac3">3.5.1.6</a>: Distributed Data</b></p>
<p id=4f692dac9d4a18060c7ed7ab3c560bea><b><a href="#4f692dac9d4a18060c7ed7ab3c560bea">3.5.1.7</a>: Hardware: Fixed vs. Utility vs. Cloud</b></p>
<p id=cd0b3e19dbeb9aa7495f50e8b3698932><b><a href="#cd0b3e19dbeb9aa7495f50e8b3698932">3.5.1.7.1</a>: Fixed Hardware</b></p>
<p id=b4df504c277c470cd0ad26990e1ae72e><b><a href="#b4df504c277c470cd0ad26990e1ae72e">3.5.1.7.2</a>: Utility Hardware</b></p>
<p id=a69a4ba83c5494ef7dba4d5ef550c7cd><b><a href="#a69a4ba83c5494ef7dba4d5ef550c7cd">3.5.1.7.3</a>: Cloud Hardware</b></p>
<p id=23c810f8045fe70f023448e7aeaa259c><b><a href="#23c810f8045fe70f023448e7aeaa259c">3.5.1.7.3.1</a>: *aaS</b></p>
<br>
Everything as a Service.<br>
<p id=cc126bbb155f6cf8bd48d01908206040><b><a href="#cc126bbb155f6cf8bd48d01908206040">3.5.1.7.4</a>: What do you have to care about?</b></p>
<p id=25a7c2f4dc01247e2e4d86c271ee3eb4><b><a href="#25a7c2f4dc01247e2e4d86c271ee3eb4">3.5.1.8</a>: Types of Complexity</b></p>
<br>
There are a number of different kinds of complexity that we have to cope with while performing Engineering tasks.&nbsp;&nbsp;Let's enumerate them so we can refer to them explicitly, instead of clumping them all together as "complexity" or having to describe them each time.<br>
<br>
Each of these types of complexity also represent a spectrum or axis, as we only think of complexity as something heads toward 1.0, while things closer to 0.0 on the axis are seen as simple.<br>
<br>
This means that any issue can be evaluated on all types of complexity, to get a better understanding of it's total "complexity shape".<br>
<br>
- Large-scale Complexity<br>
- Detail Complexity<br>
<h2 id=b897d8c3f141f288841664b42ade8068><a href="#b897d8c3f141f288841664b42ade8068">3.6</a>: Code management</h2>
<h2 id=44e191e4a8799ec4d8239c53a915b728><a href="#44e191e4a8799ec4d8239c53a915b728">3.7</a>: Perfect is the enemy of done</h2>
<h3 id=d98cb46eb6a0d64a68131fa80be27a81><a href="#d98cb46eb6a0d64a68131fa80be27a81">3.7.1</a>: Quality is Never #1; Utility is Always #1</h3>
<h3 id=8004ec99010dd83302cefe3d12375a6a><a href="#8004ec99010dd83302cefe3d12375a6a">3.7.2</a>: Security Is Also Not #1</h3>
<h2 id=53ee284612b4d4678a26814fc2442067><a href="#53ee284612b4d4678a26814fc2442067">3.8</a>: Troubleshooting</h2>
<h3 id=222b0da1a677c8319df0b5742703e46f><a href="#222b0da1a677c8319df0b5742703e46f">3.8.1</a>: Monitoring</h3>
<h3 id=5e9a4e088d8a4899a4a8579fec56b098><a href="#5e9a4e088d8a4899a4a8579fec56b098">3.8.2</a>: Spectrums</h3>
<p id=2cda0e85947b37088449bf5d24291155><b><a href="#2cda0e85947b37088449bf5d24291155">3.8.2.1</a>: Comparisons</b></p>
<h2 id=ac39699dc841781b49de6156b7d47f07><a href="#ac39699dc841781b49de6156b7d47f07">3.9</a>: Skill Ladders</h2>
<h3 id=8c334623a47643e18e33479feebf5bed><a href="#8c334623a47643e18e33479feebf5bed">3.9.1</a>: Graphing Skills</h3>
<h3 id=5e25a809a807106b545adb208a4fa99d><a href="#5e25a809a807106b545adb208a4fa99d">3.9.2</a>: Understanding Your Own Ladder</h3>
<h2 id=291d5132845ea58ade7ea580866bf0f6><a href="#291d5132845ea58ade7ea580866bf0f6">3.10</a>: When to use Statistics</h2>
<br>
<br>
<br>
When I started this book I made some statistical counters, which are sections, words and lines written.<br>
<br>
I estimated from about 280 sections off of my first 10 sections written, that I would have about 208,000 words at the end of the book.<br>
<br>
I have been checking my percentage complete, such as currently:<br>
<br>
"""<br>
 Total Sections: 301 Populated Sections: 54 Current Goal: Populate Empty Sections: 247 (Done: 17.9%)<br>
<br>
Lines: 2197<br>
<br>
Words: 37668<br>
"""<br>
<br>
And the sections and word percentages to completion have almost kept perfect alignment the entire time I have been writing this work.<br>
<br>
Yesterday was:<br>
<br>
>>> 33000 / 200000.<br>
0.165<br>
<br>
And today (with the above quote):<br>
<br>
>>> 37600 / 200000.<br>
0.188<br>
<br>
18.8% word vs 17.9% sections, in terms of estimated complete.<br>
<br>
Additionally I have been adding sections and removing them as I see fit.&nbsp;&nbsp;Im not trying to match this data up, and Im not trying to count words in my sections, I just write what seems to fill the topic section, and move on.<br>
<br>
And yet the percentage complete to my initial rough-calculation of 208,000 words, remaining in-line with the number of sections I have.&nbsp;&nbsp;I will do an analysis on this from my Github entries, since all of this is in version control once the book is done.<br>
<br>
This is a topic that apparently works very well with statistical analysis, and the results are "amazingly accurate" as a study of the population of words and sections I write over time.<br>
<br>
Apparently there is some kind of statistical slant I have to writing a certain number of words a day, a certain number of sections a day, and so on.<br>
<h3 id=18ddda391b891bf36f9b2387380f5e67><a href="#18ddda391b891bf36f9b2387380f5e67">3.10.1</a>: Across many things: Appliable</h3>
<h3 id=967dc75f17be743f5b44485436fceff2><a href="#967dc75f17be743f5b44485436fceff2">3.10.2</a>: For a given thing: Not Applicable</h3>
<h3 id=feb605a9dd85dcc6e0d371d023dea881><a href="#feb605a9dd85dcc6e0d371d023dea881">3.10.3</a>: Exercises</h3>
<h2 id=2d543cb2a0bfd85b80eacbcb10cf77b2><a href="#2d543cb2a0bfd85b80eacbcb10cf77b2">3.11</a>: How to Select Tools</h2>
<h3 id=17c8887cbd04084bc3b75f577132b78e><a href="#17c8887cbd04084bc3b75f577132b78e">3.11.1</a>: Many stand alone tools will end up being replaced</h3>
<p id=9362cba32d5a5c9dd234aecef27564d4><b><a href="#9362cba32d5a5c9dd234aecef27564d4">3.11.1.1</a>: Text and data and the purpose of the tools</b></p>
<p id=e122b3c42185ad60077b1cc58c7f1f22><b><a href="#e122b3c42185ad60077b1cc58c7f1f22">3.11.1.2</a>: Explain Replacement of DNS, DHCP, etc</b></p>
<p id=957ddd798c6271497229ea774b39e478><b><a href="#957ddd798c6271497229ea774b39e478">3.11.1.2.1</a>: Zones, Subnets, etc</b></p>
<h2 id=27893ca25e6be2dd440c59fcc7aa321e><a href="#27893ca25e6be2dd440c59fcc7aa321e">3.12</a>: Name spaces</h2>
<h2 id=ac19b6971bff8dc5db71667d1cb1d022><a href="#ac19b6971bff8dc5db71667d1cb1d022">3.13</a>: Structure as Logic</h2>
<br>
Explain how I use schema and other structures in place of Logic, reducing the total amount of Logic, and making the gap between working features and Logic-creation much smaller.<br>
<br>
How this scales better than not doing this, writing everything as Logic without help from Structure.<br>
<br>
Structure is Efficient Alignment, in practice.<br>

# Chapter 4: Automation Philosophy and Methodology in Operations






<h2 id=92fb73bc7b038ce1ccda5ff2fbfdbd56><a href="#92fb73bc7b038ce1ccda5ff2fbfdbd56">4.1</a>: ***** Removing classes of work.</h2>
<h3 id=b7ed43cb9d71411713c556599a83a068><a href="#b7ed43cb9d71411713c556599a83a068">4.1.1</a>: Manual automation is a force multiplier.&nbsp;&nbsp;Mistakes are also multipled.&nbsp;&nbsp;Unintended consequences can be severe and wide-spread.</h3>
<h3 id=6715d22e2b900a354a2308f0a78af63e><a href="#6715d22e2b900a354a2308f0a78af63e">4.1.2</a>: Making people do more complicated and dangerous activtiies should not be an end-goal of automation, though it will likely be an intermediary step.</h3>
<p id=5530d1c5607e5f60f382ea9e52ce84d2><b><a href="#5530d1c5607e5f60f382ea9e52ce84d2">4.1.2.1</a>: Step with caution.</b></p>
<h2 id=80ef8721e561c4cedf7d5e7c71ded573><a href="#80ef8721e561c4cedf7d5e7c71ded573">4.2</a>: Introduce spectrum of automatability.&nbsp;&nbsp;How automateable is something in configure X vs Y?&nbsp;&nbsp;This is automatability.</h2>
<h2 id=24e3b555ee6f249c33c40b79fce7e744><a href="#24e3b555ee6f249c33c40b79fce7e744">4.3</a>: Working with N axis data for evaluation of properties.&nbsp;&nbsp;Properties are scalar, but there are many dimensions to measure, and collectively they are near-infinite.</h2>
<h3 id=5b9d7b060f1397403be31640db9326c5><a href="#5b9d7b060f1397403be31640db9326c5">4.3.1</a>: Tuning your goals based on your methods.</h3>
<h3 id=45ba9f44240bd3d8eb4785969cda5301><a href="#45ba9f44240bd3d8eb4785969cda5301">4.3.2</a>: How to create your own Axioms.&nbsp;&nbsp;Some standard axioms.&nbsp;&nbsp;Axiomatic development.</h3>
<h3 id=ee01dd35dc1f46d2db9f2bb0383055da><a href="#ee01dd35dc1f46d2db9f2bb0383055da">4.3.3</a>: Tools to fit the job.&nbsp;&nbsp;Testing in an operational environment.&nbsp;&nbsp;Mock-tests, etc in a world of only side effects.&nbsp;&nbsp;Using Vagrant and VMs to test allows these side-effects to be tested, but take time to set up.&nbsp;&nbsp;Worth it, but you may not start there in a live environment because of all the legacy that would have to be replicated and is changing all the time in non-standard ways.</h3>
<h3 id=2694eafa373f1024fd47adf1fc0878be><a href="#2694eafa373f1024fd47adf1fc0878be">4.3.4</a>: How to standardize things.&nbsp;&nbsp;Simplification.&nbsp;&nbsp;The benefits and limitations.&nbsp;&nbsp;Simpler means less options at any given time.&nbsp;&nbsp;1-1 work is infinite precision and difficult to scale.&nbsp;&nbsp;Simpler is can be deep precision in 1 or several ways, but does not allow all options.&nbsp;&nbsp;Build your option matrix out of what you need, ensure all your use cases are covered.</h3>
<h2 id=024280ac08d372e795de22ac03f8aec5><a href="#024280ac08d372e795de22ac03f8aec5">4.4</a>: All processes can be automated to get a desired effect, if enough information about it is known.</h2>
<h2 id=a562892f336213a7fd2005780a71e6b4><a href="#a562892f336213a7fd2005780a71e6b4">4.5</a>: Introduce Intelligence.&nbsp;&nbsp;Actionable Intelligence.</h2>
<h2 id=3c09a1e29d529b0e7e64d4c2cf6e026f><a href="#3c09a1e29d529b0e7e64d4c2cf6e026f">4.6</a>: Automating anything</h2>
<h3 id=6a253a9ff3699cfa00ae788353e36df9><a href="#6a253a9ff3699cfa00ae788353e36df9">4.6.1</a>: Pre-Solving Problems</h3>
<br>
What are we doing when we automate?<br>
<br>
We are pre-solving problems.<br>
<br>
If we did not automate a solution, we would need to show up (as a human), and see what needs to be done, and then do it.<br>
<br>
When we pre-solve a problem, we are figuring out in advance how to detect a problem, how to "see it" with monitoring data collection, and creating troubleshooting logic (testing the environment) to determine how to solve a given set of problems.<br>
<br>
If we are comprehensive about describing which problems can occur, and we are comprehensive about what states the problems may contain, it is possible to Black Box an entire set of problems so that they can be solved with Logic instead of Humans.<br>
<br>
This is what makes the elimination of Classes of Work possible.<br>
<br>
Through understanding our environments and using systemic thinking and the Slicing The Pie technique to ensure we have comprehensive coverage of anything we are looking at, we can pre-solve problems by going through all their states.<br>
<br>
In testing our solutions, we will find mistakes and incorrect assumptions we have made, and over time Reality will inform us of additional mistakes, incorrect assumptions and also contexts we were not aware of, or did not prioritize.<br>
<br>
As these new areas are added to our awareness, and we prioritize them we will continue to slice the pie into more sections which allow us to cope with these problems and pre-solve them as well.<br>
<h2 id=18279c1b25b35838b531d26379bf8feb><a href="#18279c1b25b35838b531d26379bf8feb">4.7</a>: Total elimination of manual work.&nbsp;&nbsp;How to remove classes of work from being necessary.</h2>
<h2 id=5ddef01855119bd34e5ea45dc320de43><a href="#5ddef01855119bd34e5ea45dc320de43">4.8</a>: Building the data and action chains, to create all workflow.</h2>
<h2 id=bab4fcb00ea2749653c2a43573413ce6><a href="#bab4fcb00ea2749653c2a43573413ce6">4.9</a>: The data requirements:&nbsp;&nbsp;Authentication, Authorization, Versioning, Change Management, Deployment, Pre-Post Deployment Actions, Schema Management</h2>
<h2 id=08a271c1b1d52b0b22293cc0aa24981f><a href="#08a271c1b1d52b0b22293cc0aa24981f">4.10</a>: How to construct an unbreakable process.&nbsp;&nbsp;How to stop that process from being completed/sealed, so that it breaks.&nbsp;&nbsp;How to ensure it breaks all the time, by setting conditions accordingly.</h2>
<h3 id=0667659ec138ba985e276e32c2c874a5><a href="#0667659ec138ba985e276e32c2c874a5">4.10.1</a>: Faux-automation.&nbsp;&nbsp;Manual automation.&nbsp;&nbsp;Automation-assist.&nbsp;&nbsp;Full-automation.&nbsp;&nbsp;Comprehensive Life-Cycle automation.</h3>
<h3 id=cc4e2b2b382a5b8203afd5f7c286d1e7><a href="#cc4e2b2b382a5b8203afd5f7c286d1e7">4.10.2</a>: This can be started as Procedure for Humans, but it will not be unbreakable, as people will make mistakes entering data (running commands is entering data)</h3>
<p id=4952dddaa19b91207fda5e21b66cb544><b><a href="#4952dddaa19b91207fda5e21b66cb544">4.10.2.1</a>: Entered on the right system?&nbsp;&nbsp;Right command?&nbsp;&nbsp;Right args?&nbsp;&nbsp;Right path?&nbsp;&nbsp;Right data?&nbsp;&nbsp;Right goal?&nbsp;&nbsp;Right everything?</b></p>
<h2 id=55fc6a2fc3929e32f3e6aa8c650e52c3><a href="#55fc6a2fc3929e32f3e6aa8c650e52c3">4.11</a>: Flexibility and dangers of an automation system.</h2>
<h2 id=9d7a7dfb8deeb7338094c604cb4d6853><a href="#9d7a7dfb8deeb7338094c604cb4d6853">4.12</a>: Distributed OS.&nbsp;&nbsp;DOS.&nbsp;&nbsp;N units, all being controlled, configured and scheduling work.</h2>
<h3 id=10b09a38df50bfa7e5a5c390d4cfffad><a href="#10b09a38df50bfa7e5a5c390d4cfffad">4.12.1</a>: Does not need a "traditional" cluster scheduler.&nbsp;&nbsp;Can use these these for "cron" type jobs though.</h3>
<h2 id=9fbbf8329fb60dc10037a5af19f31002><a href="#9fbbf8329fb60dc10037a5af19f31002">4.13</a>: Monitoring is the heart of automation.&nbsp;&nbsp;You cant control what you dont have info on.</h2>
<h3 id=e52665a326340a943354050c831ed263><a href="#e52665a326340a943354050c831ed263">4.13.1</a>: Instelligence:&nbsp;&nbsp;Actionable?&nbsp;&nbsp;Timely?&nbsp;&nbsp;Relevant?&nbsp;&nbsp;Correct?&nbsp;&nbsp;(Cross check it, all must align)</h3>
<h2 id=8ffdb0c910c1a74549d0d30d43ee3420><a href="#8ffdb0c910c1a74549d0d30d43ee3420">4.14</a>: Behavioral AI.&nbsp;&nbsp;An expert system, build by experts in Ops and Biz goals.</h2>
<h3 id=3fa9092174f6aa792fa739418160f025><a href="#3fa9092174f6aa792fa739418160f025">4.14.1</a>: Do not use fuzzy info until you have exhausted discrete/precise info.&nbsp;&nbsp;And turn the fuzzy info into a discrete/precise data point, so it can be acted on cleanly by logic.</h3>
<h3 id=102b1d39363d43827086af170dbc6c22><a href="#102b1d39363d43827086af170dbc6c22">4.14.2</a>: N of M failures is not fuzzy, even though it has a scalar value, and not boolean.</h3>
<h2 id=ab57d26b3045a6b20cffdd14faba910c><a href="#ab57d26b3045a6b20cffdd14faba910c">4.15</a>: 3 States:&nbsp;&nbsp;Now, Desired, Current State (Whats Out there?)</h2>
<h3 id=734e804607130b865c31b46d6cfbafb8><a href="#734e804607130b865c31b46d6cfbafb8">4.15.1</a>: How to manage.&nbsp;&nbsp;Importing, synthesizing, checking.</h3>
<h3 id=2c53820f8696b9c71bf7779bf141f713><a href="#2c53820f8696b9c71bf7779bf141f713">4.15.2</a>: Versioning, commits, pre/post-commit logic.</h3>
<h2 id=c8d4ceee72c4e9bec9a140aab31af0a7><a href="#c8d4ceee72c4e9bec9a140aab31af0a7">4.16</a>: Agent model.&nbsp;&nbsp;Centralized model.</h2>
<h2 id=8df33f2e3ab42652f8dbc974a55ade69><a href="#8df33f2e3ab42652f8dbc974a55ade69">4.17</a>: Library model.&nbsp;&nbsp;RPC model.&nbsp;&nbsp;Framework model.</h2>
<h2 id=8f3dc2bb1b918f96ed62f145545bf67d><a href="#8f3dc2bb1b918f96ed62f145545bf67d">4.18</a>: ORM vs wrapping lib vs straight SQL/data query.</h2>
<h2 id=a287441fde41b224c7f9d96589d445b0><a href="#a287441fde41b224c7f9d96589d445b0">4.19</a>: Scales,&nbsp;&nbsp;1000s/millions, not billions.&nbsp;&nbsp;Can make this "configuration scale" not "production deployment end-user scale".&nbsp;&nbsp;Optimize only when necessary, use tools that do heavy lifting for Time series data analysis, and import results and last N snippets into OpsDB.</h2>
<h2 id=e75b67627fcd0302ecae6162320e7b36><a href="#e75b67627fcd0302ecae6162320e7b36">4.20</a>: Selective Data Updating for Pyramid method and Mesh method.</h2>
<h2 id=8e5a823181660693663ac9171ea437f7><a href="#8e5a823181660693663ac9171ea437f7">4.21</a>: Compare Pyramid vs Mesh (p2p).&nbsp;&nbsp;Pros and cons.</h2>
<h2 id=52c5a2714542df457a2f43133a312847><a href="#52c5a2714542df457a2f43133a312847">4.22</a>: Introduce the dotted notation as a universal naming convention, for lookups, it can universally address any type of DAG data:&nbsp;&nbsp; domain.sub.thing.11.field.subfield.11.arrayfield.20.subsubfield</h2>
<h3 id=9d4135ad596f06c4521954e1f4b1e02f><a href="#9d4135ad596f06c4521954e1f4b1e02f">4.22.1</a>: **** Use this DAG lookup to go into YAML, DBs, etc.&nbsp;&nbsp;Schema Man can allow this.&nbsp;&nbsp;Can use sub-searches like globs (domain.thing.*.field) and translate that into SQL or whatever for more advanced usage.</h3>

# Chapter 5: Components of Engineering


In previous sections on Engineering I went over the philosophy and balance of engineering, and now I will break things into distinct components that we deal with, how they are related to each other, and how they fit into the overall toolbox of Engineering.





<h2 id=9d57ceec05645c59d6f2075d9f0010f6><a href="#9d57ceec05645c59d6f2075d9f0010f6">5.1</a>: Requirements</h2>
<h2 id=2ba77efca2a265edd1324d3bd9428fe9><a href="#2ba77efca2a265edd1324d3bd9428fe9">5.2</a>: Resources</h2>
<h2 id=3acfea5cb34700d7f57c71c7e91a56f1><a href="#3acfea5cb34700d7f57c71c7e91a56f1">5.3</a>: Goals</h2>
<h2 id=02777f4142c6f5eb7965e29b23cb99d0><a href="#02777f4142c6f5eb7965e29b23cb99d0">5.4</a>: Logic</h2>
<h2 id=448c60cae646ed5fb663c0e80f3ac6cc><a href="#448c60cae646ed5fb663c0e80f3ac6cc">5.5</a>: Environments</h2>
<h2 id=2cf2c8956445474303f9b37fdb3b3b4f><a href="#2cf2c8956445474303f9b37fdb3b3b4f">5.6</a>: Processes</h2>
<h3 id=3031549e01eccd24655c465ee066c55a><a href="#3031549e01eccd24655c465ee066c55a">5.6.1</a>: Adding Features</h3>
<h3 id=ac8f07d1f42734da546748635a0468ec><a href="#ac8f07d1f42734da546748635a0468ec">5.6.2</a>: Fixing Bugs</h3>
<h3 id=a892022d31a6ce8da3a2963df04f98d6><a href="#a892022d31a6ce8da3a2963df04f98d6">5.6.3</a>: Improving Efficiency</h3>
<h3 id=21af229194fd859b177ed5ffc69d3e53><a href="#21af229194fd859b177ed5ffc69d3e53">5.6.4</a>: Performing Maintenance</h3>
<h3 id=8d11cc51c9df4be833ccd1ded438597e><a href="#8d11cc51c9df4be833ccd1ded438597e">5.6.5</a>: Designing a New Version of a System</h3>
<h3 id=3b22dfec3a78e7c005242ec53c1fb0d6><a href="#3b22dfec3a78e7c005242ec53c1fb0d6">5.6.6</a>: Replacing a System</h3>
<h3 id=e55ae25922d8e9ed603a00ac583a5a95><a href="#e55ae25922d8e9ed603a00ac583a5a95">5.6.7</a>: Depricating a System</h3>

# Chapter 6: Components of Operational Environments






<h2 id=e0456dfc4344813c454b2832f721d7cc><a href="#e0456dfc4344813c454b2832f721d7cc">6.1</a>: Troubleshooting</h2>

# Chapter 7: Components of Automation Environments






<h2 id=a26d014573a051d21bf35b17d0eda041><a href="#a26d014573a051d21bf35b17d0eda041">7.1</a>: The process of building this system in your organization.</h2>
<h3 id=87e63ce8f2071f53f8805c0cd6fc706e><a href="#87e63ce8f2071f53f8805c0cd6fc706e">7.1.1</a>: Collect all unique data in one place.&nbsp;&nbsp;Ensure it is accurate by checking against reality, and combing through it manually to see if things line up, spot checking and automation checking every one by script.</h3>
<h3 id=f36abc40f33f81d73b6b8fd94bc37ff3><a href="#f36abc40f33f81d73b6b8fd94bc37ff3">7.1.2</a>: Things that are unique to you, vs things that are general to everyone.</h3>
<p id=0623d9b6199fbeb9e183439df55431b9><b><a href="#0623d9b6199fbeb9e183439df55431b9">7.1.2.1</a>: FQDNs, IPs, HW specs, OS specs, configuration variables, specific workflow and stuff.</b></p>
<h2 id=7007cad30eb5ca34743dbc74ecb214d6><a href="#7007cad30eb5ca34743dbc74ecb214d6">7.2</a>: Imaging vs re-building from scratch</h2>
<h3 id=5016b7b3143e119640e94393d4b76590><a href="#5016b7b3143e119640e94393d4b76590">7.2.1</a>: Correctness, up-to-date, vs speed.</h3>
<h2 id=206e9c61bb5ef53bbded00a8c8964b9e><a href="#206e9c61bb5ef53bbded00a8c8964b9e">7.3</a>: *** The Progression of an Automation System:&nbsp;&nbsp;Walk through all the stages **</h2>
<h3 id=6dab388a16ed3d77edcd61d24e22f562><a href="#6dab388a16ed3d77edcd61d24e22f562">7.3.1</a>: These shouldnt be an order so much, as people can take different routes.&nbsp;&nbsp; How to evaluate each of these spectrums/axis of data, scalars, would be good.</h3>
<h3 id=d7b7edd2b384d2fb2aa8ae8da1767599><a href="#d7b7edd2b384d2fb2aa8ae8da1767599">7.3.2</a>: Manual everything</h3>
<h3 id=1451f4580715a78839eb3ada548626a9><a href="#1451f4580715a78839eb3ada548626a9">7.3.3</a>: Kickstarts and auto config&nbsp;&nbsp;(AWS gets you here)</h3>
<h3 id=1c20fb798339d70263c0b78365f27f78><a href="#1c20fb798339d70263c0b78365f27f78">7.3.4</a>: Sys configuration tools, Monitoring, Centralized Logging, etc.&nbsp;&nbsp;Normal sys admin process.</h3>
<h3 id=8744736462545259d69fc1e0eacdc78a><a href="#8744736462545259d69fc1e0eacdc78a">7.3.5</a>: Issue tracking systems, change management ticket systems.</h3>
<p id=611430f5641a791eec9fda109deaecde><b><a href="#611430f5641a791eec9fda109deaecde">7.3.5.1</a>: Good to have different CMS for tickets, because your ops logic will change, but its more useful to track the CMS data right in the ops db for a real record of things, because it lists the complete workloads.</b></p>
<h3 id=1fc55849153c719e757bb6cba8124d73><a href="#1fc55849153c719e757bb6cba8124d73">7.3.6</a>: Databases for assets, inventory, etc</h3>
<h2 id=4f78d48397b0d75399cddbac6661aa4f><a href="#4f78d48397b0d75399cddbac6661aa4f">7.4</a>: * The more sources of authoritative data, the more data drift and non-alignment between the data (fields tracking similar but non-matching things, naming differences, not able to point to same primary keys, etc)</h2>
<h2 id=c60e4b0680418499aa5840cafca907a5><a href="#c60e4b0680418499aa5840cafca907a5">7.5</a>: Data survives longer than code/logic, business logic stays all the time, but the assets described in the DB remain the same, even if they are used differently, and different meta-data is stored about them.</h2>

# Chapter 8: The OpsDB






<h2 id=64bbdc8ed0e1e42739b42a4fc419e08e><a href="#64bbdc8ed0e1e42739b42a4fc419e08e">8.1</a>: What is it?</h2>
<h3 id=6d85b906bd9d454887125ebb31840c17><a href="#6d85b906bd9d454887125ebb31840c17">8.1.1</a>: Your OpsDB is the desires and actionable knowledge of your company.&nbsp;&nbsp;Everything inside it can be acted upon, it is better global information than any single person can have, so it is the best communication mechanism for a system that has multiple people with their own information (all companies over 1 employee).&nbsp;&nbsp;Synchronizes information, makes transactional.</h3>
<h3 id=f9918b64d4f419d98d2f8342088bea27><a href="#f9918b64d4f419d98d2f8342088bea27">8.1.2</a>: Setting realistic expectations for this project will be one of your biggest challenges.&nbsp;&nbsp;Once the premise is understood, it is difficult to stop "magical" thinking about the project, as the intention is to solve all solvable problems, people see it as a magic machine.</h3>
<h3 id=3140a4b8520344ef6af72c4b6709e379><a href="#3140a4b8520344ef6af72c4b6709e379">8.1.3</a>: It is a system or "machine" that can be used to solve all problems, in that it is a centralized database and method for acting against that data.&nbsp;&nbsp;That is immediately a universal set of tools, because every piece of software is data with a method for acting against it.</h3>
<h2 id=febf95c8835573c89a43474f25043f21><a href="#febf95c8835573c89a43474f25043f21">8.2</a>: Data Driven Design:&nbsp;&nbsp;My methodology.&nbsp;&nbsp;Start with the data, work from there.&nbsp;&nbsp;Testing against data is key.</h2>
<h3 id=addcf00c3304307ee3ec5717fab5c768><a href="#addcf00c3304307ee3ec5717fab5c768">8.2.1</a>: Separate data changing logic from non-data changing logic.&nbsp;&nbsp;This is like the Model/Controller separation, but is different because it is about any type of action, not just GUI-like actions.</h3>
<h3 id=63ca29ecfdbd33f8b82529d48bf7e2f6><a href="#63ca29ecfdbd33f8b82529d48bf7e2f6">8.2.2</a>: Work systems.&nbsp;&nbsp;Distributed Job schedulers.</h3>
<h3 id=b9188413cc8c6606506e014873b6b930><a href="#b9188413cc8c6606506e014873b6b930">8.2.3</a>: Collection of data:&nbsp;&nbsp;Events (logs/etc), Time Series, Config State (md5sum, etc), Active/Live State (up/down)</h3>
<h3 id=727550ddb6653e016e1496f196e288ac><a href="#727550ddb6653e016e1496f196e288ac">8.2.4</a>: Data Driven Development.&nbsp;&nbsp;My methodology.</h3>
<p id=c2f8690440b17c7c50567db20222ffe1><b><a href="#c2f8690440b17c7c50567db20222ffe1">8.2.4.1</a>: Start with data.&nbsp;&nbsp;Fo over all features as represented in data.</b></p>
<h2 id=f233ed09310a458264d313be344b885a><a href="#f233ed09310a458264d313be344b885a">8.3</a>: The Data (base)</h2>
<h3 id=b81585e0fda170c7250649704866ac0a><a href="#b81585e0fda170c7250649704866ac0a">8.3.1</a>: Modeling off of reality.&nbsp;&nbsp;Logical ideas change all the time, business decisions and directions change all the time, staff changes regularly, reality will hold true, but it's perceived differently by everyone.&nbsp;&nbsp;Still trying to map to reality gives the most common information to the most people who will work with it, and a common method of communication, and is therefore better than not.</h3>
<h2 id=eb0781821183170b505cc3d53ed8f810><a href="#eb0781821183170b505cc3d53ed8f810">8.4</a>: Naming conventions.&nbsp;&nbsp;Set them and try to abide by them consistently.&nbsp;&nbsp;This will determine how frequently things must be looked up to be used, for someone familiar with the sytem.&nbsp;&nbsp;Python vs PHP.</h2>
<h2 id=88eefb88d8bdddb29a06e49470b741b5><a href="#88eefb88d8bdddb29a06e49470b741b5">8.5</a>: My rules:&nbsp;&nbsp;No plurals in data (code is ok), strict lookup methods, limit methods of relationality.&nbsp;&nbsp;DAG lookups, with normalized relations in data (not-DAG, has cycles, data doesnt have a direction when there are cycles, the search could start anywhere).</h2>
<h2 id=580a184d5471cd2ae0aa2951fafffcee><a href="#580a184d5471cd2ae0aa2951fafffcee">8.6</a>: What tools you will need to manage this data.&nbsp;&nbsp; Problems with ORM, problems with non-ORMs.&nbsp;&nbsp;The tools chosen will determine the level of automatability.</h2>
<h2 id=af2c0408d1a232656d0845019e4790ef><a href="#af2c0408d1a232656d0845019e4790ef">8.7</a>: Building the logic system.</h2>
<h3 id=c587a72562db2e142ed7bce6ba82c2fb><a href="#c587a72562db2e142ed7bce6ba82c2fb">8.7.1</a>: Ensuring uniqueness of elements that require guarantees.</h3>
<h3 id=d02f1a4ff1c843265bfaa4d20accf4d0><a href="#d02f1a4ff1c843265bfaa4d20accf4d0">8.7.2</a>: Infrastructure.&nbsp;&nbsp;Pre-Services.</h3>
<h3 id=37233edbc6bbf446d6353f066766b5d4><a href="#37233edbc6bbf446d6353f066766b5d4">8.7.3</a>: Configuration of Services.</h3>
<h3 id=06bfc3797691d54fdd6e34c13c4e2ec3><a href="#06bfc3797691d54fdd6e34c13c4e2ec3">8.7.4</a>: Monitoring of Services.</h3>
<h3 id=e01a2cff836d04f498744d984298c363><a href="#e01a2cff836d04f498744d984298c363">8.7.5</a>: Life-Cycle Management of services.</h3>
<h2 id=2e7bd70786c580dcfbd4a9115bf0bb8f><a href="#2e7bd70786c580dcfbd4a9115bf0bb8f">8.8</a>: The layers of an automation system:</h2>
<h3 id=63b722744987837de93cab18cb980051><a href="#63b722744987837de93cab18cb980051">8.8.1</a>: Description of environment</h3>
<h3 id=cd394f4051b52bbe62e5ebb2cd8310ff><a href="#cd394f4051b52bbe62e5ebb2cd8310ff">8.8.2</a>: Provisioning</h3>
<p id=3ccd753ebf4dc31d41da2ddd58d657d6><b><a href="#3ccd753ebf4dc31d41da2ddd58d657d6">8.8.2.1</a>: One-Time configuration</b></p>
<p id=2ea0777930172d51b11974c4b9870340><b><a href="#2ea0777930172d51b11974c4b9870340">8.8.2.2</a>: Continuous Configuration</b></p>
<p id=60fee5b4808b14ad3b519f3642b92ba9><b><a href="#60fee5b4808b14ad3b519f3642b92ba9">8.8.2.3</a>: State management</b></p>
<p id=8959758dbd6b6f3cf8506033ed26a74e><b><a href="#8959758dbd6b6f3cf8506033ed26a74e">8.8.2.4</a>: One-time actions (manual state control of distributed systems)</b></p>
<p id=b7738190443498e5389dd4bb606b3213><b><a href="#b7738190443498e5389dd4bb606b3213">8.8.2.5</a>: Maintenance actions (taking offline)</b></p>
<p id=dc1141d3dbdaed262a31451319e4a0d6><b><a href="#dc1141d3dbdaed262a31451319e4a0d6">8.8.2.6</a>: Marking broken HW, fixing HW, migrating OS positions.</b></p>
<p id=dadcbabed40306c7ac679c0ce0715aca><b><a href="#dadcbabed40306c7ac679c0ce0715aca">8.8.2.7</a>: What stays the same, what changes?&nbsp;&nbsp;IPs for LOM on HW.&nbsp;&nbsp;IPs for OSes on virtual.</b></p>
<p id=47628abed8e1db8e9ed815f84bb4d116><b><a href="#47628abed8e1db8e9ed815f84bb4d116">8.8.2.8</a>: Tracking N things.&nbsp;&nbsp;Primaries vs. position.&nbsp;&nbsp;Ordered lists are the best?</b></p>
<h2 id=c5e3fc0965c2fdd764070ce7089ab03e><a href="#c5e3fc0965c2fdd764070ce7089ab03e">8.9</a>: How to "translate" data changes, making many changes at once, like matrix multiplication.&nbsp;&nbsp;Changing from Puppet to Salt, etc.</h2>
<h2 id=1431f5a1f11b9fb451cc24ff2fee85c5><a href="#1431f5a1f11b9fb451cc24ff2fee85c5">8.10</a>: How to Build your own OpsDB.&nbsp;&nbsp;What you need:</h2>
<h3 id=9853534dc81b1e9e41d72d4363f0a542><a href="#9853534dc81b1e9e41d72d4363f0a542">8.10.1</a>: View (Webpage, API)</h3>
<h3 id=276746c8ba1e2809eb7df2308d002381><a href="#276746c8ba1e2809eb7df2308d002381">8.10.2</a>: DB Backend</h3>
<p id=ff326af388f41f4924ffad21eb1dfed3><b><a href="#ff326af388f41f4924ffad21eb1dfed3">8.10.2.1</a>: Method for safely making changes to data</b></p>
<p id=036106589f472c34b5d06d007dea3f2b><b><a href="#036106589f472c34b5d06d007dea3f2b">8.10.2.1.1</a>: Versioning, Change Management</b></p>
<p id=1cdc99a3dfdde59fb854db0175cb63c4><b><a href="#1cdc99a3dfdde59fb854db0175cb63c4">8.10.2.1.1.1</a>: Roll backs</b></p>
<p id=c49dd8f1c6c2c694c834e61f716fb0fa><b><a href="#c49dd8f1c6c2c694c834e61f716fb0fa">8.10.2.1.1.2</a>: Pre-Post Commits</b></p>
<p id=0e83ef919a005decfa42731ac7f54b07><b><a href="#0e83ef919a005decfa42731ac7f54b07">8.10.2.1.1.3</a>: Locking, to stop problematic race conditions</b></p>
<p id=019b9ff6745a81e4c068d893c7f13852><b><a href="#019b9ff6745a81e4c068d893c7f13852">8.10.2.1.1.3.1</a>: Channeled locking, to limit domains of locks</b></p>
<p id=80bc1f096de2420328753be58a57dceb><b><a href="#80bc1f096de2420328753be58a57dceb">8.10.2.1.1.3.1.1</a>: Size of domain, and rate of change and lock duration determine requirements</b></p>
<p id=5d14c394196a168616acd71cd98b3e1d><b><a href="#5d14c394196a168616acd71cd98b3e1d">8.10.2.1.2</a>: Single choke point for DB changes</b></p>
<p id=b0cb8e8e7ef02730d62e746be34c4735><b><a href="#b0cb8e8e7ef02730d62e746be34c4735">8.10.2.1.2.1</a>: Web/API all use the same code, so different paths give different results.</b></p>
<p id=f17e11f935b8c1a4aa11102e9f73223e><b><a href="#f17e11f935b8c1a4aa11102e9f73223e">8.10.2.1.2.2</a>: Role users (scripts) can auto-commit changes, but should go through same process, because needed for auditing, troubleshooting, and maintaining integrity and pre/post-commit logic</b></p>
<h3 id=540cf17fe6e0e04bd037e55d7ce2f5ce><a href="#540cf17fe6e0e04bd037e55d7ce2f5ce">8.10.3</a>: Pull method, to gather data.&nbsp;&nbsp;Time Series, Logs, State/Configs, Events, etc</h3>
<p id=c4337517e5ddb7098a69ab9ea06a54fe><b><a href="#c4337517e5ddb7098a69ab9ea06a54fe">8.10.3.1</a>: Creates Global Authority DB</b></p>
<p id=a12e034abf7648e012dba8f6624f26f3><b><a href="#a12e034abf7648e012dba8f6624f26f3">8.10.3.1.1</a>: Can be distributed, if sync. is strong</b></p>
<p id=462d69372dfef02a563fa6444c55cd24><b><a href="#462d69372dfef02a563fa6444c55cd24">8.10.3.1.1.1</a>: Need Transactions on all pieces of total DB, so that things are changed in block fastion, all this way, then all that way.&nbsp;&nbsp;Keeping alignment.&nbsp;&nbsp;(Like a shot in Pool, game.&nbsp;&nbsp;Stick and balls must line up to make it into the pocket.)</b></p>
<p id=277518558b3f7c13c97da337398a3239><b><a href="#277518558b3f7c13c97da337398a3239">8.10.3.1.1.2</a>: Will come later in the process, in the "How to implement" section</b></p>
<p id=dc439f9efa60e2ef3a3b7a76233e90b4><b><a href="#dc439f9efa60e2ef3a3b7a76233e90b4">8.10.3.1.2</a>: Selective Replication.&nbsp;&nbsp;Will have local and global portions.&nbsp;&nbsp; Easy to separate instances (2 MySQL instances) so taht there is a Global DB (replicated from Master) and a Local DB, pulled from Local, which replicates to Master.</b></p>
<p id=36da14c0258aed53bb129e50b7540c0b><b><a href="#36da14c0258aed53bb129e50b7540c0b">8.10.3.1.2.1</a>: In this scenario, the Master will need to have N instances, where N is the number of sub-masters, so it can replicate.&nbsp;&nbsp;Then it will pull and integrate this data into it's own global system, and then synthesize.</b></p>
<p id=8a7a7c7b2388bd544de92c5e305fac1b><b><a href="#8a7a7c7b2388bd544de92c5e305fac1b">8.10.3.1.2.1.1</a>: This Global pull-integrate-synthesize is then replicated out everywhere, and is the REAL data that can be acted upon.&nbsp;&nbsp;It has met all constraints and has a view into everything</b></p>
<p id=acd4663d59d1c72e97ec62dfc8144a85><b><a href="#acd4663d59d1c72e97ec62dfc8144a85">8.10.3.1.2.1.1.1</a>: Some Logic can run off of Local data, because it is locally concerned.&nbsp;&nbsp;When Logic needs to act on Global data, its obvious it needs to be correct and current global data.&nbsp;&nbsp;Intelligence.</b></p>
<p id=bed7228195793a630892b855fc99a256><b><a href="#bed7228195793a630892b855fc99a256">8.10.3.1.2.2</a>: Collection is local.&nbsp;&nbsp;Work from Global.</b></p>
<p id=87f7c87b586607ad6a5f02b42dbc6fd9><b><a href="#87f7c87b586607ad6a5f02b42dbc6fd9">8.10.3.1.2.2.1</a>: How to work on partitioon?</b></p>
<p id=d7f9ae8a09db2ce495f7b9c3de1765c2><b><a href="#d7f9ae8a09db2ce495f7b9c3de1765c2">8.10.3.1.2.2.1.1</a>: Can use local data for N time, until is stale.&nbsp;&nbsp;Logic can decide how stale the data can be, can have Rules for lag time allowances.</b></p>
<h3 id=a00ef370998cbb3006289af9b995a5b9><a href="#a00ef370998cbb3006289af9b995a5b9">8.10.4</a>: Orchestration.&nbsp;&nbsp;Remote Execution.&nbsp;&nbsp;Seall the loop and check.&nbsp;&nbsp;Post-Provisioning will need to run commands to check that things really worked.&nbsp;&nbsp;Same as any other type of action. Do the action, get the result, but then go check and make sure it worked.&nbsp;&nbsp;Check again to see if it failed after some time.&nbsp;&nbsp;Ensure another action hasnt caused this (acted on the same Resource)</h3>
<h3 id=db268b9d5648f3cf17247aa4466aca44><a href="#db268b9d5648f3cf17247aa4466aca44">8.10.5</a>: Config Management.&nbsp;&nbsp;Make known changes on a system.&nbsp;&nbsp;It should be in "X state"</h3>
<h3 id=0a8618fa5985ed1fdc24f110dc27c026><a href="#0a8618fa5985ed1fdc24f110dc27c026">8.10.6</a>: State Management.</h3>
<p id=8b695cbf41a4ec0c65cc346d3f4ec397><b><a href="#8b695cbf41a4ec0c65cc346d3f4ec397">8.10.6.1</a>: OS Level</b></p>
<p id=13c2c758c5deddeef82f376abc18fd9d><b><a href="#13c2c758c5deddeef82f376abc18fd9d">8.10.6.2</a>: Service level (dealing with the execution of services, and proper functionoining of the service)</b></p>
<p id=c4dcd142e927de912d9547bc2fdc0b04><b><a href="#c4dcd142e927de912d9547bc2fdc0b04">8.10.6.3</a>: Running-Service level (dealing with things inside a running service.&nbsp;&nbsp;This is a user of the service, instead of a controller, but it is an "administrative" type of use)</b></p>
<h3 id=dd58ffaa4ecbdac2411f233050464747><a href="#dd58ffaa4ecbdac2411f233050464747">8.10.7</a>: Work Scheduling</h3>
<p id=a70b03745f8075613c39c401fa6ebb3c><b><a href="#a70b03745f8075613c39c401fa6ebb3c">8.10.7.1</a>: Global cron jobs, etc.</b></p>
<p id=1ba95b39f638a0a938fe583f13451394><b><a href="#1ba95b39f638a0a938fe583f13451394">8.10.7.1.1</a>: In maint?&nbsp;&nbsp;Is right machine (master/slave/role/etc)?&nbsp;&nbsp;Dont take down prod.</b></p>
<p id=b0daa3658be541aa293ab0b9ded206da><b><a href="#b0daa3658be541aa293ab0b9ded206da">8.10.7.1.2</a>: Dont ignore failures of jobs.&nbsp;&nbsp;Keep logs for auditing, so we know what happened, and what it happened for troubleshooting and Root Cause Analysis.</b></p>
<p id=0044ef67424877e39c1ba3c6053e8c31><b><a href="#0044ef67424877e39c1ba3c6053e8c31">8.10.7.1.3</a>: Track times for analysis to determine failures of scale-performance changes</b></p>
<h3 id=fb473bfadfe142c63f22f088a56d5977><a href="#fb473bfadfe142c63f22f088a56d5977">8.10.8</a>: Capacity Planning.&nbsp;&nbsp;When will you run out of:&nbsp;&nbsp;Disk? RAM?&nbsp;&nbsp;CPU? Connections?&nbsp;&nbsp;etc</h3>
<p id=0c6c6113cb02a2a1ff6e897237e5402b><b><a href="#0c6c6113cb02a2a1ff6e897237e5402b">8.10.8.1</a>: Resources of our services.&nbsp;&nbsp;Network Loadbalancer has N potential connections, and we can determine that by a MAX check on how much its done, and where it has produced failures after MAX_WORKING values have been breached.&nbsp;&nbsp;Might not be the LB though, just correlation.</b></p>
<h3 id=a6e21acd13a2849ee9c611451ba8b30a><a href="#a6e21acd13a2849ee9c611451ba8b30a">8.10.9</a>: Access Control.&nbsp;&nbsp;Authorization to do work.</h3>
<h3 id=becd8bbe6534ed50063f3c3345ad5e51><a href="#becd8bbe6534ed50063f3c3345ad5e51">8.10.10</a>: Security zones</h3>
<p id=6ed06f2275ddd84dd98eb2bdea49c011><b><a href="#6ed06f2275ddd84dd98eb2bdea49c011">8.10.10.1</a>: Environments and Security Zones</b></p>
<br>
<br>
Environments are natural Security Zones, because we have a goal in mind for everything inside an Environment, so everything has a similar base set of Security Requirements, and therefore a Security Posture that is required.<br>
<p id=d6deb64dba22f963c4a9b01b99beecb8><b><a href="#d6deb64dba22f963c4a9b01b99beecb8">8.10.10.2</a>: Tiered Security Zones</b></p>
<br>
Let's make a map of what tiers we could have in security zones.<br>
<br>
- Tier 1: Member of the organization.&nbsp;&nbsp;Employee or outsider?<br>
<br>
The first tier will simply be a boolean of whether a person is a member of the organization in question.&nbsp;&nbsp;"Do you work for us?"<br>
<br>
This is a basic question of insider vs. outsider.&nbsp;&nbsp;This tier can have additional children tiers for all departments and groups in an organization, as wall as professional rank, such as Vice President (VP) vs. Engineer will be two different levels of tiered security in the employee category.<br>
<br>
This has blurred lines for Contractors, Consultants, Vendors and Partners.<br>
<br>
Contractors are paid as work-for-hire "employees", without the employee benefits.&nbsp;&nbsp;This is usually focused on individuals that are contracted for work, but sometimes is a separate organization who is contracted (usually for lower level work, or non-core services).&nbsp;&nbsp;Contractors will usually have similar access to employees at their same level, with perhaps some additional restrictions to making changes or seeing sensitive information.<br>
<br>
Consultants are short-term or contracted for specific work, and often for informational work, rather than manual labor type work (including technical manual labor, like writing code in this).&nbsp;&nbsp;Consultants are often given very limited access to a company's data and resources, as they have a specific task to perform which does not need general employee-level access.<br>
<br>
Vendors are organizations who sell software, hardware or services to an organization, and are not associated with any individuals.&nbsp;&nbsp;Vendors are generally not given any access to data or resources, except in the case of special technical support investigations, which are rare and may still not be allowed by organizations who are serious about security.<br>
<br>
Partners are a mix between contractors, consultants and vendors.&nbsp;&nbsp;They may be a Vendor, which is making a co-sponsored project with your organization, and so they need limited access to all relevant project data and may need resource access to test integration.&nbsp;&nbsp;Partner employees may be given contractor or consultant level access, depending on the partnership goals and time lines.<br>
<br>
- Tier 2: Environment level.&nbsp;&nbsp;Production, staging, QA, development?<br>
<br>
This is a statement of a basic operational environment.&nbsp;&nbsp;Where are you?&nbsp;&nbsp;What are you allowed to do here?<br>
<br>
Described thoroughly here: {{ section_10c0b236af1081d0c601a87fb274211c }}<br>
<br>
- Tier 3: Location level.&nbsp;&nbsp;Specific datacenter in a Tier 2 environment.<br>
<br>
Inside of a Production Environment, you might be in Data Center #1, which may have some different rules from Data Center #2, because the build-outs were done at different times, or different resources are located in each of them.<br>
<br>
- Tier 4: Resource level.<br>
<br>
Inside of a Tier 2 environment (and maybe Tier 3), there will be special resources, such as a database that stores Personal Identification Information (PII), or credit card information (PCI), etc.<br>
<br>
For these special resources they may need additional sub-environmental security zones, such as internal DMZs (ie: "de-militarized zones", which is like a security "draw-bridge" or "fire-wall" area).&nbsp;&nbsp;<br>
<br>
This could also be external DMZs, which are used for services that take external requests which may be considered "more dangerous" or otherwise having a different security posture requirement, which is placed into a separate special area of the network.&nbsp;&nbsp;This allows for example a place to put a file-server that is accessible by partners or vendors, but if compromised does not give privileged access into the Production network.<br>
<br>
Roughly these 4 tiers break down into:<br>
<br>
- Authentication, authorization:&nbsp;&nbsp;"Are you one of us?"<br>
- Operational Environment:&nbsp;&nbsp;"What do we want to happen at this point?"<br>
- Specific Location:&nbsp;&nbsp;"What do we do in this location that is special?"<br>
- Resource specific: "Is the specific resource in question special?"<br>
<p id=70a1fe53dd9bfa2e1dea47c2e80559ff><b><a href="#70a1fe53dd9bfa2e1dea47c2e80559ff">8.10.10.3</a>: Security Zones Inside Environments</b></p>
<h3 id=e3cba7be54f69ef1b2d51192e0ef633e><a href="#e3cba7be54f69ef1b2d51192e0ef633e">8.10.11</a>: Deployments, as separate from Config</h3>
<p id=f05b48f95386109c5c79cfc128fc44e3><b><a href="#f05b48f95386109c5c79cfc128fc44e3">8.10.11.1</a>: Code deploy</b></p>
<p id=1d1be487a8a4d497425c60ca93d25285><b><a href="#1d1be487a8a4d497425c60ca93d25285">8.10.11.2</a>: Data/Schema deploy</b></p>
<p id=f08b1ca1ab0f2290f2a2c3b8b8b97ffc><b><a href="#f08b1ca1ab0f2290f2a2c3b8b8b97ffc">8.10.11.2.1</a>: When tied together.&nbsp;&nbsp;Ways to avoid problems, ways to increase problems.</b></p>
<p id=ed24cd5011374fb609ff91ea5d18cc17><b><a href="#ed24cd5011374fb609ff91ea5d18cc17">8.10.11.2.2</a>: Lifetimes, rate of change, etc</b></p>
<p id=88ff2ffdc4b027db0a400a53602c0063><b><a href="#88ff2ffdc4b027db0a400a53602c0063">8.10.11.2.3</a>: Service up/down.&nbsp;&nbsp;In/out of LB.&nbsp;&nbsp;(Active)</b></p>
<h3 id=938f106673899a434d955e75ed15a20a><a href="#938f106673899a434d955e75ed15a20a">8.10.12</a>: Network config and planning</h3>
<p id=95c64ed20fa4a1dbb04c67f0aea42b82><b><a href="#95c64ed20fa4a1dbb04c67f0aea42b82">8.10.12.1</a>: VLANs.&nbsp;&nbsp;Hidden systems, ensure not old IPs (collisions)</b></p>
<p id=19579404710a661869e4eea32f5e1c96><b><a href="#19579404710a661869e4eea32f5e1c96">8.10.12.1.1</a>: Can defer their use until that HW is proven to not use that IP anymore.&nbsp;&nbsp;Like its in Escrow.&nbsp;&nbsp;Once really released, it can be re-used.&nbsp;&nbsp; Nice.</b></p>
<p id=8307c8ed240946f143913fa06d1021f4><b><a href="#8307c8ed240946f143913fa06d1021f4">8.10.12.2</a>: LOM IPs stay with the hardware.&nbsp;&nbsp;DHCP timeouts, etc.&nbsp;&nbsp;Server IPs stay with "ServerInstance" (OSInstance)</b></p>
<h3 id=203ffd1d4778494bd7a2556c2a0ac90e><a href="#203ffd1d4778494bd7a2556c2a0ac90e">8.10.13</a>: VM Provisioning.&nbsp;&nbsp;Hybrid.</h3>
<h3 id=f7ae4f5ab54c3927652049bdcf35e555><a href="#f7ae4f5ab54c3927652049bdcf35e555">8.10.14</a>: Self Service tools.</h3>
<h3 id=276b07fae87391ca794e8587e972cf4e><a href="#276b07fae87391ca794e8587e972cf4e">8.10.15</a>: How to plan to do this in your existing environment.&nbsp;&nbsp;A map from:&nbsp;&nbsp;Here -> There.</h3>
<h2 id=dc9b1c51ebd041941929fe8845a2c78e><a href="#dc9b1c51ebd041941929fe8845a2c78e">8.11</a>: States of machines:&nbsp;&nbsp;Unknown, Unprovisioned/Spare, Provisioned-Inactive, Active, In Maintenance, Transition-To X State, Broken, Fixed (waitig to be Unprovisioned/Spare)</h2>

# Chapter 9: How to Implement the OpsDB in your Current Environment






<h2 id=4e188beb6a9e453253679bb857ac7767><a href="#4e188beb6a9e453253679bb857ac7767">9.1</a>: The OSI layer for getting things done:</h2>
<h3 id=458b9365b935744307dce791d0f73ea6><a href="#458b9365b935744307dce791d0f73ea6">9.1.1</a>: Physical.&nbsp;&nbsp;Real world things.</h3>
<p id=7543ac663d8be861d64b607357cbc148><b><a href="#7543ac663d8be861d64b607357cbc148">9.1.1.1</a>: People are always required for real world things, because robots arent good enough yet.&nbsp;&nbsp;Physical must manage physical.</b></p>
<h3 id=a782fd2d1471fc65afd9abcdc78c14ed><a href="#a782fd2d1471fc65afd9abcdc78c14ed">9.1.2</a>: Configuration.&nbsp;&nbsp;How real world things are configured.</h3>
<p id=719bc5f15fa7d54e8a67977bf0901094><b><a href="#719bc5f15fa7d54e8a67977bf0901094">9.1.2.1</a>: Logical.</b></p>
<h3 id=6331cb83195fd5b2bd738c89abc4ec84><a href="#6331cb83195fd5b2bd738c89abc4ec84">9.1.3</a>: State.&nbsp;&nbsp;How real world things are managed.</h3>
<p id=719bc5f15fa7d54e8a67977bf0901094><b><a href="#719bc5f15fa7d54e8a67977bf0901094">9.1.3.1</a>: Logical.</b></p>
<h3 id=b53ddf4dc4025191a641f212d24e1be3><a href="#b53ddf4dc4025191a641f212d24e1be3">9.1.4</a>: Automation.&nbsp;&nbsp;How software can manage configuration and state.</h3>
<p id=32f7e1e930dc786f657dc6a88b1bbde3><b><a href="#32f7e1e930dc786f657dc6a88b1bbde3">9.1.4.1</a>: Automation ends where people begin.&nbsp;&nbsp;If you have no automation, the people manage the config and state.</b></p>
<p id=95e40183969996603b8e5e3425a932c4><b><a href="#95e40183969996603b8e5e3425a932c4">9.1.4.2</a>: Automation is the control of logical devices and state.&nbsp;&nbsp;It does not control Physical devices, but does control their state.&nbsp;&nbsp;(Even in the case of directing a physical robot, the automation updates state, and it takes something physical (motors, servos, cogs) to make the physical thing move.)</b></p>
<h3 id=173c2bec1142197f6757fcb7d4a8dbbf><a href="#173c2bec1142197f6757fcb7d4a8dbbf">9.1.5</a>: Process (and Procedures).&nbsp;&nbsp;How people work around the lower levels.</h3>
<h3 id=8e203f62002cbf6f27b191f991da6f30><a href="#8e203f62002cbf6f27b191f991da6f30">9.1.6</a>: Policy.&nbsp;&nbsp;Dictates how processes can be implemented.&nbsp;&nbsp;Policies may be directly contradicting Process, such as "No one is allowed to X", while a process requires a person to do exactly that.</h3>
<h3 id=7fdcde9fe4218f5aa5a0a40cc5501fbd><a href="#7fdcde9fe4218f5aa5a0a40cc5501fbd">9.1.7</a>: Business...&nbsp;&nbsp;Business goals</h3>
<h3 id=9fe2a787f3e54166e4252165680a59d2><a href="#9fe2a787f3e54166e4252165680a59d2">9.1.8</a>: Political.&nbsp;&nbsp;The realities of the business goals, determined by how well people will work together to achieve them.</h3>
<h3 id=3ff1735de8bc414c4f645abe641ad297><a href="#3ff1735de8bc414c4f645abe641ad297">9.1.9</a>: Financial...&nbsp;&nbsp;Financial reality, approved or not.&nbsp;&nbsp;Timing.&nbsp;&nbsp;Delays.</h3>
<h3 id=b982d3de81bba13dd46914991650f426><a href="#b982d3de81bba13dd46914991650f426">9.1.10</a>: Legal...&nbsp;&nbsp;Hard stop, must change direction if told by legal.</h3>
<h2 id=3f2cc3566a84cad0a234647ab1300021><a href="#3f2cc3566a84cad0a234647ab1300021">9.2</a>: Planning for projects in the real world</h2>
<h3 id=236e9bb833a610161cfbaaba9e6bb6fe><a href="#236e9bb833a610161cfbaaba9e6bb6fe">9.2.1</a>: The end-date comes first.&nbsp;&nbsp;Whether you have any say in that is only occassionally true, even if you are asked how long it will take.</h3>
<h3 id=cba0d1f4cdd7b395395d6b34e6523e97><a href="#cba0d1f4cdd7b395395d6b34e6523e97">9.2.2</a>: Things will interrupt your work that were not planned for in the time estimates, and this will mean less work gets done</h3>
<h3 id=c7eec3bac3f711b65028b49170529559><a href="#c7eec3bac3f711b65028b49170529559">9.2.3</a>: You will have normal duties to attend to, this will interrupt things getting done</h3>
<h3 id=c2a0b4944f0d52aaec4ba066f1860790><a href="#c2a0b4944f0d52aaec4ba066f1860790">9.2.4</a>: Meetings.&nbsp;&nbsp;Whether you enjoy them, are ambivalent, or dislike them, they are going to occur and take time.</h3>
<h3 id=05c0e353e04741273d56999b7e33a595><a href="#05c0e353e04741273d56999b7e33a595">9.2.5</a>: Mental-Context-switching cost.&nbsp;&nbsp;Ramp up time.</h3>
<p id=d14a0f795ad0930b2ab59e40ff6742b4><b><a href="#d14a0f795ad0930b2ab59e40ff6742b4">9.2.5.1</a>: Know what kind of work you are going to start, and pick the best time to do so.&nbsp;&nbsp;If it needs more ramp-up time, then pick a block where you are less likely to be interrupted.</b></p>
<p id=ca064b32d34547ac269d1b85fa693e6d><b><a href="#ca064b32d34547ac269d1b85fa693e6d">9.2.5.2</a>: Break your open time periods into "units" of 30 minutes or 2 hours or whatever you can have contiguously, and see what you can FINISH in that time.&nbsp;&nbsp;It is easy to lose days/weeks to getting little changes made, but not moving ahead in terms of usable progress.</b></p>
<p id=ae9af424cff9e20bb4d775d699db9e81><b><a href="#ae9af424cff9e20bb4d775d699db9e81">9.2.5.2.1</a>: When each time block arrives, try to get what you can finish, and hopefully test and put into place, in that 1 session.&nbsp;&nbsp;This isnt possible for some work, because it's too big, so break that into stages that can fit into one of these time blocks.&nbsp;&nbsp;A simple method, would be: write it in 1, test it in another, and finally deploy it in the 3rd.</b></p>

# Chapter 10: Planet Scale Automation


[Placeholder for the time being, just to briefly explain]



UM = Function + Side Effects = A method for describing any individual action



UMC = Universal Machine Context.  A label for a set of UMs.  These are actions that are all related to each other, so all UMs in a UMC can be said to be on the same "layer".



UMCR = UMC Relationship.  A mapping from either an input, output or effect, from one UMC UM to another UMC UM.  This is described *as* a UM.  The set of all UMCRs between two UMCs is itself a UMC.  The UMC of the relationship between the two UMCs.



In this way, all functions can be mapped, for any "context" or "layer", and then all contexts/layers can be mapped, and then all relationships between all contexts and layers can be mapped.



Does this need to be taken to it's extreme with a full-mesh mapping?  No.



It is only important that we have a mechanism for how to link the different layers we will eventually end up creating together under a scalable and simple system, which this is.  I believe there is probably no simpler system that can be invented to describe this set of complex relationships together, because there is a minimal set of data being tracked.



One would have to track less data, and do the same or more work to create a better effect, so I can state I believe this is currently an optimal solution for the present understanding of how we could scale to full-mesh style sizes of Planet Scale Automation.









<h2 id=89e9cad9ead3a66e01d0bae846f5659b><a href="#89e9cad9ead3a66e01d0bae846f5659b">10.1</a>: Universal Machines as infinite recursive abstraction</h2>
<br>
<br>
[Fill out...]<br>
<br>
How this works:&nbsp;&nbsp;<br>
<br>
UMCs are different "Pies" in the "Slicing the Pie" concept, but they are all the same "Pie".<br>
<br>
So you can slice the same Pie up in one UMC.<br>
<br>
Then in another UMC you make different slices to the same pie.<br>
<br>
This is why UMCs and UMCRs are needed, in that you still only have "One Pie", but you want to track one Set-Of-Slice from another Set-Of-Slices, and then map the relationships between all the sliced pieces and stuff.<br>
<br>
This is obvious when you think about Planetary Scale.<br>
<br>
We only have 1 Planet we are dealing with (for now, and then its the same thing all over, no change for Universal Scale Automation, or Multi-Versal Scale Automation), or whatever).<br>
<br>
We have 1 Planet now, and we can slice that pie up in lots of ways.&nbsp;&nbsp;But do we really think that a single "set" of slices will be good enough to describe automating the entire planet?<br>
<br>
Of course not, we have so many different viewpoints on things that we will need many "contexts" into this, which is exactly what UMCs are.&nbsp;&nbsp;They are the mappings to contexts, of all the ways of seeing the "slice-the-pie" method of understanding and controlling something, as big as a Planet/Universe/etc, and also being able to map with deterministic and accurate precious between those different contexts, with the best information available to you to do so (since some concepts may not map cleanly, and results will be accordingly "less good").<br>
<h2 id=46ed9a6f00444101408c655cfb39cf12><a href="#46ed9a6f00444101408c655cfb39cf12">10.2</a>: Single Layer Systems</h2>
<br>
The entire "OpsDB" as it has been presented in this book can be considered a single "context" or "layer" system because it was created so that all pieces were equal, relational, and shared a place with each other under concepts like Don't Repeat Yourself (DRY), and other methodologies so that there would not be overlaying contexts.<br>
<br>
This would be different in a situation where an existing legacy system already existed, and the OpsDB was created in parallel, and they both had to share their work.<br>
<br>
However, in this last case it is unlikely you would want to create two UMCs, because the OpsDB will become the dominant system, and the legacy system will be deprecated, so there is no reason to spend the time mapping between them with UMs.<br>
<br>
If both systems were required, because of some requirement, and you wanted to maintain the different contexts independently, but wanted them to work together, or through each other's interfaces (so that there was a single-operator for any given task), then a sub-set of UMCRs would be required to map the two contexts together.<br>
<br>
Generally, you will want to aim for a single-layer system because it is simpler, and requires less work to design and maintain, but if you find that you must have more complexity or complicated systems because of your requirements, then you can use the UM/UMC/UMCR methods to recursively cover all the differences between them in a comprehensive manner, if you implement the interfaces accurately.<br>
<h2 id=29b43af5a912570685fa7d00e13a1509><a href="#29b43af5a912570685fa7d00e13a1509">10.3</a>: Multi-Layer Systems</h2>
<br>
<br>
If comprehensive automation systems can be created as a Single-Layer System, than why would we ever need Multi-Layer Systems?<br>
<br>
Why can't OpsDB scale into a Planet Scale Automation system without UMCs and UMCRs?<br>
<br>
The reason is that OpsDB is taking a look at the data from a strictly virtual perspective.&nbsp;&nbsp;It maps to physical devices, hardware and physical locations of things, and other physical attributes and issues, but it is primarily a logical system for controlling logical elements, which simply map to physical elements.<br>
<br>
But, if one wants to automation an entire Planet's worth of infrastructure, then one is going to have to take many different perspectives than the one we have settled on for the OpsDB.<br>
<br>
There will be many different views of these systems, which are in themselves just as valid as the OpsDB view, but do not mesh well with the intent of the OpsDB layout as I have described it here.<br>
<br>
In essence, these will be new OpsDBs, written in the same method as the OpsDB I have laid out, but with very different goals and requirements, so that the current OpsDB has it's purpose, and so do these additional supplementary OpsDBs.<br>
<br>
So, how can they all work together, in a way where things don't break, and they don't fight over resources (race conditions), and their different views of the systems, can be integrated together.<br>
<br>
This is where the UMCs and UMCRs come into play.<br>
<br>
Your logical OpsDB for controlling your system is a UMC, and your other OpsDB for meeting your other goals is another UMC, and the UMCRs connect them and allow them to work together, with their different views, but in complementary and non-conflicting ways.<br>
<h2 id=2829f790c87aab7f136a97f515a3c8d0><a href="#2829f790c87aab7f136a97f515a3c8d0">10.4</a>: N-M-... Layer Systems</h2>
<br>
<br>
Give examples of how we would need different systems that work together, and brief mappings between them.<br>
<br>
Use things like physical infrastructure, gas or electrical delivery grids, etc.<br>

# Chapter 11: General Advice






<h2 id=0a605e177cdf62b2e4fd820e73cbecf7><a href="#0a605e177cdf62b2e4fd820e73cbecf7">11.1</a>: Go over code reviews, and config reviews.</h2>
<h3 id=a720022abaff2d1c9e31daf42dc94dee><a href="#a720022abaff2d1c9e31daf42dc94dee">11.1.1</a>: *** Mark this as my personal opinion.&nbsp;&nbsp;Not as something provable.&nbsp;&nbsp;This is color. ***</h3>
<h3 id=3519e134dd26a81e963ccf09964c8a88><a href="#3519e134dd26a81e963ccf09964c8a88">11.1.2</a>: Normal pitfalls.&nbsp;&nbsp;Dont really check, "Yes Stamp".</h3>
<p id=7cfef0cbf3e4fb479b3309647eb17ca6><b><a href="#7cfef0cbf3e4fb479b3309647eb17ca6">11.1.2.1</a>: Too style oriented.&nbsp;&nbsp;Enforcing a style is important in some areas, but less important in others.&nbsp;&nbsp;It is better to keep a team cohevsive to know these differences, so that on some things you are strict (variable naming) and on other things you are flexible (commenting style).&nbsp;&nbsp;People write prose more personally than they name variables, and variables have to be used by many people, whereas the message in a comment in based on the author's mental state when they wrote it, which is very subjective, and people have very different styles.</b></p>
<p id=3caece8edc80e43f05cec661ae0cf2f7><b><a href="#3caece8edc80e43f05cec661ae0cf2f7">11.1.2.1.1</a>: I recommend allowing people to have their own unique style in areas that will not harm the ease-of-use and resiliency/robustness of the Logic, and strictness on naming conventions, and basic formatting (indentation)</b></p>
<p id=8923934b9a6ece208968c72ceb0460c4><b><a href="#8923934b9a6ece208968c72ceb0460c4">11.1.2.1.1.1</a>: Strictness can be kept inside individual projects, with a general theme to a department or company.&nbsp;&nbsp;These are degrees to each of this which will make actually working with other people nicer, while</b></p>
<h2 id=fa154a30257b81d67d9e7c7114d4c549><a href="#fa154a30257b81d67d9e7c7114d4c549">11.2</a>: Root Cause Analysis write ups.</h2>
<h3 id=57a8fb171628609c4f4a074359da7864><a href="#57a8fb171628609c4f4a074359da7864">11.2.1</a>: How to not bullshit these.&nbsp;&nbsp;Dont lie.&nbsp;&nbsp;Dont criticize every failure, because failures WILL happen.&nbsp;&nbsp;The only way to avoid them is to REMOVE the CLASS OF WORK.</h3>
<h2 id=676e5f44878bdde31c3379f2c69b98ae><a href="#676e5f44878bdde31c3379f2c69b98ae">11.3</a>: Create a set of Checklists.</h2>
<h3 id=508068aefcdc803e5f88092d9cafbbf5><a href="#508068aefcdc803e5f88092d9cafbbf5">11.3.1</a>: Automation Spectrum</h3>
<h3 id=47245b1f66b268d9bf3e915e19d7106e><a href="#47245b1f66b268d9bf3e915e19d7106e">11.3.2</a>: Automation Layers</h3>
<p id=4d89acb0c6cf7d6c14c7c9925ffee864><b><a href="#4d89acb0c6cf7d6c14c7c9925ffee864">11.3.2.1</a>: Sub-Components of layers.&nbsp;&nbsp;How well are they implemented, 1-5 scale or something</b></p>
<h3 id=10909577585a58647fbb1902112b6ab3><a href="#10909577585a58647fbb1902112b6ab3">11.3.3</a>: Talk about how to make your own checklists and scales.&nbsp;&nbsp;This is flexible, not dogmatic.&nbsp;&nbsp;The important part is that we can communicate what we are talking about, in a way where multiple individuals and groups can agree, allowing us to work successfully together.</h3>
<h2 id=0109e0d4643177fefe7ccc3fe1c7a872><a href="#0109e0d4643177fefe7ccc3fe1c7a872">11.4</a>: Self-evaluation?&nbsp;&nbsp;How to evaluate your actions, how to make plans to improve.</h2>
<h2 id=90ee09235d729b6403260561482812a7><a href="#90ee09235d729b6403260561482812a7">11.5</a>: Introduce the Basic Laws of Human Stupidity.&nbsp;&nbsp;Not meant as insult or joke, but as quantitative method of determining the intelligence of an action.&nbsp;&nbsp;This is the model I will use in this book.</h2>
<h2 id=7f0428bc4e8fd20bc8ddd31b00ea1d75><a href="#7f0428bc4e8fd20bc8ddd31b00ea1d75">11.6</a>: Journmanship, apprenticeship.&nbsp;&nbsp;What we are missing.&nbsp;&nbsp;Valuing experience.&nbsp;&nbsp;Im old, of course thats my take.</h2>
<h2 id=5ca3d14cd4988a84227bb91b9f59650b><a href="#5ca3d14cd4988a84227bb91b9f59650b">11.7</a>: The benefits of "vanilla" use of tools.&nbsp;&nbsp;Less upkeep.&nbsp;&nbsp;Only change what you strictly need to change.&nbsp;&nbsp;Spend time optimizing only in critical areas.&nbsp;&nbsp;Reduce things that need to be manually maintained.</h2>
<h2 id=cc2951537c1aa0cd251fbda6639f2b8f><a href="#cc2951537c1aa0cd251fbda6639f2b8f">11.8</a>: "Lowest Common Denominator" problem</h2>
<br>
In response to: http://euphoricus.blogspot.com/2015/11/everybody-is-doing-tdd-take-two.html<br>
<br>
<br>
<br>
Reduction to this workflow does not mean that this workflow can be understood and implemented with the same results in any manner.<br>
<br>
I call this the "Lowest Common Denominator" problem.&nbsp;&nbsp;In any given situation, there are some common things that are understood between all parties, and these are the things that can be communicated "clearly".<br>
<br>
These concepts are used to divide up the problem so that they can be solved, hence denominator.&nbsp;&nbsp;The problem is that in order for the parties to agree, they have to use the simplest methods of communicating that every party can understand, which is where the "common" and "lowest" (simplest) come from.<br>
<br>
The issue here is that there are more efficient ways of doing things, that are not as simple, but not all parties will have equal knowledge of all of these things, presenting a dilemma:&nbsp;&nbsp;Do you aim for higher efficiency or higher commonality?<br>
<br>
This is something every given team/organization should decide for themselves, because they work on a spectrum.&nbsp;&nbsp;If you aim for more commonality, you lower the bar on what techniques are common to all parties, and you will lose the benefits that un-commonly-known techniques may provide.<br>
<br>
If you aim for efficiency of techniques, you enter the area where not all parties understand the techniques.&nbsp;&nbsp;This is also exemplified by the "single person vs. large team" spectrum.&nbsp;&nbsp;Single people are able to use efficiencies that even a 2-person team cannot, because of the immediate nature of communication inside one's own head.<br>
<br>
As soon as the communication must be externalized, there is a massive loss of efficiency in the communication, and as the team grows the communication problems grow factorially.<br>
<br>
How massive is this loss in terms of efficiency in communication between your own thoughts, and communicating with 1 external person?&nbsp;&nbsp;{{ stats_memory_cycles_per_second_vs_words_per_minute }}<br>
<br>
To give an example, this is the difference between accessing something already loaded into RAM and Layer 1 Cache, vs accessing something on a 5400 RPM slow rotating spindle disk, on a remote computer, that is networked via satellite, and resides on another planet (Earth -> Mars).&nbsp;&nbsp;That is the type of inefficiency that is created between going from one's own thoughts, to communicating with 1 other person.<br>
<br>
When communicating with teams or large groups of people, this is made worse, as often the communicate is by proxy, so not only is the communication inter-planetary in terms of efficiency, it is through a lossy-proxy, which will change the data and is more likely to summarize it, dropping out many details and changing the terminology, phrasing, and perhaps even the intent.<br>
<br>
So while your assertion that everything can be broken down into: Create Test, Implement Thing To Be Tested, Verified Test.&nbsp;&nbsp;<br>
<br>
This does not mean that all different types of processes give the same results merely because of this.<br>
<br>
To give an analogy, I can say that all data in a database could be stored in a single table with 3 fields:<br>
<br>
- Group<br>
- Type<br>
- Value<br>
<br>
All of these fields can be BLOBs, so we only need 1 storage type, and from that all data actions done in any other method can be implemented.<br>
<br>
This is true, but it is not efficient.<br>
<br>
This is a similar spectrum to having "single ownership" vs "team ownership".&nbsp;&nbsp;They provide different benefits, and cause different problems.&nbsp;&nbsp;Single ownership allows for the efficiency that a single owner can bring, but at the loss of wider understanding and access.<br>
<br>
Team ownership provides wider understanding and access, but limits the amount of efficiency that can be used due to all members of the team needing to be able to understand all of the implementation well enough to work with it.<br>
<br>
Anything that is not immediately well-understood by any member of the team, in a team-ownership environment, should be converted into a method in which that team member can understand it.&nbsp;&nbsp;This should be applied to all changes, recursively, so that all details fit this criteria.<br>
<br>
Taken to it's extreme, it is easy to see how this solution will be "dumbed down" (not to be insulting, merely to illustrate the point) to the most common knowledge (low tech vs high tech), and this will have an effect on the efficiency and manageability of the work.<br>
<br>
There is a "tipping point" where this "low-tech" type direction starts to become a problem in itself, either by not performing fast enough, or not being small enough to manage, as size has a direct impact on complexity as well.&nbsp;&nbsp;More things are harder to manage than less things, just as more complex things are harder to manager than simple things.<br>
<br>
__Exchange__<br>
<br>
Author:&nbsp;&nbsp;So are you are saying that the workflow is same, but it just differs in implementation? I'm leaving that question out for now. I believe it is possible to separate the questions of workflow and it's implementation. So first think I want to agree on is on which workflow produces best result. After we agree on that, we can talk about it's implementation.<br>
<br>
<br>
Me:<br>
<br>
I completely agree with your interest in coming to agreement on workflow, techniques and terminology.&nbsp;&nbsp;I think this is important work, and the surface has barely been scratched on it in our industry (even with places like the c2 wiki, which are comically in-depth).&nbsp;&nbsp;Just wanted to say that.<br>
<br>
I think there are a couple of issues here.<br>
<br>
The first is the matter of deconstructionism.&nbsp;&nbsp;For every layer of abstraction you remove when deconstructing something, you lose the context and connotations (intentions) of that symbolic abstraction as well.<br>
<br>
So I can further deconstruct your deconstruction into this:<br>
<br>
- Think<br>
- Act<br>
- Evaluate<br>
<br>
Now we have an even simpler model, and we aren't restricting to programming.&nbsp;&nbsp;The problem is that we also aren't even talking about software development any more, we've gone so general that it has lost it's original purpose, which is to better understand how to do something related to developing software.<br>
<br>
In similar ways, each abstraction layer removed to get to the point of:<br>
<br>
- Create test<br>
- Write code<br>
- Evaluate test<br>
<br>
Has lost the contexts, connotations, and further layers of abstractions that each of the concrete methods that would be used in place of those 3 things, and the many nuanced sub-things that would be required to properly detail those replaces.<br>
<br>
Taken to it's extreme, on that same spectrum, you go from the 3 things I just typed in, to the complete work of code you intended to produce, in it's ideal fully-tested-and-shippable form.<br>
<br>
This is the full-spectrum of analysis:&nbsp;&nbsp;From complete abstraction to complete concrete implementation.<br>
<br>
So we can tune the discussion to any parameter for both this spectrum, and any related axioms for determining the results of the work that we wish to get through our efforts.<br>
<br>
My point was mostly that we should not lose out on efficiency, if we desire efficiency, because we also desire commonality.&nbsp;&nbsp;As they have a spectrum between them.&nbsp;&nbsp;(Almost anything can be put with anything else into a spectrum, like two points making a line segment, so I'm not drawing from any specific examples here, more in idea-space)<br>
<h3 id=e5829271e6cfb5927f3a4d4aec1b10df><a href="#e5829271e6cfb5927f3a4d4aec1b10df">11.8.1</a>: "Best Practices" Means Not-Thinking</h3>
<br>
Everyone wants to know a "good" way to do something, or better yet a "better" way of doing something, or best yet, the "best" way of doing something.<br>
<br>
And so, "Best Practices" were created, to be sold by authorities (of any type or experience level) as to what you should do under a given situation, often with little context at all in terms of pros-and-cons of the implementation, because the authors often have very little personal experience in managing the solution being offered.<br>
<br>
Why would I broadly declare this to be true?&nbsp;&nbsp;Because for any given "best" solution to be published would require more caveats and warnings than any advice, because "best" is a very specific set of criteria, and they by definition are not taking any of your specific environmental issues into account.<br>
<br>
Why would I broadly state that this is tantamount to Not Thinking?&nbsp;&nbsp;Because if one does not take into account one's specific environment, requirements, resources and goals into consideration in making plans for action, than what is one doing?<br>
<br>
It is following a recipe, without checking if the recipe will even give you what you want.&nbsp;&nbsp;Do you even know what you want?&nbsp;&nbsp;Probably only vaguely if you want to follow someone else's Best Practices, because you are leaving all the decision making as to what the effects of the system will be up to someone who doesn't know you, your circumstances, your environment, your requirements, your resources or your goals.<br>
<br>
Does leaving all that up to someone who doesn't know any of those things sound like Good Thinking to you?&nbsp;&nbsp;It does not to me, which is why I stated this section's title as I did.<br>
<br>
Reading over the "Best Practices" of others is not in any way bad, and one should try to collect up all the ways that people are doing things, or at least all the major archetypes of those methods, so that one has a good perspective of external activity to help guide one's own decision.<br>
<br>
But, then one should make one's decision based on your own environment, your own understanding of your resources, your own understanding of your requirements, your own understanding of your goals, and in this way you can tailor any external or internally created methodology to meet those needs, and because you thought about it yourself, whenever you discover something is inefficient you have the tools to re-design the solution to meet the new problem and solve it.<br>
<br>
If you are simply following someone else's recipe, you are unequipped to change the recipe, because none of the thinking about how to build and apply the recipe were your own, so changes will be not mapped to all the issues I mentioned.&nbsp;&nbsp;Often people are more likely to just switch to a different recipe, which they see as a New Silver Bullet, because the last one didn't work.<br>
<br>
Repeating this process wastes time and other resources, and you give up all the opportunity you could have been leveraging if you had made your own plans, because you could make smaller changes since you well-understood all the components and decisions.<br>
<h2 id=013f970372d2f2259b0f133564b0c04a><a href="#013f970372d2f2259b0f133564b0c04a">11.9</a>: The Similarities of All Code</h2>
<br>
Explain how all code is similar, and all programs are implementing 95%+ the same functionality, and 5%- unique functionality.<br>
<br>
Explain how to take this apart and put it back together again, and how to apply it.<br>
<h2 id=5ac173696667f68ef9bd32089e41e060><a href="#5ac173696667f68ef9bd32089e41e060">11.10</a>: Penalties of Over-Abstraction</h2>
<br>
{{ todo__needs_editing__maybe_moved_into_another_section }}<br>
<br>
Removing the real-worldness of things always makes them easier to abstract, and also makes them unequipped to solve any real-world problems as-is.<br>
<br>
Many times when a real-world problem is finally solved with the non-real-worldness-based abstracted solution, the fit is not a good one, because the abstracted solution factored out critical elements of the problem, and now the problem is solved less efficiently, and in some cases too inefficiently.<br>
<br>
It yields better results to design a solution to an exact problem, so that you can solve it as efficiently as possible, and then abstract the solution into two split pieces: an abstracted library layer and a real-world implementation layer.<br>
<br>
Then you know the abstracted version solves a problem efficiently, because it's the exact solution you just designed to solve your problem-at-hand efficiently.<br>
<br>
If it worked for this problem efficiently, there are likely other problems that can also make highly efficient or sufficiently efficient use of the abstracted solution as well.<br>
<br>
This is obviously something that can be logically proved if someone wanted to spend the effort.<br>
<h2 id=822a93e6d35a5d2173bda4a30b16591b><a href="#822a93e6d35a5d2173bda4a30b16591b">11.11</a>: Releasing the poison</h2>
<br>
This is the only non-Operations advice that I will give in this book, because I think it is the most important non-technical advice I can give, and it has to do with inter-human communication and inter-human relationships.<br>
<br>
No matter what society, culture or place you are born in, grow up in, and live in, there are elements around you that are harmful to you, and affect you in a negative manner.<br>
<br>
In dealing with other people, we often encounter negativity in many dimensions, whether it is in attitude, verbally, or physically.<br>
<br>
And in our own actions, we ourselves will have negative attributes that are presented and may affect our co-workers, team mates, as well as ourselves, friends and family.<br>
<br>
A term I have begun to use for this type of thing is "poison", and to use it in a sentence might be something like, "I am poisoned, and have become toxic and it is effecting myself and others".&nbsp;&nbsp;This reads pretty harshly to me, but it is meant to be clarifying and not vague or down-played.<br>
<br>
I believe that all of us are both our own greatest allies, and our own worst enemies.&nbsp;&nbsp;Our own actions have more impact on us than any other individual's can have, because we are the ones who coordinate our actions every second of every of day of our lives, whether we are directly aware of the coordination for each action or not.<br>
<br>
In term's of our larger group's influence on us, this is actually more of our own influence on ourselves, as we have interpreted the intention of our larger society, culture or group, and our position in it.&nbsp;&nbsp;I find conflict between my view of how I think I should fit into my group, versus how I would like to fit into my group.&nbsp;&nbsp;And the same is true for "how the group thinks about me", to anthropomorphize the "collective dynamic" or "group think" or "social pressure" or "super ego" or whatever.<br>
<br>
But, this is not merely negative, it is also positive, as I take the good things about my culture and group, and I am seen positively by them and myself, and I see the positive ways that I fit into the group, and they do me.<br>
<br>
In order to improve myself, I need to focus more on seeing these positive things, and how others can see me positively, and less on the negative.&nbsp;&nbsp;My attention alone will create time that I spend reflecting on the negative aspects, where I could be putting effort into actively making things more positive, and spending my time inspecting the positive aspects of things to determine how to strengthen them, and create more of them.<br>
<br>
I refer to this, internally (and now written into a book, I guess), as "releasing the poison", which is releasing the things inside me that make me "more toxic", so that I can be "less toxic", with the goal of being "not toxic".<br>
<br>
I say "releasing" instead of some other term, because these are active patterns in myself, things that I do, that I didn't have to do, but did.&nbsp;&nbsp;So these are habits or reflexes which need to be changed, but in order to do something else, I must stop doing what I am already doing.&nbsp;&nbsp;So I refer to this as "releasing" it, as it is something I am "holding on to", which is why I keep doing it.&nbsp;&nbsp;I think this distinction is important, as it underlines how this is completely an internal process, that I can accomplish myself, with no external validation.&nbsp;&nbsp;<br>
<br>
Why is it important that I can continue to make progress without external validation?&nbsp;&nbsp;It is important, because if people act in negative ways to me or around me, I do not need to respond with negativity or spend time dwelling on the negativity.&nbsp;&nbsp;<br>
<br>
Acting with negativity creates a feedback loop, where one party is negative to another party, and the other responds with negativity (understandable, even if they were neutral or positive prior to the introduced negativity), and the first continues to respond negative and may increase it, and so on.<br>
<br>
Because this feedback loop only intensifies until one of the party "turns down the volume", or turns it off, then it becomes clear why so many problems exist between people. <br>
<br>
I am certainly not through with my journey on this path, but I feel continual improvement as I have created an internal process of inspecting things that occur in my life, and comparing them to the model I have created for how I spend time related to negativity, versus how I spend time related to positivity.<br>
<br>
This allows me to see where I have made mistakes more easily, and gives me the incentive to take action to try to correct those mistakes.&nbsp;&nbsp;Often simply not taking action to correct a negative-effect action creates even more problems down the road which requires much work or may be unsalvageable, where taking a smaller effort earlier on, after detecting the problem, leads to less problems in the future and a more positive outcome and duration.<br>
<br>
If I have said or done something that may have caused a problem for someone, in any way, I can realize this and then mention it to them in passing, or ask to talk with them and go over what happened, and how I would prefer things were resolved, trying to fix any problems that were created, and create and keep a positive relationship with them.<br>
<br>
This, however, does not mean that I ignore problems because "problems are negative".&nbsp;&nbsp;I do not see problems being negative, even though "problem" and "obstacle" are normally negative-quality terms.&nbsp;&nbsp;In engineering, and especially in more maintenance type aspects such as Operations, problems and obstacles are almost all we deal with.&nbsp;&nbsp;Everything could be phrased as a problem, and it could be flipped around to being phrased as an opportunity.&nbsp;&nbsp;<br>
<br>
I don't recommend trying to phrase problems as opportunities all the time, because it leads to sounding unrealistic, but if you look at them positively, they really are opportunities that one can take advantage of to greater or lesser degrees to get greater or lesser benefits, if one can view them appropriately, and work with the knowledge gained from that vision into their nature.<br>
<br>
I think this methodology this has been very good for me, and recommend spending some time to think about this, and how it intersects with your life, and who you are, and if you can think of ways that bring about similar improvements in your own life, which can make working with other people more enjoyable and efficient, and brings you more happiness, contentment and a more fulfilling life with more accomplishments and friends.<br>
<h2 id=44f9bf60bb151279b7142342746370b4><a href="#44f9bf60bb151279b7142342746370b4">11.12</a>: Randomly Collected Spectrums</h2>
<br>
Spectrums I thought of, but have not yet placed in a particular part of the book.<br>
<br>
<br>
Spectrum: Caring<br>
<br>
Shame <=====> Pride<br>
<br>
Without caring about things, one cannot feel shame over bad actions, nor pride in good actions.&nbsp;&nbsp;This is an effect of having an environment where the care-takers do not care about their environment, only about getting through another day.<br>
<br>
When you care, you will avoid creating Shame for yourself and others.&nbsp;&nbsp;When you care, you will try to perform actions you and others can be Proud of.&nbsp;&nbsp;These are good things, because they will form as a compass, pointing in the direction you want to go towards and away from.<br>
<br>
If your assessments are in Alignment with Reality, then you have high assurance that you are creating a better Environment for yourself.<br>
<h2 id=52c0b5a8fe454c355a43001dcfc72c08><a href="#52c0b5a8fe454c355a43001dcfc72c08">11.13</a>: How To Make A Decision</h2>
<br>
Describe how to make a decision immediately based on data.<br>
<br>
How to decide when you need more data.<br>
<br>
How to decide when you have enough data.<br>
<br>
How to make an immediate decision when you have enough data.<br>
<br>
How you can explain your decision based on the data you had to others.&nbsp;&nbsp;Charting, graphing, etc.<br>

# Chapter 12: Everywhere.  Throughout the book.






<h2 id=a7df76e3e33c3832af992a160d248f3b><a href="#a7df76e3e33c3832af992a160d248f3b">12.1</a>: Have "Wouldnt it be nice?" sections, where I posit what would be improvements I have yet to experience.&nbsp;&nbsp;Coming to terms, agreeing on the foundational details, agreeing on the axioms, agreeing on how to relate data to the axioms.&nbsp;&nbsp;Agreeing on how to act against axioms.&nbsp;&nbsp;With these done, we can work much better as a team, and discuss them.</h2>
