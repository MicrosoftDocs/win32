---
title: EM_GETLINECOUNT message (Winuser.h)
description: Gets the number of lines in a multiline edit control. You can send this message to either an edit control or a rich edit control.
ms.assetid: 9fe63c10-7395-4f98-a672-14960a70d14f
keywords:
- EM_GETLINECOUNT message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETLINECOUNT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM_GETLINECOUNT message (Winuser.h)

Gets the number of lines in a multiline edit control. You can send this message to either an edit control or a rich edit control.

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

The return value is an integer specifying the total number of text lines in the multiline edit control or rich edit control. If the control has no text, the return value is 1. The return value will never be less than 1.

## Remarks

The **EM\_GETLINECOUNT** message retrieves the total number of text lines, not just the number of lines that are currently visible.

If the Wordwrap feature is enabled, the number of lines can change when the dimensions of the editing window change.

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

[**EM\_GETLINE**](em-getline.md)
</dt> <dt>

[**EM\_LINELENGTH**](em-linelength.md)
</dt> <dt>

[**Edit\_GetLineCount**](/windows/desktop/api/Windowsx/nf-windowsx-edit_getlinecount)
</dt> </dl>

 

 





