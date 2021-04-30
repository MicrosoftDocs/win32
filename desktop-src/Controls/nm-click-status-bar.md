---
title: NM_CLICK (status bar) notification code (Commctrl.h)
description: Notifies the parent window of a status bar control that the user has clicked the left mouse button within the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 179ccbe9-f51f-4356-b91a-10d7e3607b09
keywords:
- NM_CLICK (status bar) notification code Windows Controls
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

# NM\_CLICK (status bar) notification code

Notifies the parent window of a status bar control that the user has clicked the left mouse button within the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_CLICK

    lpnm = (LPNMMOUSE) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMMOUSE**](/windows/win32/api/commctrl/ns-commctrl-nmmouse) structure that contains additional information about this notification. The **dwItemSpec** member contains the index of the section that was clicked.

</dd> </dl>

## Return value

Return **TRUE** to indicate that the mouse click was handled and suppress default processing by the system. Return **FALSE** to allow default processing of the click.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





