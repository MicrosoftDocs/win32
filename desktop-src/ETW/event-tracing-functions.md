---
Description: Event trace controllers use the following functions to manage event tracing sessions.
ms.assetid: 6f0f1173-19e1-4aec-b6a6-77f18f819c30
title: Event Tracing Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Event Tracing Functions

Event trace controllers use the following functions to manage event tracing sessions.



| Controller function                                              | Description                                                                                                                                                  |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ControlTrace**](controltrace.md)                             | Flushes, queries, updates, or stops the specified session.                                                                                                   |
| [**EnableTrace**](enabletrace.md)                               | Enables or disables a classic event trace provider.                                                                                                          |
| [**EnableTraceEx**](enabletraceex-func.md)                      | Enables or disables a manifested event trace provider.                                                                                                       |
| [**EnableTraceEx2**](enabletraceex2.md)                         | Enables or disables a manifested event trace provider.                                                                                                       |
| [**EnumerateTraceGuids**](enumeratetraceguids.md)               | Retrieves information about registered event trace providers.                                                                                                |
| [**EnumerateTraceGuidsEx**](enumeratetraceguidsex.md)           | Retrieves information about registered event trace providers that are running on the computer.                                                               |
| [**FlushTrace**](flushtrace.md)                                 | Flushes buffered events for the specified session.The [**ControlTrace**](controltrace.md) function supersedes this function.<br/>                     |
| [**QueryAllTraces**](queryalltraces.md)                         | Retrieves property settings and statistics for all sessions.                                                                                                 |
| [**QueryTrace**](querytrace.md)                                 | Retrieves property settings and statistics for the specified session. The [**ControlTrace**](controltrace.md) function supersedes this function.<br/> |
| [**QueryTraceProcessingHandle**](querytraceprocessinghandle.md) | Retrieves container information from the specified session.                                                                                                  |
| [**StartTrace**](starttrace.md)                                 | Starts the specified session.                                                                                                                                |
| [**StopTrace**](stoptrace.md)                                   | Stops the specified session. The [**ControlTrace**](controltrace.md) function supersedes this function.<br/>                                          |
| [**TraceQueryInformation**](tracequeryinformation.md)           | Queries event tracing session settings for the specified information class.                                                                                  |
| [**TraceSetInformation**](tracesetinformation.md)               | Enables or disables the specified information class.                                                                                                         |
| [**UpdateTrace**](updatetrace.md)                               | Updates the properties of the specified session. The [**ControlTrace**](controltrace.md) function supersedes this function.<br/>                      |



 

[Classic](about-event-tracing.md#providers) event trace providers use the following functions to generate events.



| Provider function                                                            | Description                                                                                                  |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**ControlCallback**](controlcallback.md)                                   | Providers implement this callback to receive enable or disable event tracing notifications from controllers. |
| [**CreateTraceInstanceId**](createtraceinstanceid.md)                       | Creates an identifier for a group of related events.                                                         |
| [**GetTraceEnableFlags**](gettraceenableflags.md)                           | Retrieves the enable flags set by the [**EnableTrace**](enabletrace.md) function.                           |
| [**GetTraceEnableLevel**](gettraceenablelevel.md)                           | Retrieves the enable level set by the [**EnableTrace**](enabletrace.md) function.                           |
| [**GetTraceLoggerHandle**](gettraceloggerhandle.md)                         | Retrieves the event tracing session handle passed to the [**EnableTrace**](enabletrace.md) function.        |
| [**RegisterTraceGuids**](registertraceguids.md)                             | Registers a provider and its event trace classes.                                                            |
| [**TraceEvent**](traceevent.md)                                             | Generates an event.                                                                                          |
| [**TraceEventInstance**](traceeventinstance.md)                             | Generates events for a transaction.                                                                          |
| [**TraceMessage**](tracemessage.md)[**TraceMessageVa**](tracemessageva.md) | Generates informational messages.                                                                            |
| [**UnregisterTraceGuids**](unregistertraceguids.md)                         | Unregisters a provider and its event trace classes.                                                          |



 

