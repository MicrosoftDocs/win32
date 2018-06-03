---
title: Item object
description: Contains an item on an imaging Device. See the Items (Device) property or Items (Item) property for details on accessing Item objects.
ms.assetid: 194d77ad-195d-4512-b1ba-9681cb148782
keywords:
- Item object WIA Automation
- Item object WIA Automation , described
topic_type:
- apiref
api_name:
- Item
api_location:
- Wiaaut.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Item object

Contains an item on an imaging [**Device**](-wiaaut-device.md). See the [**Items (Device)**](-wiaaut-idevice-items.md) property or [**Items (Item)**](-wiaaut-iitem-items.md) property for details on accessing **Item** objects.

## Members

The **Item** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Item** object has these methods.



| Method                                                        | Description                                                                                   |
|:--------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| [**ExecuteCommand (Item)**](-wiaaut-iitem-executecommand.md) | Issues the command specified by *CommandID*.<br/>                                       |
| [**Transfer**](-wiaaut-iitem-transfer.md)                    | Retrieves an [**ImageFile**](-wiaaut-imagefile.md) object from an imaging device.<br/> |



 

### Properties

The **Item** object has these properties.



| Property                                                         | Access type          | Description                                                                                                                               |
|:-----------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| [**Commands (Item)**](-wiaaut-iitem-commands.md)<br/>     | Read-only<br/> | Retrieves a collection of all commands for this **Item** object.<br/>                                                               |
| [**Formats (Item)**](-wiaaut-iitem-formats.md)<br/>       | Read-only<br/> | Retrieves a collection of all supported format types for this **Item**.<br/>                                                        |
| [**ItemID**](-wiaaut-iitem-itemid.md)<br/>                | Read-only<br/> | Retrieves the ItemID for this **Item**.<br/>                                                                                        |
| [**Items (Item)**](-wiaaut-iitem-items.md)<br/>           | Read-only<br/> | Retrieves a collection of all child items for this item<br/>                                                                        |
| [**Properties (Item)**](-wiaaut-iitem-properties.md)<br/> | Read-only<br/> | Retrieves a collection of all properties for this **Item**.<br/>                                                                    |
| [**WiaItem (Item)**](-wiaaut-iitem-wiaitem.md)<br/>       | Read-only<br/> | Retrieves the underlying [IWiaItem](http://msdn.microsoft.com/library/ms630113(VS.85).aspx) interface for this **Item**.<br/> |



 

## Remarks

Note that the imaging item that the **Item** object represents is independent of the **Item** object. A user can delete an imaging item while your application is using it. Accessing an **Item** object's properties or methods after this occurs can result in errors.

For example code, see [Enumerate Root Level Items and Display Their Names](https://www.bing.com/search?q=Enumerate Root Level Items and Display Their Names) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**ExecuteCommand (Item)**](-wiaaut-iitem-executecommand.md)

[**Item (Items)**](-wiaaut-iitems-item.md)

[**GetItem**](-wiaaut-idevice-getitem.md)

[**ExecuteCommand (Device)**](-wiaaut-idevice-executecommand.md)



 

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

[**ShowItemProperties**](-wiaaut-icommondialog-showitemproperties.md)
</dt> <dt>

[**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md)
</dt> <dt>

[**ExecuteCommand (Device)**](-wiaaut-idevice-executecommand.md)
</dt> <dt>

[**GetItem**](-wiaaut-idevice-getitem.md)
</dt> <dt>

[**ExecuteCommand (Item)**](-wiaaut-iitem-executecommand.md)
</dt> <dt>

[**Item (Items)**](-wiaaut-iitems-item.md)
</dt> </dl>

 

 





