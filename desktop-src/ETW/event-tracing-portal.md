---
description: This documentation is for user-mode applications that want to use ETW. For information about instrumenting device drivers that run in kernel mode, see WPP Software Tracing and Adding Event Tracing to Kernel-Mode Drivers in the Windows Driver Kit (WDK).
ms.assetid: 3de69436-671b-46a2-8d92-4eb3af2a4233
title: Event Tracing
ms.topic: article
ms.date: 05/31/2018
---

# Event Tracing

## Purpose

Event Tracing for Windows (ETW) provides application programmers the ability to start and stop event tracing sessions, instrument an application to provide trace events, and consume trace events. Trace events contain an event header and provider-defined data that describes the current state of an application or operation. You can use the events to debug an application and perform capacity and performance analysis.

This documentation is for user-mode applications that want to use ETW. For information about instrumenting device drivers that run in kernel mode, see [WPP Software Tracing](/windows-hardware/drivers/devtest/wpp-software-tracing) and [Adding Event Tracing to Kernel-Mode Drivers](/windows-hardware/drivers/devtest/event-tracing-for-windows--etw-) in the Windows Driver Kit (WDK).

## Where applicable

Use ETW when you want to instrument your application, log user or kernel events to a log file, and consume events from a log file or in real time.

## Developer audience

ETW is designed for C and C++ developers who write user-mode applications.

## Run-time requirements

ETW is included in Microsoft Windows 2000 and later. For information about which operating systems are required to use a particular function, see the Requirements section of the documentation for the function.

## Process ETW traces in .NET code

You can use the [.NET TraceProcessing API](https://www.nuget.org/packages/Microsoft.Windows.EventTracing.Processing.All) to analyze ETW traces for your applications and other software components. This API is used internally at Microsoft to analyze ETW data produced the Windows engineering system, and it is also used to power several tables in [Windows Performance Analyzer](/windows-hardware/test/wpt/windows-performance-analyzer). This API is available as a NuGet package.

For more information, see [this article](/windows/apps/trace-processing/overview).

## In this section



| Topic                                                                     | Description                                                                        |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [What's New in Event Tracing](what-s-new-in-event-tracing.md)<br/> | New features that were added to Event Tracing in each release.<br/>          |
| [About Event Tracing](about-event-tracing.md)<br/>                 | General information about Event Tracing.<br/>                                |
| [Using Event Tracing](using-event-tracing.md)<br/>                 | Task-related topics that describe how to use the ETW API.<br/>               |
| [Event Tracing Reference](event-tracing-reference.md)<br/>         | Detailed descriptions of ETW functions and other programming elements. <br/> |



 

 

 
