---
title: EM_LINEINDEX message (Winuser.h)
description: Gets the character index of the first character of a specified line in a multiline edit control.
ms.assetid: 'vs|controls|~\controls\editcontrols\editcontrolreference\editcontrolmessages\em_lineindex.htm'
keywords:
- EM_LINEINDEX message Windows Controls
topic_type:
- apiref
api_name:
- EM_LINEINDEX
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM_LINEINDEX message (Winuser.h)

Gets the character index of the first character of a specified line in a multiline edit control. A character index is the zero-based index of the character from the beginning of the edit control. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based line number. A value of -1 specifies the current line number (the line that contains the caret).

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is the character index of the line specified in the *wParam* parameter, or it is -1 if the specified line number is greater than the number of lines in the edit control.

## Remarks

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**EM\_LINEFROMCHAR**](em-linefromchar.md)
</dt> </dl>

 

 





