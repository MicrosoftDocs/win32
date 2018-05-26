---
Description: The Peer Distribution API defines the following data types.
ms.assetid: 5a378965-696c-4205-b9de-bdf93f00018f
title: Peer Distribution API Data Types
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Peer Distribution API Data Types

The Peer Distribution API defines the following data types.


```C++
typedef HANDLE PEERDIST_INSTANCE_HANDLE;
typedef HANDLE PEERDIST_CONTENT_HANDLE;
typedef HANDLE PEERDIST_CONTENTINFO_HANDLE;
typedef HANDLE PEERDIST_STREAM_HANDLE;
```





| Data type                                                                                                                     | Description                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PEERDIST_INSTANCE_HANDLE"></span><span id="peerdist_instance_handle"></span>**PEERDIST\_INSTANCE\_HANDLE**          | A handle associated with the Peer Distribution instance. This handle is created by [**PeerDistStartup**](/windows/win32/PeerDist/nf-peerdist-peerdiststartup?branch=master), and used in most Peer Distribution operations.<br/>                                          |
| <span id="PEERDIST_CONTENT_HANDLE"></span><span id="peerdist_content_handle"></span>**PEERDIST\_CONTENT\_HANDLE**             | A handle associated with content. This handle is created by [**PeerDistClientOpenContent**](/windows/win32/PeerDist/nf-peerdist-peerdistclientopencontent?branch=master) and is referenced when opening, closing, adding, or publishing content.<br/>                     |
| <span id="PEERDIST_CONTENTINFO_HANDLE"></span><span id="peerdist_contentinfo_handle"></span>**PEERDIST\_CONTENTINFO\_HANDLE** | A handle associated with content information. This handle is created by [**PeerDistServerOpenContentInformation**](/windows/win32/PeerDist/nf-peerdist-peerdistserveropencontentinformation?branch=master), and is used when retrieving encoded content information.<br/> |
| <span id="PEERDIST_STREAM_HANDLE"></span><span id="peerdist_stream_handle"></span>**PEERDIST\_STREAM\_HANDLE**                | A handle associated with a data stream. This handle is created by [**PeerDistServerPublishStream**](/windows/win32/PeerDist/nf-peerdist-peerdistserverpublishstream?branch=master) and is referenced when publishing, closing, or adding to streamed content.<br/>        |



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 Professional \[desktop apps only\]<br/>                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Peerdist.h</dt> </dl> |



 

 




