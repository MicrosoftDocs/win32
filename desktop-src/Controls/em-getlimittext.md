---
title: EM_GETLIMITTEXT message (Winuser.h)
description: Gets the current text limit for an edit control. You can send this message to either an edit control or a rich edit control.
ms.assetid: 778967f0-c090-46a2-9f27-194b17bbb1be
keywords:
- EM_GETLIMITTEXT message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETLIMITTEXT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETLIMITTEXT message

Gets the current text limit for an edit control. You can send this message to either an edit control or a rich edit control.

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

The return value is the text limit.

## Remarks

**Edit controls, Rich Edit 2.0 and later:** The text limit is the maximum amount of text, in **TCHAR**s, that the control can contain. For ANSI text, this is the number of bytes; for Unicode text, this is the number of characters. Two documents with the same character limit will yield the same text limit, even if one is ANSI and the other is Unicode.

**Rich Edit 1.0:** The text limit is the maximum amount of text, in bytes, that the rich edit control can contain.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETLIMITTEXT**](em-setlimittext.md)
</dt> </dl>

 

 





