---
title: N
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7b759f53-68e0-4a4f-ad72-fa8cef8223e7'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
---

# N

[A](a-gly.md) B [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) [F](f-gly.md) [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J K [L](l-gly.md) [M](m-gly.md) N [O](o-gly.md) [P](p-gly.md) [Q](q-gly.md) [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) U [V](v-gly.md) [W](w-gly.md) X Y Z

<dl> <dt>

<span id="_wolf_network_gly"></span><span id="_WOLF_NETWORK_GLY"></span>**network**
</dt> <dd>

A [*cluster object*](c-gly.md#-wolf-cluster-object-gly) that carries internal communication between [*nodes*](#-wolf-node-gly) and/or provides client access to cluster [*resources*](r-gly.md#-wolf-resource-gly).

</dd> <dt>

<span id="_wolf_network_interface_gly"></span><span id="_WOLF_NETWORK_INTERFACE_GLY"></span>**network interface**
</dt> <dd>

See [*network interface card*](#-wolf-network-interface-card-gly).

</dd> <dt>

<span id="_wolf_network_interface_card_gly"></span><span id="_WOLF_NETWORK_INTERFACE_CARD_GLY"></span>**network interface card (NIC)**
</dt> <dd>

A hardware plug-in board that connects a [*node*](#-wolf-node-gly) to a local area network. If the node is a member of a [*failover cluster*](f-gly.md#mscs-failover-cluster-gly), the network interface is a [*cluster object*](c-gly.md#-wolf-cluster-object-gly).

Also called *adapter card*.

</dd> <dt>

<span id="_wolf_network_load_balancing_cluster_gly"></span><span id="_WOLF_NETWORK_LOAD_BALANCING_CLUSTER_GLY"></span>**Network Load Balancing cluster**
</dt> <dd>

One of two types of clusters provided by [*Windows Clustering*](w-gly.md#-wolf-windows-clustering-gly) that distributes and load balances network connections among servers, providing high availability and [*scalability*](s-gly.md#-wolf-scalability-gly) for stateless TCP/IP applications and services.

</dd> <dt>

<span id="_wolf_network_name_resource_gly"></span><span id="_WOLF_NETWORK_NAME_RESOURCE_GLY"></span>**Network Name resource**
</dt> <dd>

An network name being managed as a cluster [*resource*](r-gly.md#-wolf-resource-gly) by the Network Name [*resource type*](r-gly.md#-wolf-resource-type-gly). A Network Name resource must be used with an IP Address resource, a combination referred to as a [*failover cluster instance*](f-gly.md#mscs-failover-cluster-instance-gly).

</dd> <dt>

<span id="_wolf_network_partition_gly"></span><span id="_WOLF_NETWORK_PARTITION_GLY"></span>**network partition**
</dt> <dd>

Situation that occurs when all [*networks*](#-wolf-network-gly) designated to carry internal cluster communication fail and [*nodes*](#-wolf-node-gly) cannot receive [*heartbeat*](h-gly.md#-wolf-heartbeat-gly) signals from each other. Also known as split brain syndrome.

</dd> <dt>

<span id="_wolf_nic_gly"></span><span id="_WOLF_NIC_GLY"></span>**NIC**
</dt> <dd>

See [*network interface card*](#-wolf-network-interface-card-gly).

</dd> <dt>

<span id="_wolf_node_gly"></span><span id="_WOLF_NODE_GLY"></span>**node**
</dt> <dd>

A Microsoft Windows Server system that is an [*active*](a-gly.md#-wolf-active-gly) or [*inactive*](i-gly.md#-wolf-inactive-gly) member of a server [*cluster*](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

<span id="_wolf_node_manager_gly"></span><span id="_WOLF_NODE_MANAGER_GLY"></span>**Node Manager**
</dt> <dd>

Software component in the [*Cluster service*](c-gly.md#-wolf-cluster-service-gly) that maintains all [*node*](#-wolf-node-gly) and [*network*](#-wolf-network-gly) configuration and state information. Also controls operation of the [*cluster network driver*](c-gly.md#-wolf-cluster-network-driver-gly).

</dd> <dt>

<span id="_wolf_node_version_gly"></span><span id="_WOLF_NODE_VERSION_GLY"></span>**node version**
</dt> <dd>

Two version numbers that describe the lowest and highest versions of the Cluster service with which a node is compatible. A node's version is compared with the [*cluster version*](c-gly.md#-wolf-cluster-version-gly) before it is allowed to join the cluster. The [**NodeHighestVersion**](nodes-nodehighestversion.md) and [**NodeLowestVersion**](nodes-nodelowestversion.md) properties specify the node version.

</dd> </dl>

 

 




