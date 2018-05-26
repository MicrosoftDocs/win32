---
title: NM\_RCLICK (header) notification code
description: Notifies a tree-view controls parent window that the user has clicked the right mouse button within the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: b453db51-9c41-4a85-8bc0-72bec10f8646
keywords:
- NM_RCLICK (header) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_RCLICK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NM\_RCLICK (header) notification code

Notifies a tree-view control's parent window that the user has clicked the right mouse button within the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_RCLICK

    lpnmh = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master) structure that contains additional information about this notification.

</dd> </dl>

## Return value

Return nonzero to not allow the default processing, or zero to allow the default processing.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





