---
title: Cluster.NetInterfaces property
description: Returns a ClusNetInterfaces collection providing access to the network interfaces in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f4fbac67-f196-4fd8-a678-8f7877e70f6a'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["NetInterfaces property Failover Cluster", "NetInterfaces property Failover Cluster , Cluster object", "Cluster object Failover Cluster , NetInterfaces property"]
topic_type:
- apiref
api_name:
- Cluster.NetInterfaces
- ISCluster.get_NetInterfaces
api_location:
- MsClus.dll
api_type:
- COM
---

# Cluster.NetInterfaces property

\[The **NetInterfaces** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusNetInterfaces**](clusnetinterfaces-collection.md) collection providing access to the [network interfaces](network-interfaces.md) in a [*cluster*](c-gly.md#-wolf-cluster-gly).

This property is read-only.

## Syntax


```VB
Cluster.NetInterfaces
```



## Property value

A [**ClusNetInterfaces**](clusnetinterfaces-collection.md) collection.

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

[**ClusNetInterfaces**](clusnetinterfaces-collection.md)
</dt> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





