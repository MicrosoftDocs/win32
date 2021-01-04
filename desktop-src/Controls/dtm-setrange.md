---
title: DTM_SETRANGE message (Commctrl.h)
description: Sets the minimum and maximum allowable system times for a date and time picker (DTP) control. You can send this message explicitly or use the DateTime\_SetRange macro.
ms.assetid: ef0f48f2-906e-4ae0-839d-177e0fb7f14e
keywords:
- DTM_SETRANGE message Windows Controls
topic_type:
- apiref
api_name:
- DTM_SETRANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTM\_SETRANGE message

Sets the minimum and maximum allowable system times for a date and time picker (DTP) control. You can send this message explicitly or use the [**DateTime\_SetRange**](/windows/desktop/api/Commctrl/nf-commctrl-datetime_setrange) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A value specifying which range values are valid. This parameter can be a combination of the following values:



| Value                                                                                                                                          | Meaning                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GDTR_MIN"></span><span id="gdtr_min"></span><dl> <dt>**GDTR\_MIN**</dt> </dl> | The first element in the [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure array is valid and will be used to set the minimum allowable system time.<br/>  |
| <span id="GDTR_MAX"></span><span id="gdtr_max"></span><dl> <dt>**GDTR\_MAX**</dt> </dl> | The second element in the [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure array is valid and will be used to set the maximum allowable system time.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a two-element array of [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structures. The first element of the **SYSTEMTIME** array contains the minimum allowable time. The second element of the **SYSTEMTIME** array contains the maximum allowable time. It is not necessary to fill an array element that is not specified in the *wParam* parameter.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

The date and time picker displays only dates/times that fall within the specified range, preventing the user from selecting a date and time that falls outside the range. If the [**DTM\_SETSYSTEMTIME**](dtm-setsystemtime.md) message specifies a date and time that falls outside the range, it will fail.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

