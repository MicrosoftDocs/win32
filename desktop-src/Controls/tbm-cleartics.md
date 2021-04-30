---
title: TBM_CLEARTICS message (Commctrl.h)
description: Removes the current tick marks from a trackbar. This message does not remove the first and last tick marks, which are created automatically by the trackbar.
ms.assetid: 2830497c-2cf0-4068-810c-c05d4e0abb8b
keywords:
- TBM_CLEARTICS message Windows Controls
topic_type:
- apiref
api_name:
- TBM_CLEARTICS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_CLEARTICS message

Removes the current tick marks from a trackbar. This message does not remove the first and last tick marks, which are created automatically by the trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Redraw flag. If this parameter is **TRUE**, the trackbar is redrawn after the tick marks are cleared. If this parameter is **FALSE**, the message clears the tick marks but does not redraw the trackbar.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





