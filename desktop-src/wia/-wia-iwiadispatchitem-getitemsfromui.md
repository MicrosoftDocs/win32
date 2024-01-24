---
description: The GetItemsFromUI method of the Item object displays a dialog box that allows a user to select images and audio to transfer from a device.
ms.assetid: 0ee9a248-20ed-4e1f-a8ce-615c4a6a2bce
title: Item.GetItemsFromUI method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Item.GetItemsFromUI
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# Item.GetItemsFromUI method

The **GetItemsFromUI** method of the [**Item**](-wia-item.md) object displays a dialog box that allows a user to select images and audio to transfer from a device.

## Syntax


```JScript
retVal = Item.GetItemsFromUI(
  Flags = 0,
  Intent = 0
)
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**WiaFlag**](-wia-wiaflag.md)**

<dt>



 (0)


</dt> <dd>

Default. \[in\] Specifies dialog box behavior. The valid values for this parameter are the same as for the *lFlags* parameter of the [**DeviceDlg**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiaitem-devicedlg) method.

</dd> </dl> </dd> <dt>

*Intent* \[in\]
</dt> <dd>

Type: **WiaIntent**

<dt>



 (0)


</dt> <dd>

Default. \[in\] Specifies what type of data the image is intended to represent. For a list of image intent values, see [**Image Intent Constants**](-wia-imageintentconstants.md).

</dd> </dl> </dd> </dl>

## Return value

Type: **ICollection**

This method returns a collection of [**Item**](-wia-item.md) objects that represent the items selected by the user. If no items are selected, the collection is empty.

## Remarks

For Microsoft Visual Basic applications, add a reference to "Windows Image Acquisition 1.01 Type Library".

This method applies only to devices (root items). The method returns a collection of [**Item**](-wia-item.md) objects that represent the images or audio clips selected by the user.

If no items are selected by the user, the method returns an empty collection.

## Examples

The following example demonstrates the use of the **GetItemsFromUI** method to allow a user to select images from a dialog box.


```JScript
<SCRIPT LANGUAGE="VBScript">
Dim objWia
Dim objDeviceInfoCollection
Dim objDeviceInfo
Dim objRootItem
Dim objSelectedItems
 
Set objWIA = CreateObject("Wia.Script")
 
Set objDeviceInfoCollection = objWia.Devices
 
For Each objDeviceInfo In objDeviceInfoCollection
    Set objRootItem = objWia.Create(objDeviceInfo)
    Set objSelectedItems = objRootItem.GetItemsFromUI(0, 0)
    ' Do something with selected items.
Next
</SCRIPT>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




