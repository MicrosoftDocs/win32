---
description: IWiaUIExtension::DeviceDialog method - Provides a custom user interface that replaces the default system user interface.
ms.assetid: 5dbcacde-5bbe-459d-804f-5ce7eb1cd8d8
title: IWiaUIExtension::DeviceDialog method (Wiadevd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaUIExtension.DeviceDialog
api_type: 
- COM
api_location: 
- Wiadevd.h
---

# IWiaUIExtension::DeviceDialog method

Provides a custom user interface that replaces the default system user interface.

## Syntax


```C++
HRESULT DeviceDialog(
  [in] PDEVICEDIALOGDATA *pDeviceDialogData
);
```



## Parameters

<dl> <dt>

*pDeviceDialogData* \[in\]
</dt> <dd>

Type: **PDEVICEDIALOGDATA\***

Points to a [**DEVICEDIALOGDATA**](-wia-devicedialogdata.md) structure that contains all of the data needed to implement the device dialog.

</dd> </dl>

## Return value

Type: **HRESULT**

If the method succeeds, it returns S\_OK. If the user cancels the dialog, the method returns S\_FALSE. If the method is not implemented, it returns E\_NOTIMPL. If the method fails, it returns a standard COM error code.

## Remarks

If you implement the [**IWiaUIExtension**](-wia-iwiauiextension.md) interface and do not want to replace the system user interface, this method must still be implemented, but it should do nothing more than return E\_NOTIMPL.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wiadevd.h</dt> </dl> |



 

 




