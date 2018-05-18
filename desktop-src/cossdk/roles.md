---
Description: 'The Roles collection is always related to an object in the Applications collection. It holds an object for each role assigned to the application to which it is related.'
ms.assetid: 'a7395d48-0193-420f-92ca-b0427ba9d496'
title: Roles collection
---

# Roles collection

The **Roles** collection is always related to an object in the [**Applications**](applications.md) collection. It holds an object for each role assigned to the application to which it is related.

This collection supports the [**Add**](icatalogcollection-add.md) and [**Remove**](icatalogcollection-remove.md) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **Roles** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**UsersInRole**](usersinrole.md)

You can navigate to this collection from the following collections:

-   [**Applications**](applications.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [Description](#description)
-   [Name](#name)

### Description



|                |                            |
|----------------|----------------------------|
| Description    | A description of the role. |
| Access         | ReadWrite                  |
| Type           | String                     |
| Default        | ""                         |
| Minimum system | Windows 2000               |



 

### Name



|                |                                                                                                                                                                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The role name. Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Key**](icatalogobject-key.md) or [**Name**](icatalogobject-name.md) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                                                                                                                   |
| Type           | String                                                                                                                                                                                                                                                      |
| Default        | "New Role"                                                                                                                                                                                                                                                  |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



