---
title: ClusNode.NetInterfaces property
description: A ClusNodeNetInterfaces collection providing access to the network interfaces installed on a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 98799b21-6646-430c-8194-debc7985fa9d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- NetInterfaces property Failover Cluster
- NetInterfaces property Failover Cluster , ClusNode object
- ClusNode object Failover Cluster , NetInterfaces property
topic_type:
- apiref
api_name:
- ClusNode.NetInterfaces
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusNode.NetInterfaces property

\[The **NetInterfaces** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusNodeNetInterfaces**](clusnodenetinterfaces-collection.md) collection providing access to the [network interfaces](network-interfaces.md) installed on a [node](nodes.md).

This property is read-only.

## Syntax


```VB
ClusNode.NetInterfaces
```



## Property value

A [**ClusNodeNetInterfaces**](clusnodenetinterfaces-collection.md) collection.

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

[**ClusNodeNetInterfaces**](clusnodenetinterfaces-collection.md)
</dt> </dl>

 

 





