---
title: Using ETW Events of Other Providers to Bracket Activities
description: Using ETW Events of Other Providers to Bracket Activities
ms.assetid: '4eb880a2-0fd0-4dc8-9962-d28cafa21be0'
---

# Using ETW Events of Other Providers to Bracket Activities

Often it is beneficial to understand what the process being analyzed was performing when the heap allocations were done. Many applications and system processes have a rich set of ETW events that delineate activities and the timestamps from these can be used to aid in selecting areas for investigation.

In some applications, there are events that mark the beginning and ending of navigation and the timestamps for those events can be used to select a region of interest with the Select Interval dialog presented on the context menu that is presented from right clicking within a graph view.

The following screen shot shows the Select Interval dialog box displaying start and end times.

![screen shot of the select interval dialog box showing start and end times](images/he-img25.png)

 

 




