---
title: Using the Video Control
description: Using the Video Control
ms.assetid: ff269a7a-3b9e-4125-8be1-594327e7177c
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the Video Control

> [!Note]  
> This topic applies to Windows XP or later.

 

The Video Control is a lightweight ActiveX control that gives Automation clients access to the powerful features of DirectShow. For the first time, you can write advanced television applications using Visual Basic.

Using the Video Control, you can:

-   Play analog or digital TV broadcasts from a variety of network types, including analog, ATSC, and DVB.
-   Create sophisticated mixing and blending effects using the Video Mixing Renderer.
-   Create DVD-based applications.
-   Create stream buffer applications.
-   Play local video and audio files.

These tasks can be done with only a few lines of code. More importantly, this code can be neutral as to the network type. As new network types are supported, the application will automatically support them, without any changes to the application. This is possible because the tuning information is stored in Tune Request objects, which encapsulate network details. The application simply retrieves the tune request from whatever storage mechanism it uses, and submits the tune request to the Video Control.

This section contains the following topics:

-   [Video Control Overview](video-control-overview.md)
-   [Tuning with the Video Control](tuning-with-the-video-control.md)
-   [Using the Stream Buffer Engine with the Video Control](using-the-stream-buffer-engine-with-the-video-control.md)
-   [TV Applications in C++ (Video Control)](tv-applications-in-c--video-control.md)
-   [DVD Applications in Visual Basic (Video Control)](dvd-applications-in-visual-basic--video-control.md)

## Related topics

<dl> <dt>

[Video Control](video-control.md)
</dt> </dl>

 

 




