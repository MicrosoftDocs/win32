---
title: EM_LINESCROLL message (Winuser.h)
description: Scrolls the text in a multiline edit control.
ms.assetid: 5398082d-f1ef-4a3a-9e5a-83cf286adbf1
keywords:
- EM_LINESCROLL message Windows Controls
topic_type:
- apiref
api_name:
- EM_LINESCROLL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_LINESCROLL message

Scrolls the text in a multiline edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

**Edit controls:** The number of characters to scroll horizontally.

**Rich edit controls:** This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

The number of lines to scroll vertically.

</dd> </dl>

## Return value

If the message is sent to a multiline edit control, the return value is **TRUE**.

If the message is sent to a single-line edit control, the return value is **FALSE**.

## Remarks

The control does not scroll vertically past the last line of text in the edit control. If the current line plus the number of lines specified by the *lParam* parameter exceeds the total number of lines in the edit control, the value is adjusted so that the last line of the edit control is scrolled to the top of the edit-control window.

**Edit controls:** The **EM\_LINESCROLL** message scrolls the text vertically or horizontally in a multiline edit control. The **EM\_LINESCROLL** message can be used to scroll horizontally past the last character of any line.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. The **EM\_LINESCROLL** message scrolls the text vertically in a multiline edit control. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 





