---
title: RBN\_ENDDRAG notification code
description: Sent by a rebar control when the user stops dragging a band. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 24b06144-6a4c-46a4-bef1-d6592f72a2c0
keywords:
- RBN_ENDDRAG notification code Windows Controls
topic_type:
- apiref
api_name:
- RBN_ENDDRAG
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

# RBN\_ENDDRAG notification code

Sent by a rebar control when the user stops dragging a band. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
RBN_ENDDRAG

    lpnmrb = (LPNMREBAR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMREBAR**](/windows/win32/Commctrl/ns-commctrl-tagnmrebar?branch=master) structure that contains information about the notification code.

</dd> </dl>

## Return value

The return value for this notification code is not used.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





