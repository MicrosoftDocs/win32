---
title: WINS Service
description: The WINS Service resource type supports the Windows Internet Name Service (WINS) as a cluster resource. There can be only one instance of a resource of this type in the cluster; in other words, a cluster can support only one WINS Service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 78c620be-f198-481e-bd0e-50c57f0ff0a8
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource types Failover Cluster ,WINS Service
- WINS Service resource type Failover Cluster
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WINS Service

The WINS Service [resource type](resource-types.md) supports the Windows Internet Name Service (WINS) as a [*cluster*](c-gly.md#-wolf-cluster-gly) [resource](resources.md). There can be only one instance of a [resource](resources.md) of this type in the *cluster*; in other words, a cluster can support only one WINS Service.

The following table summarizes the characteristics of the WINS resource type.



| Characteristic                                        | Description                                                                                                        |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Required [dependencies](resource-dependencies.md)    | Storage class resource, such as a [Physical Disk](physical-disk.md), and an [IP Address](ip-address.md) resource |
| Required [private properties](private-properties.md) | [**DatabasePath**](the-wins-service-databasepath.md), [**BackupPath**](the-wins-service-backuppath.md)           |
| Optional private properties                           | None                                                                                                               |



 

 

 




