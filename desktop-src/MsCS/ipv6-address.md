---
title: IPv6 Address
description: The IPv6 Address resource type is used to manage Internet Protocol version 6 (IPv6) network addresses.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1f91dc67-f3c9-4345-9710-addab2ab1a4d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource types Failover Cluster ,IPv6 Address
- IPv6 Address resource type Failover Cluster
- IPv6 Address resource type Failover Cluster ,resources
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPv6 Address

The IPv6 Address resource type is used to manage Internet Protocol version 6 (IPv6) network addresses. When an IPv6 Address resource is included in a [group](groups.md) with a [Network Name](network-name.md) resource, the group can be accessed by network clients as a [failover cluster instance](virtual-servers.md) (formerly known as a virtual server).

The following table summarizes the characteristics of the IPv6 Address resource type.



| Characteristic                                        | Description                                                                                       |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Required [dependencies](resource-dependencies.md)    | None                                                                                              |
| Required [private properties](private-properties.md) | [**Address**](address.md), [**Network**](network-prop.md), [**PrefixLength**](prefixlength.md) |
| Optional private properties                           | None                                                                                              |



 

## Related topics

<dl> <dt>

[Resource Types](resource-types.md)
</dt> </dl>

 

 




