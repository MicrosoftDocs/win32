---
title: Display Names
description: It is important to distinguish between the display name of a resource type and the registered name of a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '02c61e81-486c-4543-b345-a1b2dde41982'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["display names Failover Cluster", "resource types Failover Cluster ,display names"]
---

# Display Names

It is important to distinguish between the display name of a [resource type](resource-types.md) and the registered name of a resource type.

-   The display name of a resource type is the name that appears in the [Cluster Administrator](cluster-administrator.md) user interface. The display name can be changed through the [**Name**](resource-types-name.md) property for resource types.
-   The registered name of a resource type is part of the resource type's internal definition as registered with the [Cluster service](cluster-service.md) when the resource type is first created (for more information, see [Registering Resource Types](registering-resource-types.md)). The names of predefined resource types ( [IP Address](ip-address.md), [Physical Disk](physical-disk.md), [Generic Application](generic-application.md), and so on) are examples of registered resource type names. The registered name of a resource type can be changed only by unregistering the resource type and registering it under a new name.

 

 




