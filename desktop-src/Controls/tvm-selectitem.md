---
title: TVM_SELECTITEM message (Commctrl.h)
description: Selects the specified tree-view item, scrolls the item into view, or redraws the item in the style used to indicate the target of a drag-and-drop operation.
ms.assetid: 8b943958-7b93-4e54-99de-200121cf0752
keywords:
- TVM_SELECTITEM message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SELECTITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SELECTITEM message

Selects the specified tree-view item, scrolls the item into view, or redraws the item in the style used to indicate the target of a drag-and-drop operation. You can send this message explicitly or by using the [**TreeView\_Select**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_select), [**TreeView\_SelectItem**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_selectitem), or [**TreeView\_SelectDropTarget**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_selectdroptarget) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Action flag. This parameter can be one of the following values:




| Value | Meaning | 
|-------|---------|
| <span id="TVGN_CARET"></span><span id="tvgn_caret"></span><dl><dt><strong>TVGN_CARET</strong></dt></dl> | Sets the selection to the specified item. The tree-view control's parent window receives the <a href="tvn-selchanging.md">TVN_SELCHANGING</a> and <a href="tvn-selchanged.md">TVN_SELCHANGED</a> notification codes. <br /> | 
| <span id="TVGN_DROPHILITE"></span><span id="tvgn_drophilite"></span><dl><dt><strong>TVGN_DROPHILITE</strong></dt></dl> | Redraws the specified item in the style used to indicate the target of a drag-and-drop operation.<br /> | 
| <span id="TVGN_FIRSTVISIBLE"></span><span id="tvgn_firstvisible"></span><dl><dt><strong>TVGN_FIRSTVISIBLE</strong></dt></dl> | Ensures that the specified item is visible, and, if possible, displays it at the top of the control's window. Tree-view controls display as many items as will fit in the window. If the specified item is near the bottom of the control's hierarchy of items, it might not become the first visible item, depending on how many items fit in the window.<br /> | 
| <span id="TVSI_NOSINGLEEXPAND"></span><span id="tvsi_nosingleexpand"></span><dl><dt><strong>TVSI_NOSINGLEEXPAND</strong></dt></dl> | When a single item is selected, ensures that the treeview does not expand the children of that item. This is valid only if used with the TVGN_CARET flag. <br /><blockquote>[!Note]<br />To use this flag, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see <a href="cookbook-overview.md">Enabling Visual Styles</a>.</blockquote><br /> | 




 

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to an item. If *lParam* is **NULL**, the control is set to have no selected item.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

If the specified item is the child of a collapsed parent item, the parent's list of child items is expanded to reveal the specified item. In this case, the control's parent window receives the [TVN\_ITEMEXPANDING](tvn-itemexpanding.md) and [TVN\_ITEMEXPANDED](tvn-itemexpanded.md) notification codes.

Using the [**TreeView\_SelectItem**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_selectitem) macro is equivalent to sending the **TVM\_SELECTITEM** message with *wParam* set to the TVGN\_CARET value. Using the [**TreeView\_SelectDropTarget**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_selectdroptarget) macro is equivalent to sending the **TVM\_SELECTITEM** message with *wParam* set to the TVGN\_DROPHILITE value. Using [**TreeView\_SelectSetFirstVisible**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_selectsetfirstvisible) is equivalent to sending the **TVM\_SELECTITEM** message with *wParam* set to the TVGN\_FIRSTVISIBLE value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





