---
title: EM_REDO message (Richedit.h)
description: Sends an EM\_REDO message to a rich edit control to redo the next action in the control's redo queue.
ms.assetid: 28ec1ec2-a56d-442f-b3cb-9feeb92edaeb
keywords:
- EM_REDO message Windows Controls
topic_type:
- apiref
api_name:
- EM_REDO
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_REDO message

Sends an **EM\_REDO** message to a rich edit control to redo the next action in the control's redo queue.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

If the **Redo** operation succeeds, the return value is a nonzero value.

If the **Redo** operation fails, the return value is zero.

## Remarks

To determine whether there are any actions in the control's redo queue, send the [**EM\_CANREDO**](em-canredo.md) message.

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

[**EM\_UNDO**](em-undo.md)
</dt> </dl>

 

 





