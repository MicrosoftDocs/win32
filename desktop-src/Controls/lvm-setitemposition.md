---
title: LVM_SETITEMPOSITION message (Commctrl.h)
description: Moves an item to a specified position in a list-view control (must be in icon or small icon view). You can send this message explicitly or by using the ListView\_SetItemPosition macro.
ms.assetid: dfb35af4-e6c3-40fc-9d7c-cf0d68a3ea01
keywords:
- LVM_SETITEMPOSITION message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETITEMPOSITION
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETITEMPOSITION message

Moves an item to a specified position in a list-view control (must be in icon or small icon view). You can send this message explicitly or by using the [**ListView\_SetItemPosition**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setitemposition) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the list-view item.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the new x-position of the item's upper-left corner, in view coordinates. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the new y-position of the item's upper-left corner, in view coordinates.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

If the list-view control has the [**LVS\_AUTOARRANGE**](list-view-window-styles.md) style, the items in the list-view control are arranged after the position of the item is set.

On Windows Vista, sending this message to a list-view control with the [**LVS\_AUTOARRANGE**](list-view-window-styles.md) style does nothing, and the return value is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

