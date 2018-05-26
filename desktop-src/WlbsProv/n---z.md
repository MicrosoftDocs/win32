---
title: N - Z
description: A \ 8211;E F \ 8211;M N \ 8211;Z
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6c399a89-dddf-44ef-a743-5d7fe691529c
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# N - Z

[A–E](https://msdn.microsoft.com/library/aa367183) [F–M](https://msdn.microsoft.com/library/aa369591) N–Z

<dl> <dt>

<span id="mscs.n___z_1_gly"></span><span id="MSCS.N___Z_1_GLY"></span>**namespace**
</dt> <dd>

As used by *WMI*, a namespace is a group of classes and instances. This group controls the scope and visibility of the classes and instances it contains. Namespaces are like logical databases.

</dd> <dt>

<span id="mscs.n___z_2_gly"></span><span id="MSCS.N___Z_2_GLY"></span>**network interface card (NIC)**
</dt> <dd>

A hardware plug-in board that connects a *node* to a local area network. Network Load Balancing currently supports FDDI, Ethernet and fast Ethernet adapter cards.

Also called adapter card.

</dd> <dt>

<span id="mscs.n___z_3_gly"></span><span id="MSCS.N___Z_3_GLY"></span>**Network Load Balancing cluster**
</dt> <dd>

One of two types of clusters provided by *Windows Clustering* that distributes and load balances network connections among servers, providing *scalability* for stateless TCP/IP applications and services.

</dd> <dt>

<span id="mscs.n___z_4_gly"></span><span id="MSCS.N___Z_4_GLY"></span>**NIC**
</dt> <dd>

See *network interface card*.

</dd> <dt>

<span id="mscs.n___z_5_gly"></span><span id="MSCS.N___Z_5_GLY"></span>**node**
</dt> <dd>

As used in the Network Load Balancing documentation, a node (also called a [*host*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-2-gly)) is a computer that runs an Internet server program or service. A [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) consists of multiple nodes connected over a local area network, which is in turn connected to the Internet.

</dd> <dt>

<span id="mscs.n___z_6_gly"></span><span id="MSCS.N___Z_6_GLY"></span>**port range**
</dt> <dd>

All of the port numbers within a range specified by a minimum and maximum port number. Every *port rule* includes a port range defining the port numbers affected by the rule.

</dd> <dt>

<span id="mscs.n___z_7_gly"></span><span id="MSCS.N___Z_7_GLY"></span>**port rule**
</dt> <dd>

A setting that determines how Network Load Balancing filters incoming traffic for a range of ports. Administrators configure a port rule by specifying a [*filtering mode*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-1-gly), *protocols*, and a *port range*. A port rule applies the filtering mode to all traffic of the specified protocols flowing into all ports in the specified range. The Network Load Balancing API includes functions to enable and disable port rules.

</dd> <dt>

<span id="mscs.n___z_8_gly"></span><span id="MSCS.N___Z_8_GLY"></span>**protocol**
</dt> <dd>

The kind of network traffic to which a *port rule* applies. Protocol can be set to TCP, UDP, or both.

</dd> <dt>

<span id="mscs.n___z_9_gly"></span><span id="MSCS.N___Z_9_GLY"></span>**provider**
</dt> <dd>

A component that allows *Windows Management Instrumentation* (WMI) to communicate with new kinds of managed objects by extending the WMI class repository. The Network Load Balancing Provider defines classes for querying and configuring *Network Load Balancing clusters*, *nodes*, and *port rules*.

</dd> <dt>

<span id="mscs.n___z_10_gly"></span><span id="MSCS.N___Z_10_GLY"></span>**provider client**
</dt> <dd>

The computer system from which an application connects to a *provider* through *WMI*.

</dd> <dt>

<span id="mscs.n___z_11_gly"></span><span id="MSCS.N___Z_11_GLY"></span>**provider node**
</dt> <dd>

The [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) *node* on which the Network Load Balancing *provider* is running.

</dd> <dt>

<span id="mscs.n___z_12_gly"></span><span id="MSCS.N___Z_12_GLY"></span>**remote administration**
</dt> <dd>

Describes how WMI views the connection between the provider client and the provider node. The connection is always treated as remote even if the provider client and the provider node are the same computer system. Remote administration has nothing to do with whether an operation is considered a [*local operation*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-7-gly) or a *remote operation*.

</dd> <dt>

<span id="mscs.n___z_13_gly"></span><span id="MSCS.N___Z_13_GLY"></span>**remote connection**
</dt> <dd>

A situation where the *provider client* and the provider *node* happen to be different computer systems. Remote connections has nothing to do with whether an operation is considered a [*local operation*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-7-gly) or a *remote operation*.

See also [*local connection*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-6-gly) and *remote administration*.

</dd> <dt>

<span id="mscs.n___z_14_gly"></span><span id="MSCS.N___Z_14_GLY"></span>**remote operation**
</dt> <dd>

Any operation initiated by the Network Load Balancing *provider* that affects a *node* other than the *provider*. The word "remote" in this context means "remote relative to the provider." A node will respond to a remote operation only if its **RemoteControlEnabled** setting is **TRUE**.

</dd> <dt>

<span id="mscs.n___z_15_gly"></span><span id="MSCS.N___Z_15_GLY"></span>**routed connection**
</dt> <dd>

A WMI connection in which the *namespace* resolves to the cluster IP address and is routed to a provider node according to the Network Load Balancing *port rules* currently in effect.

</dd> <dt>

<span id="mscs.n___z_16_gly"></span><span id="MSCS.N___Z_16_GLY"></span>**scalability**
</dt> <dd>

A measure of how well a computer system can grow to meet increasing demands.

</dd> <dt>

<span id="mscs.n___z_17_gly"></span><span id="MSCS.N___Z_17_GLY"></span>**server cluster**
</dt> <dd>

See [*failover cluster*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-failover-cluster-gly).

</dd> <dt>

<span id="mscs.n___z_18_gly"></span><span id="MSCS.N___Z_18_GLY"></span>**single-host filtering mode**
</dt> <dd>

A *port rule* setting in which all traffic flowing into the *port range* defined by the port rule is handled by a single *node*.

</dd> <dt>

<span id="mscs.n___z_vip_gly"></span><span id="MSCS.N___Z_VIP_GLY"></span>**VIP**
</dt> <dd>

See [*cluster IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly).

</dd> <dt>

<span id="mscs.n___z_19_gly"></span><span id="MSCS.N___Z_19_GLY"></span>**Windows Clustering**
</dt> <dd>

A feature that supports two different types of clusters: the [*failover cluster*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-failover-cluster-gly) and the *network load balancing cluster*.

</dd> <dt>

<span id="mscs.n___z_20_gly"></span><span id="MSCS.N___Z_20_GLY"></span>**Windows Management Instrumentation (WMI)**
</dt> <dd>

A unified architecture for describing, accessing, and instrumenting objects. Part of this architecture is a large repository of [*CIM classes*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-3-gly) that WMI can use to carry out management tasks on specific objects.

</dd> <dt>

<span id="mscs.n___z_21_gly"></span><span id="MSCS.N___Z_21_GLY"></span>**WMI**
</dt> <dd>

See *Windows Management Instrumentation*.

</dd> <dt>

<span id="mscs.n___z_22_gly"></span><span id="MSCS.N___Z_22_GLY"></span>**WMI class**
</dt> <dd>

A template for a type of managed object. WMI classes are based on the [*Common Information Model (CIM)*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-7-gly), as implemented in *Windows Management Instrumentation* (WMI).

</dd> </dl>

 

 




