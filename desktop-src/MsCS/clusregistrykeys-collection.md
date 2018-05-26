---
title: ClusRegistryKeys collection
description: Represents the list of registry keys that are checkpointed for a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 888f70d9-6562-4add-895d-604f22d75307
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusRegistryKeys collection Failover Cluster
- ClusRegistryKeys collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusRegistryKeys
- ISClusRegistryKeys
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ClusRegistryKeys collection

\[The **ClusRegistryKeys** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Represents the list of registry keys that are [checkpointed](checkpointing.md) for a [resource](resources.md).

## Members

The **ClusRegistryKeys** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusRegistryKeys** collection has these methods.



| Method                                            | Description                                                       |
|:--------------------------------------------------|:------------------------------------------------------------------|
| [**AddItem**](clusregistrykeys-additem.md)       | Adds an object to the **ClusRegistryKeys** collection.<br/> |
| [**Refresh**](clusregistrykeys-refresh.md)       | Refreshes the data in the collection.<br/>                  |
| [**RemoveItem**](clusregistrykeys-removeitem.md) | Deletes an object from the collection.<br/>                 |



 

### Properties

The **ClusRegistryKeys** collection has these properties.



| Property                                              | Access type          | Description                                                 |
|:------------------------------------------------------|:---------------------|:------------------------------------------------------------|
| [**Count**](clusregistrykeys-count.md)<br/>    | Read-only<br/> | Returns the number of objects in the collection.<br/> |
| [**Item**](clusresgroupresources-item.md)<br/> | Read-only<br/> | Returns a single object from the collection.<br/>     |



 

## Remarks

A **ClusRegistryKeys** collection:

-   Contains registry keys as strings.
-   Is obtained from [**ClusResource.RegistryKeys**](clusresource-registrykeys.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusRegistryKeys is defined as F2E6072A-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Property Management Objects](property-management-objects.md)
</dt> </dl>

 

 





