---
Description: The WM\_NCPAINT message is sent to a window when its frame must be painted.
ms.assetid: d8a2a8b9-2c5d-484c-be09-67eb33de67c0
title: WM_NCPAINT message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_NCPAINT message

The **WM\_NCPAINT** message is sent to a window when its frame must be painted.

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

A handle to the update region of the window. The update region is clipped to the window frame.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

An application returns zero if it processes this message.

## Remarks

The [**DefWindowProc**](https://msdn.microsoft.com/library/ms633572(v=VS.85).aspx) function paints the window frame.

An application can intercept the **WM\_NCPAINT** message and paint its own custom window frame. The clipping region for a window is always rectangular, even if the shape of the frame is altered.

The *wParam* value can be passed to [**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex) as in the following example.


```C++
case WM_NCPAINT:
{
    HDC hdc;
    hdc = GetDCEx(hwnd, (HRGN)wParam, DCX_WINDOW|DCX_INTERSECTRGN);
    // Paint into this DC 
    ReleaseDC(hwnd, hdc);
}
```



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

[**GetWindowDC**](/windows/desktop/api/Winuser/nf-winuser-getwindowdc)
</dt> <dt>

[**WM\_PAINT**](wm-paint.md)
</dt> <dt>

[**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex)
</dt> </dl>

 

 




