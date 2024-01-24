---
title: TVN_SELCHANGING notification code (Commctrl.h)
description: Notifies a tree-view control's parent window that the selection is about to change from one item to another. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 53f24ee0-433c-4680-9075-5e2b21117ed9
keywords:
- TVN_SELCHANGING notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_SELCHANGING
- TVN_SELCHANGINGA
- TVN_SELCHANGINGW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_SELCHANGING notification code

Notifies a tree-view control's parent window that the selection is about to change from one item to another. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_SELCHANGING 

    pnmtv = (LPNMTREEVIEW) lParam 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTREEVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmtreeviewa) structure. The **itemOld** and **itemNew** members contain valid information about the currently selected item and the newly selected item. The **action** member indicates whether a mouse or keyboard action is causing the selection to change. For a list of possible values, see the description of the [TVN\_SELCHANGED](tvn-selchanged.md) notification code.

</dd> </dl>

## Return value

Returns **TRUE** to prevent the selection from changing.

## Remarks

When responding to this notification code, applications should not delete the items that are gaining or losing the selection.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_SELCHANGINGW** (Unicode) and **TVN\_SELCHANGINGA** (ANSI)<br/>           |



 

 





