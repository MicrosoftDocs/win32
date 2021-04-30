---
title: SB_GETPARTS message (Commctrl.h)
description: Retrieves a count of the parts in a status window. The message also retrieves the coordinate of the right edge of the specified number of parts.
ms.assetid: 2535f490-4d6b-468a-b13c-096941e61bf4
keywords:
- SB_GETPARTS message Windows Controls
topic_type:
- apiref
api_name:
- SB_GETPARTS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_GETPARTS message

Retrieves a count of the parts in a status window. The message also retrieves the coordinate of the right edge of the specified number of parts.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Number of parts for which to retrieve coordinates. If this parameter is greater than the number of parts in the window, the message retrieves coordinates for existing parts only.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an integer array that has the same number of elements as parts specified by *wParam*. Each element in the array receives the client coordinate of the right edge of the corresponding part. If an element is set to -1, the position of the right edge for that part extends to the right edge of the window. To retrieve the current number of parts, set this parameter to zero.

</dd> </dl>

## Return value

Returns the number of parts in the window.

## Remarks

This message always returns the number of parts in the status bar.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





