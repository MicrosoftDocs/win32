---
title: EM_GETIMEMODEBIAS message (Richedit.h)
description: Retrieves the Input Method Editor (IME) mode bias for a Microsoft Rich Edit control.
ms.assetid: e8ca899f-3423-4814-86e9-133dfd11f9a6
keywords:
- EM_GETIMEMODEBIAS message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETIMEMODEBIAS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETIMEMODEBIAS message

Retrieves the Input Method Editor (IME) mode bias for a Microsoft Rich Edit control.

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

This message returns the current IME mode bias setting.

## Remarks

To get the Text Services Framework mode bias, use [**EM\_GETCTFMODEBIAS**](em-getctfmodebias.md).

The application should call [**EM\_ISIME**](em-isime.md) before calling this function.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_ISIME**](em-isime.md)
</dt> <dt>

[**EM\_GETCTFMODEBIAS**](em-getctfmodebias.md)
</dt> </dl>

 

 





