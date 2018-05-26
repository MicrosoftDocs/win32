---
title: RBN\_BEGINDRAG notification code
description: Sent by a rebar control when the user begins dragging a band. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: e1565b31-7694-43cc-87ee-c9294a0612cd
keywords:
- RBN_BEGINDRAG notification code Windows Controls
topic_type:
- apiref
api_name:
- RBN_BEGINDRAG
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

# RBN\_BEGINDRAG notification code

Sent by a rebar control when the user begins dragging a band. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
RBN_BEGINDRAG

    lpnmrb = (LPNMREBAR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMREBAR**](/windows/win32/Commctrl/ns-commctrl-tagnmrebar?branch=master) structure that contains information about the notification code.

</dd> </dl>

## Return value

Return zero to allow the rebar to continue the drag operation, or nonzero to abort the drag operation.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





