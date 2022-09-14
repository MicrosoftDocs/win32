---
title: TraceLogging Functions
description:
  TraceLogging provides the following functions that allow you to work with
  Event Tracing for Windows (ETW) providers
ms.assetid: 93CCBCDE-F010-476B-BC6F-887E7DCC0AB0
ms.topic: article
ms.date: 06/06/2022
---

# TraceLogging Functions

TraceLogging provides the following functions that allow you to work with Event
Tracing for Windows (ETW) providers:

- [**TraceLoggingProviderEnabled**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingproviderenabled)
  returns true if any consumer is listening for events from a TraceLogging
  provider.
- [**TraceLoggingProviderId**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingproviderid)
  returns the provider ID (aka control GUID) of a TraceLogging provider.
- [**TraceLoggingRegister**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingregister)
  opens a TraceLogging provider.
- [**TraceLoggingRegisterEx**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingregisterex)
  opens a TraceLogging provider with a callback.
- [**TraceLoggingSetInformation**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingsetinformation)
  configures extra settings on a TraceLogging provider.
- [**TraceLoggingUnregister**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingunregister)
  closes a TraceLogging provider.

## Related topics

[About Event Tracing](/windows/desktop/ETW/about-event-tracing)

[TraceLogging](trace-logging-portal.md)
