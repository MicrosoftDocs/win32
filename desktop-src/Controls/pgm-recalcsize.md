---
title: PGM_RECALCSIZE message (Commctrl.h)
description: Forces the pager control to recalculate the size of the contained window. Sending this message will result in a PGN\_CALCSIZE notification being sent. You can send this message explicitly or use the Pager\_RecalcSize macro.
ms.assetid: 51b75ce8-2b41-4f1a-830e-b25e7d77dccb
keywords:
- PGM_RECALCSIZE message Windows Controls
topic_type:
- apiref
api_name:
- PGM_RECALCSIZE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PGM\_RECALCSIZE message

Forces the pager control to recalculate the size of the contained window. Sending this message will result in a [PGN\_CALCSIZE](pgn-calcsize.md) notification being sent. You can send this message explicitly or use the [**Pager\_RecalcSize**](/windows/desktop/api/Commctrl/nf-commctrl-pager_recalcsize) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

The return value is not used.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





