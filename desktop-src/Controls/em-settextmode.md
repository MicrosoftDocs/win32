---
title: EM_SETTEXTMODE message
description: Sets the text mode or undo level of a rich edit control. The message fails if the control contains any text.
ms.assetid: d6741234-0ef3-4cd2-8817-6c852f1b500d
keywords:
- EM_SETTEXTMODE message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETTEXTMODE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# EM\_SETTEXTMODE message

Sets the text mode or undo level of a rich edit control. The message fails if the control contains any text.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

One or more values from the [**TEXTMODE**](/windows/desktop/api/Richedit/ne-richedit-tagtextmode) enumeration type. The values specify the new settings for the control's text mode and undo level parameters.

Specify one of the following values to set the text mode parameter. If you do not specify a text mode value, the text mode remains at its current setting. 

| Value                                          | Meaning                                                                                                                                                               |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TM\_PLAINTEXT**](/windows/desktop/api/Richedit/ne-richedit-tagtextmode) | Indicates plain text mode, in which the control is similar to a standard edit control. For more information about plain text mode, see the following Remarks section. |
| [**TM\_RICHTEXT**](/windows/desktop/api/Richedit/ne-richedit-tagtextmode)   | Indicates rich text mode, in which the control has standard rich edit functionality. Rich text mode is the default setting.                                           |



 

Specify one of the following values to set the undo level parameter. If you do not specify an undo level value, the undo level remains at its current setting. 

| Value                                                      | Meaning                                                                                                                                                                            |
|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TM\_SINGLELEVELUNDO**](/windows/desktop/api/Richedit/ne-richedit-tagtextmode) | The control allows the user to undo only the last action that can be undone.                                                                                                       |
| [**TM\_MULTILEVELUNDO**](/windows/desktop/api/Richedit/ne-richedit-tagtextmode)   | The control supports multiple undo operations. This is the default setting. Use the [**EM\_SETUNDOLIMIT**](em-setundolimit.md) message to set the maximum number of undo actions. |



 

Specify one of the following values to set the code page parameter. If you do not specify an code page value, the code page remains at its current setting. 

| Value                                                    | Meaning                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TM\_SINGLECODEPAGE**](/windows/desktop/api/Richedit/ne-richedit-tagtextmode) | The control only allows the English keyboard and a keyboard corresponding to the default character set. For example, you could have Greek and English. Note that this prevents Unicode text from entering the control. For example, use this value if a Rich Edit control must be restricted to ANSI text. |
| [**TM\_MULTICODEPAGE**](/windows/desktop/api/Richedit/ne-richedit-tagtextmode)   | The control allows multiple code pages and Unicode text into the control. This is the default setting.                                                                                                                                                                                                     |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> </dl>

## Return value

If the message succeeds, the return value is zero.

If the message fails, the return value is a nonzero value.

## Remarks

In rich text mode, a rich edit control has standard rich edit functionality. However, in plain text mode, the control is similar to a standard edit control:

-   The text in a plain text control can have only one format (such as Bold, 10pt Arial).
-   The user cannot paste rich text formats, such as Rich Text Format (RTF) or embedded objects into a plain text control.
-   Rich text mode controls always have a default end-of-document marker or carriage return, to format paragraphs. Plain text controls, on the other hand, do not need the default, end-of-document marker, so it is omitted.

The control must contain no text when it receives the **EM\_SETTEXTMODE** message. To ensure there is no text, send a [**WM\_SETTEXT**](https://msdn.microsoft.com/library/windows/desktop/ms632644) message with an empty string ("").

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETTEXTMODE**](em-gettextmode.md)
</dt> <dt>

[**EM\_SETUNDOLIMIT**](em-setundolimit.md)
</dt> <dt>

[**TEXTMODE**](/windows/desktop/api/Richedit/ne-richedit-tagtextmode)
</dt> <dt>

[**WM\_SETTEXT**](https://msdn.microsoft.com/library/windows/desktop/ms632644)
</dt> </dl>

 

 





