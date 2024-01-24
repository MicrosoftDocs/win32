---
title: NM_RDBLCLK (tree view) notification code (Commctrl.h)
description: Notifies the parent of a tree-view control that the user has double-clicked the right mouse button within the control. This notification is sent in the form of a WM\_NOTIFY message.
ms.assetid: eb1ae167-32cb-45d6-92e6-7bf5f7e46c2a
keywords:
- NM_RDBLCLK (tree view) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_RDBLCLK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_RDBLCLK (tree view) notification code

Notifies the parent of a tree-view control that the user has double-clicked the right mouse button within the control. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_RDBLCLK

    lpnmh = (LPNMHDR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure that contains additional information about this notification.

</dd> </dl>

## Return value

Return nonzero to prevent the default processing, or zero to allow the default processing.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





