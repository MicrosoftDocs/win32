---
title: ReadyBoot Disk Usage Summary Table
description: ReadyBoot Disk Usage Summary Table
ms.assetid: 9875b618-974a-4b49-a10f-4bacd935b80c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ReadyBoot Disk Usage Summary Table

The "Disk Usage Summary Table" view of the ReadyBoot I/O allows the analyst to see ReadyBoot related disk usage statistics, as shown in the following screen shot.

![screen shot of a disk usage summary table showing readyboot-related disk-usage information](images/rb-07.png)

<dl> <dt>

Disk Usage Summary Table notes:
</dt> <dt>


</dt> </dl>

-   The table above shows that ReadyBoot prefetching accounted for 64% of total disk time during the time interval between first and last prefetching events.

-   Skips refer to larger reads which are not serviced by the ReadyBoot cache. This is because the disks are very efficient when doing large reads. The table further breaks down skips into:

    -   VolSnap skipped reads which are IO operations originating from the system restore component

    -   Registry skipped reads

    -   Other skipped reads

-   Non-system Volume reads and writes refer to the disk activity on the volumes other than one containing the Windows installation. Note that if other volumes reside on the same disk as the system volume, IO to such other volumes during boot would reduce ReadyBoot prefetching efficiency.

 

 




