---
title: TVN_SELCHANGED notification code (Commctrl.h)
description: Notifies a tree-view control's parent window that the selection has changed from one item to another. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 682170d3-5843-4d92-afeb-c37f3502ed5d
keywords:
- TVN_SELCHANGED notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_SELCHANGED
- TVN_SELCHANGEDA
- TVN_SELCHANGEDW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_SELCHANGED notification code

Notifies a tree-view control's parent window that the selection has changed from one item to another. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_SELCHANGED 

    pnmtv = (LPNMTREEVIEW) lParam 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTREEVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmtreeviewa) structure. The **itemOld** and **itemNew** members of the **NMTREEVIEW** structure are [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structures that contain information about the previously selected item and the newly selected item. Only the **mask**, **hItem**, **state**, and **lParam** members of these structures are valid. The **stateMask** members of the **TVITEM** structures specified by **itemOld** and **itemNew** are undefined on input. The **action** member of the **NMTREEVIEW** structure indicates the type of action that caused the selection to change. It can be one of the following values:



| Requirement | Value |
|-----------------|-------------------|
| TVC\_BYKEYBOARD | By a keystroke.   |
| TVC\_BYMOUSE    | By a mouse click. |
| TVC\_UNKNOWN    | Unknown.          |



 

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_SELCHANGEDW** (Unicode) and **TVN\_SELCHANGEDA** (ANSI)<br/>             |



 

 





