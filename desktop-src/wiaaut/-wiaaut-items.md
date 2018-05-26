---
title: Items object
description: Contains a collection of Item objects. See the Items (Device) property or Items (Item) property for details on accessing the Items object.
ms.assetid: 95b92f9b-00f7-436d-acd6-f18b6b69ae29
keywords:
- Items object WIA Automation
- Items object WIA Automation , described
topic_type:
- apiref
api_name:
- Items
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Items object

Contains a collection of [**Item**](-wiaaut-item.md) objects. See the [**Items (Device)**](-wiaaut-idevice-items.md) property or [**Items (Item)**](-wiaaut-iitem-items.md) property for details on accessing the **Items** object.

## Members

The **Items** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Items** object has these methods.



| Method                                          | Description                                                     |
|:------------------------------------------------|:----------------------------------------------------------------|
| [**Add (Items)**](-wiaaut-iitems-add.md)       | Adds a new [**Item**](-wiaaut-item.md).<br/>             |
| [**Remove (Items)**](-wiaaut-iitems-remove.md) | Removes the designated [**Item**](-wiaaut-item.md).<br/> |



 

### Properties

The **Items** object has these properties.



| Property                                                 | Access type          | Description                                                             |
|:---------------------------------------------------------|:---------------------|:------------------------------------------------------------------------|
| [**Count (Items)**](-wiaaut-iitems-count.md)<br/> | Read-only<br/> | Retrieves the number of members in the **Items** collection.<br/> |
| [**Item (Items)**](-wiaaut-iitems-item.md)<br/>   | Read-only<br/> | Retrieves the specified item in the collection by position.<br/>  |



 

## Remarks

Note that the **Items** of a [**Device**](-wiaaut-device.md) or [**Item**](-wiaaut-item.md) object can change, so be careful not to assume that the [**Count (Items)**](-wiaaut-iitems-count.md) or order of a given collection will not change.

For example code, see [Determine the Number of Items Returned by ShowSelectItems](-wiaaut-shared-samples.md#determine-the-number-of-items-returned-by-showselectitems) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Items (Item)**](-wiaaut-iitem-items.md)

[**Items (Device)**](-wiaaut-idevice-items.md)

[**ShowSelectItems**](-wiaaut-icommondialog-showselectitems.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**ShowSelectItems**](-wiaaut-icommondialog-showselectitems.md)
</dt> <dt>

[**Items (Device)**](-wiaaut-idevice-items.md)
</dt> <dt>

[**Items (Item)**](-wiaaut-iitem-items.md)
</dt> </dl>

 

 





