---
title: TVM\_HITTEST message
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TVM\_HITTEST message

Determines the location of the specified point relative to the client area of a tree-view control. You can send this message explicitly or by using the [**TreeView\_HitTest**](/windows/win32/Commctrl/nf-commctrl-treeview_hittest?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TVHITTESTINFO**](/windows/win32/Commctrl/ns-commctrl-tagtvhittestinfo?branch=master) structure. When the message is sent, the **pt** member specifies the coordinates of the point to test. When the message returns, the **hItem** member is the handle to the item at the specified point or **NULL** if no item occupies the point. Also, when the message returns, the **flags** member is a hit test value that indicates the location of the specified point. For a list of hit test values, see the description of the **TVHITTESTINFO** structure.

</dd> </dl>

## Return value

Returns the handle to the tree-view item that occupies the specified point, or **NULL** if no item occupies the point.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





