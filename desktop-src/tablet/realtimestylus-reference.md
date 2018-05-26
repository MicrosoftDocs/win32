---
Description: Provides access to the stylus events coming from pen or touch digitizers.
ms.assetid: a239b53c-7fc9-4211-962a-6cfbe0be4e4c
title: RealTimeStylus Reference
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RealTimeStylus Reference

Provides access to the stylus events coming from pen or touch digitizers.

## In This Section

-   [RealTimeStylus Classes and Interfaces](realtimestylus-classes-and-interfaces.md)
-   [RealTimeStylus Enumerations](realtimestylus-enumerations.md)
-   [RealTimeStylus Structures](realtimestylus-structures.md)

## Remarks

This object implements the [**IRealTimeStylus**](/windows/win32/RTSCom/nn-rtscom-irealtimestylus?branch=master) COM interface.

This object can be instantiated by calling the [**CoCreateInstance**](com.cocreateinstance) method in C++.

You can fully control, dynamically render, modify, and even delete data from the packet stream within the synchronous and asynchronous plug-ins of the [**RealTimeStylus Class**](/windows/win32/RTSCom/?branch=master) object.

The real time stylus provides a way to create an **InkCollecting** object that is single-threaded and resident in the application UI thread. This **InkCollecting** object accesses the real time stylus data from the queue. An **InkCollecting** object in conjunction with real time stylus enables real-time selection editing and real-time editing of the collected ink data. For more information, please see [Accessing and Manipulating Stylus Input](accessing-and-manipulating-stylus-input.md).

Use the [**RealTimeStylus Class**](/windows/win32/RTSCom/?branch=master) object to interact directly with the tablet stylus data stream or to block real-time inking. Use the [**InkCollector Class**](/windows/win32/msinkaut/?branch=master) object, [**InkOverlay Class**](/windows/win32/msinkaut/?branch=master) object, [InkPicture Control](inkpicture-control-reference.md) control, or [InkEdit Control](inkedit-control-reference.md) control when the default behavior of these objects provides the behavior you need.

The real time stylus events are on a specific window handle within a specific window input rectangle. The RealTimeStylusService can send stylus data to multiple [**RealTimeStylus Class**](/windows/win32/RTSCom/?branch=master) objects. Each **RealTimeStylus Class** object receives stylus data for a specific section of a window based on the defined [**IRealTimeStylus::WindowInputRectangle Property**](/windows/win32/RTSCom/nf-rtscom-irealtimestylus-get_windowinputrectangle?branch=master) for that **RealTimeStylus Class** object. The **RealTimeStylus Class** object gets the stylus data and then processes this through a list of synchronous and asynchronous plug-ins.

The difference between the synchronous plug-ins and the asynchronous plug-ins lies in the thread in which they execute and the calling sequence. Synchronous plug-ins are called by the thread in which the [**RealTimeStylus Class**](/windows/win32/RTSCom/?branch=master) object executes. Every time **RealTimeStylus Class** object is instantiated, an execution thread is instantiated. Synchronous plug-ins are executed on this new thread instantiated for the instance of the **RealTimeStylus Class** object. Asynchronous plug-ins are called through the UI or application thread after the packet stream has been processed by the synchronous plug-ins and stored in the output queue.

## Related topics

<dl> <dt>

[**IDynamicRenderer Interface**](/windows/win32/RTSCom/nn-rtscom-idynamicrenderer?branch=master)
</dt> <dt>

[**IStylusSyncPlugin**](/windows/win32/RTSCom/?branch=master)
</dt> <dt>

[**IStylusAsyncPlugin**](/windows/win32/RTSCom/?branch=master)
</dt> <dt>

[**IRealTimeStylus**](/windows/win32/RTSCom/nn-rtscom-irealtimestylus?branch=master)
</dt> </dl>

 

 



