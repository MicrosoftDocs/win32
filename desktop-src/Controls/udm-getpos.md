---
title: UDM_GETPOS message (Commctrl.h)
description: Retrieves the current position of an up-down control with 16-bit precision.
ms.assetid: 5f395de0-11b3-44f8-9bf4-42e27ce88a0c
keywords:
- UDM_GETPOS message Windows Controls
topic_type:
- apiref
api_name:
- UDM_GETPOS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# UDM\_GETPOS message

Retrieves the current position of an up-down control with 16-bit precision.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

If successful, the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) is set to zero and the [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is set to the control's current position. If an error occurs, the **HIWORD** is set to a nonzero value.

## Remarks

When processing this message, the up-down control updates its current position based on the caption of the buddy window. The up-down control returns an error if there is no buddy window or if the caption specifies an invalid or out-of-range value. Also, an error flag is set in the HIWORD of the return if the control is created without the [**UDS\_SETBUDDYINT**](up-down-control-styles.md) style, even though it returns a valid position value in the LOWORD of the return.

If 32-bit values have been enabled for an up-down control with [**UDM\_SETRANGE32**](udm-setrange32.md), this message returns only the lower 16 bits of the position. To retrieve the full 32-bit position, use [**UDM\_GETPOS32**](udm-getpos32.md).

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

[**UDM\_GETRANGE**](udm-getrange.md)
</dt> <dt>

[**UDM\_GETRANGE32**](udm-getrange32.md)
</dt> <dt>

[**UDM\_SETPOS**](udm-setpos.md)
</dt> <dt>

[**UDM\_SETRANGE32**](udm-setrange32.md)
</dt> </dl>

 

