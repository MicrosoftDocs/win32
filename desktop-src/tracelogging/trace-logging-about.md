---
title: About TraceLogging
description:
  TraceLogging is the new Windows 10 event tracing for user-mode applications
  and kernel-mode drivers.
ms.assetid: 8C6A9E91-98F9-4D6B-A937-A22BA7CEB1E4
ms.topic: article
ms.date: 05/31/2018
---

# About TraceLogging

TraceLogging is the new Windows 10 event tracing for user-mode applications and
kernel-mode drivers. TraceLogging is a format for self-describing Event Tracing
for Windows (ETW). TraceLogging builds on Event Tracing for Windows (ETW) and
provides a simplified way to instrument code.

TraceLogging offers the simplicity of Windows software trace preprocessor (WPP)
with the added benefit of being able to include structured data with events, the
capability of correlating events, and all without requiring a separate
instrumentation manifest XML file. Events are self-describing which means that a
binary containing the instrumentation manifest does not need to be registered on
the system in order to use the Trace Data Helper (TDH) APIs to decode and show
events.

Event Tracing for Windows (ETW) was introduced with Windows 2000 and updated in
Windows Vista. Tracelogging builds on top of the Windows Vista ETW APIs.
Providers can use the TraceLogging technology and still work on Windows Vista.
Existing controllers (using Windows VistaAPIs) can be used to control
TraceLogging providers.

TraceLogging is also compatible with existing tools. Providers that use
manifest-based ETW are still supported. You do not need to convert manifest
based ETW providers to TraceLogging providers unless you wish to take advantage
of the simplicity that TraceLogging provides. WPP tracing is also still
supported.

TraceLogging builds upon ETW but introduces several important improvements:

- Tracing an event is as simple as an API call.
- Events are self-describing and do not require any additional binaries
  containing the compiled event manifest to interpret the event. All the
  metadata about the event is recorded in the event.
- Activities inside a single process can be easily expressed through start and
  stop events.
- TraceLogging is compatible with existing instrumentation support. The new ETW
  APIs continue to support the old providers. You can invest in the new ETW APIs
  for strategic scenarios while leaving your old instrumentation points as they
  are.
- TraceLogging offers the same event tracing API for Windows 10, Xbox One, and
  Windows 10 Mobile.
- TraceLogging APIs are accessible from C, C++, .NET, and Windows Runtime.

## API high-level overview

There are three separate TraceLogging APIs that target different developer
audiences. Each API was designed to meet different sets of requirements as
appropriate for the target audience of that API.

For WinRT developers:

- [**LoggingChannel**](/uwp/api/Windows.Foundation.Diagnostics.LoggingChannel)
  has been extended in Windows 10 to log self-describing Event Tracing for
  Windows (ETW) events without the need for a manifest.
- [**LoggingActivity**](/windows/win32/api/traceloggingactivity/nl-traceloggingactivity-traceloggingactivity)
  has been extended in Windows 10 to provide activity start and stop methods
  that provide control over the format and contents of the Start and Stop
  events. Additionally, activities can be nested.

For C/C++ developers:

- TraceLoggingProvider.h contains the most efficient API, however this API is
  not well suited for use in dynamic (scripted) scenarios such as Javascript.
  This API can be used in user-mode and kernel-mode code.

For managed code (Microsoft .NET Framework) developers:

- The [EventSource](/dotnet/api/system.diagnostics.tracing.eventsource) class
  that shipped with previous versions of the .NET Framework already supported
  writing ETW events - automatically generating the manifest and embedding the
  manifest into the event stream. However, the developer still had to keep track
  of the manifest to decode the events (unless working in a scenario where the
  embedded manifest was supported). TraceLogging allows the manifest to be
  eliminated completely.

## Related topics

[About Event Tracing](/windows/desktop/ETW/about-event-tracing)
