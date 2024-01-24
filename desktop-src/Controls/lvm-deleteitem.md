---
title: LVM_DELETEITEM message (Commctrl.h)
description: Removes an item from a list-view control. You can send this message explicitly or by using the ListView\_DeleteItem macro.
ms.assetid: 0eddd4c1-7786-4a8c-a16d-9fd83cce98b3
keywords:
- LVM_DELETEITEM message Windows Controls
topic_type:
- apiref
api_name:
- LVM_DELETEITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_DELETEITEM message

Removes an item from a list-view control. You can send this message explicitly or by using the [**ListView\_DeleteItem**](/windows/desktop/api/Commctrl/nf-commctrl-listview_deleteitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The index of the list-view item to delete.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





