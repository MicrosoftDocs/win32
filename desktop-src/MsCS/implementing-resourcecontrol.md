---
title: Implementing ResourceControl
description: When the ResourceControl entry point is invoked by a cluster service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3aa4a591-b0ae-4f2f-8642-f524f7207397'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["entry point functions Failover Cluster ,implementing ResourceControl", "ResourceControl Failover Cluster ,implementing"]
---

# Implementing ResourceControl

The [Cluster service](cluster-service.md) (through a [Resource Monitor](resource-monitor.md)) invokes the [**ResourceControl**](resourcecontrol.md) entry point function when:

-   An application calls [**ClusterResourceControl**](clusterresourcecontrol.md) to initiate a [control code](control-codes.md) operation.
-   The [resource DLL](resource-dlls.md) needs to be notified of a [*cluster*](c-gly.md#-wolf-cluster-gly) event such as an upgrade.

In both cases, a control code is passed to the resource DLL as an input parameter. The DLL can implement the control code operation, instruct the Resource Monitor to handle the operation, or both.

Some control codes should be handled by the Resource Monitor; others require or benefit from customized implementation in the DLL. To determine how and why to support a particular control code, refer to the individual control code descriptions in [Control Codes](control-codes.md).

To request that the Resource Monitor process a control code, return **ERROR\_INVALID\_FUNCTION**. You can return this value for a control code even if you include support for the code in [**ResourceControl**](resourcecontrol.md), allowing you to augment the default functionality of the Resource Monitor.

As with all entry point functions, follow the [Recommended Practices for Resource DLLs](recommended-practices-for-resource-dlls.md).

## Example

See [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).

 

 




