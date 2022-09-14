---
title: NM_SETFOCUS (tree view) notification code (Commctrl.h)
description: Notifies a tree-view control's parent window that the control has received the input focus. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 4bdd6cd2-afd3-4c0b-914b-8fff55e474a9
keywords:
- NM_SETFOCUS (tree view) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_SETFOCUS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_SETFOCUS (tree view) notification code

Notifies a tree-view control's parent window that the control has received the input focus. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_SETFOCUS 

    lpnmh = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure that contains additional information about this notification.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





