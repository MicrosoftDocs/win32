---
title: EM_LINELENGTH message (Winuser.h)
description: Retrieves the length, in characters, of a line in an edit control. You can send this message to either an edit control or a rich edit control.
ms.assetid: cfb0632c-9ba9-4864-939a-dbbaed6c177e
keywords:
- EM_LINELENGTH message Windows Controls
topic_type:
- apiref
api_name:
- EM_LINELENGTH
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_LINELENGTH message

Retrieves the length, in characters, of a line in an edit control. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The character index of a character in the line whose length is to be retrieved. If this parameter is greater than the number of characters in the control, the return value is zero.

This parameter can be -1. In this case, the message returns the number of unselected characters on lines containing selected characters. For example, if the selection extended from the fourth character of one line through the eighth character from the end of the next line, the return value would be 10 (three characters on the first line and seven on the next).

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

For multiline edit controls, the return value is the length, in **TCHAR**s, of the line specified by the *wParam* parameter. For ANSI text, this is the number of bytes; for Unicode text, this is the number of characters. It does not include the carriage-return character at the end of the line.

For single-line edit controls, the return value is the length, in **TCHAR**s, of the text in the edit control.

If *wParam* is greater than the number of characters in the control, the return value is zero.

## Remarks

Use the [**EM\_LINEINDEX**](em-lineindex.md) message to retrieve a character index for a given line number within a multiline edit control.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**EM\_LINEINDEX**](em-lineindex.md)
</dt> </dl>

 

 





