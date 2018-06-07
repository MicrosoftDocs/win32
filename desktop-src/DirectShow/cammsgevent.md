---
Description: The CAMMsgEvent class is a wrapper for event objects that perform message processing.
ms.assetid: 4b94febe-169f-4f04-be93-043a8c75e3b4
title: CAMMsgEvent class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# CAMMsgEvent class

![cammsgevent class hierarchy](images/util06.png)

The `CAMMsgEvent` class is a wrapper for event objects that perform message processing.

This class derives from the [**CAMEvent**](camevent.md) object. It adds one method, [**CAMMsgEvent::WaitMsg**](cammsgevent-waitmsg.md), which dispatches incoming messages while waiting.



| Public Methods                                 | Description                                                          |
|------------------------------------------------|----------------------------------------------------------------------|
| [**CAMMsgEvent**](cammsgevent-cammsgevent.md) | Constructor.                                                         |
| [**WaitMsg**](cammsgevent-waitmsg.md)         | Waits for the event to be signaled, while dispatching sent messages. |



 

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




