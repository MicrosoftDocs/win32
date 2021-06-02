---
description: An application sends the WM\_MDICREATE message to a multiple-document interface (MDI) client window to create an MDI child window.
ms.assetid: f2313ffd-867f-4870-a667-3e5f5402776f
title: WM_MDICREATE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MDICREATE message

An application sends the **WM\_MDICREATE** message to a multiple-document interface (MDI) client window to create an MDI child window.


```C++
#define WM_MDICREATE                    0x0220
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**MDICREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-mdicreatestructa) structure containing information that the system uses to create the MDI child window.

</dd> </dl>

## Return value

Type: **HWND**

If the message succeeds, the return value is the handle to the new child window.

If the message fails, the return value is **NULL**.

## Remarks

The MDI child window is created with the [**window style**](window-styles.md) bits **WS\_CHILD**, **WS\_CLIPSIBLINGS**, **WS\_CLIPCHILDREN**, **WS\_SYSMENU**, **WS\_CAPTION**, **WS\_THICKFRAME**, **WS\_MINIMIZEBOX**, and **WS\_MAXIMIZEBOX**, plus additional style bits specified in the [**MDICREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-mdicreatestructa) structure. The system adds the title of the new child window to the window menu of the frame window. An application should use this message to create all child windows of the client window.

If an MDI client window receives any message that changes the activation of its child windows while the active child window is maximized, the system restores the active child window and maximizes the newly activated child window.

When an MDI child window is created, the system sends the [**WM\_CREATE**](wm-create.md) message to the window. The *lParam* parameter of the **WM\_CREATE** message contains a pointer to a [**CREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-createstructa) structure. The *lpCreateParams* member of this structure contains a pointer to the [**MDICREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-mdicreatestructa) structure passed with the **WM\_MDICREATE** message that created the MDI child window.

An application should not send a second **WM\_MDICREATE** message while a **WM\_MDICREATE** message is still being processed. For example, it should not send a **WM\_MDICREATE** message while an MDI child window is processing its **WM\_MDICREATE** message.

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

[**CreateMDIWindow**](/windows/win32/api/winuser/nf-winuser-createmdiwindowa)
</dt> <dt>

[**CREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-createstructa)
</dt> <dt>

[**MDICREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-mdicreatestructa)
</dt> <dt>

[**WM\_CREATE**](wm-create.md)
</dt> <dt>

[**WM\_MDIDESTROY**](wm-mdidestroy.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Multiple Document Interface](multiple-document-interface.md)
</dt> </dl>

 

 
