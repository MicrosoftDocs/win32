---
title: EM_GETPASSWORDCHAR message (Winuser.h)
description: Gets the password character that an edit control displays when the user enters text. You can send this message to either an edit control or a rich edit control.
ms.assetid: 874336f6-701b-466a-afa6-0cb3e787ba4c
keywords:
- EM_GETPASSWORDCHAR message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETPASSWORDCHAR
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETPASSWORDCHAR message

Gets the password character that an edit control displays when the user enters text. You can send this message to either an edit control or a rich edit control.

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

The return value specifies the character to be displayed in place of any characters typed by the user. If the return value is **NULL**, there is no password character, and the control displays the characters typed by the user.

## Remarks

If an edit control is created with the [**ES\_PASSWORD**](edit-control-styles.md) style, the default password character is set to an asterisk (\*). If an edit control is created without the **ES\_PASSWORD** style, there is no password character. To change the password character, send the [**EM\_SETPASSWORDCHAR**](em-setpasswordchar.md) message.

**Edit controls:** Multiline edit controls do not support the password style or messages.

**Rich edit:** Supported in Microsoft Rich Edit 2.0 and later. Both single-line and multiline edit controls support the password style and messages. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETPASSWORDCHAR**](em-setpasswordchar.md)
</dt> </dl>

 

 





