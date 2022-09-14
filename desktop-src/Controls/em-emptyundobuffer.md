---
title: EM_EMPTYUNDOBUFFER message (Winuser.h)
description: Resets the undo flag of an edit control. The undo flag is set whenever an operation within the edit control can be undone. You can send this message to either an edit control or a rich edit control.
ms.assetid: a4ff7bd9-f8ae-4f18-8429-4ceaaeeb0f94
keywords:
- EM_EMPTYUNDOBUFFER message Windows Controls
topic_type:
- apiref
api_name:
- EM_EMPTYUNDOBUFFER
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_EMPTYUNDOBUFFER message

Resets the undo flag of an edit control. The undo flag is set whenever an operation within the edit control can be undone. You can send this message to either an edit control or a rich edit control.

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

This message does not return a value.

## Remarks

The undo flag is automatically reset whenever the edit control receives a [**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext) or [**EM\_SETHANDLE**](em-sethandle.md) message.

**Edit controls and Rich Edit 1.0:** The control can only undo or redo the most recent operation.

**Rich Edit 2.0 and later:** The **EM\_EMPTYUNDOBUFFER** message empties all undo and redo buffers. Rich edit controls enable the user to undo or redo multiple operations.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_CANUNDO**](em-canundo.md)
</dt> <dt>

[**EM\_SETHANDLE**](em-sethandle.md)
</dt> <dt>

[**EM\_UNDO**](em-undo.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext)
</dt> </dl>

 

