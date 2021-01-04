---
title: PGM_SETCHILD message (Commctrl.h)
description: Sets the contained window for the pager control.
ms.assetid: 717e6720-aa42-4ecd-9520-4618a04dc28d
keywords:
- PGM_SETCHILD message Windows Controls
topic_type:
- apiref
api_name:
- PGM_SETCHILD
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PGM\_SETCHILD message

Sets the contained window for the pager control. This message will not change the parent of the contained window; it only assigns a window handle to the pager control for scrolling. In most cases, the contained window will be a child window. If this is the case, the contained window should be a child of the pager control. You can send this message explicitly or use the [**Pager\_SetChild**](/windows/desktop/api/Commctrl/nf-commctrl-pager_setchild) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the window to be contained.

</dd> </dl>

## Return value

The return value is not used.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





