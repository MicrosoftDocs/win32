---
title: EM_EXGETSEL message (Richedit.h)
description: Retrieves the starting and ending character positions of the selection in a rich edit control.
ms.assetid: 60fcf13e-6c45-4f4e-9b54-70f0985122fb
keywords:
- EM_EXGETSEL message Windows Controls
topic_type:
- apiref
api_name:
- EM_EXGETSEL
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_EXGETSEL message

Retrieves the starting and ending character positions of the selection in a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A [**CHARRANGE**](/windows/desktop/api/Richedit/ns-richedit-charrange) structure that receives the selection range.

</dd> </dl>

## Return value

This message does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**CHARRANGE**](/windows/desktop/api/Richedit/ns-richedit-charrange)
</dt> </dl>

 

 





