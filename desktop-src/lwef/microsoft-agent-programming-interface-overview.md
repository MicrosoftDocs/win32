---
title: Microsoft Agent Programming Interface Overview
description: Microsoft Agent Programming Interface Overview
ms.assetid: 8709441b-9739-4f11-a2de-40a5f5eefb72
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Agent Programming Interface Overview

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The Microsoft Agent API provides services that support the display and animation of animated characters. Implemented as an OLE Automation (Component Object Model \[COM\]) server, Microsoft Agent enables multiple applications, called clients or client applications, to host and access its animation, input, and output services at the same time. A client can be any application that connects to the Microsoft Agent's COM interfaces.

As a COM server, Microsoft Agent automatically starts up only when a client application uses the COM interfaces and requests to connect to it. It remains running until all clients close their connections. When no connected clients remain, Microsoft Agent automatically exits.

Although you can call Microsoft Agent's COM interfaces directly, Microsoft Agent also includes a Microsoft ActiveX control. This control makes it easy to access Microsoft Agent's services from programming languages that support the ActiveX control interface.

In addition to supporting stand-alone programs written for Windows, Agent can be scripted to support webpages, provided that the browser supports the ActiveX interface. Microsoft Internet Explorer includes support for ActiveX as well as scripting languages that you can use to program Agent. If you are not using Internet Explorer, consult with your vendor or supplier about the browser's support for ActiveX.

The following information provides a brief overview of the programming interfaces for the Microsoft Agent software.

-   [Animation Services](animation-services.md)
-   [Input Services](input-services.md)
-   [The Voice Commands Window](the-voice-commands-window.md)
-   [Output Services](output-services.md)

 

 




