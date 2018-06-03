---
title: ClusterNames.Count property
description: Returns the number of objects in the ClusterNames collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e67f64d2-89e1-423d-94a1-fa5d734c7194
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Count property Failover Cluster
- Count property Failover Cluster , ClusterNames collection
- ClusterNames collection Failover Cluster , Count property
topic_type:
- apiref
api_name:
- ClusterNames.Count
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusterNames.Count property

\[The **Count** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the number of objects in the [**ClusterNames**](clusternames-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusterNames.Count As Long
```



## Property value

**Long** indicating the number of objects in the collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusterNames is defined as F2E606EC-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusterNames**](clusternames-collection.md)
</dt> </dl>

 

 





