---
title: Internal Control Codes
description: Internal control codes are used exclusively by the Cluster service to notify resource DLLs of certain events. Applications cannot use internal control codes in control code functions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '94ae855b-1e57-4378-8177-20d06225f805'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["control codes Failover Cluster ,internal"]
---

# Internal Control Codes

Internal [control codes](about-control-codes.md) are used exclusively by the [Cluster service](cluster-service.md) to notify [resource DLLs](resource-dlls.md) of certain events. Applications cannot use internal control codes in [control code functions](control-code-functions.md).

If you are implementing a resource DLL, you can choose to support any internal control code that indicates an event with implications for your resources. However, note the following behavior:

-   Unless otherwise specified in the description of the control code, [internal resource control codes](internal-resource-control-codes.md) are sent to every [resource](resources.md) in the [*cluster*](c-gly.md#-wolf-cluster-gly). This means your [**ResourceControl**](resourcecontrol.md) entry point will receive one call for every resource currently supported by your DLL.
-   Unless otherwise specified in the description of the control code, [internal resource type control codes](internal-resource-type-control-codes.md) are sent to every resource type in the cluster. This means your [**ResourceTypeControl**](resourcetypecontrol.md) entry point will receive one call for every [resource type](resource-types.md) supported by your DLL.

For example, suppose a resource DLL supports three resource types and is currently managing five resource instances in the cluster. The administrator evicts a node. The resource DLL will receive the [CLUSCTL\_RESOURCE\_TYPE\_EVICT\_NODE](clusctl-resource-type-evict-node.md) control code three times (one call per resource type) through the [**ResourceTypeControl**](resourcetypecontrol.md) entry point, and will receive the [CLUSCTL\_RESOURCE\_EVICT\_NODE](clusctl-resource-evict-node.md) control code five times (one call per resource instance) through the [**ResourceControl**](resourcecontrol.md) entry point.

 

 




