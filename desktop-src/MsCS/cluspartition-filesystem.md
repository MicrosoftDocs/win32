---
title: ClusPartition.FileSystem property
description: Name of the file system residing on a storage class resource partition ( \ 0034;FAT \ 0034;, \ 0034;NTFS \ 0034;, and so on).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2cfc3851-23ee-4614-b581-e819be3f5de3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- FileSystem property Failover Cluster
- FileSystem property Failover Cluster , ClusPartition object
- ClusPartition object Failover Cluster , FileSystem property
topic_type:
- apiref
api_name:
- ClusPartition.FileSystem
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusPartition.FileSystem property

\[The **FileSystem** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the name of the file system residing on a [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly) partition ("FAT", "NTFS", and so on).

This property is read-only.

## Syntax


```VB
ClusPartition.FileSystem
```



## Property value

String that receives the file system of the storage class resource.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusPartition is defined as F2E60720-2631-11D1-89F1-00A0C90D061E<br/>    |



## See also

<dl> <dt>

[**ClusPartition**](cluspartition-object.md)
</dt> <dt>

[**ClusPartition.FileSystemFlags**](cluspartition-filesystemflags.md)
</dt> </dl>

 

 





