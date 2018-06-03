---
title: Cluster Management Applications
description: A cluster management application is a type of cluster-aware application designed to provide a user interface for monitoring or controlling at least one aspect of a failover cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 16da4eaf-186e-4bc8-afa3-cc20af6105d5
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster management applications Failover Cluster
- application types Failover Cluster ,cluster management applications
- clusters Failover Cluster , management applications
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cluster Management Applications

A cluster management application is a type of [cluster-aware application](cluster-aware-applications.md) designed to provide a user interface for monitoring or controlling at least one aspect of a [*failover cluster*](https://www.bing.com/search?q=*failover cluster*). This covers a wide range of functionality, from single-purpose monitoring tools that simply display status information about one or more [cluster objects](cluster-objects.md), to full-featured administration interfaces such as failover cluster cmdlets.

**Windows Server 2008:** The [Cluster.exe](cluster-exe.md) command is available as a full-featured administration interface.

To create a cluster management application:

-   Choose the [*Failover Cluster API*](https://www.bing.com/search?q=*Failover Cluster API*) as the basis for your application.

    **Windows Server 2008:** The [Cluster Automation Server](https://msdn.microsoft.com/library/aa372940) can alternatively be used as the basis for your application. The Cluster Automation Server does not provide access to cluster events (see [Receiving Cluster Events](receiving-cluster-events.md)).

-   Decide what aspects of the [*cluster*](https://www.bing.com/search?q=*cluster*) you want to expose to users. For example, you might want to create a "read-only" interface that only allows users to monitor information about the cluster.
-   Review the following tasks and determine what kinds of interactions your application needs to implement:

    -   [Receiving cluster events](receiving-cluster-events.md)
    -   [Getting cluster information](getting-information-from-the-cluster.md)
    -   [Changing the cluster configuration](changing-the-cluster-configuration.md)

 

 




