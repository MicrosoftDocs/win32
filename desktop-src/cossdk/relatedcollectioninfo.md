---
Description: 'Retrieves information about other collections related to the collection from which it is called.'
ms.assetid: 'daea5b23-6a13-46f4-89c8-0d93b614311e'
title: RelatedCollectionInfo collection
---

# RelatedCollectionInfo collection

Retrieves information about other collections related to the collection from which it is called. The **RelatedCollectionInfo** collection is accessible from any [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object by using the [**GetCollection**](icatalogcollection-getcollection.md) method. The **RelatedCollectionInfo** collection contains one object for each collection that is accessible from the original collection. Related collections follow the Component Services administration tool collection hierarchy.

This collection does not support the [**Add**](icatalogcollection-add.md) and [**Remove**](icatalogcollection-remove.md) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **RelatedCollectionInfo** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**PropertyInfo**](propertyinfo.md)
-   **RelatedCollectionInfo**

You can navigate to this collection from every collection.

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [Name](#name)

### Name



|                |                                                                                                                                                                                                            |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The name of the related collection. This property is returned when the [**Key**](icatalogobject-key.md) or [**Name**](icatalogobject-name.md) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                                                                   |
| Type           | String                                                                                                                                                                                                     |
| Default        | None                                                                                                                                                                                                       |
| Minimum system | Windows 2000                                                                                                                                                                                               |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



