---
Description: Retrieves information regarding running applications.
ms.assetid: 148e42aa-e99e-4fa2-8b74-a7ebf82b99d0
title: ApplicationInstances collection
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ApplicationInstances collection

Retrieves information regarding running applications.

This collection supports the [**Add**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-add?branch=master) and [**Remove**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-remove?branch=master) methods of the [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) object.

## Members

The **ApplicationInstances** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Applications**](applications.md)
-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](/windows/win32/ComAdmin/?branch=master) object within the collection:

-   [Application](#applicationinstances-collection)
-   [HasRecycled](#hasrecycled)
-   [InstanceID](#instanceid)
-   [IsPaused](#ispaused)
-   [PartitionID](#partitionid)
-   [ProcessID](#processid)

### Application



|                |                                     |
|----------------|-------------------------------------|
| Description    | The ID for the running application. |
| Access         | ReadOnly                            |
| Type           | String                              |
| Default        | N/A                                 |
| Minimum system | Windows XP                          |



 

### HasRecycled



|                |                                                               |
|----------------|---------------------------------------------------------------|
| Description    | Indicates whether the application instance has been recycled. |
| Access         | ReadOnly                                                      |
| Type           | Bool                                                          |
| Default        | False                                                         |
| Minimum system | Windows XP                                                    |



 

### InstanceID



|                |                                                                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The globally unique identifier for the application instance. This property is returned when the [**Key**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_key?branch=master) or [**Name**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_name?branch=master) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                                                                                            |
| Type           | String                                                                                                                                                                                                                              |
| Default        | N/A                                                                                                                                                                                                                                 |
| Minimum system | Windows XP                                                                                                                                                                                                                          |



 

### IsPaused



|                |                                                                 |
|----------------|-----------------------------------------------------------------|
| Description    | Indicates whether the application instance is currently paused. |
| Access         | ReadOnly                                                        |
| Type           | Bool                                                            |
| Default        | False                                                           |
| Minimum system | Windows XP                                                      |



 

### PartitionID



|                |                                                 |
|----------------|-------------------------------------------------|
| Description    | The partition ID that the application is using. |
| Access         | ReadOnly                                        |
| Type           | String                                          |
| Default        | N/A                                             |
| Minimum system | Windows XP                                      |



 

### ProcessID



|                |                                             |
|----------------|---------------------------------------------|
| Description    | The process ID of the application instance. |
| Access         | ReadOnly                                    |
| Type           | String                                      |
| Default        | N/A                                         |
| Minimum system | Windows XP                                  |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



