---
title: Month Calendar Control Styles (CommCtrl.h)
description: The following style constants are used when creating month calendar controls.
ms.assetid: 8d9b2239-fd13-4579-81a2-0385fd318e83
topic_type:
- apiref
api_name:
- MCS_DAYSTATE
- MCS_MULTISELECT
- MCS_WEEKNUMBERS
- MCS_NOTODAYCIRCLE
- MCS_NOTODAY
- MCS_NOTRAILINGDATES
- MCS_SHORTDAYSOFWEEK
- MCS_NOSELCHANGEONNAV
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Month Calendar Control Styles

The following style constants are used when creating month calendar controls.



| Constant                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                          |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MCS_DAYSTATE"></span><span id="mcs_daystate"></span><dl> <dt>**MCS\_DAYSTATE**</dt> </dl>                         | [Version 4.70](common-control-versions.md). The month calendar sends [MCN\_GETDAYSTATE](mcn-getdaystate.md) notifications to request information about which days should be displayed in bold.<br/>                                                                                                          |
| <span id="MCS_MULTISELECT"></span><span id="mcs_multiselect"></span><dl> <dt>**MCS\_MULTISELECT**</dt> </dl>                | [Version 4.70](common-control-versions.md). The month calendar enables the user to select a range of dates within the control. By default, the maximum range is one week. You can change the maximum range that can be selected by using the [**MCM\_SETMAXSELCOUNT**](mcm-setmaxselcount.md) message. <br/> |
| <span id="MCS_WEEKNUMBERS"></span><span id="mcs_weeknumbers"></span><dl> <dt>**MCS\_WEEKNUMBERS**</dt> </dl>                | [Version 4.70](common-control-versions.md). The month calendar control displays week numbers (1-52) to the left of each row of days. Week 1 is defined as the first week that contains at least four days. <br/>                                                                                              |
| <span id="MCS_NOTODAYCIRCLE"></span><span id="mcs_notodaycircle"></span><dl> <dt>**MCS\_NOTODAYCIRCLE**</dt> </dl>          | [Version 4.70](common-control-versions.md). The month calendar control does not circle the "today" date. <br/>                                                                                                                                                                                                |
| <span id="MCS_NOTODAY"></span><span id="mcs_notoday"></span><dl> <dt>**MCS\_NOTODAY**</dt> </dl>                            | [Version 4.70](common-control-versions.md).The month calendar control does not display the "today" date at the bottom of the control. <br/>                                                                                                                                                                   |
| <span id="MCS_NOTRAILINGDATES"></span><span id="mcs_notrailingdates"></span><dl> <dt>**MCS\_NOTRAILINGDATES**</dt> </dl>    | **Windows Vista.** Dates from the previous and next months are not displayed in the current month's calendar.<br/>                                                                                                                                                                                              |
| <span id="MCS_SHORTDAYSOFWEEK"></span><span id="mcs_shortdaysofweek"></span><dl> <dt>**MCS\_SHORTDAYSOFWEEK**</dt> </dl>    | **Windows Vista.** Short day names are displayed in the header.<br/>                                                                                                                                                                                                                                            |
| <span id="MCS_NOSELCHANGEONNAV"></span><span id="mcs_noselchangeonnav"></span><dl> <dt>**MCS\_NOSELCHANGEONNAV**</dt> </dl> | **Windows Vista.** The selection is not changed when the user navigates next or previous in the calendar. This allows the user to select a range larger than is visible.<br/>                                                                                                                                  |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





