---
title: EM_SETCTFOPENSTATUS message (Richedit.h)
description: Opens or closes the Text Services Framework (TSF) keyboard.
ms.assetid: 9bdabf5a-93db-4b0e-9528-807d262de866
keywords:
- EM_SETCTFOPENSTATUS message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETCTFOPENSTATUS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETCTFOPENSTATUS message

Opens or closes the Text Services Framework (TSF) keyboard.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

To turn on the TSF keyboard, use **TRUE**. To turn off the TSF keyboard, use **FALSE**.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

If successful, this message returns **TRUE**. If unsuccessful, this message returns **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETCTFOPENSTATUS**](em-getctfopenstatus.md)
</dt> </dl>

 

 





