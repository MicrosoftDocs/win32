---
Description: Sent when an application requests that a window be created by calling the CreateWindowEx or CreateWindow function.
ms.assetid: d484d0fc-bad0-4fcb-bf4b-37cbc50846ee
title: WM\_CREATE message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_CREATE message

Sent when an application requests that a window be created by calling the [**CreateWindowEx**](/windows/desktop/api/Winuser/nf-winuser-createwindowexa) or [**CreateWindow**](/windows/desktop/api/Winuser/nf-winuser-createwindowa) function. (The message is sent before the function returns.) The window procedure of the new window receives this message after the window is created, but before the window becomes visible.

A window receives this message through its [**WindowProc**](/windows/desktop/api/Winuser/nf-winuser-callwindowproca) function.


```C++
#define WM_CREATE                       0x0001
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**CREATESTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagclientcreatestruct) structure that contains information about the window being created.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero to continue creation of the window. If the application returns –1, the window is destroyed and the [**CreateWindowEx**](/windows/desktop/api/Winuser/nf-winuser-createwindowexa) or [**CreateWindow**](/windows/desktop/api/Winuser/nf-winuser-createwindowa) function returns a **NULL** handle.

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

[**CreateWindow**](/windows/desktop/api/Winuser/nf-winuser-createwindowa)
</dt> <dt>

[**CreateWindowEx**](/windows/desktop/api/Winuser/nf-winuser-createwindowexa)
</dt> <dt>

[**CREATESTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagclientcreatestruct)
</dt> <dt>

[**WM\_NCCREATE**](wm-nccreate.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




