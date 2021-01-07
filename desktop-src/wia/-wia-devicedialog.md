---
description: Used by applications to display a device dialog box to the user.
ms.assetid: 3b486220-32ab-4d6c-872c-684f9d1ee660
title: DeviceDialog function (Wiadevd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeviceDialog
api_type: 
- LibDef
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# DeviceDialog function

Used by applications to display a device dialog box to the user.

## Syntax


```C++
HRESULT WINAPI DeviceDialog(
  _In_ PDEVICEDIALOGDATA pDeviceDialogData
);
```



## Parameters

<dl> <dt>

*pDeviceDialogData* \[in\]
</dt> <dd>

Type: **PDEVICEDIALOGDATA**

The [**DEVICEDIALOGDATA**](-wia-devicedialogdata.md) to use to create the device dialog.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wiadevd.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



## See also

<dl> <dt>

[**DEVICEDIALOGDATA**](-wia-devicedialogdata.md)
</dt> </dl>

 

 




