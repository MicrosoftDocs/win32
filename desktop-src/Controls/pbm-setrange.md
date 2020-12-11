---
title: PBM_SETRANGE message (Commctrl.h)
description: Sets the minimum and maximum values for a progress bar and redraws the bar to reflect the new range.
ms.assetid: 251eb8c5-bedc-4e2c-90c2-e1626cb00420
keywords:
- PBM_SETRANGE message Windows Controls
topic_type:
- apiref
api_name:
- PBM_SETRANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PBM\_SETRANGE message

Sets the minimum and maximum values for a progress bar and redraws the bar to reflect the new range.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the minimum range value, and the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the maximum range value. The minimum range value must not be negative. By default, the minimum value is zero. The maximum range value must be greater than the minimum range value. By default, the maximum range value is 100.

</dd> </dl>

## Return value

Returns the previous range values if successful, or zero otherwise. The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the previous minimum value, and the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the previous maximum value.

## Remarks

If you do not set the range values, the system sets the minimum value to 0 and the maximum value to 100. Because this message expresses the range as a 16-bit unsigned integer, it can extend from 0 to 65,535. The minimum value in the range can be from 0 to 65,535. Likewise, the maximum value can be from 0 to 65,535.

To set a larger range, call [**PBM\_SETRANGE32**](pbm-setrange32.md).

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

[**PBM\_GETRANGE**](pbm-getrange.md)
</dt> <dt>

[**PBM\_SETRANGE32**](pbm-setrange32.md)
</dt> </dl>

 

