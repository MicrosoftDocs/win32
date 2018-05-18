---
Description: 'Event trace controllers use the following functions to manage event tracing sessions.'
ms.assetid: '6f0f1173-19e1-4aec-b6a6-77f18f819c30'
title: Event Tracing Functions
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
| [**CveEventWrite**](cveeventwrite.md)                        | A tracing function for publishing events when an attempted security vulnerability exploit is detected in your user-mode application.   |
| [**EnableCallback**](enablecallback.md)                      | Providers implement this callback to receive enable or disable event tracing notifications from controllers.                           |
| [**EventActivityIdControl**](eventactivityidcontrol-func.md) | Creates, queries, and sets the current activity identifier used by the [**EventWriteTransfer**](eventwritetransfer-func.md) function. |
| [**EventEnabled**](eventenabled-func.md)                     | Determines if the event is enabled for any session.                                                                                    |
| [**EventProviderEnabled**](eventproviderenabled-func.md)     | Determines if the event is enabled for any session.                                                                                    |
| [**EventRegister**](eventregister-func.md)                   | Registers the provider.                                                                                                                |
| [**EventSetInformation**](eventsetinformation.md)            | Performs operations on a registration object.                                                                                          |
| [**EventUnregister**](eventunregister-func.md)               | Removes the provider's registration.                                                                                                   |
| [**EventWrite**](eventwrite-func.md)                         | Writes an event. This function is superseded by [**EventWriteEx**](eventwriteex.md).                                                  |
| [**EventWriteEx**](eventwriteex.md)                          | Writes an event.                                                                                                                       |
| [**EventWriteString**](eventwritestring-func.md)             | Writes an event that contains a string as its data.                                                                                    |
| [**EventWriteTransfer**](eventwritetransfer-func.md)         | Links events together when tracing events in an end-to-end scenario.                                                                   |



 

Event trace consumers use the following functions to process events.



