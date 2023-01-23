---
title: WM_POINTERDEVICECHANGE message
description: Sent to a window when there is a change in the settings of a monitor that has a digitizer attached to it. This message contains information regarding the scaling of the display mode.
ms.assetid: 9ED01D4C-58B4-4A21-B510-784281F9A909
keywords:
- WM_POINTERDEVICECHANGE message Input Messages and Notifications
topic_type:
- apiref
api_name:
- WM_POINTERDEVICECHANGE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 02/03/2020
---

# WM_POINTERDEVICECHANGE message

Sent to a window when there is a change in the settings of a monitor that has a digitizer attached to it. This message contains information regarding the scaling of the display mode.

> ![Important]  
> Desktop apps should be DPI aware. If your app is not DPI aware, screen coordinates contained in pointer messages and related structures might appear inaccurate due to DPI virtualization. DPI virtualization provides automatic scaling support to applications that are not DPI aware and is active by default (users can turn it off). For more information, see [Writing High-DPI Win32 Applications](/previous-versions//dd464660(v=vs.85)).

 


```C++
#define WM_POINTERDEVICECHANGE       0X238
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Contains a value from [**Pointer Device Change Constants**](pointer-device-change-constants.md).

</dd> <dt>

*lParam* 
</dt> <dd>

Additional message-specific information.

</dd> </dl>

## Return value

If the application processes this message, it should return zero.

If the application does not process this message, it should call [**DefWindowProc**](/windows/win32/api/winuser/nf-winuser-defwindowproca).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Messages](messages.md)
</dt> </dl>

 

