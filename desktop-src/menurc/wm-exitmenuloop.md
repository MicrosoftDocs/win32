---
title: WM_EXITMENULOOP message (Winuser.h)
description: Notifies an application's main window procedure that a menu modal loop has been exited.
ms.assetid: b2a9d537-af7c-4c8a-932a-95e45eb8deb5
keywords:
- WM_EXITMENULOOP message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_EXITMENULOOP
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_EXITMENULOOP message

Notifies an application's main window procedure that a menu modal loop has been exited.


```C++
#define WM_EXITMENULOOP                 0x0212
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies whether the menu is a shortcut menu. This parameter has a value of **TRUE** if it is a shortcut menu, **FALSE** if it is not.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function returns zero.

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

[**WM\_ENTERMENULOOP**](wm-entermenuloop.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Menus](menus.md)
</dt> </dl>

 

