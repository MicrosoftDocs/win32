---
title: Stopping a Trace
description: Stopping a Trace
ms.assetid: ae9a1139-262a-47bc-9ec4-dc67104b200d
keywords:
- xperf
- stop
- trace
- tracing
- NT Kernel Logger
- stop-and-merge
- merging traces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Stopping a Trace

You can view the complete list of start options by running the following command:


```
xperf -help stop
```



You can stop a trace session by using the **-stop** \[*LoggerName*\] top-level option. For example, the following command stops the kernel logger:


```
xperf -stop "NT Kernel Logger"
```



The NT Kernel Logger is used as a default when the LoggerName argument is missing. Therefore, the kernel logging session can be stopped with the following simplified command:


```
xperf -stop 
```



Be aware that the **-stop** top-level option stops NT Kernel Logger without merging the trace. NT Kernel Logger can be stopped and merged with the following command:


```
xperf -stop -d trace.etl
```



The stop-and-merge top-level option, **-d***filename*, uses as input all traces that are stopped before it on the same Xperf command line. When no **-stop** \[*LoggerName*\] top-level options are present, **-d** assumes an implied **-stop** for the kernel logger. This simplification reduces the previous command to:


```
xperf -d trace.etl
```



In this example, the kernel logger is stopped and merged into the trace file Trace.etl. For more information about interpreting trace merges, see the [Detailed Walkthrough](detailed-walkthrough.md) topic.

 

 




