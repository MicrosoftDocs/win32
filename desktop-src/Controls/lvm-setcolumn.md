---
title: LVM\_SETCOLUMN message
description: Sets the attributes of a list-view column. You can send this message explicitly or by using the ListView\_SetColumn macro.
ms.assetid: '8ca1c269-fd86-4561-940d-b75f8ca2b731'
keywords: ["LVM_SETCOLUMN message Windows Controls"]
topic_type:
- apiref
api_name:
- LVM_SETCOLUMN
- LVM_SETCOLUMNW
- LVM_SETCOLUMNW
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# LVM\_SETCOLUMN message

Sets the attributes of a list-view column. You can send this message explicitly or by using the [**ListView\_SetColumn**](listview-setcolumn.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the column.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**LVCOLUMN**](lvcolumn.md) structure that contains the new column attributes. The **mask** member specifies which column attributes to set. If the **mask** member specifies the LVCF\_TEXT value, the **pszText** member is the address of a null-terminated string and the **cchTextMax** member is ignored.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVM\_SETCOLUMNW** (Unicode) and **LVM\_SETCOLUMNW** (ANSI)<br/>               |



 

 





