---
title: MCM_SETTODAY message (Commctrl.h)
description: Sets the \ 0034;today \ 0034; selection for a month calendar control. You can send this message explicitly or by using the MonthCal\_SetToday macro.
ms.assetid: fcd4d33d-e661-4e02-8d19-666d80e1a070
keywords:
- MCM_SETTODAY message Windows Controls
topic_type:
- apiref
api_name:
- MCM_SETTODAY
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_SETTODAY message

Sets the "today" selection for a month calendar control. You can send this message explicitly or by using the [**MonthCal\_SetToday**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_settoday) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure that contains the date to be set as the "today" selection for the control. If this parameter is set to **NULL**, the control returns to the default setting.

</dd> </dl>

## Return value

The return value for this message is not used.

## Remarks

If the "today" selection is set to any date other than the default, the following conditions apply:

-   The control will not automatically update the "today" selection when the time passes midnight for the current day.
-   The control will not automatically update its display based on locale changes.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[Times in the Month Calendar Control](month-calendar-controls.md)
</dt> </dl>

 

