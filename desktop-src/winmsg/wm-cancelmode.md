---
Description: Sent to cancel certain modes, such as mouse capture.
ms.assetid: c801233a-c4d8-4fd9-aaf0-3d4503bbce26
title: WM\_CANCELMODE message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_CANCELMODE message

Sent to cancel certain modes, such as mouse capture. For example, the system sends this message to the active window when a dialog box or message box is displayed. Certain functions also send this message explicitly to the specified window regardless of whether it is the active window. For example, the [**EnableWindow**](inputdev.enablewindow) function sends this message when disabling the specified window.

A window receives this message through its [**WindowProc**](windowproc.md) function.


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

When the **WM\_CANCELMODE** message is sent, the [**DefWindowProc**](defwindowproc.md) function cancels internal processing of standard scroll bar input, cancels internal menu processing, and releases the mouse capture.

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

[**DefWindowProc**](defwindowproc.md)
</dt> <dt>

[**EnableWindow**](inputdev.enablewindow)
</dt> <dt>

[**ReleaseCapture**](inputdev.releasecapture)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




