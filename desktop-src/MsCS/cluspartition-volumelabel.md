---
title: ClusPartition.VolumeLabel property
description: Volume label of a storage class resource partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 12fbb270-63a4-438c-9492-82a4568ebcfc
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- VolumeLabel property Failover Cluster
- VolumeLabel property Failover Cluster , ClusPartition object
- ClusPartition object Failover Cluster , VolumeLabel property
topic_type:
- apiref
api_name:
- ClusPartition.VolumeLabel
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusPartition.VolumeLabel property

\[The **VolumeLabel** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the volume label of a [*storage class resource*](https://www.bing.com/search?q=*storage class resource*) partition.

This property is read-only.

## Syntax


```VB
ClusPartition.VolumeLabel
```



## Property value

String that receives the volume label of the partition.

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
</dt> </dl>

 

 





