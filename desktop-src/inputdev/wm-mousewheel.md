---
title: WM_MOUSEWHEEL message (Winuser.h)
description: Sent to the focus window when the mouse wheel is rotated.
ms.assetid: 9831cceb-bbf3-42a0-a0f9-c2d6ad4573eb
keywords:
- WM_MOUSEWHEEL message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_MOUSEWHEEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MOUSEWHEEL message

Sent to the focus window when the mouse wheel is rotated. The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function propagates the message to the window's parent. There should be no internal forwarding of the message, since **DefWindowProc** propagates it up the parent chain until it finds a window that processes it.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
#define WM_MOUSEWHEEL                   0x020A
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The high-order word indicates the distance the wheel is rotated, expressed in multiples or divisions of **WHEEL\_DELTA**, which is 120. A positive value indicates that the wheel was rotated forward, away from the user; a negative value indicates that the wheel was rotated backward, toward the user.

The low-order word indicates whether various virtual keys are down. This parameter can be one or more of the following values.



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

The low-order word specifies the x-coordinate of the pointer, relative to the upper-left corner of the screen.

The high-order word specifies the y-coordinate of the pointer, relative to the upper-left corner of the screen.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

Use the following code to get the information in the *wParam* parameter:


```
fwKeys = GET_KEYSTATE_WPARAM(wParam);
zDelta = GET_WHEEL_DELTA_WPARAM(wParam);
```



Use the following code to obtain the horizontal and vertical position:


```
xPos = GET_X_LPARAM(lParam); 
yPos = GET_Y_LPARAM(lParam); 
```



As noted above, the x-coordinate is in the low-order **short** of the return value; the y-coordinate is in the high-order **short** (both represent *signed* values because they can take negative values on systems with multiple monitors). If the return value is assigned to a variable, you can use the [**MAKEPOINTS**](/windows/desktop/api/wingdi/nf-wingdi-makepoints) macro to obtain a [**POINTS**](/previous-versions//dd162808(v=vs.85)) structure from the return value. You can also use the [**GET\_X\_LPARAM**](/windows/desktop/api/windowsx/nf-windowsx-get_x_lparam) or [**GET\_Y\_LPARAM**](/windows/desktop/api/windowsx/nf-windowsx-get_y_lparam) macro to extract the x- or y-coordinate.

> [!IMPORTANT]
> Do not use the [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) or [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) macros to extract the x- and y- coordinates of the cursor position because these macros return incorrect results on systems with multiple monitors. Systems with multiple monitors can have negative x- and y- coordinates, and **LOWORD** and **HIWORD** treat the coordinates as unsigned quantities.

 

The wheel rotation will be a multiple of **WHEEL\_DELTA**, which is set at 120. This is the threshold for action to be taken, and one such action (for example, scrolling one increment) should occur for each delta.

The delta was set to 120 to allow Microsoft or other vendors to build finer-resolution wheels (a freely-rotating wheel with no notches) to send more messages per rotation, but with a smaller value in each message. To use this feature, you can either add the incoming delta values until **WHEEL\_DELTA** is reached (so for a delta-rotation you get the same response), or scroll partial lines in response to the more frequent messages. You can also choose your scroll granularity and accumulate deltas until it is reached.

Note, there is no *fwKeys* for **MSH\_MOUSEWHEEL**. Otherwise, the parameters are exactly the same as for **WM\_MOUSEWHEEL**.

It is up to the application to forward **MSH\_MOUSEWHEEL** to any embedded objects or controls. The application is required to send the message to an active embedded OLE application. It is optional that the application sends it to a wheel-enabled control with focus. If the application does send the message to a control, it can check the return value to see if the message was processed. Controls are required to return a value of **TRUE** if they process the message.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windowsx.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**GET\_KEYSTATE\_WPARAM**](/windows/win32/api/winuser/nf-winuser-get_keystate_wparam)
</dt> <dt>

[**GET\_X\_LPARAM**](/windows/desktop/api/windowsx/nf-windowsx-get_x_lparam)
</dt> <dt>

[**GET\_Y\_LPARAM**](/windows/desktop/api/windowsx/nf-windowsx-get_y_lparam)
</dt> <dt>

[**GET\_WHEEL\_DELTA\_WPARAM**](/windows/win32/api/winuser/nf-winuser-get_wheel_delta_wparam)
</dt> <dt>

[**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))
</dt> <dt>

[**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))
</dt> <dt>

[**mouse\_event**](/windows/win32/api/winuser/nf-winuser-mouse_event)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Mouse Input](mouse-input.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**GetSystemMetrics**](/windows/desktop/api/winuser/nf-winuser-getsystemmetrics)
</dt> <dt>

[**MAKEPOINTS**](/windows/desktop/api/wingdi/nf-wingdi-makepoints)
</dt> <dt>

[**POINTS**](/previous-versions//dd162808(v=vs.85))
</dt> <dt>

[**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa)
</dt> </dl>

 

