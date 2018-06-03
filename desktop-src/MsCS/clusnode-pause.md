---
title: ClusNode.Pause method
description: Suspends the cluster activity of a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2fd16dda-b554-47fa-a040-15c7685d6392
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Pause method Failover Cluster
- Pause method Failover Cluster , ClusNode object
- ClusNode object Failover Cluster , Pause method
topic_type:
- apiref
api_name:
- ClusNode.Pause
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusNode.Pause method

\[The **Pause** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Suspends the [*cluster*](https://www.bing.com/search?q=*cluster*) activity of a [node](nodes.md).

## Syntax


```VB
ClusNode.Pause()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Use the [**ClusNode.Resume**](clusnode-resume.md) method to return a paused node to active status.

While a node is paused, [groups](groups.md) cannot be moved to the node either through the [failover](failover.md) process or administrator action. A [*paused*](https://www.bing.com/search?q=*paused*) node returns **ClusterNodePaused** as the value for its [**ClusNode.State**](clusnode-state.md) property.

Groups that are owned by a paused node remain owned by that node. A paused node's groups and resources can be taken offline, but they cannot be brought online. Because the paused state is persistent, a paused node continues to be paused when it is rebooted.

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

[**ClusNode.Resume**](clusnode-resume.md)
</dt> <dt>

[**ClusNode.State**](clusnode-state.md)
</dt> </dl>

 

 





