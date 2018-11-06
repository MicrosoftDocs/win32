---
title: DirectShow and Windows Media
description: DirectShow and Windows Media
ms.assetid: e2ddc781-9f56-4f77-a191-015018755eff
keywords:
- Windows Media Format SDK,DirectShow
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- DirectShow,about
ms.topic: article
ms.date: 05/31/2018
---

# DirectShow and Windows Media

As an alternative to using the Windows Media Format SDK exclusively, applications can also read and write Windows Media-based content by using the Microsoft® DirectShow® streaming architecture, as described in the following sections.



| Section                                                                                   | Description                                                                                                                                 |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [About DirectShow](about-directshow.md)                                                  | Describes DirectShow in general terms and tells where to get more information about it.                                                     |
| [Why Use DirectShow?](why-use-directshow.md)                                             | Describes how DirectShow simplifies certain tasks in the creation and playback of Windows Media–based content.                              |
| [Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)                    | Describes how to play ASF files using DirectShow.                                                                                           |
| [Creating ASF Files in DirectShow](creating-asf-files-in-directshow.md)                  | Describes how to create ASF files using DirectShow.                                                                                         |
| [WMT\_STATUS Event Notification in DirectShow](wmt-status-notification-in-directshow.md) | Describes which **WMT\_STATUS** events are handled by the ASF Reader and ASF Writer filters, and how applications can receive those events. |
| [DRM Support in DirectShow](drm-support-in-directshow.md)                                | Describes how to read and write DRM-protected files through DirectShow.                                                                     |
| [DirectShow QASF Reference](directshow-qasf-reference.md)                                | Contains the reference documentation for the DirectShow components that support Windows Media.                                              |



 

Three sample applications in the SDK illustrate the use of DirectShow: DSCopy, DSPlay, and DSSeekFM. For more information, see [Sample Applications](sample-applications.md).

> [!Note]  
> Applications that use the QASF components included in this SDK require the Microsoft DirectX® 8.1 or later SDK runtime to be installed on Windows® 2000, Windows 98, and Windows 95 systems. Specifically, this runtime is required by the DMO Wrapper filter which hosts the Windows Media codecs in a DirectShow filter graph.

 

 

 




