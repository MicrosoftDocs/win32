---
title: ClusResPossibleOwnerNodes.Item property
description: Returns a node from a resource's list of possible owner nodes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a8db9fab-822e-453f-ba5f-b5e75e6be7be
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusResPossibleOwnerNodes class
- ClusResPossibleOwnerNodes class Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusResPossibleOwnerNodes.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResPossibleOwnerNodes.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [node](nodes.md) from a [resource's](resources.md) list of [*possible owner*](https://www.bing.com/search?q=*possible owner*) nodes.

This property is read-only.

## Syntax


```VB
ClusResPossibleOwnerNodes.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusNode**](clusnode-object.md) object that receives the specified node.

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                      |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>            |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>          |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>          |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>          |
| IID<br/>                      | IID\_ISClusResPossibleOwnerNodes is defined as F2E6070E-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**ClusResPossibleOwnerNodes**](clusrespossibleownernodes-collection.md)
</dt> <dt>

[**ClusResPossibleOwnerNodes.Count**](clusrespossibleownernodes-count.md)
</dt> </dl>

 

 





