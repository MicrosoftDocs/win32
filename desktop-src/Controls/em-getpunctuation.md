---
title: EM_GETPUNCTUATION message (Richedit.h)
description: Gets the current punctuation characters for the rich edit control.
ms.assetid: 1c04967b-d75e-4f54-b35b-cd50bac9cdfa
keywords:
- EM_GETPUNCTUATION message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETPUNCTUATION
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETPUNCTUATION message

Gets the current punctuation characters for the rich edit control.

> [!Note]  
> This message is supported only in Asian-language versions of Microsoft Rich Edit 1.0. It is not supported in any later versions of Rich Edit.

 

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The punctuation type can be one of the following values.



| Value                                                                                                                                                      | Meaning                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| <span id="PC_LEADING"></span><span id="pc_leading"></span><dl> <dt>**PC\_LEADING**</dt> </dl>       | Leading punctuation characters<br/>   |
| <span id="PC_FOLLOWING"></span><span id="pc_following"></span><dl> <dt>**PC\_FOLLOWING**</dt> </dl> | Following punctuation characters<br/> |
| <span id="PC_DELIMITER"></span><span id="pc_delimiter"></span><dl> <dt>**PC\_DELIMITER**</dt> </dl> | Delimiter<br/>                        |
| <span id="PC_OVERFLOW"></span><span id="pc_overflow"></span><dl> <dt>**PC\_OVERFLOW**</dt> </dl>    | Not supported<br/>                    |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**PUNCTUATION**](/windows/desktop/api/Richedit/ns-richedit-punctuation) structure that receives the punctuation characters.

</dd> </dl>

## Return value

If the operation succeeds, the return value is a nonzero value.

If the operation fails, the return value is zero.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_SETPUNCTUATION**](em-setpunctuation.md)
</dt> <dt>

[**PUNCTUATION**](/windows/desktop/api/Richedit/ns-richedit-punctuation)
</dt> </dl>

 

 





