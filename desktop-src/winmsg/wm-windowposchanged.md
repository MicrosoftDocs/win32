---
Description: 'Sent to a window whose size, position, or place in the Z order has changed as a result of a call to the SetWindowPos function or another window-management function.'
ms.assetid: '1eabd0b1-1f92-4576-b7fb-8af50fb04526'
title: 'WM\_WINDOWPOSCHANGED message'
---

# WM\_WINDOWPOSCHANGED message

Sent to a window whose size, position, or place in the Z order has changed as a result of a call to the [**SetWindowPos**](setwindowpos.md) function or another window-management function.

A window receives this message through its [**WindowProc**](windowproc.md) function.


```C++
#define WM_WINDOWPOSCHANGED             0x0047
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**WINDOWPOS**](windowpos.md) structure that contains information about the window's new size and position.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

## Remarks

By default, the [**DefWindowProc**](defwindowproc.md) function sends the [**WM\_SIZE**](wm-size.md) and [**WM\_MOVE**](wm-move.md) messages to the window. The **WM\_SIZE** and **WM\_MOVE** messages are not sent if an application handles the **WM\_WINDOWPOSCHANGED** message without calling **DefWindowProc**. It is more efficient to perform any move or size change processing during the **WM\_WINDOWPOSCHANGED** message without calling **DefWindowProc**.

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

[**EndDeferWindowPos**](enddeferwindowpos.md)
</dt> <dt>

[**SetWindowPos**](setwindowpos.md)
</dt> <dt>

[**WINDOWPOS**](windowpos.md)
</dt> <dt>

[**WM\_MOVE**](wm-move.md)
</dt> <dt>

[**WM\_SIZE**](wm-size.md)
</dt> <dt>

[**WM\_WINDOWPOSCHANGING**](wm-windowposchanging.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




