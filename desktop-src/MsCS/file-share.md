---
title: File Share
description: Used to manage file shares that applications and clients can access using a network path.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 414c5f97-0a3a-4e01-8ab7-340f547ba101
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resource types Failover Cluster ,File Share
- File Share resource type Failover Cluster
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# File Share

\[The File Share [resource type](resource-types.md) property is available for use in Windows Server 2003. It may be altered or unavailable in subsequent versions.\]

The File Share [resource type](resource-types.md) is used to manage file shares that applications and clients can access using a network path. The File Share resource type supports the Microsoft Distributed File System (DFS).The following table summarizes the characteristics of the File Share resource type.



| Characteristic                                        | Description                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required [dependencies](resource-dependencies.md)    | None                                                                                                                                                                                                                                                                                                                                                                                       |
| Required [private properties](private-properties.md) | [**Path**](file-shares-path.md), [**ShareName**](file-shares-sharename.md)                                                                                                                                                                                                                                                                                                               |
| Optional private properties                           | [**CSCCache**](file-shares-csccache.md), [**HideSubDirShares**](file-shares-hidesubdirshares.md), [**IsDfsRoot**](file-shares-isdfsroot.md), [**MaxUsers**](file-shares-maxusers.md), [**Remark**](file-shares-remark.md), [**ShareSubDirs**](file-shares-sharesubdirs.md), [**Security**](file-shares-security.md), [**Security Descriptor**](file-shares-security-descriptor.md) |



 

**Note**  When you use Cluster Administrator to create a new File Share resource, permissions for the "Everyone" group for that file share are set to read-only by default. However, if you use cluster.exe or the Cluster API to create the File Share resource, permissions for the "Everyone" group for that file share are set to full control by default. You can change the default permissions by modifying the [Security Property for File Shares](file-shares-security.md).

 

 




