---
description: Sent to cancel certain modes, such as mouse capture.
ms.assetid: c801233a-c4d8-4fd9-aaf0-3d4503bbce26
title: WM_CANCELMODE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CANCELMODE message

Sent to cancel certain modes, such as mouse capture. For example, the system sends this message to the active window when a dialog box or message box is displayed. Certain functions also send this message explicitly to the specified window regardless of whether it is the active window. For example, the [**EnableWindow**](/windows/win32/api/winuser/nf-winuser-enablewindow) function sends this message when disabling the specified window.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
#define WM_CANCELMODE                   0x001F
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

## Remarks

When the **WM\_CANCELMODE** message is sent, the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function cancels internal processing of standard scroll bar input, cancels internal menu processing, and releases the mouse capture.

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

[**EnableWindow**](/windows/win32/api/winuser/nf-winuser-enablewindow)
</dt> <dt>

[**ReleaseCapture**](/windows/win32/api/winuser/nf-winuser-releasecapture)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 
