---
title: Configuring Resources
description: Configuring a resource is the process of adjusting its properties, establishing its required dependencies, and making other changes so that it is ready to be brought online.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ff5376f2-2d43-4fbd-b560-07049ab93b16'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resources Failover Cluster ,configuring"]
---

# Configuring Resources

Configuring a [resource](resources.md) is the process of adjusting its properties, establishing its required [dependencies](resource-dependencies.md), and making other changes so that it is ready to be brought online.

1.  Assign values to all of the resource's required [private properties](private-properties.md). (See [Setting Properties](setting-properties.md).)
2.  Assign values to any of the resource's other [private](private-properties.md) or [common properties](common-properties.md) as necessary. For example, set any special failure or [failover](failover.md) policies for the resource.
3.  If necessary, create registry and crypto [checkpoints](checkpointing.md) for the resource by calling [**ClusterResourceControl**](clusterresourcecontrol.md) with the [CLUSCTL\_RESOURCE\_ADD\_CRYPTO\_CHECKPOINT](clusctl-resource-add-crypto-checkpoint.md) and [CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT](clusctl-resource-add-registry-checkpoint.md) control codes.
4.  Get the required dependencies of the resource by using the [CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-get-required-dependencies.md) control code.
5.  If the resource has required dependencies, you must create and configure those resources as well. The dependencies may have required dependencies of their own. Create all the required resources and call [**AddClusterResourceDependency**](addclusterresourcedependency.md) to establish each required dependency relationship.
6.  Create additional dependencies as desired.
7.  If the resource is a server application being published to clients through a failover cluster instance, use the [service utility functions](service-utility-functions.md) to initialize an appropriate service environment.

## Example Code

The following sections contain examples of resource configuration:

-   [Creating Physical Disk Resources](creating-physical-disk-resources.md)
-   [Creating IP Address Resources](creating-ip-address-resources.md)
-   [Creating Network Name Resources](creating-network-name-resources.md)

 

 




