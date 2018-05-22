---
title: NM\_RDBLCLK (status bar) notification code
description: Notifies the parent windows of a status bar control that the user has double-clicked the right mouse button within the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: '57d8c5a7-e179-4b65-a3aa-5566d5780c18'
keywords: ["NM_RDBLCLK (status bar) notification code Windows Controls"]
topic_type:
- apiref
api_name:
- NM_RDBLCLK
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# NM\_RDBLCLK (status bar) notification code

Notifies the parent windows of a status bar control that the user has double-clicked the right mouse button within the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_RDBLCLK

    lpnm = (LPNMMOUSE) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMMOUSE**](nmmouse.md) structure that contains additional information about this notification. The **dwItemSpec** member contains the index of the section that was clicked.

</dd> </dl>

## Return value

Return **TRUE** to indicate that the mouse click was handled and suppress default processing by the system. Return **FALSE** to allow default processing of the click.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





