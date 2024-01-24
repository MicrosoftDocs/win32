---
title: DTM_GETMONTHCAL message (Commctrl.h)
description: Gets the handle to a date and time picker's (DTP) child month calendar control. You can send this message explicitly or use the DateTime\_GetMonthCal macro.
ms.assetid: 78bbdcc9-2b2b-420b-be9b-6f2f573d60b6
keywords:
- DTM_GETMONTHCAL message Windows Controls
topic_type:
- apiref
api_name:
- DTM_GETMONTHCAL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTM\_GETMONTHCAL message

Gets the handle to a date and time picker's (DTP) child month calendar control. You can send this message explicitly or use the [**DateTime\_GetMonthCal**](/windows/desktop/api/Commctrl/nf-commctrl-datetime_getmonthcal) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to a DTP control's child month calendar control if successful, or **NULL** otherwise.

## Remarks

DTP controls create a child month calendar control when the user clicks the drop-down arrow ([DTN\_DROPDOWN](dtn-dropdown.md) notification). When the month calendar is no longer needed, it is destroyed (a [DTN\_CLOSEUP](dtn-closeup.md) notification is sent on destruction). So your application must not rely on a static handle to the DTP control's child month calendar.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[DTN\_CLOSEUP](dtn-closeup.md)
</dt> <dt>

[DTN\_DROPDOWN](dtn-dropdown.md)
</dt> </dl>

 

 





