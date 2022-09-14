---
description: An application sends the WM\_MDINEXT message to a multiple-document interface (MDI) client window to activate the next or previous child window.
ms.assetid: a4822b99-330a-4094-bad9-b9a5923e02a8
title: WM_MDINEXT message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MDINEXT message

An application sends the **WM\_MDINEXT** message to a multiple-document interface (MDI) client window to activate the next or previous child window.


```C++
#define WM_MDINEXT                      0x0224
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the MDI child window. The system activates the child window that is immediately before or after the specified child window, depending on the value of the *lParam* parameter. If the *wParam* parameter is **NULL**, the system activates the child window that is immediately before or after the currently active child window.

</dd> <dt>

*lParam* 
</dt> <dd>

If this parameter is zero, the system activates the next MDI child window and places the child window identified by the *wParam* parameter behind all other child windows. If this parameter is nonzero, the system activates the previous child window, placing it in front of the child window identified by *wParam*.

</dd> </dl>

## Return value

Type: **zero**

The return value is always zero.

## Remarks

If an MDI client window receives any message that changes the activation of its child windows while the active MDI child window is maximized, the system restores the active child window and maximizes the newly activated child window.

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

[**WM\_MDIACTIVATE**](wm-mdiactivate.md)
</dt> <dt>

[**WM\_MDIGETACTIVE**](wm-mdigetactive.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Multiple Document Interface](multiple-document-interface.md)
</dt> </dl>

 

 




