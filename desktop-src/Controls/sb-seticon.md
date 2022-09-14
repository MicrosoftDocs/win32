---
title: SB_SETICON message (Commctrl.h)
description: Sets the icon for a part in a status bar.
ms.assetid: d8528cd1-54d2-44ba-b0d6-29111f75616a
keywords:
- SB_SETICON message Windows Controls
topic_type:
- apiref
api_name:
- SB_SETICON
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_SETICON message

Sets the icon for a part in a status bar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the part that will receive the icon. If this parameter is -1, the status bar is assumed to be a simple status bar.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the icon to be set. If this value is **NULL**, the icon is removed from the part.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

The status bar will not destroy the icon. It is the calling application's responsibility to keep track of and destroy any icons.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





