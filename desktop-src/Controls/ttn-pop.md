---
title: TTN\_POP notification code
description: Notifies the owner window that a tooltip is about to be hidden. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 44a38f1a-f1df-4057-bf76-f87eb467f0d7
keywords:
- TTN_POP notification code Windows Controls
topic_type:
- apiref
api_name:
- TTN_POP
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

# TTN\_POP notification code

Notifies the owner window that a tooltip is about to be hidden. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TTN_POP

    pnmh = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master) structure.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





