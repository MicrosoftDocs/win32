---
title: EM_FINDWORDBREAK message (Richedit.h)
description: Finds the next word break before or after the specified character position or retrieves information about the character at that position.
ms.assetid: b5df1365-4672-4c82-8ae4-ebf8b60bf871
keywords:
- EM_FINDWORDBREAK message Windows Controls
topic_type:
- apiref
api_name:
- EM_FINDWORDBREAK
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_FINDWORDBREAK message

Finds the next word break before or after the specified character position or retrieves information about the character at that position.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the find operation. This parameter can be one of the following values.



| Value                                                                                                                                                                  | Meaning                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WB_CLASSIFY"></span><span id="wb_classify"></span><dl> <dt>**WB\_CLASSIFY**</dt> </dl>                | Returns the character class and word-break flags of the character at the specified position.<br/>                                                                                                                          |
| <span id="WB_ISDELIMITER"></span><span id="wb_isdelimiter"></span><dl> <dt>**WB\_ISDELIMITER**</dt> </dl>       | Returns **TRUE** if the character at the specified position is a delimiter, or **FALSE** otherwise.<br/>                                                                                                                   |
| <span id="WB_LEFT"></span><span id="wb_left"></span><dl> <dt>**WB\_LEFT**</dt> </dl>                            | Finds the nearest character before the specified position that begins a word.<br/>                                                                                                                                         |
| <span id="WB_LEFTBREAK"></span><span id="wb_leftbreak"></span><dl> <dt>**WB\_LEFTBREAK**</dt> </dl>             | Finds the next word end before the specified position. This value is the same as WB\_PREVBREAK.<br/>                                                                                                                       |
| <span id="WB_MOVEWORDLEFT"></span><span id="wb_movewordleft"></span><dl> <dt>**WB\_MOVEWORDLEFT**</dt> </dl>    | Finds the next character that begins a word before the specified position. This value is used during CTRL+LEFT ARROW key processing. This value is the similar to WB\_MOVEWORDPREV. See Remarks for more information.<br/> |
| <span id="WB_MOVEWORDRIGHT"></span><span id="wb_movewordright"></span><dl> <dt>**WB\_MOVEWORDRIGHT**</dt> </dl> | Finds the next character that begins a word after the specified position. This value is used during CTRL+right key processing. This value is similar to WB\_MOVEWORDNEXT. See Remarks for more information.<br/>           |
| <span id="WB_RIGHT"></span><span id="wb_right"></span><dl> <dt>**WB\_RIGHT**</dt> </dl>                         | Finds the next character that begins a word after the specified position.<br/>                                                                                                                                             |
| <span id="WB_RIGHTBREAK"></span><span id="wb_rightbreak"></span><dl> <dt>**WB\_RIGHTBREAK**</dt> </dl>          | Finds the next end-of-word delimiter after the specified position. This value is the same as WB\_NEXTBREAK.<br/>                                                                                                           |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Zero-based character starting position.

</dd> </dl>

## Return value

The message returns a value based on the *wParam* parameter.



| Return code                                                                                    | Description                                                                                                            |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**wParam**</dt> </dl>          | Return Value<br/>                                                                                                |
| <dl> <dt>**WB\_CLASSIFY**</dt> </dl>    | Returns the character class and word-break flags of the character at the specified position.<br/>                |
| <dl> <dt>**WB\_ISDELIMITER**</dt> </dl> | Returns **TRUE** if the character at the specified position is a delimiter; otherwise it returns **FALSE**.<br/> |
| <dl> <dt>**Others**</dt> </dl>          | Returns the character index of the word break.<br/>                                                              |



 

## Remarks

If *wParam* is WB\_LEFT and WB\_RIGHT, the word-break procedure finds word breaks only after delimiters. This matches the functionality of an edit control. If *wParam* is WB\_MOVEWORDLEFT or WB\_MOVEWORDRIGHT, the word-break procedure also compares character classes and word-break flags.

For information about character classes and word-break flags, see [Word and Line Breaks](using-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





