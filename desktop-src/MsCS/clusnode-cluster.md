---
title: ClusNode.Cluster property
description: Cluster object providing access to the cluster associated with a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fd0e7191-0df5-465e-b867-2c395447ebc9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Cluster property Failover Cluster
- Cluster property Failover Cluster , ClusNode object
- ClusNode object Failover Cluster , Cluster property
topic_type:
- apiref
api_name:
- ClusNode.Cluster
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusNode.Cluster property

\[The **Cluster** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**Cluster**](cluster-object.md) object providing access to the [*cluster*](https://www.bing.com/search?q=*cluster*) associated with a [node](nodes.md).

This property is read-only.

## Syntax


```VB
ClusNode.Cluster
```



## Property value

A [**Cluster**](cluster-object.md) object.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNode is defined as F2E606F8-2631-11D1-89F1-00A0C90D061E<br/>         |



## See also

<dl> <dt>

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





