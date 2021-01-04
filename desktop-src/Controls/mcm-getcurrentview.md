---
title: MCM_GETCURRENTVIEW message (Commctrl.h)
description: Gets the current view of the calendar. You can send this message explicitly or by using the MonthCal\_GetCurrentView macro.
ms.assetid: 9c42ebf6-611e-4e50-9dcc-cf7fd63b32eb
keywords:
- MCM_GETCURRENTVIEW message Windows Controls
topic_type:
- apiref
api_name:
- MCM_GETCURRENTVIEW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCM\_GETCURRENTVIEW message

Gets the current view of the calendar. You can send this message explicitly or by using the [**MonthCal\_GetCurrentView**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_getcurrentview) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

Current view. One of the following values.



| Return code                                                                                  | Description              |
|----------------------------------------------------------------------------------------------|--------------------------|
| <dl> <dt>**MCMV\_MONTH**</dt> </dl>   | Monthly view.<br/> |
| <dl> <dt>**MCMV\_YEAR**</dt> </dl>    | Annual view.<br/>  |
| <dl> <dt>**MCMV\_DECADE**</dt> </dl>  | Decade view.<br/>  |
| <dl> <dt>**MCMV\_CENTURY**</dt> </dl> | Century view.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





