---
description: An application sends the WM\_MDIACTIVATE message to a multiple-document interface (MDI) client window to instruct the client window to activate a different MDI child window.
ms.assetid: c5de18b5-fac3-4e55-9eca-3b6672df0e7b
title: WM_MDIACTIVATE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MDIACTIVATE message

An application sends the **WM\_MDIACTIVATE** message to a multiple-document interface (MDI) client window to instruct the client window to activate a different MDI child window.


```C++
#define WM_MDIACTIVATE                  0x0222
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the MDI child window to be activated.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application sends this message to an MDI client window, the return value is zero.

An MDI child window should return zero if it processes this message.

## Remarks

As the client window processes this message, it sends **WM\_MDIACTIVATE** to the child window being deactivated and to the child window being activated. The message parameters received by an MDI child window are as follows:

<dl> <dt>

<span id="wParam"></span><span id="wparam"></span><span id="WPARAM"></span>*wParam*
</dt> <dd>

A handle to the MDI child window being deactivated.

</dd> <dt>

<span id="lParam"></span><span id="lparam"></span><span id="LPARAM"></span>*lParam*
</dt> <dd>

A handle to the MDI child window being activated.

</dd> </dl>

An MDI child window is activated independently of the MDI frame window. When the frame window becomes active, the child window last activated by using the **WM\_MDIACTIVATE** message receives the [**WM\_NCACTIVATE**](wm-ncactivate.md) message to draw an active window frame and title bar; the child window does not receive another **WM\_MDIACTIVATE** message.

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

[**WM\_MDIGETACTIVE**](wm-mdigetactive.md)
</dt> <dt>

[**WM\_MDINEXT**](wm-mdinext.md)
</dt> <dt>

[**WM\_NCACTIVATE**](wm-ncactivate.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Multiple Document Interface](multiple-document-interface.md)
</dt> </dl>

 

 




