---
title: ClusNodes.Item property
description: Single node from a ClusNodes collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5cb658c3-4eaa-482d-b467-04c1f65ed8a0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusNodes collection
- ClusNodes collection Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusNodes.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusNodes.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a single [node](nodes.md) from a [**ClusNodes**](clusnodes-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusNodes.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusNode**](clusnode-object.md) object that receives the specified node.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNodes is defined as F2E606FA-2631-11D1-89F1-00A0C90D061E<br/>        |



## See also

<dl> <dt>

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**ClusNodes**](clusnodes-collection.md)
</dt> <dt>

[**ClusNodes.Count**](clusnodes-count.md)
</dt> </dl>

 

 





