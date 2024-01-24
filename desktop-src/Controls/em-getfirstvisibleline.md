---
title: EM_GETFIRSTVISIBLELINE message (Winuser.h)
description: Gets the zero-based index of the uppermost visible line in a multiline edit control. You can send this message to either an edit control or a rich edit control.
ms.assetid: 022838d2-7948-4c5a-92ca-655822c4f672
keywords:
- EM_GETFIRSTVISIBLELINE message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETFIRSTVISIBLELINE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETFIRSTVISIBLELINE message

Gets the zero-based index of the uppermost visible line in a multiline edit control. You can send this message to either an edit control or a rich edit control.

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

The return value is the zero-based index of the uppermost visible line in a multiline edit control.

**Edit controls:** For single-line edit controls, the return value is the zero-based index of the first visible character.

**Rich edit controls:** For single-line rich edit controls, the return value is zero.

## Remarks

The number of lines and the length of the lines in an edit control depend on the width of the control and the current Wordwrap setting.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 





