---
title: MCM_GETMAXSELCOUNT message (Commctrl.h)
description: Retrieves the maximum date range that can be selected in a month calendar control. You can send this message explicitly or by using the MonthCal\_GetMaxSelCount macro.
ms.assetid: 34204231-3a3c-4eba-913d-b0c27769c338
keywords:
- MCM_GETMAXSELCOUNT message Windows Controls
topic_type:
- apiref
api_name:
- MCM_GETMAXSELCOUNT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_GETMAXSELCOUNT message

Retrieves the maximum date range that can be selected in a month calendar control. You can send this message explicitly or by using the [**MonthCal\_GetMaxSelCount**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_getmaxselcount) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns an INT value that represents the total number of days that can be selected for the control.

## Remarks

You can change the maximum date range that can be selected by using the [**MCM\_SETMAXSELCOUNT**](mcm-setmaxselcount.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





