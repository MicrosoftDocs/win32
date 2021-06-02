---
title: NM_CLICK (list view) notification code (Commctrl.h)
description: Sent by a list-view control when the user clicks an item with the left mouse button. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 7921bc27-54ca-4bb2-ac88-8267776661ab
keywords:
- NM_CLICK (list view) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_CLICK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_CLICK (list view) notification code

Sent by a list-view control when the user clicks an item with the left mouse button. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_CLICK

    lpnmitem = (LPNMITEMACTIVATE) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

[Version 4.71](common-control-versions.md). Pointer to an [**NMITEMACTIVATE**](/windows/win32/api/commctrl/ns-commctrl-nmitemactivate) structure that contains additional information about this notification. The **iItem**, **iSubItem**, and **ptAction** members of this structure contain information about the item.

</dd> </dl>

## Return value

The return value for this notification is not used.

## Remarks

The **iItem** member of *lParam* is only valid if the icon or first-column label has been clicked. To determine which item is selected when a click takes place elsewhere in a row, send an [**LVM\_SUBITEMHITTEST**](lvm-subitemhittest.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





