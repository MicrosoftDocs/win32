---
Description: .
ms.assetid: c5dedcab-3e6f-433f-95de-d741321c683e
title: Preventing Memory Leaks in Windows Applications
ms.topic: article
ms.date: 05/31/2018
---

# Preventing Memory Leaks in Windows Applications

## Affected Platforms

<dl> **Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  
</dl>

## Description

Memory leaks are a class of bugs where the application fails to release memory when no longer needed. Over time, memory leaks affect the performance of both the particular application as well as the operating system. A large leak might result in unacceptable response times due to excessive paging. Eventually the application as well as other parts of the operating system will experience failures.

Windows will free all memory allocated by the application on process termination, so short-running applications will not affect overall system performance significantly. However, leaks in long-running processes like services or even Explorer plug-ins can greatly impact system reliability and might force the user to reboot Windows in order to make the system usable again.

Applications can allocate memory on their behalf by multiple means. Each type of allocation can result in a leak if not freed after use. Here are some examples of common allocation patterns:

-   Heap memory via the [**HeapAlloc**](https://msdn.microsoft.com/library/Aa366597(v=VS.85).aspx) function or its C/C++ runtime equivalents **malloc** or **new**
-   Direct allocations from the operating system via the [**VirtualAlloc**](https://msdn.microsoft.com/library/Aa366887(v=VS.85).aspx) function.
-   Kernel handles created via Kernel32 APIs such as [**CreateFile**](https://msdn.microsoft.com/library/Aa363858(v=VS.85).aspx), [**CreateEvent**](https://msdn.microsoft.com/library/ms682396(v=VS.85).aspx), or [**CreateThread**](https://msdn.microsoft.com/library/ms682453(v=VS.85).aspx), hold kernel memory on behalf of the application
-   GDI and USER handles created via User32 and Gdi32 APIs (by default, each process has a quota of 10,000 handles)

## Best Practices

Monitoring the resource consumption of your application over time is the first step in detecting and diagnosing memory leaks. Use Windows Task Manager and add the following columns: "Commit Size", "Handles", "User Objects", and "GDI Objects". This will allow you to establish a baseline for your application and monitor resource usage over time.

![](images/preventingmemoryleaks-windowstaskmanager.gif)

The following Microsoft tools provide more-detailed information and can help to detect and diagnose leaks for the various allocation types in your application:

-   Performance Monitor and Resource Monitor are part of Windows 7 and can monitor and graph resource use over time
-   The latest version of Application Verifier can diagnose heap leaks on Windows 7
-   UMDH, which is part of the Debugging Tools for Windows, analyzes the heap memory allocations for a given process and can help find leaks and other unusual usage patterns
-   Xperf is a sophisticated performance analysis tool with support for heap allocation traces
-   CRT Debug Heap tracks heap allocations and can help build your own heap debugging features

Certain coding and design practices can limit the number of leaks in your code.

-   Use smart pointers in C++ code both for heap allocations as well as for Win32 resources like kernel **HANDLE**s. The C++ Standard library provides the **auto\_ptr** class for heap allocations. For other allocation types you will need to write your own classes. The ATL library provides a rich set of classes for automatic resource management for both heap objects and kernel handles
-   Use compiler intrinsic features like **\_com\_ptr\_t** to encapsulate your COM interface pointers into "smart pointers" and assist with reference counting. There are similar classes for other COM data types: **\_bstr\_t** and **\_variant\_t**
-   Monitor your .NET code unusual memory usage. Managed code is not immune to memory leaks. See ["Tracking down managed memory leaks"](https://blogs.msdn.com/ricom/archive/2004/12/10/279612.aspx) on how to find GC leaks
-   Be aware of leak patterns in web client-side code. Circular references between COM objects and scripting engines like JScript can cause large leaks in web applications. ["Understanding and Solving Internet Explorer Leak Patterns"](https://msdn.microsoft.com/library/ms976398(v=MSDN.10).aspx) has more information on these kinds of leaks. You can use the JavaScript Memory Leak Detector to debug memory leaks in your code. While Windows Internet Explorer 8, which is shipping with Windows 7, mitigates most of these issues, older browsers are still vulnerable to these bugs
-   Avoid using multiple exit paths from a function. Allocations assigned to variables at function scope should be freed in one particular block at the end of the function
-   Do not use exceptions in your code without freeing all local variables in functions. If you use native exceptions, free all your allocations inside the \_\_finally block. If you use C++ exceptions, all your heap and handle allocations need to be wrapped in smart pointers
-   Do not discard or reinitialize a [**PROPVARIANT**](https://msdn.microsoft.com/library/Aa380072(v=VS.85).aspx) object without calling the [**PropVariantClear**](https://msdn.microsoft.com/library/Aa380073(v=VS.85).aspx) function

## Links to Resources

*Common Allocation Patterns:*

-   [**Heap Allocation Function**](https://msdn.microsoft.com/library/Aa366597(v=VS.85).aspx)
-   [**Memory Allocation Function**](https://msdn.microsoft.com/library/6ewkz86d(v=VS.71).aspx)
-   [**New Operator (C++)**](https://msdn.microsoft.com/library/kewsb8ba(v=VS.71).aspx)
-   [**Virtual Allocation Function**](https://msdn.microsoft.com/library/Aa366887(v=VS.85).aspx)
-   [Kernel Objects](https://msdn.microsoft.com/library/ms724485(v=VS.85).aspx)
-   [GDI Object Handles](https://msdn.microsoft.com/library/ms724291(v=VS.85).aspx)
-   [User Interface Object Handles](https://msdn.microsoft.com/library/ms725486(v=VS.85).aspx)

*Microsoft Tools:*

-   [Application Verifier](application-verifier.md)
-   [Debugging Tools for Windows](https://msdn.microsoft.com/library/Ff551063(v=VS.85).aspx)
-   [User-Mode Dump Heap](https://msdn.microsoft.com/library/Ff558947(v=VS.85).aspx)
-   [Trace Capture, Processing, and Analysis Tool](https://msdn.microsoft.com/performance/cc825801.aspx)
-   [CRT Debug Heap](https://msdn.microsoft.com/library/974tc9t1(v=VS.71).aspx)

*Additional Links:*

-   [**auto\_ptr Class**](https://msdn.microsoft.com/library/ew3fk483(v=VS.71).aspx)
-   [Active Template Library (ATL) Memory Classes](https://msdn.microsoft.com/library/44yh1z4f(v=VS.71).aspx)
-   [**\_com\_ptr\_t Object**](https://msdn.microsoft.com/library/417w8b3b(v=VS.71).aspx)
-   [**\_bstr\_t Class**](https://msdn.microsoft.com/library/zthfhkd6(v=VS.71).aspx)
-   [**\_variant\_yt Class**](https://msdn.microsoft.com/library/x295h94e(v=VS.71).aspx)
-   ["Tracking down managed memory leaks"](https://blogs.msdn.com/ricom/archive/2004/12/10/279612.aspx)
-   ["Understanding and Solving Internet Explorer Leak Patterns"](https://msdn.microsoft.com/library/ms976398(v=MSDN.10).aspx)
-   ["JavaScript Memory Leak Detector"](https://blogs.msdn.com/b/gpde/archive/2008/01/16/new-javascript-memory-leak-detector-from-our-team.aspx)
-   [Circular Memory Leak Mitigation (in browsers):](https://msdn.microsoft.com/library/Dd361842(v=VS.85).aspx)
-   [**try-finally statement**](https://msdn.microsoft.com/library/yb3kz605(v=VS.71).aspx)
-   [**PROPVARIANT Structure**](https://msdn.microsoft.com/library/Aa380072(v=VS.85).aspx)
-   [**PropVariantClear Function**](https://msdn.microsoft.com/library/Aa380073(v=VS.85).aspx)

 

 



