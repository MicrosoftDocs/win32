---
title: ClusResType.PossibleOwnerNodes property
description: Returns the nodes specified as possible owners of a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9437a940-bb61-4de1-9d4b-54876161e02c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PossibleOwnerNodes property Failover Cluster
- PossibleOwnerNodes property Failover Cluster , ClusResType object
- ClusResType object Failover Cluster , PossibleOwnerNodes property
topic_type:
- apiref
api_name:
- ClusResType.PossibleOwnerNodes
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResType.PossibleOwnerNodes property

\[The **PossibleOwnerNodes** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the [nodes](nodes.md) specified as [*possible owners*](p-gly.md#-wolf-possible-owner-gly) of a [resource type](resource-types.md).

This property is read-only.

## Syntax


```VB
ClusResType.PossibleOwnerNodes
```



## Property value

A [**ClusResTypePossibleOwnerNodes**](clusrestypepossibleownernodes-collection.md) collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResType is defined as F2E60710-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**ClusResType**](clusrestype-object.md)
</dt> <dt>

[**ClusResTypePossibleOwnerNodes**](clusrestypepossibleownernodes-collection.md)
</dt> </dl>

 

 





