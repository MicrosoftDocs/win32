---
title: ClusNode.NodeID property
description: Unique identifier of a cluster node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8ef68a5e-e7a0-4b32-8649-4fd194520ea6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- NodeID property Failover Cluster
- NodeID property Failover Cluster , ClusNode object
- ClusNode object Failover Cluster , NodeID property
topic_type:
- apiref
api_name:
- ClusNode.NodeID
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusNode.NodeID property

\[The **NodeID** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the unique identifier of a cluster [node](nodes.md).

This property is read-only.

## Syntax


```VB
ClusNode.NodeID
```



## Property value

**String** that receives the node's unique identifier.

## Remarks

The **NodeID** of a node is stored under **HKEY\_LOCAL\_MACHINE**\\**Cluster**\\**Node**.

**NodeID** is not accessible through [Cluster Administrator](cluster-administrator.md).

Changing the name of a node does not affect its **NodeID**.

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

[CLUSCTL\_NODE\_GET\_ID](clusctl-node-get-id.md)
</dt> <dt>

[**ClusNode**](clusnode-object.md)
</dt> </dl>

 

 





