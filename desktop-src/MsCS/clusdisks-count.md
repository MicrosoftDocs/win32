---
title: ClusDisks.Count property
description: Number of disks in the ClusDisks collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6b0f88df-391d-4cfb-b0be-cf77747d024e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Count property Failover Cluster", "Count property Failover Cluster , ClusDisks class", "ClusDisks class Failover Cluster , Count property"]
topic_type:
- apiref
api_name:
- ClusDisks.Count
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusDisks.Count property

\[The **Count** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the number of disks in the [**ClusDisks**](clusdisks-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusDisks.Count
```



## Property value

**Long** indicating the number of disks in the collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusDisks is defined as F2E60726-2631-11D1-89F1-00A0C90D061E<br/>        |



## See also

<dl> <dt>

[**ClusDisks**](clusdisks-collection.md)
</dt> </dl>

 

 





