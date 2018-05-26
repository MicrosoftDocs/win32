---
title: ClusResTypePossibleOwnerNodes.Item property
description: Returns a possible owner node from the collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0d698f44-7480-43da-871b-51e7be2f9eff
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusResTypePossibleOwnerNodes class
- ClusResTypePossibleOwnerNodes class Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusResTypePossibleOwnerNodes.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResTypePossibleOwnerNodes.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [*possible owner*](p-gly.md#-wolf-possible-owner-gly) [node](nodes.md) from the collection.

This property is read-only.

## Syntax


```VB
ClusResTypePossibleOwnerNodes.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusNode**](clusnode-object.md) object that receives the specified node.

## Remarks

A node obtained from **Item** is one of the possible owner nodes of the [resource type](resource-types.md) from which the collection was obtained.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                          |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>                |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>              |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>              |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>              |
| IID<br/>                      | IID\_ISClusResTypePossibleOwnerNodes is defined as F2E60718-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResTypePossibleOwnerNodes**](clusrestypepossibleownernodes-collection.md)
</dt> <dt>

[**ClusResTypePossibleOwnerNodes.Count**](clusrestypepossibleownernodes-count.md)
</dt> </dl>

 

 





