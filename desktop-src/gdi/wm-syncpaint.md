---
Description: The WM\_SYNCPAINT message is used to synchronize painting while avoiding linking independent GUI threads.
ms.assetid: 4446be4e-e0b9-46ce-95b2-bea876348c25
title: WM\_SYNCPAINT message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_SYNCPAINT message

The **WM\_SYNCPAINT** message is used to synchronize painting while avoiding linking independent GUI threads.

A window receives this message through its [**WindowProc**](_win32_windowproc_cpp) function.


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

When a window has been hidden, shown, moved, or sized, the system may determine that it is necessary to send a **WM\_SYNCPAINT** message to the top-level windows of other threads. Applications must pass **WM\_SYNCPAINT** to [**DefWindowProc**](_win32_defwindowproc_cpp) for processing. The **DefWindowProc** function will send a [**WM\_NCPAINT**](wm-ncpaint.md) message to the window procedure if the window frame must be painted and send a [**WM\_ERASEBKGND**](_win32_wm_erasebkgnd_cpp) message if the window background must be erased.

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

[**DefWindowProc**](_win32_defwindowproc_cpp)
</dt> <dt>

[**GetDCEx**](/windows/win32/Winuser/nf-winuser-getdcex?branch=master)
</dt> <dt>

[**GetWindowDC**](/windows/win32/Winuser/nf-winuser-getwindowdc?branch=master)
</dt> <dt>

[**WM\_PAINT**](wm-paint.md)
</dt> </dl>

 

 