[Manifest-based](about-event-tracing.md#providers) event trace providers use the following functions to generate events.



| Provider function                                             | Description                                                                                                                            |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**CveEventWrite**](/windows/desktop/api/SecurityBaseAPI/nf-securitybaseapi-cveeventwrite)                        | A tracing function for publishing events when an attempted security vulnerability exploit is detected in your user-mode application.   |
| [**EnableCallback**](/windows/desktop/api/Evntprov/nc-evntprov-penablecallback)                      | Providers implement this callback to receive enable or disable event tracing notifications from controllers.                           |
| [**EventActivityIdControl**](/windows/desktop/api/Evntprov/nf-evntprov-eventactivityidcontrol) | Creates, queries, and sets the current activity identifier used by the [**EventWriteTransfer**](/windows/desktop/api/Evntprov/nf-evntprov-eventwritetransfer) function. |
| [**EventEnabled**](/windows/desktop/api/Evntprov/nf-evntprov-eventenabled)                     | Determines if the event is enabled for any session.                                                                                    |
| [**EventProviderEnabled**](/windows/desktop/api/Evntprov/nf-evntprov-eventproviderenabled)     | Determines if the event is enabled for any session.                                                                                    |
| [**EventRegister**](/windows/desktop/api/Evntprov/nf-evntprov-eventregister)                   | Registers the provider.                                                                                                                |
| [**EventSetInformation**](/windows/desktop/api/Evntprov/nf-evntprov-eventsetinformation)            | Performs operations on a registration object.                                                                                          |
| [**EventUnregister**](/windows/desktop/api/Evntprov/nf-evntprov-eventunregister)               | Removes the provider's registration.                                                                                                   |
| [**EventWrite**](/windows/desktop/api/Evntprov/nf-evntprov-eventwrite)                         | Writes an event. This function is superseded by [**EventWriteEx**](/windows/desktop/api/Evntprov/nf-evntprov-eventwriteex).                                                  |
| [**EventWriteEx**](/windows/desktop/api/Evntprov/nf-evntprov-eventwriteex)                          | Writes an event.                                                                                                                       |
| [**EventWriteString**](/windows/desktop/api/Evntprov/nf-evntprov-eventwritestring)             | Writes an event that contains a string as its data.                                                                                    |
| [**EventWriteTransfer**](/windows/desktop/api/Evntprov/nf-evntprov-eventwritetransfer)         | Links events together when tracing events in an end-to-end scenario.                                                                   |



 

Event trace consumers use the following functions to process events.



