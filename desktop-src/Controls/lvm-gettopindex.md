---
title: LVM_GETTOPINDEX message (Commctrl.h)
description: Retrieves the index of the topmost visible item when in list or report view. You can send this message explicitly or by using the ListView\_GetTopIndex macro.
ms.assetid: 'vs|controls|~\controls\listview\messages\lvm_gettopindex.htm'
keywords:
- LVM_GETTOPINDEX message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETTOPINDEX
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETTOPINDEX message

Retrieves the index of the topmost visible item when in list or report view. You can send this message explicitly or by using the [**ListView\_GetTopIndex**](/windows/desktop/api/Commctrl/nf-commctrl-listview_gettopindex) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the index of the item if successful. Returns zero if the list-view control is in icon or small icon view, or if the list-view control is in details view with groups enabled.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





