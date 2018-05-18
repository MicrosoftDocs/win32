---
title: ClusNode.Evict method
description: Removes a node from the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e65a230e-3931-4e1a-b80d-3fd2499d330c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Evict method Failover Cluster", "Evict method Failover Cluster , ClusNode object", "ClusNode object Failover Cluster , Evict method"]
topic_type:
- apiref
api_name:
- ClusNode.Evict
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusNode.Evict method

\[The **Evict** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Removes a [node](nodes.md) from the [*cluster*](c-gly.md#-wolf-cluster-gly).

## Syntax


```VB
ClusNode.Evict()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

An evicted node is no longer a member of the [*cluster*](c-gly.md#-wolf-cluster-gly). The [Cluster service](cluster-service.md) must be reinstalled on the node to reestablish the node's cluster membership.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNode is defined as F2E606F8-2631-11D1-89F1-00A0C90D061E<br/>         |



## See also

<dl> <dt>

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**Cluster Object**](cluster-object.md)
</dt> </dl>

 

 





