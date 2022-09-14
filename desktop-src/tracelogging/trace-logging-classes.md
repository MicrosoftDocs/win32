---
title: TraceLogging Classes
description:
  TraceLogging provides the following classes that provide support for logging
  Event Tracing for Windows (ETW) events during an activity
ms.assetid: 345898F5-20D1-4E3A-9827-8D7999BA77E2
ms.topic: article
ms.date: 06/06/2022
---

# TraceLogging Classes

The Windows SDK provides the following C++ classes that provide support for
logging TraceLogging events during an ETW activity:

- [**TraceLoggingActivity**](/windows/win32/api/traceloggingactivity/nl-traceloggingactivity-traceloggingactivity)
  helps manage a TraceLogging ETW activity where events are explicitly
  associated with the activity.
- [**TraceLoggingThreadActivity**](/windows/win32/api/traceloggingactivity/nl-traceloggingactivity-traceloggingthreadactivity)
  helps manage a TraceLogging ETW activity where events are implicitly
  associated with the activity based on the thread-local default activity ID.
- [**TraceLoggingThreadActivityIdSetter**](/windows/desktop/api/traceloggingactivity/nl-traceloggingactivity-traceloggingthreadactivityidsetter)
  helps set the thread-local default activity ID on scope entry and restore the
  original ID on scope exit.

## Related topics

[About Event Tracing](/windows/desktop/ETW/about-event-tracing)

[TraceLogging](trace-logging-portal.md)
