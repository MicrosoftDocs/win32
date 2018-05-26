---
title: ClusResPossibleOwnerNodes.RemoveItem method
description: Removes a node from a resources possible owners list.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f6018dd5-7cfc-4d1f-bb2f-23c87c671349
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RemoveItem method Failover Cluster
- RemoveItem method Failover Cluster , ClusResPossibleOwnerNodes class
- ClusResPossibleOwnerNodes class Failover Cluster , RemoveItem method
topic_type:
- apiref
api_name:
- ClusResPossibleOwnerNodes.RemoveItem
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResPossibleOwnerNodes.RemoveItem method

\[The **RemoveItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Removes a [node](nodes.md) from a [resource's](resources.md) [*possible owners*](p-gly.md#-wolf-possible-owner-gly) list.

## Syntax


```VB
ClusResPossibleOwnerNodes.RemoveItem( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

A **Variant** that identifies an object in the collection by name or numeric index. Index numbers range from 1 to [**ClusResPossibleOwnerNodes.Count**](clusrespossibleownernodes-count.md).

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                      |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>            |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>          |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>          |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>          |
| IID<br/>                      | IID\_ISClusResPossibleOwnerNodes is defined as F2E6070E-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResPossibleOwnerNodes**](clusrespossibleownernodes-collection.md)
</dt> <dt>

[**ClusResPossibleOwnerNodes.Count**](clusrespossibleownernodes-count.md)
</dt> </dl>

 

 





