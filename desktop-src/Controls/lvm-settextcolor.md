---
title: LVM_SETTEXTCOLOR message (Commctrl.h)
description: Sets the text color of a list-view control. You can send this message explicitly or by using the ListView\_SetTextColor macro.
ms.assetid: ff90c18b-0cd7-4331-bcd8-61044e891d1f
keywords:
- LVM_SETTEXTCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETTEXTCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETTEXTCOLOR message

Sets the text color of a list-view control. You can send this message explicitly or by using the [**ListView\_SetTextColor**](/windows/desktop/api/Commctrl/nf-commctrl-listview_settextcolor) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

A [**COLORREF**](/windows/desktop/gdi/colorref) that specifies the new text color.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

