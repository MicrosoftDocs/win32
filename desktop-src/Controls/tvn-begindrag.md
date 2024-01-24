---
title: TVN_BEGINDRAG notification code (Commctrl.h)
description: Notifies a tree-view control's parent window that a drag-and-drop operation involving the left mouse button is being initiated. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: e118354a-329e-424c-b137-78342cc00957
keywords:
- TVN_BEGINDRAG notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_BEGINDRAG
- TVN_BEGINDRAGA
- TVN_BEGINDRAGW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_BEGINDRAG notification code

Notifies a tree-view control's parent window that a drag-and-drop operation involving the left mouse button is being initiated. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_BEGINDRAG 

    pnmtv = (LPNMTREEVIEW) lParam 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTREEVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmtreeviewa) structure. The **itemNew** member is a [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure that contains valid information about the item being dragged in the **hItem**, **state**, and **lParam** members. The **ptDrag** member specifies the current screen coordinates of the mouse.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

A tree-view control that has the [**TVS\_DISABLEDRAGDROP**](tree-view-control-window-styles.md) style does not send this notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_BEGINDRAGW** (Unicode) and **TVN\_BEGINDRAGA** (ANSI)<br/>               |



 

 





