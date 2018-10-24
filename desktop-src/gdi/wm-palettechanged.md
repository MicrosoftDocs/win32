---
Description: The WM\_PALETTECHANGED message is sent to all top-level and overlapped windows after the window with the keyboard focus has realized its logical palette, thereby changing the system palette.
ms.assetid: 2eed568b-1a16-47d2-ae26-3f1dec35e893
title: WM_PALETTECHANGED message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_PALETTECHANGED message

The **WM\_PALETTECHANGED** message is sent to all top-level and overlapped windows after the window with the keyboard focus has realized its logical palette, thereby changing the system palette. This message enables a window that uses a color palette but does not have the keyboard focus to realize its logical palette and update its client area.

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

A handle to the window that caused the system palette to change.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Remarks

This message must be sent to all top-level and overlapped windows, including the one that changed the system palette. If any child windows use a color palette, this message must be passed on to them as well.

To avoid creating an infinite loop, a window that receives this message must not realize its palette, unless it determines that *wParam* does not contain its own window handle.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Colors Overview](colors.md)
</dt> <dt>

[Color Messages](color-messages.md)
</dt> <dt>

[**WM\_PALETTEISCHANGING**](wm-paletteischanging.md)
</dt> <dt>

[**WM\_QUERYNEWPALETTE**](wm-querynewpalette.md)
</dt> </dl>

 

 




