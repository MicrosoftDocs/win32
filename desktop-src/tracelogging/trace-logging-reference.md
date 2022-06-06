---
title: TraceLogging Reference
description:
  The following topics provide information about the native TraceLogging
  API.TraceLogging builds on Event Tracing for Windows (ETW) and provides a
  simplified way to instrument code.
ms.assetid: 9E3F2140-DDB0-4C30-B7D0-A81F11823AA6
ms.topic: article
ms.date: 06/06/2022
---

# TraceLogging Reference

The following topics provide information about the C/C++ TraceLogging API.

> [!NOTE]
> This reference describes C/C++ TraceLogging APIs designed for use when
> the events are known at compile time. If you are generating events from .NET
> code, use the .NET
> [**EventSource**](/dotnet/api/system.diagnostics.tracing.eventsource) class.
> Otherwise, if you are using Windows Runtime (WinRT), use
> [**LoggingChannel**](/uwp/api/Windows.Foundation.Diagnostics.LoggingChannel).
> Otherwise, you might be able to use a community-supported option such as
> [**TraceLoggingDynamic**](https://github.com/microsoft/tracelogging/tree/main/etw).

TraceLogging builds on Event Tracing for Windows (ETW) and is easier to use than
manifest-based ETW or WPP. TraceLogging allows you to generate events that
include structured data, supports event correlation using ETW activities, and
does not require a separate instrumentation manifest XML file for decoding.

TraceLoggingProvider.h is the recommended API for C/C++ developers in user or
kernel mode. The following links describe the C/C++ API.

- [Classes](trace-logging-classes.md)
- [Functions](trace-logging-functions.md)
- [Macros](trace-logging-macros.md)

Note that the value of WINVER (user-mode) will affect the way
TraceLoggingProvider.h behaves:

- If WINVER is not set before including `<windows.h>`, then `<windows.h>` will
  set WINVER to a default value corresponding to the SDK version.
- If you use TraceLoggingProvider.h with WINVER set to 0x0602 (Windows 8) or
  higher, the program may not run on Windows Vista or Windows 7.
- If you use TraceLoggingProvider.h with WINVER set to 0x0600 (Windows Vista) or
  0x0601 (Windows 7), the program will be configured for compatibility and will
  work on the specified versions of Windows.
