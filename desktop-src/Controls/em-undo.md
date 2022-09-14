---
title: EM_UNDO message (Winuser.h)
description: This message undoes the last edit control operation in the control's undo queue. You can send this message to either an edit control or a rich edit control.
ms.assetid: c4bff128-0383-40c5-8f29-7738f7f26871
keywords:
- EM_UNDO message Windows Controls
topic_type:
- apiref
api_name:
- EM_UNDO
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_UNDO message

This message undoes the last edit control operation in the control's undo queue. You can send this message to either an edit control or a rich edit control.

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

For a single-line edit control, the return value is always **TRUE**.

For a multiline edit control, the return value is **TRUE** if the undo operation is successful, or **FALSE** if the undo operation fails.

## Remarks

**Edit controls and Rich Edit 1.0:** An undo operation can also be undone. For example, you can restore deleted text with the first **EM\_UNDO** message, and remove the text again with a second **EM\_UNDO** message as long as there is no intervening edit operation.

**Rich Edit 2.0 and later:** The undo feature is multilevel so sending two **EM\_UNDO** messages will undo the last two operations in the undo queue. To redo an operation, send the [**EM\_REDO**](em-redo.md) message.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**EM\_CANUNDO**](em-canundo.md)
</dt> </dl>

 

 





