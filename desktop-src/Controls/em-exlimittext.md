---
title: EM_EXLIMITTEXT message (Richedit.h)
description: Sets an upper limit to the amount of text the user can type or paste into a rich edit control.
ms.assetid: 66fcdbb9-99ac-4122-b89c-be4aef80fbae
keywords:
- EM_EXLIMITTEXT message Windows Controls
topic_type:
- apiref
api_name:
- EM_EXLIMITTEXT
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_EXLIMITTEXT message

Sets an upper limit to the amount of text the user can type or paste into a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies the maximum amount of text that can be entered. If this parameter is zero, the default maximum is used, which is 64K characters. A COM object counts as a single character.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

The text limit set by the **EM\_EXLIMITTEXT** message does not limit the amount of text that you can stream into a rich edit control using the [**EM\_STREAMIN**](em-streamin.md) message with *lParam* set to SF\_TEXT. However, it does limit the amount of text that you can stream into a rich edit control using the **EM\_STREAMIN** message with *lParam* set to SF\_RTF.

Before **EM\_EXLIMITTEXT** is called, the default limit to the amount of text a user can enter is 32,767 characters.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_STREAMIN**](em-streamin.md)
</dt> </dl>

 

 





