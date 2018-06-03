---
title: ClusResource.RemoveResourceNode method
description: Removes a node from the list of possible nodes that can host the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4ec493da-4524-4015-8aa7-fb4a8c3d78de
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RemoveResourceNode method Failover Cluster
- RemoveResourceNode method Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , RemoveResourceNode method
topic_type:
- apiref
api_name:
- ClusResource.RemoveResourceNode
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResource.RemoveResourceNode method

\[The **RemoveResourceNode** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Removes a [node](nodes.md) from the list of possible nodes that can host the [resource](resources.md).

## Syntax


```VB
ClusResource.RemoveResourceNode( _
  ByVal Node _
)
```



## Parameters

<dl> <dt>

*Node* 
</dt> <dd>

The [**ClusNode**](clusnode-object.md) object to be removed.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





