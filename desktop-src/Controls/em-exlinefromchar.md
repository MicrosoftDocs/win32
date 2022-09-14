---
title: EM_EXLINEFROMCHAR message (Richedit.h)
description: Determines which line contains the specified character in a rich edit control.
ms.assetid: 497482fb-9640-4063-a9f5-e0691b65225d
keywords:
- EM_EXLINEFROMCHAR message Windows Controls
topic_type:
- apiref
api_name:
- EM_EXLINEFROMCHAR
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_EXLINEFROMCHAR message

Determines which line contains the specified character in a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Zero-based index of the character.

</dd> </dl>

## Return value

This message returns the zero-based index of the line.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





