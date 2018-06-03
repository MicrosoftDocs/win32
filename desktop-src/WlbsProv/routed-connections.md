---
title: Routed Connections
description: In a routed connection, you specify an object path that resolves to the cluster IP address and the WMI connection is routed to one of the cluster nodes based on the Network Load Balancing port rules.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9243ec03-3fe6-49f9-b1e2-3eff7cf6d406
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- connections Failover Cluster ,routed NLB connections
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Routed Connections

In a routed connection, you specify an object path that resolves to the [*cluster IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly) and the [*WMI*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-21-gly) connection is routed to one of the cluster [*nodes*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) based on the Network Load Balancing [*port rules*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly). There are disadvantages associated with routed connections:

-   If cluster activity has been stopped on all nodes, the connection will fail.
-   You have no control over which node will be selected as the [*provider node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-11-gly).
-   If you change the cluster IP address of the provider node, you will lose your connection.
-   If nodes are added or removed from the cluster, you might lose your connection.

The recommended way to establish a connection to WMI is to use a [direct connection](direct-connections.md).

Cluster object paths have the form:

**\\\\***name***\\root\\MicrosoftNLB**

where *name* can be any URL, name, or IP address that resolves to the cluster IP address.

 

 




