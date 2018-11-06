---
title: Prototyping a User Interface
description: This topic explores how prototyping a user interface can help minimize design flaws and ensure a successful user experience.
ms.assetid: 16e3fabb-9cd1-4517-8f19-b1d80c956ee0
ms.topic: article
ms.date: 05/31/2018
---

# Prototyping a User Interface

This topic explores how prototyping a user interface can help minimize design flaws and ensure a successful user experience.

## Introduction

Sometimes, as a project moves forward, small assumptions and well-intentioned but poor decisions accumulate, turning hours of work into a lousy user experience. The smart teams eliminate their mistakes before they ship by using a technique called UI prototyping. Combined with usability studies, prototypes keep teams headed in the right direction.

## Why Prototype?

Prototyping is a means of exploring ideas before you invest in them. All experienced craftspeople and engineers create prototypes of their work before they build anything: Architects create models out of paper or cardboard, or with virtual reality tools. Aeronautic engineers use wind tunnels. Bridge builders create stress models. Software and Web designers create mock-ups of how users will interact with their designs.

The best reason to prototype is to save time and resources. The value of a prototype is that it is a facade—like a Hollywood set, where only the front of the building is constructed. Relative to the real product, prototypes are easy and inexpensive to create. So, for a minimal investment, usability and design problems can be found and the UI adjusted before substantial investment is made in the final design and technologies.

On examining the needs of a particular project, reasons for creating a prototype other than saving money might be found. Is the goal to explore a new interface model? Make modifications to one part of the existing design? Investigate a new technology? Before starting, it's important to be clear about why you're building what you're building. Beginning with clear goals helps make effort direct and effective. The reasons for creating prototypes fall into three basic categories:

-   Proof of concept.

    Among some teams there are disagreements about the future direction of a project. A prototype can be used to prove that an idea or new approach has merit or value. A prototype can help illustrate that an idea works, express its qualities in a visual and interactive way, and/or motivate team members to think about the problem from another perspective.

-   Design exploration.

    If designing interactive software, the only way to explore how something will be used is to create a mock-up and interact with it. Sometimes the mock-up is tied to a usability study, where parts of the prototype can be evaluated in a structured way. Sometimes it's just a way to clearly express to a developer how something should work or look. In many cases, a designer might simply be experimenting, in an effort to get a sense for what approach might work. Anyone on the team can use prototypes to explore design issues, although designers are generally the most skilled. Design explorations should be directed at trying to solve specific problems that are recognized in the product.

-   Technical exploration.

    Developers investigating implementation approaches to a problem often try out different coding techniques to see if they work well. Using COM+, Dynamic HTML (DHTML), Microsoft Win32, or specific coding approaches within each technology have different tradeoffs. Sometimes a prototype represents an exploration into what technology will work well to support a certain UI feature.

Sometimes prototypes are created for a combination of these reasons. If a team plans well enough, they can allot time for a developer and a designer or project manager to work together on a prototype. In such cases, it's extremely important to clearly define the goals and the contributions each team member is expected to make. Everyone should be clear on what the goals are, what's at stake, and what the potential outcome will be.

## Who Is Involved?

Prototyping can be done informally by anyone, regardless of their background or role in the project. It's easy to make a simple but effective prototype by taking a bitmap from Adobe Photoshop, putting it into the Microsoft FrontPage Web site creation and management tool, and adding active buttons or links. These lightweight prototypes only go so far, and can become unwieldy for complex interactions.

For more formal prototypes by larger teams, a developer or project manager will often collaborate with a designer and a usability engineer. Together they'll generate ideas, build a prototype that represents the best ideas, and then go into the lab to see how effective it is in solving user problems. Developers might get involved if they can spare the time, or if their technical expertise is needed. Often the designer or project manager will do most of the scripting or coding to build the prototype.

## When Should a Prototype be Built?

Depending on the scope of the prototype and the level of detail required, prototypes can be built at any time during the project. Most often they are created early in the project, during the planning and specification phase, before developers write any production code. That's when the need for exploration is greatest, and when the time investment needed is most viable. If developers instead of program managers or designers are prototyping, scheduling time becomes even more important because of the need to make sure the work invested in the prototype is accounted for in the development schedule. Planning for any UI release should include some level of prototyping.

Late in a project, smaller prototypes can help resolve tough design and technical issues. A quick HTML mock-up of how a dialog box or Web page should behave can help answer a developer's question or give other teammates a feel for what the desired experience should be. In some cases, a strong program manager or designer can implement the behavior in Microsoft JScript development software and approximate much of the programming logic that developers will need to think through.

The time it takes to create a prototype can vary tremendously, depending on the scope and precision of what the end result needs to look like. An informal prototype could mean a few hours of work by one person; a more organized effort can involve weeks of effort by an entire team.

## Where Should the Focus Be?

In a prototype, build only as much of the design as is needed. It's okay to have buttons that do not work, or text that never updates. As long as the required interactions can be experienced, it's fine to use smoke and mirrors for the rest. Here are a few reasons why efforts should be carefully focused:

