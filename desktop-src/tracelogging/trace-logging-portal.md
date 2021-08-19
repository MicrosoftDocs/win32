---
title: TraceLogging
description: TraceLogging
ms.assetid: c516424a-9eba-4b56-80de-8c713fd3461a
ms.topic: article
ms.date: 05/31/2018
---

# TraceLogging

## Purpose

TraceLogging is the new Windows 10 event tracing framework for user-mode applications and kernel-mode drivers. TraceLogging builds on Event Tracing for Windows (ETW) and provides a simplified way to instrument code.

## In this section




| Topic | Description | 
|-------|-------------|
| <a href="trace-logging-about.md">About TraceLogging</a><br /> | TraceLogging is the new Windows 10 event tracing for user-mode applications and kernel-mode drivers. TraceLogging is a format for self-describing Event Tracing for Windows (ETW). TraceLogging builds on Event Tracing for Windows (ETW) and provides a simplified way to instrument code.<br /> | 
| <a href="tracelogging-using-tracelogging.md">Using TraceLogging</a><br /> | The following topics provide a TraceLogging quick start for native and managed code, with examples.<br /> | 
| <a href="trace-logging-reference.md">TraceLogging Reference</a><br /> | The following topics provide information about the native TraceLogging API.<br /> TraceLogging builds on Event Tracing for Windows (ETW) and provides a simplified way to instrument code. TraceLogging allows you to include structured data with events, correlate events, and does not require a separate instrumentation manifest XML file.<br /><span class="underline">For WinRT developers</span><br /><ul><li><a href="/uwp/api/Windows.Foundation.Diagnostics.LoggingChannel"><strong>LoggingChannel</strong></a> has been extended in Windows 10 to log self-describing Event Tracing for Windows (ETW) events without the need for a manifest.</li><li><a href="/windows/win32/api/traceloggingactivity/nl-traceloggingactivity-traceloggingactivity"><strong>LoggingActivity</strong></a> has been extended in Windows 10 to provide activity start and stop methods that provide control over the format and contents of the Start and Stop events. Additionally, activities can be nested.</li></ul><span class="underline">For managed code (Microsoft .NET Framework) developers</span><br /><ul><li>The <a href="/dotnet/api/system.diagnostics.tracing.eventsource">EventSource</a> class that shipped with previous versions of the .NET Framework already supports writing ETW events without the need for a manifest. However, developers were required to use EventSource as a base class and add attributes and methods to the derived class that were turned into an ETW manifest automatically. Now, developers do not have to derive from EventSource and can instead use EventSource directly to log self-describing events that do not require a manifest.</li></ul><span class="underline">For C/C++ developers</span><br /><ul><li>TraceLoggingProvider.h is the recommended API for C/C++ developers in user or kernel mode. This API is not well suited for use in dynamic (scripted) scenarios such as Javascript. The following links describe the C/C++ API.</li></ul> | 




 

## Developer audience

TraceLogging is designed for use by user-mode application developers and kernel-mode driver developers who want to add tracing to their code.

