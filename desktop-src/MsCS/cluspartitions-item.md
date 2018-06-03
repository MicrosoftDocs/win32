---
title: ClusPartitions.Item property
description: Single partition from a ClusPartitions collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 62b58676-b026-428a-b035-9ad65e326a03
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusPartitions collection
- ClusPartitions collection Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusPartitions.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusPartitions.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a single partition from a [**ClusPartitions**](cluspartitions-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusPartitions.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusPartition**](cluspartition-object.md) object that receives the specified properties.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusPartitions is defined as F2E60722-2631-11D1-89F1-00A0C90D061E<br/>   |



## See also

<dl> <dt>

[**ClusPartition**](cluspartition-object.md)
</dt> <dt>

[**ClusPartitions**](cluspartitions-collection.md)
</dt> <dt>

[**ClusPartitions.Count**](cluspartitions-count.md)
</dt> </dl>

 

 





