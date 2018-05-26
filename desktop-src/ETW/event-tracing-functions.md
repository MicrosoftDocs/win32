---
Description: Event trace controllers use the following functions to manage event tracing sessions.
ms.assetid: 6f0f1173-19e1-4aec-b6a6-77f18f819c30
title: Event Tracing Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**CveEventWrite**](/windows/win32/SecurityBaseAPI/nf-securitybaseapi-cveeventwrite?branch=master)                        | A tracing function for publishing events when an attempted security vulnerability exploit is detected in your user-mode application.   |
| [**EnableCallback**](/windows/win32/Evntprov/nc-evntprov-penablecallback?branch=master)                      | Providers implement this callback to receive enable or disable event tracing notifications from controllers.                           |
| [**EventActivityIdControl**](/windows/win32/Evntprov/nf-evntprov-eventactivityidcontrol?branch=master) | Creates, queries, and sets the current activity identifier used by the [**EventWriteTransfer**](/windows/win32/Evntprov/nf-evntprov-eventwritetransfer?branch=master) function. |
| [**EventEnabled**](/windows/win32/Evntprov/nf-evntprov-eventenabled?branch=master)                     | Determines if the event is enabled for any session.                                                                                    |
| [**EventProviderEnabled**](/windows/win32/Evntprov/nf-evntprov-eventproviderenabled?branch=master)     | Determines if the event is enabled for any session.                                                                                    |
| [**EventRegister**](/windows/win32/Evntprov/nf-evntprov-eventregister?branch=master)                   | Registers the provider.                                                                                                                |
| [**EventSetInformation**](/windows/win32/Evntprov/nf-evntprov-eventsetinformation?branch=master)            | Performs operations on a registration object.                                                                                          |
| [**EventUnregister**](/windows/win32/Evntprov/nf-evntprov-eventunregister?branch=master)               | Removes the provider's registration.                                                                                                   |
| [**EventWrite**](/windows/win32/Evntprov/nf-evntprov-eventwrite?branch=master)                         | Writes an event. This function is superseded by [**EventWriteEx**](/windows/win32/Evntprov/nf-evntprov-eventwriteex?branch=master).                                                  |
| [**EventWriteEx**](/windows/win32/Evntprov/nf-evntprov-eventwriteex?branch=master)                          | Writes an event.                                                                                                                       |
| [**EventWriteString**](/windows/win32/Evntprov/nf-evntprov-eventwritestring?branch=master)             | Writes an event that contains a string as its data.                                                                                    |
| [**EventWriteTransfer**](/windows/win32/Evntprov/nf-evntprov-eventwritetransfer?branch=master)         | Links events together when tracing events in an end-to-end scenario.                                                                   |



 

Event trace consumers use the following functions to process events.



