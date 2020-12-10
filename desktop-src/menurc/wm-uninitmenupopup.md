---
title: WM_UNINITMENUPOPUP message (Winuser.h)
description: Sent when a drop-down menu or submenu has been destroyed.
ms.assetid: 06129d88-6cf9-4d55-b8eb-6f78994bc87a
keywords:
- WM_UNINITMENUPOPUP message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_UNINITMENUPOPUP
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_UNINITMENUPOPUP message

Sent when a drop-down menu or submenu has been destroyed.


```C++
#define WM_UNINITMENUPOPUP              0x0125
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the menu

</dd> <dt>

*lParam* 
</dt> <dd>

The high-order word identifies the menu that was destroyed. Currently, this parameter can only be **MF\_SYSMENU** (the window menu).

</dd> </dl>

## Remarks

If an application receives a [**WM\_INITMENUPOPUP**](wm-initmenupopup.md) message, it will receive a **WM\_UNINITMENUPOPUP** message.

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

[**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))
</dt> <dt>

**Conceptual**
</dt> <dt>

[Menus](menus.md)
</dt> </dl>

 

