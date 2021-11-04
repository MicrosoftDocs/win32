---
title: Date and Time Picker Control Styles (CommCtrl.h)
description: The window styles listed here are specific to date and time picker controls.
ms.assetid: d3b95521-75ef-4cca-b801-94c6f749aa47
topic_type:
- apiref
api_name:
- DTS_APPCANPARSE
- DTS_LONGDATEFORMAT
- DTS_RIGHTALIGN
- DTS_SHOWNONE
- DTS_SHORTDATEFORMAT
- DTS_SHORTDATECENTURYFORMAT
- DTS_TIMEFORMAT
- DTS_UPDOWN
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Date and Time Picker Control Styles

The window styles listed here are specific to date and time picker controls.



| Constant                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DTS_APPCANPARSE"></span><span id="dts_appcanparse"></span><dl> <dt>**DTS\_APPCANPARSE**</dt> </dl>                                  | Allows the owner to parse user input and take necessary action. It enables users to edit within the client area of the control when they press the F2 key. The control sends [DTN\_USERSTRING](dtn-userstring.md) notification codes when users are finished.<br/>                                                                                                                                                                                                                                                                    |
| <span id="DTS_LONGDATEFORMAT"></span><span id="dts_longdateformat"></span><dl> <dt>**DTS\_LONGDATEFORMAT**</dt> </dl>                         | Displays the date in long format. The default format string for this style is defined by LOCALE\_SLONGDATEFORMAT, which produces output like "Friday, April 19, 1996". When this style is used, the dropdown button does not display an icon.<br/>                                                                                                                                                                                                                                                                                     |
| <span id="DTS_RIGHTALIGN"></span><span id="dts_rightalign"></span><dl> <dt>**DTS\_RIGHTALIGN**</dt> </dl>                                     | The drop-down month calendar will be right-aligned with the control instead of left-aligned, which is the default. <br/>                                                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="DTS_SHOWNONE"></span><span id="dts_shownone"></span><dl> <dt>**DTS\_SHOWNONE**</dt> </dl>                                           | It is possible to have no date currently selected in the control. With this style, the control displays a check box that is automatically selected whenever a date is picked or entered. If the check box is subsequently deselected, the application cannot retrieve the date from the control because, in essence, the control has no date. The state of the check box can be set with the [**DTM\_SETSYSTEMTIME**](dtm-setsystemtime.md) message or queried with the [**DTM\_GETSYSTEMTIME**](dtm-getsystemtime.md) message.<br/> |
| <span id="DTS_SHORTDATEFORMAT"></span><span id="dts_shortdateformat"></span><dl> <dt>**DTS\_SHORTDATEFORMAT**</dt> </dl>                      | Displays the date in short format. The default format string for this style is defined by LOCALE\_SSHORTDATE, which produces output like "4/19/96".<br/>                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="DTS_SHORTDATECENTURYFORMAT"></span><span id="dts_shortdatecenturyformat"></span><dl> <dt>**DTS\_SHORTDATECENTURYFORMAT**</dt> </dl> | **Version 5.80.** Similar to the **DTS\_SHORTDATEFORMAT** style, except the year is a four-digit field. The default format string for this style is based on LOCALE\_SSHORTDATE. The output looks like: "4/19/1996".<br/>                                                                                                                                                                                                                                                                                                              |
| <span id="DTS_TIMEFORMAT"></span><span id="dts_timeformat"></span><dl> <dt>**DTS\_TIMEFORMAT**</dt> </dl>                                     | Displays the time. The default format string for this style is defined by LOCALE\_STIMEFORMAT, which produces output like "5:31:42 PM".<br/>                                                                                                                                                                                                                                                                                                                                                                                           |
| <span id="DTS_UPDOWN"></span><span id="dts_updown"></span><dl> <dt>**DTS\_UPDOWN**</dt> </dl>                                                 | Places an up-down control to the right of the DTP control to modify date-time values. This style can be used in place of the drop-down month calendar, which is the default style.<br/>                                                                                                                                                                                                                                                                                                                                                |



## Remarks

The DTS\_XXXFORMAT styles that define the display format cannot be combined. If none of the format styles are suitable, use a [**DTM\_SETFORMAT**](dtm-setformat.md) message to define a custom format.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





