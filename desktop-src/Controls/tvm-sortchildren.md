---
title: TVM_SORTCHILDREN message (Commctrl.h)
description: Sorts the child items of the specified parent item in a tree-view control. You can send this message explicitly or by using the TreeView\_SortChildren macro.
ms.assetid: c18bcd5f-c083-46ee-873b-d3100b0d7b04
keywords:
- TVM_SORTCHILDREN message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SORTCHILDREN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SORTCHILDREN message

Sorts the child items of the specified parent item in a tree-view control. You can send this message explicitly or by using the [**TreeView\_SortChildren**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_sortchildren) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value that specifies whether the sorting is recursive. Set *wParam* to **TRUE** to sort all levels of child items below the parent item. Otherwise, only the parent's immediate children are sorted.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the parent item whose child items are to be sorted.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

This message alphabetizes the tree items using [**lstrcmpi**](/windows/desktop/api/winbase/nf-winbase-lstrcmpia) on the item name. You can use the [**TVM\_SORTCHILDRENCB**](tvm-sortchildrencb.md) message to customize the ordering behavior.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

