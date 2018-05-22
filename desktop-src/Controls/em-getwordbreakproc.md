---
title: EM\_GETWORDBREAKPROC message
description: Gets the address of the current Wordwrap function. You can send this message to either an edit control or a rich edit control.
ms.assetid: '564b4b1b-913f-4040-bb28-eea50c0c3738'
keywords: ["EM_GETWORDBREAKPROC message Windows Controls"]
topic_type:
- apiref
api_name:
- EM_GETWORDBREAKPROC
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# EM\_GETWORDBREAKPROC message

Gets the address of the current Wordwrap function. You can send this message to either an edit control or a rich edit control.

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

The return value specifies the address of the application-defined Wordwrap function. The return value is **NULL** if no Wordwrap function exists.

## Remarks

A Wordwrap function scans a text buffer that contains text to be sent to the display, looking for the first word that does not fit on the current display line. The wordwrap function places this word at the beginning of the next line on the display. A Wordwrap function defines the point at which the system should break a line of text for multiline edit controls, usually at a space character that separates two words.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[*EditWordBreakProc*](editwordbreakproc.md)
</dt> <dt>

[**EM\_FMTLINES**](em-fmtlines.md)
</dt> <dt>

[**EM\_SETWORDBREAKPROC**](em-setwordbreakproc.md)
</dt> </dl>

 

 





