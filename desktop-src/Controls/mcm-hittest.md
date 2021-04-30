---
title: MCM_HITTEST message (Commctrl.h)
description: Determines which portion of a month calendar control is at a given point on the screen. You can send this message explicitly or by using the MonthCal\_HitTest macro.
ms.assetid: 51e74b07-4ed7-488d-ad5d-116f046577fc
keywords:
- MCM_HITTEST message Windows Controls
topic_type:
- apiref
api_name:
- MCM_HITTEST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_HITTEST message

Determines which portion of a month calendar control is at a given point on the screen. You can send this message explicitly or by using the [**MonthCal\_HitTest**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_hittest) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**MCHITTESTINFO**](/windows/desktop/api/Commctrl/ns-commctrl-mchittestinfo) structure. Upon sending the message, the **cbSize** member must be set to the size of the **MCHITTESTINFO** structure, and **pt** must be set to the point you want to hit test.

</dd> </dl>

## Return value

Sets values in members of the



| Return code                                                                                           | Description                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**MCHT\_CALENDAR**</dt> </dl>         | The given point was within the calendar.<br/>                                                                                                                                                                                                                       |
| <dl> <dt>**MCHT\_CALENDARBK**</dt> </dl>       | The given point was in the calendar's background.<br/>                                                                                                                                                                                                              |
| <dl> <dt>**MCHT\_CALENDARDATE**</dt> </dl>     | The given point was on a particular date within the calendar. The [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure at *lParam->st* is set to the date at the given point.<br/>                                                                                    |
| <dl> <dt>**MCHT\_CALENDARDATENEXT**</dt> </dl> | The given point was over a date from the next month (partially displayed at the end of the currently displayed month). If the user clicks here, the month calendar will scroll its display to the next month or set of months.<br/>                                 |
| <dl> <dt>**MCHT\_CALENDARDATEPREV**</dt> </dl> | The given point was over a date from the previous month (partially displayed at the end of the currently displayed month). If the user clicks here, the month calendar will scroll its display to the previous month or set of months.<br/>                         |
| <dl> <dt>**MCHT\_CALENDARDAY**</dt> </dl>      | The given point was over a day abbreviation ("Fri", for example). The [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure at *lParam->st* is set to the corresponding date in the top row.<br/>                                                                      |
| <dl> <dt>**MCHT\_CALENDARWEEKNUM**</dt> </dl>  | The given point was over a week number ([**MCS\_WEEKNUMBERS**](month-calendar-control-styles.md) style only). The [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure at *lParam->st* is set to the corresponding date in the leftmost column.<br/> |
| <dl> <dt>**MCHT\_NEXT**</dt> </dl>             | The given point is in an area that will cause the month calendar to scroll its display to the next month or set of months. This flag is used to modify other hit test flags.<br/>                                                                                   |
| <dl> <dt>**MCHT\_NOWHERE**</dt> </dl>          | The given point was not on the month calendar control, or it was in an inactive portion of the control.<br/>                                                                                                                                                        |
| <dl> <dt>**MCHT\_PREV**</dt> </dl>             | The given point is in an area that will cause the month calendar to scroll its display to the previous month or set of months. This flag is used to modify other hit test flags.<br/>                                                                               |
| <dl> <dt>**MCHT\_TITLE**</dt> </dl>            | The given point was over a month's title.<br/>                                                                                                                                                                                                                      |
| <dl> <dt>**MCHT\_TITLEBK**</dt> </dl>          | The given point was over the background of a month's title.<br/>                                                                                                                                                                                                    |
| <dl> <dt>**MCHT\_TITLEBTNNEXT**</dt> </dl>     | The given point was over the button at the top right corner of the control. If the user clicks here, the month calendar will scroll its display to the next month or set of months. <br/>                                                                           |
| <dl> <dt>**MCHT\_TITLEBTNPREV**</dt> </dl>     | The given point was over the button at the top left corner of the control. If the user clicks here, the month calendar will scroll its display to the previous month or set of months. <br/>                                                                        |
| <dl> <dt>**MCHT\_TITLEMONTH**</dt> </dl>       | The given point was in a month's title bar, over a month name.<br/>                                                                                                                                                                                                 |
| <dl> <dt>**MCHT\_TITLEYEAR**</dt> </dl>        | The given point was in a month's title bar, over the year value.<br/>                                                                                                                                                                                               |
| <dl> <dt>**MCHT\_TODAYLINK**</dt> </dl>        | The given point was on the "today" link at the bottom of the month calendar control.<br/> The **uHit** member of the [**MCHITTESTINFO**](/windows/desktop/api/Commctrl/ns-commctrl-mchittestinfo) structure at *lParam* will equal the return value. <br/>                                          |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

