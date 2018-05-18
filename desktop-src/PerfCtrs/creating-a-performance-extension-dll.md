---
Description: 'A provider is a performance DLL that provides counter data to consumers.'
ms.assetid: 'bbb777fe-b97e-4777-b797-ec8525065610'
title: Creating a Performance Extension DLL
---

# Creating a Performance Extension DLL

A provider is a performance DLL that provides counter data to consumers. The performance DLL must export the [**OpenPerformanceData**](openperformancedata.md), [**CollectPerformanceData**](collectperformancedata.md), and [**ClosePerformanceData**](closeperformancedata.md) functions. Typically, you use a module definition (.def) file to export the functions. The system calls these functions when a consumer queries performance data.

The first time a consumer calls [**RegQueryValueEx**](https://msdn.microsoft.com/library/windows/desktop/ms724911), or if the consumer uses the [**RegOpenKey**](https://msdn.microsoft.com/library/windows/desktop/ms724895) or [**RegConnectRegistry**](https://msdn.microsoft.com/library/windows/desktop/ms724840) function to open **HKEY\_PERFORMANCE\_DATA**, the system calls the [**OpenPerformanceData**](openperformancedata.md) function for each provider that is [registered](adding-performance-counters.md) on the computer. The exception is if the provider specifies the list of objects that it supports in the \[objects\] section of the .INI file. In this case, the system calls the provider only if one of the queried objects matches an object from the list.

The [**OpenPerformanceData**](openperformancedata.md) function gives each provider an opportunity to initialize its performance data structures. Then, if the **OpenPerformanceData** function returns successfully, the system calls the provider's [**CollectPerformanceData**](collectperformancedata.md) function. Subsequent calls to [**RegQueryValueEx**](https://msdn.microsoft.com/library/windows/desktop/ms724911) cause the system to call the **CollectPerformanceData** function.

When the consumer finishes collecting performance data, it specifies **HKEY\_PERFORMANCE\_DATA** in a call to the [**RegCloseKey**](https://msdn.microsoft.com/library/windows/desktop/ms724837) function. This causes the system to call the [**ClosePerformanceData**](closeperformancedata.md) function for each provider. The providers are then unloaded.

It is possible for multiple consumers to collect performance data at the same time. The system calls [**OpenPerformanceData**](openperformancedata.md) and [**ClosePerformanceData**](closeperformancedata.md) functions only once for each consumer requesting performance data.

> [!Note]  
> Be sure to include extern "C" in your C++ code to prevent the compiler from adding decorations to your function names; otherwise, the system will fail to call your functions. If this occurs, the system adds a **Disable Performance Counters** value to your **Performance** key and disables your provider.

 

For more information on writing a performance DLL, see the following topics:

-   [Implementing the OpenPerformanceData function](implementing-openperformancedata.md)
-   [Implementing the CollectPerformanceData function](implementing-collectperformancedata.md)
-   [Error Handling in the DLL](error-handling-in-the-dll.md)
-   [Restricting Access to Performance Extension DLLs](restricting-access-to-performance-extension--dlls.md)
-   [Performance DLL Samples](performance-dll-samples.md)

 

 



