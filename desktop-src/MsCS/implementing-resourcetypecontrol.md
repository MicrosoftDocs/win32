---
title: Implementing ResourceTypeControl
description: When the ResourceTypeControl entry point is invoked by a cluster service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 23d16976-1491-43d7-9dea-9cd8ae8086cb
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- entry point functions Failover Cluster ,implementing ResourceTypeControl
- ResourceTypeControl Failover Cluster ,implementing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing ResourceTypeControl

The [Cluster service](cluster-service.md) (through a [Resource Monitor](resource-monitor.md)) invokes the [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master) entry point function when:

-   An application calls [**ClusterResourceTypeControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcetypecontrol?branch=master) to initiate a [control code](control-codes.md) operation.
-   The [resource DLL](resource-dlls.md) needs to be notified of a [*cluster*](c-gly.md#-wolf-cluster-gly) event such as an upgrade.

In both cases, a control code is passed to the resource DLL as an input parameter. The DLL can implement the control code operation, instruct the Resource Monitor to handle the operation, or both.

Some control codes should be handled by the Resource Monitor; others require or benefit from customized implementation in the DLL. Support for any of the other control codes is optional. To determine how and why to support a particular control code, see [Control Codes](control-codes.md).

To request that the Resource Monitor process a control code, return **ERROR\_INVALID\_FUNCTION**. You can return this value for a control code even if you include support for the code in [**ResourceTypeControl**](/windows/previous-versions/ResApi/nc-resapi-presource_type_control_routine?branch=master), allowing you to augment the default functionality of the Resource Monitor.

As with all entry point functions, follow the [Recommended Practices for Resource DLLs](recommended-practices-for-resource-dlls.md).

## Example

See [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).

 

 




