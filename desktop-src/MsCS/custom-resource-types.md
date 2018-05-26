---
title: Custom Resource Types
description: You may develop or encounter resources that require, or at least benefit from, specialized management routines not provided by any existing resource types. For those kinds of resources, you should create a custom resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 60e21949-fbcd-488f-a620-18eb77bf4276
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- custom resource types Failover Cluster
- resource types Failover Cluster ,custom
- application types Failover Cluster ,custom resource types
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Custom Resource Types

You may develop or encounter [resources](resources.md) that require, or at least benefit from, specialized management routines not provided by any existing [resource types](resource-types.md). For those kinds of resources, you should create a custom resource type.

You can create a custom resource type to:

-   Support a new type of resource. For example, you could use a new type of storage device as the [quorum resource](quorum-resource.md) by creating a custom resource type for the device. A new resource type can also be created to manage one or more [cluster-aware applications](cluster-aware-applications.md).
-   Augment or replace one of the predefined resource types to add functionality. For example, you might have a set of [cluster-unaware](cluster-unaware-applications.md), mission-critical legacy applications that need more careful management than the [Generic Application](generic-application.md) resource type can provide. You could create a Generic Application resource type wrapper to specifically handle the applications.

A custom resource type provides the following benefits:

-   It ensures that the resource has everything it needs before bringing the resource online.
-   It adjusts how the [Cluster service](cluster-service.md) checks the status and detects the failure of your resource.
-   It supports private [properties](private-properties.md) and other parameters specific to the resource.
-   It implements graceful shutdown routines, allowing the resource to perform cleanup tasks before termination.
-   It enables event and error logging for the resource.
-   It maintains awareness of cluster events. For example, the [Cluster service](cluster-service.md) will notify a [resource DLL](resource-dlls.md) if the Cluster service version has changed due to an upgrade or uninstall, but only a custom resource type designed to detect this notification can respond appropriately.

Together, the benefits of a custom resource type result in [highly available](high-availability.md) cluster resources.

For information on how to generate, customize, and register a resource type, see [Creating Resource Types](creating-resource-types.md).

 

 




