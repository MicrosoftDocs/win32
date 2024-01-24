---
title: TVM_INSERTITEM message (Commctrl.h)
description: Inserts a new item in a tree-view control. You can send this message explicitly or by using the TreeView\_InsertItem macro.
ms.assetid: c5e5f88f-6ec8-4b95-89ea-97f6f1fd735e
keywords:
- TVM_INSERTITEM message Windows Controls
topic_type:
- apiref
api_name:
- TVM_INSERTITEM
- TVM_INSERTITEMA
- TVM_INSERTITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_INSERTITEM message

Inserts a new item in a tree-view control. You can send this message explicitly or by using the [**TreeView\_InsertItem**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_insertitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TVINSERTSTRUCT**](/windows/win32/api/commctrl/ns-commctrl-tvinsertstructa) structure that specifies the attributes of the tree-view item.

</dd> </dl>

## Return value

Returns the **HTREEITEM** handle to the new item if successful, or **NULL** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVM\_INSERTITEMW** (Unicode) and **TVM\_INSERTITEMA** (ANSI)<br/>             |



## See also

<dl> <dt>

[TVN\_ENDLABELEDIT](tvn-endlabeledit.md)
</dt> </dl>

 

 





