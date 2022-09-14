---
title: EM_SETWORDBREAKPROCEX message (Richedit.h)
description: Sets the extended word-break procedure for a rich edit control.
ms.assetid: 2b45f747-ae15-470b-a786-98d8135289da
keywords:
- EM_SETWORDBREAKPROCEX message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETWORDBREAKPROCEX
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETWORDBREAKPROCEX message

Sets the extended word-break procedure for a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [*EditWordBreakProcEx*](/windows/desktop/api/Richedit/nc-richedit-editwordbreakprocex) function, or **NULL** to use the default procedure.

</dd> </dl>

## Return value

This message returns the address of the previous extended word-break procedure.

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

[**EditWordBreakProcEx**](/windows/desktop/api/Richedit/nc-richedit-editwordbreakprocex)
</dt> <dt>

[**EM\_GETWORDBREAKPROCEX**](em-getwordbreakprocex.md)
</dt> </dl>

 

 





