---
description: A private event tracing session is a user-mode event tracing session that runs in the same process as its event trace providers&\#8212;the private session and the providers that it enables must all be in the same process.
ms.assetid: fb6a3899-194e-4cb7-b9e5-a7ff85fb7891
title: Configuring and Starting a Private Logger Session
ms.topic: article
ms.date: 05/31/2018
---

# Configuring and Starting a Private Logger Session

A private event tracing session is a user-mode event tracing session that runs in the same process as its event trace providers—the private session and the providers that it enables must all be in the same process. The benefit of using a private session is that the private session does not count against the maximum of 64 event tracing sessions executing simultaneously.

Configuring and starting a private session is similar to starting a normal event trace session. The difference is that **Wnode.Guid** member of the [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure must contain the **GUID** of the provider, not the session, and the provider must have already registered the GUID. Note that if you also set the EVENT\_TRACE\_PRIVATE\_IN\_PROC logging mode, you can use a different **GUID** for the session and provider. For details on starting a normal event trace session, see [Configuring and Starting an Event Tracing Session](configuring-and-starting-an-event-tracing-session.md).

Note that you cannot start, stop, or flush a private trace session from DllMain; you should do so in the initialization and finalization routines of the DLL.

From Windows 8.1 to Windows 10, version 1607, event payload, scope, and stack walk filters can be used by the [**EnableTraceEx2**](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2) function and the [**ENABLE\_TRACE\_PARAMETERS**](/windows/win32/api/evntrace/ns-evntrace-enable_trace_parameters) and [**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-event_filter_descriptor) structures to filter on specific conditions in a logger session. For more information on event payload filters, see the [**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter), and [**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters) functions and the **ENABLE\_TRACE\_PARAMETERS**, **EVENT\_FILTER\_DESCRIPTOR**, and [**PAYLOAD\_FILTER\_PREDICATE**](/windows/desktop/api/Tdh/ns-tdh-payload_filter_predicate) structures.

Starting with Windows 10, version 1703, low privilege users can now start a private logger session in processes they started. The provider no longer needs to be registered prior to enabling or starting the private session, meaning the provider is "pre-enabled" similar to how non-private session providers are. There is a limit of 8 system wide private loggers to an individual process. For increased performance in cross process scenarios, it's recommended to use filtering for session APIs (including [**ControlTrace**](/windows/win32/api/evntrace/nf-evntrace-controltracea), [**QueryTrace**](/windows/win32/api/evntrace/nf-evntrace-querytracea), [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea), and [**StopTrace**](/windows/win32/api/evntrace/nf-evntrace-stoptracea)) when starting a system wide private logger. Note that the same filters should be passed to all session APIs. For more information about filters, see [**EVENT\_TRACE\_PROPERTIES\_V2**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties_v2).

For details on starting an event tracing session, see [Configuring and Starting an Event Tracing Session](configuring-and-starting-an-event-tracing-session.md).

For details on starting an NT Kernel Logger session, see [Configuring and Starting the NT Kernel Logger Session](configuring-and-starting-the-nt-kernel-logger-session.md).

For details on starting a Global Logger session, see [Configuring and Starting a Global Logger Session](configuring-and-starting-the-global-logger-session.md).

For details on starting an AutoLogger session, see [Configuring and Starting an AutoLogger Session](configuring-and-starting-an-autologger-session.md).

## Related topics

<dl> <dt>

[Configuring and Starting a SystemTraceProvider Session](configuring-and-starting-a-systemtraceprovider-session.md)
</dt> <dt>

[Configuring and Starting an AutoLogger Session](configuring-and-starting-an-autologger-session.md)
</dt> <dt>

[Configuring and Starting an Event Tracing Session](configuring-and-starting-an-event-tracing-session.md)
</dt> <dt>

[Configuring and Starting the NT Kernel Logger Session](configuring-and-starting-the-nt-kernel-logger-session.md)
</dt> <dt>

[**EnableTraceEx2**](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2)
</dt> <dt>

[**ENABLE\_TRACE\_PARAMETERS**](/windows/win32/api/evntrace/ns-evntrace-enable_trace_parameters)
</dt> <dt>

[**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties)
</dt> <dt>

[**EVENT\_TRACE\_PROPERTIES\_V2**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties_v2)
</dt> <dt>

[**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-event_filter_descriptor)
</dt> <dt>

[**PAYLOAD\_FILTER\_PREDICATE**](/windows/desktop/api/Tdh/ns-tdh-payload_filter_predicate)
</dt> <dt>

[**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters)
</dt> <dt>

[**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter)
</dt> <dt>

[Updating an Event Tracing Session](updating-an-event-tracing-session.md)
</dt> </dl>

 

 
