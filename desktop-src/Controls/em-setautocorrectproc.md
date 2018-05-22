---
title: EM\_SETAUTOCORRECTPROC message
description: Defines the current autocorrect callback procedure.
ms.assetid: '2FA48CFC-0D7C-41EF-8207-5EDC644FF3BC'
keywords: ["EM_SETAUTOCORRECTPROC message Windows Controls"]
topic_type:
- apiref
api_name:
- EM_SETAUTOCORRECTPROC
api_location:
- Richedit.h
api_type:
- HeaderDef
---

# EM\_SETAUTOCORRECTPROC message

Defines the current autocorrect callback procedure.


```C++
#define EM_SETAUTOCORRECTPROC       (WM_USER + 234)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [*AutoCorrectProc*](autocorrectproc.md) callback function.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero

</dd> </dl>

## Return value

If the operation succeeds, the return value is zero. If the operation fails, the return value is a nonzero value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[*AutoCorrectProc*](autocorrectproc.md)
</dt> <dt>

[**EM\_CALLAUTOCORRECTPROC**](em-callautocorrectproc.md)
</dt> <dt>

[**EM\_GETAUTOCORRECTPROC**](em-getautocorrectproc.md)
</dt> </dl>

 

 





