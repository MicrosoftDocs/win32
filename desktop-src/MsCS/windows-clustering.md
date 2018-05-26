---
title: Windows Clustering
description: With network load balancing clusters, filter and distribute TCP/IP traffic across a range of nodes, regulate connection load according to administrator-defined port rules. With failover clusters, maintain consistent cluster images on all nodes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 47247d48-d401-41dc-9aae-128840eb6d3a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Windows Clustering Failover Cluster
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Windows Clustering

A cluster is a group of independent computer systems, referred to as nodes, working together as a unified computing resource. A cluster provides a single name for clients to use and a single administrative interface, and it guarantees that data is consistent across nodes.

Windows Clustering encompasses two different clustering technologies. These technologies implement the following two types of clusters.

-   A *network load balancing cluster* filters and distributes TCP/IP traffic across a range of nodes, regulating connection load according to administrator-defined port rules.
-   A [*failover cluster*](f-gly.md#mscs-failover-cluster-gly) provides high availability for services, applications, and other resources through an architecture that maintains a consistent image of the cluster on all nodes and that allows nodes to transfer resource ownership on demand.

The following are the programming interfaces for the Windows Clustering technologies:

-   The [Network Load Balancing Provider](https://msdn.microsoft.com/library/cc296105) allows developers to create remote administration and configuration tools as well as customized user interfaces for Network Load Balancing clusters.
-   The [Failover Cluster APIs](failover-cluster-apis-portal.md) allow developers to create cluster-aware applications, implement high availability for new types of resources, and create remote administration and configuration tools.

 

 




