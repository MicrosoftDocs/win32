---
Description: Sent to a window when the window is about to be hidden or shown.
ms.assetid: dea7c9aa-eba7-4b93-a4c5-9b2d36999780
title: WM\_SHOWWINDOW message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_SHOWWINDOW message

Sent to a window when the window is about to be hidden or shown.

A window receives this message through its [**WindowProc**](/windows/win32/Winuser/nf-winuser-callwindowproca?branch=master) function.


```C++
#define WM_SHOWWINDOW                   0x0018
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Indicates whether a window is being shown. If *wParam* is **TRUE**, the window is being shown. If *wParam* is **FALSE**, the window is being hidden.

</dd> <dt>

*lParam* 
</dt> <dd>

The status of the window being shown. If *lParam* is zero, the message was sent because of a call to the [**ShowWindow**](/windows/win32/Winuser/nf-winuser-showwindow?branch=master) function; otherwise, *lParam* is one of the following values.



| Value                                                                                                                                                                                                                         | Meaning                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <span id="SW_OTHERUNZOOM"></span><span id="sw_otherunzoom"></span><dl> <dt>**SW\_OTHERUNZOOM**</dt> <dt>4</dt> </dl>       | The window is being uncovered because a maximize window was restored or minimized.<br/> |
| <span id="SW_OTHERZOOM"></span><span id="sw_otherzoom"></span><dl> <dt>**SW\_OTHERZOOM**</dt> <dt>2</dt> </dl>             | The window is being covered by another window that has been maximized.<br/>             |
| <span id="SW_PARENTCLOSING"></span><span id="sw_parentclosing"></span><dl> <dt>**SW\_PARENTCLOSING**</dt> <dt>1</dt> </dl> | The window's owner window is being minimized.<br/>                                      |
| <span id="SW_PARENTOPENING"></span><span id="sw_parentopening"></span><dl> <dt>**SW\_PARENTOPENING**</dt> <dt>3</dt> </dl> | The window's owner window is being restored.<br/>                                       |



 

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

## Remarks

The [**DefWindowProc**](/windows/win32/Winuser/nf-winuser-defwindowproca?branch=master) function hides or shows the window, as specified by the message. If a window has the [**WS\_VISIBLE**](window-styles.md) style when it is created, the window receives this message after it is created, but before it is displayed. A window also receives this message when its visibility state is changed by the [**ShowWindow**](/windows/win32/Winuser/nf-winuser-showwindow?branch=master) or [**ShowOwnedPopups**](/windows/win32/Winuser/nf-winuser-showownedpopups?branch=master) function.

The **WM\_SHOWWINDOW** message is not sent under the following circumstances:

-   When a top-level, overlapped window is created with the [**WS\_MAXIMIZE**](window-styles.md) or **WS\_MINIMIZE** style.
-   When the **SW\_SHOWNORMAL** flag is specified in the call to the [**ShowWindow**](/windows/win32/Winuser/nf-winuser-showwindow?branch=master) function.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](/windows/win32/Winuser/nf-winuser-defwindowproca?branch=master)
</dt> <dt>

[**ShowOwnedPopups**](/windows/win32/Winuser/nf-winuser-showownedpopups?branch=master)
</dt> <dt>

[**ShowWindow**](/windows/win32/Winuser/nf-winuser-showwindow?branch=master)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




