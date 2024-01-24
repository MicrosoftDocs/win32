---
title: CB_GETDROPPEDCONTROLRECT message (Winuser.h)
description: An application sends a CB\_GETDROPPEDCONTROLRECT message to retrieve the screen coordinates of a combo box in its dropped-down state.
ms.assetid: fd8d78c0-e1a8-49c8-9e35-a105d00b863c
keywords:
- CB_GETDROPPEDCONTROLRECT message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETDROPPEDCONTROLRECT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_GETDROPPEDCONTROLRECT message

An application sends a **CB\_GETDROPPEDCONTROLRECT** message to retrieve the screen coordinates of a combo box in its dropped-down state.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that receives the coordinates of the combo box in its dropped-down state.

</dd> </dl>

## Return value

If the message succeeds, the return value is nonzero.

If the message fails, the return value is zero.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**RECT**](/windows/win32/api/windef/ns-windef-rect)
</dt> </dl>

 

