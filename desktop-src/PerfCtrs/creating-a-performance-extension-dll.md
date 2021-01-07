---
description: A provider is a performance DLL that provides counter data to consumers.
ms.assetid: bbb777fe-b97e-4777-b797-ec8525065610
title: Creating a Performance Extension DLL
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Performance Extension DLL

> [!IMPORTANT]
> Due to significant performance and reliability limitations, the method for providing performance counter data that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the method described in [Providing Counter Data Using Version 2.0](providing-counter-data-using-version-2-0.md) for creating new performance counters and that you migrate existing performance counters to use that method as well.

A [V1 provider](providing-counter-data.md) uses a performance DLL that provides counter data to consumers. The performance DLL must export the [**OpenPerformanceData**](/previous-versions/windows/desktop/legacy/aa372200(v=vs.85)), [**CollectPerformanceData**](/windows/win32/api/winperf/nc-winperf-pm_collect_proc), and [**ClosePerformanceData**](/windows/win32/api/winperf/nc-winperf-pm_close_proc) functions. Typically, you use a module definition (.def) file to export the functions from the DLL. The system calls these functions when a consumer queries performance data.

The first time a consumer calls [**RegQueryValueEx**](/windows/desktop/api/winreg/nf-winreg-regqueryvalueexa), or if the consumer uses the [**RegOpenKey**](/windows/desktop/api/winreg/nf-winreg-regopenkeya) or [**RegConnectRegistry**](/windows/desktop/api/winreg/nf-winreg-regconnectregistrya) function to open `HKEY_PERFORMANCE_DATA`, the system calls the [**OpenPerformanceData**](/previous-versions/windows/desktop/legacy/aa372200(v=vs.85)) function for each provider that is [registered](adding-performance-counters.md) on the computer. The exception is if the provider specifies the list of objects that it supports in the `[objects]` section of the .INI file. In this case, the system calls the provider only if one of the queried objects matches an object from the list.

The [**OpenPerformanceData**](/previous-versions/windows/desktop/legacy/aa372200(v=vs.85)) function gives each provider an opportunity to initialize its performance data structures. Then, if the **OpenPerformanceData** function returns successfully, the system calls the provider's [**CollectPerformanceData**](/windows/win32/api/winperf/nc-winperf-pm_collect_proc) function. Subsequent calls to [**RegQueryValueEx**](/windows/desktop/api/winreg/nf-winreg-regqueryvalueexa) cause the system to call the **CollectPerformanceData** function.

When the consumer finishes collecting performance data, it specifies `HKEY_PERFORMANCE_DATA` in a call to the [**RegCloseKey**](/windows/desktop/api/winreg/nf-winreg-regclosekey) function. This causes the system to call the [**ClosePerformanceData**](/windows/win32/api/winperf/nc-winperf-pm_close_proc) function for each provider. The providers are then unloaded.

It is possible for multiple consumers to collect performance data at the same time. The system calls [**OpenPerformanceData**](/previous-versions/windows/desktop/legacy/aa372200(v=vs.85)) and [**ClosePerformanceData**](/windows/win32/api/winperf/nc-winperf-pm_close_proc) functions only once each time the DLL is loaded or unloaded.

> [!Note]
> Be sure to include extern "C" in your C++ code to prevent the compiler from adding decorations to your function names; otherwise, the system may fail to find your functions.

> [!Note]
> If an error occurs while loading your performance DLL, finding your functions, or calling your functions, the system will disable the provider for subsequent collections within the same process. In addition, if this occurs while running in a privileged process, the system adds a **Disable Performance Counters** value to your **Performance** key to prevent the provider from being loaded in the future.

For more information on writing a performance DLL, see the following topics:

- [Implementing the OpenPerformanceData function](implementing-openperformancedata.md)
- [Implementing the CollectPerformanceData function](implementing-collectperformancedata.md)
- [Error Handling in the DLL](error-handling-in-the-dll.md)
- [Restricting Access to Performance Extension DLLs](restricting-access-to-performance-extension--dlls.md)
- [Performance DLL Samples](performance-dll-samples.md)
