---
title: TVM_SETHOT message (Commctrl.h)
description: Sets the hot item for a tree-view control. You can send this message explicitly or by using the TreeView\_SetHot macro.
ms.assetid: 5e7368f5-40ce-4e7b-bbe3-5fe0b17181a8
keywords:
- TVM_SETHOT message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETHOT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SETHOT message

\[Intended for internal use; not recommended for use in applications. This message may not be supported in future versions of Windows.\]

Sets the hot item for a tree-view control. You can send this message explicitly or by using the [**TreeView\_SetHot**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_sethot) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the new hot item. If this value is **NULL**, the tree-view control will be set to have no hot item.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Security Considerations

Using this message might compromise the security of your program.

## Remarks

The *hot item* is the item that the mouse is hovering over. This message makes an item look like it is the hot item even if the mouse is not hovering over it.

This message has no visible effect if the [**TVS\_TRACKSELECT**](tree-view-control-window-styles.md) style is not set.

If it succeeds, this message causes the hot item to be redrawn.

This message is ignored if *lParam* is **NULL** and the tree-view control is tracking the mouse.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TreeView\_SetHot**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_sethot)
</dt> </dl>

 

 





