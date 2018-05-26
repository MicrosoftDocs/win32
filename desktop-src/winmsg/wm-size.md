---
Description: Sent to a window after its size has changed.
ms.assetid: e3e14dcd-9236-48bd-a692-6985d8146f81
title: WM\_SIZE message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_SIZE message

Sent to a window after its size has changed.

A window receives this message through its [**WindowProc**](/windows/win32/Winuser/nf-winuser-callwindowproca?branch=master) function.


```C++
#define WM_SIZE                         0x0005
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The type of resizing requested. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                   | Meaning                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| <span id="SIZE_MAXHIDE"></span><span id="size_maxhide"></span><dl> <dt>**SIZE\_MAXHIDE**</dt> <dt>4</dt> </dl>       | Message is sent to all pop-up windows when some other window is maximized.<br/>                              |
| <span id="SIZE_MAXIMIZED"></span><span id="size_maximized"></span><dl> <dt>**SIZE\_MAXIMIZED**</dt> <dt>2</dt> </dl> | The window has been maximized.<br/>                                                                          |
| <span id="SIZE_MAXSHOW"></span><span id="size_maxshow"></span><dl> <dt>**SIZE\_MAXSHOW**</dt> <dt>3</dt> </dl>       | Message is sent to all pop-up windows when some other window has been restored to its former size.<br/>      |
| <span id="SIZE_MINIMIZED"></span><span id="size_minimized"></span><dl> <dt>**SIZE\_MINIMIZED**</dt> <dt>1</dt> </dl> | The window has been minimized.<br/>                                                                          |
| <span id="SIZE_RESTORED"></span><span id="size_restored"></span><dl> <dt>**SIZE\_RESTORED**</dt> <dt>0</dt> </dl>    | The window has been resized, but neither the **SIZE\_MINIMIZED** nor **SIZE\_MAXIMIZED** value applies.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word of *lParam* specifies the new width of the client area.

The high-order word of *lParam* specifies the new height of the client area.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

## Remarks

If the [**SetScrollPos**](_win32_SetScrollPos) or [**MoveWindow**](/windows/win32/Winuser/nf-winuser-movewindow?branch=master) function is called for a child window as a result of the **WM\_SIZE** message, the *bRedraw* or *bRepaint* parameter should be nonzero to cause the window to be repainted.

Although the width and height of a window are 32-bit values, the *lParam* parameter contains only the low-order 16 bits of each.

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

[**HIWORD**](/windows/win32/Windef/nf-ntintsafe-hiword?branch=master)
</dt> <dt>

[**LOWORD**](/windows/win32/Windef/nf-ntintsafe-loword?branch=master)
</dt> <dt>

[**MoveWindow**](/windows/win32/Winuser/nf-winuser-movewindow?branch=master)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**SetScrollPos**](_win32_SetScrollPos)
</dt> </dl>

 

 




