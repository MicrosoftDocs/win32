---
description: The WM\_DISPLAYCHANGE message is sent to all windows when the display resolution has changed.
ms.assetid: 5a6111fd-648e-41a9-aaf8-e5d93f5d54cd
title: WM_DISPLAYCHANGE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DISPLAYCHANGE message

The **WM\_DISPLAYCHANGE** message is sent to all windows when the display resolution has changed.

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


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

The new image depth of the display, in bits per pixel.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word specifies the horizontal resolution of the screen.

The high-order word specifies the vertical resolution of the screen.

</dd> </dl>

## Remarks

This message is only sent to top-level windows. For all other windows it is posted.

## Requirements



| Requirement | Value |
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

[**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))
</dt> <dt>

[**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))
</dt> </dl>

 

 
