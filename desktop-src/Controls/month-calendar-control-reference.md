---
title: Month Calendar Control Reference
description: This section contains information about programming elements used with month calendar controls.
ms.assetid: '14f358d9-2ec4-4667-8b66-57e18942eb1b'
---

# Month Calendar Control Reference

This section contains information about programming elements used with month calendar controls.

### Overviews



| Topic                                                              | Contents                                                                                |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [About Month Calendar Controls](month-calendar-controls.md)       | A month calendar control implements a calendar-like user interface.<br/>          |
| [Using Month Calendar Controls](using-month-calendar-controls.md) | This section provides information about programming month calendar controls.<br/> |



 

### Macros



| Topic                                                                 | Contents                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MonthCal\_GetCalendarBorder**](monthcal-getcalendarborder.md)     | Gets the border size, in pixels, of a month calendar control. You can use this macro or send the [**MCM\_GETCALENDARBORDER**](mcm-getcalendarborder.md) message explicitly.<br/>                                                                                                                           |
| [**MonthCal\_GetCalendarCount**](monthcal-getcalendarcount.md)       | Gets the number of calendars currently displayed in the calendar control. You can use this macro or send the [**MCM\_GETCALENDARCOUNT**](mcm-getcalendarcount.md) message explicitly.<br/>                                                                                                                 |
| [**MonthCal\_GetCalendarGridInfo**](monthcal-getcalendargridinfo.md) | Gets information about a calendar grid.<br/>                                                                                                                                                                                                                                                                |
| [**MonthCal\_GetCALID**](monthcal-getcalid.md)                       | Gets the current calendar ID for the given calendar control. You can use this macro or send the [**MCM\_GETCALID**](mcm-getcalid.md) message explicitly.<br/>                                                                                                                                              |
| [**MonthCal\_GetColor**](monthcal-getcolor.md)                       | Retrieves the color for a given portion of a month calendar control. You can use this macro or send the [**MCM\_GETCOLOR**](mcm-getcolor.md) message explicitly. <br/>                                                                                                                                     |
| [**MonthCal\_GetCurrentView**](monthcal-getcurrentview.md)           | Gets the view for a month calendar control. You can use this macro or send the [**MCM\_GETCURRENTVIEW**](mcm-getcurrentview.md) message explicitly.<br/>                                                                                                                                                   |
| [**MonthCal\_GetCurSel**](monthcal-getcursel.md)                     | Retrieves the currently selected date. You can use this macro or send the [**MCM\_GETCURSEL**](mcm-getcursel.md) message explicitly. <br/>                                                                                                                                                                 |
| [**MonthCal\_GetFirstDayOfWeek**](monthcal-getfirstdayofweek.md)     | Retrieves the first day of the week for a month calendar control. You can use this macro or send the [**MCM\_GETFIRSTDAYOFWEEK**](mcm-getfirstdayofweek.md) message explicitly. <br/>                                                                                                                      |
| [**MonthCal\_GetMaxSelCount**](monthcal-getmaxselcount.md)           | Retrieves the maximum date range that can be selected in a month calendar control. You can use this macro or send the [**MCM\_GETMAXSELCOUNT**](mcm-getmaxselcount.md) message explicitly. <br/>                                                                                                           |
| [**MonthCal\_GetMaxTodayWidth**](monthcal-getmaxtodaywidth.md)       | Retrieves the maximum width of the "today" string in a month calendar control. This includes the label text and the date text. You can use this macro or send the [**MCM\_GETMAXTODAYWIDTH**](mcm-getmaxtodaywidth.md) message explicitly. <br/>                                                           |
| [**MonthCal\_GetMinReqRect**](monthcal-getminreqrect.md)             | Retrieves the minimum size required to display a full month in a month calendar control. Size information is presented in the form of a [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) structure. You can use this macro or send the [**MCM\_GETMINREQRECT**](mcm-getminreqrect.md) message explicitly. <br/>                        |
| [**MonthCal\_GetMonthDelta**](monthcal-getmonthdelta.md)             | Retrieves the scroll rate for a month calendar control. The scroll rate is the number of months that the control moves its display when the user clicks a scroll button. You can use this macro or send the [**MCM\_GETMONTHDELTA**](mcm-getmonthdelta.md) message explicitly. <br/>                       |
| [**MonthCal\_GetMonthRange**](monthcal-getmonthrange.md)             | Retrieves date information (using [**SYSTEMTIME**](https://msdn.microsoft.com/library/windows/desktop/ms724950) structures) that represents the high and low limits of a month calendar control's display. You can use this macro or send the [**MCM\_GETMONTHRANGE**](mcm-getmonthrange.md) message explicitly. <br/>                             |
| [**MonthCal\_GetRange**](monthcal-getrange.md)                       | Retrieves the minimum and maximum allowable dates set for a month calendar control. You can use this macro or send the [**MCM\_GETRANGE**](mcm-getrange.md) message explicitly. <br/>                                                                                                                      |
| [**MonthCal\_GetSelRange**](monthcal-getselrange.md)                 | Retrieves date information that represents the upper and lower limits of the date range currently selected by the user. You can use this macro or send the [**MCM\_GETSELRANGE**](mcm-getselrange.md) message explicitly. <br/>                                                                            |
| [**MonthCal\_GetToday**](monthcal-gettoday.md)                       | Retrieves the date information for the date specified as "today" for a month calendar control. You can use this macro or send the [**MCM\_GETTODAY**](mcm-gettoday.md) message explicitly. <br/>                                                                                                           |
| [**MonthCal\_GetUnicodeFormat**](monthcal-getunicodeformat.md)       | Retrieves the Unicode character format flag for the control. You can use this macro or send the [**MCM\_GETUNICODEFORMAT**](mcm-getunicodeformat.md) message explicitly. <br/>                                                                                                                             |
| [**MonthCal\_HitTest**](monthcal-hittest.md)                         | Determines which portion of a month calendar control is at a given point on the screen. You can use this macro or send the [**MCM\_HITTEST**](mcm-hittest.md) message explicitly. <br/>                                                                                                                    |
| [**MonthCal\_SetCalendarBorder**](monthcal-setcalendarborder.md)     | Sets the border size, in pixels, of a month calendar control. You can use this macro or send the [**MCM\_SETCALENDARBORDER**](mcm-setcalendarborder.md) message explicitly.<br/>                                                                                                                           |
| [**MonthCal\_SetCALID**](monthcal-setcalid.md)                       | Sets the calendar ID for the given calendar control. You can use this macro or send the [**MCM\_SETCALID**](mcm-setcalid.md) message explicitly.<br/>                                                                                                                                                      |
| [**MonthCal\_SetColor**](monthcal-setcolor.md)                       | Sets the color for a given portion of a month calendar control. You can use this macro or send the [**MCM\_SETCOLOR**](mcm-setcolor.md) message explicitly. <br/>                                                                                                                                          |
| [**MonthCal\_SetCurrentView**](monthcal-setcurrentview.md)           | Sets the view for a month calendar control. You can use this macro or send the [**MCM\_SETCURRENTVIEW**](mcm-setcurrentview.md) message explicitly.<br/>                                                                                                                                                   |
| [**MonthCal\_SetCurSel**](monthcal-setcursel.md)                     | Sets the currently selected date for a month calendar control. If the specified date is not in view, the control updates the display to bring it into view. You can use this macro or send the [**MCM\_SETCURSEL**](mcm-setcursel.md) message explicitly. <br/>                                            |
| [**MonthCal\_SetDayState**](monthcal-setdaystate.md)                 | Sets the day states for all months that are currently visible within a month calendar control. You can use this macro or send the [**MCM\_SETDAYSTATE**](mcm-setdaystate.md) message explicitly. <br/>                                                                                                     |
| [**MonthCal\_SetFirstDayOfWeek**](monthcal-setfirstdayofweek.md)     | Sets the first day of the week for a month calendar control. You can use this macro or send the [**MCM\_SETFIRSTDAYOFWEEK**](mcm-setfirstdayofweek.md) message explicitly. <br/>                                                                                                                           |
| [**MonthCal\_SetMaxSelCount**](monthcal-setmaxselcount.md)           | Sets the maximum number of days that can be selected in a month calendar control. You can use this macro or send the [**MCM\_SETMAXSELCOUNT**](mcm-setmaxselcount.md) message explicitly. <br/>                                                                                                            |
| [**MonthCal\_SetMonthDelta**](monthcal-setmonthdelta.md)             | Sets the scroll rate for a month calendar control. The scroll rate is the number of months that the control moves its display when the user clicks a scroll button. You can use this macro or send the [**MCM\_SETMONTHDELTA**](mcm-setmonthdelta.md) message explicitly. <br/>                            |
| [**MonthCal\_SetRange**](monthcal-setrange.md)                       | Sets the minimum and maximum allowable dates for a month calendar control. You can use this macro or send the [**MCM\_SETRANGE**](mcm-setrange.md) message explicitly. <br/>                                                                                                                               |
| [**MonthCal\_SetSelRange**](monthcal-setselrange.md)                 | Sets the selection for a month calendar control to a given date range. You can use this macro or send the [**MCM\_SETSELRANGE**](mcm-setselrange.md) message explicitly. <br/>                                                                                                                             |
| [**MonthCal\_SetToday**](monthcal-settoday.md)                       | Sets the "today" selection for a month calendar control. You can use this macro or send the [**MCM\_SETTODAY**](mcm-settoday.md) message explicitly. <br/>                                                                                                                                                 |
| [**MonthCal\_SetUnicodeFormat**](monthcal-setunicodeformat.md)       | Sets the Unicode character format flag for the control. This message allows you to change the character set used by the control at run time rather than having to re-create the control. You can use this macro or send the [**MCM\_SETUNICODEFORMAT**](mcm-setunicodeformat.md) message explicitly. <br/> |
| [**MonthCal\_SizeRectToMin**](monthcal-sizerecttomin.md)             | Calculates how many calendars will fit in the given rectangle, and then returns the minimum size that a rectangle needs to be to fit that number of calendars. You can use this macro or send the [**MCM\_SIZERECTTOMIN**](mcm-sizerecttomin.md) message explicitly.<br/>                                  |



 

### Messages



| Topic                                                       | Contents                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MCM\_GETCALENDARBORDER**](mcm-getcalendarborder.md)     | Gets the size of the border, in pixels. You can send this message explicitly or by using the [**MonthCal\_GetCurrentView**](monthcal-getcurrentview.md) macro.<br/>                                                                                                                                                  |
| [**MCM\_GETCALENDARCOUNT**](mcm-getcalendarcount.md)       | Gets the number of calendars currently displayed in the calendar control. You can send this message explicitly or by using the [**MonthCal\_GetCalendarCount**](monthcal-getcalendarcount.md) macro.<br/>                                                                                                            |
| [**MCM\_GETCALENDARGRIDINFO**](mcm-getcalendargridinfo.md) | Gets information about a calendar grid.<br/>                                                                                                                                                                                                                                                                          |
| [**MCM\_GETCALID**](mcm-getcalid.md)                       | Gets the calendar ID for the given calendar control. You can send this message explicitly or by using the [**MonthCal\_GetCALID**](monthcal-getcalid.md) macro.<br/>                                                                                                                                                 |
| [**MCM\_GETCOLOR**](mcm-getcolor.md)                       | Retrieves the color for a given portion of a month calendar control. You can send this message explicitly or by using the [**MonthCal\_GetColor**](monthcal-getcolor.md) macro. <br/>                                                                                                                                |
| [**MCM\_GETCURRENTVIEW**](mcm-getcurrentview.md)           | Gets the current view of the calendar. You can send this message explicitly or by using the [**MonthCal\_GetCurrentView**](monthcal-getcurrentview.md) macro.<br/>                                                                                                                                                   |
| [**MCM\_GETCURSEL**](mcm-getcursel.md)                     | Retrieves the currently selected date. You can send this message explicitly or by using the [**MonthCal\_GetCurSel**](monthcal-getcursel.md) macro. <br/>                                                                                                                                                            |
| [**MCM\_GETFIRSTDAYOFWEEK**](mcm-getfirstdayofweek.md)     | Retrieves the first day of the week for a month calendar control. You can send this message explicitly or by using the [**MonthCal\_GetFirstDayOfWeek**](monthcal-getfirstdayofweek.md) macro. <br/>                                                                                                                 |
| [**MCM\_GETMAXSELCOUNT**](mcm-getmaxselcount.md)           | Retrieves the maximum date range that can be selected in a month calendar control. You can send this message explicitly or by using the [**MonthCal\_GetMaxSelCount**](monthcal-getmaxselcount.md) macro. <br/>                                                                                                      |
| [**MCM\_GETMAXTODAYWIDTH**](mcm-getmaxtodaywidth.md)       | Retrieves the maximum width of the "today" string in a month calendar control. This includes the label text and the date text. You can send this message explicitly or by using the [**MonthCal\_GetMaxTodayWidth**](monthcal-getmaxtodaywidth.md) macro. <br/>                                                      |
| [**MCM\_GETMINREQRECT**](mcm-getminreqrect.md)             | Retrieves the minimum size required to display a full month in a month calendar control. You can send this message explicitly or by using the [**MonthCal\_GetMinReqRect**](monthcal-getminreqrect.md) macro. <br/>                                                                                                  |
| [**MCM\_GETMONTHDELTA**](mcm-getmonthdelta.md)             | Retrieves the scroll rate for a month calendar control. The scroll rate is the number of months that the control moves its display when the user clicks a scroll button. You can send this message explicitly or by using the [**MonthCal\_GetMonthDelta**](monthcal-getmonthdelta.md) macro. <br/>                  |
| [**MCM\_GETMONTHRANGE**](mcm-getmonthrange.md)             | Retrieves date information (using [**SYSTEMTIME**](https://msdn.microsoft.com/library/windows/desktop/ms724950) structures) that represents the high and low limits of a month calendar control's display. You can send this message explicitly or by using the [**MonthCal\_GetMonthRange**](monthcal-getmonthrange.md) macro. <br/>                        |
| [**MCM\_GETRANGE**](mcm-getrange.md)                       | Retrieves the minimum and maximum allowable dates set for a month calendar control. You can send this message explicitly or by using the [**MonthCal\_GetRange**](monthcal-getrange.md) macro. <br/>                                                                                                                 |
| [**MCM\_GETSELRANGE**](mcm-getselrange.md)                 | Retrieves date information that represents the upper and lower limits of the date range currently selected by the user. You can send this message explicitly or by using the [**MonthCal\_GetSelRange**](monthcal-getselrange.md) macro. <br/>                                                                       |
| [**MCM\_GETTODAY**](mcm-gettoday.md)                       | Retrieves the date information for the date specified as "today" for a month calendar control. You can send this message explicitly or by using the [**MonthCal\_GetToday**](monthcal-gettoday.md) macro. <br/>                                                                                                      |
| [**MCM\_GETUNICODEFORMAT**](mcm-getunicodeformat.md)       | Retrieves the Unicode character format flag for the control. You can send this message explicitly or use the [**MonthCal\_GetUnicodeFormat**](monthcal-getunicodeformat.md) macro. <br/>                                                                                                                             |
| [**MCM\_HITTEST**](mcm-hittest.md)                         | Determines which portion of a month calendar control is at a given point on the screen. You can send this message explicitly or by using the [**MonthCal\_HitTest**](monthcal-hittest.md) macro. <br/>                                                                                                               |
| [**MCM\_SETCALENDARBORDER**](mcm-setcalendarborder.md)     | Sets the size of the border, in pixels. You can send this message explicitly or by using the [**MonthCal\_SetCurrentView**](monthcal-setcurrentview.md) macro.<br/>                                                                                                                                                  |
| [**MCM\_SETCALID**](mcm-setcalid.md)                       | Sets the calendar ID for the given calendar control. You can send this message explicitly or by using the [**MonthCal\_SetCALID**](monthcal-setcalid.md) macro.<br/>                                                                                                                                                 |
| [**MCM\_SETCOLOR**](mcm-setcolor.md)                       | Sets the color for a given portion of a month calendar control. You can send this message explicitly or by using the [**MonthCal\_SetColor**](monthcal-setcolor.md) macro. <br/>                                                                                                                                     |
| [**MCM\_SETCURRENTVIEW**](mcm-setcurrentview.md)           | Sets the current view of the calendar. You can send this message explicitly or by using the [**MonthCal\_SetCurrentView**](monthcal-setcurrentview.md) macro.<br/>                                                                                                                                                   |
| [**MCM\_SETCURSEL**](mcm-setcursel.md)                     | Sets the currently selected date for a month calendar control. If the specified date is not in view, the control updates the display to bring it into view. You can send this message explicitly or by using the [**MonthCal\_SetCurSel**](monthcal-setcursel.md) macro. <br/>                                       |
| [**MCM\_SETDAYSTATE**](mcm-setdaystate.md)                 | Sets the day states for all months that are currently visible within a month calendar control. You can send this message explicitly or by using the [**MonthCal\_SetDayState**](monthcal-setdaystate.md) macro. <br/>                                                                                                |
| [**MCM\_SETFIRSTDAYOFWEEK**](mcm-setfirstdayofweek.md)     | Sets the first day of the week for a month calendar control. You can send this message explicitly or by using the [**MonthCal\_SetFirstDayOfWeek**](monthcal-setfirstdayofweek.md) macro. <br/>                                                                                                                      |
| [**MCM\_SETMAXSELCOUNT**](mcm-setmaxselcount.md)           | Sets the maximum number of days that can be selected in a month calendar control. You can send this message explicitly or by using the [**MonthCal\_SetMaxSelCount**](monthcal-setmaxselcount.md) macro. <br/>                                                                                                       |
| [**MCM\_SETMONTHDELTA**](mcm-setmonthdelta.md)             | Sets the scroll rate for a month calendar control. The scroll rate is the number of months that the control moves its display when the user clicks a scroll button. You can send this message explicitly or by using the [**MonthCal\_SetMonthDelta**](monthcal-setmonthdelta.md) macro. <br/>                       |
| [**MCM\_SETRANGE**](mcm-setrange.md)                       | Sets the minimum and maximum allowable dates for a month calendar control. You can send this message explicitly or by using the [**MonthCal\_SetRange**](monthcal-setrange.md) macro. <br/>                                                                                                                          |
| [**MCM\_SETSELRANGE**](mcm-setselrange.md)                 | Sets the selection for a month calendar control to a given date range. You can send this message explicitly or by using the [**MonthCal\_SetSelRange**](monthcal-setselrange.md) macro. <br/>                                                                                                                        |
| [**MCM\_SETTODAY**](mcm-settoday.md)                       | Sets the "today" selection for a month calendar control. You can send this message explicitly or by using the [**MonthCal\_SetToday**](monthcal-settoday.md) macro. <br/>                                                                                                                                            |
| [**MCM\_SETUNICODEFORMAT**](mcm-setunicodeformat.md)       | Sets the Unicode character format flag for the control. This message allows you to change the character set used by the control at run time rather than having to re-create the control. You can send this message explicitly or use the [**MonthCal\_SetUnicodeFormat**](monthcal-setunicodeformat.md) macro. <br/> |
| [**MCM\_SIZERECTTOMIN**](mcm-sizerecttomin.md)             | Calculates how many calendars will fit in the given rectangle, and then returns the minimum size that a rectangle needs to be to fit that number of calendars. You can send this message explicitly or by using the [**MonthCal\_SizeRectToMin**](monthcal-sizerecttomin.md) macro.<br/>                             |



 

### Notifications



| Topic                                                              | Contents                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MCN\_GETDAYSTATE](mcn-getdaystate.md)                            | Sent by a month calendar control to request information about how individual days should be displayed. This notification code is sent only by month calendar controls that use the [**MCS\_DAYSTATE**](month-calendar-control-styles.md#mcs-daystate) style, and it is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/> |
| [MCN\_SELCHANGE](mcn-selchange.md)                                | Sent by a month calendar control when the currently selected date or range of dates changes. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                                                  |
| [MCN\_SELECT](mcn-select.md)                                      | Sent by a month calendar control when the user makes an explicit date selection within a month calendar control. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                                   |
| [MCN\_VIEWCHANGE](mcn-viewchange.md)                              | Sent by a month calendar control when the current view changes. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.<br/>                                                                                                                                                                                |
| [NM\_RELEASEDCAPTURE (monthcal)](nm-releasedcapture-monthcal-.md) | Notifies a monthcal control's parent window that the control is releasing mouse capture. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                                                           |



 

### Structures



| Topic                                  | Contents                                                                                                                                                                                                                                                           |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MCGRIDINFO**](mcgridinfo.md)       | Contains information about part of a calendar control.<br/>                                                                                                                                                                                                  |
| [**MCHITTESTINFO**](mchittestinfo.md) | Carries information specific to hit-testing points for a month calendar control. This structure is used with the [**MCM\_HITTEST**](mcm-hittest.md) message and the corresponding [**MonthCal\_HitTest**](monthcal-hittest.md) macro. <br/>                |
| [**NMDAYSTATE**](nmdaystate.md)       | Carries information required to process the [MCN\_GETDAYSTATE](mcn-getdaystate.md) notification code. All members of this structure are for input, except **prgDayState**, which the receiving application must set when processing MCN\_GETDAYSTATE. <br/> |
| [**NMSELCHANGE**](nmselchange.md)     | Carries information required to process the [MCN\_SELCHANGE](mcn-selchange.md) notification code. <br/>                                                                                                                                                     |
| [**NMVIEWCHANGE**](nmviewchange.md)   | Stores information required to process the [MCN\_VIEWCHANGE](mcn-viewchange.md) notification code.<br/>                                                                                                                                                     |



 

### Constants



| Topic                                                              | Contents                                                                                  |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [Month Calendar Control Styles](month-calendar-control-styles.md) | The following style constants are used when creating month calendar controls. <br/> |



 

### Data Types



| Topic                                  | Contents                                                                                              |
|----------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**MONTHDAYSTATE**](monthdaystate.md) | The **MONTHDAYSTATE** data type is a bitfield that holds the state of each day in a month.<br/> |



 

 

 





