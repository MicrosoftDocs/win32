---
title: NM\_CLICK (tab) notification code
description: Notifies the parent window of a tab control that the user has clicked the left mouse button within the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: b892aded-d6b8-4a04-bfdd-0153b65eaccc
keywords:
- NM_CLICK (tab) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_CLICK
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

# NM\_CLICK (tab) notification code

Notifies the parent window of a tab control that the user has clicked the left mouse button within the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_CLICK
        
    lpnmh = (LPNMHDR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master) structure that contains additional information about this notification.

</dd> </dl>

## Return value

The return value is ignored by the tab control.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





