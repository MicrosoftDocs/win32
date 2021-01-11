---
description: Windows Image Acquisition (WIA) hardware devices are represented as hierarchical trees of Item objects. The root item in this tree represents the device itself, while child items represent images, folders, or scanning beds.
ms.assetid: 240557d6-665e-4879-8c6e-f564ca61e031
title: Item object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Item
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# Item object

Windows Image Acquisition (WIA) hardware devices are represented as hierarchical trees of **Item** objects. The root item in this tree represents the device itself, while child items represent images, folders, or scanning beds.

Use the **Item** object to transfer data to a file, to navigate the item tree for a particular device, or to retrieve information about an image or a device.

## Members

The **Item** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Item** object has these methods.



| Method                                                         | Description                                                                                                                                                                                                                                                                    |
|:---------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetItemsFromUI**](-wia-iwiadispatchitem-getitemsfromui.md) | The [**GetItemsFromUI**](-wia-iwiadispatchitem-getitemsfromui.md) method of the **Item** object displays a dialog box that allows a user to select images and audio to transfer from a device.<br/>                                                                     |
| [**GetPropById**](-wia-iwiadispatchitem-getpropbyid.md)       | The [**GetPropById**](-wia-iwiadispatchitem-getpropbyid.md) method of the **Item** object uses the ID of an item property to return its value.<br/>                                                                                                                     |
| [**TakePicture**](-wia-iwiadispatchitem-takepicture.md)       | The [**TakePicture**](-wia-iwiadispatchitem-takepicture.md) method of the **Item** object causes a digital camera device to take a picture and returns an **Item** object that represents the resulting image. This method applies only to digital camera devices.<br/> |
| [**Transfer**](-wia-iwiadispatchitem-transfer.md)             | The [**Transfer**](-wia-iwiadispatchitem-transfer.md) method of the **Item** object transfers data from a device to a file. This method applies only to device type items.<br/>                                                                                         |



 

### Properties

The **Item** object has these properties.



| Property                                                                    | Access type          | Description                                                                                                                                                                                                                                                 |
|:----------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Children**](-wia-iwiadispatchitem-children.md)<br/>               | Read-only<br/> | The [**Children**](-wia-iwiadispatchitem-children.md) property of the **Item** object retrieves a collection of **Item** objects. The items in this collection represent items that are direct children of this item in the hierarchical tree. <br/> |
| [**ConnectStatus**](-wia-iwiadispatchitem-connectstatus.md)<br/>     | Read-only<br/> | Retrieves the connection status of the device. This property applies only to items of type device (root items). Possible values are "connected", "disconnected", or **NULL** (if this property does not apply to the item). <br/>                     |
| [**FirmwareVersion**](-wia-iwiadispatchitem-firmwareversion.md)<br/> | Read-only<br/> | Retrieves the firmware version of the device. This property applies only to items of type device (root items). <br/>                                                                                                                                  |
| [**FullName**](-wia-iwiadispatchitem-fullname.md)<br/>               | Read-only<br/> | Retrieves the full name of the item as it appears in the UI. <br/>                                                                                                                                                                                    |
| [**Height**](-wia-iwiadispatchitem-height.md)<br/>                   | Read-only<br/> | The height, in pixels, of the item. <br/>                                                                                                                                                                                                             |
| [**ItemType**](-wia-iwiadispatchitem-itemtype.md)<br/>               | Read-only<br/> | The type of this item. <br/>                                                                                                                                                                                                                          |
| [**Name**](-wia-iwiadispatchitem-name.md)<br/>                       | Read-only<br/> | The name of the item as it appears in the UI. <br/>                                                                                                                                                                                                   |
| [**PictureHeight**](-wia-iwiadispatchitem-pictureheight.md)<br/>     | Read-only<br/> | The height, in pixels, of images produced by this digital camera. Applies only to digital cameras. <br/>                                                                                                                                              |
| [**PictureWidth**](-wia-iwiadispatchitem-picturewidth.md)<br/>       | Read-only<br/> | The width, in pixels, of images produced by this digital camera. Applies only to digital cameras. <br/>                                                                                                                                               |
| [**ThumbHeight**](-wia-iwiadispatchitem-thumbheight.md)<br/>         | Read-only<br/> | The height, in pixels, of the thumbnail image. This property returns -1 if this item does not support thumbnails. <br/>                                                                                                                               |
| [**Thumbnail**](-wia-iwiadispatchitem-thumbnail.md)<br/>             | Read-only<br/> | The path and filename of the thumbnail image. This property is **NULL** if the item does not support thumbnails, or if a path cannot be built. <br/>                                                                                                  |
| [**ThumbWidth**](-wia-iwiadispatchitem-thumbwidth.md)<br/>           | Read-only<br/> | The width, in pixels, of the thumbnail image. This property returns -1 if this item does not support thumbnails. <br/>                                                                                                                                |
| [**Time**](-wia-iwiadispatchitem-time.md)<br/>                       | Read-only<br/> | The current time. Applies only to devices. <br/>                                                                                                                                                                                                      |
| [**Width**](-wia-iwiadispatchitem-width.md)<br/>                     | Read-only<br/> | The width, in pixels, of the item. <br/>                                                                                                                                                                                                              |



 

## Remarks

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**TakePicture**](-wia-iwiadispatchitem-takepicture.md)

[**Create**](-wia-iwiadeviceinfo-create.md)

[**Create**](-wia-iwia-create.md)



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




