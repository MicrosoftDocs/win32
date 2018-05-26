---
title: Monitoring DFSR
description: The DFSR WMI provider provides classes for monitoring DFSR resources and activity.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 913e0943-c4b8-49f1-b953-797d28bb3af2
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Distributed File System Replication Files , monitoring
- monitoring Distributed File System Replication Files
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Monitoring DFSR

The DFSR WMI provider provides the following classes for monitoring DFSR resources and activity.



| Class                                                        | Description                                                                                                               |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**DfsrConflictInfo**](dfsrconflictinfo.md)                 | Provides information about conflicted files.                                                                              |
| [**DfsrConnectionInfo**](dfsrconnectioninfo.md)             | Represents a connection. An object of this class has the same lifetime as the in-memory connection object in the service. |
| [**DfsrIdRecordInfo**](dfsridrecordinfo.md)                 | Each object of this class represents a resource that may be present on the file system or tombstone.                      |
| [**DfsrInfo**](dfsrinfo.md)                                 | Represents the state of the DFSR service.                                                                                 |
| [**DfsrLocalMemberInfo**](dfsrlocalmemberinfo.md)           | Provides information about a local replication group membership configured on the computer.                               |
| [**DfsrReplicatedFolderInfo**](dfsrreplicatedfolderinfo.md) | Represents information about a replicated folder.                                                                         |
| [**DfsrSyncInfo**](dfsrsyncinfo.md)                         | Represents a synchronization session.                                                                                     |
| [**DfsrVolumeInfo**](dfsrvolumeinfo.md)                     | Provides information for each volume that has or had replicated folders.                                                  |



 

 

 




