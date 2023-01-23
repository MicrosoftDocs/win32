---
title: WM_PARENTNOTIFY message
description: Sent to a window when a significant action occurs on a descendant window.
ms.assetid: 4bdc37da-227c-4be1-bf0b-99704caa1444
keywords:
- WM_PARENTNOTIFY message Input Messages and Notifications
topic_type:
- apiref
api_name:
- WM_PARENTNOTIFY
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 02/03/2020
---

# WM_PARENTNOTIFY message

Sent to a window when a significant action occurs on a descendant window. This message is now extended to include the [**WM_POINTERDOWN**](wm-pointerdown.md) event. When the child window is being created, the system sends [**WM_PARENTNOTIFY**](/previous-versions/windows/desktop/inputmsg/wm-parentnotify) just before the [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function that creates the window returns. When the child window is being destroyed, the system sends the message before any processing to destroy the window takes place.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.

> ![Important]  
> Desktop apps should be DPI aware. If your app is not DPI aware, screen coordinates contained in pointer messages and related structures might appear inaccurate due to DPI virtualization. DPI virtualization provides automatic scaling support to applications that are not DPI aware and is active by default (users can turn it off). For more information, see [Writing High-DPI Win32 Applications](/previous-versions//dd464660(v=vs.85)).

 


```C++
#define WM_PARENTNOTIFY             0x0210
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The low-order word of *wParam* specifies the event for which the parent is being notified. The value of the high-order word depends on the value of the low-order word. This parameter can be one of the following values.



| LOWORD(*wParam*)                                                                                                                                                                                                             | Meaning                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WM_CREATE"></span><span id="wm_create"></span><dl> <dt>**WM_CREATE**</dt> <dt>0x0001</dt> </dl>                | The child window is being created.<br/> HIWORD(*wParam*) is the identifier of the child window.<br/> *lParam* is a handle to the child window.<br/>                                                                                                                                                                                                                          |
| <span id="WM_DESTROY"></span><span id="wm_destroy"></span><dl> <dt>**WM_DESTROY**</dt> <dt>0x0002</dt> </dl>             | The child window is being destroyed.<br/> HIWORD(*wParam*) is the identifier of the child window.<br/> *lParam* is a handle to the child window.<br/>                                                                                                                                                                                                                        |
| <span id="WM_LBUTTONDOWN"></span><span id="wm_lbuttondown"></span><dl> <dt>**WM_LBUTTONDOWN**</dt> <dt>0x0201</dt> </dl> | The user has placed the cursor over the child window and has clicked the left mouse button.<br/> HIWORD(*wParam*) is undefined.<br/> *lParam* is the x-coordinate of the cursor is the low-order word, and the y-coordinate of the cursor is the high-order word.<br/>                                                                                                       |
| <span id="WM_MBUTTONDOWN"></span><span id="wm_mbuttondown"></span><dl> <dt>**WM_MBUTTONDOWN**</dt> <dt>0x0207</dt> </dl> | The user has placed the cursor over the child window and has clicked the middle mouse button.<br/> HIWORD(*wParam*) is undefined.<br/> *lParam* is the x-coordinate of the cursor is the low-order word, and the y-coordinate of the cursor is the high-order word.<br/>                                                                                                     |
| <span id="WM_RBUTTONDOWN"></span><span id="wm_rbuttondown"></span><dl> <dt>**WM_RBUTTONDOWN**</dt> <dt>0x0204</dt> </dl> | The user has placed the cursor over the child window and has clicked the right mouse button.<br/> HIWORD(*wParam*) is undefined.<br/> *lParam* is the x-coordinate of the cursor is the low-order word, and the y-coordinate of the cursor is the high-order word.<br/>                                                                                                      |
| <span id="WM_XBUTTONDOWN"></span><span id="wm_xbuttondown"></span><dl> <dt>**WM_XBUTTONDOWN**</dt> <dt>0x020B</dt> </dl> | The user has placed the cursor over the child window and has clicked the first or second X button.<br/> HIWORD(*wParam*) indicates which button was pressed. This parameter can be one of the following values: XBUTTON1 or XBUTTON2.<br/> *lParam* is the x-coordinate of the cursor is the low-order word, and the y-coordinate of the cursor is the high-order word.<br/> |
| <span id="WM_POINTERDOWN"></span><span id="wm_pointerdown"></span><dl> <dt>**WM_POINTERDOWN**</dt> <dt>0x0246</dt> </dl> | A pointer has made contact with the child window.<br/> HIWORD(*wParam*) contains the identifier of the pointer that generated the [**WM_POINTERDOWN**](wm-pointerdown.md) event.<br/>                                                                                                                                                                                            |



 

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

If the application processes this message, it returns zero.

If the application does not process this message, it calls [**DefWindowProc**](/windows/win32/api/winuser/nf-winuser-defwindowproca).

## Remarks

This message is also sent to all ancestor windows of the child window, including the top-level window.

All child windows, except those that have the **WS_EX_NOPARENTNOTIFY** extended window style, send this message to their parent windows. By default, child windows in a dialog box have the **WS_EX_NOPARENTNOTIFY** style, unless the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function is called to create the child window without this style.

This notification provides the child window's ancestor windows an opportunity to examine the pointer information and, if required, capture the pointer using the pointer capture functions.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Messages](messages.md)
</dt> <dt>

[**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa)
</dt> <dt>

[**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa)
</dt> <dt>

[**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))
</dt> <dt>

[**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))
</dt> <dt>

[**WM_CREATE**](../winmsg/wm-create.md)
</dt> <dt>

[**WM_DESTROY**](../winmsg/wm-destroy.md)
</dt> <dt>

[**WM_LBUTTONDOWN**](../inputdev/wm-lbuttondown.md)
</dt> <dt>

[**WM_MBUTTONDOWN**](../inputdev/wm-mbuttondown.md)
</dt> <dt>

[**WM_RBUTTONDOWN**](../inputdev/wm-rbuttondown.md)
</dt> <dt>

[**WM_XBUTTONDOWN**](../inputdev/wm-xbuttondown.md)
</dt> </dl>

 

