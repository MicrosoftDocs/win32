---
title: ClusResTypeResources collection
description: Provides access to the resources of a particular type in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3164f2ee-7230-4d77-8c7c-cfba3aaee9d4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusResTypeResources collection Failover Cluster
- ClusResTypeResources collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusResTypeResources
- ISClusResTypeResources
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ClusResTypeResources collection

\[The **ClusResTypeResources** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [resources](resources.md) of a particular [type](resource-types.md) in a [*cluster*](c-gly.md#-wolf-cluster-gly).

## Members

The **ClusResTypeResources** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResTypeResources** collection has these methods.



| Method                                                | Description                                                              |
|:------------------------------------------------------|:-------------------------------------------------------------------------|
| [**CreateItem**](clusrestyperesources-createitem.md) | Creates a new cluster resource and adds it to the collection.<br/> |
| [**DeleteItem**](clusrestyperesources-deleteitem.md) | Deletes a resource from the collection.<br/>                       |
| [**Refresh**](clusrestyperesources-refresh.md)       | Refreshes the data in the collection.<br/>                         |



 

### Properties

The **ClusResTypeResources** collection has these properties.



| Property                                               | Description                                                 |
|:-------------------------------------------------------|:------------------------------------------------------------|
| [**Count**](clusrestyperesources-count.md)<br/> | Returns the number of objects in the collection.<br/> |
| [**Item**](clusrestyperesources-item.md)<br/>   | Returns a single resource from the collection.<br/>   |



 

## Remarks

A [**ClusResPossibleOwnerNodes**](clusrespossibleownernodes-collection.md) collection:

-   Contains [**ClusResource**](clusresource-object.md) objects.
-   Is obtained from [**ClusResType.Resources**](clusrestype-resources.md).

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                 |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>     |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>     |
| IID<br/>                      | IID\_ISClusResTypeResources is defined as F2E60714-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Resource Type Management Objects](resource-type-management-objects.md)
</dt> </dl>

 

 





