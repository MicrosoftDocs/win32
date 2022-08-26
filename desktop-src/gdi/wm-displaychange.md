---
description: The WM\_DISPLAYCHANGE message is sent to all windows when the display resolution has changed.
ms.assetid: 5a6111fd-648e-41a9-aaf8-e5d93f5d54cd
title: WM_DISPLAYCHANGE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DISPLAYCHANGE message

The **WM\_DISPLAYCHANGE** message is sent to all windows when the display resolution has changed.

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

The new image depth of the display, in bits per pixel.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word specifies the horizontal resolution of the screen.

The high-order word specifies the vertical resolution of the screen.

</dd> </dl>

## Remarks

This message is only sent to top-level windows. For all other windows it is posted.

**BEGIN**

If the user has a single display system, the above is perfectly clear. On multiple-monitor systems, I think the behavior isn't described well enough here to be usable without lots of time-consuming experimentation:

If the Windows virtual desktop is composed of MULTIPLE displays, then this message is (surely) generated whenever there is a mode change to ANY of the displays that make up (_extend_) the Windows virtual desktop?

(it's also worth mentioning what happens when the primary display is being _duplicated_ by another display)

...but the information in this message only provides updated **width**, **height** and **bpp** info. It says nothing about _which_ display changed on a multi-display system. Since this message is broadcast to all top-level windows, one wonders whether it's necessary to position an invisible, top-level window _on each monitor_ in order to be able to distinguish which display has changed? But since there's never been any mention of "on monitor X" when other docs refer to "top-level windows", I assume it _doesn't_/_can't_ work that way.

**END**

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

 

 
