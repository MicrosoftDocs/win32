---
title: WM_ACTIVATE message (Winuser.h)
description: Sent to both the window being activated and the window being deactivated.
ms.assetid: a62bb9f7-f286-4d0d-a1ca-370950c188b2
keywords:
- WM_ACTIVATE message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_ACTIVATE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_ACTIVATE message

Sent to both the window being activated and the window being deactivated. If the windows use the same input queue, the message is sent synchronously, first to the window procedure of the top-level window being deactivated, then to the window procedure of the top-level window being activated. If the windows use different input queues, the message is sent asynchronously, so the window is activated immediately.


```C++
#define WM_ACTIVATE                     0x0006
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The low-order word specifies whether the window is being activated or deactivated. This parameter can be one of the following values. The high-order word specifies the minimized state of the window being activated or deactivated. A nonzero value indicates the window is minimized.



| Value                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WA_ACTIVE"></span><span id="wa_active"></span><dl> <dt>**WA\_ACTIVE**</dt> <dt>1</dt> </dl>                | Activated by some method other than a mouse click (for example, by a call to the [**SetActiveWindow**](/windows/win32/api/winuser/nf-winuser-setactivewindow) function or by use of the keyboard interface to select the window).<br/> |
| <span id="WA_CLICKACTIVE"></span><span id="wa_clickactive"></span><dl> <dt>**WA\_CLICKACTIVE**</dt> <dt>2</dt> </dl> | Activated by a mouse click.<br/>                                                                                                                                                                     |
| <span id="WA_INACTIVE"></span><span id="wa_inactive"></span><dl> <dt>**WA\_INACTIVE**</dt> <dt>0</dt> </dl>          | Deactivated.<br/>                                                                                                                                                                                    |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the window being activated or deactivated, depending on the value of the *wParam* parameter. If the low-order word of *wParam* is **WA\_INACTIVE**, *lParam* is the handle to the window being activated. If the low-order word of *wParam* is **WA\_ACTIVE** or **WA\_CLICKACTIVE**, *lParam* is the handle to the window being deactivated. This handle can be **NULL**.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

If the window is being activated and is not minimized, the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function sets the keyboard focus to the window. If the window is activated by a mouse click, it also receives a [**WM\_MOUSEACTIVATE**](wm-mouseactivate.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**SetActiveWindow**](/windows/win32/api/winuser/nf-winuser-setactivewindow)
</dt> <dt>

[**WM\_MOUSEACTIVATE**](wm-mouseactivate.md)
</dt> <dt>

[**WM\_NCACTIVATE**](/windows/desktop/winmsg/wm-ncactivate)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Input](keyboard-input.md)
</dt> </dl>

 

