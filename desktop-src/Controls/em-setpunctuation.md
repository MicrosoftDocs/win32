---
title: EM_SETPUNCTUATION message (Richedit.h)
description: Sets the punctuation characters for a rich edit control.
ms.assetid: c0c8ad14-63e2-4be8-8fc0-6b8ef9be4522
keywords:
- EM_SETPUNCTUATION message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETPUNCTUATION
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETPUNCTUATION message

Sets the punctuation characters for a rich edit control.

> [!Note]  
> This message is supported only in Asian-language versions of Microsoft Rich Edit 1.0. It is not supported in any later versions.

 

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the punctuation type, which can be one of the following values.



| Value                                                                                                                                                      | Meaning                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <span id="PC_LEADING"></span><span id="pc_leading"></span><dl> <dt>**PC\_LEADING**</dt> </dl>       | Leading punctuation characters.<br/>   |
| <span id="PC_FOLLOWING"></span><span id="pc_following"></span><dl> <dt>**PC\_FOLLOWING**</dt> </dl> | Following punctuation characters.<br/> |
| <span id="PC_DELIMITER"></span><span id="pc_delimiter"></span><dl> <dt>**PC\_DELIMITER**</dt> </dl> | Delimiter.<br/>                        |
| <span id="PC_OVERFLOW_"></span><span id="pc_overflow_"></span><dl> <dt>**PC\_OVERFLOW** </dt> </dl> | Not supported.<br/>                    |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**PUNCTUATION**](/windows/desktop/api/Richedit/ns-richedit-punctuation) structure that contains the punctuation characters.

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

[**EM\_GETPUNCTUATION**](em-getpunctuation.md)
</dt> <dt>

[**PUNCTUATION**](/windows/desktop/api/Richedit/ns-richedit-punctuation)
</dt> </dl>

 

 





