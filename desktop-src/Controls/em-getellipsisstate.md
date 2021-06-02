---
title: EM_GETELLIPSISSTATE message (Richedit.h)
description: Retrieves the current ellipsis state.
ms.assetid: D02AE225-F5BF-401A-9877-55C68946CDBE
keywords:
- EM_GETELLIPSISSTATE message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETELLIPSISSTATE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETELLIPSISSTATE message

Retrieves the current ellipsis state.


```C++
#define EM_GETELLIPSISSTATE       (WM_USER + 322)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

The return value is TRUE if an ellipsis is being displayed and FALSE otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETELLIPSISMODE**](em-getellipsismode.md)
</dt> <dt>

[**EM\_SETELLIPSISMODE**](em-setellipsismode.md)
</dt> </dl>

 

 





