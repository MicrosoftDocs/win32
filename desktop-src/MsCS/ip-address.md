---
title: IP Address
description: The IP Address resource type is used to manage Internet Protocol (IP) network addresses.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3ed966f1-0177-4376-a36d-4a2fda327470
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource types Failover Cluster ,IP Address
- IP Address resource type Failover Cluster
- IP Address resource type Failover Cluster ,resources
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IP Address

The IP Address resource type is used to manage Internet Protocol (IP) network addresses. When an IP Address resource is included in a [group](groups.md) with a [Network Name](network-name.md) resource, the group can be accessed by network clients as a [failover cluster instance](virtual-servers.md) (formerly known as a virtual server).

The following table summarizes the characteristics of the IP Address resource type.



| Characteristic                                        | Description                                                                                                                     |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Required [dependencies](resource-dependencies.md)    | None                                                                                                                            |
| Required [private properties](private-properties.md) | [**Address**](ip-addresses-address.md), [**Network**](ip-addresses-network.md), [**SubnetMask**](ip-addresses-subnetmask.md) |
| Optional private properties                           | [**EnableNetBIOS**](ip-addresses-enablenetbios.md)                                                                             |



 

 

 




