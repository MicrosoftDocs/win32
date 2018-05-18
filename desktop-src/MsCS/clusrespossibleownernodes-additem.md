---
title: ClusResPossibleOwnerNodes.AddItem method
description: Adds a node to a resource's \ 32; possible owners list.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '35d5eda5-09b6-4379-847a-dbb35f59f565'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["AddItem method Failover Cluster", "AddItem method Failover Cluster , ClusResPossibleOwnerNodes class", "ClusResPossibleOwnerNodes class Failover Cluster , AddItem method"]
topic_type:
- apiref
api_name:
- ClusResPossibleOwnerNodes.AddItem
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResPossibleOwnerNodes.AddItem method

\[The **AddItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Adds a node to a [resource's](resources.md) [*possible owners*](p-gly.md#-wolf-possible-owner-gly) list.

## Syntax


```VB
ClusResPossibleOwnerNodes.AddItem( _
  ByVal objNode _
)
```



## Parameters

<dl> <dt>

*objNode* 
</dt> <dd>

A [**ClusNode**](clusnode-object.md) object to add to the possible owners list.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                      |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>            |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>          |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>          |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>          |
| IID<br/>                      | IID\_ISClusResPossibleOwnerNodes is defined as F2E6070E-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**ClusResPossibleOwnerNodes**](clusrespossibleownernodes-collection.md)
</dt> </dl>

 

 





