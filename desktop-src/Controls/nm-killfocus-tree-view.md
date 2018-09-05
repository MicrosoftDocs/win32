---
title: NM_KILLFOCUS (tree view) notification code
description: Notifies a tree-view control's parent window that the control has lost the input focus. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: f6646a39-6480-4417-9c1c-ffd2417ca7dd
keywords:
- NM_KILLFOCUS (tree view) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_KILLFOCUS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NM\_KILLFOCUS (tree view) notification code

Notifies a tree-view control's parent window that the control has lost the input focus. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_KILLFOCUS

    lpnmh = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-_nmhdr) structure that contains additional information about this notification.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





