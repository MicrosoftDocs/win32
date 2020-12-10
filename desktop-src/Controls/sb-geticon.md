---
title: SB_GETICON message (Commctrl.h)
description: Retrieves the icon for a part in a status bar.
ms.assetid: f99508e3-afa8-48fd-b87a-fce41c4410ff
keywords:
- SB_GETICON message Windows Controls
topic_type:
- apiref
api_name:
- SB_GETICON
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_GETICON message

Retrieves the icon for a part in a status bar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the part that contains the icon to be retrieved. If this parameter is -1, the status bar is assumed to be a [Simple Mode](status-bars.md) status bar.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to the icon if successful, or **NULL** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





