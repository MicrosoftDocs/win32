---
title: Overview of the Tuning Process
description: Overview of the Tuning Process
ms.assetid: 5ff63877-1917-43a6-9cbc-27b164b94db5
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Overview of the Tuning Process

The Unified Tuning Model enable applications to use a standard procedure for tuning to any program on any type of network using any kind of compatible device. When an application uses the tuning model to perform tuning, it will automatically work with any new network types that may be supported in the future, either by Microsoft or by third parties such as cable or satellite providers.

The following diagram shows the components that are involved in the tuning process.

![tuning process](images/tuning-model4.gif)

The Video Control is an ActiveX control that builds and controls the filter graph. For more information, see [Using the Video Control](using-the-video-control.md). The exact filters that appear in the graph depend on the underlying hardware. For more information, see [Microsoft TV Technologies Internals](microsoft-tv-technologies-internals.md).

> \[!Important\]  
> The Video Control is available only for Windows XP and later. With DirectX, you can use tuning model objects to create analog and digital TV applications for Windows 98SE, Windows 2000 and Window Me, but without the benefit of the Video Control. For those platforms, the application must build the filter graph, as described in [Writing Digital TV Applications with DirectX](writing-digital-tv-applications-with-directx.md).

 

The application tunes to a program by submitting a *tune request* object to the Video Control (or to the Network Provider filter). The recommended way for the application to get tune requests is to create a tune request database, also called a *guide store*. A guide store contains information about programs that can be displayed to the end-user, along with network-specific tuning information for the tuning hardware.

Third parties can also provide a software component called a *guide store loader*, which populates a guide store using service information found in the transport stream. A guide store could also be populated using information downloaded from the Web or some other source.

The following illustration shows the general relationship among the Tuning Model objects. The Tuning Model objects are described in the following sections. The COM interfaces for C++ are also shown; for Visual Basic, the application invokes methods and properties on the object.

![tuning model objects](images/tuning-model-objects.gif)

The System Tuning Spaces object contains a collection of *tuning spaces*. Each tuning space represents a different network type. A tuning space is used to create tune request objects, which contain the information needed to tune to a program. **Locator** objects contain additional information about the signal. The tuning space may contain a default locator, which is used to locate the default transport stream within the multiplex. The tuning space object, the tune request object, and the locator object are all network-specific. Separate objects are provided for ATSC, DVB, analog television, and other network types.

A program contains one or more elementary streams. Each elementary stream is called a *component*, and is described by its *component type*, such as audio or video. Some components may be mutually exclusive. For example, a program might contain two audio streams in different languages. A tuning space can have a list of preferred component types. If so, these are used to select the default components from the stream. An application can override the defaults based on the user's preferences. For example, it might choose a secondary audio stream in another language.

 

 




