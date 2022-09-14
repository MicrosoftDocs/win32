---
title: EM_CANREDO message (Richedit.h)
description: Determines whether there are any actions in the control redo queue.
ms.assetid: 4a76adc8-f815-4cf7-8742-b7695e5a0f64
keywords:
- EM_CANREDO message Windows Controls
topic_type:
- apiref
api_name:
- EM_CANREDO
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_CANREDO message

Determines whether there are any actions in the control redo queue.

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

If there are actions in the control redo queue, the return value is a nonzero value.

If the redo queue is empty, the return value is zero.

## Remarks

To redo the most recent undo operation, send the [**EM\_REDO**](em-redo.md) message.

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

[**EM\_GETREDONAME**](em-getredoname.md)
</dt> <dt>

[**EM\_GETUNDONAME**](em-getundoname.md)
</dt> <dt>

[**EM\_REDO**](em-redo.md)
</dt> <dt>

[**EM\_UNDO**](em-undo.md)
</dt> </dl>

 

 





