---
title: LVM_GETITEMPOSITION message (Commctrl.h)
description: Retrieves the position of a list-view item. You can send this message explicitly or by using the ListView\_GetItemPosition macro.
ms.assetid: e5841089-c34e-498e-b94c-45c845bfc747
keywords:
- LVM_GETITEMPOSITION message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETITEMPOSITION
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETITEMPOSITION message

Retrieves the position of a list-view item. You can send this message explicitly or by using the [**ListView\_GetItemPosition**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getitemposition) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the list-view item.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**POINT**](/windows/win32/api/windef/ns-windef-point) structure that receives the position of the item's upper-left corner, in view coordinates.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

