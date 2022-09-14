---
title: LVM_UPDATE message (Commctrl.h)
description: Updates a list-view item. If the list-view control has the LVS\_AUTOARRANGE style, this macro causes the list-view control to be arranged. You can send this message explicitly or by using the ListView\_Update macro.
ms.assetid: 81b332e9-4bea-481e-a7c5-613371103550
keywords:
- LVM_UPDATE message Windows Controls
topic_type:
- apiref
api_name:
- LVM_UPDATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_UPDATE message

Updates a list-view item. If the list-view control has the [**LVS\_AUTOARRANGE**](list-view-window-styles.md) style, this macro causes the list-view control to be arranged. You can send this message explicitly or by using the [**ListView\_Update**](/windows/desktop/api/Commctrl/nf-commctrl-listview_update) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the item to update.

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



 

 





