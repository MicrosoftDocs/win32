---
title: Cluster.PrivateProperties property
description: Returns the read/write private properties of a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f866a25f-64ef-4289-b95a-c55cb90a5d42
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PrivateProperties property Failover Cluster
- PrivateProperties property Failover Cluster , Cluster object
- Cluster object Failover Cluster , PrivateProperties property
topic_type:
- apiref
api_name:
- Cluster.PrivateProperties
- ISCluster.get_PrivateProperties
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Cluster.PrivateProperties property

\[The **PrivateProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read/write [private properties](private-properties.md) of a [*cluster*](c-gly.md#-wolf-cluster-gly).

This property is read-only.

## Syntax


```VB
Cluster.PrivateProperties
```



## Property value

A [**ClusProperties**](clusproperties-collection.md) collection that receives the read/write private properties of the cluster.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCluster is defined as F2E606E4-2631-11D1-89F1-00A0C90D061E<br/>          |



## See also

<dl> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





