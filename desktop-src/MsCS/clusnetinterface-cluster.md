---
title: ClusNetInterface.Cluster property
description: Cluster object providing access to the cluster associated with a network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fa09d9be-805c-4cf3-b2ac-8b194e52f429
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Cluster property Failover Cluster
- Cluster property Failover Cluster , ClusNetInterface object
- ClusNetInterface object Failover Cluster , Cluster property
topic_type:
- apiref
api_name:
- ClusNetInterface.Cluster
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusNetInterface.Cluster property

\[The **Cluster** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**Cluster**](cluster-object.md) object providing access to the [*cluster*](c-gly.md#-wolf-cluster-gly) associated with a [network interface](network-interfaces.md).

This property is read-only.

## Syntax


```VB
ClusNetInterface.Cluster
```



## Property value

A [**Cluster**](cluster-object.md) object that receives the cluster associated with the network interface.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNetInterface is defined as F2E606EE-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusNetInterface**](clusnetinterface-object.md)
</dt> <dt>

[**ClusterObject**](cluster-object.md)
</dt> </dl>

 

 





