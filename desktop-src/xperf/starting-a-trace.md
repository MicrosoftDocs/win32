---
title: Starting a Trace
description: Starting a Trace
ms.assetid: 'aab30f1c-7d88-44de-8a53-8f7e8900556d'
keywords: ["xperf", "start", "providers", "logger name", "REGISTRY flag", "trace", "tracing"]
---

# Starting a Trace

The full list of start options can be viewed by running the following command:


```
xperf -help start
```



You can view a list of all the kernel flags by using the following command:


```
xperf -providers k
```



Tracing sessions are started by using the **-start** \[*LoggerName*\] top-level option. For example, the following command starts the kernel logger with Base and FileIO groups and the REGISTRY flag:


```
xperf -on DiagEasy+FILE_IO_INIT+REGISTRY
```



In this case example, the groups Base and FileIO are enabled in addition to the flag REGISTRY. The total set of flags enabled is the union of the Base and FileIO groups in addition to the REGISTRY flag. Alternatively, you can enable all the associated flags:


```
xperf -on LOADER+PROC_THREAD+DISK_IO+HARD_FAULTS+DPC+INTERRUPT+CSWITCH+PERF_COUNTER+FILE_IO_INIT+REGISTRY
```



Both commands produce the same results. The flags and groups are separated by the '+' token. Also be aware that command-line processing is not case sensitive. You can use any mix of upper and/or lower case text. For more information on describing providers please see [WPA Providers](wpa-providers.md).

 

 




