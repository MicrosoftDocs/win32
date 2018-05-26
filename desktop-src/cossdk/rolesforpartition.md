---
Description: The RolesForPartition collection is always related to an object in the Partitions collection. It holds an object for each role assigned to the partition to which it is related.
ms.assetid: 56985f55-d6e8-4066-b6d5-21c62d4278ce
title: RolesForPartition collection
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RolesForPartition collection

The **RolesForPartition** collection is always related to an object in the [**Partitions**](partitions.md) collection. It holds an object for each role assigned to the partition to which it is related.

This collection does not support the [**Add**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-add?branch=master) and [**Remove**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-remove?branch=master) methods of the [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) object.

## Members

The **RolesForPartition** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**UsersInPartitionRole**](usersinpartitionrole.md)

You can navigate to this collection from the following collections:

-   [**Partitions**](partitions.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](/windows/win32/ComAdmin/?branch=master) object within the collection:

-   [Description](#description)
-   [Name](#name)

### Description



|                |                            |
|----------------|----------------------------|
| Description    | A description of the role. |
| Access         | ReadOnly                   |
| Type           | String                     |
| Default        | ""                         |
| Minimum system | Windows Server 2003        |



 

### Name



|                |                                                                                                                                                                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The role name. Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Key**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_key?branch=master) or [**Name**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_name?branch=master) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                                                                                                                    |
| Type           | String                                                                                                                                                                                                                                                      |
| Default        | ""                                                                                                                                                                                                                                                          |
| Minimum system | Windows Server 2003                                                                                                                                                                                                                                         |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



