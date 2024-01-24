---
title: EM_SETUIANAME message (Richedit.h)
description: Sets the name of a rich edit control for UI Automation (UIA).
ms.assetid: 60506FEE-9708-4668-8846-42B0B696DD9A
keywords:
- EM_SETUIANAME message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETUIANAME
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETUIANAME message

Sets the name of a rich edit control for UI Automation (UIA).


```C++
#define EM_SETUIANAME       (WM_USER + 320)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the null-terminated name string.

</dd> </dl>

## Return value

TRUE if the name for UIA is successfully set, otherwise FALSE.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





