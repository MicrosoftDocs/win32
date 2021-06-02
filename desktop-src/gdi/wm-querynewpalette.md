---
description: The WM\_QUERYNEWPALETTE message informs a window that it is about to receive the keyboard focus, giving the window the opportunity to realize its logical palette when it receives the focus.
ms.assetid: bc9f76ca-62af-4f0b-8791-49269a1b23d1
title: WM_QUERYNEWPALETTE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_QUERYNEWPALETTE message

The **WM\_QUERYNEWPALETTE** message informs a window that it is about to receive the keyboard focus, giving the window the opportunity to realize its logical palette when it receives the focus.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


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

If the window realizes its logical palette, it must return **TRUE**; otherwise, it must return **FALSE**.

## Requirements



| Requirement | Value |
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

[**WM\_PALETTECHANGED**](wm-palettechanged.md)
</dt> <dt>

[**WM\_PALETTEISCHANGING**](wm-paletteischanging.md)
</dt> </dl>

 

 
