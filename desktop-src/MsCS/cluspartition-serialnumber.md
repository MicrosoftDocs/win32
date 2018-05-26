---
title: ClusPartition.SerialNumber property
description: Serial number of a storage class resource partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ffc91ad2-c3ce-4fa0-994f-2a2269dff52c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- SerialNumber property Failover Cluster
- SerialNumber property Failover Cluster , ClusPartition object
- ClusPartition object Failover Cluster , SerialNumber property
topic_type:
- apiref
api_name:
- ClusPartition.SerialNumber
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusPartition.SerialNumber property

\[The **SerialNumber** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the serial number of a [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly) partition.

This property is read-only.

## Syntax


```VB
ClusPartition.SerialNumber
```



## Property value

**Long** containing the serial number of the partition.

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

 

 





