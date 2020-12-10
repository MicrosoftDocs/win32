---
title: PGM_GETBKCOLOR message (Commctrl.h)
description: Retrieves the current background color for the pager control. You can send this message explicitly or use the Pager\_GetBkColor macro.
ms.assetid: c39ad721-fe39-44e9-8305-67444acc5d65
keywords:
- PGM_GETBKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- PGM_GETBKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PGM\_GETBKCOLOR message

Retrieves the current background color for the pager control. You can send this message explicitly or use the [**Pager\_GetBkColor**](/windows/desktop/api/Commctrl/nf-commctrl-pager_getbkcolor) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a **COLORREF** value that contains the current background color.

## Remarks

By default, the pager control will use the system button face color as the background color. This is the same color that can be retrieved by calling [**GetSysColorBrush**](/windows/desktop/api/winuser/nf-winuser-getsyscolorbrush) with COLOR\_BTNFACE.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

