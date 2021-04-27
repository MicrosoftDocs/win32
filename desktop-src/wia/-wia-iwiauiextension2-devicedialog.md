---
description: IWiaUIExtension2::DeviceDialog method - Provides a custom user interface that replaces the default system user interface.
ms.assetid: 0d70392d-294a-42bf-adc5-1006f83d7e21
title: IWiaUIExtension2::DeviceDialog method (Wiadevd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaUIExtension2.DeviceDialog
api_type: 
- COM
api_location: 
- Wiadevd.h
---

# IWiaUIExtension2::DeviceDialog method

Provides a custom user interface that replaces the default system user interface.

## Syntax


```C++
HRESULT DeviceDialog(
  [in] PDEVICEDIALOGDATA2 *pDeviceDialogData
);
```



## Parameters

<dl> <dt>

*pDeviceDialogData* \[in\]
</dt> <dd>

Type: **PDEVICEDIALOGDATA2\***

Points to a [**DEVICEDIALOGDATA2**](-wia-devicedialogdata2.md) structure that contains all of the data needed to implement the device dialog.

</dd> </dl>

## Return value

Type: **HRESULT**

If the method succeeds, it returns S\_OK. If the user cancels the dialog, the method returns S\_FALSE. If the method fails, it returns an appropriate error code. The following table shows some of the possible return status codes.



| Error code    | Description                              |
|---------------|------------------------------------------|
| E\_INVALIDARG | Parameter pDeviceDialogData is **NULL**. |
| E\_NOTIMPL    | The method is not implemented.           |



 

## Remarks

If you implement the [**IWiaUIExtension2**](-wia-iwiauiextension2.md) interface and do not want to replace the system user interface, this method must still be implemented, but it should do nothing more than return E\_NOTIMPL.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wiadevd.h</dt> </dl> |



 

 




