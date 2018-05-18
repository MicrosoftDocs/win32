---
Description: 'Contains an object for each user in the role to which the collection is related.'
ms.assetid: 'e7d9e5e8-1927-42b2-bdd5-0c49a562c31f'
title: UsersInRole collection
---

# UsersInRole collection

Contains an object for each user in the role to which the collection is related.

This collection supports the [**Add**](icatalogcollection-add.md) and [**Remove**](icatalogcollection-remove.md) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **UsersInRole** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Roles**](roles.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [User](#usersinrole-collection)

### User



|                |                                                                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The user name. This property is returned when the [**Key**](icatalogobject-key.md) or [**Name**](icatalogobject-name.md) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                                             |
| Type           | String                                                                                                                                                                                |
| Default        | "New User"                                                                                                                                                                            |
| Minimum system | Windows 2000                                                                                                                                                                          |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



