---
title: EM_GETTEXTLENGTHEX message (Richedit.h)
description: Calculates text length in various ways. It is usually called before creating a buffer to receive the text from the control.
ms.assetid: 42c89b7b-e48d-4517-9993-ce58ff9e4e40
keywords:
- EM_GETTEXTLENGTHEX message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETTEXTLENGTHEX
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETTEXTLENGTHEX message

Calculates text length in various ways. It is usually called before creating a buffer to receive the text from the control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Pointer to a [**GETTEXTLENGTHEX**](/windows/desktop/api/Richedit/ns-richedit-gettextlengthex) structure that receives the text length information.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> </dl>

## Return value

The message returns the number of **TCHAR**s in the edit control, depending on the setting of the flags in the [**GETTEXTLENGTHEX**](/windows/desktop/api/Richedit/ns-richedit-gettextlengthex) structure. If incompatible flags were set in the **flags** member, the message returns E\_INVALIDARG .

## Remarks

This message is a fast and easy way to determine the number of characters in the Unicode version of the rich edit control. However, for a non-Unicode target code page you will potentially be converting to a combination of single-byte and double-byte characters.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**GETTEXTLENGTHEX**](/windows/desktop/api/Richedit/ns-richedit-gettextlengthex)
</dt> </dl>

 

 





