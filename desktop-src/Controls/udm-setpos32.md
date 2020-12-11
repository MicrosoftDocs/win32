---
title: UDM_SETPOS32 message (Commctrl.h)
description: Sets the position of an up-down control with 32-bit precision.
ms.assetid: a337f2a1-0e3d-4ff4-a224-57b7f25c4bd0
keywords:
- UDM_SETPOS32 message Windows Controls
topic_type:
- apiref
api_name:
- UDM_SETPOS32
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# UDM\_SETPOS32 message

Sets the position of an up-down control with 32-bit precision.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Variable of type integer that specifies the new position for the up-down control. If the parameter is outside the control's specified range, *lParam* is set to the nearest valid value.

</dd> </dl>

## Return value

Returns the previous position.

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

[**UDM\_GETPOS**](udm-getpos.md)
</dt> <dt>

[**UDM\_SETPOS**](udm-setpos.md)
</dt> <dt>

[**UDM\_GETPOS32**](udm-getpos32.md)
</dt> </dl>

 

 





