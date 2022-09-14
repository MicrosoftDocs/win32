---
title: NM_LDOWN (toolbar) notification code (Commctrl.h)
description: Notifies a toolbar's parent window that the left mouse button has been pressed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: f5b356fb-265b-4eb0-a5a3-2a22d688f847
keywords:
- NM_LDOWN (toolbar) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_LDOWN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_LDOWN (toolbar) notification code

Notifies a toolbar's parent window that the left mouse button has been pressed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_LDOWN

    lpnmmouse = (LPNMMOUSE) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMMOUSE**](/windows/win32/api/commctrl/ns-commctrl-nmmouse) structure that contains information about this notification code. If the mouse was clicked on a toolbar item, the **dwItemSpec** member contains the item identifier and the **dwItemData** member contains the item data. If the mouse was clicked on a separator or white space in the toolbar, the **dwItemSpec** member will contain -1.

</dd> </dl>

## Return value

Returns **FALSE** to allow the toolbar control to perform default processing of the event, or **TRUE** to prevent the control from processing the event.

## Remarks

This notification is sent after the [TBN\_DROPDOWN](tbn-dropdown.md) notification code has been sent.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





