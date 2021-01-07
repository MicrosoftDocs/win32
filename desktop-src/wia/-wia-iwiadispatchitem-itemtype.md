---
description: The type of this item. Read-only.
ms.assetid: 6c613a08-41aa-4242-80c0-75e1981a676f
title: Item.ItemType property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Item.ItemType
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# Item.ItemType property

The type of this item. Read-only.

This property is read-only.

## Syntax


```JScript
propVal = Item.ItemType
```



## Property value

The following values are possible:



| Value  | Description                                     |
|--------|-------------------------------------------------|
| device | The item is a WIA hardware device.              |
| folder | The item is a folder that contains other items. |
| file   | The item is an image or audio file.             |
| audio  | The item is an audio clip.                      |
| image  | The item is an image.                           |



 

## Remarks

An item can have more than one type. For example, every image is of both "image" and "file" types. **ItemType** returns a string that includes all valid types for the item, separated by semicolons. For example, "image;file". There are no spaces in this string, and there is not a semicolon at the end.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




