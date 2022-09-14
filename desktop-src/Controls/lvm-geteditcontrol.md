---
title: LVM_GETEDITCONTROL message (Commctrl.h)
description: Gets the handle to the edit control being used to edit a list-view item's text. You can send this message explicitly or by using the ListView\_GetEditControl macro.
ms.assetid: 70450b24-9879-4be8-9bc9-f87008b66415
keywords:
- LVM_GETEDITCONTROL message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETEDITCONTROL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETEDITCONTROL message

Gets the handle to the edit control being used to edit a list-view item's text. You can send this message explicitly or by using the [**ListView\_GetEditControl**](/windows/desktop/api/Commctrl/nf-commctrl-listview_geteditcontrol) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to the edit control if successful, or **NULL** otherwise.

## Remarks

When label editing begins, an edit control is created, positioned, and initialized. Before it is displayed, the list-view control sends its parent window an [LVN\_BEGINLABELEDIT](lvn-beginlabeledit.md) notification code.

To customize label editing, implement a handler for [LVN\_BEGINLABELEDIT](lvn-beginlabeledit.md) and have it send an **LVM\_GETEDITCONTROL** message to the list-view control. If a label is being edited, the return value will be a handle to the edit control. Use this handle to customize the edit control by sending the usual **EM\_XXX** messages.

When the user completes or cancels editing, the edit control is destroyed and the handle is no longer valid. You can subclass the edit control, but you should not destroy it. To cancel editing, send the list-view control a [**WM\_CANCELMODE**](/windows/desktop/winmsg/wm-cancelmode) message.

The list-view item being edited is the currently focused item that is, the item in the focused state. To find an item based on its state, use the [**LVM\_GETNEXTITEM**](lvm-getnextitem.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**ListView\_GetEditControl**](/windows/desktop/api/Commctrl/nf-commctrl-listview_geteditcontrol)
</dt> </dl>

 

