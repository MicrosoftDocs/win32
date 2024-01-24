---
title: SB_SIMPLE message (Commctrl.h)
description: Specifies whether a status window displays simple text or displays all window parts set by a previous SB\_SETPARTS message.
ms.assetid: 457209cb-67d4-4a9f-8d18-75aa5eb9ca1d
keywords:
- SB_SIMPLE message Windows Controls
topic_type:
- apiref
api_name:
- SB_SIMPLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_SIMPLE message

Specifies whether a status window displays simple text or displays all window parts set by a previous [**SB\_SETPARTS**](sb-setparts.md) message.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Display type flag. If this parameter is **TRUE**, the window displays simple text. If it is **FALSE**, it displays multiple parts.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

The return value is not used.

## Remarks

If the status window is being changed from nonsimple to simple, or vice versa, the window is immediately redrawn.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





