---
title: ClusNode.Resume method
description: Resumes the cluster activity of a node after it has been paused by the ClusNode.Pause method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 74e465e2-1328-4e05-b287-3ce27359c67a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Resume method Failover Cluster
- Resume method Failover Cluster , ClusNode object
- ClusNode object Failover Cluster , Resume method
topic_type:
- apiref
api_name:
- ClusNode.Resume
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusNode.Resume method

\[The **Resume** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Resumes the [*cluster*](c-gly.md#-wolf-cluster-gly) activity of a [node](nodes.md) after it has been [*paused*](p-gly.md#-wolf-paused-gly) by the [**ClusNode.Pause**](clusnode-pause.md) method.

## Syntax


```VB
ClusNode.Resume()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

When a node resumes cluster activity after it has been paused, it returns **ClusterNodeUp** as the value for its [**ClusNode.State**](clusnode-state.md) property.

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

[**ClusNode.Pause**](clusnode-pause.md)
</dt> <dt>

[**ClusNode.State**](clusnode-state.md)
</dt> </dl>

 

 





