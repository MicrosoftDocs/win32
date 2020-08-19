---
title: Designing a User Interface
description: This section describes in detail some of the tasks associated with designing a UI for a Windows application.
ms.assetid: 22deda0c-bf03-4fcd-9cc9-6381b601c152
ms.topic: article
ms.date: 05/31/2018
---

# Designing a User Interface

This section describes in detail some of the tasks associated with designing a UI for a Windows application.

-   [Introduction](#introduction)
-   [Functional Requirements](#functional-requirements)
-   [User Analysis](#user-analysis)
    -   [Problem Statements](#problem-statements)
    -   [Priorities](#priorities)
-   [Conceptual Design](#conceptual-design)
-   [Logical Design](#logical-design)
-   [Physical Design](#physical-design)

## Introduction

UI design can be divided into three essential elements : functionality, aesthetics, and performance.

More often than not, the primary focus during application development is functionality. Is the application usable? Does it enable users to complete tasks? However, functionality is only a part of the story.

Aesthetics describe how things are shown and presented, the style in which things are communicated to the user. Aesthetics are very subjective and much more difficult to quantify than functional requirements and performance metrics. Aesthetics typically come down to simple choices—how colors complement each other or how UI elements convey their meaning—that often affect the way a person feels about something and influence how successful they are using it.

Performance is measured by not only speed, but also reliability. If an application looks and feels great, is easy to use, but crashes repeatedly, it likely won't be very successful. The application has to provide a user with full confidence in its reliability.

The following are some design phase tasks that can contribute to a successful UI for a Windows application.

## Functional Requirements

Consider the following suggestions early in the design phase to optimize the user experience across the broadest audience possible:

-   Follow UI design guidelines.

    Become familiar with the [Windows User Experience Interaction Guidelines](../uxguide/guidelines.md) and refer to them often as the design, implementation, and testing of the application UI progresses.

-   Ensure that the UI is accessible.

    Be sure to integrate accessibility into the UI design from the beginning of the product lifecycle. Retrofitting accessibility can be extremely costly because part of accessibility development requires attention at the architectural level. For more information, download the [Engineering Software for Accessibility eBook](https://www.microsoft.com/download/details.aspx?id=19262).

-   Support the international marketplace.

    Windows includes technologies that enable support for many cultures and written languages in a Windows application. If the application is targeting the international marketplace, it is important to include internationalization support in the UI design from the beginning of the project. For more information, see [Internationalization for Windows Applications](../intl/international-support.md).

## User Analysis

A critical step in designing a successful interface is attaining a basic understanding of what users need and want from an application before writing any code. Remember, potential users of an application are already doing their job in some way and existing tools and processes should be understood as fully as possible. Do not design without fully considering these issues.

The simplest and most informal approach is talking to the intended users of the product. Get information directly from the source–avoid using managers or executives as proxies for actual consumers. Consider having small groups of developers and program managers pay informal visits to users in their workplaces where there is an opportunity to discuss how they work and gather details of the issues they face with their current tools.

Remember, do not to ask leading or biased questions as this will directly affect the quality and validity of the user feedback. Keep the following in mind when composing questions during this phase:

-   Who are our users? What skills and knowledge do they have?
-   What different sources of data can we use to understand their experience?
-   What goals and tasks will they use our product to complete?
-   What assumptions are we making and how can we verify them?
-   What sources of data do we have? (Usability studies and heuristic evaluations are good places to start.)

### Problem Statements

Once all user feedback has been collected, analyze and distill it into related issues and requirements. Try to avoid thinking about solutions at this point. Make sure the problems are fully identified, not just the symptoms.

It is often helpful to compose a list of one sentence problem statements (from the users perspective) for each issue or requirement. For example, "Resize edit box width to 15 characters" is not a problem. But "It is too difficult to type in long search terms" is a valid problem statement. The difference is dramatic. Try not to define the solution and the problem at the same time: often the real problem is lost. In this example, there may be many other ways to solve the problem of search terms, including changing the size of the edit box. Always keep alternative solutions in mind.

The following are additional examples of problem statements:

-   It is difficult to navigate from one section of the Web site to another.
-   Users have to wait too long for the software to load.
-   Our security error messages are difficult to understand.
-   The registration page has too many questions, and users often abandon it.
-   Finding a specific product on the site index is too hard to complete.

If the problem statements are broad enough, there are likely to be many innovative and creative ways to solve them.

### Priorities

The act of taking a list of items, and ranking them by priority, defines a release. Without clear priorities, teams may fight and argue over what things should be done and what things should be cut. The work involved in setting priorities should be easier with the research complete, but it's always a challenge.

Setting priorities requires the ability to evaluate on at least three criteria: schedule, team, and business. There may be a predefined schedule set for the project, which limits the size and scale of the work that can be done. A problem that is likely to require rewriting half the code-base should not be attempted during a small release cycle.

The makeup and nature of a team defines what kinds of work can be done. What other commitments does the team have? Is there a designer or usability engineer on the team? What skills with Web or UI design does the team have? Last, and most important, are business considerations. What are the revenue goals for this project? Who are the competitors? What are the advantages of solving certain problems? What partnerships can be forged? Any other considerations should also be identified before prioritizing the list.

Once prioritized, the list of problem statements sets the direction for the product and ensures that development is targeted in the right areas.

## Conceptual Design

Typically, the UI is not addressed in the conceptual design phase. However, this phase does require a thorough business model with complete user profiles and usage scenarios which are imperative for a successful user experience.

## Logical Design

The logical design phase is when the initial prototypes that support the conceptual design are developed.

The specific hardware and software technologies to be used during development are also identified in this phase, which can determine the capabilities of the UI in the final product. For more information, see [User Interface Technologies](user-interface-technologies-for-windows-applications.md).

In addition to the development tools, the various hardware requirements and form factors that are to be targeted by the application should be identified.

## Physical Design

The physical design phase determines how a UI design is to be implemented for the specific hardware and form factors that were identified in the logical design.

It is during this phase that hardware or form factor limitations might introduce unexpected constraints on the UI that require significant refinements to the design.

 

 