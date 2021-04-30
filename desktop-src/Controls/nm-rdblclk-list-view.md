---
title: NM_RDBLCLK (list view) notification code (Commctrl.h)
description: Sent by a list-view control when the user double-clicks an item with the right mouse button. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: ebbb127f-07bd-48e0-bf38-7bbda5802f70
keywords:
- NM_RDBLCLK (list view) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_RDBLCLK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_RDBLCLK (list view) notification code

Sent by a list-view control when the user double-clicks an item with the right mouse button. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_RDBLCLK

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

The **iItem** member of *lParam* is valid only if the icon or first-column label has been clicked. To determine which item is selected when a click takes place elsewhere in a row, send an [**LVM\_SUBITEMHITTEST**](lvm-subitemhittest.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





