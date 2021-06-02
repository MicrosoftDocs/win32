---
title: PBM_SETRANGE32 message (Commctrl.h)
description: Sets the minimum and maximum values for a progress bar to 32-bit values, and redraws the bar to reflect the new range.
ms.assetid: 7958ea14-17b4-4c0e-97ec-b09fa0d36e8b
keywords:
- PBM_SETRANGE32 message Windows Controls
topic_type:
- apiref
api_name:
- PBM_SETRANGE32
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PBM\_SETRANGE32 message

Sets the minimum and maximum values for a progress bar to 32-bit values, and redraws the bar to reflect the new range.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Minimum range value. By default, the minimum value is zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Maximum range value. This value must be greater than *wParam*. By default, the maximum value is 100.

</dd> </dl>

## Return value

Returns a **DWORD** value that holds the previous 16-bit low limit in its [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) and the previous 16-bit high limit in its [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)). If the previous ranges were 32-bit values, the return value consists of the **LOWORD**s of both 32-bit limits.

## Remarks

To retrieve the entire high and low 32-bit values, use the [**PBM\_GETRANGE**](pbm-getrange.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

