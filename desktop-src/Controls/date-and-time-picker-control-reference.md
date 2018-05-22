---
title: Date and Time Picker
description: This section contains information about the API elements used with date and time picker controls.
ms.assetid: '2b1a4a0e-84e6-4b65-9bf7-0384f4313aff'
---

# Date and Time Picker

This section contains information about the API elements used with date and time picker controls.

### Overviews



| Topic                                                                    | Contents                                                                                                                                                     |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Date and Time Picker Controls](date-and-time-picker-controls.md) | A *date and time picker (DTP) control* provides a simple and intuitive interface through which to exchange date and time information with a user.<br/> |
| [Using Date and Time Picker Controls](using-date-and-time-picker.md)    | This section provides information and sample code for implementing date and time picker controls. <br/>                                                |



 

### Macros



| Topic                                                                     | Contents                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DateTime\_CloseMonthCal**](datetime-closemonthcal.md)                 | Closes the date and time picker (DTP) control. Use this macro or send the [**DTM\_CLOSEMONTHCAL**](dtm-closemonthcal.md) message explicitly.<br/>                                                                                                                     |
| [**DateTime\_GetDateTimePickerInfo**](datetime-getdatetimepickerinfo.md) | Gets information for a specified date and time picker (DTP) control.<br/>                                                                                                                                                                                              |
| [**DateTime\_GetIdealSize**](datetime-getidealsize.md)                   | Gets the size needed to display the control without clipping. Use this macro or send the [**DTM\_GETIDEALSIZE**](dtm-getidealsize.md) message explicitly.<br/>                                                                                                        |
| [**DateTime\_GetMonthCal**](datetime-getmonthcal.md)                     | Gets the handle to a date and time picker's (DTP) child month calendar control. You can use this macro or send the [**DTM\_GETMONTHCAL**](dtm-getmonthcal.md) message explicitly. <br/>                                                                               |
| [**DateTime\_GetMonthCalColor**](datetime-getmonthcalcolor.md)           | Gets the color for a given portion of the month calendar within a date and time picker (DTP) control. You can use this macro or send the [**DTM\_GETMCCOLOR**](dtm-getmccolor.md) message explicitly. <br/>                                                           |
| [**DateTime\_GetMonthCalFont**](datetime-getmonthcalfont.md)             | Gets the font that the date and time picker (DTP) control's child month calendar control is currently using. You can use this macro or send the [**DTM\_GETMCFONT**](dtm-getmcfont.md) message explicitly. <br/>                                                      |
| [**DateTime\_GetMonthCalStyle**](datetime-getmonthcalstyle.md)           | Gets the style of a specified DTP control. Use this macro or send the [**DTM\_GETMCSTYLE**](dtm-getmcstyle.md) message explicitly.<br/>                                                                                                                               |
| [**DateTime\_GetRange**](datetime-getrange.md)                           | Gets the current minimum and maximum allowable system times for a date and time picker (DTP) control. You can use this macro, or send the [**DTM\_GETRANGE**](dtm-getrange.md) message explicitly. <br/>                                                              |
| [**DateTime\_GetSystemtime**](datetime-getsystemtime.md)                 | Gets the currently selected time from a date and time picker (DTP) control and places it in a specified [**SYSTEMTIME**](https://msdn.microsoft.com/library/windows/desktop/ms724950) structure. You can use this macro, or send the [**DTM\_GETSYSTEMTIME**](dtm-getsystemtime.md) message explicitly. <br/> |
| [**DateTime\_SetFormat**](datetime-setformat.md)                         | Sets the display of a date and time picker (DTP) control based on a given format string. You can use this macro or send the [**DTM\_SETFORMAT**](dtm-setformat.md) message explicitly. <br/>                                                                          |
| [**DateTime\_SetMonthCalColor**](datetime-setmonthcalcolor.md)           | Sets the color for a given portion of the month calendar within a date and time picker (DTP) control. You can use this macro or send the [**DTM\_SETMCCOLOR**](dtm-setmccolor.md) message explicitly. <br/>                                                           |
| [**DateTime\_SetMonthCalFont**](datetime-setmonthcalfont.md)             | Sets the font to be used by the date and time picker (DTP) control's child month calendar control. You can use this macro or explicitly send the [**DTM\_SETMCFONT**](dtm-setmcfont.md) message. <br/>                                                                |
| [**DateTime\_SetMonthCalStyle**](datetime-setmonthcalstyle.md)           | Sets the style for a specified DTP control. Use this macro or send the [**DTM\_SETMCSTYLE**](dtm-setmcstyle.md) message explicitly.<br/>                                                                                                                              |
| [**DateTime\_SetRange**](datetime-setrange.md)                           | Sets the minimum and maximum allowable system times for a date and time picker (DTP) control. You can use this macro or send the [**DTM\_SETRANGE**](dtm-setrange.md) message explicitly. <br/>                                                                       |
| [**DateTime\_SetSystemtime**](datetime-setsystemtime.md)                 | Sets a date and time picker (DTP) control to a given date and time. You can use this macro or send the [**DTM\_SETSYSTEMTIME**](dtm-setsystemtime.md) message explicitly. <br/>                                                                                       |



 

### Messages



| Topic                                                           | Contents                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DTM\_CLOSEMONTHCAL**](dtm-closemonthcal.md)                 | Closes a DTP control. Send this message explicitly or by using the [**DateTime\_CloseMonthCal**](datetime-closemonthcal.md) macro.<br/>                                                                                                                                        |
| [**DTM\_GETDATETIMEPICKERINFO**](dtm-getdatetimepickerinfo.md) | Gets information on a date and time picker (DTP) control.<br/>                                                                                                                                                                                                                  |
| [**DTM\_GETIDEALSIZE**](dtm-getidealsize.md)                   | Gets the size needed to display the control without clipping. Send this message explicitly or by using the [**DateTime\_GetIdealSize**](datetime-getidealsize.md) macro.<br/>                                                                                                  |
| [**DTM\_GETMCCOLOR**](dtm-getmccolor.md)                       | Gets the color for a given portion of the month calendar within a date and time picker (DTP) control. You can send this message explicitly or use the [**DateTime\_GetMonthCalColor**](datetime-getmonthcalcolor.md) macro. <br/>                                              |
| [**DTM\_GETMCFONT**](dtm-getmcfont.md)                         | Gets the font that the date and time picker (DTP) control's child month calendar control is currently using. You can send this message explicitly or use the [**DateTime\_GetMonthCalFont**](datetime-getmonthcalfont.md) macro. <br/>                                         |
| [**DTM\_GETMCSTYLE**](dtm-getmcstyle.md)                       | Gets the style of a DTP control. Send this message explicitly or by using the [**DateTime\_GetMonthCalStyle**](datetime-getmonthcalstyle.md) macro.<br/>                                                                                                                       |
| [**DTM\_GETMONTHCAL**](dtm-getmonthcal.md)                     | Gets the handle to a date and time picker's (DTP) child month calendar control. You can send this message explicitly or use the [**DateTime\_GetMonthCal**](datetime-getmonthcal.md) macro. <br/>                                                                              |
| [**DTM\_GETRANGE**](dtm-getrange.md)                           | Gets the current minimum and maximum allowable system times for a date and time picker (DTP) control. You can send this message explicitly or use the [**DateTime\_GetRange**](datetime-getrange.md) macro. <br/>                                                              |
| [**DTM\_GETSYSTEMTIME**](dtm-getsystemtime.md)                 | Gets the currently selected time from a date and time picker (DTP) control and places it in a specified [**SYSTEMTIME**](https://msdn.microsoft.com/library/windows/desktop/ms724950) structure. You can send this message explicitly or use the [**DateTime\_GetSystemtime**](datetime-getsystemtime.md) macro. <br/> |
| [**DTM\_SETFORMAT**](dtm-setformat.md)                         | Sets the display of a date and time picker (DTP) control based on a given format string. You can send this message explicitly or use the [**DateTime\_SetFormat**](datetime-setformat.md) macro. <br/>                                                                         |
| [**DTM\_SETMCCOLOR**](dtm-setmccolor.md)                       | Sets the color for a given portion of the month calendar within a date and time picker (DTP) control. You can send this message explicitly or use the [**DateTime\_SetMonthCalColor**](datetime-setmonthcalcolor.md) macro. <br/>                                              |
| [**DTM\_SETMCFONT**](dtm-setmcfont.md)                         | Sets the font to be used by the date and time picker (DTP) control's child month calendar control. You can send this message explicitly or use the [**DateTime\_SetMonthCalFont**](datetime-setmonthcalfont.md) macro.<br/>                                                    |
| [**DTM\_SETMCSTYLE**](dtm-setmcstyle.md)                       | Sets the style of a DTP control. Send this message explicitly or by using the [**DateTime\_SetMonthCalStyle**](datetime-setmonthcalstyle.md) macro.<br/>                                                                                                                       |
| [**DTM\_SETRANGE**](dtm-setrange.md)                           | Sets the minimum and maximum allowable system times for a date and time picker (DTP) control. You can send this message explicitly or use the [**DateTime\_SetRange**](datetime-setrange.md) macro. <br/>                                                                      |
| [**DTM\_SETSYSTEMTIME**](dtm-setsystemtime.md)                 | Sets the time in a date and time picker (DTP) control. You can send this message explicitly or use the [**DateTime\_SetSystemtime**](datetime-setsystemtime.md) macro. <br/>                                                                                                   |



 

### Notifications



| Topic                                                   | Contents                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DTN\_CLOSEUP](dtn-closeup.md)                         | Sent by a date and time picker (DTP) control when the user closes the drop-down month calendar. The month calendar is closed when the user chooses a date from the month calendar or clicks the drop-down arrow while the calendar is open. <br/>                                                                                                      |
| [DTN\_DATETIMECHANGE](dtn-datetimechange.md)           | Sent by a date and time picker (DTP) control whenever a change occurs. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                                                                                  |
| [DTN\_DROPDOWN](dtn-dropdown.md)                       | Sent by a date and time picker (DTP) control when the user activates the drop-down month calendar. <br/>                                                                                                                                                                                                                                               |
| [DTN\_FORMAT](dtn-format.md)                           | Sent by a date and time picker (DTP) control to request text to be displayed in a callback field. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                                                       |
| [DTN\_FORMATQUERY](dtn-formatquery.md)                 | Sent by a date and time picker (DTP) control to retrieve the maximum allowable size of the string that will be displayed in a callback field. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                           |
| [DTN\_USERSTRING](dtn-userstring.md)                   | Sent by a date and time picker (DTP) control when a user finishes editing a string in the control. This notification code is only sent by DTP controls that are set to the [**DTS\_APPCANPARSE**](date-and-time-picker-control-styles.md#dts-appcanparse) style. This message is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/> |
| [DTN\_WMKEYDOWN](dtn-wmkeydown.md)                     | Sent by a date and time picker (DTP) control when the user types in a callback field. This message is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                                                                             |
| [NM\_KILLFOCUS (date time)](nm-killfocus-date-time.md) | Notifies a date and time picker control's parent window that the control has lost the input focus. [**NM\_KILLFOCUS (date time)**](nm-killfocus-date-time.md) is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                 |
| [NM\_SETFOCUS (date time)](nm-setfocus-date-time-.md)  | Notifies a date and time picker control's parent window that the control has received the input focus. [NM\_SETFOCUS (date time)](nm-setfocus-date-time-.md) is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. <br/>                                                                                                                  |



 

### Structures



| Topic                                                  | Contents                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DATETIMEPICKERINFO**](datetimepickerinfo.md)       | Contains information about a DTP control. <br/>                                                                                                                                                                                                                                                                                                                                              |
| [**NMDATETIMECHANGE**](nmdatetimechange.md)           | Contains information about a change that has taken place in a date and time picker (DTP) control. This structure is used with the [DTN\_DATETIMECHANGE](dtn-datetimechange.md) notification code. <br/>                                                                                                                                                                                     |
| [**NMDATETIMEFORMAT**](nmdatetimeformat.md)           | Contains information about a portion of the format string that defines a callback field within a date and time picker (DTP) control. It carries the substring that defines the callback field and contains a buffer to receive the string that will be displayed in the callback field. This structure is used with the [DTN\_FORMAT](dtn-format.md) notification code. <br/>               |
| [**NMDATETIMEFORMATQUERY**](nmdatetimeformatquery.md) | Contains information about a date and time picker (DTP) control callback field. It contains a substring (taken from the control's format string) that defines a callback field. The structure receives the maximum allowable size of the text that will be displayed in the callback field. This structure is used with the [DTN\_FORMATQUERY](dtn-formatquery.md) notification code. <br/> |
| [**NMDATETIMESTRING**](nmdatetimestring.md)           | Contains information specific to an edit operation that has taken place in a date and time picker (DTP) control. This message is used with the [DTN\_USERSTRING](dtn-userstring.md) notification code. <br/>                                                                                                                                                                                |
| [**NMDATETIMEWMKEYDOWN**](nmdatetimewmkeydown.md)     | Carries information used to describe and handle a [DTN\_WMKEYDOWN](dtn-wmkeydown.md) notification code. <br/>                                                                                                                                                                                                                                                                               |



 

### Constants



| Topic                                                                          | Contents                                                                                |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [Date and Time Picker Control Styles](date-and-time-picker-control-styles.md) | The window styles listed here are specific to date and time picker controls.<br/> |



 

 

 





