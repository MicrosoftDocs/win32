---
Description: 'This section describes the new features that were added to Event Tracing for Windows in each release.'
ms.assetid: '5d94a6d2-2280-4a97-aa5a-c9ca2c016c84'
title: 'What''s New in Event Tracing'
---

# What's New in Event Tracing

This section describes the new features that were added to Event Tracing for Windows in each release.

## Windows 10, version 1709

ETW can now optionally track binaries for all providers that are enabled to the session. The tracking applies retroactively for providers that were enabled to the session prior to the call, as well as for all future providers that are enabled to the session. You can also now query for the currently-configured maximum number of system loggers allowed by the operating system. For more information, see the **TraceProviderBinaryTracking** and **TraceMaxLoggersQuery** values of the [**TRACE\_INFO\_CLASS**](trace-info-class.md) enumeration, as well as [Retrieving Additional Event Tracing Data](retrieving-additional-event-tracing-data.md).

ETW can now filter events based on event name. You can also determine which events get their stacks captured. For more information, see the **EVENT\_FILTER\_TYPE\_EVENT\_NAME**, **EVENT\_FILTER\_TYPE\_STACKWALK\_NAME** , and **EVENT\_FILTER\_TYPE\_STACKWALK\_LEVEL\_KW** values of the [**EVENT\_FILTER\_DESCRIPTOR**](event-filter-descriptor.md) structure, as well as the associated [**EVENT\_FILTER\_EVENT\_NAME**](event-filter-event-name.md) and [**EVENT\_FILTER\_LEVEL\_KW**](event-filter-level-kw.md) structures.

## Windows 10

[TraceLogging](tracelogging.trace_logging_portal) builds on ETW and provides a simplified way to instrument code for native, .NET and WinRT developers. TraceLogging allows you to include structured data with events, correlate events, and does not require a separate instrumentation manifest XML file.

[Provider Traits](provider-traits.md) were added as a method of attaching more data to an individual provider registration. They can be used for manifest-based or TraceLogging providers. This currently includes support for adding a Provider Name and/or a Provider Group to an individual provider registration. Provider Groups are a new feature to allow multiple ETW providers to be controlled in aggregate by the group they belong to.

Periodic capture state is a way to allow capture state notifications to be routinely sent to providers. When this is enabled, notifications will only be sent to provider registrations that have been previously enabled to the current session. Each provider can define its own response (if any) to a notification. For implementation details, see [**TRACE\_PERIODIC\_CAPTURE\_STATE\_INFO**](trace-periodic-capture-state-info.md).

## Windows 8.1 and Windows Server 2012 R2

The following features have been added to Event Tracing on Windows 8.1 and Windows Server 2012 R2.

Functions that support using event payload, scope, and stack walk filters used by the [**EnableTraceEx2**](enabletraceex2.md) function and the [**ENABLE\_TRACE\_PARAMETERS**](enable-trace-parameters.md) and [**EVENT\_FILTER\_DESCRIPTOR**](event-filter-descriptor.md) structures to filter on specific conditions in a logger session. For more information, see:

-   [**TdhAggregatePayloadFilters**](tdhaggregatepayloadfilters.md)
-   [**TdhCleanupPayloadEventFilterDescriptor**](tdhcleanuppayloadeventfilterdescriptor.md)
-   [**TdhCreatePayloadFilter**](tdhcreatepayloadfilter.md)
-   [**TdhDeletePayloadFilter**](tdhdeletepayloadfilter.md)

In addition, see the extensively revised documentation for the [**EnableTraceEx2**](enabletraceex2.md) function and the [**ENABLE\_TRACE\_PARAMETERS**](enable-trace-parameters.md) and [**EVENT\_FILTER\_DESCRIPTOR**](event-filter-descriptor.md) structures that are used by these features.

A structure that defines an event payload filter predicate that describes how to filter on a single field in a trace session used by the new [**TdhCreatePayloadFilter**](tdhcreatepayloadfilter.md) function and a new structure used by event ID and stack walk filters. For more information, see:

-   [**EVENT\_FILTER\_EVENT\_ID**](event-filter-event-id.md)
-   [**PAYLOAD\_FILTER\_PREDICATE**](payload-filter-predicate.md)

Functions that retrieve information on events present in the provider manifest. For more information, see:

-   [**TdhEnumerateManifestProviderEvents**](tdhenumeratemanifestproviderevents.md)
-   [**TdhGetManifestEventInformation**](tdhgetmanifesteventinformation.md)

A structure that defines an array of events in a provider manifest used by the new [**TdhEnumerateManifestProviderEvents**](tdhenumeratemanifestproviderevents.md) function. For more information, see:

-   [**PROVIDER\_EVENT\_INFO**](provider-event-info.md)

## Windows 8 and Windows Server 2012

The following features have been added to the Event Tracing on Windows 8 and Windows Server 2012.

Functions that performs operations on a registration object, provide event payload parsing, provide trace provider browsing, query event tracing session settings, and process a relogged trace file. For more information, see:

