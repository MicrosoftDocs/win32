---
title: WM_INPUT_DEVICE_CHANGE message
description: Sent to the window that registered to receive raw input. A window receives this message through its WindowProc function.
ms.assetid: 2f98d8ea-b47b-4dea-9c38-f9697b18053a
keywords:
- WM_INPUT_DEVICE_CHANGE message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_INPUT_DEVICE_CHANGE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_INPUT\_DEVICE\_CHANGE message

Sent to the window that registered to receive raw input.

A window receives this message through its [**WindowProc**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
#define WM_INPUT_DEVICE_CHANGE          0x00FE
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter can be one of the following values.



| Value                                                                                                                                                                                                             | Meaning                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <span id="GIDC_ARRIVAL"></span><span id="gidc_arrival"></span><dl> <dt>**GIDC\_ARRIVAL**</dt> <dt>1</dt> </dl> | A new device has been added to the system. <br/> |
| <span id="GIDC_REMOVAL"></span><span id="gidc_removal"></span><dl> <dt>**GIDC\_REMOVAL**</dt> <dt>2</dt> </dl> | A device has been removed from the system. <br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The handle to the raw input device. Call [**GetRawInputDeviceInfo**](https://msdn.microsoft.com/en-us/library/ms645597(v=VS.85).aspx) to get more information regarding the device.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 





