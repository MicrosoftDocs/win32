---
title: TVM_EDITLABEL message (Commctrl.h)
description: Begins in-place editing of the specified item's text, replacing the text of the item with a single-line edit control containing the text.
ms.assetid: ae844cbf-fa43-4f91-90cc-688f44bf77a5
keywords:
- TVM_EDITLABEL message Windows Controls
topic_type:
- apiref
api_name:
- TVM_EDITLABEL
- TVM_EDITLABELA
- TVM_EDITLABELW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_EDITLABEL message

Begins in-place editing of the specified item's text, replacing the text of the item with a single-line edit control containing the text. This message implicitly selects and focuses the specified item. You can send this message explicitly or by using the [**TreeView\_EditLabel**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_editlabel) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the item to edit.

</dd> </dl>

## Return value

Returns the handle to the edit control used to edit the item text if successful, or **NULL** otherwise.

## Remarks

This message sends a [TVN\_BEGINLABELEDIT](tvn-beginlabeledit.md) notification code to the parent of the tree-view control.

When the user completes or cancels editing, the edit control is destroyed and the handle is no longer valid. You can subclass the edit control, but do not destroy it.

The control must have the focus before you send this message to the control. Focus can be set using the [**SetFocus**](/windows/desktop/api/winuser/nf-winuser-setfocus) function.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVM\_EDITLABELW** (Unicode) and **TVM\_EDITLABELA** (ANSI)<br/>               |



 

