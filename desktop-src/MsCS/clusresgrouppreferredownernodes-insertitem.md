---
title: ClusResGroupPreferredOwnerNodes.InsertItem method
description: Adds a node to the ClusResGroupPreferredOwnerNodes collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ae234397-a592-41a3-a30d-cb4b6450e332
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- InsertItem method Failover Cluster
- InsertItem method Failover Cluster , ClusResGroupPreferredOwnerNodes class
- ClusResGroupPreferredOwnerNodes class Failover Cluster , InsertItem method
topic_type:
- apiref
api_name:
- ClusResGroupPreferredOwnerNodes.InsertItem
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResGroupPreferredOwnerNodes.InsertItem method

\[The **InsertItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Adds a [node](nodes.md) to the [**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md) collection.

## Syntax


```VB
ClusResGroupPreferredOwnerNodes.InsertItem( _
  ByVal objNode, _
  ByVal lPosition _
)
```



## Parameters

<dl> <dt>

*objNode* 
</dt> <dd>

A [**ClusNode**](clusnode-object.md) object to be added to the collection.

</dd> <dt>

*lPosition* 
</dt> <dd>

Optional. **Long** that identifies the location within the collection to add the new node. Highly preferred, high-priority nodes have low position values (that is, they occur first in the list).

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Adding a node to a group's [**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md) collection means that the node is listed as a [*preferred owner*](p-gly.md#-wolf-preferred-owner-gly) node for the group. Use *lPosition* to specify an order of preference, with low values corresponding to highly preferred, high-priority nodes.

To add a node to the end of the list, use the [**ClusResGroupPreferredOwnerNodes.AddItem**](clusresgrouppreferredownernodes-additem.md) method.

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

[**ClusResGroupPreferredOwnerNodes.AddItem**](clusresgrouppreferredownernodes-additem.md)
</dt> </dl>

 

 





