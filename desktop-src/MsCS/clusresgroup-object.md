---
title: ClusResGroup object
description: Enables operations on a group, its properties, and related objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cd0e8510-4eb0-45fe-819e-f40fe4bfa4e7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusResGroup object Failover Cluster
- ClusResGroup object Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusResGroup
- ISClusResGroup
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ClusResGroup object

\[The **ClusResGroup** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Enables operations on a [group](groups.md), its properties, and related objects. Use **ClusResGroup** to move groups between [nodes](nodes.md), bring groups [*online*](https://www.bing.com/search?q=*online*) and [*offline*](https://www.bing.com/search?q=*offline*), access the [resources](resources.md) in the group, and perform other group-related tasks.

## Members

The **ClusResGroup** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResGroup** object has these methods.



| Method                                  | Description                                                   |
|:----------------------------------------|:--------------------------------------------------------------|
| [**Delete**](clusresgroup-delete.md)   | Deletes a group from the collection.<br/>               |
| [**Move**](clusresgroup-move.md)       | Moves a group to the most preferred possible node.<br/> |
| [**Offline**](clusresgroup-offline.md) | Takes a group offline.<br/>                             |
| [**Online**](clusresgroup-online.md)   | Brings a group online.<br/>                             |



 

### Properties

The **ClusResGroup** object has these properties.



| Property                                                                   | Access type          | Description                                                                                                                                                                                                                                 |
|:---------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Cluster**](clusresgroup-cluster.md)<br/>                         | Read-only<br/> | Returns the [*cluster*](https://www.bing.com/search?q=*cluster*) associated with a group.<br/>                                                                                                                                                    |
| [**CommonProperties**](clusresgroup-commonproperties.md)<br/>       | Read-only<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the group's read/write [common properties](common-properties.md).<br/>                                                                           |
| [**CommonROProperties**](clusresgroup-commonroproperties.md)<br/>   | Read-only<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the group's read-only common properties.<br/>                                                                                                     |
| [**Name**](clusresgroup-name.md)<br/>                               | Read-only<br/> | Read/write property that sets the name of a group.<br/>                                                                                                                                                                               |
| [**OwnerNode**](clusresgroup-ownernode.md)<br/>                     | Read-only<br/> | Returns a group's node.<br/>                                                                                                                                                                                                          |
| [**PreferredOwnerNodes**](clusresgroup-preferredownernodes.md)<br/> | Read-only<br/> | Returns a [**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md) collection providing access to the nodes that belong in a group's [*preferred owner*](https://www.bing.com/search?q=*preferred owner*) list.<br/> |
| [**PrivateProperties**](clusresgroup-privateproperties.md)<br/>     | Read-only<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the group's read/write [private properties](private-properties.md).<br/>                                                                         |
| [**PrivateROProperties**](clusresgroup-privateroproperties.md)<br/> | Read-only<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the group's read-only private properties.<br/>                                                                                                    |
| [**Resources**](clusresgroup-resources.md)<br/>                     | Read-only<br/> | Returns a [**ClusResGroupResources**](clusresgroupresources-collection.md) collection providing access to the resources in a group.<br/>                                                                                             |
| [**State**](clusresgroup-state.md)<br/>                             | Read-only<br/> | Returns the state of a group.<br/>                                                                                                                                                                                                    |



 

## Remarks

A **ClusResGroup** object:

-   Is obtained from [**ClusResGroups**](clusresgroups-collection.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroup is defined as F2E60706-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[Group Management Objects](group-management-objects.md)
</dt> </dl>

 

 





