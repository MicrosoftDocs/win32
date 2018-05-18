---
title: Resource API
description: The Resource API defines interfaces that allow the Cluster service to manage resources through a Resource Monitor and a resource DLL.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '764a35dd-a681-4af0-8e2c-281a254a3a30'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Resource API Failover Cluster"]
---

# Resource API

The Resource API defines interfaces that allow the [Cluster service](cluster-service.md) to manage [resources](resources.md) through a [Resource Monitor](resource-monitor.md) and a [resource DLL](resource-dlls.md). The Cluster service initiates requests with a Resource Monitor, and the Resource Monitor passes the requests to the resource. Status and event information are passed back from the [resource DLL](resource-dlls.md) to the Cluster service.

Unlike the [Cluster API](cluster-api.md), the Resource API is always available. Resource DLLs should use the Resource API whenever possible to isolate themselves from Cluster service failures.

The Resource API includes definitions for the following:

-   [Resource DLL Functions](resource-dll-entry-point-functions.md)
-   [Cluster Utility Functions](cluster-utility-functions.md)
-   [Resource DLL Structures](resource-dll-structures.md)

 

 




