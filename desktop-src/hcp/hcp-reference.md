---
title: HCP Reference
ms.assetid: 32747e50-5318-44c0-bf89-b6dfad3feb5f
description: 
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HCP Reference

Application profiling tools can use the Hardware Counter Profiling (HCP) API to get the following counter data on a per-thread basis:

-   The cycle time of the thread (excludes the time spent interrupted)
-   The number of context switches
-   A bitmap that identifies the reasons for the context switches (including page faults)
-   Hardware performance counters

You can enable profiling for one or more threads. To enable profiling for a thread, you must call the [**EnableThreadProfiling**](/windows/win32/Winbase/nf-winbase-enablethreadprofiling?branch=master) function from the thread itself—you cannot enable thread B from thread A.

You can gather thread profiling data, hardware performance counters, or both. To profile hardware performance counters, you need a driver to configure the counters. The performance counters are configured globally for the system, so every thread has access to the same hardware counter data. The counters must be configured before you enable profiling. For information on configuring hardware performance counters, see the **KeSetHardwareCounterConfiguration** function in the Windows Driver Kit (WDK).

HCP supports the x86 and AMD64 architectures; however, the IA64 architecture is not supported.

After calling [**EnableThreadProfiling**](/windows/win32/Winbase/nf-winbase-enablethreadprofiling?branch=master) to enable profiling on the thread, you would call the [**ReadThreadProfilingData**](/windows/win32/Winbase/nf-winbase-readthreadprofilingdata?branch=master) function before and after areas of interest in your code (for example, before and after a function call) to help isolate bottlenecks or other issues in your code. Before exiting the thread, call the [**DisableThreadProfiling**](/windows/win32/Winbase/nf-winbase-disablethreadprofiling?branch=master) function to release system resources.

Use the following programming elements to write applications that enable and read thread profiling data and hardware performance counter data:

-   [HCP Enumerations](hcp-enumerations.md)
-   [HCP Functions](hcp-functions.md)
-   [HCP Structures](hcp-structures.md)

 

 




