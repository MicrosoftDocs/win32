---
title: WM_POINTERWHEEL message
description: Posted to the window with foreground keyboard focus when a scroll wheel is rotated.
ms.assetid: 6eec37da-2200-4be1-bf0b-44704caa1320
keywords:
- WM_POINTERWHEEL message Input Messages and Notifications
topic_type:
- apiref
api_name:
- WM_POINTERWHEEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 02/03/2020
---

# WM_POINTERWHEEL message

Posted to the window with foreground keyboard focus when a scroll wheel is rotated.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.

> ![Important]  
> Desktop apps should be DPI aware. If your app is not DPI aware, screen coordinates contained in pointer messages and related structures might appear inaccurate due to DPI virtualization. DPI virtualization provides automatic scaling support to applications that are not DPI aware and is active by default (users can turn it off). For more information, see [Writing High-DPI Win32 Applications](/previous-versions//dd464660(v=vs.85)).

 


```C++
#define WM_POINTERWHEEL            0x024E
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Contains the pointer identifier and wheel delta. Use the following macros to retrieve this information.

[**GET_POINTERID_WPARAM**](/windows/win32/api/winuser/nf-winuser-get_pointerid_wparam)(wParam): pointer identifier.

[**GET_WHEEL_DELTA_WPARAM**](/windows/win32/api/winuser/nf-winuser-get_wheel_delta_wparam)(wParam): wheel delta as a signed short value.

</dd> <dt>

*lParam* 
</dt> <dd>

Contains the point location of the pointer.

> [!Note]  
> Because the pointer may make contact with the device over a non-trivial area, this point location may be a simplification of a more complex pointer area. Whenever possible, an application should use the complete pointer area information instead of the point location.

 

Use the following macros to retrieve the physical screen coordinates of the point.

-   [**GET_X_LPARAM**](/windows/win32/api/windowsx/nf-windowsx-get_x_lparam)(lParam): the x (horizontal point) coordinate.
-   [**GET_Y_LPARAM**](/windows/win32/api/windowsx/nf-windowsx-get_y_lparam)(lParam): the y (vertical point) coordinate.

</dd> </dl>

## Return value

If the application processes this message, it should return zero.

If the application does not process this message, it should call [**DefWindowProc**](/windows/win32/api/winuser/nf-winuser-defwindowproca).

## Remarks

To retrieve the wheel scroll units, use the **inputData** filed of the [**POINTER_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_info) structure returned by calling [**GetPointerInfo**](/windows/win32/api/winuser/ns-winuser-pointer_info) function. This field contains a signed value and is expressed in a multiple of **WHEEL_DELTA**. A positive value indicates a rotation forward and a negative value indicates a rotation backward.

Note that the wheel inputs may be delivered even if the mouse cursor is located outside of application s window. The wheel messages are delivered in a way very similar to the keyboard inputs. The focus window of the foregournd message queue receives the wheel messages.

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

 

