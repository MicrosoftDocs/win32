---
title: WM_MENURBUTTONUP message (Winuser.h)
description: Sent when the user releases the right mouse button while the cursor is on a menu item.
ms.assetid: e061cba0-6aea-4df4-a39a-7e55f0db45c0
keywords:
- WM_MENURBUTTONUP message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_MENURBUTTONUP
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MENURBUTTONUP message

Sent when the user releases the right mouse button while the cursor is on a menu item.


```C++
#define WM_MENURBUTTONUP                0x0122
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the menu item on which the right mouse button was released.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the menu containing the item.

</dd> </dl>

## Remarks

The **WM\_MENURBUTTONUP** message allows applications to provide a context-sensitive menu also known as a shortcut menu for the menu item specified in this message. To display a context-sensitive menu for a menu item, call the [**TrackPopupMenuEx**](/windows/desktop/api/Winuser/nf-winuser-trackpopupmenuex) function with **TPM\_RECURSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Menus Overview](menus.md)
</dt> </dl>

 

 





