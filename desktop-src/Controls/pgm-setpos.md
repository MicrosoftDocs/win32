---
title: PGM_SETPOS message (Commctrl.h)
description: Sets the current scroll position for the pager control. You can send this message explicitly or use the Pager\_SetPos macro.
ms.assetid: b882ea2d-9dab-4d36-9201-29522141f779
keywords:
- PGM_SETPOS message Windows Controls
topic_type:
- apiref
api_name:
- PGM_SETPOS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PGM\_SETPOS message

Sets the current scroll position for the pager control. You can send this message explicitly or use the [**Pager\_SetPos**](/windows/desktop/api/Commctrl/nf-commctrl-pager_setpos) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Value of type **int** that contains the new scroll position, in pixels.

</dd> </dl>

## Return value

The return value is not used.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





