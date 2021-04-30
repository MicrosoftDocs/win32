---
title: WM_CTLCOLORDLG message (Winuser.h)
description: Sent to a dialog box before the system draws the dialog box. By responding to this message, the dialog box can set its text and background colors using the specified display device context handle.
ms.assetid: 5b90ab3f-b751-486f-a0fa-33f791c31a26
keywords:
- WM_CTLCOLORDLG message Dialog Boxes
topic_type:
- apiref
api_name:
- WM_CTLCOLORDLG
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CTLCOLORDLG message

Sent to a dialog box before the system draws the dialog box. By responding to this message, the dialog box can set its text and background colors using the specified display device context handle.


```C++
#define WM_CTLCOLORDLG                  0x0136
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the device context for the dialog box.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the dialog box.

</dd> </dl>

## Return value

If an application processes this message, it must return a handle to a brush. The system uses the brush to paint the background of the dialog box.

## Remarks

By default, the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function selects the default system colors for the dialog box.

The system does not automatically destroy the returned brush. It is the application's responsibility to destroy the brush when it is no longer needed.

The **WM\_CTLCOLORDLG** message is never sent between threads. It is sent only within one thread.

Note that the **WM\_CTLCOLORDLG** message is sent to the dialog box itself; all of the other **WM\_CTLCOLOR\*** messages are sent to the owner of the control.

If a dialog box procedure handles this message, it should cast the desired return value to an **INT\_PTR** and return the value directly. If the dialog box procedure returns **FALSE**, then default message handling is performed. The **DWL\_MSGRESULT** value set by the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function is ignored.

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

[**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dialog Boxes](dialog-boxes.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**RealizePalette**](/windows/desktop/api/wingdi/nf-wingdi-realizepalette)
</dt> <dt>

[**SelectPalette**](/windows/desktop/api/wingdi/nf-wingdi-selectpalette)
</dt> </dl>

 

