---
title: MCIWNDM\_SETTIMERS message
description: The MCIWNDM\_SETTIMERS message sets the update periods used by MCIWnd to update the trackbar in the MCIWnd window, update the position information displayed in the window title bar, and send notification messages to the parent window.
ms.assetid: '06407c67-b620-4f80-9fe9-456cdf3d0666'
keywords: ["MCIWNDM_SETTIMERS message Windows Multimedia"]
topic_type:
- apiref
api_name:
- MCIWNDM_SETTIMERS
api_location:
- Vfw.h
api_type:
- HeaderDef
---

# MCIWNDM\_SETTIMERS message

The **MCIWNDM\_SETTIMERS** message sets the update periods used by MCIWnd to update the trackbar in the MCIWnd window, update the position information displayed in the window title bar, and send notification messages to the parent window. You can send this message explicitly or by using the [**MCIWndSetTimers**](mciwndsettimers.md) macro.


```C++
MCIWNDM_SETTIMERS 
wParam = (WPARAM) (UINT) active; 
lParam = (LPARAM) (UINT) inactive; 
```



## Parameters

<dl> <dt>

<span id="active"></span><span id="ACTIVE"></span>*active*
</dt> <dd>

Update period used by MCIWnd when it is the active window. The default value is 500 milliseconds. Storage for this value is limited to 16 bits.

</dd> <dt>

<span id="inactive"></span><span id="INACTIVE"></span>*inactive*
</dt> <dd>

Update period used by MCIWnd when it is the inactive window. The default value is 2000 milliseconds. Storage for this value is limited to 16 bits.

</dd> </dl>

## Return Value

This message does not return a value.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[**MCIWndSetTimers**](mciwndsettimers.md)
</dt> </dl>

 

 





