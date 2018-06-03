---
title: Resource Types
description: Cluster resources are categorized by type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d02e4f51-7b86-451a-a51c-ea850ae464d1
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster objects Failover Cluster ,resource types
- resource types Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource Types

Cluster [resources](resources.md) are categorized by type. Failover Clustering defines several types of resources and provides [resource DLLs](resource-dlls.md) to manage these types. Third-party developers are encouraged to create new types to fit the specific needs of their [cluster-aware applications](cluster-aware-applications.md) and services. By creating a new resource type, developers can have more control over how [*failover clusters*](https://www.bing.com/search?q=*failover clusters*) manage their application or service.

The following default resource types are included with all failover clusters.

-   [Cluster Name](network-name.md)
-   [DFS Replicated Folder](dfs-replicated-folder.md)
-   [DHCP Service](dhcp-service.md)
-   [Distributed File System](distributed-file-system.md)
-   [Distributed Network Name](distributed-network-name.md)
-   [Distributed Transaction Coordinator](distributed-transaction-coordinator.md)
-   [File Server](file-server.md)
-   [Generic Application](generic-application.md)
-   [Generic Script](generic-script.md)
-   [Generic Service](generic-service.md)
-   [IP Address](ip-address.md)
-   [IPv6 Address](ipv6-address.md)
-   [IPv6 Tunnel Address](ipv6-tunnel-address.md)
-   [iSNS](isns.md)
-   [Message Queuing](message-queuing.md)
-   [Message Queuing Triggers](message-queuing-triggers.md)
-   [Physical Disk](physical-disk.md)
-   [Print Spooler](print-spooler.md)
-   [Scale Out File Server](scale-out-file-server.md)
-   [Storage Pool](storage-pool.md)
-   [Task Scheduler](task-scheduler.md)
-   [Virtual Machine](virtual-machine.md)
-   [Virtual Machine Configuration](virtual-machine-configuration.md)
-   [Virtual Machine Replication Broker](virtual-machine-replication-broker.md)
-   [WINS Service](wins-service.md)
-   [Cloud Witness](cloud-witness.md)
-   [Health Agent](health-agent.md)
-   [Storage Policies](storage-policies.md)
-   [Storage QoS Policy Manager](storage-qos-policy-manager.md)
-   [Virtual Machine Cluster WMI](virtual-machine-cluster-wmi.md)

**Windows Server 2008 R2 and Windows Server 2008:  **

The following resource types are not supported:

-   [DFS Replicated Folder](dfs-replicated-folder.md)
-   [Distributed File System](distributed-file-system.md)
-   [Distributed Network Name](distributed-network-name.md)
-   [File Server](file-server.md)
-   [iSNS](isns.md)
-   [Message Queuing Triggers](message-queuing-triggers.md)
-   [Scale Out File Server](scale-out-file-server.md)
-   [Storage Pool](storage-pool.md)
-   [Task Scheduler](task-scheduler.md)
-   [Virtual Machine Replication Broker](virtual-machine-replication-broker.md)

For more information on working with resource types, see the following topics.

-   [Resource Type Common Properties](resource-type-common-properties.md)
-   [Resource Type Control Codes](resource-type-control-codes.md)
-   [Cluster Management Functions](cluster-management-functions.md)
-   [Creating Resource Types](creating-resource-types.md)

 

 




