---
title: WM_NCHITTEST message (Winuser.h)
description: Sent to a window in order to determine what part of the window corresponds to a particular screen coordinate.
ms.assetid: 4c860466-a9f8-4af8-96b9-cee005481875
keywords:
- WM_NCHITTEST message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_NCHITTEST
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_NCHITTEST message

Sent to a window in order to determine what part of the window corresponds to a particular screen coordinate. This can happen, for example, when the cursor moves, when a mouse button is pressed or released, or in response to a call to a function such as [**WindowFromPoint**](/windows/desktop/api/winuser/nf-winuser-windowfrompoint). If the mouse is not captured, the message is sent to the window beneath the cursor. Otherwise, the message is sent to the window that has captured the mouse.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.

```C++
#define WM_NCHITTEST 0x0084
```

## Parameters

<dl> <dt>
*wParam* 
</dt> <dd>
This parameter is not used.
</dd> <dt>
*lParam* 
</dt> <dd>
The low-order word specifies the x-coordinate of the cursor. The coordinate is relative to the upper-left corner of the screen.

The high-order word specifies the y-coordinate of the cursor. The coordinate is relative to the upper-left corner of the screen.
</dd> </dl>

## Return value

The return value of the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function is one of the following values, indicating the position of the cursor hot spot.

| Return code/value | Description |
|-------------------|-------------|
| **HTERROR**</br>-2 | On the screen background or on a dividing line between windows (same as **HTNOWHERE**, except that the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function produces a system beep to indicate an error). |
| **HTTRANSPARENT**</br>-1 | In a window currently covered by another window in the same thread (the message will be sent to underlying windows in the same thread until one of them returns a code that is not **HTTRANSPARENT**). |
| **HTNOWHERE**</br>0 | On the screen background or on a dividing line between windows. |
| **HTCLIENT**</br>1 | In a client area. |
| **HTCAPTION**</br>2 | In a title bar. |
| **HTSYSMENU**</br>3 | In a window menu or in a **Close** button in a child window. |
| **HTSIZE**</br>**HTGROWBOX**</br>4 | In a size box. |
| **HTMENU**</br>5 | In a menu. |
| **HTHSCROLL**</br>6 | In a horizontal scroll bar. |
| **HTVSCROLL**</br>7 | In the vertical scroll bar. |
| **HTREDUCE**</br>**HTMINBUTTON**</br>8 | In a **Minimize** button. |
| **HTZOOM**</br>**HTMAXBUTTON**</br>9 | In a **Maximize** button. |
| **HTLEFT**</br>**HTSIZEFIRST**</br>10 | In the left border of a resizable window (the user can click the mouse to resize the window horizontally). |
| **HTRIGHT**</br>11 | In the right border of a resizable window (the user can click the mouse to resize the window horizontally). |
| **HTTOP**</br>12 | In the upper-horizontal border of a window. |
| **HTTOPLEFT**</br>13 | In the upper-left corner of a window border. |
| **HTTOPRIGHT**</br>14 | In the upper-right corner of a window border. |
| **HTBOTTOM**</br>15 | In the lower-horizontal border of a resizable window (the user can click the mouse to resize the window vertically). |
| **HTBOTTOMLEFT**</br>16 | In the lower-left corner of a border of a resizable window (the user can click the mouse to resize the window diagonally). |
| **HTBOTTOMRIGHT**</br>**HTSIZELAST**</br>17 | In the lower-right corner of a border of a resizable window (the user can click the mouse to resize the window diagonally). |
| **HTBORDER**</br>18 | In the border of a window that does not have a sizing border. |
| **HTOBJECT**</br>19 | Not implemented. Do not use. |
| **HTCLOSE**</br>20 | In a **Close** button. |
| **HTHELP**</br>21 | In a **Help** button. |

## Remarks

Use the following code to obtain the horizontal and vertical position:

```
xPos = GET_X_LPARAM(lParam); 
yPos = GET_Y_LPARAM(lParam);
```

As noted above, the x-coordinate is in the low-order **short** of the return value; the y-coordinate is in the high-order **short** (both represent *signed* values because they can take negative values on systems with multiple monitors). If the return value is assigned to a variable, you can use the [**MAKEPOINTS**](/windows/desktop/api/wingdi/nf-wingdi-makepoints) macro to obtain a [**POINTS**](/previous-versions//dd162808(v=vs.85)) structure from the return value. You can also use the [**GET\_X\_LPARAM**](/windows/desktop/api/windowsx/nf-windowsx-get_x_lparam) or [**GET\_Y\_LPARAM**](/windows/desktop/api/windowsx/nf-windowsx-get_y_lparam) macro to extract the x- or y-coordinate.

> [!IMPORTANT]
> Do not use the [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) or [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) macros to extract the x- and y- coordinates of the cursor position because these macros return incorrect results on systems with multiple monitors. Systems with multiple monitors can have negative x- and y- coordinates, and **LOWORD** and **HIWORD** treat the coordinates as unsigned quantities.

**Windows Vista:** When creating custom frames that include the standard caption buttons, this message should first be passed to the [**DwmDefWindowProc**](/windows/desktop/api/dwmapi/nf-dwmapi-dwmdefwindowproc) function. This enables the Desktop Window Manager (DWM) to provide hit-testing for the captions buttons. If **DwmDefWindowProc** does not handle the message, further processing of **WM\_NCHITTEST** may be needed.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/> |
| Header<br/> | <dl> <dt>Winuser.h (include Windowsx.h)</dt> </dl> |

## See also

**Reference**

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)

[**GET\_X\_LPARAM**](/windows/desktop/api/windowsx/nf-windowsx-get_x_lparam)

[**GET\_Y\_LPARAM**](/windows/desktop/api/windowsx/nf-windowsx-get_y_lparam)

**Conceptual**

[Mouse Input](mouse-input.md)

**Other Resources**

[**MAKEPOINTS**](/windows/desktop/api/wingdi/nf-wingdi-makepoints)

[**POINTS**](/previous-versions//dd162808(v=vs.85))