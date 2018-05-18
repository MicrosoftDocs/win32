---
title: IPv6 Tunnel Address
description: The IPv6 Tunnel Address resource type is used to manage Internet Protocol version 6 (IPv6) network tunnel addresses.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e59df4d3-d30b-4d23-853f-d71644c932f7'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource types Failover Cluster ,IPv6 Tunnel Address", "IPv6 Tunnel Address resource type Failover Cluster", "IPv6 Tunnel Address resource type Failover Cluster ,resources"]
---

# IPv6 Tunnel Address

The IPv6 Tunnel Address resource type is used to manage Internet Protocol version 6 (IPv6) network tunnel addresses. When an IPv6 Tunnel Address resource is included in a [group](groups.md) with a [Network Name](network-name.md) resource, the group can be accessed by network clients as a [failover cluster instance](virtual-servers.md) (formerly known as a virtual server).

The following table summarizes the characteristics of the IPv6 Tunnel Address resource type.



| Characteristic                                        | Description                           |
|-------------------------------------------------------|---------------------------------------|
| Required [dependencies](resource-dependencies.md)    | [IP Address](ip-address.md) resource |
| Required [private properties](private-properties.md) | [**TunnelType**](tunneltype.md)      |
| Optional private properties                           | None                                  |



 

## Related topics

<dl> <dt>

[Resource Types](resource-types.md)
</dt> </dl>

 

 




