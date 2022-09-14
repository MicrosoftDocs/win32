---
description: The Children property of the Item object retrieves a collection of Item objects. The items in this collection represent items that are direct children of this item in the hierarchical tree. Read-only.
ms.assetid: 94ad3385-9ce9-4a44-87bb-1d7170c8d45c
title: Item.Children property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Item.Children
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# Item.Children property

The **Children** property of the [**Item**](-wia-item.md) object retrieves a collection of **Item** objects. The items in this collection represent items that are direct children of this item in the hierarchical tree. Read-only.

This property is read-only.

## Syntax


```JScript
propVal = Item.Children
```



## Property value

Variable that receives the objects.

## Remarks

Use this property to navigate the hierarchical tree of [**Item**](-wia-item.md) objects that represent a device, the folders and the files that reside on the device.

The **Children** property is a collection of [**Item**](-wia-item.md) objects only from the level directly beneath this **Item** object in the tree. To navigate further levels down the tree, use this property recursively.

If the item cannot or does not have any child items, this property returns an empty collection.

> [!Note]  
> This collection is 0-based.

 

## Examples

The following example demonstrates the use of the **Children** property to retrieve and enumerate a collection of the child items of a device. If the device is a digital camera, the collection typically contains folder and image items. If the device is a scanner, the collection typically contains items that represent scanning beds.


```JScript
<SCRIPT LANGUAGE="VBScript">
Dim objWia
Dim objDeviceInfoCollection
Dim objDeviceInfo
Dim objRootItem
Dim objItemCollection
Dim objItem
 
Set objWIA = CreateObject("Wia.Script")
 
Set objDeviceInfoCollection = objWia.Devices
 
For Each objDeviceInfo In objDeviceInfoCollection
    Set objRootItem = objWia.Create(objDeviceInfo)
    objItemCollection = objRootItem.Children
    For Each objItem In objItemCollection
        ' Do something with the child item
    Next
Next
</SCRIPT>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




