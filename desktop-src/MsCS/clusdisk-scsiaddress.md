---
title: ClusDisk.ScsiAddress property
description: ClusScsiAddress object describing SCSI information about a Physical Disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2f9bd5e9-a939-438d-9bd1-bd9ef30c53cd'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ScsiAddress property Failover Cluster", "ScsiAddress property Failover Cluster , ClusDisk object", "ClusDisk object Failover Cluster , ScsiAddress property"]
topic_type:
- apiref
api_name:
- ClusDisk.ScsiAddress
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusDisk.ScsiAddress property

\[The **ScsiAddress** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusScsiAddress**](clusscsiaddress-object.md) object describing [*SCSI*](s-gly.md#-wolf-small-computer-system-interface-gly) information about a [Physical Disk](physical-disk.md).

This property is read-only.

## Syntax


```VB
ClusDisk.ScsiAddress
```



## Property value

A [**ClusScsiAddress**](clusscsiaddress-object.md) object that receives the SCSI information.

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

[**ClusDisk.Signature**](clusdisk-signature.md)
</dt> </dl>

 

 





