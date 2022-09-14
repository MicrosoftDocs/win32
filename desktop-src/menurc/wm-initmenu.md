---
title: WM_INITMENU message (Winuser.h)
description: Sent when a menu is about to become active.
ms.assetid: d0fcc6d8-f57c-4d04-b9e7-4cfab6add173
keywords:
- WM_INITMENU message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_INITMENU
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_INITMENU message

Sent when a menu is about to become active. It occurs when the user clicks an item on the menu bar or presses a menu key. This allows the application to modify the menu before it is displayed.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
#define WM_INITMENU                     0x0116
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the menu to be initialized.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

A **WM\_INITMENU** message is sent only when a menu is first accessed; only one **WM\_INITMENU** message is generated for each access. For example, moving the mouse across several menu items while holding down the button does not generate new messages. **WM\_INITMENU** does not provide information about menu items.

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

[**WM\_INITMENUPOPUP**](wm-initmenupopup.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Accelerators](keyboard-accelerators.md)
</dt> </dl>

 

