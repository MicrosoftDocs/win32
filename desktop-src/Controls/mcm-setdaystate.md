---
title: MCM_SETDAYSTATE message (Commctrl.h)
description: Sets the day states for all months that are currently visible within a month calendar control. You can send this message explicitly or by using the MonthCal\_SetDayState macro.
ms.assetid: 518cb2a9-ea82-40b4-88ca-f901b6f9f8c4
keywords:
- MCM_SETDAYSTATE message Windows Controls
topic_type:
- apiref
api_name:
- MCM_SETDAYSTATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_SETDAYSTATE message

Sets the day states for all months that are currently visible within a month calendar control. You can send this message explicitly or by using the [**MonthCal\_SetDayState**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_setdaystate) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value indicating how many elements are in the array that *lParam* points to.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an array of [**MONTHDAYSTATE**](monthdaystate.md) values that define how the month calendar control will draw each day in its display.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

An application can explicitly set day state information by sending this message, but the state will not persist when a different part of the calendar is scrolled into view. Day state information is usually set in response to the [MCN\_GETDAYSTATE](mcn-getdaystate.md) notification code, which is sent whenever the control needs to be refreshed.

The array at *lParam* must contain as many elements as the value returned by the following macro:

`MonthCal_GetMonthRange(hwndMC, GMR_DAYSTATE, NULL);`

Keep in mind that the array at *lParam* must contain [**MONTHDAYSTATE**](monthdaystate.md) values that correspond with all months currently in the control's display, in chronological order. This includes the two months that may be partially displayed before the first month and after the last month.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[Using Month Calendar Controls](using-month-calendar-controls.md)
</dt> </dl>

 

 





