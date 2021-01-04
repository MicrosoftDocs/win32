---
title: EM_SETWORDBREAKPROC message (Winuser.h)
description: Replaces an edit control's default Wordwrap function with an application-defined Wordwrap function. You can send this message to either an edit control or a rich edit control.
ms.assetid: e5029b75-5f35-43a5-876d-24e81605bb49
keywords:
- EM_SETWORDBREAKPROC message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETWORDBREAKPROC
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETWORDBREAKPROC message

Replaces an edit control's default Wordwrap function with an application-defined Wordwrap function. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

The address of the application-defined Wordwrap function. For more information about breaking lines, see the description of the [*EditWordBreakProc*](/windows/win32/api/winuser/nc-winuser-editwordbreakproca) callback function.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

A Wordwrap function scans a text buffer that contains text to be sent to the screen, looking for the first word that does not fit on the current screen line. The Wordwrap function places this word at the beginning of the next line on the screen.

A Wordwrap function defines the point at which the system should break a line of text for multiline edit controls, usually at a space character that separates two words. Either a multiline or a single-line edit control might call this function when the user presses arrow keys in combination with the CTRL key to move the caret to the next word or previous word. The default Wordwrap function breaks a line of text at a space character. The application-defined function may define the Wordwrap to occur at a hyphen or a character other than the space character.

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

[*EditWordBreakProc*](/windows/win32/api/winuser/nc-winuser-editwordbreakproca)
</dt> <dt>

[**EM\_FMTLINES**](em-fmtlines.md)
</dt> <dt>

[**EM\_GETWORDBREAKPROC**](em-getwordbreakproc.md)
</dt> </dl>

 

