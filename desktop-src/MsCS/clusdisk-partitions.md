---
title: ClusDisk.Partitions property
description: ClusPartitions collection containing partition information about a Physical Disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d0a6ec99-c7c8-4746-aaa7-ee70a2e8f355
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Partitions property Failover Cluster
- Partitions property Failover Cluster , ClusDisk object
- ClusDisk object Failover Cluster , Partitions property
topic_type:
- apiref
api_name:
- ClusDisk.Partitions
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusDisk.Partitions property

\[The **Partitions** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusPartitions**](cluspartitions-collection.md) collection containing partition information about a [Physical Disk](physical-disk.md).

This property is read-only.

## Syntax


```VB
ClusDisk.Partitions
```



## Property value

A [**ClusPartitions**](cluspartitions-collection.md) collection that receives the partition information.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusDisk is defined as F2E60724-2631-11D1-89F1-00A0C90D061E<br/>         |



## See also

<dl> <dt>

[**ClusDisk**](clusdisk-object.md)
</dt> <dt>

[**ClusDisk.ScsiAddress**](clusdisk-scsiaddress.md)
</dt> <dt>

[**ClusDisk.Signature**](clusdisk-signature.md)
</dt> </dl>

 

 





