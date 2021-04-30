---
title: LVM_GETTOOLTIPS message (Commctrl.h)
description: Retrieves the tooltip control that the list-view control uses to display tooltips. You can send this message explicitly or use the ListView\_GetToolTips macro.
ms.assetid: a3522c64-9498-40b8-9062-c112b7c8cacc
keywords:
- LVM_GETTOOLTIPS message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETTOOLTIPS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETTOOLTIPS message

Retrieves the tooltip control that the list-view control uses to display tooltips. You can send this message explicitly or use the [**ListView\_GetToolTips**](/windows/desktop/api/Commctrl/nf-commctrl-listview_gettooltips) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle of the tooltip control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**LVM\_SETTOOLTIPS**](lvm-settooltips.md)
</dt> </dl>

 

 





