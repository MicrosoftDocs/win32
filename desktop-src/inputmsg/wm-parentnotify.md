---
title: WM\_PARENTNOTIFY message
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

# WM\_PARENTNOTIFY message

Sent to a window when a significant action occurs on a descendant window. This message is now extended to include the [**WM\_POINTERDOWN**](wm-pointerdown.md) event. When the child window is being created, the system sends [**WM\_PARENTNOTIFY**](https://msdn.microsoft.com/library/windows/desktop/hh454920) just before the [**CreateWindow**](https://msdn.microsoft.com/library/windows/desktop/ms632679) or [**CreateWindowEx**](https://msdn.microsoft.com/library/windows/desktop/ms632680) function that creates the window returns. When the child window is being destroyed, the system sends the message before any processing to destroy the window takes place.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.

> \[!Important\]  
> Desktop apps should be DPI aware. If your app is not DPI aware, screen coordinates contained in pointer messages and related structures might appear inaccurate due to DPI virtualization. DPI virtualization provides automatic scaling support to applications that are not DPI aware and is active by default (users can turn it off). For more information, see [Writing High-DPI Win32 Applications](https://msdn.microsoft.com/library/windows/desktop/dd464660).

 


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
| <span id="WM_CREATE"></span><span id="wm_create"></span><dl> <dt>**WM\_CREATE**</dt> <dt>0x0001</dt> </dl>                | The child window is being created.<br/> HIWORD(*wParam*) is the identifier of the child window.<br/> *lParam* is a handle to the child window.<br/>                                                                                                                                                                                                                          |
| <span id="WM_DESTROY"></span><span id="wm_destroy"></span><dl> <dt>**WM\_DESTROY**</dt> <dt>0x0002</dt> </dl>             | The child window is being destroyed.<br/> HIWORD(*wParam*) is the identifier of the child window.<br/> *lParam* is a handle to the child window.<br/>                                                                                                                                                                                                                        |
| <span id="WM_LBUTTONDOWN"></span><span id="wm_lbuttondown"></span><dl> <dt>**WM\_LBUTTONDOWN**</dt> <dt>0x0201</dt> </dl> | The user has placed the cursor over the child window and has clicked the left mouse button.<br/> HIWORD(*wParam*) is undefined.<br/> *lParam* is the x-coordinate of the cursor is the low-order word, and the y-coordinate of the cursor is the high-order word.<br/>                                                                                                       |
| <span id="WM_MBUTTONDOWN"></span><span id="wm_mbuttondown"></span><dl> <dt>**WM\_MBUTTONDOWN**</dt> <dt>0x0207</dt> </dl> | The user has placed the cursor over the child window and has clicked the middle mouse button.<br/> HIWORD(*wParam*) is undefined.<br/> *lParam* is the x-coordinate of the cursor is the low-order word, and the y-coordinate of the cursor is the high-order word.<br/>                                                                                                     |
| <span id="WM_RBUTTONDOWN"></span><span id="wm_rbuttondown"></span><dl> <dt>**WM\_RBUTTONDOWN**</dt> <dt>0x0204</dt> </dl> | The user has placed the cursor over the child window and has clicked the right mouse button.<br/> HIWORD(*wParam*) is undefined.<br/> *lParam* is the x-coordinate of the cursor is the low-order word, and the y-coordinate of the cursor is the high-order word.<br/>                                                                                                      |
| <span id="WM_XBUTTONDOWN"></span><span id="wm_xbuttondown"></span><dl> <dt>**WM\_XBUTTONDOWN**</dt> <dt>0x020B</dt> </dl> | The user has placed the cursor over the child window and has clicked the first or second X button.<br/> HIWORD(*wParam*) indicates which button was pressed. This parameter can be one of the following values: XBUTTON1 or XBUTTON2.<br/> *lParam* is the x-coordinate of the cursor is the low-order word, and the y-coordinate of the cursor is the high-order word.<br/> |
| <span id="WM_POINTERDOWN"></span><span id="wm_pointerdown"></span><dl> <dt>**WM\_POINTERDOWN**</dt> <dt>0x0246</dt> </dl> | A pointer has made contact with the child window.<br/> HIWORD(*wParam*) contains the identifier of the pointer that generated the [**WM\_POINTERDOWN**](wm-pointerdown.md) event.<br/>                                                                                                                                                                                            |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Contains the point location of the pointer.

> [!Note]  
> Because the pointer may make contact with the device over a non-trivial area, this point location may be a simplification of a more complex pointer area. Whenever possible, an application should use the complete pointer area information instead of the point location.

 

Use the following macros to retrieve the physical screen coordinates of the point.

-   [**GET\_X\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632654)(lParam): the x (horizontal point) coordinate.
-   [**GET\_Y\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632655)(lParam): the y (vertical point) coordinate.

</dd> </dl>

## Return value

If the application processes this message, it returns zero.

If the application does not process this message, it calls [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572).

## Remarks

This message is also sent to all ancestor windows of the child window, including the top-level window.

All child windows, except those that have the **WS\_EX\_NOPARENTNOTIFY** extended window style, send this message to their parent windows. By default, child windows in a dialog box have the **WS\_EX\_NOPARENTNOTIFY** style, unless the [**CreateWindowEx**](https://msdn.microsoft.com/library/windows/desktop/ms632680) function is called to create the child window without this style.

This notification provides the child window's ancestor windows an opportunity to examine the pointer information and, if required, capture the pointer using the pointer capture functions.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Messages](messages.md)
</dt> <dt>

[**CreateWindow**](https://msdn.microsoft.com/library/windows/desktop/ms632679)
</dt> <dt>

[**CreateWindowEx**](https://msdn.microsoft.com/library/windows/desktop/ms632680)
</dt> <dt>

[**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657)
</dt> <dt>

[**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659)
</dt> <dt>

[**WM\_CREATE**](https://msdn.microsoft.com/library/windows/desktop/ms632619)
</dt> <dt>

[**WM\_DESTROY**](https://msdn.microsoft.com/library/windows/desktop/ms632620)
</dt> <dt>

[**WM\_LBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645607)
</dt> <dt>

[**WM\_MBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645610)
</dt> <dt>

[**WM\_RBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646242)
</dt> <dt>

[**WM\_XBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646245)
</dt> </dl>

 

 





