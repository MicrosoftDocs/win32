---
title: Cluster-Unaware Applications
description: Definition of a cluster-unaware application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4b7e9322-a1cc-4c2d-868d-816dbf4ba666
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster-unaware applications Failover Cluster
- application types Failover Cluster ,cluster-unaware applications
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Cluster-Unaware Applications

A cluster-unaware application is distinguished by the following features.

-   The application does not use the [Failover Cluster API](the-server-cluster-api.md). Therefore, it cannot discover information about the cluster environment, interact with [cluster objects](cluster-objects.md), detect that it is running in a [*cluster*](c-gly.md#-wolf-cluster-gly), or change its behavior between clustered and non-clustered systems.
-   If the application is managed as a cluster [resource](resources.md), it is managed as a [Generic Application](generic-application.md) resource type or [Generic Service](generic-service.md) resource type. These [resource types](resource-types.md) provide very basic routines for failure detection and application shutdown. Therefore, a cluster-unaware application might not be able to perform the initialization and cleanup tasks needed for it to be consistently available in the cluster.

Most older applications are cluster-unaware. However, a cluster-unaware application can be made [cluster-aware](cluster-aware-applications.md) by [creating resource types](creating-resource-types.md) to manage the application. A custom resource type provides the initialization, cleanup, and management routines specific to the needs of the application.

There is nothing inherently wrong with cluster-unaware applications. As long as they are functioning and highly available to cluster [resources](resources.md) when managed as [Generic Applications](generic-application.md) or [Generic Services](generic-service.md), there is no need to make them cluster-aware. However, if an application does not start, stop, or [*failover*](f-gly.md#-wolf-failover-gly) consistently when managed by the generic types, it should be made cluster-aware.

 

 




