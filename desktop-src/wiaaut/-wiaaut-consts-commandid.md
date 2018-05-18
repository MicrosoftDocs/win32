---
title: CommandID Constants
description: Specifies common Device and Item commands as String versions of GUIDs.
ms.assetid: '48f0155c-276f-4ffd-bf42-33ee184d08e5'
topic_type:
- apiref
api_name:
- wiaCommandSynchronize
- wiaCommandTakePicture
- wiaCommandDeleteAllItems
- wiaCommandChangeDocument
- wiaCommandUnloadDocument
api_location:
- Wiaaut.h
api_type:
- HeaderDef
---

# CommandID Constants

Specifies common [**Device**](-wiaaut-device.md) and [**Item**](-wiaaut-item.md) commands as **String** versions of GUIDs.



| Constant/value                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                          |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="wiaCommandSynchronize"></span><span id="wiacommandsynchronize"></span><span id="WIACOMMANDSYNCHRONIZE"></span><dl> <dt>**wiaCommandSynchronize**</dt> <dt>{9B26B7B2-ACAD-11D2-A093-00C04F72DC3C}</dt> </dl>             | CommandID for Synchronize. Causes the device driver to synchronize cached items with the hardware device.<br/>                                                 |
| <span id="wiaCommandTakePicture"></span><span id="wiacommandtakepicture"></span><span id="WIACOMMANDTAKEPICTURE"></span><dl> <dt>**wiaCommandTakePicture**</dt> <dt>{AF933CAC-ACAD-11D2-A093-00C04F72DC3C}</dt> </dl>             | CommandID for Take Picture. Causes a WIA device to acquire an image.<br/>                                                                                      |
| <span id="wiaCommandDeleteAllItems"></span><span id="wiacommanddeleteallitems"></span><span id="WIACOMMANDDELETEALLITEMS"></span><dl> <dt>**wiaCommandDeleteAllItems**</dt> <dt>{E208C170-ACAD-11D2-A093-00C04F72DC3C}</dt> </dl> | CommandID for Delete All Items. Notifies the device to delete all items that can be deleted from the device.<br/>                                              |
| <span id="wiaCommandChangeDocument"></span><span id="wiacommandchangedocument"></span><span id="WIACOMMANDCHANGEDOCUMENT"></span><dl> <dt>**wiaCommandChangeDocument**</dt> <dt>{04E725B0-ACAE-11D2-A093-00C04F72DC3C}</dt> </dl> | CommandID for Change Document. Causes the document scanner to load the next page in its document handler. Does not apply to other device types.<br/>           |
| <span id="wiaCommandUnloadDocument"></span><span id="wiacommandunloaddocument"></span><span id="WIACOMMANDUNLOADDOCUMENT"></span><dl> <dt>**wiaCommandUnloadDocument**</dt> <dt>{1F3B3D8E-ACAE-11D2-A093-00C04F72DC3C}</dt> </dl> | CommandID for Unload Document. Notifies the document scanner to unload all remaining pages in its document handler. Does not apply to other device types.<br/> |



## Remarks

Use a **CommandID Constants** constant as the value for the *CommandID* parameter for the [**ExecuteCommand (Device)**](-wiaaut-idevice-executecommand.md) and [**ExecuteCommand (Item)**](-wiaaut-iitem-executecommand.md) methods. You can also use a **CommandID Constants** constant as the value of the CommandID properties in a [**DeviceCommand**](-wiaaut-devicecommand.md) object.

The following example shows how to signal a camera to take a picture if the device selected is a camera.


```
Dim dev 'As Device

Set dev = CommonDialog1.ShowSelectDevice

If dev.Type = CameraDeviceType Then
    Dim itm 'As Item
    
    Set itm = dev.ExecuteCommand(wiaCommandTakePicture)
End If
```



Similar to the previous code example, the following example shows how to determine if the selected device supports the **wiaCommandTakePicture** command.


```
Dim dev 'As Device
Dim dc 'As DeviceCommand

Set dev = CommonDialog1.ShowSelectDevice
For Each dc In dev.Commands
    If dc.CommandID = wiaCommandTakePicture Then
        MsgBox "Selected device supports the TakePicture command"
    End If
End If
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**CommandID**](-wiaaut-idevicecommand-commandid.md)
</dt> </dl>

 

 





