---
title: TBM_SETRANGE message (Commctrl.h)
description: Sets the range of minimum and maximum logical positions for the slider in a trackbar.
ms.assetid: 9c225742-8e5e-4f47-af8c-8243b6c90c1d
keywords:
- TBM_SETRANGE message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETRANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETRANGE message

Sets the range of minimum and maximum logical positions for the slider in a trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Redraw flag. If this parameter is **TRUE**, the trackbar is redrawn after the range is set. If this parameter is **FALSE**, the message sets the range but does not redraw the trackbar.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the minimum position for the slider, and the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the maximum position.

</dd> </dl>

## Return value

No return value.

## Remarks

If the current slider position is outside the new range, the **TBM\_SETRANGE** message sets the slider position to the new maximum or minimum value.

Because this message takes two 16-bit unsigned integer values, the maximum range that this message can specify is from 0 to 65,535. To specify larger range values, use the [**TBM\_SETRANGEMIN**](tbm-setrangemin.md) and [**TBM\_SETRANGEMAX**](tbm-setrangemax.md) messages.

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

[**TBM\_SETRANGEMAX**](tbm-setrangemax.md)
</dt> <dt>

[**TBM\_SETRANGEMIN**](tbm-setrangemin.md)
</dt> </dl>

 

