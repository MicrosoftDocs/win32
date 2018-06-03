---
title: ClusResGroup.OwnerNode property
description: Returns the node currently hosting a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d42e2f2e-5a67-4e9e-9e54-34f514c0a8f2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- OwnerNode property Failover Cluster
- OwnerNode property Failover Cluster , ClusResGroup class
- ClusResGroup class Failover Cluster , OwnerNode property
topic_type:
- apiref
api_name:
- ClusResGroup.OwnerNode
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResGroup.OwnerNode property

\[The **OwnerNode** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the [node](nodes.md) currently hosting a [group](groups.md).

This property is read-only.

## Syntax


```VB
ClusResGroup.OwnerNode
```



## Property value

A [**ClusNode**](clusnode-object.md) object that receives the node that is currently hosting the group.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroup is defined as F2E60706-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> </dl>

 

 





