---
title: Debugging Resource DLLs
description: Because the Cluster service runs as a service and the Resource Monitor runs as a separate process, debugging resource DLLs can be more complicated than debugging regular DLLs or applications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1caa8fe7-e1fb-48f1-9823-2896faeaa320'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource DLLs Failover Cluster ,debugging"]
---

# Debugging Resource DLLs

Because the [Cluster service](cluster-service.md) runs as a service and the [Resource Monitor](resource-monitor.md) runs as a separate process, debugging [resource DLLs](resource-dlls.md) can be more complicated than debugging regular DLLs or applications.

The following procedure describes how to debug a resource DLL:

**To debug a resource DLL**

1.  Configure your environment for debugging. For information, see [Preparing a Development Environment](preparing-a-development-environment.md).

2.  Stop the Cluster service using the following command:

    **Net Stop ClusSvc**

3.  Restart the Cluster service locally by typing the following command from the cluster directory:

    **Start ClusSvc -debug**

    When the Cluster service starts, it creates a [Resource Monitor](resource-monitor.md) for your resource and attaches your debugger to it. At this point, your debugger is invoked. You can now set breakpoints in the DLL. For example, to debug the [**ResourceTypeControl**](resourcetypecontrol.md) entry point function, attach a debugger to the main Resource Monitor process and set a breakpoint at **s\_RmResourceTypeControl**. You can set additional breakpoints in the DLL once the call to [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) is stepped over.

4.  Start [Cluster Administrator](cluster-administrator.md).

5.  Create a new [resource](resources.md) of the type supported by your resource DLL. Specify that the resource should run in a separate Resource Monitor. A dedicated Resource Monitor is required during debugging to help you isolate problems and ensure that other resources remain unaffected by those problems.

6.  View the properties of the new resource by clicking **Properties** on the **File** menu after selecting the new resource.

7.  Click the **Debug** tab.

8.  In the **Debug Command Prefix** edit control, type the full path to your debugger.

9.  Click **OK**.

The following procedure describes how to debug a resource type:

**To debug a resource type**

1.  Set the resource type's [**DebugControlFunctions**](resource-types-debugcontrolfunctions.md) property to **TRUE**. Use the following PowerShell invocation:

    **Get-ClusterResource** *DisplayName* **\| Set-ClusterParameter DebugControlFunctions 1**

    Substitute the [display name](display-names.md) of your resource type for *DisplayName*.

    **Windows Server 2008:  **

    PowerShell cmdlets for failover clustering are not available. Use the following Cluster.exe command instead:

    **cluster restype** *DisplayName* **/prop DebugControlFunctions=1**

2.  Set the resource type's [**DebugPrefix**](resource-types-debugprefix.md) property to the path to your debugger. Use the following PowerShell invocation:

    **Get-ClusterResource** *DisplayName* **\| Set-ClusterParameter DebugPrefix** *path*

    Substitute the display name of your resource type for *DisplayName* and the path to your debugger for *path*.

    **Windows Server 2008:  **

    PowerShell cmdlets for failover clustering are not available. Use the following Cluster.exe command instead:

    **cluster restype** *DisplayName* **/prop DebugPrefix=***path*

    When your [**ResourceTypeControl**](resourcetypecontrol.md) entry point function is called, the [Cluster service](cluster-service.md) checks the settings for these properties. If [**DebugControlFunctions**](resource-types-debugcontrolfunctions.md) is set to **TRUE** and [**DebugPrefix**](resource-types-debugprefix.md) contains a valid path, the Cluster service creates a new [Resource Monitor](resource-monitor.md) process for [**ResourceTypeControl**](resourcetypecontrol.md) and attaches the specified debugger to it.

3.  If you want to debug startup code (the [**Startup**](startup.md) and [**Open**](open.md) entry point functions) in a resource DLL while the resource is being created, set the [**DebugPrefix**](resource-types-debugprefix.md) property on the resource type beforehand by invoking PowerShell failover cluster cmdlets. Then, when a resource is created, select the **Use Separate Resource Monitor** check box, and click the **Next** button to start the debugger immediately.

    **Windows Server 2008:  **

    You can also use Cluster.exe to set the [**DebugPrefix**](resource-types-debugprefix.md) property.

4.  When a resource of the specified type is created, the Resource Monitor waits until the debugger has attached. The Resource Monitor then calls [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) followed by [**DebugBreak**](https://msdn.microsoft.com/library/windows/desktop/ms679297). Some debuggers (such as CDB and WinDbg) also break when they attach, while others (such as MsDev) do not. In any case, the Resource Monitor displays a message in the debugger's output window when the debugger attaches and after loading the resource DLL.

 

 




