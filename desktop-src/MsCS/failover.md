---
title: Failover
description: Defines Failover Cluster group failover behavior.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6722d075-02e0-4817-abc3-dce8951c17da
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- failover Failover Cluster
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Failover

The [Cluster service](cluster-service.md) attempts to fail over a [group](groups.md) when:

-   The [node](nodes.md) currently hosting the group becomes inactive for any reason.
-   One of the [resources](resources.md) within the group fails, and the resource's [**RestartAction**](resources-restartaction.md) property is set to **ClusterResourceRestartNotify**.
-   An administrator or developer forces failover.

A failover attempt consists of the following steps:

1.  The Cluster service takes all the resources in the group offline in an order determined by the group's [dependency](resource-dependencies.md) hierarchy: dependent resources first, followed by the resources on which they depend. For example, if an application depends on a [Physical Disk](physical-disk.md) resource, the Cluster service takes the application offline first, allowing the application to write changes to the disk before the disk is taken offline.

    The Cluster service takes a resource offline by invoking, through a [Resource Monitor](resource-monitor.md), the [**Offline**](/windows/previous-versions/ResApi/nc-resapi-poffline_routine?branch=master) entry point function of the [resource DLL](resource-dlls.md) managing the resource. **Offline** implements shutdown procedures for the resource. If the resource does not shut down within a time limit specified by the resource's [**PendingTimeout**](resources-pendingtimeout.md) property, the Cluster service forcefully terminates the resource by calling the resource DLL's [**Terminate**](/windows/previous-versions/ResApi/nc-resapi-pterminate_routine?branch=master) entry point function.

2.  When all of the resources are offline, the Cluster service attempts to transfer the group to the node that is listed next on the group's list of preferred host nodes.
3.  If the Cluster service successfully moves the group to another node, it attempts to bring all of the group's resources online, this time starting at the bottom of the dependency hierarchy. Failover is complete when all of the group's resources are online on the new node.

The Cluster service continues attempting to fail over a group until it succeeds or until a specified number of attempts have been made within a specified time span. A group's [**FailoverThreshold**](groups-failoverthreshold.md) and [**FailoverPeriod**](groups-failoverperiod.md) properties specify a maximum number of failover attempts that can occur in an interval of time. If the Cluster service exceeds this limit, it concludes that the group cannot be brought online anywhere in the [*cluster*](c-gly.md#-wolf-cluster-gly) and stops trying to fail over the group.

## Ways to control failover policy

-   Define how the [*failover cluster*](f-gly.md#mscs-failover-cluster-gly) detects and responds to the failure of individual resources in the group. For information, see [Resource Failure](resource-failure.md).
-   Control the order in which the Cluster service takes resources offline by establishing dependency relationships between resources. For information, see [Resource Dependencies](resource-dependencies.md).
-   When developing [custom resource types](custom-resource-types.md), provide implementations of [**Offline**](/windows/previous-versions/ResApi/nc-resapi-poffline_routine?branch=master) specific to the needs of the resource being supported. **Offline** should shut down the resource quickly and gracefully. For information, see [Implementing Offline](implementing-offline.md).
-   Specify a resource's [**PendingTimeout**](resources-pendingtimeout.md) property to control how long the [Cluster service](cluster-service.md) waits for the resource to shut down gracefully.
-   Maintain an accurate, prioritized list of the nodes that can act as host for the group. Make sure the nodes on the list have the capacity to host the group effectively. For information, see [**SetClusterGroupNodeList**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_node_list?branch=master) and [Enumerating Objects](enumerating-objects.md).
-   Adjust a group's [**FailoverThreshold**](groups-failoverthreshold.md) and [**FailoverPeriod**](groups-failoverperiod.md) properties to control how the group responds to unsuccessful failover. For more information on working with properties, see [Setting Properties](setting-properties.md).

 

 




