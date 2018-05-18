---
title: ClusResource.AddResourceNode method
description: Adds a new node to the list of possible nodes that can host the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '98727cb1-238f-4bd8-b83a-e3838f824a16'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["AddResourceNode method Failover Cluster", "AddResourceNode method Failover Cluster , ClusResource class", "ClusResource class Failover Cluster , AddResourceNode method"]
topic_type:
- apiref
api_name:
- ClusResource.AddResourceNode
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResource.AddResourceNode method

\[The **AddResourceNode** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Adds a new [node](nodes.md) to the list of possible nodes that can host the [resource](resources.md).

## Syntax


```VB
ClusResource.AddResourceNode( _
  ByVal objNode _
)
```



## Parameters

<dl> <dt>

*objNode* 
</dt> <dd>

The [**ClusNode**](clusnode-object.md) object to add to the list.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
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

 

 





