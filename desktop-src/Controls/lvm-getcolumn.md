---
title: LVM_GETCOLUMN message (Commctrl.h)
description: Gets the attributes of a list-view control's column. You can send this message explicitly or by using the ListView\_GetColumn macro.
ms.assetid: 59b4bbfc-6c38-4faa-8f2e-3ea5d24e55a6
keywords:
- LVM_GETCOLUMN message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETCOLUMN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETCOLUMN message

Gets the attributes of a list-view control's column. You can send this message explicitly or by using the [**ListView\_GetColumn**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getcolumn) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The index of the column.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**LVCOLUMN**](/windows/win32/api/commctrl/ns-commctrl-lvcolumna) structure that specifies the information to retrieve and receives information about the column. The **mask** member specifies which column attributes to retrieve. If the **mask** member specifies the LVCF\_TEXT value, the **pszText** member must contain the address of the buffer that receives the item text and the **cchTextMax** member must specify the size of the buffer.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





