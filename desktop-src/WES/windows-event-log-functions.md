---
title: Windows Event Log Functions
description: Windows Event Log defines the following functions that you can use to get events from a channel or event log and to get the metadata for a provider and the events that it generates.
ms.assetid: '0bc008e4-c01c-482b-b910-49de3de22fab'
---

# Windows Event Log Functions

Windows Event Log defines the following functions that you can use to get events from a channel or event log and to get the metadata for a provider and the events that it generates.



| Function                                                                   | Description                                                                                                                                                                                                       |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EVT\_SUBSCRIBE\_CALLBACK**](evt-subscribe-callback.md)                 | Implement this callback if you call the [**EvtSubscribe**](evtsubscribe.md) function to receive events that match your query.                                                                                    |
| [**EvtArchiveExportedLog**](evtarchiveexportedlog.md)                     | Adds localized strings to the events in the specified log file.                                                                                                                                                   |
| [**EvtCancel**](evtcancel.md)                                             | Cancels all pending operations on a handle.                                                                                                                                                                       |
| [**EvtClearLog**](evtclearlog.md)                                         | Removes all events from the specified channel and writes them to the target log file.                                                                                                                             |
| [**EvtClose**](evtclose.md)                                               | Closes an open handle.                                                                                                                                                                                            |
| [**EvtCreateBookmark**](evtcreatebookmark.md)                             | Creates a bookmark that identifies an event in a channel.                                                                                                                                                         |
| [**EvtCreateRenderContext**](evtcreaterendercontext.md)                   | Creates a context that specifies the information in the event that you want to render.                                                                                                                            |
| [**EvtExportLog**](evtexportlog.md)                                       | Copies events from the specified channel or log file and writes them to the target log file.                                                                                                                      |
| [**EvtFormatMessage**](evtformatmessage.md)                               | Formats a message string.                                                                                                                                                                                         |
| [**EvtGetChannelConfigProperty**](evtgetchannelconfigproperty.md)         | Gets the specified channel configuration property.                                                                                                                                                                |
| [**EvtGetEventInfo**](evtgeteventinfo.md)                                 | Gets information that identifies the structured XML query that selected the event and the channel or log file from which it came.                                                                                 |
| [**EvtGetEventMetadataProperty**](evtgeteventmetadataproperty.md)         | Gets the specified event metadata property.                                                                                                                                                                       |
| [**EvtGetExtendedStatus**](evtgetextendedstatus.md)                       | Gets a text message that contains the extended error information for the current error.                                                                                                                           |
| [**EvtGetLogInfo**](evtgetloginfo.md)                                     | Gets information about a channel or log file.                                                                                                                                                                     |
| [**EvtGetObjectArrayProperty**](evtgetobjectarrayproperty.md)             | Gets a provider metadata property from the specified object in the array.                                                                                                                                         |
| [**EvtGetObjectArraySize**](evtgetobjectarraysize.md)                     | Gets the number of elements in the array of objects.                                                                                                                                                              |
| [**EvtGetPublisherMetadataProperty**](evtgetpublishermetadataproperty.md) | Gets the specified provider metadata property.                                                                                                                                                                    |
| [**EvtGetQueryInfo**](evtgetqueryinfo.md)                                 | Gets information about a query that you ran that identifies the list of channels or log files that the query attempted to access and a list of return codes that indicates the success or failure of each access. |
| [**EvtNext**](evtnext.md)                                                 | Gets the next event from the query or subscription results.                                                                                                                                                       |
| [**EvtNextChannelPath**](evtnextchannelpath.md)                           | Gets a channel name from the enumerator.                                                                                                                                                                          |
| [**EvtNextEventMetadata**](evtnexteventmetadata.md)                       | Gets an event definition from the enumerator.                                                                                                                                                                     |
| [**EvtNextPublisherId**](evtnextpublisherid.md)                           | Gets the identifier of a provider from the enumerator.                                                                                                                                                            |
| [**EvtOpenChannelConfig**](evtopenchannelconfig.md)                       | Gets a handle that you use to read or modify a channel's configuration property.                                                                                                                                  |
| [**EvtOpenChannelEnum**](evtopenchannelenum.md)                           | Gets a handle that you use to enumerate the list of channels that are registered on the computer.                                                                                                                 |
| [**EvtOpenEventMetadataEnum**](evtopeneventmetadataenum.md)               | Gets a handle that you use to enumerate the list of events that the provider defines.                                                                                                                             |
| [**EvtOpenLog**](evtopenlog.md)                                           | Gets a handle to a channel or log file that you can then use to get information about the channel or log file.                                                                                                    |
| [**EvtOpenPublisherEnum**](evtopenpublisherenum.md)                       | Gets a handle that you use to enumerate the list of registered providers on the computer.                                                                                                                         |
| [**EvtOpenPublisherMetadata**](evtopenpublishermetadata.md)               | Gets a handle that you use to read the specified provider's metadata.                                                                                                                                             |
| [**EvtOpenSession**](evtopensession.md)                                   | Establishes a connection to a remote computer that you can use when calling the other Windows Event Log functions.                                                                                                |
| [**EvtQuery**](evtquery.md)                                               | Runs a query to retrieve events from a channel or log file that match the specified query criteria.                                                                                                               |
| [**EvtRender**](evtrender.md)                                             | Renders an XML fragment based on the rendering context that you specify.                                                                                                                                          |
| [**EvtSaveChannelConfig**](evtsavechannelconfig.md)                       | Saves the changes made to a channel's configuration.                                                                                                                                                              |
| [**EvtSeek**](evtseek.md)                                                 | Seeks to a specific event in a query result set.                                                                                                                                                                  |
| [**EvtSetChannelConfigProperty**](evtsetchannelconfigproperty.md)         | Sets the specified configuration property of a channel.                                                                                                                                                           |
| [**EvtSubscribe**](evtsubscribe.md)                                       | Creates a subscription that will receive current and future events from a channel or log file that match the specified query criteria.                                                                            |
| [**EvtUpdateBookmark**](evtupdatebookmark.md)                             | Updates the bookmark with information that identifies the specified event.                                                                                                                                        |



 

 

 




