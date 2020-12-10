---
title: DTM_SETFORMAT message (Commctrl.h)
description: Sets the display of a date and time picker (DTP) control based on a given format string. You can send this message explicitly or use the DateTime\_SetFormat macro.
ms.assetid: a89fa3ad-9894-4c52-ab56-fb62208e39b3
keywords:
- DTM_SETFORMAT message Windows Controls
topic_type:
- apiref
api_name:
- DTM_SETFORMAT
- DTM_SETFORMATA
- DTM_SETFORMATW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTM\_SETFORMAT message

Sets the display of a date and time picker (DTP) control based on a given format string. You can send this message explicitly or use the [**DateTime\_SetFormat**](/windows/desktop/api/Commctrl/nf-commctrl-datetime_setformat) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a zero-terminated [format string](date-and-time-picker-controls.md) that defines the desired display. Setting this parameter to **NULL** will reset the control to the default format string for the current style.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

It is acceptable to include extra characters within the format string to produce a more rich display. However, any nonformat characters must be enclosed within single quotes. For example, the format string "'Today is: 'hh':'m':'s ddddMMMdd', 'yyy" would produce output like "Today is: 04:22:31 Tuesday Mar 23, 1996".

> [!Note]  
> A DTP control tracks locale changes when it is using the default format string. If you set a custom format string, it will not be updated in response to locale changes.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **DTM\_SETFORMATW** (Unicode) and **DTM\_SETFORMATA** (ANSI)<br/>               |



 

 





