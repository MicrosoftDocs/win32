---
title: NM\_RETURN (list view) notification code
description: Notifies a list-view controls parent window that the control has the input focus and that the user has pressed the ENTER key. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 21a8d308-d747-4020-8925-d982234bcf81
keywords:
- NM_RETURN (list view) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_RETURN
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

# NM\_RETURN (list view) notification code

Notifies a list-view control's parent window that the control has the input focus and that the user has pressed the ENTER key. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_RETURN 

    lpnmh = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master) structure that contains additional information about this notification.

</dd> </dl>

## Return value

The return value for this notification is not used.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





