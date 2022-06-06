---
title: TraceLogging
description: TraceLogging
ms.assetid: c516424a-9eba-4b56-80de-8c713fd3461a
ms.topic: article
ms.date: 05/31/2018
---

# TraceLogging

## Purpose

TraceLogging is the new Windows 10 event tracing framework for user-mode
applications and kernel-mode drivers. TraceLogging builds on Event Tracing for
Windows (ETW) and provides a simplified way to instrument code.

## In this section

- [**About TraceLogging**](./trace-logging-about.md)

  TraceLogging is the new Windows 10 event tracing for user-mode applications
  and kernel-mode drivers. TraceLogging is a format for self-describing Event
  Tracing for Windows (ETW). TraceLogging builds on Event Tracing for Windows
  (ETW) and provides a simplified way to instrument code.

- [**Using TraceLogging**](./tracelogging-using-tracelogging.md)

  These topics provide a TraceLogging quick start for native and managed code,
  with examples.

- [**TraceLogging Reference**](./trace-logging-reference.md)

  These topics provide information about the native TraceLogging API.

  TraceLogging builds on Event Tracing for Windows (ETW) and provides a
  simplified way to instrument code. TraceLogging allows you to include
  structured data with events, correlate events, and does not require a separate
  instrumentation manifest XML file.

  - **For WinRT developers:**

    [**LoggingChannel**](/uwp/api/Windows.Foundation.Diagnostics.LoggingChannel)
    has been extended in Windows 10 to log self-describing Event Tracing for
    Windows (ETW) events without the need for a manifest.

    [**LoggingActivity**](/windows/win32/api/traceloggingactivity/nl-traceloggingactivity-traceloggingactivity)
    has been extended in Windows 10 to provide activity start and stop methods
    that provide control over the format and contents of the Start and Stop
    events. Additionally, activities can be nested.

  - **For managed code (Microsoft .NET Framework) developers:**

    The [**EventSource**](/dotnet/api/system.diagnostics.tracing.eventsource)
    class that shipped with previous versions of the .NET Framework already
    supports writing ETW events without the need for a manifest. However,
    developers were required to use EventSource as a base class and add
    attributes and methods to the derived class that were turned into an ETW
    manifest automatically. Now, developers do not have to derive from
    EventSource and can instead use EventSource directly to log self-describing
    events that do not require a manifest.

  - **For C/C++ developers:**

    [**TraceLoggingProvider.h**](/windows/win32/api/traceloggingprovider/) is
    the recommended API for C/C++ developers in user or kernel mode.

## Developer audience

TraceLogging is designed for use by user-mode application developers and
kernel-mode driver developers who want to add tracing to their code.
