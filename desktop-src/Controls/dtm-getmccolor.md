---
title: DTM_GETMCCOLOR message (Commctrl.h)
description: Gets the color for a given portion of the month calendar within a date and time picker (DTP) control. You can send this message explicitly or use the DateTime\_GetMonthCalColor macro.
ms.assetid: 892e8c23-f0d0-4fd6-98ed-39592c4d316f
keywords:
- DTM_GETMCCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- DTM_GETMCCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTM\_GETMCCOLOR message

Gets the color for a given portion of the month calendar within a date and time picker (DTP) control. You can send this message explicitly or use the [**DateTime\_GetMonthCalColor**](/windows/desktop/api/Commctrl/nf-commctrl-datetime_getmonthcalcolor) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A value of type **int** specifying which month calendar color to retrieve. This value can be one of the following:



| Value                                                                                                                                                                     | Meaning                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MCSC_BACKGROUND"></span><span id="mcsc_background"></span><dl> <dt>**MCSC\_BACKGROUND**</dt> </dl>       | Retrieve the background color displayed between months.<br/>                                                                                                                                      |
| <span id="MCSC_MONTHBK"></span><span id="mcsc_monthbk"></span><dl> <dt>**MCSC\_MONTHBK**</dt> </dl>                | Retrieve the background color displayed within the month.<br/>                                                                                                                                    |
| <span id="MCSC_TEXT"></span><span id="mcsc_text"></span><dl> <dt>**MCSC\_TEXT**</dt> </dl>                         | Retrieve the color used to display text within a month.<br/>                                                                                                                                      |
| <span id="MCSC_TITLEBK"></span><span id="mcsc_titlebk"></span><dl> <dt>**MCSC\_TITLEBK**</dt> </dl>                | Retrieve the background color displayed in the calendar's title.<br/>                                                                                                                             |
| <span id="MCSC_TITLETEXT"></span><span id="mcsc_titletext"></span><dl> <dt>**MCSC\_TITLETEXT**</dt> </dl>          | Retrieve the color used to display text within the calendar's title.<br/>                                                                                                                         |
| <span id="MCSC_TRAILINGTEXT"></span><span id="mcsc_trailingtext"></span><dl> <dt>**MCSC\_TRAILINGTEXT**</dt> </dl> | Retrieve the color used to display header day and trailing day text. Header and trailing days are the days from the previous and following months that appear on the current month calendar.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a **COLORREF** value that represents the color setting for the specified portion of the month calendar control if successful. The message returns -1 if unsuccessful.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





