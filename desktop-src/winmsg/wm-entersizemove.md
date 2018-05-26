---
Description: Sent one time to a window after it enters the moving or sizing modal loop.
ms.assetid: fe09db71-2c79-47f2-b575-516e960915d4
title: WM\_ENTERSIZEMOVE message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_ENTERSIZEMOVE message

Sent one time to a window after it enters the moving or sizing modal loop. The window enters the moving or sizing modal loop when the user clicks the window's title bar or sizing border, or when the window passes the [**WM\_SYSCOMMAND**](menurc.wm_syscommand) message to the [**DefWindowProc**](/windows/win32/Winuser/nf-winuser-defwindowproca?branch=master) function and the *wParam* parameter of the message specifies the **SC\_MOVE** or **SC\_SIZE** value. The operation is complete when [**DefWindowProc**](/windows/win32/Winuser/nf-winuser-defwindowproca?branch=master) returns.

The system sends the **WM\_ENTERSIZEMOVE** message regardless of whether the dragging of full windows is enabled.

A window receives this message through its [**WindowProc**](/windows/win32/Winuser/nf-winuser-callwindowproca?branch=master) function.


```C++
#define WM_ENTERSIZEMOVE                0x0231
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

An application should return zero if it processes this message.

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

[**WM\_EXITSIZEMOVE**](wm-exitsizemove.md)
</dt> <dt>

[**WM\_SYSCOMMAND**](menurc.wm_syscommand)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




