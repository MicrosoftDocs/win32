---
title: EM\_GETIMECOMPTEXT message
description: Retrieves the Input Method Editor (IME) composition text.
ms.assetid: '1516305c-5f87-4ae0-97db-8709c71abacc'
keywords: ["EM_GETIMECOMPTEXT message Windows Controls"]
topic_type:
- apiref
api_name:
- EM_GETIMECOMPTEXT
api_location:
- Richedit.h
api_type:
- HeaderDef
---

# EM\_GETIMECOMPTEXT message

Retrieves the Input Method Editor (IME) composition text.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**IMECOMPTEXT**](imecomptext.md) structure.

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



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**IMECOMPTEXT**](imecomptext.md)
</dt> </dl>

 

 





