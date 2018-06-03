---
title: Cluster API
description: The Cluster API, defined in ClusAPI.h and ClusAPI.lib, provides the programming elements necessary to work directly with cluster objects and interact with the Cluster service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 865ac74e-5e37-4a2d-a4a4-b23eb45824ce
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Cluster API Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cluster API

The Cluster API, defined in ClusAPI.h and ClusAPI.lib, provides the programming elements necessary to work directly with [cluster objects](cluster-objects.md) and interact with the [Cluster service](cluster-service.md). These header files are located in the directory where your Windows SDK headers are stored: *%PROGRAMFILES%*\\Microsoft SDKs\\Windows\\*version number*\\Include.

The Cluster API is not available until the Cluster service has started. [Resource DLLs](resource-dlls.md) should take this into account and use the Resource API for operations that might take place in the absence of the Cluster service.

**Note**  When you use the Cluster API to create a new File Share resource, permissions for the Everyone group for that file share are set to full control by default. You can change the default permissions by modifying the [Security Property for File Shares](file-shares-security.md).

The Cluster API is divided into the following subsets:

-   [Cluster Database Access Functions](cluster-database-access-functions.md)
-   [Cluster Object Management Functions](cluster-object-management-functions.md)
-   [Control Code Functions](control-code-functions.md)
-   [Control Codes](control-codes.md)
-   [Data Structures](data-structures.md)

 

 




