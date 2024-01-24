---
title: PBM_GETRANGE message (Commctrl.h)
description: Retrieves information about the current high and low limits of a given progress bar control.
ms.assetid: 676b7a37-bdde-4307-9888-9a0cf40db2db
keywords:
- PBM_GETRANGE message Windows Controls
topic_type:
- apiref
api_name:
- PBM_GETRANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PBM\_GETRANGE message

Retrieves information about the current high and low limits of a given progress bar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Flag value specifying which limit value is to be used as the message's return value. This parameter can be one of the following values:



| Value                                                                                                                                    | Meaning                           |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| <span id="TRUE"></span><span id="true"></span><dl> <dt>****TRUE****</dt> </dl>    | Return the low limit.<br/>  |
| <span id="FALSE"></span><span id="false"></span><dl> <dt>****FALSE****</dt> </dl> | Return the high limit.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**PBRANGE**](/windows/desktop/api/Commctrl/ns-commctrl-pbrange) structure that is to be filled with the high and low limits of the progress bar control. If this parameter is set to **NULL**, the control will return only the limit specified by *wParam*.

</dd> </dl>

## Return value

Returns an INT that represents the limit value specified by *wParam*. If *lParam* is not **NULL**, *lParam* must point to a [**PBRANGE**](/windows/desktop/api/Commctrl/ns-commctrl-pbrange) structure that is to be filled with both limit values.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





