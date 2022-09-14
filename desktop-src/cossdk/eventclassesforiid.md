---
description: Retrieves information regarding event classes.
ms.assetid: 33a87692-cacf-4a1c-974e-8d0e20295333
title: EventClassesForIID collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EventClassesForIID
api_type: 
- COM
api_location: 
---

# EventClassesForIID collection

Retrieves information regarding event classes.

The connection between publisher and subscriber(s) is managed by an [**EventClass**](/windows/desktop/api/eventsys/nn-eventsys-ieventclass) object, which is a COM+ component that contains the interfaces and methods used by a publisher to fire events.

This collection supports the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **EventClassesForIID** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [Application](#application)
-   [Bitness](#bitness)
-   [CLSID](#clsid)
-   [Description](#description)
-   [IsPrivateComponent](#isprivatecomponent)
-   [ProgID](#progid)

### Application



| Entry | Value |
|----------------|----------------------------------------------------------|
| Description    | The GUID for the application containing the event class. |
| Access         | ReadOnly                                                 |
| Type           | String                                                   |
| Default        | N/A                                                      |
| Minimum system | Windows XP                                               |



 

### Bitness



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Represents the binary bitness type of the event class. On systems that use 64-bit Windows, this property distinguishes between 64-bit components and 32-bit components. |
| Access         | ReadOnly                                                                                                                                                                |
| Type           | Long Possible values:COMAdmin32BitComponent (0x1)COMAdmin64BitComponent (0x2)                                                                                           |
| Default        | N/A                                                                                                                                                                     |
| Minimum system | Windows XP                                                                                                                                                              |



 

### CLSID



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The GUID for the event class. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                      |
| Type           | String                                                                                                                                                        |
| Default        | N/A                                                                                                                                                           |
| Minimum system | Windows XP                                                                                                                                                    |



 

### Description



| Entry | Value |
|----------------|----------------------------|
| Description    | Describes the event class. |
| Access         | ReadOnly                   |
| Type           | String                     |
| Default        | ""                         |
| Minimum system | Windows XP                 |



 

### IsPrivateComponent



| Entry | Value |
|----------------|---------------------------------------------------------|
| Description    | Indicates whether the event class component is private. |
| Access         | ReadOnly                                                |
| Type           | Bool                                                    |
| Default        | False                                                   |
| Minimum system | Windows XP                                              |



 

### ProgID



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A friendly name used to identify the event class. This property is returned when the [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                                            |
| Type           | String                                                                                                                                                                              |
| Default        | ""                                                                                                                                                                                  |
| Minimum system | Windows XP                                                                                                                                                                          |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
