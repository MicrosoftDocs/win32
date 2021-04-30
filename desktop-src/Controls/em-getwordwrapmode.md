---
title: EM_GETWORDWRAPMODE message (Richedit.h)
description: Gets the current word wrap and word-break options for the rich edit control.
ms.assetid: a87d80d6-2e9e-40ba-9348-a1cc1ef8ec10
keywords:
- EM_GETWORDWRAPMODE message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETWORDWRAPMODE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETWORDWRAPMODE message

Gets the current word wrap and word-break options for the rich edit control.

> [!Note]  
> This message is supported only in Asian-language versions of Microsoft Rich Edit 1.0. It is not supported in any later versions of Rich Edit.

 

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

The message returns the current word wrap and word-break options.

## Remarks

This message must not be sent by the application-defined, word-break procedure.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





