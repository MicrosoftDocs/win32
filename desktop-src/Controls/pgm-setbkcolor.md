---
title: PGM_SETBKCOLOR message (Commctrl.h)
description: Sets the current background color for the pager control. You can send this message explicitly or use the Pager\_SetBkColor macro.
ms.assetid: 720a25d7-3854-4f28-b227-bafab7b1e8c9
keywords:
- PGM_SETBKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- PGM_SETBKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PGM\_SETBKCOLOR message

Sets the current background color for the pager control. You can send this message explicitly or use the [**Pager\_SetBkColor**](/windows/desktop/api/Commctrl/nf-commctrl-pager_setbkcolor) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

**COLORREF** value that contains the new background color of the pager control.

</dd> </dl>

## Return value

Returns a **COLORREF** value that contains the previous background color.

## Remarks

By default, the pager control will use the system button face color as the background color. This is the same color that can be retrieved by calling [**GetSysColorBrush**](/windows/desktop/api/winuser/nf-winuser-getsyscolorbrush) with COLOR\_BTNFACE.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

