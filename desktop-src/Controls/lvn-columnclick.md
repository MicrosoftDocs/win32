---
title: LVN_COLUMNCLICK notification code (Commctrl.h)
description: Notifies a list-view control's parent window that a column header was clicked while the list-view control was in report mode. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: a6bfbd6c-4778-47a7-92e9-9140d46d89cc
keywords:
- LVN_COLUMNCLICK notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_COLUMNCLICK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_COLUMNCLICK notification code

Notifies a list-view control's parent window that a column header was clicked while the list-view control was in report mode. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_COLUMNCLICK

    pnmv = (LPNMLISTVIEW) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLISTVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmlistview) structure. The **iItem** member is -1, and the **iSubItem** member identifies the column. All other members are zero.

</dd> </dl>

## Return value

No return value.

## Remarks

Using header control formats such as HDF\_CHECKBOX to modify the format of column headers in a list-view control causes the control to send the [HDN\_ITEMSTATEICONCLICK](hdn-itemstateiconclick.md) notification code instead of LVN\_COLUMNCLICK when a header item is clicked.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





