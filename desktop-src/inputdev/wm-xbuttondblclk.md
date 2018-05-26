---
title: WM\_XBUTTONDBLCLK message
description: Posted when the user double-clicks the first or second X button while the cursor is in the client area of a window.
ms.assetid: 68f7abaf-cf6d-499a-957f-3c4d73cdbdee
keywords:
- WM_XBUTTONDBLCLK message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_XBUTTONDBLCLK
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_XBUTTONDBLCLK message

Posted when the user double-clicks the first or second X button while the cursor is in the client area of a window. If the mouse is not captured, the message is posted to the window beneath the cursor. Otherwise, the message is posted to the window that has captured the mouse.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
#define WM_XBUTTONDBLCLK                0x020D
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The low-order word indicates whether various virtual keys are down. It can be one or more of the following values.



| Value                                                                                                                                                                                                               | Meaning                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| <span id="MK_CONTROL"></span><span id="mk_control"></span><dl> <dt>**MK\_CONTROL**</dt> <dt>0x0008</dt> </dl>    | The CTRL key is down.<br/>            |
| <span id="MK_LBUTTON"></span><span id="mk_lbutton"></span><dl> <dt>**MK\_LBUTTON**</dt> <dt>0x0001</dt> </dl>    | The left mouse button is down.<br/>   |
| <span id="MK_MBUTTON"></span><span id="mk_mbutton"></span><dl> <dt>**MK\_MBUTTON**</dt> <dt>0x0010</dt> </dl>    | The middle mouse button is down.<br/> |
| <span id="MK_RBUTTON"></span><span id="mk_rbutton"></span><dl> <dt>**MK\_RBUTTON**</dt> <dt>0x0002</dt> </dl>    | The right mouse button is down.<br/>  |
| <span id="MK_SHIFT"></span><span id="mk_shift"></span><dl> <dt>**MK\_SHIFT**</dt> <dt>0x0004</dt> </dl>          | The SHIFT key is down.<br/>           |
| <span id="MK_XBUTTON1"></span><span id="mk_xbutton1"></span><dl> <dt>**MK\_XBUTTON1**</dt> <dt>0x0020</dt> </dl> | The first X button is down.<br/>      |
| <span id="MK_XBUTTON2"></span><span id="mk_xbutton2"></span><dl> <dt>**MK\_XBUTTON2**</dt> <dt>0x0040</dt> </dl> | The second X button is down.<br/>     |



 

The high-order word indicates which button was double-clicked. It can be one of the following values.



| Value                                                                                                                                                                                                     | Meaning                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <span id="XBUTTON1"></span><span id="xbutton1"></span><dl> <dt>**XBUTTON1**</dt> <dt>0x0001</dt> </dl> | The first X button was double-clicked.<br/>  |
| <span id="XBUTTON2"></span><span id="xbutton2"></span><dl> <dt>**XBUTTON2**</dt> <dt>0x0002</dt> </dl> | The second X button was double-clicked.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word specifies the x-coordinate of the cursor. The coordinate is relative to the upper-left corner of the client area.

The high-order word specifies the y-coordinate of the cursor. The coordinate is relative to the upper-left corner of the client area.

</dd> </dl>

## Return value

If an application processes this message, it should return **TRUE**. For more information about processing the return value, see the Remarks section.

## Remarks

Use the following code to get the information in the *wParam* parameter:


```
fwKeys = GET_KEYSTATE_WPARAM (wParam); 
fwButton = GET_XBUTTON_WPARAM (wParam); 
```



Use the following code to obtain the horizontal and vertical position:


```
xPos = GET_X_LPARAM(lParam); 
yPos = GET_Y_LPARAM(lParam); 
```



As noted above, the x-coordinate is in the low-order **short** of the return value; the y-coordinate is in the high-order **short** (both represent *signed* values because they can take negative values on systems with multiple monitors). If the return value is assigned to a variable, you can use the [**MAKEPOINTS**](https://msdn.microsoft.com/library/windows/desktop/dd145043) macro to obtain a [**POINTS**](https://msdn.microsoft.com/library/windows/desktop/dd162808) structure from the return value. You can also use the [**GET\_X\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632654) or [**GET\_Y\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632655) macro to extract the x- or y-coordinate.

> \[!Important\]  
> Do not use the [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) or [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) macros to extract the x- and y- coordinates of the cursor position because these macros return incorrect results on systems with multiple monitors. Systems with multiple monitors can have negative x- and y- coordinates, and **LOWORD** and **HIWORD** treat the coordinates as unsigned quantities.

 

Only windows that have the **CS\_DBLCLKS** style can receive **WM\_XBUTTONDBLCLK** messages, which the system generates whenever the user presses, releases, and again presses an X button within the system's double-click time limit. Double-clicking one of these buttons actually generates four messages: [**WM\_XBUTTONDOWN**](wm-xbuttondown.md), [**WM\_XBUTTONUP**](wm-xbuttonup.md), **WM\_XBUTTONDBLCLK**, and **WM\_XBUTTONUP** again.

Unlike the [**WM\_LBUTTONDBLCLK**](wm-lbuttondblclk.md), [**WM\_MBUTTONDBLCLK**](wm-mbuttondblclk.md), and [**WM\_RBUTTONDBLCLK**](wm-rbuttondblclk.md) messages, an application should return **TRUE** from this message if it processes it. Doing so will allow software that simulates this message on Windows systems earlier than Windows 2000 to determine whether the window procedure processed the message or called [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) to process it.

## Requirements



|                                     |                                                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windowsx.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572)
</dt> <dt>

[**GET\_KEYSTATE\_WPARAM**](/windows/win32/Winuser/nf-winuser-get_keystate_wparam?branch=master)
</dt> <dt>

[**GET\_X\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632654)
</dt> <dt>

[**GET\_XBUTTON\_WPARAM**](/windows/win32/Winuser/nf-winuser-get_xbutton_wparam?branch=master)
</dt> <dt>

[**GET\_Y\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632655)
</dt> <dt>

[**GetCapture**](/windows/win32/Winuser/nf-winuser-getcapture?branch=master)
</dt> <dt>

[**GetDoubleClickTime**](/windows/win32/Winuser/nf-winuser-getdoubleclicktime?branch=master)
</dt> <dt>

[**SetDoubleClickTime**](/windows/win32/Winuser/nf-winuser-setdoubleclicktime?branch=master)
</dt> <dt>

[**WM\_XBUTTONDOWN**](wm-xbuttondown.md)
</dt> <dt>

[**WM\_XBUTTONUP**](wm-xbuttonup.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Mouse Input](mouse-input.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**MAKEPOINTS**](https://msdn.microsoft.com/library/windows/desktop/dd145043)
</dt> <dt>

[**POINTS**](https://msdn.microsoft.com/library/windows/desktop/dd162808)
</dt> </dl>

 

 





