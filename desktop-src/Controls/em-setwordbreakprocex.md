---
title: EM\_SETWORDBREAKPROCEX message
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Pointer to an [*EditWordBreakProcEx*](/windows/win32/Richedit/nc-richedit-editwordbreakprocex?branch=master) function, or **NULL** to use the default procedure.

</dd> </dl>

## Return value

This message returns the address of the previous extended word-break procedure.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EditWordBreakProcEx**](/windows/win32/Richedit/nc-richedit-editwordbreakprocex?branch=master)
</dt> <dt>

[**EM\_GETWORDBREAKPROCEX**](em-getwordbreakprocex.md)
</dt> </dl>

 

 





