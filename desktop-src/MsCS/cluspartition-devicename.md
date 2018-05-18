---
title: ClusPartition.DeviceName property
description: Device name of a storage class resource partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bd94ee19-33d1-43dd-bf4e-dddc63ea1e43'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DeviceName property Failover Cluster", "DeviceName property Failover Cluster , ClusPartition object", "ClusPartition object Failover Cluster , DeviceName property"]
topic_type:
- apiref
api_name:
- ClusPartition.DeviceName
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusPartition.DeviceName property

\[The **DeviceName** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the device name of a [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly) partition.

This property is read-only.

## Syntax


```VB
ClusPartition.DeviceName
```



## Property value

String that receives the device name of the partition.

## Remarks

The device name returned contains no backslashes.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusPartition is defined as F2E60720-2631-11D1-89F1-00A0C90D061E<br/>    |



## See also

<dl> <dt>

[**ClusPartition**](cluspartition-object.md)
</dt> </dl>

 

 





