---
title: TVM_EXPAND message (Commctrl.h)
description: The TVM\_EXPAND message expands or collapses the list of child items associated with the specified parent item, if any. You can send this message explicitly or by using the TreeView\_Expand macro.
ms.assetid: d6c2e5b2-ce36-4c2b-b527-91c6de56e305
keywords:
- TVM_EXPAND message Windows Controls
topic_type:
- apiref
api_name:
- TVM_EXPAND
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_EXPAND message

The **TVM\_EXPAND** message expands or collapses the list of child items associated with the specified parent item, if any. You can send this message explicitly or by using the [**TreeView\_Expand**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_expand) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Action flag. This parameter can be one or more of the following values:



| Value                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TVE_COLLAPSE"></span><span id="tve_collapse"></span><dl> <dt>**TVE\_COLLAPSE**</dt> </dl>                | Collapses the list. <br/>                                                                                                                                                                                                                                                       |
| <span id="TVE_COLLAPSERESET"></span><span id="tve_collapsereset"></span><dl> <dt>**TVE\_COLLAPSERESET**</dt> </dl> | Collapses the list and removes the child items. The [**TVIS\_EXPANDEDONCE**](tree-view-control-item-states.md) state flag is reset. This flag must be used with the TVE\_COLLAPSE flag.<br/>                                                                 |
| <span id="TVE_EXPAND"></span><span id="tve_expand"></span><dl> <dt>**TVE\_EXPAND**</dt> </dl>                      | Expands the list.<br/>                                                                                                                                                                                                                                                          |
| <span id="TVE_EXPANDPARTIAL"></span><span id="tve_expandpartial"></span><dl> <dt>**TVE\_EXPANDPARTIAL**</dt> </dl> | [Version 4.70](common-control-versions.md). Partially expands the list. In this state the child items are visible and the parent item's plus sign (+), indicating that it can be expanded, is displayed. This flag must be used in combination with the TVE\_EXPAND flag.<br/> |
| <span id="TVE_TOGGLE"></span><span id="tve_toggle"></span><dl> <dt>**TVE\_TOGGLE**</dt> </dl>                      | Collapses the list if it is expanded or expands it if it is collapsed.<br/>                                                                                                                                                                                                     |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the parent item to expand or collapse.

</dd> </dl>

## Return value

Returns nonzero if the operation was successful, or zero otherwise.

## Remarks

Expanding a node that is already expanded is considered a successful operation and [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) returns a nonzero value. Collapsing a node returns zero if the node is already collapsed; otherwise it returns nonzero. Attempting to expand or collapse a node that has no children is considered a failure and **SendMessage** returns zero.

When an item is first expanded by a **TVM\_EXPAND** message, the action generates [TVN\_ITEMEXPANDING](tvn-itemexpanding.md) and [TVN\_ITEMEXPANDED](tvn-itemexpanded.md) notification codes and the item's [**TVIS\_EXPANDEDONCE**](tree-view-control-item-states.md) state flag is set. As long as this state flag remains set, subsequent **TVM\_EXPAND** messages do not generate TVN\_ITEMEXPANDING or TVN\_ITEMEXPANDED notifications. To reset the **TVIS\_EXPANDEDONCE** state flag, you must send a **TVM\_EXPAND** message with the TVE\_COLLAPSE and TVE\_COLLAPSERESET flags set. Attempting to explicitly set **TVIS\_EXPANDEDONCE** will result in unpredictable behavior.

The expand operation may fail if the owner of the treeview control denies the operation in response to a [TVN\_ITEMEXPANDING](tvn-itemexpanding.md) notification.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

