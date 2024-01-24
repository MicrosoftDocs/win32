---
title: PBM_SETPOS message (Commctrl.h)
description: Sets the current position for a progress bar and redraws the bar to reflect the new position.
ms.assetid: 9ebeaa19-0f42-4af7-85d8-aae22498fd6f
keywords:
- PBM_SETPOS message Windows Controls
topic_type:
- apiref
api_name:
- PBM_SETPOS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PBM\_SETPOS message

Sets the current position for a progress bar and redraws the bar to reflect the new position.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Signed integer that becomes the new position.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the previous position.

## Remarks

If *wParam* is outside the range of the control, the position is set to the closest boundary.

Do not send this message to a control that has the [**PBS\_MARQUEE**](progress-bar-control-styles.md) style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





