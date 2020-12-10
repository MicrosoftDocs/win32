---
title: TVM_ENSUREVISIBLE message (Commctrl.h)
description: Ensures that a tree-view item is visible, expanding the parent item or scrolling the tree-view control, if necessary. You can send this message explicitly or by using the TreeView\_EnsureVisible macro.
ms.assetid: 7053438a-f9ca-4c4c-9da6-46b99fe1e4f8
keywords:
- TVM_ENSUREVISIBLE message Windows Controls
topic_type:
- apiref
api_name:
- TVM_ENSUREVISIBLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_ENSUREVISIBLE message

Ensures that a tree-view item is visible, expanding the parent item or scrolling the tree-view control, if necessary. You can send this message explicitly or by using the [**TreeView\_EnsureVisible**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_ensurevisible) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the item.

</dd> </dl>

## Return value

Returns nonzero if the system scrolled the items in the tree-view control and no items were expanded. Otherwise, the message returns zero.

## Remarks

If the TVM\_ENSUREVISIBLE message expands the parent item, the parent window receives the [TVN\_ITEMEXPANDING](tvn-itemexpanding.md) and [TVN\_ITEMEXPANDED](tvn-itemexpanded.md) notification codes.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





