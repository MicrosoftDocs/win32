---
description: The RolesForPartition collection is always related to an object in the Partitions collection. It holds an object for each role assigned to the partition to which it is related.
ms.assetid: 56985f55-d6e8-4066-b6d5-21c62d4278ce
title: RolesForPartition collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RolesForPartition
api_type: 
- COM
api_location: 
---

# RolesForPartition collection

The **RolesForPartition** collection is always related to an object in the [**Partitions**](partitions.md) collection. It holds an object for each role assigned to the partition to which it is related.

This collection does not support the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **RolesForPartition** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**UsersInPartitionRole**](usersinpartitionrole.md)

You can navigate to this collection from the following collections:

-   [**Partitions**](partitions.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [Description](#description)
-   [Name](#name)

### Description



| Entry | Value |
|----------------|----------------------------|
| Description    | A description of the role. |
| Access         | ReadOnly                   |
| Type           | String                     |
| Default        | ""                         |
| Minimum system | Windows Server 2003        |



 

### Name



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The role name. Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) or [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                                                                                                                    |
| Type           | String                                                                                                                                                                                                                                                      |
| Default        | ""                                                                                                                                                                                                                                                          |
| Minimum system | Windows Server 2003                                                                                                                                                                                                                                         |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
