---
Description: Retrieves information regarding event classes.
ms.assetid: 33a87692-cacf-4a1c-974e-8d0e20295333
title: EventClassesForIID collection
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EventClassesForIID collection

Retrieves information regarding event classes.

The connection between publisher and subscriber(s) is managed by an [**EventClass**](/windows/win32/eventsys/nn-eventsys-ieventclass?branch=master) object, which is a COM+ component that contains the interfaces and methods used by a publisher to fire events.

This collection supports the [**Add**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-add?branch=master) and [**Remove**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-remove?branch=master) methods of the [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) object.

## Members

The **EventClassesForIID** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](/windows/win32/ComAdmin/?branch=master) object within the collection:

-   [Application](#application)
-   [Bitness](#bitness)
-   [CLSID](#clsid)
-   [Description](#description)
-   [IsPrivateComponent](#isprivatecomponent)
-   [ProgID](#progid)

### Application



|                |                                                          |
|----------------|----------------------------------------------------------|
| Description    | The GUID for the application containing the event class. |
| Access         | ReadOnly                                                 |
| Type           | String                                                   |
| Default        | N/A                                                      |
| Minimum system | Windows XP                                               |



 

### Bitness



|                |                                                                                                                                                                         |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Represents the binary bitness type of the event class. On systems that use 64-bit Windows, this property distinguishes between 64-bit components and 32-bit components. |
| Access         | ReadOnly                                                                                                                                                                |
| Type           | Long Possible values:COMAdmin32BitComponent (0x1)COMAdmin64BitComponent (0x2)                                                                                           |
| Default        | N/A                                                                                                                                                                     |
| Minimum system | Windows XP                                                                                                                                                              |



 

### CLSID



|                |                                                                                                                                                               |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The GUID for the event class. This property is returned when the [**Key**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_key?branch=master) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                      |
| Type           | String                                                                                                                                                        |
| Default        | N/A                                                                                                                                                           |
| Minimum system | Windows XP                                                                                                                                                    |



 

### Description



|                |                            |
|----------------|----------------------------|
| Description    | Describes the event class. |
| Access         | ReadOnly                   |
| Type           | String                     |
| Default        | ""                         |
| Minimum system | Windows XP                 |



 

### IsPrivateComponent



|                |                                                         |
|----------------|---------------------------------------------------------|
| Description    | Indicates whether the event class component is private. |
| Access         | ReadOnly                                                |
| Type           | Bool                                                    |
| Default        | False                                                   |
| Minimum system | Windows XP                                              |



 

### ProgID



|                |                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A friendly name used to identify the event class. This property is returned when the [**Name**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_name?branch=master) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                                            |
| Type           | String                                                                                                                                                                              |
| Default        | ""                                                                                                                                                                                  |
| Minimum system | Windows XP                                                                                                                                                                          |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



