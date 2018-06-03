---
title: The Disk I/O Action
description: The Disk I/O Action
ms.assetid: 60d4bdcb-1da8-4410-965c-fbf30c43dd05
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# The Disk I/O Action

The disk I/O action produces a text report that summarizes the various metrics regarding disk I/O. The usage for this action is:


```
-a diskio [-util -summary -counts -detail] 
```





| Option                  | Description                                                               |
|-------------------------|---------------------------------------------------------------------------|
| util \[n\] <br/>  | Show disk utilization for n second intervals, default 1 second<br/> |
| summary <br/>     | Show IO summary report for each file <br/>                          |
| detail <br/>      | Show details of each IO <br/>                                       |
| overlap <br/>     | Show overlapping of IOs <br/>                                       |
| range T1 T2 <br/> | Show data between times T1 and T2, both in use <br/>                |



 

If no report type is selected, default is to show disk utilization report.

 

 





