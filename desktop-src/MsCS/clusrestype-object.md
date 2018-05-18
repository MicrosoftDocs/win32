---
title: ClusResType object
description: Enables operations on a resource type, its properties, and related objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e4ad6364-f318-47f9-a276-d99c91ffbbb5'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusResType object Failover Cluster", "ClusResType object Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusResType
- ISClusResType
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResType object

\[The **ClusResType** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Enables operations on a [resource type](resource-types.md), its properties, and related objects.

## Members

The **ClusResType** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResType** object has these methods.



| Method                                               | Description                                                                                                                                                    |
|:-----------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AvailableDisks**](clusrestype-availabledisks.md) | Returns a [**ClusDisks**](clusdisks-collection.md) collection representing the [Physical Disks](physical-disk.md) available to the resource type.<br/> |
| [**Delete**](clusrestype-delete.md)                 | Deletes the resource type.<br/>                                                                                                                          |



 

### Properties

The **ClusResType** object has these properties.



| Property                                                                  | Description                                                                                                                                                                                                                      |
|:--------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Cluster**](clusrestype-cluster.md)<br/>                         | Returns the [*cluster*](c-gly.md#-wolf-cluster-gly) associated with the resource type.<br/>                                                                                                                               |
| [**CommonProperties**](clusrestype-commonproperties.md)<br/>       | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the resource type's read/write [common properties](common-properties.md).<br/>                                                        |
| [**CommonROProperties**](clusrestype-commonroproperties.md)<br/>   | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the resource type's read-only [common properties](common-properties.md).<br/>                                                         |
| [**PossibleOwnerNodes**](clusrestype-possibleownernodes.md)<br/>   | Returns a [**ClusResTypePossibleOwnerNodes**](clusrestypepossibleownernodes-collection.md) collection containing the [*possible owner*](p-gly.md#-wolf-possible-owner-gly) [nodes](nodes.md) of the resource type.<br/> |
| [**PrivateProperties**](clusrestype-privateproperties.md)<br/>     | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the resource type's read/write [private properties](private-properties.md).<br/>                                                      |
| [**PrivateROProperties**](clusrestype-privateroproperties.md)<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the resource type's read-only private properties.<br/>                                                                                 |
| [**Resources**](clusrestype-resources.md)<br/>                     | Returns all resources of a given type that are present in the cluster.<br/>                                                                                                                                                |



 

## Remarks

A **ClusResType** object:

-   Is obtained from [**ClusResTypes**](clusrestypes-collection.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResType is defined as F2E60710-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[Resource Type Management Objects](resource-type-management-objects.md)
</dt> </dl>

 

 





