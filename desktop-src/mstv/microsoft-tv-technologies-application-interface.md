---
title: Microsoft TV Technologies Application Interface
description: Microsoft TV Technologies Application Interface
ms.assetid: 03aac331-3e90-4464-a502-d34a51a70b24
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Microsoft TV Technologies Application Interface

The most important concepts in Microsoft® TV Technologies are the Video Control and the Microsoft Unified Tuning Model. Both are shown in the following illustration.

![microsoft tv technologies architecture](images/mstv-arch.gif)

The Video Control is an ActiveX® control that handles television tuning, DVD and file playback, and stream buffering.

> [!Note]  
> The Video Control requires Windows XP or later. For applications intended to run on earlier platforms, see [Writing Digital TV Applications with DirectX](writing-digital-tv-applications-with-directx.md).

 

Internally, the Video Control creates a DirectShow filter graph. It also creates various helper components that manage the filter graph. These components are grouped into three categories:

-   *Input devices* represent data sources, such as a TV tuners.
-   *Output devices* represent renderers, such as video renderers or audio renderers.
-   *Features* represent additional services that DirectShow can provide, such as closed captioning or IP data services.

Devices and features provide the application with a higher level of abstraction than the underlying DirectShow filters. They give you a consistent set of interfaces for controlling DirectShow, organized around functionality rather than the internal implementation. For more information about using the Video Control, see [Using the Video Control](using-the-video-control.md).

The Unified Tuning Model is an API that defines tuning on any type of network, using any kind of compatible device. Microsoft TV Technologies includes software components that implement the Unified Tuning Model for several network types, including ATSC and Digital Cable. Third parties can implement the Unified Tuning Model for other network types. By using the tuning model to perform tuning, an application will automatically support any new network types that may be introduced in the future, either by Microsoft or by third parties.

From the application's standpoint, the main object in the Unified Tuning Model is the *tune request*. A tune request contains all the information that the Video Control needs to tune to a particular broadcast service. Tune requests are typically created by a separate component, called a guide store loader, and then stored in a database. The application performs tuning by getting a tune request from the database and submitting it to the Video Control. For more information, see [The Microsoft Unified Tuning Model](the-microsoft-unified-tuning-model.md).

## Related topics

<dl> <dt>

[Overview of Microsoft TV Technologies](overview-of-microsoft-tv-technologies.md)
</dt> </dl>

 

 




