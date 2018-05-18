---
title: Detecting Resource Failure
description: The cluster monitors the environment for node, network, and Cluster service failures. Your resource DLL must implement a failure detection system that detects and responds to potential problems in the resources it supports.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7306abab-cd5b-4c13-95a3-8b34d3029463'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resources Failover Cluster ,failure,detecting", "resource failure Failover Cluster ,detecting"]
---

# Detecting Resource Failure

The [*cluster*](c-gly.md#-wolf-cluster-gly) monitors the environment for [node](nodes.md), [network](networks.md), and [Cluster service](cluster-service.md) failures. Your [resource DLL](resource-dlls.md) must implement a failure detection system that detects and responds to potential problems in the resources it supports.

A good failure detection system detects potential problems as they occur, accurately assesses their severity, and responds in a way that maximizes availability.

For information on the various aspects of detecting resource failure, see the following topics:

-   [Implementing Asynchronous Failure Detection](implementing-asynchronous-failure-detection.md)
-   [Implementing LooksAlive](implementing-looksalive.md)
-   [Implementing IsAlive](implementing-isalive.md)

 

 




