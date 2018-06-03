---
title: ClusNode.ResourceGroups property
description: Returns a ClusResGroups collection providing access to the groups currently owned by the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 45eae46b-54d2-4945-aab1-8b471df64881
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ResourceGroups property Failover Cluster
- ResourceGroups property Failover Cluster , ClusNode object
- ClusNode object Failover Cluster , ResourceGroups property
topic_type:
- apiref
api_name:
- ClusNode.ResourceGroups
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusNode.ResourceGroups property

\[The **ResourceGroups** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusResGroups**](clusresgroups-collection.md) collection providing access to the [groups](groups.md) currently owned by the [node](nodes.md).

This property is read-only.

## Syntax


```VB
ClusNode.ResourceGroups
```



## Property value

A [**ClusResGroups**](clusresgroups-collection.md) collection.

## Remarks

To retrieve information about all of the groups in the [*cluster*](https://www.bing.com/search?q=*cluster*), use the [**Cluster.ResourceGroups**](cluster-resourcegroups.md) property.

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

[**ClusResGroups**](clusresgroups-collection.md)
</dt> <dt>

[**Cluster.ResourceGroups**](cluster-resourcegroups.md)
</dt> </dl>

 

 





