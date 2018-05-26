---
title: Quick Start - Enabling Data Capture on an Existing Process
description: Quick Start - Enabling Data Capture on an Existing Process
ms.assetid: bda34d1f-57ff-446e-af8f-2741c8056f82
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Quick Start - Enabling Data Capture on an Existing Process

Under certain circumstances it is beneficial to start data capture after a process is initiated:

-   The scenario being analyzed may not occur until well after the application launches.

-   The analyst determines there is no need to analyze the initial heap allocations occurring on process start.

-   Starting data capture on launch can generate extremely large trace files that can take considerable time and resources to analyze, particularly if process heap analysis is being done in conjunction with other WPA event captures.

Capturing event data from an existing process starts heap allocation data collection at arbitrary times in the execution of an application. By not capturing startup allocations and subsequent heap information, the amount of data collected can be significantly reduced.

Start the default kernel logger, NT Kernel Logger, with the BASE flag, from an elevated command prompt:


```
C:\etl xperf -on BASE
```



To enable heap tracing on an existing process, substitute the actual process ID for *XXX* in the following command.


```
C:\etl> xperf -start HeapSession -heap -Pid XXX  -BufferSize 1024 -MinBuffers 128 -MaxBuffers 128 -stackwalk HeapAlloc+HeapRealloc
```



Prepare the traces for analysis in the same manner as done for data capture for a process started by WPA.


```
C:\etl> xperf -stop -stop HeapSession -d heapTrace.etl 
```



 

 




