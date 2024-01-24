---
title: TBM_SETRANGEMIN message (Commctrl.h)
description: Sets the minimum logical position for the slider in a trackbar.
ms.assetid: 85071be2-4df3-4b54-9122-b6dc767f6cb9
keywords:
- TBM_SETRANGEMIN message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETRANGEMIN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETRANGEMIN message

Sets the minimum logical position for the slider in a trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Redraw flag. If this parameter is **TRUE**, the message redraws the trackbar after the range is set. If this parameter is **FALSE**, the message sets the range but does not redraw the trackbar.

</dd> <dt>

*lParam* 
</dt> <dd>

Minimum position for the slider.

</dd> </dl>

## Return value

No return value.

## Remarks

If the current slider position is less than the new minimum, the **TBM\_SETRANGEMIN** message sets the slider position to the new minimum value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TBM\_SETRANGE**](tbm-setrange.md)
</dt> <dt>

[**TBM\_SETRANGEMAX**](tbm-setrangemax.md)
</dt> </dl>

 

 





