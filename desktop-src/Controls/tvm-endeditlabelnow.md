---
title: TVM_ENDEDITLABELNOW message (Commctrl.h)
description: Ends the editing of a tree-view item's label. You can send this message explicitly or by using the TreeView\_EndEditLabelNow macro.
ms.assetid: 68de2020-9311-4958-859a-de55f5e41fcf
keywords:
- TVM_ENDEDITLABELNOW message Windows Controls
topic_type:
- apiref
api_name:
- TVM_ENDEDITLABELNOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_ENDEDITLABELNOW message

Ends the editing of a tree-view item's label. You can send this message explicitly or by using the [**TreeView\_EndEditLabelNow**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_endeditlabelnow) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Variable that indicates whether the editing is canceled without being saved to the label. If this parameter is **TRUE**, the system cancels editing without saving the changes. Otherwise, the system saves the changes to the label.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

This message causes the [TVN\_ENDLABELEDIT](tvn-endlabeledit.md) notification code to be sent to the parent window of the tree-view control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





