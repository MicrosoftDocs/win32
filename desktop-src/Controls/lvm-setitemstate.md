---
title: LVM_SETITEMSTATE message (Commctrl.h)
description: Changes the state of an item in a list-view control. You can send this message explicitly or by using the ListView\_SetItemState macro.
ms.assetid: aecd14dd-cfd0-4c7c-bddc-f65022de68c9
keywords:
- LVM_SETITEMSTATE message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETITEMSTATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETITEMSTATE message

Changes the state of an item in a list-view control. You can send this message explicitly or by using the [**ListView\_SetItemState**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setitemstate) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the list-view item. If this parameter is -1, then the state change is applied to all items.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure. The **stateMask** member specifies which state bits to change, and the **state** member contains the new values for those bits. The other members are ignored.

</dd> </dl>

## Return value

If you send this message explicitly, it returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

An item's state value includes a set of bit flags that indicate the item's state. The state value can also include image list indexes that indicate the item's state image and overlay image.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





