---
title: DTM_SETMCSTYLE message (Commctrl.h)
description: Sets the style of a date and time picker (DTP) control. Send this message explicitly or by using the DateTime\_SetMonthCalStyle macro.
ms.assetid: 6b480a1e-c76e-4026-ab2a-5ec53df6fa28
keywords:
- DTM_SETMCSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- DTM_SETMCSTYLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTM\_SETMCSTYLE message

Sets the style of a date and time picker (DTP) control. Send this message explicitly or by using the [**DateTime\_SetMonthCalStyle**](/windows/desktop/api/Commctrl/nf-commctrl-datetime_setmonthcalstyle) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>A style value. For more information see <a href="month-calendar-control-styles.md">Month Calendar Control Styles</a>.</dd> </dl>

## Return value

Returns the value of the previous style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





