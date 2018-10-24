---
title: WM_MOUSEHWHEEL message
description: Sent to the active window when the mouse's horizontal scroll wheel is tilted or rotated.
ms.assetid: 4d6a3d73-38ef-450d-89d2-2d381fc7a7c3
keywords:
- WM_MOUSEHWHEEL message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_MOUSEHWHEEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_MOUSEHWHEEL message

Sent to the active window when the mouse's horizontal scroll wheel is tilted or rotated. The [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function propagates the message to the window's parent. There should be no internal forwarding of the message, since **DefWindowProc** propagates it up the parent chain until it finds a window that processes it.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
#define WM_MOUSEHWHEEL                  0x020E
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The high-order word indicates the distance the wheel is rotated, expressed in multiples or factors of **WHEEL\_DELTA**, which is set to 120. A positive value indicates that the wheel was rotated to the right; a negative value indicates that the wheel was rotated to the left.

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

Use the following code to obtain the information in the *wParam* parameter.


```
fwKeys = GET_KEYSTATE_WPARAM(wParam);
zDelta = GET_WHEEL_DELTA_WPARAM(wParam);
```



Use the following code to obtain the horizontal and vertical position.


```
xPos = GET_X_LPARAM(lParam); 
yPos = GET_Y_LPARAM(lParam);
```



As noted above, the x-coordinate is in the low-order **short** of the return value; the y-coordinate is in the high-order **short** (both represent *signed* values because they can take negative values on systems with multiple monitors). If the return value is assigned to a variable, you can use the [**MAKEPOINTS**](https://msdn.microsoft.com/library/windows/desktop/dd145043) macro to obtain a [**POINTS**](https://msdn.microsoft.com/library/windows/desktop/dd162808) structure from the return value. You can also use the [**GET\_X\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632654) or [**GET\_Y\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632655) macro to extract the x- or y-coordinate.

> \[!Important\]  
> Do not use the [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) or [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) macros to extract the x- and y- coordinates of the cursor position because these macros return incorrect results on systems with multiple monitors. Systems with multiple monitors can have negative x- and y- coordinates, and **LOWORD** and **HIWORD** treat the coordinates as unsigned quantities.

 

The wheel rotation is a multiple of **WHEEL\_DELTA**, which is set to 120. This is the threshold for action to be taken, and one such action (for example, scrolling one increment) should occur for each delta.

The delta was set to 120 to allow Microsoft or other vendors to build finer-resolution wheels (for example, a freely-rotating wheel with no notches) to send more messages per rotation, but with a smaller value in each message. To use this feature, you can either add the incoming delta values until **WHEEL\_DELTA** is reached (so for a delta-rotation you get the same response), or scroll partial lines in response to more frequent messages. You can also choose your scroll granularity and accumulate deltas until it is reached.

## Requirements



|                                     |                                                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windowsx.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**GET\_KEYSTATE\_WPARAM**](https://msdn.microsoft.com/en-us/library/ms646251(v=VS.85).aspx)
</dt> <dt>

[**GET\_X\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632654)
</dt> <dt>

[**GET\_Y\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632655)
</dt> <dt>

[**GET\_WHEEL\_DELTA\_WPARAM**](https://msdn.microsoft.com/en-us/library/ms646254(v=VS.85).aspx)
</dt> <dt>

[**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657)
</dt> <dt>

[**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659)
</dt> <dt>

[**mouse\_event**](https://msdn.microsoft.com/en-us/library/ms646260(v=VS.85).aspx)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Mouse Input](mouse-input.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**GetSystemMetrics**](https://msdn.microsoft.com/library/windows/desktop/ms724385)
</dt> <dt>

[**MAKEPOINTS**](https://msdn.microsoft.com/library/windows/desktop/dd145043)
</dt> <dt>

[**POINTS**](https://msdn.microsoft.com/library/windows/desktop/dd162808)
</dt> <dt>

[**SystemParametersInfo**](https://msdn.microsoft.com/library/windows/desktop/ms724947)
</dt> </dl>

 

 





