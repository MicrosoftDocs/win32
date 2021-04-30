---
description: The Network Monitor SDK includes the functions and sample code you need to build experts. However, you can also use existing tools, including a dialog editor.
ms.assetid: 6a3834b7-753f-42cc-986f-3d7e8bf79fd9
title: Programming an Expert
ms.topic: article
ms.date: 05/31/2018
---

# Programming an Expert

The Network Monitor SDK includes the functions and sample code you need to build experts. However, you can also use existing tools, including a dialog editor.

## Minimum Requirements to Run an Expert

The following table lists the DLL entry points and expert functions you must use to build an expert.



| Name                                                 | Type               | Required?                                       |
|------------------------------------------------------|--------------------|-------------------------------------------------|
| [**DllMain**](dllmain-expert.md)                    | DLL entry function | Yes                                             |
| [**Register Expert**](register-expert.md)           | DLL entry function | Yes                                             |
| [**Run**](run.md)                                   | DLL entry function | Yes                                             |
| [**Configure**](configure.md)                       | DLL entry function | Only if the expert provides user configuration. |
| [**ExpertIndicateStatus**](expertindicatestatus.md) | Expert function    | Yes                                             |
| [**ExpertSubmitEvent**](expertsubmitevent.md)       | Expert function    | Yes                                             |



 

Review the expert and parser reference topics in the Network Monitor SDK to update your source code and then use the sample code and procedures provided in these topics:

-   [Building an Expert](building-an-expert.md)
-   [Installing an Expert](installing-an-expert-to-network-monitor-2-1.md)
-   [Debugging an Expert](debugging-an-expert.md)

Expert DLLs require the C, not the C++, calling convention because functions are called through function pointers by using an overlay. Through a set of specialized expert functions, the expert has access to the frames in the capture. The expert can use most of the Network Monitor API to manipulate the returned data. When an expert finds information to send to the user, it packages the information in an event data structure and submits it to Network Monitor, which then displays the information in an expert output window. The expert must periodically update Network Monitor with percentage-completion status information, which is provided by the [**ExpertIndicateStatus**](expertindicatestatus.md) function.

The expert's exported functions are called as follows:

-   When Network Monitor is creating the list of experts to present to the user, Network Monitor calls the [**Register Expert**](register-expert.md) function.
-   After the call to **Register**, if the expert is configurable, Network Monitor calls the [**Configure**](configure.md) function.
-   When the Network Monitor user clicks **Run Expert**, Network Monitor calls the [**Run**](run.md) function.

When experts analyze the requested frames and find a problem, they use [**ExpertSubmitEvent**](expertsubmitevent.md) to submit an event that contains information about the problem. Network Monitor distributes the event to either the standard (shared) Event Viewer or (if the expert registers for it) to a private Event Viewer.

 

 



