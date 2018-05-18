---
title: Cluster Name
description: The Cluster Name resource type is used to provide an alternate computer name for an entity that exists on a network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7b5b9d3f-98ab-419b-936e-26e9e5fc022d'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource types Failover Cluster ,Cluster Name", "Cluster Name resource type Failover Cluster", "Cluster Name resource type Failover Cluster ,resources", "resource types Failover Cluster ,Network Name", "Network Name resource type Failover Cluster", "Network Name resource type Failover Cluster ,resources"]
---

# Cluster Name

The Cluster Name [resource type](resource-types.md) is used to provide an alternate computer name for an entity that exists on a [network](networks.md). When included in a [group](groups.md) with an [IP Address](ip-address.md) [resource](resources.md), a Cluster Name resource provides an identity to the group, allowing the group to be accessed by network clients as a [failover cluster instance](virtual-servers.md).

The following table summarizes the characteristics of the Cluster Name resource type.



| Characteristic                                        | Description                           |
|-------------------------------------------------------|---------------------------------------|
| Required [dependencies](resource-dependencies.md)    | [IP Address](ip-address.md) resource |
| Required [private properties](private-properties.md) | [**Name**](network-names-name.md)    |
| Optional private properties                           | None                                  |



 

A Cluster Name resource type has two [**Name**](network-names-name.md) properties.



| Property                                                | Store                                                         |
|---------------------------------------------------------|---------------------------------------------------------------|
| [**Name**](network-names-name.md) private property     | The name that is published on the network as a computer name. |
| [**Name**](resources-name.md) common resource property | The name of the resource itself.                              |



 

 

 




