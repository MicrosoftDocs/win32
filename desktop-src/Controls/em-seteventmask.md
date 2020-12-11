---
title: EM_SETEVENTMASK message (Richedit.h)
description: Sets the event mask for a rich edit control. The event mask specifies which notification codes the control sends to its parent window.
ms.assetid: 139f6e44-fc54-40f2-a3f6-2b7efc819cae
keywords:
- EM_SETEVENTMASK message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETEVENTMASK
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETEVENTMASK message

Sets the event mask for a rich edit control. The event mask specifies which notification codes the control sends to its parent window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

New event mask for the rich edit control. For a list of event masks, see [**Rich Edit Control Event Mask Flags**](rich-edit-control-event-mask-flags.md).

</dd> </dl>

## Return value

This message returns the previous event mask.

## Remarks

The default event mask (before any is set) is ENM\_NONE.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_GETEVENTMASK**](em-geteventmask.md)
</dt> <dt>

[**Rich Edit Control Event Mask Flags**](rich-edit-control-event-mask-flags.md)
</dt> </dl>

 

 





