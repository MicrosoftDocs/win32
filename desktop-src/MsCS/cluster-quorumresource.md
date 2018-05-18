---
title: Cluster.QuorumResource property
description: Returns the current quorum resource for a cluster or allows a new quorum resource to be designated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e9c1f32a-2008-470e-b451-312cce49c93a'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["QuorumResource property Failover Cluster", "QuorumResource property Failover Cluster , Cluster object", "Cluster object Failover Cluster , QuorumResource property"]
topic_type:
- apiref
api_name:
- Cluster.QuorumResource
- ISCluster.get_QuorumResource
- ISCluster.put_QuorumResource
api_location:
- MsClus.dll
api_type:
- COM
---

# Cluster.QuorumResource property

\[The **QuorumResource** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the current [quorum resource](quorum-resource.md) for a [*cluster*](c-gly.md#-wolf-cluster-gly) or allows a new quorum resource to be designated.

This property is read/write.

## Syntax


```VB
Cluster.QuorumResource
```



## Property value

A [**ClusResource**](clusresource-object.md) object representing the cluster's quorum resource.

## Remarks

An alternate way to assign a quorum resource is to call that resource's [**ClusResource.BecomeQuorumResource**](clusresource-becomequorumresource.md) method.

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

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**ClusResource.BecomeQuorumResource**](clusresource-becomequorumresource.md)
</dt> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





