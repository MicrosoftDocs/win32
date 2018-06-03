---
title: Cluster-Aware Applications
description: Definition of a cluster-aware application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2c72d084-e2bf-4582-b097-70c5f92b1cd6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster-aware applications Failover Cluster
- application types Failover Cluster ,cluster-aware applications
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cluster-Aware Applications

An application is capable of being cluster-aware if it has the following characteristics:

-   It uses TCP/IP as a network protocol.
-   It maintains data in a configurable location.
-   It supports transaction processing.

Most database applications, transaction processing applications, file and print server applications, and other groupware applications are capable of being made cluster-aware.

There are two types of cluster-aware applications:

-   Applications that are managed as [highly available](high-availability.md) cluster [resources](resources.md) by a [custom resource type](custom-resource-types.md). If you want your application to be highly available, to [fail over](failover.md), to benefit from customized failure detection policies, or to be made available to clients on a [failover cluster instance](virtual-servers.md), your application needs to be managed as a cluster resource. This means that in addition to any cluster-awareness you want to add to the application, you will need to create a custom resource type to manage the application. For more information, see [Creating Resource Types](creating-resource-types.md)
-   Applications that interact with the [*cluster*](https://www.bing.com/search?q=*cluster*) but are not cluster resources. [Cluster Administrator](cluster-administrator.md) is an example of such an application. This category also includes cluster-aware performance monitors, configuration tools, setup applications, event handlers, and cluster management applications.

To create a cluster-aware application, review the following tasks and determine what kinds of interactions your application needs to implement:

-   [Receiving cluster events](receiving-cluster-events.md)
-   [Getting cluster information](getting-information-from-the-cluster.md)
-   [Changing the cluster configuration](changing-the-cluster-configuration.md)

The following table presents examples of different kinds of cluster-aware applications and the event, information, and configuration tasks you may want to implement for such applications.



| Cluster-aware application                         | Event tasks                                                      | Information tasks                                                                                                                                                                                                 | Configuration tasks                                                                                                                                                                                                 |
|---------------------------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A cluster-aware setup application.                | None.                                                            | Detect the cluster version, list the [nodes](nodes.md) in the cluster, and list the available disks.                                                                                                             | Create and configure a test group.                                                                                                                                                                                  |
| A remote failover monitor and performance tracker | Any events involving group or resource state changes or movement | List the nodes in the cluster, the [groups](groups.md) on each node, and the [resources](resources.md) in each group. Retrieve group and resource properties, especially those relating to times and intervals. | None (a read-only interface).                                                                                                                                                                                       |
| A resource configuration wizard                   | None.                                                            | Be able to provide feedback and verification on the changes the user is making.                                                                                                                                   | Back up the [cluster database](cluster-database.md), create a group, create resources, change properties, create dependencies, change owner node lists, create registry and crypto checkpoints, and change states. |



 

 

 




