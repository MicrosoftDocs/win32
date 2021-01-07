---
description: An application sends the WM\_MDIMAXIMIZE message to a multiple-document interface (MDI) client window to maximize an MDI child window.
ms.assetid: 7c5e4157-13f6-40d7-a64a-076bd14aca0d
title: WM_MDIMAXIMIZE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MDIMAXIMIZE message

An application sends the **WM\_MDIMAXIMIZE** message to a multiple-document interface (MDI) client window to maximize an MDI child window. The system resizes the child window to make its client area fill the client window. The system places the child window's window menu icon in the rightmost position of the frame window's menu bar, and places the child window's restore icon in the leftmost position. The system also appends the title bar text of the child window to that of the frame window.


```C++
#define WM_MDIMAXIMIZE                  0x0225
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the MDI child window to be maximized.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **zero**

The return value is always zero.

## Remarks

If an MDI client window receives any message that changes the activation of its child windows while the currently active MDI child window is maximized, the system restores the active child window and maximizes the newly activated child window.

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

[**WM\_MDIRESTORE**](wm-mdirestore.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Multiple Document Interface](multiple-document-interface.md)
</dt> </dl>

 

 




