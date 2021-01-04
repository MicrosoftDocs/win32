---
title: LVM_INSERTITEM message (Commctrl.h)
description: Inserts a new item in a list-view control. You can send this message explicitly or by using the ListView\_InsertItem macro.
ms.assetid: ac283e81-5b9f-4a90-acdb-fd7813c9cb84
keywords:
- LVM_INSERTITEM message Windows Controls
topic_type:
- apiref
api_name:
- LVM_INSERTITEM
- LVM_INSERTITEMA
- LVM_INSERTITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_INSERTITEM message

Inserts a new item in a list-view control. You can send this message explicitly or by using the [**ListView\_InsertItem**](/windows/desktop/api/Commctrl/nf-commctrl-listview_insertitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure that specifies the attributes of the list-view item. Use the **iItem** member to specify the zero-based index at which the new item should be inserted. If this value is greater than the number of items currently contained by the listview, the new item will be appended to the end of the list and assigned the correct index. Examine the message's return value to determine the actual index assigned to the item.

</dd> </dl>

## Return value

Returns the index of the new item if successful, or -1 otherwise.

## Remarks

You cannot use [**ListView\_InsertItem**](/windows/desktop/api/Commctrl/nf-commctrl-listview_insertitem) or **LVM\_INSERTITEM** to insert subitems. The **iSubItem** member of the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure must be zero. See [**LVM\_SETITEM**](lvm-setitem.md) for information on setting subitems.

If a list-view control has the [**LVS\_EX\_CHECKBOXES**](extended-list-view-styles.md) style set, any value placed in bits 12 through 15 of the **state** member of the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure will be ignored. When an item is added with this style set, it will always be set to the unchecked state.

If a list-view control has either the [**LVS\_SORTASCENDING**](list-view-window-styles.md) or [**LVS\_SORTDESCENDING**](list-view-window-styles.md) window style, an **LVM\_INSERTITEM** message will fail if you try to insert an item that has LPSTR\_TEXTCALLBACK as the value for its **pszText** member.

The **LVM\_INSERTITEM** message will insert the new item in the proper position in the sort order if the following conditions hold:

-   You are using one of the LVS\_SORTXXX styles.
-   You are not using the [**LVS\_OWNERDRAW**](list-view-window-styles.md) style.
-   The **pszText** member of the structure pointed to by **pitem** is not set to LPSTR\_TEXTCALLBACK.

If the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure does not contain LVIF\_GROUPID in the **mask** member, the value of the **iGroupId** member is I\_GROUPIDCALLBACK by default.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVM\_INSERTITEMW** (Unicode) and **LVM\_INSERTITEMA** (ANSI)<br/>             |



 

 





