---
title: SB_SETPARTS message (Commctrl.h)
description: Sets the number of parts in a status window and the coordinate of the right edge of each part.
ms.assetid: e29e8b09-c018-4ea4-8b47-6f3713113427
keywords:
- SB_SETPARTS message Windows Controls
topic_type:
- apiref
api_name:
- SB_SETPARTS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_SETPARTS message

Sets the number of parts in a status window and the coordinate of the right edge of each part.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Number of parts to set (cannot be greater than 256).

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an integer array. The number of elements is specified in *wParam*. Each element specifies the position, in client coordinates, of the right edge of the corresponding part. If an element is -1, the right edge of the corresponding part extends to the border of the window.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





