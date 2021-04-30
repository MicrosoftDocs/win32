---
description: Specifies the applications contained within each partition.
ms.assetid: '264a35fd-ba71-4ae9-908a-24a72167c26b'
title: Partitions collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Partitions
api_type: 
- COM
api_location: 
---

# Partitions collection

Specifies the applications contained within each partition.

This collection supports the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **Partitions** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**Applications**](applications.md)
-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**RolesForPartition**](rolesforpartition.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [Changeable](#changeable)
-   [Deleteable](#deleteable)
-   [Description](#description)
-   [ID](#partitions-collection)
-   [Name](#name)

### Changeable



| Entry | Value |
|----------------|--------------------------------------------------|
| Description    | Determines whether this partition is changeable. |
| Access         | ReadWrite                                        |
| Type           | Bool                                             |
| Default        | True                                             |
| Minimum system | Windows Server 2003                              |



 

### Deleteable



| Entry | Value |
|----------------|---------------------------------------------------|
| Description    | Determines whether this partition can be deleted. |
| Access         | ReadWrite                                         |
| Type           | Bool                                              |
| Default        | True                                              |
| Minimum system | Windows Server 2003                               |



 

### Description



| Entry | Value |
|----------------|---------------------------------------------------------------------|
| Description    | This property represents the description identifying the partition. |
| Access         | ReadWrite                                                           |
| Type           | String                                                              |
| Default        | ""                                                                  |
| Minimum system | Windows Server 2003                                                 |



 

### ID



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A GUID representing the partition. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                          |
| Type           | String                                                                                                                                                             |
| Default        | <Generated>                                                                                                                                                  |
| Minimum system | Windows Server 2003                                                                                                                                                |



 

### Name



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Represents the partition name. Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | ReadWrite                                                                                                                                                                                                                              |
| Type           | String                                                                                                                                                                                                                                 |
| Default        | "New Partition"                                                                                                                                                                                                                        |
| Minimum system | Windows Server 2003                                                                                                                                                                                                                    |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
