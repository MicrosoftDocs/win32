---
Description: .
ms.assetid: c5dedcab-3e6f-433f-95de-d741321c683e
title: Preventing Memory Leaks in Windows Applications
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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

-   Heap memory via the [**HeapAlloc**](https://msdn.microsoft.com/windows/desktop/9a176312-0312-4cc1-baf5-949b346d983e) function or its C/C++ runtime equivalents **malloc** or **new**
-   Direct allocations from the operating system via the [**VirtualAlloc**](https://msdn.microsoft.com/windows/desktop/a720dd89-c47c-4e48-bbc6-f2e02dfc4ed2) function.
-   Kernel handles created via Kernel32 APIs such as [**CreateFile**](https://msdn.microsoft.com/windows/desktop/80a96083-4de9-4422-9705-b8ad2b6cbd1b), [**CreateEvent**](https://msdn.microsoft.com/windows/desktop/1f6d946e-c74c-4599-ac3d-b709216a0900), or [**CreateThread**](https://msdn.microsoft.com/windows/desktop/202a4b42-513a-45de-894a-72e56c706a58), hold kernel memory on behalf of the application
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
-   Be aware of leak patterns in web client-side code. Circular references between COM objects and scripting engines like JScript can cause large leaks in web applications. ["Understanding and Solving Internet Explorer Leak Patterns"](https://www.bing.com/search?q="Understanding and Solving Internet Explorer Leak Patterns") has more information on these kinds of leaks. You can use the JavaScript Memory Leak Detector to debug memory leaks in your code. While Windows Internet Explorer 8, which is shipping with Windows 7, mitigates most of these issues, older browsers are still vulnerable to these bugs
-   Avoid using multiple exit paths from a function. Allocations assigned to variables at function scope should be freed in one particular block at the end of the function
-   Do not use exceptions in your code without freeing all local variables in functions. If you use native exceptions, free all your allocations inside the \_\_finally block. If you use C++ exceptions, all your heap and handle allocations need to be wrapped in smart pointers
-   Do not discard or reinitialize a [**PROPVARIANT**](https://msdn.microsoft.com/windows/desktop/e86cc279-826d-4767-8d96-fc8280060ea1) object without calling the [**PropVariantClear**](https://msdn.microsoft.com/windows/desktop/062b6065-a56f-4ecd-b232-3ba338a6d806) function

## Links to Resources

*Common Allocation Patterns:*

-   [**Heap Allocation Function**](https://msdn.microsoft.com/windows/desktop/9a176312-0312-4cc1-baf5-949b346d983e)
-   [**Memory Allocation Function**](https://msdn.microsoft.com/windows/desktop/144fcee2-be34-4a03-bb7e-ed6d4b99eea0)
-   [**New Operator (C++)**](https://msdn.microsoft.com/windows/desktop/69fee812-1c28-4882-8fda-d1ad17860004)
-   [**Virtual Allocation Function**](https://msdn.microsoft.com/windows/desktop/a720dd89-c47c-4e48-bbc6-f2e02dfc4ed2)
-   [Kernel Objects](https://msdn.microsoft.com/windows/desktop/3e3288dd-155a-41d0-9d43-5f49ed4c4a9d)
-   [GDI Object Handles](https://msdn.microsoft.com/windows/desktop/699de25c-083d-4be3-a997-67418b7173e1)
-   [User Interface Object Handles](https://msdn.microsoft.com/windows/desktop/07edc049-26d9-4f42-a5e7-e1f4c8435a6c)

*Microsoft Tools:*

-   [Application Verifier](application-verifier.md)
-   [Debugging Tools for Windows](https://www.bing.com/search?q=Debugging Tools for Windows)
-   [User-Mode Dump Heap](https://www.bing.com/search?q=User-Mode Dump Heap)
-   [Trace Capture, Processing, and Analysis Tool](http://go.microsoft.com/fwlink/p/?linkid=205150)
-   [CRT Debug Heap](https://msdn.microsoft.com/windows/desktop/bf78ace6-28e4-4a04-97c6-39e0cdd00ba4)

*Additional Links:*

-   [**auto\_ptr Class**](https://msdn.microsoft.com/windows/desktop/7f9108b6-9eb3-4634-b615-cf7aa814f23b)
-   [Active Template Library (ATL) Memory Classes](https://msdn.microsoft.com/windows/desktop/be564a5e-577e-40a7-bfe3-25ad21e57270)
-   [**\_com\_ptr\_t Object**](https://msdn.microsoft.com/windows/desktop/3753a8a0-03d4-4cfd-8a9a-74872ea53971)
-   [**\_bstr\_t Class**](https://msdn.microsoft.com/windows/desktop/58841fef-fe21-4a84-aab9-780262b5201f)
-   [**\_variant\_yt Class**](https://msdn.microsoft.com/windows/desktop/6a3cbd4e-0ae8-425e-b4cf-ca0df894c93f)
-   ["Tracking down managed memory leaks"](http://go.microsoft.com/fwlink/p/?linkid=205152)
-   ["Understanding and Solving Internet Explorer Leak Patterns"](https://www.bing.com/search?q="Understanding and Solving Internet Explorer Leak Patterns")
-   ["JavaScript Memory Leak Detector"](http://go.microsoft.com/fwlink/p/?linkid=205153)
-   [Circular Memory Leak Mitigation (in browsers):](https://www.bing.com/search?q=Circular Memory Leak Mitigation (in browsers):)
-   [**try-finally statement**](https://msdn.microsoft.com/windows/desktop/514400c1-c322-4bf3-9e48-3047240b8a82)
-   [**PROPVARIANT Structure**](https://msdn.microsoft.com/windows/desktop/e86cc279-826d-4767-8d96-fc8280060ea1)
-   [**PropVariantClear Function**](https://msdn.microsoft.com/windows/desktop/062b6065-a56f-4ecd-b232-3ba338a6d806)

 

 



