---
title: LVM_GETHOTITEM message (Commctrl.h)
description: Retrieves the index of the hot item. You can send this message explicitly or use the ListView\_GetHotItem macro.
ms.assetid: f80189da-6c8b-4faf-925a-0c33fedf8c4e
keywords:
- LVM_GETHOTITEM message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETHOTITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETHOTITEM message

Retrieves the index of the hot item. You can send this message explicitly or use the [**ListView\_GetHotItem**](/windows/desktop/api/Commctrl/nf-commctrl-listview_gethotitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the index of the item that is hot.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





