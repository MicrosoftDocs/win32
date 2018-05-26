---
title: ClusResource.OwnerNode property
description: A resources current owner node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dea1d13b-8a79-4ac4-ac29-437c520965f1
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- OwnerNode property Failover Cluster
- OwnerNode property Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , OwnerNode property
topic_type:
- apiref
api_name:
- ClusResource.OwnerNode
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResource.OwnerNode property

\[The **OwnerNode** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [resource's](resources.md) current owner [node](nodes.md).

This property is read-only.

## Syntax


```VB
ClusResource.OwnerNode
```



## Property value

A [**ClusNode**](clusnode-object.md) object that receives the node currently hosting the resource.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





