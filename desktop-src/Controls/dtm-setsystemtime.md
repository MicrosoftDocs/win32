---
title: DTM_SETSYSTEMTIME message (Commctrl.h)
description: Sets the time in a date and time picker (DTP) control. You can send this message explicitly or use the DateTime\_SetSystemtime macro.
ms.assetid: aab023ac-22ef-485b-be2f-2aa76dfcf57f
keywords:
- DTM_SETSYSTEMTIME message Windows Controls
topic_type:
- apiref
api_name:
- DTM_SETSYSTEMTIME
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTM\_SETSYSTEMTIME message

Sets the time in a date and time picker (DTP) control. You can send this message explicitly or use the [**DateTime\_SetSystemtime**](/windows/desktop/api/Commctrl/nf-commctrl-datetime_setsystemtime) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A value specifying the action that should be performed. This value must be set to one of the following:



| Value                                                                                                                                             | Meaning                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GDT_VALID"></span><span id="gdt_valid"></span><dl> <dt>**GDT\_VALID**</dt> </dl> | Set the DTP control according to the data within the structure that *lParam* points to. <br/>                                                                                                                                                                 |
| <span id="GDT_NONE"></span><span id="gdt_none"></span><dl> <dt>**GDT\_NONE**</dt> </dl>    | Set the DTP control to "no date" and clear its check box. When this flag is specified, *lParam* is ignored. This flag applies only to DTP controls that are set to the [**DTS\_SHOWNONE**](date-and-time-picker-control-styles.md) style. <br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure containing the system time used to set the DTP control.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

