---
title: TVN_ITEMEXPANDING notification code (Commctrl.h)
description: Notifies a tree-view control's parent window that a parent item's list of child items is about to expand or collapse. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 5ce256df-49e5-4fbf-9cdc-79dd2edbd8ec
keywords:
- TVN_ITEMEXPANDING notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_ITEMEXPANDING
- TVN_ITEMEXPANDINGA
- TVN_ITEMEXPANDINGW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_ITEMEXPANDING notification code

Notifies a tree-view control's parent window that a parent item's list of child items is about to expand or collapse. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_ITEMEXPANDING 

    pnmtv = (LPNMTREEVIEW) lParam 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTREEVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmtreeviewa) structure. The **itemNew** member is a [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure that contains valid information about the parent item in the **hItem**, **state**, and **lParam** members. The **action** member indicates whether the list is to expand or collapse. For a list of possible values, see the description of the [**TVM\_EXPAND**](tvm-expand.md) message.

</dd> </dl>

## Return value

Returns **TRUE** to prevent the list from expanding or collapsing.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_ITEMEXPANDINGW** (Unicode) and **TVN\_ITEMEXPANDINGA** (ANSI)<br/>       |



## See also

<dl> <dt>

[TVN\_ITEMEXPANDED](tvn-itemexpanded.md)
</dt> </dl>

 

 





