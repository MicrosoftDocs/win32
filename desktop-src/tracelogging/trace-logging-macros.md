---
title: TraceLogging Macros
description:
  TraceLogging defines the following macros that you can use to define a
  provider, log events, and create activities
ms.assetid: 412881F2-329E-4537-8CBF-0DF79DA181C5
ms.topic: article
ms.date: 06/06/2022
---

# TraceLogging Macros

TraceLogging defines the following macros that you can use to define a provider,
log events, and create activities:

- [**TraceLogging Wrapper Macros**](./tracelogging-wrapper-macros.md) configure
  the event that will be written by TraceLoggingWrite.
- [**TRACELOGGING_DECLARE_PROVIDER**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-tracelogging_declare_provider)
  forward-declares a handle for a TraceLogging provider.
- [**TRACELOGGING_DEFINE_PROVIDER**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-tracelogging_define_provider)
  defines a handle for a TraceLogging provider.
- [**TRACELOGGING_DEFINE_PROVIDER_STORAGE**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-tracelogging_define_provider_storage)
  reserves static storage for a TraceLogging provider handle that will be
  defined by the user for cases where **TRACELOGGING_DEFINE_PROVIDER** cannot be
  used.
- [**TraceLoggingFunction**](/windows/win32/api/traceloggingactivity/nf-traceloggingactivity-traceloggingfunction)
  creates a
  [TraceLoggingThreadActivity](/windows/win32/api/traceloggingactivity/nl-traceloggingactivity-traceloggingthreadactivity)
  named after the current function and writes a Start event for the activity. A
  Stop activity will be written at the end of the current scope.
- [**TraceLoggingWrite**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingwrite)
  emits a TraceLogging event.
- [**TraceLoggingWriteActivity**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingwriteactivity)
  emits a TraceLogging event with specified activity IDs.
- [**TraceLoggingWriteStart**](/windows/win32/api/traceloggingactivity/nf-traceloggingactivity-traceloggingwritestart)
  starts an activity and emits the start event.
- [**TraceLoggingWriteStop**](/windows/win32/api/traceloggingactivity/nf-traceloggingactivity-traceloggingwritestop)
  stops an activity and emits the stop event.
- [**TraceLoggingWriteTagged**](/windows/win32/api/traceloggingactivity/nf-traceloggingactivity-traceloggingwritetagged)
  emits a TraceLogging event with the activity ID from a TraceLoggingActivity
  class.

## Related topics

[About Event Tracing](../etw/about-event-tracing.md)

[TraceLogging](./trace-logging-portal.md)
