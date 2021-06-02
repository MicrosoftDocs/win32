---
title: EM_LIMITTEXT message (Winuser.h)
description: EM_LIMITTEXT message - Sets the text limit of an edit control.
ms.assetid: 5a605de7-8dc7-4c54-8f18-e0b08c720856
keywords:
- EM_LIMITTEXT message Windows Controls
topic_type:
- apiref
api_name:
- EM_LIMITTEXT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_LIMITTEXT message

Sets the text limit of an edit control. The text limit is the maximum amount of text, in **TCHAR**s, that the user can type into the edit control. You can send this message to either an edit control or a rich edit control.

For edit controls and Microsoft Rich Edit 1.0, bytes are used. For Microsoft Rich Edit 2.0 and later, characters are used.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The maximum number of **TCHAR**s the user can enter. For ANSI text, this is the number of bytes; for Unicode text, this is the number of characters. This number does not include the terminating null character.

**Rich edit controls:** If this parameter is zero, the text length is set to 64,000 characters.

If this parameter is zero, the text length is set to 0x7FFFFFFE characters for single-line edit controls or -1 for multiline edit controls.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

The **EM\_LIMITTEXT** message limits only the text the user can enter. It does not affect any text already in the edit control when the message is sent, nor does it affect the length of the text copied to the edit control by the [**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext) message. If an application uses the **WM\_SETTEXT** message to place more text into an edit control than is specified in the **EM\_LIMITTEXT** message, the user can edit the entire contents of the edit control.

Before **EM\_LIMITTEXT** is called, the default limit for the amount of text a user can enter in an edit control is 32,767 characters.

For single-line edit controls, the text limit is either 0x7FFFFFFE bytes or the value of the *wParam* parameter, whichever is smaller. For multiline edit controls, this value is either -1 byte or the value of the *wParam* parameter, whichever is smaller.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. Use the message [**EM\_EXLIMITTEXT**](em-exlimittext.md) for text length values greater than 64,000. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

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

[**EM\_EXLIMITTEXT**](em-exlimittext.md)
</dt> <dt>

[**Edit\_LimitText**](/windows/desktop/api/Windowsx/nf-windowsx-edit_limittext)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext)
</dt> </dl>

 

