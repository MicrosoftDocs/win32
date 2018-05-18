---
title: Supporting Multiple Resource Types
description: A single resource DLL can support multiple resource types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2f7a5f70-53ec-4ae8-9c51-052ea739d350'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource types Failover Cluster ,supporting multiple types"]
---

# Supporting Multiple Resource Types

A single [resource DLL](resource-dlls.md) can support multiple [resource types](resource-types.md). For example, many of the resource types defined by the [Cluster service](cluster-service.md) are all supported by a single resource DLL. One reason to do this is simply for convenience—it is easier to debug and deploy a single resource DLL than to manage several different DLLs.

Combining multiple resource types into a single resource DLL also allows you to more easily manage shared data or interactions between [resources](resources.md) of different types. This is useful for applications that can be divided into functionally discrete modules, with each module supported as a separate resource type.

For example, a single database application might be supported by a Database Engine resource type, a Transaction Engine resource type, and a Connection Manager resource type. Each type has its own set of [dependencies](resource-dependencies.md), properties, failure detectors, and [failover](failover.md) policies. However, the DLL that implements these types enforces the proper relationships between the modules and provides ways to share data. Thus the DLL might allow any number of Database Engine resources in the [*cluster*](c-gly.md#-wolf-cluster-gly), but only allow one Transaction Engine resource and one Connection Manager resource per cluster.

 

 




