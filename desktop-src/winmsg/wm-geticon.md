---
description: Sent to a window to retrieve a handle to the large or small icon associated with a window. The system displays the large icon in the ALT+TAB dialog, and the small icon in the window caption.
ms.assetid: d3101a9b-9658-4a21-b1f6-2920b723926c
title: WM_GETICON message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_GETICON message

Sent to a window to retrieve a handle to the large or small icon associated with a window. The system displays the large icon in the ALT+TAB dialog, and the small icon in the window caption.

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
#define WM_GETICON                      0x007F
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The type of icon being retrieved. This parameter can be one of the following values.



| Value                                                                                                                                                                                                          | Meaning                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ICON_BIG"></span><span id="icon_big"></span><dl> <dt>**ICON\_BIG**</dt> <dt>1</dt> </dl>          | Retrieve the large icon for the window.<br/>                                                                                                                   |
| <span id="ICON_SMALL"></span><span id="icon_small"></span><dl> <dt>**ICON\_SMALL**</dt> <dt>0</dt> </dl>    | Retrieve the small icon for the window.<br/>                                                                                                                   |
| <span id="ICON_SMALL2"></span><span id="icon_small2"></span><dl> <dt>**ICON\_SMALL2**</dt> <dt>2</dt> </dl> | Retrieves the small icon provided by the application. If the application does not provide one, the system uses the system-generated icon for that window.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The DPI of the icon being retrieved. This can be used to provide different icons depending on the icon size.

</dd> </dl>

## Return value

Type: **HICON**

The return value is a handle to the large or small icon, depending on the value of *wParam*. When an application receives this message, it can return a handle to a large or small icon, or pass the message to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function.

## Remarks

When an application receives this message, it can return a handle to a large or small icon, or pass the message to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca).

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) returns a handle to the large or small icon associated with the window, depending on the value of *wParam*.

A window that has no icon explicitly set (with **WM\_SETICON**) uses the icon for the registered window class, and in this case [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) will return 0 for a **WM\_GETICON** message. If sending a **WM\_GETICON** message to a window returns 0, next try calling the [**GetClassLongPtr**](/windows/win32/api/winuser/nf-winuser-getclasslongptra) function for the window. If that returns 0 then try the [**LoadIcon**](/windows/win32/api/winuser/nf-winuser-loadicona) function.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**WM\_SETICON**](wm-seticon.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 
