---
title: MCN_SELECT notification code (Commctrl.h)
description: Sent by a month calendar control when the user makes an explicit date selection within a month calendar control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 3cabb4b2-9422-4190-85d3-ab6593891e3d
keywords:
- MCN_SELECT notification code Windows Controls
topic_type:
- apiref
api_name:
- MCN_SELECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCN\_SELECT notification code

Sent by a month calendar control when the user makes an explicit date selection within a month calendar control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
MCN_SELECT

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

The **MCN\_SELECT** notification code is similar to [**MCN\_SELCHANGE**](mcn-selchange.md), but **MCN\_SELECT** is sent only in response to a user's explicit date selections. **MCN\_SELCHANGE** applies to any selection change.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





