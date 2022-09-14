---
title: EM_SETHYPHENATEINFO message (Richedit.h)
description: Sets the way a rich edit control does hyphenation.
ms.assetid: 67126cb8-ab50-49a9-b32f-2245debf2fe3
keywords:
- EM_SETHYPHENATEINFO message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETHYPHENATEINFO
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETHYPHENATEINFO message

Sets the way a rich edit control does hyphenation.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Pointer to a [**HYPHENATEINFO**](/windows/win32/api/richedit/ns-richedit-hyphenateinfo) structure.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used, must be zero.

</dd> </dl>

## Remarks

> [!Note]  
> To enable hyphenation, the client must call [**EM\_SETTYPOGRAPHYOPTIONS**](em-settypographyoptions.md), specifying TO\_ADVANCEDTYPOGRAPHY.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETHYPHENATEINFO**](em-gethyphenateinfo.md)
</dt> </dl>

 

 





