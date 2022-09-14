---
title: NM_DBLCLK (toolbar) notification code (Commctrl.h)
description: Notifies the parent window of a toolbar control that the user has double-clicked the left mouse button within the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: c6198245-cfd4-4e1f-877d-94c1d47e09d2
keywords:
- NM_DBLCLK (toolbar) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_DBLCLK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_DBLCLK (toolbar) notification code

Notifies the parent window of a toolbar control that the user has double-clicked the left mouse button within the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_DBLCLK

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

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





