---
title: TVM_GETVISIBLECOUNT message (Commctrl.h)
description: Obtains the number of items that can be fully visible in the client window of a tree-view control. You can send this message explicitly or by using the TreeView\_GetVisibleCount macro.
ms.assetid: c3519543-3fb2-4ecf-ac01-905d0946cb1b
keywords:
- TVM_GETVISIBLECOUNT message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETVISIBLECOUNT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_GETVISIBLECOUNT message

Obtains the number of items that can be fully visible in the client window of a tree-view control. You can send this message explicitly or by using the [**TreeView\_GetVisibleCount**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getvisiblecount) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the number of items that can be fully visible in the client window of the tree-view control.

## Remarks

The number of items that can be fully visible may be greater than the number of items in the control. The control calculates this value by dividing the height of the client window by the height of an item.

Note that the return value is the number of items that can be *fully* visible. If you can see all of 20 items and part of one more item, the return value is 20.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





