---
Description: The WM\_SYNCPAINT message is used to synchronize painting while avoiding linking independent GUI threads.
ms.assetid: 4446be4e-e0b9-46ce-95b2-bea876348c25
title: WM_SYNCPAINT message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_SYNCPAINT message

The **WM\_SYNCPAINT** message is used to synchronize painting while avoiding linking independent GUI threads.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/ms633573(v=VS.85).aspx) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND hwnd, 
  UINT  uMsg, 
  WPARAM wParam, 
  LPARAM lParam     
);
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

An application returns zero if it processes this message.

## Remarks

When a window has been hidden, shown, moved, or sized, the system may determine that it is necessary to send a **WM\_SYNCPAINT** message to the top-level windows of other threads. Applications must pass **WM\_SYNCPAINT** to [**DefWindowProc**](https://msdn.microsoft.com/library/ms633572(v=VS.85).aspx) for processing. The **DefWindowProc** function will send a [**WM\_NCPAINT**](wm-ncpaint.md) message to the window procedure if the window frame must be painted and send a [**WM\_ERASEBKGND**](https://msdn.microsoft.com/library/ms648055(v=VS.85).aspx) message if the window background must be erased.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Painting and Drawing Overview](painting-and-drawing.md)
</dt> <dt>

[Painting and Drawing Messages](painting-and-drawing-messages.md)
</dt> <dt>

[**DefWindowProc**](https://msdn.microsoft.com/library/ms633572(v=VS.85).aspx)
</dt> <dt>

[**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex)
</dt> <dt>

[**GetWindowDC**](/windows/desktop/api/Winuser/nf-winuser-getwindowdc)
</dt> <dt>

[**WM\_PAINT**](wm-paint.md)
</dt> </dl>

 

 




