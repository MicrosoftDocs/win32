---
title: EM_SETSEL message (Winuser.h)
description: Selects a range of characters in an edit control. You can send this message to either an edit control or a rich edit control.
ms.assetid: 5cb7ff1e-18e8-49c8-8072-872cf32b18b0
keywords:
- EM_SETSEL message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETSEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETSEL message

Selects a range of characters in an edit control. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The starting character position of the selection.

</dd> <dt>

*lParam* 
</dt> <dd>

The ending character position of the selection.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

The start value can be greater than the end value. The lower of the two values specifies the character position of the first character in the selection. The higher value specifies the position of the first character beyond the selection.

The start value is the anchor point of the selection, and the end value is the active end. If the user uses the SHIFT key to adjust the size of the selection, the active end can move but the anchor point remains the same.

If the start is 0 and the end is -1, all the text in the edit control is selected. If the start is -1, any current selection is deselected.

**Edit controls:** The control displays a flashing caret at the end position regardless of the relative values of start and end.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

If the edit control has the [**ES\_NOHIDESEL**](edit-control-styles.md) style, the selected text is highlighted regardless of whether the control has focus. Without the **ES\_NOHIDESEL** style, the selected text is highlighted only when the edit control has the focus.

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

[**EM\_GETSEL**](em-getsel.md)
</dt> <dt>

[**EM\_REPLACESEL**](em-replacesel.md)
</dt> <dt>

[**EM\_SCROLLCARET**](em-scrollcaret.md)
</dt> <dt>

[**EM\_EXSETSEL**](em-exsetsel.md)
</dt> </dl>

 

 





