---
title: WM_CAP_DRIVER_CONNECT message (Vfw.h)
description: The WM\_CAP\_DRIVER\_CONNECT message connects a capture window to a capture driver. You can send this message explicitly or by using the capDriverConnect macro.
ms.assetid: 8804bb3c-d06c-4ddc-b116-3d292205a52d
keywords:
- WM_CAP_DRIVER_CONNECT message Windows Multimedia
topic_type:
- apiref
api_name:
- WM_CAP_DRIVER_CONNECT
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CAP\_DRIVER\_CONNECT message

The **WM\_CAP\_DRIVER\_CONNECT** message connects a capture window to a capture driver. You can send this message explicitly or by using the [**capDriverConnect**](/windows/desktop/api/Vfw/nf-vfw-capdriverconnect) macro.


```C++
WM_CAP_DRIVER_CONNECT 
wParam = (WPARAM) (iIndex); 
lParam = 0L; 
```



## Parameters

<dl> <dt>

<span id="iIndex"></span><span id="iindex"></span><span id="IINDEX"></span>*iIndex*
</dt> <dd>

Index of the capture driver. The index can range from 0 through 9.

</dd> </dl>

## Return Value

Returns **TRUE** if successful or **FALSE** if the specified capture driver cannot be connected to the capture window.

## Remarks

Connecting a capture driver to a capture window automatically disconnects any previously connected capture driver.

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

 

 





