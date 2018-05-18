---
title: Using TraceLogging
description: The following topics provide a TraceLogging quick start for native and managed code, with examples.
ms.assetid: 'CEC57517-7A0E-45AA-85F7-F358AE51EF4A'
---

# Using TraceLogging

The following topics provide a TraceLogging quick start for native and managed code, with examples.

## Prerequisites

-   Windows 10 Software Development Kit (SDK) is required to write a user-mode provider
-   Windows Driver Kit (WDK) is required to write a kernel-mode provider

## In this section



| Topic                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [TraceLogging C/C++ Quick Start](tracelogging-native-quick-start.md)<br/>                             | The following section describes the basic steps required to add TraceLogging to native user-mode code. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [TraceLogging Managed Quick Start](tracelogging-managed-quick-start.md)<br/>                          | The following section describes the basic steps required to add TraceLogging to managed code.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Record and Display TraceLogging Events](tracelogging-record-and-display-tracelogging-events.md)<br/> | Record TraceLogging events with the Windows Performance Recorder (WPR) and view them with the Windows Performance Analyzer (WPA).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [C/C++ Tracelogging Examples](tracelogging-c-cpp-tracelogging-examples.md)<br/>                       | This topic contains C/C++ Tracelogging examples.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [.NET Tracelogging Examples](tracelogging-net-examples.md)<br/>                                       | This topic contains a managed code Tracelogging example that illustrates how to log an event only when the session verbosity level is verbose, and how to log structured event data.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Universal Windows Platform Logging Example](universal-windows-platform-logging-examples.md)<br/>     | This sample shows how to use the Logging APIs in the Windows.Foundation.Diagnostics namespace, including LoggingChannel, LoggingActivity, LoggingSession, and FileLoggingSession. These classes are designed for diagnostic logging within a Windows app. These APIs were added in Windows 8.1. <br/> The LoggingChannel and LoggingActivity APIs have been extended in Windows 10 to support writing complex events using TraceLogging event encoding.<br/> The Universal Windows Platform logging example can downloaded from [GitHub](http://go.microsoft.com/fwlink/?LinkId=733296).<br/> |



 

TraceLogging samples.

## Related topics

<dl> <dt>

[TraceLogging for kernel-mode drivers and components](https://msdn.microsoft.com/library/windows/hardware/dn701955)
</dt> </dl>

 

 