| Consumer function                                                                         | Description                                                                                                                                                |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BufferCallback**](buffercallback.md)                                                  | Consumers implement this callback to receive statistics about each buffer of events that ETW delivers to an event trace consumer.                          |
| [**CloseTrace**](closetrace.md)                                                          | Closes a trace.                                                                                                                                            |
| [**EventCallback**](eventcallback.md)                                                    | Consumers implement this callback to receive all events from a session.                                                                                    |
| [**EventRecordCallback**](eventrecordcallback.md)                                        | Consumers implement this callback to receive events from a session.                                                                                        |
| [**OpenTrace**](opentrace.md)                                                            | Opens a trace for processing.                                                                                                                              |
| [**ProcessTrace**](processtrace.md)                                                      | Delivers events to a consumer for processing.                                                                                                              |
| [**TdhAggregatePayloadFilters**](/windows/win32/Tdh/nf-tdh-tdhaggregatepayloadfilters?branch=master)                          | Aggregates multiple payload filters for a single provider into a single data structure for use with the [**EnableTraceEx2**](enabletraceex2.md) function. |
| [**TdhCleanupPayloadEventFilterDescriptor**](/windows/win32/Tdh/nf-tdh-tdhcleanuppayloadeventfilterdescriptor?branch=master)  | Frees the aggregated structure of payload filters created using the [**TdhAggregatePayloadFilters**](/windows/win32/Tdh/nf-tdh-tdhaggregatepayloadfilters?branch=master) function.             |
| [**TdhCloseDecodingHandle**](/windows/win32/Tdh/nf-tdh-tdhclosedecodinghandle?branch=master)                                  | Frees resources associated with the input decoding handle.                                                                                                 |
| [**TdhCreatePayloadFilter**](/windows/win32/Tdh/nf-tdh-tdhcreatepayloadfilter?branch=master)                                  | Creates a single filter for a single payload to be used with the [**EnableTraceEx2**](enabletraceex2.md) function.                                        |
| [**TdhDeletePayloadFilter**](/windows/win32/Tdh/nf-tdh-tdhdeletepayloadfilter?branch=master)                                  | Frees the memory allocated for a single payload filter by the [**TdhCreatePayloadFilter**](/windows/win32/Tdh/nf-tdh-tdhcreatepayloadfilter?branch=master) function.                           |
| [**TdhEnumerateManifestProviderEvents**](/windows/win32/Tdh/nf-tdh-tdhenumeratemanifestproviderevents?branch=master)          | Retrieves the list of events present in the provider manifest.                                                                                             |
| [**TdhEnumerateProviderFieldInformation**](/windows/win32/Tdh/nf-tdh-tdhenumerateproviderfieldinformation?branch=master) | Retrieves the specified field metadata for a given provider.                                                                                               |
| [**TdhEnumerateProviderFilters**](/windows/win32/Tdh/nf-tdh-tdhenumerateproviderfilters?branch=master)                        | Enumerates the filters for a given provider.                                                                                                               |
| [**TdhEnumerateProviders**](/windows/win32/Tdh/nf-tdh-tdhenumerateproviders?branch=master)                               | Retrieves a list of providers that have registered a MOF or manifest file on the computer.                                                                 |
| [**TdhFormatProperty**](/windows/win32/Tdh/nf-tdh-tdhformatproperty?branch=master)                                            | Formats a property value for display.                                                                                                                      |
| [**TdhGetDecodingParameter**](/windows/win32/Tdh/nf-tdh-tdhgetdecodingparameter?branch=master)                                | Retrieves the value of a decoding parameter.                                                                                                               |
| [**TdhGetEventInformation**](/windows/win32/Tdh/nf-tdh-tdhgeteventinformation?branch=master)                             | Retrieves metadata about an event.                                                                                                                         |
| [**TdhGetEventMapInformation**](/windows/win32/Tdh/nf-tdh-tdhgeteventmapinformation?branch=master)                       | Retrieves information about the event map contained in the event.                                                                                          |
| [**TdhGetManifestEventInformation**](/windows/win32/Tdh/nf-tdh-tdhgetmanifesteventinformation?branch=master)                  | Retrieves metadata about an event in a manifest.                                                                                                           |
| [**TdhGetProperty**](/windows/win32/Tdh/nf-tdh-tdhgetproperty?branch=master)                                             | Retrieves a property value from the event data.                                                                                                            |
| [**TdhGetPropertySize**](/windows/win32/Tdh/nf-tdh-tdhgetpropertysize?branch=master)                                     | Retrieves the size of one or more property values in the event data.                                                                                       |
| [**TdhGetWppMessage**](/windows/win32/Tdh/nf-tdh-tdhgetwppmessage?branch=master)                                              | Retrieves the formatted WPP message embedded into an [**EVENT\_RECORD**](/windows/win32/relogger/ns-evntcons-_event_record?branch=master) structure.                                                      |
| [**TdhGetWppProperty**](/windows/win32/Tdh/nf-tdh-tdhgetwppproperty?branch=master)                                            | Retrieves a specific property associated with a WPP message.                                                                                               |
| [**TdhLoadManifest**](/windows/win32/Tdh/nf-tdh-tdhloadmanifest?branch=master)                                                | Loads the manifest used to decode a log file.                                                                                                              |
| [**TdhLoadManifestFromBinary**](/windows/win32/Tdh/nf-tdh-tdhloadmanifestfrombinary?branch=master)                            | Takes a NULL-terminated path to a binary file that contains metadata resources needed to decode a specific event provider.                                 |
| [**TdhOpenDecodingHandle**](/windows/win32/Tdh/nf-tdh-tdhopendecodinghandle?branch=master)                                    | Opens a decoding handle.                                                                                                                                   |
| [**TdhQueryProviderFieldInformation**](/windows/win32/Tdh/nf-tdh-tdhqueryproviderfieldinformation?branch=master)         | Retrieves information for the specified field from the event descriptions for those field values that match the given value.                               |
| [**TdhSetDecodingParameter**](/windows/win32/Tdh/nf-tdh-tdhsetdecodingparameter?branch=master)                                | Sets the value of a decoding parameter.                                                                                                                    |
| [**TdhUnloadManifest**](/windows/win32/Tdh/nf-tdh-tdhunloadmanifest?branch=master)                                            | Unloads the manifest that was loaded by the [**TdhLoadManifest**](/windows/win32/Tdh/nf-tdh-tdhloadmanifest?branch=master) function.                                                           |



 

The following functions manage access permissions to the controller and provider functions.



| Access control function                               | Description                                                                            |
|-------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**EventAccessControl**](/windows/win32/Evntcons/nf-evntcons-eventaccesscontrol?branch=master) | Adds or modifies the permissions of the specified provider or session.                 |
| [**EventAccessQuery**](/windows/win32/Evntcons/nf-evntcons-eventaccessquery?branch=master)     | Retrieves the permissions for the specified controller or provider.                    |
| [**EventAccessRemove**](/windows/win32/Evntcons/nf-evntcons-eventaccessremove?branch=master)   | Removes the permissions defined in the registry for the specified provider or session. |



 

You should not use the following functions; they may be unavailable in subsequent versions.



| Access control function                            | Description                                                                                                                   |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**EventClassCallback**](eventclasscallback.md)   | Consumers implement this callback to receive events for a specific event trace class from a session.                          |
| [**RemoveTraceCallback**](removetracecallback.md) | Stops an [**EventClassCallback**](eventclasscallback.md) function from receiving events for an event trace class.            |
| [**SetTraceCallback**](settracecallback.md)       | Specifies an [**EventClassCallback**](eventclasscallback.md) function to receive events for the specified event trace class. |



 

 

 




