---
title: LVM_SETTEXTBKCOLOR message (Commctrl.h)
description: Sets the background color of text in a list-view control. You can send this message explicitly or by using the ListView\_SetTextBkColor macro.
ms.assetid: e51d6914-0e98-47f8-b2d8-4c2404b98242
keywords:
- LVM_SETTEXTBKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETTEXTBKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETTEXTBKCOLOR message

Sets the background color of text in a list-view control. You can send this message explicitly or by using the [**ListView\_SetTextBkColor**](/windows/desktop/api/Commctrl/nf-commctrl-listview_settextbkcolor) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

New text background color. This can be CLR\_NONE for no background color.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





