---
title: ClusResGroupPreferredOwnerNodes collection
description: Provides access to the nodes that belong to the preferred owner list for a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3425825e-890c-4d3d-919e-a66963e1fc55'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusResGroupPreferredOwnerNodes collection Failover Cluster", "ClusResGroupPreferredOwnerNodes collection Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusResGroupPreferredOwnerNodes
- ISClusResGroupPreferredOwnerNodes
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResGroupPreferredOwnerNodes collection

\[The **ClusResGroupPreferredOwnerNodes** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [nodes](nodes.md) that belong to the [*preferred owner*](p-gly.md#-wolf-preferred-owner-gly) list for a [group](groups.md).

## Members

The **ClusResGroupPreferredOwnerNodes** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResGroupPreferredOwnerNodes** collection has these methods.



| Method                                                             | Description                                                                                         |
|:-------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| [**AddItem**](clusresgrouppreferredownernodes-additem.md)         | Adds a node to the preferred owners list.<br/>                                                |
| [**InsertItem**](clusresgrouppreferredownernodes-insertitem.md)   | Adds a node to the preferred owners list.<br/>                                                |
| [**Refresh**](clusresgrouppreferredownernodes-refresh.md)         | Refreshes the data in the collection.<br/>                                                    |
| [**RemoveItem**](clusresgrouppreferredownernodes-removeitem.md)   | Removes a node from preferred owners list.<br/>                                               |
| [**SaveChanges**](clusresgrouppreferredownernodes-savechanges.md) | Saves the list of preferred owner nodes to the [cluster database](cluster-database.md).<br/> |



 

### Properties

The **ClusResGroupPreferredOwnerNodes** collection has these properties.



| Property                                                                | Access type          | Description                                                                 |
|:------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------|
| [**Count**](clusresgrouppreferredownernodes-count.md)<br/>       | Read-only<br/> | Returns the number of objects in the collection.<br/>                 |
| [**Item**](clusresgrouppreferredownernodes-item.md)<br/>         | Read-only<br/> | Returns a single node from the collection.<br/>                       |
| [**Modified**](clusresgrouppreferredownernodes-modified.md)<br/> | Read-only<br/> | Reports whether any of the nodes in the collection have changed.<br/> |



 

## Remarks

A **ClusResGroupPreferredOwnerNodes** collection:

-   Contains [**ClusNode**](clusnode-object.md) objects.
-   Is obtained from [**ClusResGroup.PreferredOwnerNodes**](clusresgroup-preferredownernodes.md).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                            |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>                  |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>                |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>                |
| IID<br/>                      | IID\_ISClusResGroupPreferredOwnerNodes is defined as F2E606E8-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Group Management Objects](group-management-objects.md)
</dt> </dl>

 

 