-   Cost of building the prototype.

    The cost involved in building the prototype should be minimized. The challenge with prototyping is recognizing the minimal investment needed to effectively answer questions about the design. This is where usability studies are critical, because they clearly identify the parts of the UI that need the most work. Even without usability studies, clearly define what user problems are being solved, or what tasks are being improved, with the design in the prototype.

-   Limited lifetime.
-   Prototypes should have clearly defined lifetimes. Is the end goal a presentation at a team meeting? An executive review meeting? A spec review? A usability study? Identifying that the design solves a user problem? Once the needs for these specific objectives are met, the prototype should be set aside. The basic mindset is that the code or bitmaps generated in a prototype will be left behind. There might be exceptions where code or visuals live on in the product, but the expectation should be that this won't be the case.
-   Risk of overwhelming the team.

    Showing prototypes to developers and teammates can be tricky. An overly complex or elaborate prototype, sporting amazing visuals and animation, can overwhelm people. Always have a sense for how far to go and how much of the prototype should be taken seriously.

## What is the Scope?

As the focus for the prototyping effort is determined, consider the following:

-   Customer needs.

    Starting with an understanding of the key problems or needs of the users (perhaps something a usability engineer has provided) provides an idea about which parts of the UI design warrant the most exploration.

-   Usability study tasks.

    If creating the prototype for a usability study, discuss with the usability engineer what specific tasks will be part of the study, and design around those elements.

-   Team input.

    Talk with key developers on the team as the ideas in the prototype are coming together. Get a basic sense for what's reasonable, what's possible, and what is beyond consideration for the next release. In some cases, consider going beyond what they say is possible for one aspect of the design if it's a key point and the team needs to be challenged. However, do not do this with every aspect of your prototype as there is a fine line between pushing the limits and overwhelming your team. If the desire is to inspire the team by showing them a vision for several versions out, then go for it. However, if the requirement is to define specific changes for the next release, then focus efforts on those changes. Make sure to call out the specific changes in a modular way and show developers a path for building the designs.

-   Breadth vs. depth.

    For larger prototypes, there is the additional consideration of breadth versus depth. Should each feature in the design work just a little bit, or should one feature be chosen to prototype with almost all of its pieces and options? Try not to do both as the result might be a large, unwieldy prototype that is hard to modify and difficult to throw away.

## Flexible Prototypes

One way to focus prototyping resources is to concentrate on smart design. More effective prototypes can be created by allowing one piece of prototype code to exercise many different ideas. Instead of having five different prototypes, consider making one prototype that has the options to switch the different attributes of the prototype.

Should the toolbar be located on the left or on the top? Should we show 10 items on the home page or 20? A good prototype has some sort of built-in options panel that allows you to change the parameters of how the prototype looks or works. Keep these option panels hidden in the prototype—try to avoid a usability participant accidentally finding them during a test.

The challenge is to keep the prototype simple, but still useful enough that it can be shown to a teammate, different options can be demonstrated, and feedback can be obtained.

## Beta vs. Prototype

Beta releases do not qualify as prototypes, because they are complete engineering efforts. If a critical mistake is found in a feature of a beta release, it's unlikely to be discarded, even if it might be in the best interest of the product. The developers, testers, and designers have already invested a great deal of time, and the pressure to live with bad decisions is very high. Betas certainly do help in finding bugs and defects, but they are rarely useful in making controlled studies of the value of specific design directions.

## Tools and Technologies

There are several different tools and technologies that can be used for creating prototypes, each of which has its advantages and disadvantages. Consider the type of design work that is being prototyped and the goals of the prototyping effort before deciding which tool or technology is the right one.

-   Microsoft Visual Basic or C#.

    This is the fastest technology for creating Windows-style UI prototypes. The Web browser object makes it easy to integrate HTMLUI with standard Windows-style components. While it's true that a developer experienced with Microsoft Visual Studio might be able to generate UI faster in C/C++, this creates the temptation to reuse code from the UI prototype in the production code. It takes discipline to recognize that the goals of a quick and dirty UI prototype are highly divergent from high-quality engineering. Make sure it's clear what kind of code is being written, and that the team or manager understands what will be discarded.

-   Microsoft Expression Blend + SketchFlow.

    SketchFlow is a visual tool for designing, prototyping, and creating sophisticated user interfaces for Windows Presentation Foundation (WPF) and Microsoft Silverlight desktop and web applications. Applications are built by drawing shapes, drawing controls such as buttons and list boxes, making the pieces of an application respond to mouse clicks and other user input, and styling everything to look unique.

-   Adobe Director or Adobe Flash.

    Director is a popular UI prototyping tools among designers. It is most useful for multimedia or non-standard GUI designs, or for prototypes that require significant animation. It's high flexibility makes it cumbersome for UI-style UI compared to Visual Basic. However, a proficient Director user can generate Windows or Web UI without difficultly.

-   HTML.

    FrontPage and other HTML editors allow for fast creation of simple prototypes. To express an idea, it's often possible to create bitmaps that illustrate a sequence of user interaction, and place them into FrontPage. These images can be used to simulate how to interact with the design. JScript and DHTML take things to another level, allowing for very sophisticated logic and interaction. If using HTML to prototype a Web site, the warning just described for C/C++ applies here as well—do not fall into the trap of confusing quick prototype code with production-quality engineering.

 

 




