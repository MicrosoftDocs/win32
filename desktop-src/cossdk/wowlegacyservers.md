---
Description: 'Exposed properties for the WOWLegacyServers collection are intended to be identical to the LegacyServers collection except that the WOWLegacyServers collection is drawn from the 32-bit registry on 64-bit computers.'
ms.assetid: '72380276-214c-4f12-b575-deb975d846d3'
title: WOWLegacyServers collection
---

# WOWLegacyServers collection

Exposed properties for the **WOWLegacyServers** collection are intended to be identical to the [**LegacyServers**](legacyservers.md) collection except that the **WOWLegacyServers** collection is drawn from the 32-bit registry on 64-bit computers.

This collection does not support the [**Add**](icatalogcollection-add.md) and [**Remove**](icatalogcollection-remove.md) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **WOWLegacyServers** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [ClassName](#classname)
-   [CLSID](#clsid)
-   [InprocServer32](#inprocserver32)
-   [LocalServer32](#localserver32)
-   [ProgID](#progid)

### ClassName



|                |                        |
|----------------|------------------------|
| Description    | The name of the class. |
| Access         | ReadOnly               |
| Type           | String                 |
| Default        | N/A                    |
| Minimum system | Windows XP             |



 

### CLSID



|                |                                                                                                                                                           |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A GUID for the component. This property is returned when the [**Key**](icatalogobject-key.md) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                  |
| Type           | String                                                                                                                                                    |
| Default        | N/A                                                                                                                                                       |
| Minimum system | Windows XP                                                                                                                                                |



 

### InprocServer32



|                |                                  |
|----------------|----------------------------------|
| Description    | The file path for the component. |
| Access         | ReadOnly                         |
| Type           | String                           |
| Default        | N/A                              |
| Minimum system | Windows XP                       |



 

### LocalServer32



|                |                                                               |
|----------------|---------------------------------------------------------------|
| Description    | Specifies the full path to a 32-bit local server application. |
| Access         | ReadOnly                                                      |
| Type           | String                                                        |
| Default        | N/A                                                           |
| Minimum system | Windows XP                                                    |



 

### ProgID



|                |                                                                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A name identifying the component. This property is returned when the [**Name**](icatalogobject-name.md) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                            |
| Type           | String                                                                                                                                                              |
| Default        | N/A                                                                                                                                                                 |
| Minimum system | Windows XP                                                                                                                                                          |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



