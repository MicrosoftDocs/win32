---
title: EM_FINDTEXTEXW message (Richedit.h)
description: EM_FINDTEXTEXW message - Finds Unicode text within a rich edit control.
ms.assetid: 7b90ef06-0395-430e-8b5d-b392481a5f70
keywords:
- EM_FINDTEXTEXW message Windows Controls
topic_type:
- apiref
api_name:
- EM_FINDTEXTEXW
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_FINDTEXTEXW message

Finds Unicode text within a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the behavior of the search operation. This parameter can be one or more of the following values.



| Value                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FR_DOWN"></span><span id="fr_down"></span><dl> <dt>**FR\_DOWN**</dt> </dl>                               | Microsoft Rich Edit 2.0 and later: If set, the search is forward from **FINDTEXTEX.chrg.cpMin**; if not set, the search is backward from **FINDTEXTEX.chrg.cpMin**. <br/> Microsoft Rich Edit 1.0: The FR\_DOWN flag is ignored. The search is always forward.<br/> |
| <span id="FR_MATCHALEFHAMZA"></span><span id="fr_matchalefhamza"></span><dl> <dt>**FR\_MATCHALEFHAMZA**</dt> </dl> | If set, the search differentiates between alefs with different accents. If not set, Arabic and Hebrew alefs with different accents are all matched by the alef character. <br/>                                                                                           |
| <span id="FR_MATCHCASE"></span><span id="fr_matchcase"></span><dl> <dt>**FR\_MATCHCASE**</dt> </dl>                | If set, the search operation is case-sensitive. If not set, the search operation is case-insensitive.<br/>                                                                                                                                                                |
| <span id="FR_MATCHDIAC"></span><span id="fr_matchdiac"></span><dl> <dt>**FR\_MATCHDIAC**</dt> </dl>                | If set, the search operation considers diacritical marks. If not set, Arabic and Hebrew diacritical marks are ignored. <br/>                                                                                                                                              |
| <span id="FR_MATCHKASHIDA"></span><span id="fr_matchkashida"></span><dl> <dt>**FR\_MATCHKASHIDA**</dt> </dl>       | If set, the search operation considers kashidas. If not set, Arabic and Hebrew kashidas are ignored. <br/>                                                                                                                                                                |
| <span id="FR_WHOLEWORD"></span><span id="fr_wholeword"></span><dl> <dt>**FR\_WHOLEWORD**</dt> </dl>                | If set, the operation searches only for whole words that match the search string. If not set, the operation also searches for word fragments that match the search string.<br/>                                                                                           |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A [**FINDTEXTEXW**](/windows/desktop/api/Richedit/ns-richedit-findtextexa) structure containing information about the find operation.

</dd> </dl>

## Return value

If the target string is found, the return value is the zero-based position of the first character of the match. If the target is not found, the return value is -1.

## Remarks

Use this message to find Unicode strings. For ANSI;, use [**EM\_FINDTEXTEX**](em-findtextex.md).

The **cpMin** member of **FINDTEXTEX.chrg** always specifies the starting-point of the search, and **cpMax** specifies the end point. When searching backward, **cpMin** must be equal to or greater than **cpMax**. When searching forward, a value of -1 in **cpMax** extends the search range to the end of the text.

If the search operation finds a match, the **chrgText** member of the [**FINDTEXTEX**](/windows/desktop/api/Richedit/ns-richedit-findtextexa) structure returns the range of character positions that contains the matching text.

**EM\_FINDTEXTEXW** uses the [**FINDTEXTEXW**](/windows/desktop/api/Richedit/ns-richedit-findtextexa) structure, while [**EM\_FINDTEXTW**](em-findtextw.md) uses the [**FINDTEXTW**](/windows/win32/api/richedit/ns-richedit-findtexta) structure. The difference is that **EM\_FINDTEXTEXW** reports the range of text that was found.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_FINDTEXTW**](em-findtextw.md)
</dt> </dl>

 

 





