---
title: ClusDisk.Signature property
description: Signature of a Physical Disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f8fae469-9259-4191-8af4-a7d408ce6667
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Signature property Failover Cluster
- Signature property Failover Cluster , ClusDisk object
- ClusDisk object Failover Cluster , Signature property
topic_type:
- apiref
api_name:
- ClusDisk.Signature
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusDisk.Signature property

\[The **Signature** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the signature of a [Physical Disk](physical-disk.md).

This property is read-only.

## Syntax


```VB
ClusDisk.Signature
```



## Property value

**Long** that receives the signature of the disk.

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

[**ClusDisk.DiskNumber**](clusdisk-disknumber.md)
</dt> <dt>

[**ClusDisk.Partitions**](clusdisk-partitions.md)
</dt> <dt>

[**ClusDisk.ScsiAddress**](clusdisk-scsiaddress.md)
</dt> </dl>

 

 





