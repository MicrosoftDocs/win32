---
title: ClusResPossibleOwnerNodes collection
description: Provides access to a resource's list of possible owner \ 32; nodes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a3269288-f32f-45d5-8fd4-4e6fb257c1be'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusResPossibleOwnerNodes collection Failover Cluster", "ClusResPossibleOwnerNodes collection Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusResPossibleOwnerNodes
- ISClusResPossibleOwnerNodes
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResPossibleOwnerNodes collection

\[The **ClusResPossibleOwnerNodes** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to a resource's list of [*possible owner*](p-gly.md#-wolf-possible-owner-gly) [nodes](nodes.md).

## Members

The **ClusResPossibleOwnerNodes** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResPossibleOwnerNodes** collection has these methods.



| Method                                                           | Description                                                                           |
|:-----------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**AddItem**](clusrespossibleownernodes-additem.md)             | Adds a node to the list of possible owners of a [resource](resources.md).<br/> |
| [**Refresh**](clusrespossibleownernodes-refresh.md)             | Refreshes the data in the collection.<br/>                                      |
| [**RemoveItem**](clusresgrouppreferredownernodes-removeitem.md) | Removes a node from the collection.<br/>                                        |



 

### Properties

The **ClusResPossibleOwnerNodes** collection has these properties.



| Property                                                                | Description                                                                      |
|:------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**Count**](clusrespossibleownernodes-count.md)<br/>             | Returns the number of nodes in the collection.<br/>                        |
| [**Item**](clusrespossibleownernodes-item.md)<br/>               | Returns a single node from the collection.<br/>                            |
| [**Modified**](clusresgrouppreferredownernodes-modified.md)<br/> | Reports whether the collection has been modified since instantiation.<br/> |



 

## Remarks

A **ClusResPossibleOwnerNodes** collection:

-   Contains [**ClusNode**](clusnode-object.md) objects.
-   Is obtained from [**ClusResource.PossibleOwnerNodes**](clusresource-possibleownernodes.md).

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                      |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>            |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>          |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>          |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>          |
| IID<br/>                      | IID\_ISClusResPossibleOwnerNodes is defined as F2E6070E-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Resource Management Objects](resource-management-objects.md)
</dt> </dl>

 

 





