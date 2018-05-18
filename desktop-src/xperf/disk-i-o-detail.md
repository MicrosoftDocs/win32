---
title: Disk I/O Detail
description: Disk I/O Detail
ms.assetid: '7afb8783-3c19-4343-bf4c-86323256d1e2'
---

# Disk I/O Detail

**Overview:** Displays disk activity as offsets, as shown in the following screen shot.

![screen shot of a disk i/o detail graph](images/gr-img035.png)

**Graph Type:** Usage graph

**Y-axis Units:** Displays the color coded map of disk throughput based on process. Disk flushes are displayed as red vertical lines.

**Required Flags:** DISK\_IO

**Events Captured:** Disk I/O, File I/O and SysConfig

**Legend Description:** Offset, in bytes, of disk activity

**Graph Description:** The Disk I/O detailed graph gives a geometric interpretation of the read, write, flush and seek operations on each physical disk attached to the system at the start of the trace. The X-axis represents time. The Y-axis represents the offset on the physical disk and spans all partitions on that physical disk. The disk I/Os that are presented in the graph are grouped in series by process.

Hovering with the mouse will display tooltips based on the location of the cursor. These tooltips can include:

-   Type of activity-Read, Write, Flush, Seek

-   Initialization time

-   Completion time

-   Device name

-   Process and thread

-   Priority

 

 




