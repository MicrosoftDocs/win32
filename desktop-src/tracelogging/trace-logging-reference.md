---
title: TraceLogging Reference
description:
  The following topics provide information about the native TraceLogging
  API.TraceLogging builds on Event Tracing for Windows (ETW) and provides a
  simplified way to instrument code.
ms.assetid: 9E3F2140-DDB0-4C30-B7D0-A81F11823AA6
ms.topic: article
ms.date: 05/31/2018
---

# TraceLogging Reference

The following topics provide information about the native TraceLogging API.

TraceLogging builds on Event Tracing for Windows (ETW) and provides a simplified
way to instrument code. TraceLogging allows you to include structured data with
events, correlate events, and does not require a separate instrumentation
manifest XML file.

- **For WinRT developers:**

  [**LoggingChannel**](/uwp/api/Windows.Foundation.Diagnostics.LoggingChannel)
  has been extended in Windows 10 to log self-describing Event Tracing for
  Windows (ETW) events without the need for a manifest.

  [**LoggingActivity**](/windows/win32/api/traceloggingactivity/nl-traceloggingactivity-traceloggingactivity)
  has been extended in Windows 10 to provide activity start and stop methods
  that provide control over the format and contents of the Start and Stop
  events. Additionally, activities can be nested.

- **For managed code (Microsoft .NET Framework) developers:**

  The [EventSource](/dotnet/api/system.diagnostics.tracing.eventsource) class
  that shipped with previous versions of the .NET Framework already supports
  writing ETW events without the need for a manifest. However, developers were
  required to use EventSource as a base class and add attributes and methods to
  the derived class that were turned into an ETW manifest automatically. Now,
  developers do not have to derive from EventSource and can instead use
  EventSource directly to log self-describing events that do not require a
  manifest.

- **For C/C++ developers:**

  TraceLoggingProvider.h is the recommended API for C/C++ developers in user or
  kernel mode. This API is not well suited for use in dynamic (scripted)
  scenarios such as Javascript. The following links describe the C/C++ API.

  - [Classes](trace-logging-classes.md)
  - [Functions](trace-logging-functions.md)
  - [Macros](trace-logging-macros.md)

  Note that the value of WINVER will impact the way TraceLoggingProvider.h
  behaves.

  - If WINVER is not set before including `<windows.h>`, then `<windows.h>` will
    set WINVER to a default value corresponding to the SDK version.
  - Using TraceLoggingProvider.h with WINVER set to 0x0602 (Windows 8) or
    higher, the program will not run on Windows Vista or Windows 7.
  - Using TraceLoggingProvider.h with WINVER set to 0x0600 (Windows Vista) or
    0x0601 (Windows 7), the program will be configured for compatibility and
    will work on the specified versions of Windows.
