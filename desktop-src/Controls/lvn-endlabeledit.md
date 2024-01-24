---
title: LVN_ENDLABELEDIT notification code (Commctrl.h)
description: Notifies a list-view control's parent window about the end of label editing for an item. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 03129fef-abf1-4374-b4b8-503c46ef7115
keywords:
- LVN_ENDLABELEDIT notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_ENDLABELEDIT
- LVN_ENDLABELEDITA
- LVN_ENDLABELEDITW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_ENDLABELEDIT notification code

Notifies a list-view control's parent window about the end of label editing for an item. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_ENDLABELEDIT

    pdi = (LPNMLVDISPINFO) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLVDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmlvdispinfoa) structure. The **item** member of this structure is an [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure whose **iItem** member identifies the item being edited. The **pszText** member of **item** contains a valid value when the LVN\_ENDLABELEDIT notification code is sent, regardless of whether the LVIF\_TEXT flag is set in the **mask** member of the **LVITEM** structure. If the user cancels editing or doesn't change the text and presses *Enter* key, the **pszText** member of the **LVITEM** structure is **NULL**; otherwise, **pszText** is the address of the edited text.

</dd> </dl>

## Return value

If the **pszText** member of the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure is non-**NULL**, return **TRUE** to set the item's label to the edited text. Return **FALSE** to reject the edited text and revert to the original label.

If the **pszText** member of the [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure is **NULL**, the return value is ignored.

## Remarks

The return value of the dialog procedure is whether the message was handled. The second return value must be set by calling [**SetwindowLongPtr**](/windows/win32/api/winuser/nf-winuser-setwindowlongptra) with **DWLP_MSGRESULT**.

When the user begins editing an item label, the parent window of the list-view control receives an [LVN\_BEGINLABELEDIT](lvn-beginlabeledit.md) notification code. When the user cancels or completes the editing, the parent window receives an LVN\_ENDLABELEDIT notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVN\_ENDLABELEDITW** (Unicode) and **LVN\_ENDLABELEDITA** (ANSI)<br/>         |



 

 





