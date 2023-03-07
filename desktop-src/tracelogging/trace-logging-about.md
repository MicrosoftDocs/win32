---
title: About TraceLogging
description:
  TraceLogging is the new Windows 10 event tracing for user-mode applications
  and kernel-mode drivers.
ms.assetid: 8C6A9E91-98F9-4D6B-A937-A22BA7CEB1E4
ms.topic: article
ms.date: 06/06/2022
---

# About TraceLogging

TraceLogging is a system for logging events that can be decoded without a
manifest. On Windows, TraceLogging is used in both user-mode and kernel-mode
components to generate
[Event Tracing for Windows (ETW)](../etw/about-event-tracing.md) events.
TraceLogging builds on Event Tracing for Windows (ETW) and provides a simplified
way to instrument code.

Event Tracing for Windows (ETW) was introduced with Windows 2000 and updated in
Windows Vista. TraceLogging builds on the Windows Vista ETW APIs. Providers can
use TraceLogging when running on Windows Vista or later. Existing ETW trace
controllers can be used to control TraceLogging providers and capture traces
using Windows Vista APIs. Existing ETW trace decoders that use TDH decoding APIs
can decode TraceLogging events when running on Windows 10 or later.

TraceLogging offers several benefits:

- Simplicity of defining events directly in code, similar to WPP but without the
  need for a preprocessing tool.
- Structured data: named fields with types, support for arrays and structures.
- Event correlation through
  [ETW activities](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingopcode).
- All the decoding information for the event is included within the event
  itself, so no additional files needed to decode.
- TraceLogging event provider APIs are available for
  [C/C++](/windows/win32/api/traceloggingprovider/),
  [.NET](/dotnet/api/system.diagnostics.tracing.eventsource), and
  [Windows Runtime (WinRT)](/uwp/api/Windows.Foundation.Diagnostics.LoggingChannel).
  External support available for [Python](https://github.com/microsoft/tracelogging/tree/main/etw/python/traceloggingdynamic), Rust, etc.

While TraceLogging provides several benefits and should be considered for new
tracing, manifest-based ETW is still appropriate for many scenarios.

- If your events are targeting one of the legacy Windows Logs in Windows Event
  Log (e.g. the System or Application logs), continue to use manifest-based ETW.
- If trace file size is an important consideration, continue to use
  manifest-based ETW. TraceLogging events include the event strings (provider
  name, event name, and field names) inside each event and are usually larger
  than the equivalent manifest-based event.
- If you have a large investment in an existing trace technology, there is no
  requirement to switch to TraceLogging.
- Otherwise, consider using TraceLogging as it offers a simpler experience for
  the developer and the event consumer.

## API high-level overview

There are multiple TraceLogging APIs, each targeting different developer
audiences.

- If you need to generate events from C or C++ code,
  [**TraceLoggingProvider.h**](/windows/win32/api/traceloggingprovider/)
  provides an efficient API for generating TraceLogging events from user-mode or
  kernel-mode code. The events must be defined at compile-time.
- Otherwise, if you need to generate events from .NET code, the .NET
  [**EventSource**](/dotnet/api/system.diagnostics.tracing.eventsource) class
  supports generating both manifest-based and TraceLogging-based ETW events. The
  events must be defined at compile-time.
- Otherwise, if you are using the Windows Runtime (WinRT),
  [**LoggingChannel**](/uwp/api/Windows.Foundation.Diagnostics.LoggingChannel)
  has been extended in Windows 10 to log TraceLogging events.
- Otherwise, you might be able to use a community-supported option such as
  [**TraceLoggingDynamic**](https://github.com/microsoft/tracelogging/tree/main/etw).

## Related topics

[About Event Tracing](../etw/about-event-tracing.md)
