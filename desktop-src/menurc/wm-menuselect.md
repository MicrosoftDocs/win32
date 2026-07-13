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
ms.date: 09/26/2025
---

# WM\_MENUSELECT message

Sent to a menu's owner window when the user selects a menu item.

```cpp
#define WM_MENUSELECT                   0x011F
```

## Parameters

<dl> <dt>

*wParam*
</dt> <dd>

The low-order word specifies the menu item or submenu index. If the selected item is a command item, this parameter contains the identifier of the menu item. If the selected item opens a drop-down menu or submenu, this parameter contains the index of the drop-down menu or submenu in the main menu, and the *lParam* parameter contains the handle to the main menu; use the [**GetSubMenu**](/windows/desktop/api/Winuser/nf-winuser-getsubmenu) function to get the menu handle to the drop-down menu or submenu.

The high-order word specifies one or more menu flags. This parameter can be one or more of the following values.

| Value   | Meaning |
|--|--|
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

A handle to the main menu.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

This message is sent to a menu's owner window when the user selects a menu item in an open menu, typically by mouse-over or keyboard navigation. If the menu is closed, this message is not sent when the user moves the mouse over a top-level menu item. This message is sent only after the menu is opened by the user clicking a top-level menu item or pressing the <kbd>ALT</kbd> key.

> [!IMPORTANT]
> When a user clicks a menu item or presses **Enter** to invoke a selected menu item, a [WM_COMMAND](wm-command.md) or [WM_MENUCOMMAND](wm-menucommand.md) message is sent to the window, depending on the value of the **dwStyle** member of the [**MENUINFO**](/windows/win32/api/winuser/ns-winuser-menuinfo) structure for the menu. Use those messages to perform an action when the selected command is invoked.

If the high-order word of *wParam* contains 0xFFFF and the *lParam* parameter contains **NULL**, the system has closed the menu.

Do not use the value -1 for the high-order word of *wParam*, because this value is specified as (**UINT**) [**HIWORD**](../winmsg/hiword.md)(*wParam*). Even though 0xFFFF might be interpreted as -1 in signed contexts, if the value is 0xFFFF, it would be interpreted as 0x0000FFFF, not -1, because of the cast to a **UINT**.

For example, this code checks for 0xFFFF, not -1:

```cpp
case WM_MENUSELECT:
{
    UINT menuItem = LOWORD(wParam);
    UINT flags = HIWORD(wParam);
    HMENU hMenu = (HMENU)lParam;

    // Check for 0xFFFF, not -1.
    if (flags == 0xFFFF && hMenu == NULL) {
        // No menu item selected (menu closed).
        // ...
    }
    break;
}
```

## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |

## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**GetSubMenu**](/windows/desktop/api/Winuser/nf-winuser-getsubmenu)
</dt> <dt>

[**HIWORD**](../winmsg/hiword.md)
</dt> <dt>

[**LOWORD**](../winmsg/loword.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Accelerators](keyboard-accelerators.md)
</dt> </dl>



