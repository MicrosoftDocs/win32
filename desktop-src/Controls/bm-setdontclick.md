---
title: BM_SETDONTCLICK message (Winuser.h)
description: Sets a flag on a radio button that controls the generation of BN\_CLICKED messages when the button receives focus.
ms.assetid: 91d98bce-abea-4afc-a995-0f426ba7a518
keywords:
- BM_SETDONTCLICK message Windows Controls
topic_type:
- apiref
api_name:
- BM_SETDONTCLICK
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BM\_SETDONTCLICK message

Sets a flag on a radio button that controls the generation of [BN\_CLICKED](bn-clicked.md) messages when the button receives focus.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

A **BOOL** that specifies the state. **TRUE** to set the flag, otherwise **FALSE**.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used. Must be zero.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 





