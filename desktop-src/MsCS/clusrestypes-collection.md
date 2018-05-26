---
title: ClusResTypes collection
description: Provides access to the resource types in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 614d3ed6-255f-46ed-9354-7a73a21cac87
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusResTypes collection Failover Cluster
- ClusResTypes collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusResTypes
- ISClusResTypes
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ClusResTypes collection

\[The **ClusResTypes** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [resource types](resource-types.md) in a [*cluster*](c-gly.md#-wolf-cluster-gly).

## Members

The **ClusResTypes** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResTypes** collection has these methods.



| Method                                        | Description                                            |
|:----------------------------------------------|:-------------------------------------------------------|
| [**CreateItem**](clusrestypes-createitem.md) | Creates a new resource type in the cluster.<br/> |
| [**DeleteItem**](clusrestypes-deleteitem.md) | Deletes a resource type from the cluster.<br/>   |
| [**Refresh**](clusrestypes-refresh.md)       | Refreshes the data in the collection.<br/>       |



 

### Properties

The **ClusResTypes** collection has these properties.



| Property                                       | Description                                                    |
|:-----------------------------------------------|:---------------------------------------------------------------|
| [**Count**](clusrestypes-count.md)<br/> | Returns the number of objects in the collection.<br/>    |
| [**Item**](clusrestypes-item.md)<br/>   | Returns a single resource type from the collection.<br/> |



 

## Remarks

A **ClusResTypes** collection:

-   Contains [**ClusResType**](clusrestype-object.md) objects.
-   Is obtained from [**Cluster.ResourceTypes**](cluster-resourcetypes.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResTypes is defined as F2E60712-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[Cluster Management Objects](cluster-management-objects.md)
</dt> </dl>

 

 





