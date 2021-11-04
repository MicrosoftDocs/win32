---
title: EM_FINDTEXT message (Richedit.h)
description: EM_FINDTEXT message - Finds text within a rich edit control.
ms.assetid: f19e19a0-d8dd-4d31-b76d-f1f09577dd2d
keywords:
- EM_FINDTEXT message Windows Controls
topic_type:
- apiref
api_name:
- EM_FINDTEXT
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_FINDTEXT message

Finds text within a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specify the parameters of the search operation. This parameter can be one or more of the following values.



| Value                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FR_DOWN"></span><span id="fr_down"></span><dl> <dt>**FR\_DOWN**</dt> </dl>                               | Microsoft Rich Edit 2.0 and later: If set, the search is from the end of the current selection to the end of the document. If not set, the search is from the end of the current selection to the beginning of the document. <br/> Microsoft Rich Edit 1.0: The FR\_DOWN flag is ignored. The search is always from the end of the current selection to the end of the document.<br/> |
| <span id="FR_MATCHALEFHAMZA"></span><span id="fr_matchalefhamza"></span><dl> <dt>**FR\_MATCHALEFHAMZA**</dt> </dl> | Microsoft Rich Edit 3.0 and later: If set, the search differentiates between Arabic alefs with different accents. If not set, all alefs are matched by the alef character alone. <br/>                                                                                                                                                                                                      |
| <span id="FR_MATCHDIAC"></span><span id="fr_matchdiac"></span><dl> <dt>**FR\_MATCHDIAC**</dt> </dl>                | Microsoft Rich Edit 3.0 and later: If set, the search operation considers Arabic and Hebrew diacritical marks. If not set, diacritical marks are ignored. <br/>                                                                                                                                                                                                                             |
| <span id="FR_MATCHKASHIDA"></span><span id="fr_matchkashida"></span><dl> <dt>**FR\_MATCHKASHIDA**</dt> </dl>       | Microsoft Rich Edit 3.0 and later: If set, the search operation considers Arabic kashidas. If not set, kashidas are ignored. <br/>                                                                                                                                                                                                                                                          |
| <span id="FR_MATCHWIDTH"></span><span id="fr_matchwidth"></span><dl> <dt>**FR\_MATCHWIDTH**</dt> </dl>             | Windows 8: If set, single-byte and double-byte versions of the same character are considered to be not equal.<br/>                                                                                                                                                                                                                                                                          |
| <span id="FR_WHOLEWORD"></span><span id="fr_wholeword"></span><dl> <dt>**FR\_WHOLEWORD**</dt> </dl>                | If set, the operation searches only for whole words that match the search string. If not set, the operation also searches for word fragments that match the search string.<br/>                                                                                                                                                                                                             |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A [**FINDTEXT**](/windows/win32/api/richedit/ns-richedit-findtexta) structure containing information about the find operation.

</dd> </dl>

## Return value

If the target string is found, the return value is the zero-based position of the first character of the match. If the target is not found, the return value is -1.

## Remarks

The **cpMin** member of **FINDTEXT.chrg** always specifies the starting-point of the search, and **cpMax** specifies the end point. When searching backward, **cpMin** must be equal to or greater than **cpMax**. When searching forward, a value of -1 in **cpMax** extends the search range to the end of the text.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**FINDTEXT**](/windows/win32/api/richedit/ns-richedit-findtexta)
</dt> </dl>

 

 





