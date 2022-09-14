---
title: LVM_SETTOOLTIPS message (Commctrl.h)
description: Sets the tooltip control that the list-view control will use to display tooltips. You can send this message explicitly or use the ListView\_SetToolTips macro.
ms.assetid: 5b4335a4-e9f0-4b13-b00b-516af3b60bf1
keywords:
- LVM_SETTOOLTIPS message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETTOOLTIPS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETTOOLTIPS message

Sets the tooltip control that the list-view control will use to display tooltips. You can send this message explicitly or use the [**ListView\_SetToolTips**](/windows/desktop/api/Commctrl/nf-commctrl-listview_settooltips) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Handle to the tooltip control to be set.</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

Returns the handle to the previous tooltip control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**LVM\_GETTOOLTIPS**](lvm-gettooltips.md)
</dt> </dl>

 

 





