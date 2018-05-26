---
title: Q
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 76f55bc4-c26c-42b8-aa79-8a9e74fece00
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Q

[A](a-gly.md) B [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) [F](f-gly.md) [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J K [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) U [V](v-gly.md) [W](w-gly.md) X Y Z

<dl> <dt>

<span id="_wolf_quorum_capable_resource_gly"></span><span id="_WOLF_QUORUM_CAPABLE_RESOURCE_GLY"></span>**quorum-capable resource**
</dt> <dd>

A [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly) that is an instance of a [*resource type*](r-gly.md#-wolf-resource-type-gly) implemented to support [*quorum resources*](#-wolf-quorum-resource-gly). By default, only [*Physical Disk resources*](p-gly.md#-wolf-physical-disk-resource-gly) are quorum-capable, but developers can create resource types that support other kinds of storage class resources as quorum-capable resources.

</dd> <dt>

<span id="_wolf_quorum_log_gly"></span><span id="_WOLF_QUORUM_LOG_GLY"></span>**quorum log**
</dt> <dd>

See [*recovery log*](r-gly.md#-wolf-recovery-log-gly).

</dd> <dt>

<span id="_wolf_quorum_resource_gly"></span><span id="_WOLF_QUORUM_RESOURCE_GLY"></span>**quorum resource**
</dt> <dd>

The [*quorum-capable resource*](#-wolf-quorum-capable-resource-gly) selected to maintain essential cluster data. The quorum resource stores a synchronized version of the [*cluster database*](c-gly.md#-wolf-cluster-database-gly) as well as critical recovery information in a [*recovery log*](r-gly.md#-wolf-recovery-log-gly). The quorum resource guarantees that all [*nodes*](n-gly.md#-wolf-node-gly) have access to the most recent database changes.

</dd> </dl>

 

 




