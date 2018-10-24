---
title: TVM_GETITEMSTATE message
description: Retrieves some or all of a tree-view item's state attributes. You can send this message explicitly or by using the TreeView\_GetItemState macro.
ms.assetid: 89aaaa82-2809-4e4e-a325-5666a57c5cbb
keywords:
- TVM_GETITEMSTATE message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETITEMSTATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TVM\_GETITEMSTATE message

Retrieves some or all of a tree-view item's state attributes. You can send this message explicitly or by using the [**TreeView\_GetItemState**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getitemstate) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Handle to the item.

</dd> <dt>

*lParam* 
</dt> <dd>

Mask used to specify the states to query for. It is equivalent to the **stateMask** member of [**TVITEMEX**](/windows/desktop/api/Commctrl/ns-commctrl-tagtvitemexa).

</dd> </dl>

## Return value

Returns a **UINT** value with the appropriate state bits set to **TRUE**. Only those bits that are specified by *lParam* and that are **TRUE** will be set. This value is equivalent to the **state** member of [**TVITEMEX**](/windows/desktop/api/Commctrl/ns-commctrl-tagtvitemexa).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





