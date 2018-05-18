---
Description: 'The Microsoft Peer Distribution service supports functions for both consumer role and publisher role scenarios.'
ms.assetid: '3f5af891-4f5d-4523-8fe6-47fc6ff13b35'
title: Peer Distribution API Functions
---

# Peer Distribution API Functions

The Microsoft Peer Distribution service supports functions for both consumer role and publisher role scenarios.

## The following functions are common in both "client" and "server" scenarios.



| Common Functions                                                                                       | Description                                                                                                     |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**PeerDistStartup**](peerdiststartup.md)                                                             | Creates a new **PEERDIST\_INSTANCE\_HANDLE** instance which must be passed to all other Peer Distribution APIs. |
| [**PeerDistShutdown**](peerdistshutdown.md)                                                           | Releases resources allocated by the call to [**PeerDistStartup**](peerdiststartup.md).                         |
| [**PeerDistGetStatus**](peerdistgetstatus.md)                                                         | Returns the current status of Peer Distribution service.                                                        |
| [**PeerDistGetStatusEx**](peerdistgetstatusex.md)                                                     | Returns the current status and capabilities of the Peer Distribution service.                                   |
| [**PeerDistGetOverlappedResult**](peerdistgetoverlappedresult.md)                                     | Retrieves the results of asynchronous operations.                                                               |
| [**PeerDistRegisterForStatusChangeNotification**](peerdistregisterforstatuschangenotification.md)     | Requests that the Peer Distribution service notify the caller when a status change occurs.                      |
| [**PeerDistRegisterForStatusChangeNotificationEx**](https://msdn.microsoft.com/library/windows/desktop/hh802741) | Requests that the Peer Distribution service notify the caller when a status change occurs.                      |
| [**PeerDistUnregisterForStatusChangeNotification**](peerdistunregisterforstatuschangenotification.md) | Deregisters the status change notification for the session associated with the supplied handle.                 |



 

## The following functions are only supported in "client" scenarios.



| Client Functions                                                                             | Description                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerDistClientOpenContent**](peerdistclientopencontent.md)                               | Opens and returns a **PEERDIST\_CONTENT\_HANDLE** to reference that content.                                                                                                                                                                                                                                                                     |
| [**PeerDistClientCloseContent**](peerdistclientclosecontent.md)                             | Closes the **PEERDIST\_CONTENT\_HANDLE**.                                                                                                                                                                                                                                                                                                        |
| [**PeerDistClientGetInformationByHandle**](peerdistclientgetinformationbyhandle.md)         | Retrieves additional information from the Peer Distribution service for a specific content handle.                                                                                                                                                                                                                                               |
| [**PeerDistClientAddContentInformation**](peerdistclientaddcontentinformation.md)           | Adds content information which is then associated with the **PEERDIST\_CONTENT\_HANDLE**. A **PEERDIST\_CONTENT\_HANDLE** can be associated with any content information.                                                                                                                                                                        |
| [**PeerDistClientCompleteContentInformation**](peerdistclientcompletecontentinformation.md) | Indicates the end of the content information.                                                                                                                                                                                                                                                                                                    |
| [**PeerDistClientAddData**](peerdistclientadddata.md)                                       | Used to supply content to the local cache. Typically this is done when data could not be found on the local network as indicated when either [**PeerDistClientBlockRead**](peerdistclientblockread.md) or [**PeerDistClientStreamRead**](peerdistclientstreamread.md) complete with **ERROR\_TIMEOUT** or **PEERDIST\_ERROR\_MISSING\_DATA**.. |
| [**PeerDistClientBlockRead**](peerdistclientblockread.md)                                   | Provides random access to the content stream.                                                                                                                                                                                                                                                                                                    |
| [**PeerDistClientStreamRead**](peerdistclientstreamread.md)                                 | Provides sequential access to the content stream.                                                                                                                                                                                                                                                                                                |
| [**PeerDistClientFlushContent**](peerdistclientflushcontent.md)                             | Removes content that has been previously added to the local Peer Distribution system.                                                                                                                                                                                                                                                            |
| [**PeerDistClientCancelAsyncOperation**](peerdistclientcancelasyncoperation.md)             | Cancels asynchronous operation associated with an [OVERLAPPED](http://go.microsoft.com/fwlink/p/?linkid=131007) structure and the content handle returned by [**PeerDistClientOpenContent**](peerdistclientopencontent.md).                                                                                                                     |



 

## The following functions are only supported in "server" scenarios.



| Server Functions                                                                             | Description                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerDistServerPublishStream**](peerdistserverpublishstream.md)                           | Creates the **PEERDIST\_STREAM\_HANDLE** which can be used with [**PeerDistServerPublishAddToStream**](peerdistserverpublishaddtostream.md) to create content information for the content stream. |
| [**PeerDistServerPublishAddToStream**](peerdistserverpublishaddtostream.md)                 | Adds data to the stream referenced by the PeerDist stream handle.                                                                                                                                  |
| [**PeerDistServerPublishCompleteStream**](peerdistserverpublishcompletestream.md)           | Called to indicate that all data has been added to the stream.                                                                                                                                     |
| [**PeerDistServerCloseStreamHandle**](peerdistserverclosestreamhandle.md)                   | Closes the stream handle.                                                                                                                                                                          |
| [**PeerDistServerUnpublish**](peerdistserverunpublish.md)                                   | Unpublishes previously published content in the Peer Distribution service.                                                                                                                         |
| [**PeerDistServerOpenContentInformation**](peerdistserveropencontentinformation.md)         | Opens a **PEERDIST\_CONTENTINFO\_HANDLE** for published content.                                                                                                                                   |
| [**PeerDistServerOpenContentInformationEx**](peerdistserveropencontentinformationex.md)     | Opens a **PEERDIST\_CONTENTINFO\_HANDLE** for published content.                                                                                                                                   |
| [**PeerDistServerRetrieveContentInformation**](peerdistserverretrievecontentinformation.md) | Retrieves the content information associated with published content.                                                                                                                               |
| [**PeerDistServerCloseContentInformation**](peerdistserverclosecontentinformation.md)       | **PEERDIST\_CONTENTINFO\_HANDLE** opened by [**PeerDistServerOpenContentInformation**](peerdistserveropencontentinformation.md).                                                                  |
| [**PeerDistServerCancelAsyncOperation**](peerdistservercancelasyncoperation.md)             | Cancels the asynchronous operation associated with the content identifier and [OVERLAPPED](http://go.microsoft.com/fwlink/p/?linkid=131007) structure.                                             |



 

 

 



