---
title: LVM_EDITLABEL message (Commctrl.h)
description: Begins in-place editing of the specified list-view item's text. The message implicitly selects and focuses the specified item. You can send this message explicitly or by using the ListView\_EditLabel macro.
ms.assetid: b63f13f1-6e66-4770-af84-30bcdb241727
keywords:
- LVM_EDITLABEL message Windows Controls
topic_type:
- apiref
api_name:
- LVM_EDITLABEL
- LVM_EDITLABELA
- LVM_EDITLABELW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_EDITLABEL message

Begins in-place editing of the specified list-view item's text. The message implicitly selects and focuses the specified item. You can send this message explicitly or by using the [**ListView\_EditLabel**](/windows/desktop/api/Commctrl/nf-commctrl-listview_editlabel) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The index of the list-view item. To cancel editing, set the index to -1.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to the edit control that is used to edit the item text if successful, or **NULL** otherwise.

## Remarks

When the user completes or cancels editing, the edit control is destroyed and the handle is no longer valid. You can subclass the edit control, but you should not destroy it.

The control must have the focus before you send this message to the control. Focus can be set using the [**SetFocus**](/windows/desktop/api/winuser/nf-winuser-setfocus) function.

If *wParam* is -1, an [LVN\_ENDLABELEDIT](lvn-endlabeledit.md) notification code is sent.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVM\_EDITLABELW** (Unicode) and **LVM\_EDITLABELA** (ANSI)<br/>               |



## See also

<dl> <dt>

[**WM\_CANCELMODE**](/windows/desktop/winmsg/wm-cancelmode)
</dt> </dl>

 

