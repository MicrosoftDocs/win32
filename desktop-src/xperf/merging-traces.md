---
title: Merging Traces
description: Merging Traces
ms.assetid: cd592fb5-f3df-453c-a817-9571931ad0a8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Merging Traces

Two or more trace files from simultaneous sessions that were captured on the same machine can be merged into a single trace file. The following command merges two files named Kernel.etl and User.etl into one file, System.etl:


```
xperf -merge kernel.etl user.etl system.etl 
```



For information on starting and stopping traces please see the [Starting a Trace](starting-a-trace.md) and [Stopping a Trace](stopping-a-trace.md) sections of this document.

The resulting trace file, System.etl, contains the trace information from both Kernel.etl and User.etl, as well as additional system information that is critical for symbol decoding.

> \[!Important\]  
> An unmerged kernel trace cannot be symbol decoded correctly. For more information, see the [Symbol Support](symbol-support.md)section of this document.

 

 

 




