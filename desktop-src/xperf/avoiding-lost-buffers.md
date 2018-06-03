---
title: Avoiding Lost Buffers
description: Avoiding Lost Buffers
ms.assetid: 45e4b47d-75b9-44d3-9366-0561b6638f61
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Avoiding Lost Buffers

Some applications have a large number of heap allocations that tax the ability of ETW to keep up with the logging frequency. This is not an uncommon issue when allocation behavior is investigated for the first time for a scenario or codebase. This problem will manifest itself as lost buffers in the traces and can lead to analysis difficulties or erroneous conclusions because of incomplete data. There are several things that can be changed to ensure that ETW buffers or events are not lost during trace collection.

Larger ETW buffers are preferred over smaller buffers to enable more efficient disk IO as the buffers are written to disk. It is also a good idea to verify that the buffer size and count requests were able to be honored by the tools for the data collection the first time a particular buffer configuration is used on a machine. This is done with the "Xperf -loggers" command after starting tracing. The reason this is important is that the Xperf tools and ETW infrastructure will use non-paged pool for its buffers and there are limits to the percentage of non-page pool ETW will consume. It is possible to have ETW use page pool for its buffers instead of non-paged pool, but it is not the default and setup is more complex.


```
xperfinfo -loggers
```



The first block output from this command will be the kernel logger.


```
Logger Name           : NT Kernel Logger
Logger Id             : ffff
Logger Thread Id      : 00001100
Buffer Size           : 1024
Maximum Buffers       : 16
Minimum Buffers       : 16
Number of Buffers     : 16
Free Buffers          : 12
Buffers Written       : 1
Events Lost           : 0
Log Buffers Lost      : 0
Real Time Buffers Lost: 0
Flush Timer           : 0
Age Limit             : 15
Log File Mode         : Sequential Secure
Maximum File Size     : 0
Log Filename          : D:\kernel.etl
Trace Flags           : PROC_THREAD+LOADER+DISK_IO+HARD_FAULTS+FILENAME+PROFILE+MEMINFO
```



Later in the output there will be an entry for the HeapSession.


```
Logger Name           : HeapSession
Logger Id             : 17
Logger Thread Id      : 000014F8
Buffer Size           : 1024
Maximum Buffers       : 128
Minimum Buffers       : 128
Number of Buffers     : 128
Free Buffers          : 124
Buffers Written       : 74
Events Lost           : 0
Log Buffers Lost      : 0
Real Time Buffers Lost: 0
Flush Timer           : 0
Age Limit             : 15
Log File Mode         : Sequential
Maximum File Size     : 0
Log Filename          : D:\user.etl
Trace Flags           :
```



As stated earlier, applications that have extremely frequent allocation calls can lead to issues with the ability of ETW to keep up this the pace of logging. This will manifest itself as lost buffers in the traces. There are several ways to alleviate these issues, and not everyone is possible or beneficial in all cases;

-   Free up disk space on the system drive.

    This can increase disk throughput by reducing head seeks to find available free blocks to write the data

-   Specify a path for the HeapSession to log to a different physical hard drive than used for the OS.

-   Collect data on a more capable hardware.

-   Employ a disk subsystem with higher throughput.

-   Increase the number of buffers for the HeapSession.

-   Use a RAM drive for the HeapSession log.

-   Simplify the scenario being tested.

See the Xperf documentation for details on how to specify the destination path for a log file. Once the data collection is complete the resulting log file can be opened in Xperfview.

 

 




