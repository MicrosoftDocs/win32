---
title: EM_GETIMEOPTIONS message (Richedit.h)
description: Retrieves the current Input Method Editor (IME) options.
ms.assetid: 81ec89b9-dabd-487e-805e-e3c2e58e3068
keywords:
- EM_GETIMEOPTIONS message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETIMEOPTIONS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETIMEOPTIONS message

Retrieves the current Input Method Editor (IME) options.

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

This message returns one or more of the IME option flag values described in the [**EM\_SETIMEOPTIONS**](em-setimeoptions.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETIMEOPTIONS**](em-setimeoptions.md)
</dt> </dl>

 

 





