---
title: TVM_SHOWINFOTIP message (Commctrl.h)
description: Shows the infotip for a specified item in a tree-view control. You can send this message explicitly or by using the TreeView\_ShowInfoTip macro..
ms.assetid: ed5a1bda-5754-4bb3-aa22-8faaf1af1268
keywords:
- TVM_SHOWINFOTIP message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SHOWINFOTIP
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SHOWINFOTIP message

Shows the infotip for a specified item in a tree-view control. You can send this message explicitly or by using the [**TreeView\_ShowInfoTip**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_showinfotip) macro..

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* \[in\]
</dt> <dd>

Handle to the item.

</dd> </dl>

## Return value

Returns zero.

## Remarks

Most applications do not use this message. Infotips are shown automatically. For more information, see Using Tree-view Infotips in the [About Tree-View Controls](tree-view-controls.md) overview.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





