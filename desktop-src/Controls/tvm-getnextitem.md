---
title: TVM_GETNEXTITEM message (Commctrl.h)
description: Retrieves the tree-view item that bears the specified relationship to a specified item. You can send this message explicitly, by using the TreeView\_GetNextItem macro.
ms.assetid: 505c713c-7728-4119-bc0e-482fe7e73193
keywords:
- TVM_GETNEXTITEM message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETNEXTITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_GETNEXTITEM message

Retrieves the tree-view item that bears the specified relationship to a specified item. You can send this message explicitly, by using the [**TreeView\_GetNextItem**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getnextitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Flag specifying the item to retrieve. This parameter can be one of the following values:



| Value                                                                                                                                                                              | Meaning                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TVGN_CARET"></span><span id="tvgn_caret"></span><dl> <dt>**TVGN\_CARET**</dt> </dl>                               | Retrieves the currently selected item. You can use the [**TreeView\_GetSelection**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getselection) macro to send this message.<br/>                                                                                                                                                                          |
| <span id="TVGN_CHILD"></span><span id="tvgn_child"></span><dl> <dt>**TVGN\_CHILD**</dt> </dl>                               | Retrieves the first child item of the item specified by the *hitem* parameter. You can use the [**TreeView\_GetChild**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getchild) macro to send this message.<br/>                                                                                                                                          |
| <span id="TVGN_DROPHILITE"></span><span id="tvgn_drophilite"></span><dl> <dt>**TVGN\_DROPHILITE**</dt> </dl>                | Retrieves the item that is the target of a drag-and-drop operation. You can use the [**TreeView\_GetDropHilight**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getdrophilight) macro to send this message.<br/>                                                                                                                                         |
| <span id="TVGN_FIRSTVISIBLE"></span><span id="tvgn_firstvisible"></span><dl> <dt>**TVGN\_FIRSTVISIBLE**</dt> </dl>          | Retrieves the first item that is visible in the tree-view window. You can use the [**TreeView\_GetFirstVisible**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getfirstvisible) macro to send this message.<br/>                                                                                                                                         |
| <span id="TVGN_LASTVISIBLE"></span><span id="tvgn_lastvisible"></span><dl> <dt>**TVGN\_LASTVISIBLE**</dt> </dl>             | [Version 4.71](common-control-versions.md). Retrieves the last expanded item in the tree. This does not retrieve the last item visible in the tree-view window. You can use the [**TreeView\_GetLastVisible**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getlastvisible) macro to send this message.<br/>                                            |
| <span id="TVGN_NEXT"></span><span id="tvgn_next"></span><dl> <dt>**TVGN\_NEXT**</dt> </dl>                                  | Retrieves the next sibling item. You can use the [**TreeView\_GetNextSibling**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getnextsibling) macro to send this message.<br/>                                                                                                                                                                            |
| <span id="TVGN_NEXTSELECTED"></span><span id="tvgn_nextselected"></span><dl> <dt>**TVGN\_NEXTSELECTED**</dt> </dl>          | **Windows Vista and later.** Retrieves the next selected item. You can use the [**TreeView\_GetNextSelected**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getnextselected) macro to send this message.<br/>                                                                                                                                            |
| <span id="TVGN_NEXTVISIBLE"></span><span id="tvgn_nextvisible"></span><dl> <dt>**TVGN\_NEXTVISIBLE**</dt> </dl>             | Retrieves the next visible item that follows the specified item. The specified item must be visible. Use the [**TVM\_GETITEMRECT**](tvm-getitemrect.md) message to determine whether an item is visible. You can use the [**TreeView\_GetNextVisible**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getnextvisible) macro to send this message.<br/>   |
| <span id="TVGN_PARENT"></span><span id="tvgn_parent"></span><dl> <dt>**TVGN\_PARENT**</dt> </dl>                            | Retrieves the parent of the specified item. You can use the [**TreeView\_GetParent**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getparent) macro to send this message.<br/>                                                                                                                                                                           |
| <span id="TVGN_PREVIOUS"></span><span id="tvgn_previous"></span><dl> <dt>**TVGN\_PREVIOUS**</dt> </dl>                      | Retrieves the previous sibling item. You can use the [**TreeView\_GetPrevSibling**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getprevsibling) macro to send this message.<br/>                                                                                                                                                                        |
| <span id="TVGN_PREVIOUSVISIBLE"></span><span id="tvgn_previousvisible"></span><dl> <dt>**TVGN\_PREVIOUSVISIBLE**</dt> </dl> | Retrieves the first visible item that precedes the specified item. The specified item must be visible. Use the [**TVM\_GETITEMRECT**](tvm-getitemrect.md) message to determine whether an item is visible. You can use the [**TreeView\_GetPrevVisible**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getprevvisible) macro to send this message.<br/> |
| <span id="TVGN_ROOT"></span><span id="tvgn_root"></span><dl> <dt>**TVGN\_ROOT**</dt> </dl>                                  | Retrieves the topmost or very first item of the tree-view control. You can use the [**TreeView\_GetRoot**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getroot) macro to send this message. <br/>                                                                                                                                                       |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to an item.

</dd> </dl>

## Return value

Returns the handle to the item if successful. For most cases, the message returns a **NULL** value to indicate an error. See the Remarks section for details.

## Remarks

This message will return **NULL** if the item being retrieved is the root node of the tree. For example, if you use this message with the TVGN\_PARENT flag on a first-level child of the tree view's root node, the message will return **NULL**.

You can also use one of these related macros:



|                                                               |
|---------------------------------------------------------------|
| [**TreeView\_GetChild**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getchild)               |
| [**TreeView\_GetDropHilight**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getdrophilight)   |
| [**TreeView\_GetFirstVisible**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getfirstvisible) |
| [**TreeView\_GetLastVisible**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getlastvisible)   |
| [**TreeView\_GetNextSibling**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getnextsibling)   |
| [**TreeView\_GetNextVisible**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getnextvisible)   |
| [**TreeView\_GetParent**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getparent)             |
| [**TreeView\_GetPrevSibling**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getprevsibling)   |
| [**TreeView\_GetPrevVisible**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getprevvisible)   |
| [**TreeView\_GetRoot**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getroot)                 |
| [**TreeView\_GetSelection**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getselection)       |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





