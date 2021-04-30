---
title: MCM_SETMAXSELCOUNT message (Commctrl.h)
description: Sets the maximum number of days that can be selected in a month calendar control. You can send this message explicitly or by using the MonthCal\_SetMaxSelCount macro.
ms.assetid: 190453ab-e53b-4db7-82c1-f9d50188ad39
keywords:
- MCM_SETMAXSELCOUNT message Windows Controls
topic_type:
- apiref
api_name:
- MCM_SETMAXSELCOUNT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_SETMAXSELCOUNT message

Sets the maximum number of days that can be selected in a month calendar control. You can send this message explicitly or by using the [**MonthCal\_SetMaxSelCount**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_setmaxselcount) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value of type **int** that will be set to represent the maximum number of days that can be selected.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise. This message will fail if applied to a month calendar control that does not use the [**MCS\_MULTISELECT**](month-calendar-control-styles.md) style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





