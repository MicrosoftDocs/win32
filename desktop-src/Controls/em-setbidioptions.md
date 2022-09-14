---
title: EM_SETBIDIOPTIONS message (Richedit.h)
description: The EM\_SETBIDIOPTIONS message sets the current state of the bidirectional options in the rich edit control.
ms.assetid: b518e423-317a-4654-9d9f-c501028e2a0a
keywords:
- EM_SETBIDIOPTIONS message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETBIDIOPTIONS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETBIDIOPTIONS message

The **EM\_SETBIDIOPTIONS** message sets the current state of the bidirectional options in the rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**BIDIOPTIONS**](/windows/desktop/api/Richedit/ns-richedit-bidioptions) structure that indicates how to set the state of the bidirectional options in the rich edit control.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

The rich edit control must be in plain text mode or **EM\_SETBIDIOPTIONS** will not do anything.

In plain text controls, **EM\_SETBIDIOPTIONS** automatically determines the paragraph direction and/or alignment based on the context rules. These rules state that the direction and/or alignment is derived from the first strong character in the control. A strong character is one from which text direction can be determined (see Unicode Standard version 2.0). The paragraph direction and/or alignment is applied to the default format.

**EM\_SETBIDIOPTIONS** only switches the default paragraph format to RTL (right to left) if it finds an RTL character,

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | Rich Edit 3.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**BIDIOPTIONS**](/windows/desktop/api/Richedit/ns-richedit-bidioptions)
</dt> <dt>

[**EM\_GETBIDIOPTIONS**](em-getbidioptions.md)
</dt> </dl>

 

 





