---
title: Cluster.Nodes property
description: Returns a ClusNodes collection providing access to the nodes in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '690c9635-114f-4109-a9b9-4ebb1961c58b'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Nodes property Failover Cluster", "Nodes property Failover Cluster , Cluster object", "Cluster object Failover Cluster , Nodes property"]
topic_type:
- apiref
api_name:
- Cluster.Nodes
- ISCluster.get_Nodes
api_location:
- MsClus.dll
api_type:
- COM
---

# Cluster.Nodes property

\[The **Nodes** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusNodes**](clusnodes-collection.md) collection providing access to the [nodes](nodes.md) in a [*cluster*](c-gly.md#-wolf-cluster-gly).

This property is read-only.

## Syntax


```VB
Cluster.Nodes
```



## Property value

A [**ClusNodes**](clusnodes-collection.md) collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCluster is defined as F2E606E4-2631-11D1-89F1-00A0C90D061E<br/>          |



## See also

<dl> <dt>

[**ClusNodes**](clusnodes-collection.md)
</dt> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





