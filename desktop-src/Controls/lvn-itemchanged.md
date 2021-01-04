---
title: LVN_ITEMCHANGED notification code (Commctrl.h)
description: Notifies a list-view control's parent window that an item has changed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: d5f0b4e7-0d0c-4021-942b-71fd31880599
keywords:
- LVN_ITEMCHANGED notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_ITEMCHANGED
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_ITEMCHANGED notification code

Notifies a list-view control's parent window that an item has changed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_ITEMCHANGED

    pnmv = (LPNMLISTVIEW) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLISTVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmlistview) structure that identifies the item and specifies which of its attributes have changed. If the **iItem** member of the structure pointed to by *lParam* is -1, the change has been applied to all items in the list view.

</dd> </dl>

## Return value

No return value.

## Remarks

If a list-view control has the [**LVS\_OWNERDATA**](list-view-window-styles.md) style, and the user selects a range of items by holding down the SHIFT key and clicking the mouse, LVN\_ITEMCHANGED notification codes are not sent for each selected or deselected item. Instead, you will receive a single [LVN\_ODSTATECHANGED](lvn-odstatechanged.md) notification code, indicating that a range of items has changed state.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





