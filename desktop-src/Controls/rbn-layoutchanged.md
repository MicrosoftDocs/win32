---
title: RBN\_LAYOUTCHANGED notification code
description: Sent by a rebar control when the user changes the layout of the controls bands. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: e937d151-bfaa-41c0-a134-e70ff2f75d07
keywords:
- RBN_LAYOUTCHANGED notification code Windows Controls
topic_type:
- apiref
api_name:
- RBN_LAYOUTCHANGED
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

# RBN\_LAYOUTCHANGED notification code

Sent by a rebar control when the user changes the layout of the control's bands. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
RBN_LAYOUTCHANGED 

    lpnmhdr = (LPNMHDR) lParam;
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



 

 





