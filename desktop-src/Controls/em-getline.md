---
title: EM_GETLINE message (Winuser.h)
description: Copies a line of text from an edit control and places it in a specified buffer. You can send this message to either an edit control or a rich edit control.
ms.assetid: ff56d2c6-5013-46c6-90d8-ee2bdc9074b1
keywords:
- EM_GETLINE message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETLINE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM_GETLINE message (Winuser.h)

Copies a line of text from an edit control and places it in a specified buffer. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the line to retrieve from a multiline edit control. A value of zero specifies the topmost line. This parameter is ignored by a single-line edit control.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the buffer that receives a copy of the line. Before sending the message, set the first word of this buffer to the size, in **TCHAR**s, of the buffer. For ANSI text, this is the number of bytes; for Unicode text, this is the number of characters. The size in the first word is overwritten by the copied line.

</dd> </dl>

## Return value

The return value is the number of **TCHAR**s copied. The return value is zero if the line number specified by the *wParam* parameter is greater than the number of lines in the edit control.

## Remarks

**Edit controls:** The copied line does not contain a terminating null character.

**Rich edit controls:** Supported in Microsoft Rich Edit 1.0 and later. The copied line does not contain a terminating null character, unless no text was copied. If no text was copied, the message places a null character at the beginning of the buffer. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

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

[**EM\_LINELENGTH**](em-linelength.md)
</dt> <dt>

[**Edit\_GetLine**](/windows/desktop/api/Windowsx/nf-windowsx-edit_getline)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_GETTEXT**](/windows/desktop/winmsg/wm-gettext)
</dt> </dl>

 

