---
title: EM_SETPASSWORDCHAR message (Winuser.h)
description: Sets or removes the password character for an edit control. When a password character is set, that character is displayed in place of the characters typed by the user. You can send this message to either an edit control or a rich edit control.
ms.assetid: 9091892c-9f37-4e06-a084-9326c5f7f31e
keywords:
- EM_SETPASSWORDCHAR message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETPASSWORDCHAR
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETPASSWORDCHAR message

Sets or removes the password character for an edit control. When a password character is set, that character is displayed in place of the characters typed by the user. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The character to be displayed in place of the characters typed by the user. If this parameter is zero, the control removes the current password character and displays the characters typed by the user.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

When an edit control receives the **EM\_SETPASSWORDCHAR** message, the control redraws all visible characters using the character specified by the *wParam* parameter. If *wParam* is zero, the control redraws all visible characters using the characters typed by the user.

If an edit control is created with the [**ES\_PASSWORD**](edit-control-styles.md) style, the default password character is set to an asterisk (\*). If an edit control is created without the **ES\_PASSWORD** style, there is no password character. The **ES\_PASSWORD** style is removed if an **EM\_SETPASSWORDCHAR** message is sent with the *wParam* parameter set to zero.

**Edit controls:** Multiline edit controls do not support the password style or messages.

**Rich Edit:** Supported in Microsoft Rich Edit 2.0 and later. Both single-line and multiline edit controls support the password style and messages. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETPASSWORDCHAR**](em-getpasswordchar.md)
</dt> </dl>

 

 





