---
title: ClusNode.CommonProperties property
description: Read/write common properties of a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 976be45f-39dd-46ee-b558-026afa129b21
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CommonProperties property Failover Cluster
- CommonProperties property Failover Cluster , ClusNode object
- ClusNode object Failover Cluster , CommonProperties property
topic_type:
- apiref
api_name:
- ClusNode.CommonProperties
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusNode.CommonProperties property

\[The **CommonProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read/write [common properties](common-properties.md) of a [node](nodes.md).

This property is read-only.

## Syntax


```VB
ClusNode.CommonProperties
```



## Property value

A [**ClusProperties**](clusproperties-collection.md) collection that receives the read/write common properties of the node.

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
</dt> <dt>

[**ClusNode.CommonROProperties**](clusnode-commonroproperties.md)
</dt> </dl>

 

 





