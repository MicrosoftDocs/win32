---
title: Window Thread in Focus
description: Window Thread in Focus
ms.assetid: 'fa8d90f2-0a9f-4c45-8fc1-133ccfc1b945'
keywords: ["event graph"]
---

# Window Thread in Focus

**Overview:** Identifies the application that has window focus, as shown in the following screen shot.

![tracks the application window having focus during a specific time interval](images/gr-img020.png)

**Graph Type:** Event graph

**Y-axis Units:** None

**Required Events:** GUID e7ef96be-969f-414f-97d7-3ddb7b558ccc:0x0002

**Events Captured:** Data for this graph is best captured using published event profiles. Using trace profiles provides context for the window focus events. For more information on event profiles please see [Trace Profiles](trace-profiles.md).

**Legend Description:** Lists active processes that have had GUI window focus during the trace.

**Graph Description:** By displaying thread focus the graph indicates which GUI window had focus during a specific period which allows the analyst to see what the user was doing during a trace period.

> [!Note]  
> By isolating a process using the legend and overlaying CPU and disk graphs, the user can determine when an application has window focus and the potential ramifications of user input.

 

 

 




