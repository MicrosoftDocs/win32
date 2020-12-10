---
title: WM_MENUSELECT message (Winuser.h)
description: Sent to a menu's owner window when the user selects a menu item.
ms.assetid: 57684a19-dfaa-4e0c-a8ff-010533322cb0
keywords:
- WM_MENUSELECT message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_MENUSELECT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MENUSELECT message

Sent to a menu's owner window when the user selects a menu item.


```C++
#define WM_MENUSELECT                   0x011F
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The low-order word specifies the menu item or submenu index. If the selected item is a command item, this parameter contains the identifier of the menu item. If the selected item opens a drop-down menu or submenu, this parameter contains the index of the drop-down menu or submenu in the main menu, and the *lParam* parameter contains the handle to the main (clicked) menu; use the [**GetSubMenu**](/windows/desktop/api/Winuser/nf-winuser-getsubmenu) function to get the menu handle to the drop-down menu or submenu.

The high-order word specifies one or more menu flags. This parameter can be one or more of the following values.



| Value                                                                                                                                                                                                                             | Meaning                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MF_BITMAP"></span><span id="mf_bitmap"></span><dl> <dt>**MF\_BITMAP**</dt> <dt>0x00000004L</dt> </dl>                | Item displays a bitmap.<br/>                                                                                                 |
| <span id="MF_CHECKED"></span><span id="mf_checked"></span><dl> <dt>**MF\_CHECKED**</dt> <dt>0x00000008L</dt> </dl>             | Item is checked.<br/>                                                                                                        |
| <span id="MF_DISABLED"></span><span id="mf_disabled"></span><dl> <dt>**MF\_DISABLED**</dt> <dt>0x00000002L</dt> </dl>          | Item is disabled.<br/>                                                                                                       |
| <span id="MF_GRAYED"></span><span id="mf_grayed"></span><dl> <dt>**MF\_GRAYED**</dt> <dt>0x00000001L</dt> </dl>                | Item is grayed.<br/>                                                                                                         |
| <span id="MF_HILITE"></span><span id="mf_hilite"></span><dl> <dt>**MF\_HILITE**</dt> <dt>0x00000080L</dt> </dl>                | Item is highlighted.<br/>                                                                                                    |
| <span id="MF_MOUSESELECT"></span><span id="mf_mouseselect"></span><dl> <dt>**MF\_MOUSESELECT**</dt> <dt>0x00008000L</dt> </dl> | Item is selected with the mouse.<br/>                                                                                        |
| <span id="MF_OWNERDRAW"></span><span id="mf_ownerdraw"></span><dl> <dt>**MF\_OWNERDRAW**</dt> <dt>0x00000100L</dt> </dl>       | Item is an owner-drawn item.<br/>                                                                                            |
| <span id="MF_POPUP"></span><span id="mf_popup"></span><dl> <dt>**MF\_POPUP**</dt> <dt>0x00000010L</dt> </dl>                   | Item opens a drop-down menu or submenu.<br/>                                                                                 |
| <span id="MF_SYSMENU"></span><span id="mf_sysmenu"></span><dl> <dt>**MF\_SYSMENU**</dt> <dt>0x00002000L</dt> </dl>             | Item is contained in the window menu. The *lParam* parameter contains a handle to the menu associated with the message.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the menu that was clicked.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

If the high-order word of *wParam* contains 0xFFFF and the *lParam* parameter contains **NULL**, the system has closed the menu.

Do not use the value  1 for the high-order word of *wParam*, because this value is specified as (**UINT**) [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))(*wParam*). If the value is 0xFFFF, it would be interpreted as 0x0000FFFF, not  1, because of the cast to a **UINT**.

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

[**GetSubMenu**](/windows/desktop/api/Winuser/nf-winuser-getsubmenu)
</dt> <dt>

[**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))
</dt> <dt>

[**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Accelerators](keyboard-accelerators.md)
</dt> </dl>

 

