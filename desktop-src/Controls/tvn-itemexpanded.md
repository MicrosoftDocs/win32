---
title: TVN_ITEMEXPANDED notification code (Commctrl.h)
description: Notifies a tree-view control's parent window that a parent item's list of child items has expanded or collapsed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 18d9d61d-6ec5-4d3b-9c02-36d0e61ed232
keywords:
- TVN_ITEMEXPANDED notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_ITEMEXPANDED
- TVN_ITEMEXPANDEDA
- TVN_ITEMEXPANDEDW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_ITEMEXPANDED notification code

Notifies a tree-view control's parent window that a parent item's list of child items has expanded or collapsed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_ITEMEXPANDED 

    pnmtv = (LPNMTREEVIEW) lParam 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTREEVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmtreeviewa) structure. The **itemNew** member is a [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure that contains valid information about the parent item in the **hItem**, **state**, and **lParam** members. The **action** member indicates whether the list expanded or collapsed. For a list of possible values, see the description of the [**TVM\_EXPAND**](tvm-expand.md) message.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_ITEMEXPANDEDW** (Unicode) and **TVN\_ITEMEXPANDEDA** (ANSI)<br/>         |



## See also

<dl> <dt>

[TVN\_ITEMEXPANDING](tvn-itemexpanding.md)
</dt> </dl>

 

 