-   [**EventSetInformation**](eventsetinformation.md)
-   [**TdhCloseDecodingHandle**](tdhclosedecodinghandle.md)
-   [**TdhGetDecodingParameter**](tdhgetdecodingparameter.md)
-   [**TdhGetWppProperty**](tdhgetwppproperty.md)
-   [**TdhGetWppMessage**](tdhgetwppmessage.md)
-   [**TdhLoadManifestFromBinary**](tdhloadmanifestfrombinary.md)
-   [**TdhOpenDecodingHandle**](tdhopendecodinghandle.md)
-   [**TdhSetDecodingParameter**](tdhsetdecodingparameter.md)
-   [**TraceQueryInformation**](tracequeryinformation.md)

Interfaces that provide information to the relogger on the tracing process and when events are logged, access to data for a specific event, and access to relogger features that allow the manipulation of Event Trace Log (ETL) files. For more information, see:

-   [**ITraceEvent**](ievent.md)
-   [**ITraceEventCallback**](ieventcallback.md)
-   [**ITraceRelogger**](itracerelogger.md)

Additional enumerations used by the new functions and interfaces. For more information, see:

-   [**EVENT\_INFO\_CLASS**](event-info-class.md)
-   [**TRACE\_QUERY\_INFO\_CLASS**](etw.trace_query_info_class)

## Windows 7 and Windows Server 2008 R2

The following features were added in this release:

-   The ability for providers to define filters in the manifest. In Windows Vista, controllers could pass filter data to the provider. However, the layout of the filter data was not defined in the manifest, so the provider would have to use other means to provide the filter definition to controllers. With this release, providers can define the filter definition in the manifest (see the **filters** attribute of the [**ProviderType**](wes.eventmanifestschema_providertype_complextype) complex type). Controllers can then use the [**TdhEnumerateProviderFilters**](tdhenumerateproviderfilters.md) function to determine the filter definition. Providers that use filters should use the [**EventWriteEx**](eventwriteex.md) function to write the event.
-   The ability to use a single buffer to gather events generated on multiple processors. Using a single buffer eliminates events from appearing out of order on multi-processors computers. For details, see the [**EVENT\_TRACE\_NO\_PER\_PROCESSOR\_BUFFERING**](logging-mode-constants.md) logging mode. By default, ETW uses per-processor buffers.
-   The ability to capture a stack trace for events. To enable stack tracing for kernel events, see the [**TraceSetInformation**](tracesetinformation.md) function. To enable stack tracing for user events, see the **EVENT\_ENABLE\_PROPERTY\_STACK\_TRACE** flag for the **EnableProperty** member of [**ENABLE\_TRACE\_PARAMETERS**](enable-trace-parameters.md).
-   The ability to specify the **EVENT\_TRACE\_BUFFERING\_MODE** or **EVENT\_TRACE\_FILE\_MODE\_NEWFILE** logging mode with the **EVENT\_TRACE\_PRIVATE\_LOGGER\_MODE** logging mode (see [Logging Mode Constants](logging-mode-constants.md)).
-   The ability to enable a provider synchronously. By default, providers are enabled asynchronously. To enable a provider synchronously, set the *Timeout* parameter of [**EnableTraceEx2**](enabletraceex2.md).
-   The ability for the controller to request that the provider log its state. For details, see the **EVENT\_CONTROL\_CODE\_CAPTURE\_STATE** flag for the *ControlCode* parameter of [**EnableTraceEx2**](enabletraceex2.md).
-   The ability for consumers to format event data using the [**TdhFormatProperty**](tdhformatproperty.md) function.
-   The ability to decode manifested events on computers that do not contain the provider. For details, see the [**TdhLoadManifest**](tdhloadmanifest.md) function.

The following functions were added in this release:

-   [**EnableTraceEx2**](enabletraceex2.md)
-   [**EventWriteEx**](eventwriteex.md)
-   [**TdhEnumerateProviderFilters**](tdhenumerateproviderfilters.md)
-   [**TdhFormatProperty**](tdhformatproperty.md)
-   [**TdhLoadManifest**](tdhloadmanifest.md)
-   [**TdhUnloadManifest**](tdhunloadmanifest.md)
-   [**TraceSetInformation**](tracesetinformation.md)

The following structures were added in this release:

-   [**CLASSIC\_EVENT\_ID**](classic-event-id.md)
-   [**ENABLE\_TRACE\_PARAMETERS**](enable-trace-parameters.md)
-   [**EVENT\_EXTENDED\_ITEM\_STACK\_TRACE32**](event-extended-item-stack-trace32.md)
-   [**EVENT\_EXTENDED\_ITEM\_STACK\_TRACE64**](event-extended-item-stack-trace64.md)
-   [**EVENT\_FILTER\_HEADER**](event-filter-header.md)
-   [**PROVIDER\_FILTER\_INFO**](provider-filter-info.md)

The following enumerations were added in this release:

-   [**TRACE\_INFO\_CLASS**](trace-info-class.md)

The following MOF classes were added in this release:

-   [**StackWalk**](stackwalk.md)
-   [**StackWalk\_Event**](stackwalk-event.md)

 

 



