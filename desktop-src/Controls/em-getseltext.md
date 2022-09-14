---
title: EM_GETSELTEXT message (Richedit.h)
description: Retrieves the currently selected text in a rich edit control.
ms.assetid: 56af77c3-f2d7-4b5d-895f-a67c141459e3
keywords:
- EM_GETSELTEXT message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETSELTEXT
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETSELTEXT message

Retrieves the currently selected text in a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a buffer that receives the selected text. The calling application must ensure that the buffer is large enough to hold the selected text.

</dd> </dl>

## Return value

This message returns the number of characters copied, not including the terminating null character.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





