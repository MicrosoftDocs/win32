---
Description: Contains an object for each user in the role to which the collection is related.
ms.assetid: c6aebf7a-04d1-4c7c-a015-bc6fb4841c4a
title: UsersInPartitionRole collection
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# UsersInPartitionRole collection

Contains an object for each user in the role to which the collection is related.

This collection supports the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](/windows/desktop/api/ComAdmin/) object.

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

The following properties are supported by the [**COMAdminCatalogObject**](/windows/desktop/api/ComAdmin/) object within the collection:

-   [User](#usersinpartitionrole-collection)

### User



|                |                                                                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The user name. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) or [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                                             |
| Type           | String                                                                                                                                                                                |
| Default        | "New User"                                                                                                                                                                            |
| Minimum system | Windows Server 2003                                                                                                                                                                   |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



