---
description: Contains an object for each partition user.
ms.assetid: baec56ae-be8a-42a7-90bc-1db7c5cd7fe2
title: PartitionUsers collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PartitionUsers
api_type: 
- COM
api_location: 
---

# PartitionUsers collection

Contains an object for each partition user.

This collection supports the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **PartitionUsers** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [AccountName](#accountname)
-   [DefaultPartitionID](#defaultpartitionid)

### AccountName



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Name of the partition user's account. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) or [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                                                                    |
| Type           | String                                                                                                                                                                                                       |
| Default        | "New User"                                                                                                                                                                                                   |
| Minimum system | Windows Server 2003                                                                                                                                                                                          |



 

### DefaultPartitionID



| Entry | Value |
|----------------|--------------------------------------------------------------------|
| Description    | The globally unique identifier for the base application partition. |
| Access         | ReadWrite                                                          |
| Type           | String                                                             |
| Default        | {41E90F3E-56C1-4633-81C3-6E8BAC8BDD70}                             |
| Minimum system | Windows Server 2003                                                |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
