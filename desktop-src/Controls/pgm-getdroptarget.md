---
title: PGM_GETDROPTARGET message (Commctrl.h)
description: Retrieves a pager control's IDropTarget interface pointer. You can send this message explicitly or use the Pager\_GetDropTarget macro.
ms.assetid: 6b548c30-2d32-4372-90e4-346a27dda218
keywords:
- PGM_GETDROPTARGET message Windows Controls
topic_type:
- apiref
api_name:
- PGM_GETDROPTARGET
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PGM\_GETDROPTARGET message

Retrieves a pager control's [**IDropTarget**](/windows/desktop/api/oleidl/nn-oleidl-idroptarget) interface pointer. You can send this message explicitly or use the [**Pager\_GetDropTarget**](/windows/desktop/api/Commctrl/nf-commctrl-pager_getdroptarget) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**IDropTarget**](/windows/desktop/api/oleidl/nn-oleidl-idroptarget) pointer that receives the interface pointer. It is the caller's responsibility to call [**Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on this pointer when it is no longer needed.

</dd> </dl>

## Return value

The return value for this message is not used.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

