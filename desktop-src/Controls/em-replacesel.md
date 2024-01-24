---
title: EM_REPLACESEL message (Winuser.h)
description: Replaces the selected text in an edit control or a rich edit control with the specified text.
ms.assetid: 525e6f5a-f52f-4bab-bc76-caa484729897
keywords:
- EM_REPLACESEL message Windows Controls
topic_type:
- apiref
api_name:
- EM_REPLACESEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_REPLACESEL message

Replaces the selected text in an edit control or a rich edit control with the specified text.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies whether the replacement operation can be undone. If this is **TRUE**, the operation can be undone. If this is **FALSE** , the operation cannot be undone.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a null-terminated string containing the replacement text.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

Use the **EM\_REPLACESEL** message to replace only a portion of the text in an edit control. To replace all of the text, use the [**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext) message.

If there is no selection, the replacement text is inserted at the caret.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

In a rich edit control, the replacement text takes the formatting of the character at the caret or, if there is a selection, of the first character in the selection.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext)
</dt> </dl>

 

