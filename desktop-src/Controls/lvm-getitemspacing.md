---
title: LVM_GETITEMSPACING message (Commctrl.h)
description: Determines the spacing between items in a list-view control. You can send this message explicitly or by using the ListView\_GetItemSpacing macro.
ms.assetid: 4e43fb43-468c-4b8a-9e3b-1694e90ffef8
keywords:
- LVM_GETITEMSPACING message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETITEMSPACING
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETITEMSPACING message

Determines the spacing between items in a list-view control. You can send this message explicitly or by using the [**ListView\_GetItemSpacing**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getitemspacing) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

View for which to retrieve the item spacing. This parameter is **TRUE** for small icon view, or **FALSE** for icon view.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the amount of spacing between items. The horizontal spacing is contained in the [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) and the vertical spacing is contained in the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

