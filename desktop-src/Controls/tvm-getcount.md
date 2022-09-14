---
title: TVM_GETCOUNT message (Commctrl.h)
description: Retrieves a count of the items in a tree-view control. You can send this message explicitly or by using the TreeView\_GetCount macro.
ms.assetid: cb8477be-51c9-4e96-8fa6-f978e0c1595f
keywords:
- TVM_GETCOUNT message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETCOUNT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_GETCOUNT message

Retrieves a count of the items in a tree-view control. You can send this message explicitly or by using the [**TreeView\_GetCount**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getcount) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the count of items.

## Remarks

The node count returned by [**TreeView\_GetCount**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getcount) is limited to integer values. If you add a node beyond 32767 the macro returns a negative value. After adding 65536 nodes the count returns to zero. When this occurs, the tree-view control appears empty with no scrollbars.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





