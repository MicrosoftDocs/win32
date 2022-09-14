---
title: MCM_GETMONTHDELTA message (Commctrl.h)
description: Retrieves the scroll rate for a month calendar control. The scroll rate is the number of months that the control moves its display when the user clicks a scroll button. You can send this message explicitly or by using the MonthCal\_GetMonthDelta macro.
ms.assetid: 6db02993-b22c-430f-8928-8bd5768b2151
keywords:
- MCM_GETMONTHDELTA message Windows Controls
topic_type:
- apiref
api_name:
- MCM_GETMONTHDELTA
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_GETMONTHDELTA message

Retrieves the scroll rate for a month calendar control. The scroll rate is the number of months that the control moves its display when the user clicks a scroll button. You can send this message explicitly or by using the [**MonthCal\_GetMonthDelta**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_getmonthdelta) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

If the month delta was previously set using the [**MCM\_SETMONTHDELTA**](mcm-setmonthdelta.md) message, returns an INT value that represents the month calendar's current scroll rate. If the month delta was not previously set using the **MCM\_SETMONTHDELTA** message, or the month delta was reset to the default, returns an INT value that represents the current number of months visible.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





