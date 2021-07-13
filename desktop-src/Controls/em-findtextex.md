---
title: EM_FINDTEXTEX message (Richedit.h)
description: EM_FINDTEXTEX message - Finds text within a rich edit control.
ms.assetid: f1bf925b-2776-40b8-9d05-8484daf8d989
keywords:
- EM_FINDTEXTEX message Windows Controls
topic_type:
- apiref
api_name:
- EM_FINDTEXTEX
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_FINDTEXTEX message

Finds text within a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the behavior of the search operation. This parameter can be one or more of the following values.



| Value                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FR_DOWN"></span><span id="fr_down"></span><dl> <dt>**FR\_DOWN**</dt> </dl>                               | Microsoft Rich Edit 2.0 and later: If set, the search is forward from **FINDTEXTEX.chrg.cpMin**; if not set, the search is backward from **FINDTEXTEX.chrg.cpMin**. <br/> Microsoft Rich Edit 1.0: The FR\_DOWN flag is ignored. The search is always forward.<br/> |
| <span id="FR_MATCHALEFHAMZA"></span><span id="fr_matchalefhamza"></span><dl> <dt>**FR\_MATCHALEFHAMZA**</dt> </dl> | Microsoft Rich Edit 3.0 and later: If set, the search differentiates between Arabic and Hebrew alefs with different accents. If not set, all alefs are matched by the alef character alone. <br/>                                                                         |
| <span id="FR_MATCHCASE"></span><span id="fr_matchcase"></span><dl> <dt>**FR\_MATCHCASE**</dt> </dl>                | If set, the search operation is case-sensitive. If not set, the search operation is case-insensitive. <br/>                                                                                                                                                               |
| <span id="FR_MATCHDIAC"></span><span id="fr_matchdiac"></span><dl> <dt>**FR\_MATCHDIAC**</dt> </dl>                | Microsoft Rich Edit 3.0 and later: If set, the search operation considers Arabic and Hebrew diacritical marks. If not set, diacritical marks are ignored. <br/>                                                                                                           |
| <span id="FR_MATCHKASHIDA"></span><span id="fr_matchkashida"></span><dl> <dt>**FR\_MATCHKASHIDA**</dt> </dl>       | Microsoft Rich Edit 3.0 and later: If set, the search operation considers Arabic and Hebrew kashidas. If not set, kashidas are ignored. <br/>                                                                                                                             |
| <span id="FR_WHOLEWORD"></span><span id="fr_wholeword"></span><dl> <dt>**FR\_WHOLEWORD**</dt> </dl>                | If set, the operation searches only for whole words that match the search string. If not set, the operation also searches for word fragments that match the search string.<br/>                                                                                           |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A [**FINDTEXTEX**](/windows/desktop/api/Richedit/ns-richedit-findtextexa) structure containing information about the find operation.

</dd> </dl>

## Return value

If the target string is found, the return value is the zero-based position of the first character of the match. If the target is not found, the return value is -1.

## Remarks

Use this message to find ANSI strings. For Unicode, use [**EM\_FINDTEXTEXW**](em-findtextexw.md).

The **cpMin** member of **FINDTEXTEX.chrg** always specifies the starting-point of the search, and **cpMax** specifies the end point. When searching backward, **cpMin** must be equal to or greater than **cpMax**. When searching forward, a value of -1 in **cpMax** extends the search range to the end of the text.

If the search operation finds a match, the **chrgText** member of the [**FINDTEXTEX**](/windows/desktop/api/Richedit/ns-richedit-findtextexa) structure returns the range of character positions that contains the matching text.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_FINDTEXT**](em-findtext.md)
</dt> </dl>

 

 





