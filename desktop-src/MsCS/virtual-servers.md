---
title: Failover Cluster Instances
description: To access a network application or resource in a non-clustered environment, network clients must connect to a physical server (that is, a specific computer on the network identified by a unique network name and IP address).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 05994583-4847-4557-92e5-e748e2680b74
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster objects Failover Cluster ,groups,virtual servers
- cluster objects Failover Cluster ,groups,failover cluster instances
- virtual servers Failover Cluster
- failover cluster instances Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Failover Cluster Instances

To access a network application or [resource](resources.md) in a non-clustered environment, network clients must connect to a physical server (that is, a specific computer on the network identified by a unique network name and IP address). If that server fails, access to the application or resource is impossible.

[*Failover clusters*](https://www.bing.com/search?q=*Failover clusters*), however, allow the creation of failover cluster instances. A failover cluster instance is a [group](groups.md) that contains:

-   A [Network Name](network-name.md) resource.
-   An [IP Address](ip-address.md) resource, an [IPv6 Address](ipv6-address.md) resource, and/or an [IPv6 Tunnel Address](ipv6-tunnel-address.md) resource.
-   The resources to be accessed by the clients of the failover cluster instance. Each resource on a failover cluster instance must establish a dependency on the failover cluster instance's [Network Name](network-name.md) resource type.

A failover cluster instance acts like a physical server in the following ways:

-   It allows access to network resources.
-   It is published to network clients under a unique server name.
-   It is associated with a network name and an IP address.

However, a failover cluster instance is not associated with a specific computer and can be [*failedover*](https://www.bing.com/search?q=*failedover*) like any other group. If the [node](nodes.md) hosting the failover cluster instance fails, clients can still access the failover cluster instance's resources using the same server name.

For procedures and an example of creating a failover cluster instance, see [Creating a Failover Cluster Instance](creating-virtual-servers.md).

 

 




