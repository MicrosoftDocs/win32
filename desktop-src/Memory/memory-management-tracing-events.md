---
description: "Learn more about: Memory Management Tracing Events"
ms.assetid: D53BD414-F140-496E-884F-5A4EC4F0AAC4
title: Memory Management Tracing Events
ms.topic: article
ms.date: 05/31/2018
---

# Memory Management Tracing Events

This section describes detailed information on specific Memory management tracing event details.

Memory management tracing is a troubleshooting feature that can be enabled in retail binaries to trace certain memory management events with minimal overhead. This feature allows for better diagnostic capabilities for developers and product support. Memory management event tracing supports tracing heap allocation, reallocation, and free operations.

Memory management event tracing uses Event Tracing for Windows (ETW), a general-purpose, high-speed tracing facility provided by the operating system. ETW provides a tracing mechanism for events raised by both user-mode applications and kernel-mode device drivers. ETW can enable and disable logging dynamically, making it easy to perform detailed tracing in production environments without requiring reboots or application restarts. Memory management event tracing using ETW is supported on Windows 7 , Windows Server 2008 R2, and later. For general information on ETW, see [Improve Debugging And Performance Tuning With ETW](/archive/msdn-magazine/2007/april/event-tracing-improve-debugging-and-performance-tuning-with-etw).

The following list provides detailed information for each memory management tracing event. For additional information on any event, click the event name.



| Event Name                                                  | Description                                                         |
|-------------------------------------------------------------|---------------------------------------------------------------------|
| [**ETW\_HEAP\_EVENT\_ALLOC**](etw-heap-event-alloc.md)     | Memory management tracing event for a heap allocation operation.    |
| [**ETW\_HEAP\_EVENT\_FREE**](etw-heap-event-free.md)       | Memory management tracing event for a heap free operation.          |
| [**ETW\_HEAP\_EVENT\_REALLOC**](etw-heap-event-realloc.md) | Memory management tracing event for a heap re-allocation operation. |



 

## Related topics

<dl> <dt>

[Improve Debugging And Performance Tuning With ETW](/archive/msdn-magazine/2007/april/event-tracing-improve-debugging-and-performance-tuning-with-etw)
</dt> </dl>

 

 
