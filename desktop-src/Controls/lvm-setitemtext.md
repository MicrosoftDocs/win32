---
title: LVM_SETITEMTEXT message (Commctrl.h)
description: Changes the text of a list-view item or subitem. You can send this message explicitly or by using the ListView\_SetItemText macro.
ms.assetid: 1a9c7e4d-78e0-44c7-bf4f-d0fc7a0049f3
keywords:
- LVM_SETITEMTEXT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETITEMTEXT
- LVM_SETITEMTEXTA
- LVM_SETITEMTEXTW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETITEMTEXT message

Changes the text of a list-view item or subitem. You can send this message explicitly or by using the [**ListView\_SetItemText**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setitemtext) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the list-view item.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure. The **iSubItem** member is the index of the subitem, or it can be zero to set the item label. The **pszText** member is the address of a null-terminated string containing the new text; it can also be **NULL**. The **pszText** member can also be LPSTR\_TEXTCALLBACK to indicate a callback item for which the parent window stores the text. In this case, the list-view control sends the parent an [**LVN\_GETDISPINFO**](lvn-getdispinfo.md) notification code when it needs the text.

</dd> </dl>

## Return value

If you send this message explicitly, it returns **TRUE** if successful or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVM\_SETITEMTEXTW** (Unicode) and **LVM\_SETITEMTEXTA** (ANSI)<br/>           |



 

 





