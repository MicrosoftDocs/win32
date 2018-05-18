---
title: Creating Resources
description: General procedure for creating a resource using the Failover Cluster API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'eef2ffe6-b3d4-47c9-8867-a81ed9d66438'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resources Failover Cluster ,creating"]
---

# Creating Resources

The following procedure describes the general process of creating a [resource](resources.md).

**To Create a Resource**

1.  Obtain a handle to a new or existing [group](groups.md) in which to create the resource. See [**CreateClusterGroup**](createclustergroup.md) and [**OpenClusterGroup**](openclustergroup.md).
2.  Determine the name of the new resource. The name must be unique in the [*cluster*](c-gly.md#-wolf-cluster-gly).
3.  Determine whether the new resource should have its own [Resource Monitor](resource-monitor.md). This should be done only for volatile or unstable resources or for debugging.
4.  Call [**CreateClusterResource**](createclusterresource.md) to create a new resource in the specified group.

The resource may need to be configured before it can be brought online. For configuration procedures see [Configuring Resources](configuring-resources.md) and [Copying Resource Configurations](copying-resource-configurations.md).

## Example Code

The following sections contain examples of resource configuration.

-   [Creating Physical Disk Resources](creating-physical-disk-resources.md)
-   [Creating IP Address Resources](creating-ip-address-resources.md)
-   [Creating Network Name Resources](creating-network-name-resources.md)

 

 




