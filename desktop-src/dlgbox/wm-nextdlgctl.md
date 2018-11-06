---
title: WM_NEXTDLGCTL message
description: Sent to a dialog box procedure to set the keyboard focus to a different control in the dialog box.
ms.assetid: 63d9fac2-3057-4bfa-9960-911fd18877d4
keywords:
- WM_NEXTDLGCTL message Dialog Boxes
topic_type:
- apiref
api_name:
- WM_NEXTDLGCTL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# WM\_NEXTDLGCTL message

Sent to a dialog box procedure to set the keyboard focus to a different control in the dialog box.


```C++
#define WM_NEXTDLGCTL                   0x0028
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

If *lParam* is **TRUE**, this parameter identifies the control that receives the focus. If *lParam* is **FALSE**, this parameter indicates whether the next or previous control with the **WS\_TABSTOP** style receives the focus. If *wParam* is zero, the next control receives the focus; otherwise, the previous control with the **WS\_TABSTOP** style receives the focus.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word indicates how the system uses *wParam*. If the low-order word is **TRUE**, *wParam* is a handle associated with the control that receives the focus; otherwise, *wParam* is a flag that indicates whether the next or previous control with the **WS\_TABSTOP** style receives the focus.

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

This message performs additional dialog box management operations beyond those performed by the [**SetFocus**](https://msdn.microsoft.com/library/windows/desktop/ms646312) function **WM\_NEXTDLGCTL** updates the default pushbutton border, sets the default control identifier, and automatically selects the text of an edit control (if the target window is an edit control).

Do not use the [**SendMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644950) function to send a **WM\_NEXTDLGCTL** message if your application will concurrently process other messages that set the focus. Use the [**PostMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644944) function instead.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**PostMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644944)
</dt> <dt>

[**SendMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644950)
</dt> <dt>

[**SetFocus**](https://msdn.microsoft.com/library/windows/desktop/ms646312)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dialog Boxes](dialog-boxes.md)
</dt> </dl>

 

 





