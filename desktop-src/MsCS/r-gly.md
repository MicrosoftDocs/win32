---
title: R
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5c96839e-672a-4739-94d8-0142b3797166
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# R

[A](a-gly.md) B [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) [F](f-gly.md) [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J K [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) [Q](q-gly.md) R [S](s-gly.md) [T](t-gly.md) U [V](v-gly.md) [W](w-gly.md) X Y Z

<dl> <dt>

<span id="_wolf_recovery_log_gly"></span><span id="_WOLF_RECOVERY_LOG_GLY"></span>**recovery log**
</dt> <dd>

A file that maintains a history of all of the transactions affecting the [*cluster database*](c-gly.md#-wolf-cluster-database-gly) on all [*nodes*](n-gly.md#-wolf-node-gly). The recovery log is stored on the cluster's [*quorum resource*](q-gly.md#-wolf-quorum-resource-gly) and is also referred to as the quorum log.

</dd> <dt>

<span id="_wolf_resource_gly"></span><span id="_WOLF_RESOURCE_GLY"></span>**resource**
</dt> <dd>

A physical or logical entity that is capable of being owned by a [*node*](n-gly.md#-wolf-node-gly), brought [*online*](o-gly.md#-wolf-online-gly) and taken [*offline*](o-gly.md#-wolf-offline-gly), moved between nodes, and managed as a [*cluster object*](c-gly.md#-wolf-cluster-object-gly). A resource can be owned by only a single node at any point in time. A resource is an instance of a [*resource type*](#-wolf-resource-type-gly).

</dd> <dt>

<span id="_wolf_resource_api_gly"></span><span id="_WOLF_RESOURCE_API_GLY"></span>**Resource API**
</dt> <dd>

Subset of [*Failover Cluster API*](f-gly.md#mscs-failover-cluster-api-gly) functions that allow a [*resource DLL*](#-wolf-resource-dll-gly) to communicate with a [*Resource Monitor*](#-wolf-resource-monitor-gly). Some of the functions are implemented by a resource DLL and others are implemented by the Resource Monitor.

</dd> <dt>

<span id="_wolf_resource_class_gly"></span><span id="_WOLF_RESOURCE_CLASS_GLY"></span>**resource class**
</dt> <dd>

Numeric value that is used to identify failover cluster [*resources*](#-wolf-resource-gly) of similar capability, such as resources that can act as storage devices.

</dd> <dt>

<span id="_wolf_resource_dll_gly"></span><span id="_WOLF_RESOURCE_DLL_GLY"></span>**resource DLL**
</dt> <dd>

Dynamic-link library containing an implementation of the [*Resource API*](#-wolf-resource-api-gly) for a specific type of [*resource*](#-wolf-resource-gly). The resource DLL is loaded into the address space of its [*Resource Monitor*](#-wolf-resource-monitor-gly).

</dd> <dt>

<span id="_wolf_resource_manager_gly"></span><span id="_WOLF_RESOURCE_MANAGER_GLY"></span>**Resource Manager**
</dt> <dd>

Software component in the [*Cluster service*](c-gly.md#-wolf-cluster-service-gly) that works with the [*Failover Manager*](f-gly.md#-wolf-failover-manager-gly) to manage [*resources*](#-wolf-resource-gly) and [*groups*](g-gly.md#-wolf-group-gly) and initiate [*failover*](f-gly.md#-wolf-failover-gly) operations.

</dd> <dt>

<span id="_wolf_resource_monitor_gly"></span><span id="_WOLF_RESOURCE_MONITOR_GLY"></span>**Resource Monitor**
</dt> <dd>

Component of the Cluster service that manages communication between a [*node's*](n-gly.md#-wolf-node-gly) [*Cluster service*](c-gly.md#-wolf-cluster-service-gly) and one or more of its [*resources*](#-wolf-resource-gly).

</dd> <dt>

<span id="_wolf_resource_type_gly"></span><span id="_WOLF_RESOURCE_TYPE_GLY"></span>**resource type**
</dt> <dd>

A [*cluster object*](c-gly.md#-wolf-cluster-object-gly) used to categorize and manage [*resources*](#-wolf-resource-gly) sharing similar characteristics. A resource type is implemented in a [*resource DLL*](#-wolf-resource-dll-gly) that manages all the resources of that type in the [*cluster*](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

<span id="_wolf_rolling_upgrade_gly"></span><span id="_WOLF_ROLLING_UPGRADE_GLY"></span>**rolling upgrade**
</dt> <dd>

The process of systematically upgrading each server [*cluster*](c-gly.md#-wolf-cluster-gly) [*node*](n-gly.md#-wolf-node-gly) while the other nodes continue to provide service. Administrators perform rolling upgrades by [*failing over*](f-gly.md#-wolf-failover-gly) all [*groups*](g-gly.md#-wolf-group-gly) on a node, taking the node [*offline*](o-gly.md#-wolf-offline-gly), upgrading the node, bringing it back [*online*](o-gly.md#-wolf-online-gly), [*failing back*](f-gly.md#-wolf-failback-gly) the groups to the node, and continuing to the next node.

</dd> </dl>

 

 




