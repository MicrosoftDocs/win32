---
title: LVM_GETCOUNTPERPAGE message (Commctrl.h)
description: Calculates the number of items that can fit vertically in the visible area of a list-view control when in list or report view. Only fully visible items are counted. You can send this message explicitly or by using the ListView\_GetCountPerPage macro.
ms.assetid: 2ffd2bb1-cddf-4a4a-a4a8-087c9dc3fec0
keywords:
- LVM_GETCOUNTPERPAGE message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETCOUNTPERPAGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETCOUNTPERPAGE message

Calculates the number of items that can fit vertically in the visible area of a list-view control when in list or report view. Only fully visible items are counted. You can send this message explicitly or by using the [**ListView\_GetCountPerPage**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getcountperpage) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the number of fully visible items if successful. If the current view is icon or small icon view, the return value is the total number of items in the list-view control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





