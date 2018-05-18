---
title: ClusNetwork.Cluster property
description: Cluster object providing access to the cluster that owns the network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2ed83842-2522-4c1f-9d97-fea77c7960a3'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Cluster property Failover Cluster", "Cluster property Failover Cluster , ClusNetwork object", "ClusNetwork object Failover Cluster , Cluster property"]
topic_type:
- apiref
api_name:
- ClusNetwork.Cluster
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusNetwork.Cluster property

\[The **Cluster** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**Cluster**](cluster-object.md) object providing access to the [*cluster*](c-gly.md#-wolf-cluster-gly) that owns the [network](networks.md).

This property is read-only.

## Syntax


```VB
ClusNetwork.Cluster
```



## Property value

A [**Cluster**](cluster-object.md) object that receives the cluster.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNetwork is defined as F2E606F2-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**ClusNetwork**](clusnetwork-object.md)
</dt> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





