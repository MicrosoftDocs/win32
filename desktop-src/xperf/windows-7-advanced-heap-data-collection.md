---
title: Windows 7 Advanced Heap Data Collection
description: Windows 7 Advanced Heap Data Collection
ms.assetid: 29656c3f-6b82-4275-997d-f9ef10ca2601
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows 7 Advanced Heap Data Collection

> [!Note]  
> The topics in this section pertain only to Windows 7 and later versions of Windows.

 

In the Quick Start section of this documentation [Enabling Data Capture on Process Launch](quick-start---enabling-data-capture-on-process-launch.md) and [Enabling Data Capture on Existing Process](quick-start---enabling-data-capture-on-an-existing-process.md) discussed methods of data capture that would typically be available to end users of WPA. Both of these methods rely on WPA to control when process heap tracing begins. This is the case for both new processes and existing processes. Advanced users and developers recognize a number of issues that would arise when using either of these methods. Two new heap data capture options, IFEO and AutoLogger, address these issues.

Ideally, the use of an intermediate software layer to arbitrarily control process start times should be avoided. The analyst should have complete control of process starts. By giving the analyst this level of control more meaningful data can be collected. Also, as a side benefit of direct control, the number of processes that can be tracked is increased as are the dependencies between several interacting programs.

For example, WPA requires administrator privileges. As a result, all processes launched by WPA inherit administrator privileges. This can dramatically alter process behavior and/or functionality. In addition, some processes cannot be run with administrator privileges. Also, in some cases, particularity with services, WPA does not have the correct security context. The result is the service process will not execute. The better case is to begin tracing automatically when a process starts. By beginning tracing automatically when a process starts with IFEO, the process uses the regular security context of that process.

Starting heap tracing at boot times is not possible using command line syntax. However, by leveraging the [On/Off Transition Trace Capture tool](on-off-transition-trace-capture-tool.md) facilities and setting AutoLogger registry values, tracing can be started at boot time with no loss of data. This allows the analyst to develop a complete picture of process heap usage throughout the entire boot process and subsequent activity.

In order to initiate heap tracing two requirements must be met.

1.  A flag must be set in the Process Environment Block (PEB) for each process to be traced.

2.  Heap tracing must be turned on in the kernel.

Implementing Image File Execution Options (IFEO) or AutoLogger with WPA meets these requirements. Setting IFEO, the Process Environment Block is modified at process startup to automatically begin heap tracing. By using AutoLogger with WPA On/Off Transition Trace Capture, tracing can be started at boot time. The following two examples will demonstrate how to implement these techniques.

> [!Note]  
> IFEO and AutoLogger settings require the user to be familiar with Windows Internals and be comfortable working with the Windows Registry.

 

This section includes the following topics:

<dl>

[Image File Execution Options](image-file-execution-options.md)  
[AutoLogger](autologger.md)  
</dl>

 

 