| Consumer function                                                                         | Description                                                                                                                                                |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BufferCallback**](buffercallback.md)                                                  | Consumers implement this callback to receive statistics about each buffer of events that ETW delivers to an event trace consumer.                          |
| [**CloseTrace**](closetrace.md)                                                          | Closes a trace.                                                                                                                                            |
| [**EventCallback**](eventcallback.md)                                                    | Consumers implement this callback to receive all events from a session.                                                                                    |
| [**EventRecordCallback**](eventrecordcallback.md)                                        | Consumers implement this callback to receive events from a session.                                                                                        |
| [**OpenTrace**](opentrace.md)                                                            | Opens a trace for processing.                                                                                                                              |
| [**ProcessTrace**](processtrace.md)                                                      | Delivers events to a consumer for processing.                                                                                                              |
| [**TdhAggregatePayloadFilters**](tdhaggregatepayloadfilters.md)                          | Aggregates multiple payload filters for a single provider into a single data structure for use with the [**EnableTraceEx2**](enabletraceex2.md) function. |
| [**TdhCleanupPayloadEventFilterDescriptor**](tdhcleanuppayloadeventfilterdescriptor.md)  | Frees the aggregated structure of payload filters created using the [**TdhAggregatePayloadFilters**](tdhaggregatepayloadfilters.md) function.             |
| [**TdhCloseDecodingHandle**](tdhclosedecodinghandle.md)                                  | Frees resources associated with the input decoding handle.                                                                                                 |
| [**TdhCreatePayloadFilter**](tdhcreatepayloadfilter.md)                                  | Creates a single filter for a single payload to be used with the [**EnableTraceEx2**](enabletraceex2.md) function.                                        |
| [**TdhDeletePayloadFilter**](tdhdeletepayloadfilter.md)                                  | Frees the memory allocated for a single payload filter by the [**TdhCreatePayloadFilter**](tdhcreatepayloadfilter.md) function.                           |
| [**TdhEnumerateManifestProviderEvents**](tdhenumeratemanifestproviderevents.md)          | Retrieves the list of events present in the provider manifest.                                                                                             |
| [**TdhEnumerateProviderFieldInformation**](tdhenumerateproviderfieldinformation-func.md) | Retrieves the specified field metadata for a given provider.                                                                                               |
| [**TdhEnumerateProviderFilters**](tdhenumerateproviderfilters.md)                        | Enumerates the filters for a given provider.                                                                                                               |
| [**TdhEnumerateProviders**](tdhenumerateproviders-func.md)                               | Retrieves a list of providers that have registered a MOF or manifest file on the computer.                                                                 |
| [**TdhFormatProperty**](tdhformatproperty.md)                                            | Formats a property value for display.                                                                                                                      |
| [**TdhGetDecodingParameter**](tdhgetdecodingparameter.md)                                | Retrieves the value of a decoding parameter.                                                                                                               |
| [**TdhGetEventInformation**](tdhgeteventinformation-func.md)                             | Retrieves metadata about an event.                                                                                                                         |
| [**TdhGetEventMapInformation**](tdhgeteventmapinformation-func.md)                       | Retrieves information about the event map contained in the event.                                                                                          |
| [**TdhGetManifestEventInformation**](tdhgetmanifesteventinformation.md)                  | Retrieves metadata about an event in a manifest.                                                                                                           |
| [**TdhGetProperty**](tdhgetproperty-func.md)                                             | Retrieves a property value from the event data.                                                                                                            |
| [**TdhGetPropertySize**](tdhgetpropertysize-func.md)                                     | Retrieves the size of one or more property values in the event data.                                                                                       |
| [**TdhGetWppMessage**](tdhgetwppmessage.md)                                              | Retrieves the formatted WPP message embedded into an [**EVENT\_RECORD**](event-record.md) structure.                                                      |
| [**TdhGetWppProperty**](tdhgetwppproperty.md)                                            | Retrieves a specific property associated with a WPP message.                                                                                               |
| [**TdhLoadManifest**](tdhloadmanifest.md)                                                | Loads the manifest used to decode a log file.                                                                                                              |
| [**TdhLoadManifestFromBinary**](tdhloadmanifestfrombinary.md)                            | Takes a NULL-terminated path to a binary file that contains metadata resources needed to decode a specific event provider.                                 |
| [**TdhOpenDecodingHandle**](tdhopendecodinghandle.md)                                    | Opens a decoding handle.                                                                                                                                   |
| [**TdhQueryProviderFieldInformation**](tdhqueryproviderfieldinformation-func.md)         | Retrieves information for the specified field from the event descriptions for those field values that match the given value.                               |
| [**TdhSetDecodingParameter**](tdhsetdecodingparameter.md)                                | Sets the value of a decoding parameter.                                                                                                                    |
| [**TdhUnloadManifest**](tdhunloadmanifest.md)                                            | Unloads the manifest that was loaded by the [**TdhLoadManifest**](tdhloadmanifest.md) function.                                                           |



 

The following functions manage access permissions to the controller and provider functions.



| Access control function                               | Description                                                                            |
|-------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**EventAccessControl**](eventaccesscontrol-func.md) | Adds or modifies the permissions of the specified provider or session.                 |
| [**EventAccessQuery**](eventaccessquery-func.md)     | Retrieves the permissions for the specified controller or provider.                    |
| [**EventAccessRemove**](eventaccessremove-func.md)   | Removes the permissions defined in the registry for the specified provider or session. |



 

You should not use the following functions; they may be unavailable in subsequent versions.



| Access control function                            | Description                                                                                                                   |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**EventClassCallback**](eventclasscallback.md)   | Consumers implement this callback to receive events for a specific event trace class from a session.                          |
| [**RemoveTraceCallback**](removetracecallback.md) | Stops an [**EventClassCallback**](eventclasscallback.md) function from receiving events for an event trace class.            |
| [**SetTraceCallback**](settracecallback.md)       | Specifies an [**EventClassCallback**](eventclasscallback.md) function to receive events for the specified event trace class. |



 

 

 




