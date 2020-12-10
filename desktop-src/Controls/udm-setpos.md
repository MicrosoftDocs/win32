---
title: UDM_SETPOS message (Commctrl.h)
description: Sets the current position for an up-down control with 16-bit precision.
ms.assetid: e7c8b55f-3a4f-47e7-8c7d-e47509f27f1d
keywords:
- UDM_SETPOS message Windows Controls
topic_type:
- apiref
api_name:
- UDM_SETPOS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# UDM\_SETPOS message

Sets the current position for an up-down control with 16-bit precision.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

New position for the up-down control. If the parameter is outside the control's specified range, *lParam* will be set to the nearest valid value.

</dd> </dl>

## Return value

The return value is the previous position.

## Remarks

This message only supports 16-bit positions. If 32-bit values have been enabled for an up-down control with [**UDM\_SETRANGE32**](udm-setrange32.md), use [**UDM\_SETPOS32**](udm-setpos32.md).

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

[**UDM\_GETPOS**](udm-getpos.md)
</dt> </dl>

 

 





