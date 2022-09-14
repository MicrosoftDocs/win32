---
title: TVM_GETEDITCONTROL message (Commctrl.h)
description: Retrieves the handle to the edit control being used to edit a tree-view item's text. You can send this message explicitly or by using the TreeView\_GetEditControl macro.
ms.assetid: c89e57e8-e113-47a1-85e6-bb68990f9c1a
keywords:
- TVM_GETEDITCONTROL message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETEDITCONTROL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_GETEDITCONTROL message

Retrieves the handle to the edit control being used to edit a tree-view item's text. You can send this message explicitly or by using the [**TreeView\_GetEditControl**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_geteditcontrol) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to the edit control if successful, or **NULL** otherwise.

## Remarks

When label editing begins, an edit control is created, but not positioned or displayed. Before it is displayed, the tree-view control sends its parent window an [TVN\_BEGINLABELEDIT](tvn-beginlabeledit.md) notification code.

To customize label editing, implement a handler for [TVN\_BEGINLABELEDIT](tvn-beginlabeledit.md) and have it send a **TVM\_GETEDITCONTROL** message to the tree-view control. If a label is being edited, the return value will be a handle to the edit control. Use this handle to customize the edit control by sending the usual **EM\_XXX** messages.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





