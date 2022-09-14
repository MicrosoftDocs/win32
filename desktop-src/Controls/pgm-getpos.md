---
title: PGM_GETPOS message (Commctrl.h)
description: Retrieves the current scroll position of the pager control. You can send this message explicitly or use the Pager\_GetPos macro.
ms.assetid: 1e0f967a-3290-43b7-b812-8cf56abf2d32
keywords:
- PGM_GETPOS message Windows Controls
topic_type:
- apiref
api_name:
- PGM_GETPOS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PGM\_GETPOS message

Retrieves the current scroll position of the pager control. You can send this message explicitly or use the [**Pager\_GetPos**](/windows/desktop/api/Commctrl/nf-commctrl-pager_getpos) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns an INT value that contains the current scroll position, in pixels.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





