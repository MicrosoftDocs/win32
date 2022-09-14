---
description: The Microsoft Peer Distribution service supports functions for both consumer role and publisher role scenarios.
ms.assetid: 3f5af891-4f5d-4523-8fe6-47fc6ff13b35
title: Peer Distribution API Functions
ms.topic: article
ms.date: 05/31/2018
---

# Peer Distribution API Functions

The Microsoft Peer Distribution service supports functions for both consumer role and publisher role scenarios.

## The following functions are common in both "client" and "server" scenarios.



| Common Functions                                                                                       | Description                                                                                                     |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**PeerDistStartup**](/windows/desktop/api/PeerDist/nf-peerdist-peerdiststartup)                                                             | Creates a new **PEERDIST\_INSTANCE\_HANDLE** instance which must be passed to all other Peer Distribution APIs. |
| [**PeerDistShutdown**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistshutdown)                                                           | Releases resources allocated by the call to [**PeerDistStartup**](/windows/desktop/api/PeerDist/nf-peerdist-peerdiststartup).                         |
| [**PeerDistGetStatus**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistgetstatus)                                                         | Returns the current status of Peer Distribution service.                                                        |
| [**PeerDistGetStatusEx**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistgetstatusex)                                                     | Returns the current status and capabilities of the Peer Distribution service.                                   |
| [**PeerDistGetOverlappedResult**](/windows/desktop/api/peerdist/nf-peerdist-peerdistgetoverlappedresult)                                     | Retrieves the results of asynchronous operations.                                                               |
| [**PeerDistRegisterForStatusChangeNotification**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistregisterforstatuschangenotification)     | Requests that the Peer Distribution service notify the caller when a status change occurs.                      |
| [**PeerDistRegisterForStatusChangeNotificationEx**](/windows/desktop/api/peerdist/nf-peerdist-peerdistregisterforstatuschangenotificationex) | Requests that the Peer Distribution service notify the caller when a status change occurs.                      |
| [**PeerDistUnregisterForStatusChangeNotification**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistunregisterforstatuschangenotification) | Deregisters the status change notification for the session associated with the supplied handle.                 |



 

## The following functions are only supported in "client" scenarios.



| Client Functions                                                                             | Description                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerDistClientOpenContent**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientopencontent)                               | Opens and returns a **PEERDIST\_CONTENT\_HANDLE** to reference that content.                                                                                                                                                                                                                                                                     |
| [**PeerDistClientCloseContent**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientclosecontent)                             | Closes the **PEERDIST\_CONTENT\_HANDLE**.                                                                                                                                                                                                                                                                                                        |
| [**PeerDistClientGetInformationByHandle**](/windows/desktop/api/peerdist/nf-peerdist-peerdistclientgetinformationbyhandle)         | Retrieves additional information from the Peer Distribution service for a specific content handle.                                                                                                                                                                                                                                               |
| [**PeerDistClientAddContentInformation**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientaddcontentinformation)           | Adds content information which is then associated with the **PEERDIST\_CONTENT\_HANDLE**. A **PEERDIST\_CONTENT\_HANDLE** can be associated with any content information.                                                                                                                                                                        |
| [**PeerDistClientCompleteContentInformation**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientcompletecontentinformation) | Indicates the end of the content information.                                                                                                                                                                                                                                                                                                    |
| [**PeerDistClientAddData**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientadddata)                                       | Used to supply content to the local cache. Typically this is done when data could not be found on the local network as indicated when either [**PeerDistClientBlockRead**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientblockread) or [**PeerDistClientStreamRead**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientstreamread) complete with **ERROR\_TIMEOUT** or **PEERDIST\_ERROR\_MISSING\_DATA**.. |
| [**PeerDistClientBlockRead**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientblockread)                                   | Provides random access to the content stream.                                                                                                                                                                                                                                                                                                    |
| [**PeerDistClientStreamRead**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientstreamread)                                 | Provides sequential access to the content stream.                                                                                                                                                                                                                                                                                                |
| [**PeerDistClientFlushContent**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientflushcontent)                             | Removes content that has been previously added to the local Peer Distribution system.                                                                                                                                                                                                                                                            |
| [**PeerDistClientCancelAsyncOperation**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientcancelasyncoperation)             | Cancels asynchronous operation associated with an [OVERLAPPED](/windows/win32/api/minwinbase/ns-minwinbase-overlapped) structure and the content handle returned by [**PeerDistClientOpenContent**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistclientopencontent).                                                                                                                     |



 

## The following functions are only supported in "server" scenarios.



| Server Functions                                                                             | Description                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerDistServerPublishStream**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserverpublishstream)                           | Creates the **PEERDIST\_STREAM\_HANDLE** which can be used with [**PeerDistServerPublishAddToStream**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserverpublishaddtostream) to create content information for the content stream. |
| [**PeerDistServerPublishAddToStream**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserverpublishaddtostream)                 | Adds data to the stream referenced by the PeerDist stream handle.                                                                                                                                  |
| [**PeerDistServerPublishCompleteStream**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserverpublishcompletestream)           | Called to indicate that all data has been added to the stream.                                                                                                                                     |
| [**PeerDistServerCloseStreamHandle**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserverclosestreamhandle)                   | Closes the stream handle.                                                                                                                                                                          |
| [**PeerDistServerUnpublish**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserverunpublish)                                   | Unpublishes previously published content in the Peer Distribution service.                                                                                                                         |
| [**PeerDistServerOpenContentInformation**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserveropencontentinformation)         | Opens a **PEERDIST\_CONTENTINFO\_HANDLE** for published content.                                                                                                                                   |
| [**PeerDistServerOpenContentInformationEx**](/windows/desktop/api/peerdist/nf-peerdist-peerdistserveropencontentinformationex)     | Opens a **PEERDIST\_CONTENTINFO\_HANDLE** for published content.                                                                                                                                   |
| [**PeerDistServerRetrieveContentInformation**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserverretrievecontentinformation) | Retrieves the content information associated with published content.                                                                                                                               |
| [**PeerDistServerCloseContentInformation**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserverclosecontentinformation)       | **PEERDIST\_CONTENTINFO\_HANDLE** opened by [**PeerDistServerOpenContentInformation**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistserveropencontentinformation).                                                                  |
| [**PeerDistServerCancelAsyncOperation**](/windows/desktop/api/PeerDist/nf-peerdist-peerdistservercancelasyncoperation)             | Cancels the asynchronous operation associated with the content identifier and [OVERLAPPED](/windows/win32/api/minwinbase/ns-minwinbase-overlapped) structure.                                             |



 

 

 
