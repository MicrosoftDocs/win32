---
title: Network Load Balancing Clusters
description: This section presents a brief overview of Network Load Balancing concepts.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd988aae0-e4c8-4126-b301-09d52cb24457'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["network load balancing clusters Failover Cluster", "clusters Failover Cluster ,network load balancing clusters"]
---

# Network Load Balancing Clusters

This section presents a brief overview of Network Load Balancing concepts.

Network Load Balancing enables all [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) [*nodes*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) on a single subnet to concurrently detect incoming network traffic for one or more [*IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly).

## The Network Load Balancing Driver

On each cluster [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly), a Network Load Balancing driver acts as a filter between the network driver and the higher layers of the TCP/IP stack to allow a portion of the incoming network traffic to be received by the node. How the traffic is filtered depends on the current set of traffic handling rules.

## Host Priority

Every node (also called host) in the cluster must be assigned a [*host priority*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-3-gly), a unique integer that identifies the node and determines the order in which traffic is handled by default. The node with the lowest priority handles all traffic not otherwise handled by the current set of rules.

## Convergence

The cluster nodes exchange periodic messages and, in the event of a node failure, participate in a process called [*convergence*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-8-gly).

## Port Rules

[*Port rules*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) determine how incoming connections are distributed among nodes. A port rule consists of the following parameters:

-   A [*range of port numbers*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-6-gly) to which the port rule applies.
-   The [*protocols*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-8-gly) (TCP, UDP, or both) to which the port rule applies.
-   The [*filtering mode*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-1-gly) for the port rule. The filtering mode determines how traffic is handled by the port rule and can be set to one of the following values.



| Filtering mode                          | Description                                                                                                                                                                                                                                       |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Single-host filtering mode<br/>   | One node (the node with the highest handling priority) handles all traffic. This mode [*load balances*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-5-gly) multiple, single-host applications.<br/>                                              |
| Multiple-host filtering mode<br/> | Traffic is distributed across all cluster nodes according to the load percentage set for each node. This mode load balances a single, cluster-wide application.<br/>                                                                        |
| Disabled<br/>                     | No traffic is accepted by the ports in the [*port range*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-6-gly). When all of a node's ports are disabled, the node is said to be [*draining*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-11-gly).<br/> |



 

A port rule applies the filtering mode to all traffic of the specified protocol flowing into all ports in the specified range.

 

 





