---
Description: '.'
ms.assetid: 'c5dedcab-3e6f-433f-95de-d741321c683e'
title: Preventing Memory Leaks in Windows Applications
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

-   Heap memory via the [**HeapAlloc**](base.heapalloc) function or its C/C++ runtime equivalents **malloc** or **new**
-   Direct allocations from the operating system via the [**VirtualAlloc**](base.virtualalloc) function.
-   Kernel handles created via Kernel32 APIs such as [**CreateFile**](fs.createfile), [**CreateEvent**](base.createevent), or [**CreateThread**](base.createthread), hold kernel memory on behalf of the application
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
-   Monitor your .NET code unusual memory usage. Managed code is not immune to memory leaks. See ["Tracking down managed memory leaks"](http://go.microsoft.com/fwlink/p/?linkid=205152) on how to find GC leaks
-   Be aware of leak patterns in web client-side code. Circular references between COM objects and scripting engines like JScript can cause large leaks in web applications. ["Understanding and Solving Internet Explorer Leak Patterns"](ie_leak_patterns) has more information on these kinds of leaks. You can use the JavaScript Memory Leak Detector to debug memory leaks in your code. While Windows Internet Explorer 8, which is shipping with Windows 7, mitigates most of these issues, older browsers are still vulnerable to these bugs
-   Avoid using multiple exit paths from a function. Allocations assigned to variables at function scope should be freed in one particular block at the end of the function
-   Do not use exceptions in your code without freeing all local variables in functions. If you use native exceptions, free all your allocations inside the \_\_finally block. If you use C++ exceptions, all your heap and handle allocations need to be wrapped in smart pointers
-   Do not discard or reinitialize a [**PROPVARIANT**](stg.propvariant) object without calling the [**PropVariantClear**](stg.propvariantclear) function

## Links to Resources

*Common Allocation Patterns:*

-   [**Heap Allocation Function**](base.heapalloc)
-   [**Memory Allocation Function**](144fcee2-be34-4a03-bb7e-ed6d4b99eea0)
-   [**New Operator (C++)**](69fee812-1c28-4882-8fda-d1ad17860004)
-   [**Virtual Allocation Function**](base.virtualalloc)
-   [Kernel Objects](base.kernel_objects)
-   [GDI Object Handles](base.gdi_objects)
-   [User Interface Object Handles](base.user_objects)

*Microsoft Tools:*

-   [Application Verifier](application-verifier.md)
-   [Debugging Tools for Windows](debugger.introduction6)
-   [User-Mode Dump Heap](debugger.umdh)
-   [Trace Capture, Processing, and Analysis Tool](http://go.microsoft.com/fwlink/p/?linkid=205150)
-   [CRT Debug Heap](bf78ace6-28e4-4a04-97c6-39e0cdd00ba4)

*Additional Links:*

-   [**auto\_ptr Class**](7f9108b6-9eb3-4634-b615-cf7aa814f23b)
-   [Active Template Library (ATL) Memory Classes](be564a5e-577e-40a7-bfe3-25ad21e57270)
-   [**\_com\_ptr\_t Object**](3753a8a0-03d4-4cfd-8a9a-74872ea53971)
-   [**\_bstr\_t Class**](58841fef-fe21-4a84-aab9-780262b5201f)
-   [**\_variant\_yt Class**](6a3cbd4e-0ae8-425e-b4cf-ca0df894c93f)
-   ["Tracking down managed memory leaks"](http://go.microsoft.com/fwlink/p/?linkid=205152)
-   ["Understanding and Solving Internet Explorer Leak Patterns"](ie_leak_patterns)
-   ["JavaScript Memory Leak Detector"](http://go.microsoft.com/fwlink/p/?linkid=205153)
-   [Circular Memory Leak Mitigation (in browsers):](ie8_memory_management)
-   [**try-finally statement**](514400c1-c322-4bf3-9e48-3047240b8a82)
-   [**PROPVARIANT Structure**](stg.propvariant)
-   [**PropVariantClear Function**](stg.propvariantclear)

 

 



