---
title: Cluster.ResourceGroups property
description: Returns the groups in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '449e4432-571c-403c-81c7-da50f455224c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ResourceGroups property Failover Cluster", "ResourceGroups property Failover Cluster , Cluster object", "Cluster object Failover Cluster , ResourceGroups property"]
topic_type:
- apiref
api_name:
- Cluster.ResourceGroups
- ISCluster.get_ResourceGroups
api_location:
- MsClus.dll
api_type:
- COM
---

# Cluster.ResourceGroups property

\[The **ResourceGroups** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the [groups](groups.md) in a [*cluster*](c-gly.md#-wolf-cluster-gly).

This property is read-only.

## Syntax


```VB
Cluster.ResourceGroups
```



## Property value

A [**ClusResGroups**](clusresgroups-collection.md) collection providing access to all of the groups in the cluster.

## Remarks

To access all of the groups for a particular [node](nodes.md), use the [**ClusNode.ResourceGroups**](clusnode-resourcegroups.md) property for that node.

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

[**ClusNode.ResourceGroups**](clusnode-resourcegroups.md)
</dt> <dt>

[**ClusResGroups**](clusresgroups-collection.md)
</dt> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





