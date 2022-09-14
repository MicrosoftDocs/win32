---
title: EM_FINDTEXTW message (Richedit.h)
description: EM_FINDTEXTW message - Finds Unicode text within a rich edit control.
ms.assetid: 0c1579f5-3b37-4e28-86a2-f4e03e195f38
keywords:
- EM_FINDTEXTW message Windows Controls
topic_type:
- apiref
api_name:
- EM_FINDTEXTW
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_FINDTEXTW message

Finds Unicode text within a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the parameters of the search operation. This parameter can be one or more of the following values.



| Value                                                                                                                                                                     | Meaning                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FR_DOWN"></span><span id="fr_down"></span><dl> <dt>**FR\_DOWN**</dt> </dl>                               | If set, the operation searches from the end of the current selection to the end of the document. If not set, the operation searches from the end of the current selection to the beginning of the document.<br/> |
| <span id="FR_MATCHALEFHAMZA"></span><span id="fr_matchalefhamza"></span><dl> <dt>**FR\_MATCHALEFHAMZA**</dt> </dl> | By default, Arabic and Hebrew alefs with different accents are all matched by the alef character. Set this flag if you want the search to differentiate between alefs with different accents.<br/>               |
| <span id="FR_MATCHCASE"></span><span id="fr_matchcase"></span><dl> <dt>**FR\_MATCHCASE**</dt> </dl>                | If set, the search operation is case-sensitive. If not set, the search operation is case-insensitive.<br/>                                                                                                       |
| <span id="FR_MATCHDIAC"></span><span id="fr_matchdiac"></span><dl> <dt>**FR\_MATCHDIAC**</dt> </dl>                | By default, Arabic and Hebrew diacritical marks are ignored. Set this flag if you want the search operation to consider diacritical marks.<br/>                                                                  |
| <span id="FR_MATCHKASHIDA"></span><span id="fr_matchkashida"></span><dl> <dt>**FR\_MATCHKASHIDA**</dt> </dl>       | By default, Arabic and Hebrew kashidas are ignored. Set this flag if you want the search operation to consider kashidas.<br/>                                                                                    |
| <span id="FR_WHOLEWORD"></span><span id="fr_wholeword"></span><dl> <dt>**FR\_WHOLEWORD**</dt> </dl>                | If set, the operation searches only for whole words that match the search string. If not set, the operation also searches for word fragments that match the search string.<br/>                                  |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A [**FINDTEXTW**](/windows/win32/api/richedit/ns-richedit-findtexta) structure containing information about the find operation.

</dd> </dl>

## Return value

If the target string is found, the return value is the zero-based position of the first character of the match. If the target is not found, the return value is -1.

## Remarks

**EM\_FINDTEXTW** uses the [**FINDTEXTW**](/windows/win32/api/richedit/ns-richedit-findtexta) structure, while [**EM\_FINDTEXTEXW**](em-findtextexw.md) uses the [**FINDTEXTEXW**](/windows/desktop/api/Richedit/ns-richedit-findtextexa) structure. The difference is that **FINDTEXTEXW** reports back the range of text that was found.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_FINDTEXTEXW**](em-findtextexw.md)
</dt> </dl>

 

 





