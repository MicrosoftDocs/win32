---
Description: Contains an object for each user in the role to which the collection is related.
ms.assetid: c6aebf7a-04d1-4c7c-a015-bc6fb4841c4a
title: UsersInPartitionRole collection
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UsersInPartitionRole collection

Contains an object for each user in the role to which the collection is related.

This collection supports the [**Add**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-add?branch=master) and [**Remove**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-remove?branch=master) methods of the [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) object.

## Members

The **UsersInPartitionRole** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**RolesForPartition**](rolesforpartition.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](/windows/win32/ComAdmin/?branch=master) object within the collection:

-   [User](#usersinpartitionrole-collection)

### User



|                |                                                                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The user name. This property is returned when the [**Key**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_key?branch=master) or [**Name**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_name?branch=master) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                                             |
| Type           | String                                                                                                                                                                                |
| Default        | "New User"                                                                                                                                                                            |
| Minimum system | Windows Server 2003                                                                                                                                                                   |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



