---
title: LVN_DELETEITEM notification code (Commctrl.h)
description: Notifies a list-view control's parent window that an item is about to be deleted. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 6e3d1955-ee35-488b-8b96-3d6ebbe5ceb5
keywords:
- LVN_DELETEITEM notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_DELETEITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_DELETEITEM notification code

Notifies a list-view control's parent window that an item is about to be deleted. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_DELETEITEM

    pnmv = (LPNMLISTVIEW) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLISTVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmlistview) structure. The **iItem** member identifies the item being deleted. If the control does not have the **LVS\_OWNERDATA** style, then the *lParam* is the application-defined data associated with the item. All other members of this structure are zero.

</dd> </dl>

## Return value

No return value.

## Remarks

Do not add, delete, or rearrange items in the list view while processing this notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





