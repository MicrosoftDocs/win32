---
title: EM_GETEVENTMASK message (Richedit.h)
description: Retrieves the event mask for a rich edit control. The event mask specifies which notification codes the control sends to its parent window.
ms.assetid: cdf99f2a-e747-4b0e-9235-2719477c3ce2
keywords:
- EM_GETEVENTMASK message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETEVENTMASK
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETEVENTMASK message

Retrieves the event mask for a rich edit control. The event mask specifies which notification codes the control sends to its parent window.

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

This message returns the event mask for the rich edit control.

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

[**EM\_SETEVENTMASK**](em-seteventmask.md)
</dt> <dt>

[**Rich Edit Control Event Mask Flags**](rich-edit-control-event-mask-flags.md)
</dt> </dl>

 

 





