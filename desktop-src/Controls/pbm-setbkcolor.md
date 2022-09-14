---
title: PBM_SETBKCOLOR message (Commctrl.h)
description: Sets the background color in the progress bar.
ms.assetid: e28af958-babb-4c2e-9202-89b608c22f8e
keywords:
- PBM_SETBKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- PBM_SETBKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PBM\_SETBKCOLOR message

Sets the background color in the progress bar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

**COLORREF** value that specifies the new background color. Specify the CLR\_DEFAULT value to cause the progress bar to use its default background color.

</dd> </dl>

## Return value

Returns the previous background color, or CLR\_DEFAULT if the background color is the default color.

## Remarks

When visual styles are enabled, this message has no effect.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





