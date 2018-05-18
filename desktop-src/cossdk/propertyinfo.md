---
Description: 'Retrieves information about the properties that a specified collection supports.'
ms.assetid: '5e3963c0-6769-4b5b-8636-2d8c98a8776b'
title: PropertyInfo collection
---

# PropertyInfo collection

Retrieves information about the properties that a specified collection supports. The **PropertyInfo** collection is accessible from any [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object by using the [**GetCollection**](icatalogcollection-getcollection.md) method. The **PropertyInfo** collection contains one object for each property that is supported by the original collection.

## Members

The **PropertyInfo** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   **PropertyInfo**
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from every collection.

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [Name](#name)

### Name



|                |                                                                                                                                                                                                  |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The name of the property. This property is returned when the [**Key**](icatalogobject-key.md) or [**Name**](icatalogobject-name.md) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                                                         |
| Type           | String                                                                                                                                                                                           |
| Default        | None                                                                                                                                                                                             |
| Minimum system | Windows 2000                                                                                                                                                                                     |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



