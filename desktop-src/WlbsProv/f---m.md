---
title: F - M
description: A \ 8211;E F \ 8211;M N \ 8211;Z
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '87178ae9-7314-4fca-a5dd-cd24948dcf75'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# F - M

[A–E](https://msdn.microsoft.com/library/aa367183) F–M [N–Z](https://msdn.microsoft.com/library/aa371764)

<dl> <dt>

<span id="mscs.f___m_failover_cluster_gly"></span><span id="MSCS.F___M_FAILOVER_CLUSTER_GLY"></span>**failover cluster**
</dt> <dd>

The type of [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) that the Cluster service implements. Failover clusters are characterized by high availability. The failover cluster is one of two types of clusters provided by Microsoft [*Windows Clustering*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-19-gly).

</dd> <dt>

<span id="mscs.f___m_1_gly"></span><span id="MSCS.F___M_1_GLY"></span>**filtering mode**
</dt> <dd>

Part of a [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) specification that determines how inbound network traffic is distributed among ports.

</dd> <dt>

<span id="mscs.f___m_2_gly"></span><span id="MSCS.F___M_2_GLY"></span>**host**
</dt> <dd>

Another name for a [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly). As used in the Network Load Balancing documentation, a host is a computer that runs an Internet server program or service. A [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) consists of multiple hosts connected over a local area network, which is in turn connected to the Internet.

</dd> <dt>

<span id="mscs.f___m_3_gly"></span><span id="MSCS.F___M_3_GLY"></span>**host priority**
</dt> <dd>

A unique integer that identifies a particular [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) in the [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly). The node with the lowest priority handles all traffic not otherwise handled by the current set of [*port rules*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly).

</dd> <dt>

<span id="mscs.f___m_4_gly"></span><span id="MSCS.F___M_4_GLY"></span>**load**
</dt> <dd>

The amount of work being done by a [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly). In Network Load Balancing, load is measured as a raw number of connections.

</dd> <dt>

<span id="mscs.f___m_5_gly"></span><span id="MSCS.F___M_5_GLY"></span>**load balancing**
</dt> <dd>

A technique for scaling performance by distributing requests across multiple nodes.

</dd> <dt>

<span id="mscs.f___m_6_gly"></span><span id="MSCS.F___M_6_GLY"></span>**local connection**
</dt> <dd>

A situation where the [*provider*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly) client and the provider [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) happen to be the same computer system. This situation has nothing to do with whether an operation is considered a *local operation* or a [*remote operation*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-14-gly).

See also [*remote connection*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-13-gly) and [*remote administration*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-12-gly).

</dd> <dt>

<span id="mscs.f___m_7_gly"></span><span id="MSCS.F___M_7_GLY"></span>**local operation**
</dt> <dd>

Any operation initiated by the Network Load Balancing [*provider*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly) that affects the provider [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly). The word "local" in this context means "local relative to the provider." A node will always respond to a local operation, regardless of its **RemoteControlEnabled** setting.

</dd> <dt>

<span id="mscs.f___m_8_gly"></span><span id="MSCS.F___M_8_GLY"></span>**multiple-host filtering mode**
</dt> <dd>

A [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) setting in which multiple [*nodes*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) handle a portion of the traffic flowing into the [*port range*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-6-gly) defined by the port rule.

</dd> </dl>

 

 




