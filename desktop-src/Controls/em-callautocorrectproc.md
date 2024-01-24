---
title: EM_CALLAUTOCORRECTPROC message (Richedit.h)
description: Calls the autocorrect callback function that is stored by the EM\_SETAUTOCORRECTPROC message, provided that the text preceding the insertion point is a candidate for autocorrection.
ms.assetid: 93116467-B345-4FD9-9162-3E01CF3C6F20
keywords:
- EM_CALLAUTOCORRECTPROC message Windows Controls
topic_type:
- apiref
api_name:
- EM_CALLAUTOCORRECTPROC
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_CALLAUTOCORRECTPROC message

Calls the autocorrect callback function that is stored by the [**EM\_SETAUTOCORRECTPROC**](em-setautocorrectproc.md) message, provided that the text preceding the insertion point is a candidate for autocorrection.


```C++
#define EM_CALLAUTOCORRECTPROC       (WM_USER + 255)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A character of type **WCHAR**. If this character is a tab (U+0009), and the character preceding the insertion point isn t a tab, then the character preceding the insertion point is treated as part of the autocorrect candidate string instead of as a string delimiter; otherwise, *wParam* has no effect.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

The return value is zero if the message succeeds, or nonzero if an error occurs.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[*AutoCorrectProc*](/windows/desktop/api/Richedit/nc-richedit-autocorrectproc)
</dt> <dt>

[**EM\_GETAUTOCORRECTPROC**](em-getautocorrectproc.md)
</dt> <dt>

[**EM\_SETAUTOCORRECTPROC**](em-setautocorrectproc.md)
</dt> </dl>

 

 





