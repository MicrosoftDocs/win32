---
title: WM_GETDPISCALEDSIZE message (Winuser.h)
description: This message tells the operating system that the window will be sized to dimensions other than the default.
ms.assetid: 038CAA21-0944-45D3-8C40-A6498F36D9E4
keywords:
- WM_GETDPISCALEDSIZE message High DPI
topic_type:
- apiref
api_name:
- WM_GETDPISCALEDSIZE
api_location:
- winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_GETDPISCALEDSIZE message

This message tells the operating system that the window will be sized to dimensions other than the default.

This message is sent to top-level windows with a [DPI\_AWARENESS\_CONTEXT](dpi-awareness-context.md) of Per Monitor v2 before a [**WM\_DPICHANGED**](wm-dpichanged.md) message is sent, and allows the window to compute its desired size for the pending DPI change. As linear DPI scaling is the default behavior, this is only useful in scenarios where the window wants to scale non-linearly. If the application responds to this message, the resulting size will be the candidate rectangle send to **WM\_DPICHANGED**.

Use this message to alter the size of the rect that is provided with [**WM\_DPICHANGED**](wm-dpichanged.md).


```C++
#define WM_GETDPISCALEDSIZE       0x02E4
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The WPARAM contains a DPI value. The scaled window size that the application would set needs to be computed as if the window were to switch to this DPI.

</dd> <dt>

*lParam* 
</dt> <dd>

The LPARAM is an in/out pointer to a SIZE struct. The \_In\_ value in the LPARAM is the pending size of the window after a user-initiated move or a call to [**SetWindowPos**](/windows/desktop/api/winuser/nf-winuser-setwindowpos). If the window is being resized, this size is not necessarily the same as the window's current size at the time this message is received.

The \_Out\_ value in the LPARAM should be written to by the application to specify the desired scaled window size corresponding to the provided DPI value in the WPARAM.

</dd> </dl>

## Return value

The function returns a BOOL. Returning TRUE indicates that a new size has been computed. Returning FALSE indicates that the message will not be handled, and the default linear DPI scaling will apply to the window.

## Remarks

This message is only sent to top-level windows which have a DPI awareness context of Per Monitor v2.

This event is necessary to facilitate graceful non-linear scaling, and ensures that the windows's position remains constant in relationship to the cursor and when moving back and forth across monitors.

There is no specific default handling of this message in [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca). As for all messages it does not explicitly handle, [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca) will return zero for this message. As noted above, this return tells the system to use the default linear behavior.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



 

