---
Description: 'Sent one time to a window, after it has exited the moving or sizing modal loop.'
ms.assetid: '3466bfb5-c38d-49d8-a4ab-bf23d09c454c'
title: 'WM\_EXITSIZEMOVE message'
---

# WM\_EXITSIZEMOVE message

Sent one time to a window, after it has exited the moving or sizing modal loop. The window enters the moving or sizing modal loop when the user clicks the window's title bar or sizing border, or when the window passes the [**WM\_SYSCOMMAND**](menurc.wm_syscommand) message to the [**DefWindowProc**](defwindowproc.md) function and the *wParam* parameter of the message specifies the **SC\_MOV**E or **SC\_SIZE** value. The operation is complete when [**DefWindowProc**](defwindowproc.md) returns.

A window receives this message through its [**WindowProc**](windowproc.md) function.


```C++
#define WM_EXITSIZEMOVE                 0x0232
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

[**DefWindowProc**](defwindowproc.md)
</dt> <dt>

[**WM\_ENTERSIZEMOVE**](wm-entersizemove.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




