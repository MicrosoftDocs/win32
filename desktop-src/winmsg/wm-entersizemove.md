---
Description: Sent one time to a window after it enters the moving or sizing modal loop.
ms.assetid: fe09db71-2c79-47f2-b575-516e960915d4
title: WM_ENTERSIZEMOVE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_ENTERSIZEMOVE message

Sent one time to a window after it enters the moving or sizing modal loop. The window enters the moving or sizing modal loop when the user clicks the window's title bar or sizing border, or when the window passes the [**WM\_SYSCOMMAND**](https://msdn.microsoft.com/library/ms646360(v=VS.85).aspx) message to the [**DefWindowProc**](https://msdn.microsoft.com/library/ms633572(v=VS.85).aspx) function and the *wParam* parameter of the message specifies the **SC\_MOVE** or **SC\_SIZE** value. The operation is complete when [**DefWindowProc**](https://msdn.microsoft.com/library/ms633572(v=VS.85).aspx) returns.

The system sends the **WM\_ENTERSIZEMOVE** message regardless of whether the dragging of full windows is enabled.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/ms633573(v=VS.85).aspx) function.


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

[**DefWindowProc**](https://msdn.microsoft.com/library/ms633572(v=VS.85).aspx)
</dt> <dt>

[**WM\_EXITSIZEMOVE**](wm-exitsizemove.md)
</dt> <dt>

[**WM\_SYSCOMMAND**](https://msdn.microsoft.com/library/ms646360(v=VS.85).aspx)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




