---
title: Device.ExecuteCommand method
description: Issues the command to the imaging device.
ms.assetid: 1be9ed21-24a7-4034-8cb3-7c0e2776cb35
keywords:
- ExecuteCommand method WIA Automation
- ExecuteCommand method WIA Automation , Device object
- Device object WIA Automation , ExecuteCommand method
topic_type:
- apiref
api_name:
- Device.ExecuteCommand
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Device.ExecuteCommand method

Issues the command to the imaging device.

## Syntax


```VB
ppResult = .ExecuteCommand( _
  ByVal CommandID As BSTR _
) As HRESULT
```



## Parameters

<dl> <dt>

*CommandID* \[in\]
</dt> <dd>

Type: **BSTR**

Required. **String** value with the command to the imaging device.

</dd> </dl>

## Return value

Type: **[**Item**](-wiaaut-item.md)\*\***

Required. [**Item**](-wiaaut-item.md) value.

## Remarks

[**CommandID Constants**](-wiaaut-consts-commandid.md) are device dependent. Valid **CommandID Constants** for this device are contained in the [**Commands (Device)**](-wiaaut-idevice-commands.md) collection.

For example code, see [Take a Picture](-wiaaut-shared-samples.md#take-a-picture) in Shared Samples.

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

[**CommandID Constants**](-wiaaut-consts-commandid.md)
</dt> <dt>

[**ShowItemProperties**](-wiaaut-icommondialog-showitemproperties.md)
</dt> <dt>

[**ShowTransfer**](-wiaaut-icommondialog-showtransfer.md)
</dt> <dt>

[**Device**](-wiaaut-device.md)
</dt> <dt>

[**GetItem**](-wiaaut-idevice-getitem.md)
</dt> <dt>

[**CommandID**](-wiaaut-idevicecommand-commandid.md)
</dt> <dt>

[**Item**](-wiaaut-item.md)
</dt> <dt>

[**ExecuteCommand (Item)**](-wiaaut-iitem-executecommand.md)
</dt> <dt>

[**Item (Items)**](-wiaaut-iitems-item.md)
</dt> </dl>

 

 





