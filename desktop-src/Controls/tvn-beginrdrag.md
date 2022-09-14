---
title: TVN_BEGINRDRAG notification code (Commctrl.h)
description: Notifies a tree-view control's parent window about the initiation of a drag-and-drop operation involving the right mouse button. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 4a61d8b5-ceb9-46a3-95ef-27e843e8c986
keywords:
- TVN_BEGINRDRAG notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_BEGINRDRAG
- TVN_BEGINRDRAGA
- TVN_BEGINRDRAGW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_BEGINRDRAG notification code

Notifies a tree-view control's parent window about the initiation of a drag-and-drop operation involving the right mouse button. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_BEGINRDRAG 

    pnmtv = (LPNMTREEVIEW) lParam 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTREEVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmtreeviewa) structure. The **itemNew** member is a [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure that contains valid information in the **hItem**, **state**, and **lParam** members about the item to be dragged. The **ptDrag** member specifies the current screen coordinates of the mouse.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_BEGINRDRAGW** (Unicode) and **TVN\_BEGINRDRAGA** (ANSI)<br/>             |



 

 





