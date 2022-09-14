---
title: LVN_HOTTRACK notification code (Commctrl.h)
description: Sent by a list-view control when the user moves the mouse over an item. This notification code is only sent by list-view controls that have the LVS\_EX\_TRACKSELECT extended list-view style. It is sent in the form of a WM\_NOTIFY message.
ms.assetid: 6bbfe6b8-9b67-49e4-9481-65abe98608bb
keywords:
- LVN_HOTTRACK notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_HOTTRACK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_HOTTRACK notification code

Sent by a list-view control when the user moves the mouse over an item. This notification code is only sent by list-view controls that have the [**LVS\_EX\_TRACKSELECT**](extended-list-view-styles.md) extended list-view style. It is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_HOTTRACK

    lpnmlv = (LPNMLISTVIEW) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLISTVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmlistview) structure that contains information about this notification code. The **iItem**, **iSubItem**, and **ptAction** members of this structure contain information about the item. The receiving application can modify the **iItem** member to specify the item that will be selected. If **iItem** is set to -1, no item will be selected.

</dd> </dl>

## Return value

Return zero to allow the list view to perform its normal track select processing. If the application returns nonzero, the item will not be selected.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





