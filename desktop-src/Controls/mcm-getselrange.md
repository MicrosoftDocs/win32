---
title: MCM_GETSELRANGE message (Commctrl.h)
description: Retrieves date information that represents the upper and lower limits of the date range currently selected by the user. You can send this message explicitly or by using the MonthCal\_GetSelRange macro.
ms.assetid: a0d0a0d5-a519-4495-a87a-2438c4590e4c
keywords:
- MCM_GETSELRANGE message Windows Controls
topic_type:
- apiref
api_name:
- MCM_GETSELRANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_GETSELRANGE message

Retrieves date information that represents the upper and lower limits of the date range currently selected by the user. You can send this message explicitly or by using the [**MonthCal\_GetSelRange**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_getselrange) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a two-element array of [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structures that will receive the lower and upper limits of the user's selection. The lower and upper limits are placed in *lprgSysTimeArray*\[0\] and *lprgSysTimeArray*\[1\], respectively. This parameter must be a valid address and cannot be **NULL**.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise. **MCM\_GETSELRANGE** will fail if applied to a month calendar control that does not use the [**MCS\_MULTISELECT**](month-calendar-control-styles.md) style.

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

 

