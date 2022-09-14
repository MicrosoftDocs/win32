---
title: LVM_GETITEM message (Commctrl.h)
description: Retrieves some or all of a list-view item's attributes. You can send this message explicitly or by using the ListView\_GetItem macro.
ms.assetid: 684ad96a-2c3b-4148-b66c-41f8322500bb
keywords:
- LVM_GETITEM message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETITEM
- LVM_GETITEMA
- LVM_GETITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETITEM message

Retrieves some or all of a list-view item's attributes. You can send this message explicitly or by using the [**ListView\_GetItem**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure that specifies the information to retrieve and receives information about the list-view item.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

When the **LVM\_GETITEM** message is sent, the **iItem** and **iSubItem** members identify the item or subitem to retrieve information about and the **mask** member specifies which attributes to retrieve. For a list of possible values, see the description of the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure.

If the LVIF\_TEXT flag is set in the **mask** member of the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure, the **pszText** member must point to a valid buffer and the **cchTextMax** member must be set to the number of characters in that buffer. Applications should not assume that the text will necessarily be placed in the specified buffer. The control may instead change the **pszText** member of the structure to point to the new text, rather than place it in the buffer.

If the **mask** member specifies the LVIF\_STATE value, the **stateMask** member must specify the item state bits to retrieve. On output, the **state** member contains the values of the specified state bits.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVM\_GETITEMW** (Unicode) and **LVM\_GETITEMA** (ANSI)<br/>                   |



 

 





