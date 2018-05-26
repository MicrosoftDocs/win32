---
title: ClusResDependents collection
description: Provides access to the dependents of a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4e1f47fa-e240-4fdb-b736-9b2e64828eb0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusResDependents collection Failover Cluster
- ClusResDependents collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusResDependents
- ISClusResDependents
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ClusResDependents collection

\[The **ClusResDependents** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [dependents](resource-dependencies.md) of a [resource](resources.md). Resources added to a **ClusResDependents** collection become dependents of the resource from which the collection was obtained.

## Members

The **ClusResDependents** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResDependents** collection has these methods.



| Method                                                 | Description                                                                                      |
|:-------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**AddItem**](clusresdependents-additem.md)           | Adds an existing [*cluster*](c-gly.md#-wolf-cluster-gly) resource to the collection.<br/> |
| [**CreateItem**](clusresgroupresources-createitem.md) | Creates a new resource in the cluster and adds it to the collection.<br/>                  |
| [**DeleteItem**](clusresgroupresources-deleteitem.md) | Removes a resource from the collection and deletes the resource from the cluster.<br/>     |
| [**Refresh**](clusresdependents-refresh.md)           | Refreshes the data in the collection.<br/>                                                 |
| [**RemoveItem**](clusresdependents-removeitem.md)     | Removes a resource from the collection.<br/>                                               |



 

### Properties

The **ClusResDependents** collection has these properties.



| Property                                              | Access type          | Description                                                    |
|:------------------------------------------------------|:---------------------|:---------------------------------------------------------------|
| [**Count**](clusresdependents-count.md)<br/>   | Read-only<br/> | Returns the number of dependents in the collection.<br/> |
| [**Item**](clusresgroupresources-item.md)<br/> | Read-only<br/> | Returns a single resource from the collection.<br/>      |



 

## Remarks

A **ClusResDependents** collection:

-   Contains [**ClusResource**](clusresource-object.md) objects.
-   Is obtained from [**ClusResource.Dependencies**](clusresource-dependencies.md).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>              |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>  |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>  |
| IID<br/>                      | IID\_ISClusResDependents is defined as F2E6072E-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Resource Management Objects](resource-management-objects.md)
</dt> </dl>

 

 





