---
title: ClusResGroupPreferredOwnerNodes.AddItem method
description: Adds a node to the ClusResGroupPreferredOwnerNodes collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 001e2766-d489-4406-b11e-c19c6426dfd4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AddItem method Failover Cluster
- AddItem method Failover Cluster , ClusResGroupPreferredOwnerNodes class
- ClusResGroupPreferredOwnerNodes class Failover Cluster , AddItem method
topic_type:
- apiref
api_name:
- ClusResGroupPreferredOwnerNodes.AddItem
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResGroupPreferredOwnerNodes.AddItem method

\[The **AddItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Adds a [node](nodes.md) to the [**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md) collection.

## Syntax


```VB
ClusResGroupPreferredOwnerNodes.AddItem( _
  ByVal objNode _
)
```



## Parameters

<dl> <dt>

*objNode* 
</dt> <dd>

A [**ClusNode**](clusnode-object.md) object to be added to the collection.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Adding a node to a group's [**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md) collection means that the node is listed as a [*preferred owner*](https://www.bing.com/search?q=*preferred owner*) node for the group.

The **AddItem** method always adds a node at the end of the list, giving it the lowest priority. To add a node and specify its priority in the list, see [**ClusResGroupPreferredOwnerNodes.InsertItem**](clusresgrouppreferredownernodes-insertitem.md).

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

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md)
</dt> <dt>

[**ClusResGroupPreferredOwnerNodes.InsertItem**](clusresgrouppreferredownernodes-insertitem.md)
</dt> </dl>

 

 





