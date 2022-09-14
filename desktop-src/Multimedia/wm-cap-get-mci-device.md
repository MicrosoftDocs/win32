---
title: WM_CAP_GET_MCI_DEVICE message (Vfw.h)
description: The WM\_CAP\_GET\_MCI\_DEVICE message retrieves the name of an MCI device previously set with the WM\_CAP\_SET\_MCI\_DEVICE message. You can send this message explicitly or by using the capGetMCIDeviceName macro.
ms.assetid: c5d7d955-ab6a-4959-b79e-9ff35a282ba2
keywords:
- WM_CAP_GET_MCI_DEVICE message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_GET_MCI_DEVICE
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_GET\_MCI\_DEVICE message

The **WM\_CAP\_GET\_MCI\_DEVICE** message retrieves the name of an MCI device previously set with the [**WM\_CAP\_SET\_MCI\_DEVICE**](wm-cap-set-mci-device.md) message. You can send this message explicitly or by using the [**capGetMCIDeviceName**](/windows/desktop/api/Vfw/nf-vfw-capgetmcidevicename) macro.


```C++
WM_CAP_GET_MCI_DEVICE 
wParam = (WPARAM) (wSize); 
lParam = (LPARAM) (LPVOID) (LPSTR) (szName); 
```



## Parameters

<dl> <dt>

<span id="wSize"></span><span id="wsize"></span><span id="WSIZE"></span>*wSize*
</dt> <dd>

Length, in bytes, of the buffer referenced by**szName**.

</dd> <dt>

<span id="szName"></span><span id="szname"></span><span id="SZNAME"></span>*szName*
</dt> <dd>

Pointer to a null-terminated string that contains the MCI device name.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[Video Capture](video-capture.md)
</dt> <dt>

[Video Capture Messages](video-capture-messages.md)
</dt> </dl>

 

 





