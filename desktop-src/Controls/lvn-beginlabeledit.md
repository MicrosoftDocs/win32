---
title: LVN_BEGINLABELEDIT notification code (Commctrl.h)
description: Notifies a list-view control's parent window about the start of label editing for an item. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: c13a9e95-22a9-476e-aeee-4928b8b096b0
keywords:
- LVN_BEGINLABELEDIT notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_BEGINLABELEDIT
- LVN_BEGINLABELEDITA
- LVN_BEGINLABELEDITW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_BEGINLABELEDIT notification code

Notifies a list-view control's parent window about the start of label editing for an item. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_BEGINLABELEDIT

    pdi = (LPNMLVDISPINFO) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLVDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmlvdispinfoa) structure. The **item** member of this structure is an [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure whose **iItem** member identifies the item being edited. Note that subitems cannot be edited; the **iSubItem** member is always set to zero.

</dd> </dl>

## Return value

To allow the user to edit the label, return **FALSE**.

To prevent the user from editing the label, return **TRUE**.

## Remarks

When label editing begins, an edit control is created, positioned, and initialized. Before it is displayed, the list-view control sends its parent window an LVN\_BEGINLABELEDIT notification code.

To customize label editing, implement a handler for LVN\_BEGINLABELEDIT and have it send an [**LVM\_GETEDITCONTROL**](lvm-geteditcontrol.md) message to the list-view control. If a label is being edited, the return value will be a handle to the edit control. Use this handle to customize the edit control by sending the usual **EM\_XXX** messages.

When the user cancels or completes the editing, the parent window receives an [LVN\_ENDLABELEDIT](lvn-endlabeledit.md) notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVN\_BEGINLABELEDITW** (Unicode) and **LVN\_BEGINLABELEDITA** (ANSI)<br/>     |



 

 





