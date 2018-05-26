---
title: Implementing Resource DLLs
description: For each resource type supported by your resource DLL, you must provide implementations for all of the entry point functions except for Arbitrate and Release. You need to implement Arbitrate and Release only if your resource type is quorum-capable.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 400862c3-73c4-443d-bc60-1c1b6b34534f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource DLLs Failover Cluster ,implementing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing Resource DLLs

For each [resource type](resource-types.md) supported by your [resource DLL](resource-dlls.md), you must provide implementations for all of the entry point functions except for [**Arbitrate**](/windows/previous-versions/ResApi/nc-resapi-parbitrate_routine?branch=master) and [**Release**](/windows/previous-versions/ResApi/nc-resapi-prelease_routine?branch=master). You need to implement **Arbitrate** and **Release** only if your resource type is [*quorum-capable*](q-gly.md#-wolf-quorum-capable-resource-gly).

Implementing a resource DLL involves tasks that are qualified as follows:

-   Required: Your implementation must perform these tasks or the resource type or resource DLL will not function.
-   Recommended: Although not strictly required, these tasks are recommended for convenience, optimization, or improved performance.
-   Optional: Identifies tasks you can perform as a matter of preference.

**To implement a resource DLL**

1.  Required: Implement **DllMain** and [**Startup**](/windows/previous-versions/ResApi/nc-resapi-pstartup_routine?branch=master) to initialize the DLL and each supported resource type. See [Performing Initialization](performing-initialization.md).
2.  Required: Implement [**Open**](/windows/previous-versions/ResApi/nc-resapi-popen_routine?branch=master) and [**Close**](/windows/previous-versions/ResApi/nc-resapi-pclose_routine?branch=master) to manage the creation and deletion of resource instances. See [Managing Instances](managing-instances.md).
3.  Required: Implement [**Online**](/windows/previous-versions/ResApi/nc-resapi-ponline_routine?branch=master), [**Offline**](/windows/previous-versions/ResApi/nc-resapi-poffline_routine?branch=master), and [**Terminate**](/windows/previous-versions/ResApi/nc-resapi-pterminate_routine?branch=master) to start and stop resource instances on demand. See [Managing State Transitions](managing-state-transitions.md).
4.  Required: Implement [**IsAlive**](/windows/previous-versions/ResApi/nc-resapi-pis_alive_routine?branch=master) and [**LooksAlive**](/windows/previous-versions/ResApi/nc-resapi-plooks_alive_routine?branch=master) to detect and respond to possible resource failures. See [Detecting Resource Failure](detecting-resource-failure.md).
5.  Required: Implement [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) and [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) to handle control codes. See [Supporting Control Codes](supporting-control-codes.md).

For an example, see the ClipBookServer sample (previously known as ClipBook) that is included with the Windows SDK.

 

 




