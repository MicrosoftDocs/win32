---
title: Implementing Resource DLLs
description: For each resource type supported by your resource DLL, you must provide implementations for all of the entry point functions except for Arbitrate and Release. You need to implement Arbitrate and Release only if your resource type is quorum-capable.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '400862c3-73c4-443d-bc60-1c1b6b34534f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource DLLs Failover Cluster ,implementing"]
---

# Implementing Resource DLLs

For each [resource type](resource-types.md) supported by your [resource DLL](resource-dlls.md), you must provide implementations for all of the entry point functions except for [**Arbitrate**](arbitrate.md) and [**Release**](release.md). You need to implement **Arbitrate** and **Release** only if your resource type is [*quorum-capable*](q-gly.md#-wolf-quorum-capable-resource-gly).

Implementing a resource DLL involves tasks that are qualified as follows:

-   Required: Your implementation must perform these tasks or the resource type or resource DLL will not function.
-   Recommended: Although not strictly required, these tasks are recommended for convenience, optimization, or improved performance.
-   Optional: Identifies tasks you can perform as a matter of preference.

**To implement a resource DLL**

1.  Required: Implement **DllMain** and [**Startup**](startup.md) to initialize the DLL and each supported resource type. See [Performing Initialization](performing-initialization.md).
2.  Required: Implement [**Open**](open.md) and [**Close**](close.md) to manage the creation and deletion of resource instances. See [Managing Instances](managing-instances.md).
3.  Required: Implement [**Online**](online.md), [**Offline**](offline.md), and [**Terminate**](terminate.md) to start and stop resource instances on demand. See [Managing State Transitions](managing-state-transitions.md).
4.  Required: Implement [**IsAlive**](isalive.md) and [**LooksAlive**](looksalive.md) to detect and respond to possible resource failures. See [Detecting Resource Failure](detecting-resource-failure.md).
5.  Required: Implement [**ResourceControl**](resourcecontrol.md) and [**ResourceTypeControl**](resourcetypecontrol.md) to handle control codes. See [Supporting Control Codes](supporting-control-codes.md).

For an example, see the ClipBookServer sample (previously known as ClipBook) that is included with the Windows SDK.

 

 




