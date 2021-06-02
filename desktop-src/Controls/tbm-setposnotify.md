---
title: TBM_SETPOSNOTIFY message (Commctrl.h)
description: TBM_SETPOSNOTIFY message - Sets the current logical position of the slider in a trackbar.
ms.assetid: 02f8899a-55b0-46ae-8642-9e534ab4abf5
keywords:
- TBM_SETPOSNOTIFY message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETPOSNOTIFY
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETPOSNOTIFY message

Sets the current logical position of the slider in a trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

wParam is unused.

</dd> <dt>

*lParam* 
</dt> <dd>

New logical position of the slider. Valid logical positions are the integer values in the trackbar's range of minimum to maximum slider positions. If this value is outside the control's maximum and minimum range, the position is set to the maximum or minimum value.

</dd> </dl>

## Return value

No return value.

## Remarks

Calling **TBM\_SETPOSNOTIFY** will set the trackbar slider location like [**TBM\_SETPOS**](tbm-setpos.md) would, but it will also cause the trackbar to notify its parent of a move via a [**WM\_HSCROLL**](wm-hscroll.md) or [**WM\_VSCROLL**](wm-vscroll.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





