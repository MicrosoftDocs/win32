---
title: Windows Event Log Functions
description: Windows Event Log defines the following functions that you can use to get events from a channel or event log and to get the metadata for a provider and the events that it generates.
ms.assetid: 0bc008e4-c01c-482b-b910-49de3de22fab
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Event Log Functions

Windows Event Log defines the following functions that you can use to get events from a channel or event log and to get the metadata for a provider and the events that it generates.



| Function                                                                   | Description                                                                                                                                                                                                       |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EVT\_SUBSCRIBE\_CALLBACK**](/windows/win32/WinEvt/nc-winevt-evt_subscribe_callback?branch=master)                 | Implement this callback if you call the [**EvtSubscribe**](/windows/win32/WinEvt/nf-winevt-evtsubscribe?branch=master) function to receive events that match your query.                                                                                    |
| [**EvtArchiveExportedLog**](/windows/win32/WinEvt/nf-winevt-evtarchiveexportedlog?branch=master)                     | Adds localized strings to the events in the specified log file.                                                                                                                                                   |
| [**EvtCancel**](/windows/win32/WinEvt/nf-winevt-evtcancel?branch=master)                                             | Cancels all pending operations on a handle.                                                                                                                                                                       |
| [**EvtClearLog**](/windows/win32/WinEvt/nf-winevt-evtclearlog?branch=master)                                         | Removes all events from the specified channel and writes them to the target log file.                                                                                                                             |
| [**EvtClose**](/windows/win32/WinEvt/nf-winevt-evtclose?branch=master)                                               | Closes an open handle.                                                                                                                                                                                            |
| [**EvtCreateBookmark**](/windows/win32/WinEvt/nf-winevt-evtcreatebookmark?branch=master)                             | Creates a bookmark that identifies an event in a channel.                                                                                                                                                         |
| [**EvtCreateRenderContext**](/windows/win32/WinEvt/nf-winevt-evtcreaterendercontext?branch=master)                   | Creates a context that specifies the information in the event that you want to render.                                                                                                                            |
| [**EvtExportLog**](/windows/win32/WinEvt/nf-winevt-evtexportlog?branch=master)                                       | Copies events from the specified channel or log file and writes them to the target log file.                                                                                                                      |
| [**EvtFormatMessage**](/windows/win32/WinEvt/nf-winevt-evtformatmessage?branch=master)                               | Formats a message string.                                                                                                                                                                                         |
| [**EvtGetChannelConfigProperty**](/windows/win32/WinEvt/nf-winevt-evtgetchannelconfigproperty?branch=master)         | Gets the specified channel configuration property.                                                                                                                                                                |
| [**EvtGetEventInfo**](/windows/win32/WinEvt/nf-winevt-evtgeteventinfo?branch=master)                                 | Gets information that identifies the structured XML query that selected the event and the channel or log file from which it came.                                                                                 |
| [**EvtGetEventMetadataProperty**](/windows/win32/WinEvt/nf-winevt-evtgeteventmetadataproperty?branch=master)         | Gets the specified event metadata property.                                                                                                                                                                       |
| [**EvtGetExtendedStatus**](/windows/win32/WinEvt/nf-winevt-evtgetextendedstatus?branch=master)                       | Gets a text message that contains the extended error information for the current error.                                                                                                                           |
| [**EvtGetLogInfo**](/windows/win32/WinEvt/nf-winevt-evtgetloginfo?branch=master)                                     | Gets information about a channel or log file.                                                                                                                                                                     |
| [**EvtGetObjectArrayProperty**](/windows/win32/WinEvt/nf-winevt-evtgetobjectarrayproperty?branch=master)             | Gets a provider metadata property from the specified object in the array.                                                                                                                                         |
| [**EvtGetObjectArraySize**](/windows/win32/WinEvt/nf-winevt-evtgetobjectarraysize?branch=master)                     | Gets the number of elements in the array of objects.                                                                                                                                                              |
| [**EvtGetPublisherMetadataProperty**](/windows/win32/WinEvt/nf-winevt-evtgetpublishermetadataproperty?branch=master) | Gets the specified provider metadata property.                                                                                                                                                                    |
| [**EvtGetQueryInfo**](/windows/win32/WinEvt/nf-winevt-evtgetqueryinfo?branch=master)                                 | Gets information about a query that you ran that identifies the list of channels or log files that the query attempted to access and a list of return codes that indicates the success or failure of each access. |
| [**EvtNext**](/windows/win32/WinEvt/nf-winevt-evtnext?branch=master)                                                 | Gets the next event from the query or subscription results.                                                                                                                                                       |
| [**EvtNextChannelPath**](/windows/win32/WinEvt/nf-winevt-evtnextchannelpath?branch=master)                           | Gets a channel name from the enumerator.                                                                                                                                                                          |
| [**EvtNextEventMetadata**](/windows/win32/WinEvt/nf-winevt-evtnexteventmetadata?branch=master)                       | Gets an event definition from the enumerator.                                                                                                                                                                     |
| [**EvtNextPublisherId**](/windows/win32/WinEvt/nf-winevt-evtnextpublisherid?branch=master)                           | Gets the identifier of a provider from the enumerator.                                                                                                                                                            |
| [**EvtOpenChannelConfig**](/windows/win32/WinEvt/nf-winevt-evtopenchannelconfig?branch=master)                       | Gets a handle that you use to read or modify a channel's configuration property.                                                                                                                                  |
| [**EvtOpenChannelEnum**](/windows/win32/WinEvt/nf-winevt-evtopenchannelenum?branch=master)                           | Gets a handle that you use to enumerate the list of channels that are registered on the computer.                                                                                                                 |
| [**EvtOpenEventMetadataEnum**](/windows/win32/WinEvt/nf-winevt-evtopeneventmetadataenum?branch=master)               | Gets a handle that you use to enumerate the list of events that the provider defines.                                                                                                                             |
| [**EvtOpenLog**](/windows/win32/WinEvt/nf-winevt-evtopenlog?branch=master)                                           | Gets a handle to a channel or log file that you can then use to get information about the channel or log file.                                                                                                    |
| [**EvtOpenPublisherEnum**](/windows/win32/WinEvt/nf-winevt-evtopenpublisherenum?branch=master)                       | Gets a handle that you use to enumerate the list of registered providers on the computer.                                                                                                                         |
| [**EvtOpenPublisherMetadata**](/windows/win32/WinEvt/nf-winevt-evtopenpublishermetadata?branch=master)               | Gets a handle that you use to read the specified provider's metadata.                                                                                                                                             |
| [**EvtOpenSession**](/windows/win32/WinEvt/nf-winevt-evtopensession?branch=master)                                   | Establishes a connection to a remote computer that you can use when calling the other Windows Event Log functions.                                                                                                |
| [**EvtQuery**](/windows/win32/WinEvt/nf-winevt-evtquery?branch=master)                                               | Runs a query to retrieve events from a channel or log file that match the specified query criteria.                                                                                                               |
| [**EvtRender**](/windows/win32/WinEvt/nf-winevt-evtrender?branch=master)                                             | Renders an XML fragment based on the rendering context that you specify.                                                                                                                                          |
| [**EvtSaveChannelConfig**](/windows/win32/WinEvt/nf-winevt-evtsavechannelconfig?branch=master)                       | Saves the changes made to a channel's configuration.                                                                                                                                                              |
| [**EvtSeek**](/windows/win32/WinEvt/nf-winevt-evtseek?branch=master)                                                 | Seeks to a specific event in a query result set.                                                                                                                                                                  |
| [**EvtSetChannelConfigProperty**](/windows/win32/WinEvt/nf-winevt-evtsetchannelconfigproperty?branch=master)         | Sets the specified configuration property of a channel.                                                                                                                                                           |
| [**EvtSubscribe**](/windows/win32/WinEvt/nf-winevt-evtsubscribe?branch=master)                                       | Creates a subscription that will receive current and future events from a channel or log file that match the specified query criteria.                                                                            |
| [**EvtUpdateBookmark**](/windows/win32/WinEvt/nf-winevt-evtupdatebookmark?branch=master)                             | Updates the bookmark with information that identifies the specified event.                                                                                                                                        |



 

 

 




