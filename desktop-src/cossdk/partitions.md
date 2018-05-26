---
Description: Specifies the applications contained within each partition.
ms.assetid: fd22a64c-f2d8-48af-86e1-985e21b0f8fa
title: Partitions collection
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Partitions collection

Specifies the applications contained within each partition.

This collection supports the [**Add**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-add?branch=master) and [**Remove**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-remove?branch=master) methods of the [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) object.

## Members

The **Partitions** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**Applications**](applications.md)
-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**RolesForPartition**](rolesforpartition.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](/windows/win32/ComAdmin/?branch=master) object within the collection:

-   [Changeable](#changeable)
-   [Deleteable](#deleteable)
-   [Description](#description)
-   [ID](#partitions-collection)
-   [Name](#name)

### Changeable



|                |                                                  |
|----------------|--------------------------------------------------|
| Description    | Determines whether this partition is changeable. |
| Access         | ReadWrite                                        |
| Type           | Bool                                             |
| Default        | True                                             |
| Minimum system | Windows Server 2003                              |



 

### Deleteable



|                |                                                   |
|----------------|---------------------------------------------------|
| Description    | Determines whether this partition can be deleted. |
| Access         | ReadWrite                                         |
| Type           | Bool                                              |
| Default        | True                                              |
| Minimum system | Windows Server 2003                               |



 

### Description



|                |                                                                     |
|----------------|---------------------------------------------------------------------|
| Description    | This property represents the description identifying the partition. |
| Access         | ReadWrite                                                           |
| Type           | String                                                              |
| Default        | ""                                                                  |
| Minimum system | Windows Server 2003                                                 |



 

### ID



|                |                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A GUID representing the partition. This property is returned when the [**Key**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_key?branch=master) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                          |
| Type           | String                                                                                                                                                             |
| Default        | &lt;Generated&gt;                                                                                                                                                  |
| Minimum system | Windows Server 2003                                                                                                                                                |



 

### Name



|                |                                                                                                                                                                                                                                        |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Represents the partition name. Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Name**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_name?branch=master) property method is called on an object of this collection. |
| Access         | ReadWrite                                                                                                                                                                                                                              |
| Type           | String                                                                                                                                                                                                                                 |
| Default        | "New Partition"                                                                                                                                                                                                                        |
| Minimum system | Windows Server 2003                                                                                                                                                                                                                    |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



