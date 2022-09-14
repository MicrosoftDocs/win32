---
title: EM_GETIMECOMPTEXT message (Richedit.h)
description: Retrieves the Input Method Editor (IME) composition text.
ms.assetid: 1516305c-5f87-4ae0-97db-8709c71abacc
keywords:
- EM_GETIMECOMPTEXT message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETIMECOMPTEXT
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETIMECOMPTEXT message

Retrieves the Input Method Editor (IME) composition text.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**IMECOMPTEXT**](/windows/desktop/api/Richedit/ns-richedit-imecomptext) structure.

</dd> <dt>

*lParam* 
</dt> <dd>

The buffer that receives the composition text. The size of this buffer is contained in the **cb** member of the *wParam* structure.

</dd> </dl>

## Return value

If successful, the return value is the number of Unicode characters copied to the buffer. Otherwise, it is zero.

## Remarks

This message only takes Unicode strings.

**Security Warning:** Be sure to have a buffer sufficient for the size of the input. Failure to do so could cause problems for your application.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**IMECOMPTEXT**](/windows/desktop/api/Richedit/ns-richedit-imecomptext)
</dt> </dl>

 

 





