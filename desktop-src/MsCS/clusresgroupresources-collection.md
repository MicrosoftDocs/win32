---
title: ClusResGroupResources collection
description: Provides access to the resources that are current members of a group and allows a resource to be added to or deleted from the group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9ea90beb-86ae-4026-94bb-175e593da8fa
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusResGroupResources collection Failover Cluster
- ClusResGroupResources collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusResGroupResources
- ISClusResGroupResources
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ClusResGroupResources collection

\[The **ClusResGroupResources** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [resources](resources.md) that are current members of a [group](groups.md) and allows a resource to be added to or deleted from the group.

## Members

The **ClusResGroupResources** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResGroupResources** collection has these methods.



| Method                                                 | Description                                                                                                    |
|:-------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| [**CreateItem**](clusresgroupresources-createitem.md) | Creates a new cluster resource and adds it to the group.<br/>                                            |
| [**DeleteItem**](clusresgroupresources-deleteitem.md) | Removes a resource from the group and deletes it from the [*cluster*](c-gly.md#-wolf-cluster-gly).<br/> |
| [**Refresh**](clusresgroupresources-refresh.md)       | Refreshes the data in the collection.<br/>                                                               |



 

### Properties

The **ClusResGroupResources** collection has these properties.



| Property                                                | Access type          | Description                                                 |
|:--------------------------------------------------------|:---------------------|:------------------------------------------------------------|
| [**Count**](clusresgroupresources-count.md)<br/> | Read-only<br/> | Returns the number of objects in the collection.<br/> |
| [**Item**](clusresgroupresources-item.md)<br/>   | Read-only<br/> | Returns a single resource from the collection.<br/>   |



 

## Remarks

A **ClusResGroupResources** collection:

-   Contains [**ClusResource**](clusresource-object.md) objects.
-   Is obtained from [**ClusResGroup.Resources**](clusresgroup-resources.md).

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                  |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>        |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>      |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>      |
| IID<br/>                      | IID\_ISClusResGroupResources is defined as F2E606EA-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Group Management Objects](group-management-objects.md)
</dt> </dl>

 

 