| Consumer function                                                                         | Description                                                                                                                                                |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BufferCallback**](buffercallback.md)                                                  | Consumers implement this callback to receive statistics about each buffer of events that ETW delivers to an event trace consumer.                          |
| [**CloseTrace**](closetrace.md)                                                          | Closes a trace.                                                                                                                                            |
| [**EventCallback**](eventcallback.md)                                                    | Consumers implement this callback to receive all events from a session.                                                                                    |
| [**EventRecordCallback**](eventrecordcallback.md)                                        | Consumers implement this callback to receive events from a session.                                                                                        |
| [**OpenTrace**](opentrace.md)                                                            | Opens a trace for processing.                                                                                                                              |
| [**ProcessTrace**](processtrace.md)                                                      | Delivers events to a consumer for processing.                                                                                                              |
| [**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters)                          | Aggregates multiple payload filters for a single provider into a single data structure for use with the [**EnableTraceEx2**](enabletraceex2.md) function. |
| [**TdhCleanupPayloadEventFilterDescriptor**](/windows/desktop/api/Tdh/nf-tdh-tdhcleanuppayloadeventfilterdescriptor)  | Frees the aggregated structure of payload filters created using the [**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters) function.             |
| [**TdhCloseDecodingHandle**](/windows/desktop/api/Tdh/nf-tdh-tdhclosedecodinghandle)                                  | Frees resources associated with the input decoding handle.                                                                                                 |
| [**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter)                                  | Creates a single filter for a single payload to be used with the [**EnableTraceEx2**](enabletraceex2.md) function.                                        |
| [**TdhDeletePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhdeletepayloadfilter)                                  | Frees the memory allocated for a single payload filter by the [**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter) function.                           |
| [**TdhEnumerateManifestProviderEvents**](/windows/desktop/api/Tdh/nf-tdh-tdhenumeratemanifestproviderevents)          | Retrieves the list of events present in the provider manifest.                                                                                             |
| [**TdhEnumerateProviderFieldInformation**](/windows/desktop/api/Tdh/nf-tdh-tdhenumerateproviderfieldinformation) | Retrieves the specified field metadata for a given provider.                                                                                               |
| [**TdhEnumerateProviderFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhenumerateproviderfilters)                        | Enumerates the filters for a given provider.                                                                                                               |
| [**TdhEnumerateProviders**](/windows/desktop/api/Tdh/nf-tdh-tdhenumerateproviders)                               | Retrieves a list of providers that have registered a MOF or manifest file on the computer.                                                                 |
| [**TdhFormatProperty**](/windows/desktop/api/Tdh/nf-tdh-tdhformatproperty)                                            | Formats a property value for display.                                                                                                                      |
| [**TdhGetDecodingParameter**](/windows/desktop/api/Tdh/nf-tdh-tdhgetdecodingparameter)                                | Retrieves the value of a decoding parameter.                                                                                                               |
| [**TdhGetEventInformation**](/windows/desktop/api/Tdh/nf-tdh-tdhgeteventinformation)                             | Retrieves metadata about an event.                                                                                                                         |
| [**TdhGetEventMapInformation**](/windows/desktop/api/Tdh/nf-tdh-tdhgeteventmapinformation)                       | Retrieves information about the event map contained in the event.                                                                                          |
| [**TdhGetManifestEventInformation**](/windows/desktop/api/Tdh/nf-tdh-tdhgetmanifesteventinformation)                  | Retrieves metadata about an event in a manifest.                                                                                                           |
| [**TdhGetProperty**](/windows/desktop/api/Tdh/nf-tdh-tdhgetproperty)                                             | Retrieves a property value from the event data.                                                                                                            |
| [**TdhGetPropertySize**](/windows/desktop/api/Tdh/nf-tdh-tdhgetpropertysize)                                     | Retrieves the size of one or more property values in the event data.                                                                                       |
| [**TdhGetWppMessage**](/windows/desktop/api/Tdh/nf-tdh-tdhgetwppmessage)                                              | Retrieves the formatted WPP message embedded into an [**EVENT\_RECORD**](/windows/desktop/api/relogger/ns-evntcons-_event_record) structure.                                                      |
| [**TdhGetWppProperty**](/windows/desktop/api/Tdh/nf-tdh-tdhgetwppproperty)                                            | Retrieves a specific property associated with a WPP message.                                                                                               |
| [**TdhLoadManifest**](/windows/desktop/api/Tdh/nf-tdh-tdhloadmanifest)                                                | Loads the manifest used to decode a log file.                                                                                                              |
| [**TdhLoadManifestFromBinary**](/windows/desktop/api/Tdh/nf-tdh-tdhloadmanifestfrombinary)                            | Takes a NULL-terminated path to a binary file that contains metadata resources needed to decode a specific event provider.                                 |
| [**TdhOpenDecodingHandle**](/windows/desktop/api/Tdh/nf-tdh-tdhopendecodinghandle)                                    | Opens a decoding handle.                                                                                                                                   |
| [**TdhQueryProviderFieldInformation**](/windows/desktop/api/Tdh/nf-tdh-tdhqueryproviderfieldinformation)         | Retrieves information for the specified field from the event descriptions for those field values that match the given value.                               |
| [**TdhSetDecodingParameter**](/windows/desktop/api/Tdh/nf-tdh-tdhsetdecodingparameter)                                | Sets the value of a decoding parameter.                                                                                                                    |
| [**TdhUnloadManifest**](/windows/desktop/api/Tdh/nf-tdh-tdhunloadmanifest)                                            | Unloads the manifest that was loaded by the [**TdhLoadManifest**](/windows/desktop/api/Tdh/nf-tdh-tdhloadmanifest) function.                                                           |



 

The following functions manage access permissions to the controller and provider functions.



| Access control function                               | Description                                                                            |
|-------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**EventAccessControl**](/windows/desktop/api/Evntcons/nf-evntcons-eventaccesscontrol) | Adds or modifies the permissions of the specified provider or session.                 |
| [**EventAccessQuery**](/windows/desktop/api/Evntcons/nf-evntcons-eventaccessquery)     | Retrieves the permissions for the specified controller or provider.                    |
| [**EventAccessRemove**](/windows/desktop/api/Evntcons/nf-evntcons-eventaccessremove)   | Removes the permissions defined in the registry for the specified provider or session. |



 

You should not use the following functions; they may be unavailable in subsequent versions.



| Access control function                            | Description                                                                                                                   |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**EventClassCallback**](eventclasscallback.md)   | Consumers implement this callback to receive events for a specific event trace class from a session.                          |
| [**RemoveTraceCallback**](removetracecallback.md) | Stops an [**EventClassCallback**](eventclasscallback.md) function from receiving events for an event trace class.            |
| [**SetTraceCallback**](settracecallback.md)       | Specifies an [**EventClassCallback**](eventclasscallback.md) function to receive events for the specified event trace class. |



 

 

 




