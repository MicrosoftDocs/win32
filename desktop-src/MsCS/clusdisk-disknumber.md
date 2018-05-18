---
title: ClusDisk.DiskNumber property
description: Disk number of a Physical Disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f55fd6aa-8707-4a62-8e6c-259d7bf52d0d'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DiskNumber property Failover Cluster", "DiskNumber property Failover Cluster , ClusDisk object", "ClusDisk object Failover Cluster , DiskNumber property"]
topic_type:
- apiref
api_name:
- ClusDisk.DiskNumber
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusDisk.DiskNumber property

\[The **DiskNumber** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the disk number of a [Physical Disk](physical-disk.md).

This property is read-only.

## Syntax


```VB
ClusDisk.DiskNumber
```



## Property value

A **Variant** that receives the disk number of the disk.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusDisk is defined as F2E60724-2631-11D1-89F1-00A0C90D061E<br/>         |



## See also

<dl> <dt>

[**ClusDisk**](clusdisk-object.md)
</dt> <dt>

[**ClusDisk.Partitions**](clusdisk-partitions.md)
</dt> <dt>

[**ClusDisk.ScsiAddress**](clusdisk-scsiaddress.md)
</dt> <dt>

[**ClusDisk.Signature**](clusdisk-signature.md)
</dt> </dl>

 

 





