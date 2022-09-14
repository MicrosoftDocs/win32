---
title: TVM_DELETEITEM message (Commctrl.h)
description: Removes an item and all its children from a tree-view control. You can send this message explicitly or by using the TreeView\_DeleteItem macro.
ms.assetid: 225420a5-6ded-4786-a080-2817aa5f66c9
keywords:
- TVM_DELETEITEM message Windows Controls
topic_type:
- apiref
api_name:
- TVM_DELETEITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_DELETEITEM message

Removes an item and all its children from a tree-view control. You can send this message explicitly or by using the [**TreeView\_DeleteItem**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_deleteitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

**HTREEITEM** handle to the item to delete. If *lParam* is set to TVI\_ROOT or to **NULL**, all items are deleted. You can also use the [**TreeView\_DeleteAllItems**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_deleteallitems) macro to delete all items.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

It is not safe to delete items in response to a notification such as [TVN\_SELCHANGING](tvn-selchanging.md).

Once an item is deleted, its handle is invalid and cannot be used.

The parent window receives a [TVN\_DELETEITEM](tvn-deleteitem.md) notification code when each item is removed.

If the item label is being edited, the edit operation is canceled and the parent window receives the [TVN\_ENDLABELEDIT](tvn-endlabeledit.md) notification code.

If you delete all items in a tree-view control that has the [**TVS\_NOSCROLL**](tree-view-control-window-styles.md) style, items subsequently added may not display properly. For more information, see [**TreeView\_DeleteAllItems**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_deleteallitems).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





