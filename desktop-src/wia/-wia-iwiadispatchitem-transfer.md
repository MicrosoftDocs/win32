---
description: The Transfer method of the Item object transfers data from a device to a file. This method applies only to device type items.
ms.assetid: ed9696da-bd94-4063-80c2-311a7a441b10
title: Item.Transfer method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Item.Transfer
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# Item.Transfer method

The **Transfer** method of the [**Item**](-wia-item.md) object transfers data from a device to a file. This method applies only to device type items.

## Syntax


```JScript
Item.Transfer(
  Filename,
  AsyncTransfer = VARIANT_BOOL
)
```



## Parameters

<dl> <dt>

*Filename* \[in\]
</dt> <dd>

Type: **BSTR**

Specifies the name of the file to which the data is transferred.

</dd> <dt>

*AsyncTransfer* \[in\]
</dt> <dd>

Type: **VARIANT\_BOOL**

A Boolean value that specifies whether the transfer should be run as an asynchronous call.

<dt>



 (VARIANT\_BOOL)


</dt> <dd>

Default. Set this value to **true** if the call should be asynchronous (see **Remarks**).

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method applies only to file type items. The method checks that the item supports this method before it attempts to complete the data transfer.

Use "clipboard" as the *Filename* parameter to transfer an item to the clipboard.

Set the *AsyncTransfer* value to **false** for transfers within any application or script that runs in an environment that terminates a process at the end of a script, such as Windows Script Host (WSH). Otherwise, the script may end, and the process terminate, before the transfer completes.

The **Transfer** method has no return value. Upon completion of a transfer, this method sends an [**OnTransferComplete**](-wia--iwiaevents-ontransfercomplete.md) event to the script or application.

## Examples

The following example demonstrates the use of the **Transfer** method to transfer data from a device.


```JScript
<SCRIPT LANGUAGE="VBScript">
Dim objWia
Dim objDeviceInfoCollection
Dim objDeviceInfo
Dim objRootItem
Dim objSelectedItems
Dim objItem
 
Set objWIA = CreateObject("Wia.Script")
 
Set objDeviceInfoCollection = objWia.Devices
 
For Each objDeviceInfo In objDeviceInfoCollection
    Set objRootItem = objWia.Create(objDeviceInfo)
    Set objSelectedItems = objRootItem.GetItemsFromUI(0, 0)
    For Each objItem In objSelectedItems
        objItem.Transfer("c:\Folder\Filename.bmp")
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



 

 




