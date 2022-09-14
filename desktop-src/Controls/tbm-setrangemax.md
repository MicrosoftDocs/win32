---
title: TBM_SETRANGEMAX message (Commctrl.h)
description: Sets the maximum logical position for the slider in a trackbar.
ms.assetid: 8e9d8fd3-2ee3-4fb6-aa1f-9d6e999ef330
keywords:
- TBM_SETRANGEMAX message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETRANGEMAX
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETRANGEMAX message

Sets the maximum logical position for the slider in a trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Redraw flag. If this parameter is **TRUE**, the trackbar is redrawn after the range is set. If this parameter is **FALSE**, the message sets the range but does not redraw the trackbar.

</dd> <dt>

*lParam* 
</dt> <dd>

Maximum position for the slider.

</dd> </dl>

## Return value

No return value.

## Remarks

If the current slider position is greater than the new maximum, the **TBM\_SETRANGEMAX** message sets the slider position to the new maximum value.

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

[**TBM\_SETRANGEMIN**](tbm-setrangemin.md)
</dt> </dl>

 

 





