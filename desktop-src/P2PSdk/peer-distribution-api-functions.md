---
Description: The Microsoft Peer Distribution service supports functions for both consumer role and publisher role scenarios.
ms.assetid: 3f5af891-4f5d-4523-8fe6-47fc6ff13b35
title: Peer Distribution API Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Peer Distribution API Functions

The Microsoft Peer Distribution service supports functions for both consumer role and publisher role scenarios.

## The following functions are common in both "client" and "server" scenarios.



| Common Functions                                                                                       | Description                                                                                                     |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**PeerDistStartup**](/windows/win32/PeerDist/nf-peerdist-peerdiststartup?branch=master)                                                             | Creates a new **PEERDIST\_INSTANCE\_HANDLE** instance which must be passed to all other Peer Distribution APIs. |
| [**PeerDistShutdown**](/windows/win32/PeerDist/nf-peerdist-peerdistshutdown?branch=master)                                                           | Releases resources allocated by the call to [**PeerDistStartup**](/windows/win32/PeerDist/nf-peerdist-peerdiststartup?branch=master).                         |
| [**PeerDistGetStatus**](/windows/win32/PeerDist/nf-peerdist-peerdistgetstatus?branch=master)                                                         | Returns the current status of Peer Distribution service.                                                        |
| [**PeerDistGetStatusEx**](/windows/win32/PeerDist/nf-peerdist-peerdistgetstatusex?branch=master)                                                     | Returns the current status and capabilities of the Peer Distribution service.                                   |
| [**PeerDistGetOverlappedResult**](/windows/win32/peerdist/nf-peerdist-peerdistgetoverlappedresult?branch=master)                                     | Retrieves the results of asynchronous operations.                                                               |
| [**PeerDistRegisterForStatusChangeNotification**](/windows/win32/PeerDist/nf-peerdist-peerdistregisterforstatuschangenotification?branch=master)     | Requests that the Peer Distribution service notify the caller when a status change occurs.                      |
| [**PeerDistRegisterForStatusChangeNotificationEx**](https://msdn.microsoft.com/library/windows/desktop/hh802741) | Requests that the Peer Distribution service notify the caller when a status change occurs.                      |
| [**PeerDistUnregisterForStatusChangeNotification**](/windows/win32/PeerDist/nf-peerdist-peerdistunregisterforstatuschangenotification?branch=master) | Deregisters the status change notification for the session associated with the supplied handle.                 |



 

## The following functions are only supported in "client" scenarios.



| Client Functions                                                                             | Description                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerDistClientOpenContent**](/windows/win32/PeerDist/nf-peerdist-peerdistclientopencontent?branch=master)                               | Opens and returns a **PEERDIST\_CONTENT\_HANDLE** to reference that content.                                                                                                                                                                                                                                                                     |
| [**PeerDistClientCloseContent**](/windows/win32/PeerDist/nf-peerdist-peerdistclientclosecontent?branch=master)                             | Closes the **PEERDIST\_CONTENT\_HANDLE**.                                                                                                                                                                                                                                                                                                        |
| [**PeerDistClientGetInformationByHandle**](/windows/win32/peerdist/nf-peerdist-peerdistclientgetinformationbyhandle?branch=master)         | Retrieves additional information from the Peer Distribution service for a specific content handle.                                                                                                                                                                                                                                               |
| [**PeerDistClientAddContentInformation**](/windows/win32/PeerDist/nf-peerdist-peerdistclientaddcontentinformation?branch=master)           | Adds content information which is then associated with the **PEERDIST\_CONTENT\_HANDLE**. A **PEERDIST\_CONTENT\_HANDLE** can be associated with any content information.                                                                                                                                                                        |
| [**PeerDistClientCompleteContentInformation**](/windows/win32/PeerDist/nf-peerdist-peerdistclientcompletecontentinformation?branch=master) | Indicates the end of the content information.                                                                                                                                                                                                                                                                                                    |
| [**PeerDistClientAddData**](/windows/win32/PeerDist/nf-peerdist-peerdistclientadddata?branch=master)                                       | Used to supply content to the local cache. Typically this is done when data could not be found on the local network as indicated when either [**PeerDistClientBlockRead**](/windows/win32/PeerDist/nf-peerdist-peerdistclientblockread?branch=master) or [**PeerDistClientStreamRead**](/windows/win32/PeerDist/nf-peerdist-peerdistclientstreamread?branch=master) complete with **ERROR\_TIMEOUT** or **PEERDIST\_ERROR\_MISSING\_DATA**.. |
| [**PeerDistClientBlockRead**](/windows/win32/PeerDist/nf-peerdist-peerdistclientblockread?branch=master)                                   | Provides random access to the content stream.                                                                                                                                                                                                                                                                                                    |
| [**PeerDistClientStreamRead**](/windows/win32/PeerDist/nf-peerdist-peerdistclientstreamread?branch=master)                                 | Provides sequential access to the content stream.                                                                                                                                                                                                                                                                                                |
| [**PeerDistClientFlushContent**](/windows/win32/PeerDist/nf-peerdist-peerdistclientflushcontent?branch=master)                             | Removes content that has been previously added to the local Peer Distribution system.                                                                                                                                                                                                                                                            |
| [**PeerDistClientCancelAsyncOperation**](/windows/win32/PeerDist/nf-peerdist-peerdistclientcancelasyncoperation?branch=master)             | Cancels asynchronous operation associated with an [OVERLAPPED](http://go.microsoft.com/fwlink/p/?linkid=131007) structure and the content handle returned by [**PeerDistClientOpenContent**](/windows/win32/PeerDist/nf-peerdist-peerdistclientopencontent?branch=master).                                                                                                                     |



 

## The following functions are only supported in "server" scenarios.



| Server Functions                                                                             | Description                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerDistServerPublishStream**](/windows/win32/PeerDist/nf-peerdist-peerdistserverpublishstream?branch=master)                           | Creates the **PEERDIST\_STREAM\_HANDLE** which can be used with [**PeerDistServerPublishAddToStream**](/windows/win32/PeerDist/nf-peerdist-peerdistserverpublishaddtostream?branch=master) to create content information for the content stream. |
| [**PeerDistServerPublishAddToStream**](/windows/win32/PeerDist/nf-peerdist-peerdistserverpublishaddtostream?branch=master)                 | Adds data to the stream referenced by the PeerDist stream handle.                                                                                                                                  |
| [**PeerDistServerPublishCompleteStream**](/windows/win32/PeerDist/nf-peerdist-peerdistserverpublishcompletestream?branch=master)           | Called to indicate that all data has been added to the stream.                                                                                                                                     |
| [**PeerDistServerCloseStreamHandle**](/windows/win32/PeerDist/nf-peerdist-peerdistserverclosestreamhandle?branch=master)                   | Closes the stream handle.                                                                                                                                                                          |
| [**PeerDistServerUnpublish**](/windows/win32/PeerDist/nf-peerdist-peerdistserverunpublish?branch=master)                                   | Unpublishes previously published content in the Peer Distribution service.                                                                                                                         |
| [**PeerDistServerOpenContentInformation**](/windows/win32/PeerDist/nf-peerdist-peerdistserveropencontentinformation?branch=master)         | Opens a **PEERDIST\_CONTENTINFO\_HANDLE** for published content.                                                                                                                                   |
| [**PeerDistServerOpenContentInformationEx**](/windows/win32/peerdist/nf-peerdist-peerdistserveropencontentinformationex?branch=master)     | Opens a **PEERDIST\_CONTENTINFO\_HANDLE** for published content.                                                                                                                                   |
| [**PeerDistServerRetrieveContentInformation**](/windows/win32/PeerDist/nf-peerdist-peerdistserverretrievecontentinformation?branch=master) | Retrieves the content information associated with published content.                                                                                                                               |
| [**PeerDistServerCloseContentInformation**](/windows/win32/PeerDist/nf-peerdist-peerdistserverclosecontentinformation?branch=master)       | **PEERDIST\_CONTENTINFO\_HANDLE** opened by [**PeerDistServerOpenContentInformation**](/windows/win32/PeerDist/nf-peerdist-peerdistserveropencontentinformation?branch=master).                                                                  |
| [**PeerDistServerCancelAsyncOperation**](/windows/win32/PeerDist/nf-peerdist-peerdistservercancelasyncoperation?branch=master)             | Cancels the asynchronous operation associated with the content identifier and [OVERLAPPED](http://go.microsoft.com/fwlink/p/?linkid=131007) structure.                                             |



 

 

 



