---
title: TVM_HITTEST message (Commctrl.h)
description: Determines the location of the specified point relative to the client area of a tree-view control. You can send this message explicitly or by using the TreeView\_HitTest macro.
ms.assetid: 18ea3737-f429-4c10-9133-3b5729aa36fa
keywords:
- TVM_HITTEST message Windows Controls
topic_type:
- apiref
api_name:
- TVM_HITTEST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_HITTEST message

Determines the location of the specified point relative to the client area of a tree-view control. You can send this message explicitly or by using the [**TreeView\_HitTest**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_hittest) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TVHITTESTINFO**](/windows/win32/api/commctrl/ns-commctrl-tvhittestinfo) structure. When the message is sent, the **pt** member specifies the coordinates of the point to test. When the message returns, the **hItem** member is the handle to the item at the specified point or **NULL** if no item occupies the point. Also, when the message returns, the **flags** member is a hit test value that indicates the location of the specified point. For a list of hit test values, see the description of the **TVHITTESTINFO** structure.

</dd> </dl>

## Return value

Returns the handle to the tree-view item that occupies the specified point, or **NULL** if no item occupies the point.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





