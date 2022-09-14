---
title: LVM_SETBKCOLOR message (Commctrl.h)
description: Sets the background color of a list-view control. You can send this message explicitly or by using the ListView\_SetBkColor macro.
ms.assetid: d579249d-421d-4e7e-8992-4c7fd7277593
keywords:
- LVM_SETBKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETBKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETBKCOLOR message

Sets the background color of a list-view control. You can send this message explicitly or by using the [**ListView\_SetBkColor**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setbkcolor) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Background color to set or the CLR\_NONE value for no background color. List-view controls with background colors redraw themselves significantly faster than those without background colors.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





