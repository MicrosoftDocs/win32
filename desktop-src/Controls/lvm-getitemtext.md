---
title: LVM_GETITEMTEXT message (Commctrl.h)
description: Retrieves the text of a list-view item or subitem. You can send this message explicitly or by using the ListView\_GetItemText macro.
ms.assetid: 5711ed18-a766-4e7f-9e9d-b9203231b369
keywords:
- LVM_GETITEMTEXT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETITEMTEXT
- LVM_GETITEMTEXTA
- LVM_GETITEMTEXTW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETITEMTEXT message

Retrieves the text of a list-view item or subitem. You can send this message explicitly or by using the [**ListView\_GetItemText**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getitemtext) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the list-view item.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure. To retrieve the item text, set **iSubItem** to zero. To retrieve the text of a subitem, set **iSubItem** to the subitem's index. The **pszText** member points to a buffer that receives the text. The **cchTextMax** member specifies the number of characters in the buffer.

</dd> </dl>

## Return value

If you send this message explicitly, it returns the number of characters in the **pszText** member of the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure.

## Remarks

You can also send this message by calling the [**ListView\_GetItemText**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getitemtext) macro. However, this macro does not return the string length.

**LVM\_GETITEMTEXT** is not supported under the [**LVS\_OWNERDATA**](list-view-window-styles.md) style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVM\_GETITEMTEXTW** (Unicode) and **LVM\_GETITEMTEXTA** (ANSI)<br/>           |



 

 





