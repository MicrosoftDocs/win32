---
title: ClusNode.PrivateProperties property
description: Read/write private properties of a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 33520afe-ec3e-41dc-ad16-aaee4f5394aa
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PrivateProperties property Failover Cluster
- PrivateProperties property Failover Cluster , ClusNode object
- ClusNode object Failover Cluster , PrivateProperties property
topic_type:
- apiref
api_name:
- ClusNode.PrivateProperties
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusNode.PrivateProperties property

\[The **PrivateProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read/write [private properties](private-properties.md) of a [node](nodes.md).

This property is read-only.

## Syntax


```VB
ClusNode.PrivateProperties
```



## Property value

A [**ClusProperties**](clusproperties-collection.md) collection that receives the read/write private properties of the node.

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

[**ClusProperties**](clusproperties-collection.md)
</dt> </dl>

 

 





