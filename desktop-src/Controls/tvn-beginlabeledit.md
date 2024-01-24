---
title: TVN_BEGINLABELEDIT notification code (Commctrl.h)
description: Notifies a tree-view control's parent window about the start of label editing for an item. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 67ed1f1f-7ccc-4e84-9540-4a46f6cd3a44
keywords:
- TVN_BEGINLABELEDIT notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_BEGINLABELEDIT
- TVN_BEGINLABELEDITA
- TVN_BEGINLABELEDITW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_BEGINLABELEDIT notification code

Notifies a tree-view control's parent window about the start of label editing for an item. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_BEGINLABELEDIT 

    ptvdi = (LPNMTVDISPINFO) lParam 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTVDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmtvdispinfoa) structure. The **item** member is a [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure that contains valid information about the item being edited in the **hItem**, **state**, **lParam**, and **pszText** members.

</dd> </dl>

## Return value

Returns **TRUE** to cancel label editing.

## Remarks

When label editing begins, an edit control is created but not positioned or displayed. Before it is displayed, the tree-view control sends its parent window a TVN\_BEGINLABELEDIT notification code.

To customize label editing, implement a handler for TVN\_BEGINLABELEDIT and have it send a [**TVM\_GETEDITCONTROL**](tvm-geteditcontrol.md) message to the tree-view control. If a label is being edited, the return value will be a handle to the edit control. Use this handle to customize the edit control by sending the usual EM\_XXX messages.

When the user cancels or completes the editing, the parent window receives a [TVN\_ENDLABELEDIT](tvn-endlabeledit.md) notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_BEGINLABELEDITW** (Unicode) and **TVN\_BEGINLABELEDITA** (ANSI)<br/>     |



 

 





