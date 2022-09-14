---
description: Sent when the size and position of a window's client area must be calculated. By processing this message, an application can control the content of the window's client area when the size or position of the window changes.
ms.assetid: d2d5825e-02a5-44b8-8615-55b7259d24ba
title: WM_NCCALCSIZE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_NCCALCSIZE message

Sent when the size and position of a window's client area must be calculated. By processing this message, an application can control the content of the window's client area when the size or position of the window changes.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
#define WM_NCCALCSIZE                   0x0083
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

If *wParam* is **TRUE**, it specifies that the application should indicate which part of the client area contains valid information. The system copies the valid information to the specified area within the new client area.

If *wParam* is **FALSE**, the application does not need to indicate the valid part of the client area.

</dd> <dt>

*lParam* 
</dt> <dd>

If *wParam* is **TRUE**, *lParam* points to an [**NCCALCSIZE\_PARAMS**](/windows/win32/api/winuser/ns-winuser-nccalcsize_params) structure that contains information an application can use to calculate the new size and position of the client rectangle.

If *wParam* is **FALSE**, *lParam* points to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure. On entry, the structure contains the proposed window rectangle for the window. On exit, the structure should contain the screen coordinates of the corresponding window client area.

</dd> </dl>

## Return value

Type: **LRESULT**

If the *wParam* parameter is **FALSE**, the application should return zero.

If *wParam* is **TRUE**, the application should return zero or a combination of the following values.

If *wParam* is **TRUE** and an application returns zero, the old client area is preserved and is aligned with the upper-left corner of the new client area.



| Return code/value                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**WVR\_ALIGNTOP**</dt> <dt>0x0010</dt> </dl>    | Specifies that the client area of the window is to be preserved and aligned with the top of the new position of the window. For example, to align the client area to the upper-left corner, return the WVR\_ALIGNTOP and **WVR\_ALIGNLEFT** values.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>**WVR\_ALIGNRIGHT**</dt> <dt>0x0080</dt> </dl>  | Specifies that the client area of the window is to be preserved and aligned with the right side of the new position of the window. For example, to align the client area to the lower-right corner, return the **WVR\_ALIGNRIGHT** and WVR\_ALIGNBOTTOM values.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <dl> <dt>**WVR\_ALIGNLEFT**</dt> <dt>0x0020</dt> </dl>   | Specifies that the client area of the window is to be preserved and aligned with the left side of the new position of the window. For example, to align the client area to the lower-left corner, return the **WVR\_ALIGNLEFT** and **WVR\_ALIGNBOTTOM** values.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <dl> <dt>**WVR\_ALIGNBOTTOM**</dt> <dt>0x0040</dt> </dl> | Specifies that the client area of the window is to be preserved and aligned with the bottom of the new position of the window. For example, to align the client area to the top-left corner, return the WVR\_ALIGNTOP and **WVR\_ALIGNLEFT** values.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**WVR\_HREDRAW**</dt> <dt>0x0100</dt> </dl>     | Used in combination with any other values, except **WVR\_VALIDRECTS**, causes the window to be completely redrawn if the client rectangle changes size horizontally. This value is similar to [CS\_HREDRAW](about-window-classes.md) class style<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <dl> <dt>**WVR\_VREDRAW**</dt> <dt>0x0200</dt> </dl>     | Used in combination with any other values, except **WVR\_VALIDRECTS**, causes the window to be completely redrawn if the client rectangle changes size vertically. This value is similar to [CS\_VREDRAW](about-window-classes.md) class style<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**WVR\_REDRAW**</dt> <dt>0x0300</dt> </dl>      | This value causes the entire window to be redrawn. It is a combination of **WVR\_HREDRAW** and **WVR\_VREDRAW** values.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>**WVR\_VALIDRECTS**</dt> <dt>0x0400</dt> </dl>  | This value indicates that, upon return from [**WM\_NCCALCSIZE**](wm-nccalcsize.md), the rectangles specified by the **rgrc**\[1\] and **rgrc**\[2\] members of the [**NCCALCSIZE\_PARAMS**](/windows/win32/api/winuser/ns-winuser-nccalcsize_params) structure contain valid destination and source area rectangles, respectively. The system combines these rectangles to calculate the area of the window to be preserved. The system copies any part of the window image that is within the source rectangle and clips the image to the destination rectangle. Both rectangles are in parent-relative or screen-relative coordinates. This flag cannot be combined with any other flags. <br/> This return value allows an application to implement more elaborate client-area preservation strategies, such as centering or preserving a subset of the client area.<br/> |



 

## Remarks

The window may be redrawn, depending on whether the [CS\_HREDRAW](about-window-classes.md) or CS\_VREDRAW class style is specified. This is the default, backward-compatible processing of this message by the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function (in addition to the usual client rectangle calculation described in the preceding table).

When *wParam* is **TRUE**, simply returning 0 without processing the [**NCCALCSIZE\_PARAMS**](/windows/win32/api/winuser/ns-winuser-nccalcsize_params) rectangles will cause the client area to resize to the size of the window, including the window frame. This will remove the window frame and caption items from your window, leaving only the client area displayed.

Starting with Windows Vista, removing the standard frame by simply returning 0 when the *wParam* is **TRUE** does not affect frames that are extended into the client area using the [**DwmExtendFrameIntoClientArea**](/windows/win32/api/dwmapi/nf-dwmapi-dwmextendframeintoclientarea) function. Only the standard frame will be removed.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**MoveWindow**](/windows/win32/api/winuser/nf-winuser-movewindow)
</dt> <dt>

[**SetWindowPos**](/windows/win32/api/winuser/nf-winuser-setwindowpos)
</dt> <dt>

[**NCCALCSIZE\_PARAMS**](/windows/win32/api/winuser/ns-winuser-nccalcsize_params)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**RECT**](/previous-versions//dd162897(v=vs.85))
</dt> </dl>

 

 
