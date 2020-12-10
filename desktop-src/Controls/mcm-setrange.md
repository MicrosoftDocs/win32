---
title: MCM_SETRANGE message (Commctrl.h)
description: Sets the minimum and maximum allowable dates for a month calendar control. You can send this message explicitly or by using the MonthCal\_SetRange macro.
ms.assetid: dab9ebb0-f397-4e71-b060-ef8d7d89a6bc
keywords:
- MCM_SETRANGE message Windows Controls
topic_type:
- apiref
api_name:
- MCM_SETRANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_SETRANGE message

Sets the minimum and maximum allowable dates for a month calendar control. You can send this message explicitly or by using the [**MonthCal\_SetRange**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_setrange) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Flag values that specify which date limits are being set. This value must be one or both of the following:



| Value                                                                                                                                          | Meaning                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GDTR_MAX"></span><span id="gdtr_max"></span><dl> <dt>**GDTR\_MAX**</dt> </dl> | The maximum allowable date is being set. The [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure at *lpSysTimeArray*\[1\] must contain date information. <br/> |
| <span id="GDTR_MIN"></span><span id="gdtr_min"></span><dl> <dt>**GDTR\_MIN**</dt> </dl> | The minimum allowable date is being set. The [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure at *lpSysTimeArray*\[0\] must contain date information. <br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a two-element array of [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structures that contain the date limits. The maximum limit must be in *lpSysTimeArray*\[1\] if GDTR\_MAX is specified, and *lpSysTimeArray*\[0\] must contain the minimum limit if GDTR\_MIN is specified.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[Times in the Month Calendar Control](month-calendar-controls.md)
</dt> </dl>

 

