---
title: EM_SETWORDWRAPMODE message (Richedit.h)
description: Sets the word-wrapping and word-breaking options for a rich edit control.
ms.assetid: 43703ac8-6ae5-470b-9156-e60330ef97c4
keywords:
- EM_SETWORDWRAPMODE message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETWORDWRAPMODE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETWORDWRAPMODE message

Sets the word-wrapping and word-breaking options for a rich edit control.

> [!Note]  
> This message is supported only in Asian-language versions of Microsoft Rich Edit 1.0. It is not supported in any later versions.

 

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies one or more of the following values.



| Value                                                                                                                                                         | Meaning                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| <span id="WBF_WORDWRAP"></span><span id="wbf_wordwrap"></span><dl> <dt>**WBF\_WORDWRAP**</dt> </dl>    | Enables Asian-specific word wrap operations, such as kinsoku in Japanese. <br/>                                 |
| <span id="WBF_WORDBREAK"></span><span id="wbf_wordbreak"></span><dl> <dt>**WBF\_WORDBREAK**</dt> </dl> | Enables English word-breaking operations in Japanese and Chinese. Enables Hangeul word-breaking operation.<br/> |
| <span id="WBF_OVERFLOW"></span><span id="wbf_overflow"></span><dl> <dt>**WBF\_OVERFLOW**</dt> </dl>    | Recognizes overflow punctuation. (Not currently supported.)<br/>                                                |
| <span id="WBF_LEVEL1"></span><span id="wbf_level1"></span><dl> <dt>**WBF\_LEVEL1**</dt> </dl>          | Sets the Level 1 punctuation table as the default.<br/>                                                         |
| <span id="WBF_LEVEL2"></span><span id="wbf_level2"></span><dl> <dt>**WBF\_LEVEL2**</dt> </dl>          | Sets the Level 2 punctuation table as the default.<br/>                                                         |
| <span id="WBF_CUSTOM"></span><span id="wbf_custom"></span><dl> <dt>**WBF\_CUSTOM**</dt> </dl>          | Sets the application-defined punctuation table.<br/>                                                            |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> </dl>

## Return value

This message returns the current word-wrapping and word-breaking options.

## Remarks

This message must not be sent by the application defined word breaking procedure.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





