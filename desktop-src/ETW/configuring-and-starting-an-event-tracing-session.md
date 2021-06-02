---
description: To configure an event tracing session, use the EVENT\_TRACE\_PROPERTIES structure to specify the properties of the session.
ms.assetid: 8a6aa39c-ec81-42ac-a26e-29f1f6960220
title: Configuring and Starting an Event Tracing Session
ms.topic: article
ms.date: 05/31/2018
---

# Configuring and Starting an Event Tracing Session

To configure an event tracing session, use the [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure to specify the properties of the session. The memory you allocate for the **EVENT\_TRACE\_PROPERTIES** structure must be large enough to also contain the session and log file names that follow the structure in memory.

After you specify the properties of the session, call the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function to start the session. If the function succeeds, the *SessionHandle* parameter will contain the session handle, and the **LoggerNameOffset** property will contain the offset to the name of the session.

To enable the providers that you want to log events to your session, call the [**EnableTrace**](/windows/win32/api/evntrace/nf-evntrace-enabletrace) function to enable classic providers and the [**EnableTraceEx**](/windows/win32/api/evntrace/nf-evntrace-enabletraceex) function to enable [manifest-based](about-event-tracing.md) providers. To enable providers that you want log events to your session filtering on specific conditions on Windows 8.1,Windows Server 2012 R2, and later, call the [**EnableTraceEx2**](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2) function.

In addition, you can also trace additional information on an event with a call to the [**TraceSetInformation**](/windows/win32/api/evntrace/nf-evntrace-tracesetinformation) function. **TraceSetInformation** puts additional trace information into the extended data section of an event, and can include information such as the trace version info, or what providers are currently registered on the system. For more information, see [Retrieving Additional Event Tracing Data](retrieving-additional-event-tracing-data.md).

Up to eight trace sessions can enable and receive events from the same [manifest-based](about-event-tracing.md) provider. However, only one trace session can enable a [classic](about-event-tracing.md) provider. If more than one trace session tries to enable a classic provider, the first session would stop receiving events when the second session enables the provider. For example, if Session A enabled Provider 1 and then Session B enabled Provider 1, only Session B would receive events from Provider 1.

You can use any of the three functions to enable a provider but you may lose functionality if you use [**EnableTrace**](/windows/win32/api/evntrace/nf-evntrace-enabletrace) to enable a manifest-based provider because you will not be able to provide a MatchAllKeyword value, specify extended data items to include in the event, or provide provider-defined filter data. For more information, see the Remarks section of each function.

On Windows 8.1,Windows Server 2012 R2, and later, event payload , scope, and stack walk filters can be used by the [**EnableTraceEx2**](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2) function and the [**ENABLE\_TRACE\_PARAMETERS**](/windows/win32/api/evntrace/ns-evntrace-enable_trace_parameters) and [**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-event_filter_descriptor) structures to filter on specific conditions in a logger session. For more information on event payload filters, see the [**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter), and [**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters) functions and the **ENABLE\_TRACE\_PARAMETERS**, **EVENT\_FILTER\_DESCRIPTOR**, and [**PAYLOAD\_FILTER\_PREDICATE**](/windows/desktop/api/Tdh/ns-tdh-payload_filter_predicate) structures.

To determine the level and keywords used to enable a manifest-based provider, use one of the following commands:

-   **Logman** **query** *provider-name*
-   **Wevtutil** **gp** *provider-name*

The commands list the level and keywords only, the provider must document any filter data requirements for potential controllers.

To enumerate the manifest-based providers use **Wevtutil** **ep**.

For classic providers, it is up to the provider to document and make available to potential controllers the severity levels or enable flags that it supports. If the provider wants to be enabled by any controller, the provider should accept 0 for the severity level and enable flags and interpret 0 as a request to perform default logging (whatever that may be).

You can enable the provider before or after the provider registers itself. After enabling the provider, ETW will then call the provider's callback function. If the provider is not registered, ETW will call the provider's callback function after it registers itself.

You can also use the [**EnableTrace**](/windows/win32/api/evntrace/nf-evntrace-enabletrace) function to disable the provider (stop it from logging events to your session) or to update the logging level or enable flags of the provider. With the [**EnableTraceEx**](/windows/win32/api/evntrace/nf-evntrace-enabletraceex) function, you can disable the provider or update the level, keywords, extended data and filter data. Each time you call the **EnableTrace** or **EnableTraceEx** function, ETW calls the provider's callback function. The provider remains enabled for the session until the session disables the provider.

To stop the trace session after collecting events, call the [**ControlTrace**](/windows/win32/api/evntrace/nf-evntrace-controltracea) function and pass EVENT\_TRACE\_CONTROL\_STOP as the control code. To specify the session to stop, you can pass the event tracing session handle obtained from an earlier call to the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function, or the name of a previously started session. Be sure to disable all providers before stopping the session. If you stop the session before first disabling the provider, ETW will disable the provider and try to call the provider's control callback function. If the application that started the session ends without disabling the provider or calling the **ControlTrace** function, the provider remains enabled.

If [**ControlTrace**](/windows/win32/api/evntrace/nf-evntrace-controltracea) is successful, the session properties are updated to reflect the final property values and run statistics for the event tracing session.

For an example that starts an event tracing session, see the following:

-   [Example that Creates a Session and Enables a Manifest-based Provider](example-that-creates-a-session-and-enables-a-manifest-based-provider.md) - starts a trace session, enables a manifest-based provider, disables the provider and then stops the session.

For details on starting a trace session, see one of the following:

-   [Configuring and Starting a SystemTraceProvider Session](configuring-and-starting-a-systemtraceprovider-session.md)
-   [Configuring and Starting the NT Kernel Logger Session](configuring-and-starting-the-nt-kernel-logger-session.md)
-   [Configuring and Starting an AutoLogger Session](configuring-and-starting-an-autologger-session.md)
-   [Configuring and Starting the Global Logger Session](configuring-and-starting-the-global-logger-session.md)
-   [Configuring and Starting a Private Logger Session](configuring-and-starting-a-private-logger-session.md)

## Related topics

<dl> <dt>

[Configuring and Starting a Private Logger Session](configuring-and-starting-a-private-logger-session.md)
</dt> <dt>

[Configuring and Starting a SystemTraceProvider Session](configuring-and-starting-a-systemtraceprovider-session.md)
</dt> <dt>

[Configuring and Starting an AutoLogger Session](configuring-and-starting-an-autologger-session.md)
</dt> <dt>

[Configuring and Starting the NT Kernel Logger Session](configuring-and-starting-the-nt-kernel-logger-session.md)
</dt> <dt>

[**ControlTrace**](/windows/win32/api/evntrace/nf-evntrace-controltracea)
</dt> <dt>

[**EnableTrace**](/windows/win32/api/evntrace/nf-evntrace-enabletrace)
</dt> <dt>

[**EnableTraceEx**](/windows/win32/api/evntrace/nf-evntrace-enabletraceex)
</dt> <dt>

[**EnableTraceEx2**](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2)
</dt> <dt>

[**ENABLE\_TRACE\_PARAMETERS**](/windows/win32/api/evntrace/ns-evntrace-enable_trace_parameters)
</dt> <dt>

[**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-event_filter_descriptor)
</dt> <dt>

[**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties)
</dt> <dt>

[**PAYLOAD\_FILTER\_PREDICATE**](/windows/desktop/api/Tdh/ns-tdh-payload_filter_predicate)
</dt> <dt>

[**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea)
</dt> <dt>

[**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters)
</dt> <dt>

[**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter)
</dt> <dt>

[Updating an Event Tracing Session](updating-an-event-tracing-session.md)
</dt> </dl>

 

 
