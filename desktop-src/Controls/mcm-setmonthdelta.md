---
title: MCM_SETMONTHDELTA message (Commctrl.h)
description: Sets the scroll rate for a month calendar control. The scroll rate is the number of months that the control moves its display when the user clicks a scroll button. You can send this message explicitly or by using the MonthCal\_SetMonthDelta macro.
ms.assetid: 2d01b95f-3be8-4548-80b5-ac01d3e49e9f
keywords:
- MCM_SETMONTHDELTA message Windows Controls
topic_type:
- apiref
api_name:
- MCM_SETMONTHDELTA
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_SETMONTHDELTA message

Sets the scroll rate for a month calendar control. The scroll rate is the number of months that the control moves its display when the user clicks a scroll button. You can send this message explicitly or by using the [**MonthCal\_SetMonthDelta**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_setmonthdelta) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value representing the number of months to be set as the control's scroll rate. If this value is zero, the month delta is reset to the default, which is the number of months displayed in the control.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns an INT value that represents the previous scroll rate. If the scroll rate was not previously set, the return value is zero.

## Remarks

The PAGE UP and PAGE DOWN keys, VK\_PRIOR and VK\_NEXT, change the selected month by one, regardless of the number of months displayed or the value set by **MCM\_SETMONTHDELTA**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





