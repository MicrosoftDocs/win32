---
title: ReadyBoot Events
description: ReadyBoot Events
ms.assetid: 3c38e53d-0dab-4c96-bdf7-024bfbe5f4a5
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ReadyBoot Events

Windows Performance Analyzer reports all major ReadyBoot events, as described in the following table.



| Event Type               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HIT<br/>           | Indicates a read request that was satisfied from the ReadyBoot cache instead of the disk. The reads reflected in these events do not appear in the Disk I/O graphs or summary tables.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| MISS<br/>          | Indicates a read request that was not satisfied from the ReadyBoot cache but was satisfied by the disk instead. Misses appear as DiskRead events in the [Disk I/O Graphs](disk-i-o.md) and Summary Tables. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PEND<br/>          | Indicates a read request for data that ReadyBoot cannot yet satisfy from the ReadyBoot cache but which is expected to be in the ReadyBoot cache within a short period of time. Holding the request instead of turning it into a cache miss and letting it go to the hard drive avoids interruptions in the prefetch IO schedule and lets ReadyBoot maintain its prefetching throughput. Once the data is in the cache, the request is satisfied and a HIT event is logged. If the data is not prefetched into the cache in time (not common) then the access will be satisfied from the disk and a MISS event as well as a DiskRead event will be logged. <br/> |
| PREFETCH/PREF<br/> | Indicates a read request that corresponds to a prefetch IO by the ReadyBoot component. The data for the request is added to the ReadyBoot cache. Note that these events show up as DiskRead events with Source field value of 'Prefetch' in the Disk I/O graphs and summary tables. <br/>                                                                                                                                                                                                                                                                                                                                                                       |
| WRITE<br/>         | Indicates a write request. Writes also appear as DiskWrite events in the Disk I/O graphs and summary tables. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |



 

> [!Note]  
> Due to implementation details, the process and thread information displayed for the prefetch, write, and miss events is not the process and thread actually performing the IO. To obtain the process and thread information for those event types, the corresponding events in the Disk I/O graphs and summary tables should be used.

 

 

 





