---
title: ClusResTypePossibleOwnerNodes collection
description: Provides access to the possible owner nodes of a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: be22d5b1-8c61-40a5-883c-f49651ba623d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusResTypePossibleOwnerNodes collection Failover Cluster
- ClusResTypePossibleOwnerNodes collection Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusResTypePossibleOwnerNodes
- ISClusResTypePossibleOwnerNodes
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ClusResTypePossibleOwnerNodes collection

\[The **ClusResTypePossibleOwnerNodes** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [*possible owner*](https://www.bing.com/search?q=*possible owner*) [nodes](nodes.md) of a [resource type](resource-types.md).

## Members

The **ClusResTypePossibleOwnerNodes** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResTypePossibleOwnerNodes** collection has these methods.



| Method                                                   | Description                                      |
|:---------------------------------------------------------|:-------------------------------------------------|
| [**Refresh**](clusrestypepossibleownernodes-refresh.md) | Refreshes the data in the collection.<br/> |



 

### Properties

The **ClusResTypePossibleOwnerNodes** collection has these properties.



| Property                                                        | Description                                                 |
|:----------------------------------------------------------------|:------------------------------------------------------------|
| [**Count**](clusrestypepossibleownernodes-count.md)<br/> | Returns the number of objects in the collection.<br/> |
| [**Item**](clusrestypepossibleownernodes-item.md)<br/>   | Returns a single node from the collection.<br/>       |



 

## Remarks

A [**ClusResPossibleOwnerNodes**](clusrespossibleownernodes-collection.md) collection contains [**ClusNode**](clusnode-object.md) objects. It is obtained from [**ClusResType.PossibleOwnerNodes**](clusrestype-possibleownernodes.md).

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                          |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>                |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>              |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>              |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>              |
| IID<br/>                      | IID\_ISClusResTypePossibleOwnerNodes is defined as F2E60718-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Resource Type Management Objects](resource-type-management-objects.md)
</dt> </dl>

 

 





