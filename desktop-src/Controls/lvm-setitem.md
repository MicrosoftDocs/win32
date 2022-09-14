---
title: LVM_SETITEM message (Commctrl.h)
description: Sets some or all of a list-view item's attributes. You can also send LVM\_SETITEM to set the text of a subitem. You can send this message explicitly or by using the ListView\_SetItem macro.
ms.assetid: f1189b5d-bce7-4569-b4b9-bd750d7ef505
keywords:
- LVM_SETITEM message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETITEM
- LVM_SETITEMA
- LVM_SETITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETITEM message

Sets some or all of a list-view item's attributes. You can also send LVM\_SETITEM to set the text of a subitem. You can send this message explicitly or by using the [**ListView\_SetItem**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure that contains the new item attributes. The **iItem** and **iSubItem** members identify the item or subitem, and the **mask** member specifies which attributes to set. If the **mask** member specifies the LVIF\_TEXT value, the **pszText** member is the address of a null-terminated string and the **cchTextMax** member is ignored. If the **mask** member specifies the LVIF\_STATE value, the **stateMask** member specifies which item states to change and the **state** member contains the values for those states.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

To set the attributes of a list-view item, set the **iItem** member of the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure to the index of the item, and set the **iSubItem** member to zero. For an item, you can set the **state**, **pszText**, **iImage**, and **lParam** members of the **LVITEM** structure.

To set the text of a subitem, set the **iItem** and **iSubItem** members to indicate the specific subitem, and use the **pszText** member to specify the text. Alternatively, you can use the [**ListView\_SetItemText**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setitemtext) macro to set the text of a subitem. You cannot set the **state** or **lParam** members for subitems because subitems do not have these attributes. In version 4.70 and later, you can set the **iImage** member for subitems. The subitem image will be displayed if the list-view control has the [**LVS\_EX\_SUBITEMIMAGES**](extended-list-view-styles.md) extended style. Previous versions will ignore the subitem image.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVM\_SETITEMW** (Unicode) and **LVM\_SETITEMA** (ANSI)<br/>                   |



 

 





