---
title: Windows Events
description: Events are typically used for troubleshooting application and driver software.Prior to Windows Vista, you would use either Event Tracing for Windows (ETW) or Event Logging to log events.Windows Vista introduced a new event model that unified both the Event Tracing for Windows (ETW) and Windows Event Log API.Windows 10 introduces TraceLogging which builds on ETW and provides a simplified way to instrument code for native, .NET and WinRT developers.
ms.assetid: c10baa8d-50b9-4fda-89d0-d00b1d9f5404
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Events

Events are typically used for troubleshooting application and driver software.

-   Prior to Windows Vista, you would use either [Event Tracing for Windows](https://msdn.microsoft.com/library/windows/desktop/bb968803) (ETW) or [Event Logging](https://msdn.microsoft.com/library/windows/desktop/aa363652) to log events.
-   Windows Vista introduced a new event model that unified both the [Event Tracing for Windows](https://msdn.microsoft.com/library/windows/desktop/bb968803) (ETW) and [Windows Event Log](https://msdn.microsoft.com/library/windows/desktop/aa385780) API.
-   Windows 10 introduces [TraceLogging](https://msdn.microsoft.com/library/windows/desktop/dn904636) which builds on ETW and provides a simplified way to instrument code for native, .NET and WinRT developers.

The new [TraceLogging](https://msdn.microsoft.com/library/windows/desktop/dn904636) model allows you to include structured data with events, correlate events, and does not require a separate instrumentation manifest XML file.

The Windows Vista model uses an XML manifest to define the events that you want to publish. Events can be published to a channel or an ETW session. You can publish the events to the following types of channels: Admin, Operational, Analytic and Debug. If you use only ETW to enable the publisher, you do not need to specify channels in your manifest. For complete details on writing a manifest, see [Writing an Instrumentation Manifest](https://msdn.microsoft.com/library/windows/desktop/dd996930), and for information on channels, see [Defining Channels](https://msdn.microsoft.com/library/windows/desktop/dd996911).

To register your event publisher and to publish events, you use the ETW API. For details, see [Providing Events](https://msdn.microsoft.com/library/windows/desktop/aa364098) and [Developing a Provider](https://msdn.microsoft.com/library/windows/desktop/dd996919). The event publisher will automatically write the events to the channels specified in the manifest if they are enabled.

If you want to control the events that an event publisher publishes at a finer level of granularity, use the ETW API. For example, if the manifest defines both write and read events, you can enable only the write events. An event can also specify a level value such as warning or error, so you can limit the events that are written to those that specify the error level. For details, see [Controlling Event Tracing Sessions](https://msdn.microsoft.com/library/windows/desktop/aa363694). The events are written to the session's log file.

Consuming events involves retrieving the events from an event channel, an event log file (.evtx or .evt files), a trace file (.etl files), or a real-time ETW session. To consume events from an ETW trace file or a real-time ETW session, use the trace data helper (TDH) functions in ETW to consume the events. You can also use TDH to read the event metadata. For details, see [Consuming Events](https://msdn.microsoft.com/library/windows/desktop/aa363692). To consume events from an event channel or an event log file, use the Windows Event Log functions to query or subscribe to events. For more information, see [Querying for Events](https://msdn.microsoft.com/library/windows/desktop/aa385650) or [Subscribing to Events](https://msdn.microsoft.com/library/windows/desktop/aa385771).

Prior to Windows Vista, you must use [Event Tracing for Windows](https://msdn.microsoft.com/library/windows/desktop/bb968803) or [Event Logging](https://msdn.microsoft.com/library/windows/desktop/aa363652) to publish and consume events.

 

 




