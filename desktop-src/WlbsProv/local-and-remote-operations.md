---
title: Local and Remote Operations
description: The Network Load Balancing cluster software with which the provider interacts categorizes operations as local or remote based on the location of the effect of the operation relative to the origin of the operation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d7da5018-ac97-4fd6-9352-7937004bb854
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- local operations in NLB Failover Cluster
- remote operations in NLB Failover Cluster
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Local and Remote Operations

The [*Network Load Balancing cluster*](https://msdn.microsoft.com/library/aa371764) software with which the [*provider*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly) interacts categorizes operations as local or remote based on the location of the effect of the operation relative to the origin of the operation:

-   If an operation originates from a [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly), and it affects the same node, the operation is local. A node always responds to local operations
-   If an operation originates from one node and it affects another node, the operation is remote. Only nodes on which remote control is enabled respond to remote control operations.

The Network Load Balancing provider conforms to this architecture as follows:

-   If an operation originates from the [*provider node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-11-gly), and it affects the same node, the operation is local. Local operations include enumerating, instantiating, and using the classes representing the provider node and its settings and [*port rules*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly).
-   If an operation originates from the provider node, and it affects a different node, the operation is remote. Remote operations include enumerating, instantiating, and using the classes representing the cluster or any node, setting, or port rule external to the provider node.

Although the Network Load Balancing provider allows remote operations, making use of remote operations in your application is not recommended for the following reasons:

-   Remote operations depend on remote control being enabled, which is a configuration with significant security issues (see the Network Load Balancing online help documentation). By relying on remote control being enabled, remote operations require the user or the application to put network security at risk.
-   Remote operations can produce inconsistent and unreliable results if some nodes have remote control enabled and others do not (see [Enumerating Nodes](enumerating-nodes.md)). To guarantee that operations are applied uniformly across all nodes, use local operations.
-   Remote operations are unnecessary. You can configure an entire cluster safely and reliably through a series of local operations.

> [!Note]  
> To maximize the effectiveness and security of your application, always perform local operations with the Network Load Balancing provider. For more information, see the [Standard Usage Model](standard-usage-model.md) for the Network Load Balancing provider.

 

 

 




