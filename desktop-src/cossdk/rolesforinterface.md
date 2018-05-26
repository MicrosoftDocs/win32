---
Description: Contains an object for each role assigned to the interface to which the collection is related. The roles must already be assigned at the application level.
ms.assetid: f5c1dc9a-13da-4504-a244-4ce8058240b8
title: RolesForInterface collection
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RolesForInterface collection

Contains an object for each role assigned to the interface to which the collection is related. The roles must already be assigned at the application level.

This collection supports the [**Add**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-add?branch=master) and [**Remove**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-remove?branch=master) methods of the [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) object.

## Members

The **RolesForInterface** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**InterfacesForComponent**](interfacesforcomponent.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](/windows/win32/ComAdmin/?branch=master) object within the collection:

-   [Name](#name)

### Name



|                |                                                                                                                                                                                                                                                                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The role name. Must already be a role assigned to the application (appearing in the Roles collection). Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Key**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_key?branch=master) or [**Name**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_name?branch=master) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                                                                                                                                                                                                           |
| Type           | String                                                                                                                                                                                                                                                                                                                                              |
| Default        | "New Role"                                                                                                                                                                                                                                                                                                                                          |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                                        |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



