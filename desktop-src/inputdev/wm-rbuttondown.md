---
title: WM\_RBUTTONDOWN message
description: Posted when the user presses the right mouse button while the cursor is in the client area of a window.
ms.assetid: da1a7d7c-6e49-4097-8b43-dcee7bd5fb3f
keywords:
- WM_RBUTTONDOWN message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_RBUTTONDOWN
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

# WM\_RBUTTONDOWN message

Posted when the user presses the right mouse button while the cursor is in the client area of a window. If the mouse is not captured, the message is posted to the window beneath the cursor. Otherwise, the message is posted to the window that has captured the mouse.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
#define WM_RBUTTONDOWN                  0x0204
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Indicates whether various virtual keys are down. This parameter can be one or more of the following values.



| Value                                                                                                                                                                                                               | Meaning                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| <span id="MK_CONTROL"></span><span id="mk_control"></span><dl> <dt>**MK\_CONTROL**</dt> <dt>0x0008</dt> </dl>    | The CTRL key is down.<br/>            |
| <span id="MK_LBUTTON"></span><span id="mk_lbutton"></span><dl> <dt>**MK\_LBUTTON**</dt> <dt>0x0001</dt> </dl>    | The left mouse button is down.<br/>   |
| <span id="MK_MBUTTON"></span><span id="mk_mbutton"></span><dl> <dt>**MK\_MBUTTON**</dt> <dt>0x0010</dt> </dl>    | The middle mouse button is down.<br/> |
| <span id="MK_RBUTTON"></span><span id="mk_rbutton"></span><dl> <dt>**MK\_RBUTTON**</dt> <dt>0x0002</dt> </dl>    | The right mouse button is down.<br/>  |
| <span id="MK_SHIFT"></span><span id="mk_shift"></span><dl> <dt>**MK\_SHIFT**</dt> <dt>0x0004</dt> </dl>          | The SHIFT key is down.<br/>           |
| <span id="MK_XBUTTON1"></span><span id="mk_xbutton1"></span><dl> <dt>**MK\_XBUTTON1**</dt> <dt>0x0020</dt> </dl> | The first X button is down.<br/>      |
| <span id="MK_XBUTTON2"></span><span id="mk_xbutton2"></span><dl> <dt>**MK\_XBUTTON2**</dt> <dt>0x0040</dt> </dl> | The second X button is down.<br/>     |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word specifies the x-coordinate of the cursor. The coordinate is relative to the upper-left corner of the client area.

The high-order word specifies the y-coordinate of the cursor. The coordinate is relative to the upper-left corner of the client area.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

Use the following code to obtain the horizontal and vertical position:


```
xPos = GET_X_LPARAM(lParam); 
yPos = GET_Y_LPARAM(lParam); 
```



As noted above, the x-coordinate is in the low-order **short** of the return value; the y-coordinate is in the high-order **short** (both represent *signed* values because they can take negative values on systems with multiple monitors). If the return value is assigned to a variable, you can use the [**MAKEPOINTS**](https://msdn.microsoft.com/library/windows/desktop/dd145043) macro to obtain a [**POINTS**](https://msdn.microsoft.com/library/windows/desktop/dd162808) structure from the return value. You can also use the [**GET\_X\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632654) or [**GET\_Y\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632655) macro to extract the x- or y-coordinate.

> \[!Important\]  
> Do not use the [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) or [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) macros to extract the x- and y- coordinates of the cursor position because these macros return incorrect results on systems with multiple monitors. Systems with multiple monitors can have negative x- and y- coordinates, and **LOWORD** and **HIWORD** treat the coordinates as unsigned quantities.

 

To detect that the ALT key was pressed, check whether [**GetKeyState**](/windows/win32/Winuser/nf-winuser-getkeystate?branch=master) with **VK\_MENU** &lt; 0. Note, this must not be [**GetAsyncKeyState**](/windows/win32/Winuser/nf-winuser-getasynckeystate?branch=master).

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

[**GET\_X\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632654)
</dt> <dt>

[**GET\_Y\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632655)
</dt> <dt>

[**GetCapture**](/windows/win32/Winuser/nf-winuser-getcapture?branch=master)
</dt> <dt>

[**GetKeyState**](/windows/win32/Winuser/nf-winuser-getkeystate?branch=master)
</dt> <dt>

[**SetCapture**](/windows/win32/Winuser/nf-winuser-setcapture?branch=master)
</dt> <dt>

[**WM\_RBUTTONDBLCLK**](wm-rbuttondblclk.md)
</dt> <dt>

[**WM\_RBUTTONUP**](wm-rbuttonup.md)
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

 

 





