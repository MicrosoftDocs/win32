---
title: ClusProperties collection
description: Provides access to the properties of a cluster object, allowing individual property values to be changed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b117b0eb-e188-4514-8e11-9acca1303e8f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusProperties collection Failover Cluster", "ClusProperties collection Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusProperties
- ISClusProperties
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusProperties collection

\[The **ClusProperties** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the properties of a [cluster object](cluster-objects.md), allowing individual property values to be changed.

## Members

The **ClusProperties** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#clusproperties-collection)

### Methods

The **ClusProperties** collection has these methods.



| Method                                                    | Description                                                                                                     |
|:----------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
| [**CreateItem**](clusproperties-createitem.md)           | Creates a new [**ClusProperty**](clusproperty-object.md) object and adds it to the collection.<br/>      |
| [**Refresh**](clusproperties-refresh.md)                 | Updates the collection with current property data from the [cluster database](cluster-database.md).<br/> |
| [**SaveChanges**](clusproperties-savechanges.md)         | Saves all property data in the collection to the cluster database.<br/>                                   |
| [**UseDefaultValue**](clusproperties-usedefaultvalue.md) | Deletes a property from the collection.<br/>                                                              |



 

### Properties

The **ClusProperties** collection has these properties.



| Property                                               | Access type          | Description                                                                                                                                                                                                                  |
|:-------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Common**](clusproperties-common.md)<br/>     | Read-only<br/> | Indicates whether the properties in the collection are [common properties](common-properties.md).<br/>                                                                                                                |
| [**Count**](clusproperties-count.md)<br/>       | Read-only<br/> | Returns the number of properties in the collection.<br/>                                                                                                                                                               |
| [**Item**](clusproperties-item.md)<br/>         | Read-only<br/> | Returns a single property from the collection.<br/>                                                                                                                                                                    |
| [**Modified**](clusproperties-modified.md)<br/> | Read-only<br/> | Indicates whether any properties in the collection have been added, removed, or modified since the last [**Refresh**](clusproperties-refresh.md) or [**SaveChanges**](clusproperties-savechanges.md) operation.<br/> |
| [**Private**](clusproperties-private.md)<br/>   | Read-only<br/> | Indicates whether the properties in the collection are [private properties](private-properties.md).<br/>                                                                                                              |
| [**ReadOnly**](clusproperties-readonly.md)<br/> | Read-only<br/> | Indicates whether the properties in the collection are [read-only properties](read-only-properties.md).<br/>                                                                                                          |



 

## Remarks

A **ClusProperties** collection is similar to a [property list](property-lists.md) in that the data in the collection is a local copy of real data stored in the cluster database. When an instance of the **ClusProperties** collection is created, it receives a snapshot of the stored data. Changes to the **ClusProperties** collection do not take effect in the [*cluster*](c-gly.md#-wolf-cluster-gly) until the [**SaveChanges**](clusproperties-savechanges.md) method is invoked. Similarly, changes to the cluster database are not reflected in the collection until the [**Refresh**](clusproperties-refresh.md) method is called.

A **ClusProperties** collection:

-   Contains [**ClusProperty**](clusproperty-object.md) objects.
-   Can be obtained from any of the following objects.

    [**ClusNetwork**](clusnetwork-object.md)

    [**ClusNetInterface**](clusnetinterface-object.md)

    [**ClusNode**](clusnode-object.md)

    [**ClusResGroup**](clusresgroup-object.md)

    [**ClusResource**](clusresource-object.md)

    [**ClusResType**](clusrestype-object.md)

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusProperties is defined as F2E60700-2631-11D1-89F1-00A0C90D061E<br/>   |



## See also

<dl> <dt>

[Property Management Objects](property-management-objects.md)
</dt> </dl>

 

 





