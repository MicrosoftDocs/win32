---
title: ClusResGroupPreferredOwnerNodes.RemoveItem method
description: Removes a node from the ClusResGroupPreferredOwnerNodes collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9126b3ae-4dd3-402a-bda9-ce2d3ded8b36
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RemoveItem method Failover Cluster
- RemoveItem method Failover Cluster , ClusResGroupPreferredOwnerNodes class
- ClusResGroupPreferredOwnerNodes class Failover Cluster , RemoveItem method
topic_type:
- apiref
api_name:
- ClusResGroupPreferredOwnerNodes.RemoveItem
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResGroupPreferredOwnerNodes.RemoveItem method

\[The **RemoveItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Removes a [node](nodes.md) from the [**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md) collection.

## Syntax


```VB
ClusResGroupPreferredOwnerNodes.RemoveItem( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

A **Variant** identifying the node to be removed either by name or numeric index.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Removing a node from a [group's](groups.md) [**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md) collection removes the node from the group's [*preferred owners*](https://www.bing.com/search?q=*preferred owners*) list.

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                            |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>                  |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>                |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>                |
| IID<br/>                      | IID\_ISClusResGroupPreferredOwnerNodes is defined as F2E606E8-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md)
</dt> </dl>

 

 





