---
title: MCM_GETCALENDARCOUNT message (Commctrl.h)
description: Gets the number of calendars currently displayed in the calendar control. You can send this message explicitly or by using the MonthCal\_GetCalendarCount macro.
ms.assetid: b9463f02-d37b-49b0-8387-0938020c23ee
keywords:
- MCM_GETCALENDARCOUNT message Windows Controls
topic_type:
- apiref
api_name:
- MCM_GETCALENDARCOUNT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_GETCALENDARCOUNT message

Gets the number of calendars currently displayed in the calendar control. You can send this message explicitly or by using the [**MonthCal\_GetCalendarCount**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_getcalendarcount) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

Number of calendars currently displayed in the calendar control. The maximum number of allowed calendars is 12.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





