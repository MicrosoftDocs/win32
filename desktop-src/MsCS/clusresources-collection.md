---
title: ClusResources collection
description: Provides access to the resources that belong to a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 56dd53e7-7e2e-481f-b343-da51c7c52553
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusResources collection Failover Cluster
- ClusResources collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusResources
- ISClusResources
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ClusResources collection

\[The **ClusResources** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [resources](resources.md) that belong to a [*cluster*](https://www.bing.com/search?q=*cluster*).

## Members

The **ClusResources** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResources** collection has these methods.



| Method                                         | Description                                                      |
|:-----------------------------------------------|:-----------------------------------------------------------------|
| [**CreateItem**](clusresources-createitem.md) | Creates a new resource and adds it to the collection.<br/> |
| [**DeleteItem**](clusresources-deleteitem.md) | Deletes a resource from the cluster.<br/>                  |
| [**Refresh**](clusresources-refresh.md)       | Refreshes the data in the collection.<br/>                 |



 

### Properties

The **ClusResources** collection has these properties.



| Property                                        | Access type          | Description                                                 |
|:------------------------------------------------|:---------------------|:------------------------------------------------------------|
| [**Count**](clusresources-count.md)<br/> | Read-only<br/> | Returns the number of objects in the collection.<br/> |
| [**Item**](clusresources-item.md)<br/>   | Read-only<br/> | Returns a single resource from the collection.<br/>   |



 

## Remarks

A **ClusResources** collection:

-   Contains [**ClusResource**](clusresource-object.md) objects.
-   Is obtained from [**Cluster.Resources**](cluster-resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResources is defined as F2E6070C-2631-11D1-89F1-00A0C90D061E<br/>    |



## See also

<dl> <dt>

[Cluster Management Objects](cluster-management-objects.md)
</dt> </dl>

 

 





