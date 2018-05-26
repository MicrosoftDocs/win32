---
title: ClusResGroups collection
description: Provides access to all cluster groups belonging either to a cluster or to a particular node in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7411d5f9-15c0-4c03-9128-c6b636979a50
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusResGroups collection Failover Cluster
- ClusResGroups collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusResGroups
- ISClusResGroups
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ClusResGroups collection

\[The **ClusResGroups** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to all cluster [groups](groups.md) belonging either to a [*cluster*](c-gly.md#-wolf-cluster-gly) or to a particular [node](nodes.md) in a cluster.

## Members

The **ClusResGroups** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResGroups** collection has these methods.



| Method                                         | Description                                                   |
|:-----------------------------------------------|:--------------------------------------------------------------|
| [**CreateItem**](clusresgroups-createitem.md) | Creates a new group and adds it to the collection.<br/> |
| [**DeleteItem**](clusresgroups-deleteitem.md) | Deletes a group from the collection.<br/>               |
| [**Refresh**](clusresgroups-refresh.md)       | Refreshes the data in the collection.<br/>              |



 

### Properties

The **ClusResGroups** collection has these properties.



| Property                                        | Access type          | Description                                                 |
|:------------------------------------------------|:---------------------|:------------------------------------------------------------|
| [**Count**](clusresgroups-count.md)<br/> | Read-only<br/> | Returns the number of objects in the collection.<br/> |
| [**Item**](clusresgroups-item.md)<br/>   | Read-only<br/> | Returns a single group from the collection.<br/>      |



 

## Remarks

A **ClusResGroups** collection:

-   Contains [**ClusResGroup**](clusresgroup-object.md) objects.
-   Is obtained from [**Cluster.ResourceGroups**](cluster-resourcegroups.md) or [**ClusNode.ResourceGroups**](clusnode-resourcegroups.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroups is defined as F2E60708-2631-11D1-89F1-00A0C90D061E<br/>    |



## See also

<dl> <dt>

[Cluster Management Objects](cluster-management-objects.md)
</dt> </dl>

 

 





