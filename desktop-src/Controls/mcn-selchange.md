---
title: MCN_SELCHANGE notification code (Commctrl.h)
description: Sent by a month calendar control when the currently selected date or range of dates changes. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 8923524f-d257-409d-bd3e-021684b88856
keywords:
- MCN_SELCHANGE notification code Windows Controls
topic_type:
- apiref
api_name:
- MCN_SELCHANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCN\_SELCHANGE notification code

Sent by a month calendar control when the currently selected date or range of dates changes. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
MCN_SELCHANGE

    lpNMSelChange = (LPNMSELCHANGE) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMSELCHANGE**](/windows/win32/api/commctrl/ns-commctrl-nmselchange) structure that contains information about the currently selected date range.

</dd> </dl>

## Return value

No return value.

## Remarks

For example, the control sends MCN\_SELCHANGE when the user explicitly changes the selection within the current month or when the selection is implicitly changed in response to next/previous month navigation. This notification code is also sent by the system at regular intervals so that the control can respond to date changes.

This notification code is similar to [MCN\_SELECT](mcn-select.md), but it is sent in response to any selection change. MCN\_SELECT is sent only for an explicit date selection.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





