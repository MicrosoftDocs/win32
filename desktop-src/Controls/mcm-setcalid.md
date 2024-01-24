---
title: MCM_SETCALID message (Commctrl.h)
description: Sets the calendar ID for the given calendar control. You can send this message explicitly or by using the MonthCal\_SetCALID macro.
ms.assetid: 4b9d06f5-0784-4a17-b401-982206d4be67
keywords:
- MCM_SETCALID message Windows Controls
topic_type:
- apiref
api_name:
- MCM_SETCALID
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_SETCALID message

Sets the calendar ID for the given calendar control. You can send this message explicitly or by using the [**MonthCal\_SetCALID**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_setcalid) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The calendar ID. One of the [Calendar Identifiers](/windows/desktop/Intl/calendar-identifiers) constants.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

Unused.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

