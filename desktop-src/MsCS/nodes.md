---
title: Nodes
description: A cluster node is a Microsoft Windows Server system that has a working installation of the Cluster service. By definition, a node is always considered to be a member of a cluster; a node that ceases to be a member of a cluster ceases to be a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4381e378-7bf2-4dbc-b56e-3fed33193d32
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster objects Failover Cluster ,nodes
- nodes Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Nodes

A cluster node is a Microsoft Windows Server system that has a working installation of the [Cluster service](cluster-service.md). By definition, a node is always considered to be a member of a [*cluster*](https://www.bing.com/search?q=*cluster*); a node that ceases to be a member of a cluster ceases to be a node.

A node's participation in cluster operations is described by the following terms.



| Term        | Meaning                                                                                  |
|-------------|------------------------------------------------------------------------------------------|
| not running | The node is turned off or not operational.                                               |
| running     | The node is physically plugged in, turned on, booted, and capable of executing programs. |
| inactive    | The node is running but not participating in cluster operations.                         |
| active      | The node is running and participating in cluster operations.                             |



 

An active node can act as host to cluster [groups](groups.md).

When the Cluster service is installed, the administrator must choose whether the node should form its own cluster or join an existing cluster. After installation is complete, the node always attempts to join an existing cluster whenever it is restarted. A node locates an existing cluster by searching for active nodes along the [networks](networks.md) designated for internal communication.

When a node attempts to join an existing cluster, the cluster validates the node's name and verifies [version compatibility](version-compatibility.md). If the validation process succeeds, the cluster allows the node to join. The node updates its copy of the [cluster database](cluster-database.md) from the cluster database on the other active nodes.

If a node cannot join an existing cluster because it cannot locate another active node, it attempts to form its own cluster by gaining access to the [quorum resource](quorum-resource.md). If access is granted, the node uses the recovery logs to update its cluster database and becomes active as a new cluster.

### Claims Based Access Control

**Windows Server 2008 R2 and Windows Server 2008:** This feature is not supported.

All nodes within the same cluster must have the identical support setting for Claims Based Access Control (CBAC). This setting is usually accessed through group policy by traversing the policy tree nodes **Administrative Templates**, **System**, and **Kerberos**, and then changing the **Kerberos client support for claims, compound authentication and Kerberos armoring** item to the appropriate configuration value.

Alternatively, you can change this setting manually within the registry key by accessing the following registry key name on the client:

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**Lsa**\\**Kerberos**\\**Parameters**

Within that registry key, add a registry value named **EnableCbacAndArmor** with type **REG\_DWORD**. To enable CBAC, set this registry value name to a value of 1. To disable CBAC, set the value of 0. If **EnableCbacAndArmor** is missing, CBAC is disabled by default.

For more information on working with nodes, see the following topics:

-   [Node Common Properties](node-common-properties.md)
-   [Node Control Codes](node-control-codes.md)
-   [Node Management Functions](node-management-functions.md)

 

 




