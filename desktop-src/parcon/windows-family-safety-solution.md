---
description: Windows Family Safety Solution
ms.assetid: b89cf0c7-bf9f-4bcb-b008-8b7c792f3300
title: Windows Family Safety Solution
ms.topic: article
ms.date: 05/31/2018
---

# Windows Family Safety Solution

Key requirements defined by Microsoft for a more comprehensive solution are as follows. Note the definition for online is a primarily Internet-facing technology, unlike an offline client which is usually bounded at the computer.

-   Provide a single, easy to find area in the operating system user interface where all parental controls policies, control of activity monitoring, and activity data for an identity may be readily discovered.

-   Support monitoring of sufficient activity of the controlled user so that a parent or guardian has reasonable confidence that risky activities may be discovered. Also, log reconfiguration of the controlled user's policies so that unintended or unauthorized changes are discoverable.

-   Expose activity monitoring capabilities through standard Windows Vista event logging interfaces, and provide an in-box viewer solution. Define standard activity events, and provide for extensibility to custom event generation by ISVs.

-   Promote that all monitoring and restrictions for a user are turned on only on an opt-in basis by parents or guardians. Wherever possible, restrictions functionality should be completely inactive for non-controlled users to minimize security and application compatibility risks.

-   Microsoft shall strive, whenever possible, not to make value judgments by age or other parameters for the controlled user (third parties may choose to do so). Such decisions are left up to the parent or guardian, often influenced by communities or organizations.

-   Provide implementations in the product for offline activity monitoring and restrictions where few or no offerings are available today, where the associated safety-risk functionality is available in the product, or where a Microsoft solution provides capable and robust functionality fully integrated with the design of the operating system.

-   Generally, promote that applications perform their own logging and restrictions for best context and UI experience.

    Exception: Provide comprehensive online activity monitoring and restrictions in selected areas where the benefit to consumers and industry outweigh the costs.

-   Expose parental controls user interface settings and activity event definitions by using public APIs so that third parties may query for state, modify settings, and read activity logs if they are running with sufficient Windows account privileges.

An overarching goal is to promote third-party parental controls solutions' coexistence with the in-box functionality, and support adding value by integrating with, extending, or providing alternative capabilities where suitable.

 

 



