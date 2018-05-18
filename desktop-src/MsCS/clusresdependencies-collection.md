---
title: ClusResDependencies collection
description: Provides access to the dependencies of a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '10695840-38ec-4614-8bbd-5772a53dea4b'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusResDependencies collection Failover Cluster", "ClusResDependencies collection Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusResDependencies
- ISClusResDependencies
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResDependencies collection

\[The **ClusResDependencies** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [dependencies](resource-dependencies.md) of a [resource](resources.md). Resources added to a **ClusResDependencies** collection become dependencies of the resource from which the collection was obtained.

## Members

The **ClusResDependencies** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResDependencies** collection has these methods.



| Method                                                 | Description                                                                                                 |
|:-------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**AddItem**](clusresdependencies-additem.md)         | Adds an existing [*cluster*](c-gly.md#-wolf-cluster-gly) resource to the dependency collection.<br/> |
| [**CreateItem**](clusresgroupresources-createitem.md) | Creates a new resource in the cluster and adds it to the dependency collection.<br/>                  |
| [**DeleteItem**](clusresgroupresources-deleteitem.md) | Removes a resource from the dependency collection and deletes the resource from the cluster.<br/>     |
| [**Refresh**](clusresdependencies-refresh.md)         | Refreshes the data in the collection.<br/>                                                            |
| [**RemoveItem**](clusresdependencies-removeitem.md)   | Removes a dependency from the collection.<br/>                                                        |



 

### Properties

The **ClusResDependencies** collection has these properties.



| Property                                              | Access type          | Description                                                      |
|:------------------------------------------------------|:---------------------|:-----------------------------------------------------------------|
| [**Count**](clusresdependencies-count.md)<br/> | Read-only<br/> | Returns the number of dependencies in the collection.<br/> |
| [**Item**](clusresgroupresources-item.md)<br/> | Read-only<br/> | Returns a single dependency from the collection.<br/>      |



 

## Remarks

A **ClusResDependencies** collection:

-   Contains [**ClusResource**](clusresource-object.md) objects.
-   Is obtained from [**ClusResource.Dependencies**](clusresource-dependencies.md).

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>      |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>    |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>    |
| IID<br/>                      | IID\_ISClusResDependencies is defined as F2E60704-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Resource Management Objects](resource-management-objects.md)
</dt> </dl>

 

 





