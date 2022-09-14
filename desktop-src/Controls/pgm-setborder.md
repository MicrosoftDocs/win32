---
title: PGM_SETBORDER message (Commctrl.h)
description: Sets the current border size for the pager control. You can send this message explicitly or use the Pager\_SetBorder macro.
ms.assetid: 073a1f9e-f05b-4203-9035-8106e87e55cd
keywords:
- PGM_SETBORDER message Windows Controls
topic_type:
- apiref
api_name:
- PGM_SETBORDER
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PGM\_SETBORDER message

Sets the current border size for the pager control. You can send this message explicitly or use the [**Pager\_SetBorder**](/windows/desktop/api/Commctrl/nf-commctrl-pager_setborder) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

New size of the border, in pixels. This value should not be larger than the pager button or less than zero. If *lParam* is too large, the border will be drawn the same size as the button. If *lParam* is negative, the border size will be set to zero.

</dd> </dl>

## Return value

Returns an INT value that contains the previous border size, in pixels.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





