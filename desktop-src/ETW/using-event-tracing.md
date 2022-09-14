---
description: The following topics describe how to use the ETW API for event tracing.
ms.assetid: 7362874a-8206-4973-bb79-a9eaff55feb4
title: Using Event Tracing
ms.topic: article
ms.date: 05/31/2018
---

# Using Event Tracing

The following topics describe how to use the ETW API for event tracing.



| Topic                                                                          | Description                                                                                                             |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [Controlling Event Tracing Sessions](controlling-event-tracing-sessions.md)   | Describes how to manage event tracing sessions.                                                                         |
| [Providing Events](providing-events.md)                                       | Describes how to register and instrument an event trace provider.                                                       |
| [Consuming Events](consuming-events.md)                                       | Describes how to implement callback functions used to consume and process events from a trace log file or in real time. |
| [Windows Software Trace Preprocessor](windows-software-trace-preprocessor.md) | Provides an efficient mechanism to log and consume events that occur during the execution of an application or driver.  |



 

Include the Wmistr.h header file before including the Evntrace.h header file.

 

 



