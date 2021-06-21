---
title: TBM_SETPOS message (Commctrl.h)
description: TBM_SETPOS message - Sets the current logical position of the slider in a trackbar.
ms.assetid: df6c4e5d-2847-419d-82b5-334d53bb6ba1
keywords:
- TBM_SETPOS message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETPOS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETPOS message

Sets the current logical position of the slider in a trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Redraw flag. If this parameter is **TRUE**, the message redraws the control with the slider at the position given by *lParam*. If this parameter is **FALSE**, the message does not redraw the slider at the new position. Note that the message sets the value of the slider position (as returned by the [**TBM\_GETPOS**](tbm-getpos.md) message) regardless of the *wParam* parameter.

</dd> <dt>

*lParam* 
</dt> <dd>

New logical position of the slider. Valid logical positions are the integer values in the trackbar's range of minimum to maximum slider positions. If this value is outside the control's maximum and minimum range, the position is set to the maximum or minimum value.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





