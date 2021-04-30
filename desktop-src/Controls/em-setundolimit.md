---
title: EM_SETUNDOLIMIT message (Richedit.h)
description: Sets the maximum number of actions that can stored in the undo queue of a rich edit control.
ms.assetid: 485dbcda-89f4-40de-ad55-cd524958e910
keywords:
- EM_SETUNDOLIMIT message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETUNDOLIMIT
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETUNDOLIMIT message

Sets the maximum number of actions that can stored in the undo queue of a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the maximum number of actions that can be stored in the undo queue.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> </dl>

## Return value

The return value is the new maximum number of undo actions for the rich edit control. This value may be less than *wParam* if memory is limited.

## Remarks

By default, the maximum number of actions in the undo queue is 100. If you increase this number, there must be enough available memory to accommodate the new number. For better performance, set the limit to the smallest possible value.

Setting the limit to zero disables the **Undo** feature.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_CANREDO**](em-canredo.md)
</dt> <dt>

[**EM\_GETREDONAME**](em-getredoname.md)
</dt> <dt>

[**EM\_GETUNDONAME**](em-getundoname.md)
</dt> <dt>

[**EM\_REDO**](em-redo.md)
</dt> <dt>

[**EM\_UNDO**](em-undo.md)
</dt> </dl>

 

 





