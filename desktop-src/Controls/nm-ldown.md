---
title: NM\_LDOWN notification code
description: Notifies a controls parent window that the left mouse button has been pressed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 59546fc3-f7c5-4b2d-9fd7-2ff89d72cd9f
keywords:
- NM_LDOWN notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_LDOWN
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

# NM\_LDOWN notification code

Notifies a control's parent window that the left mouse button has been pressed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_LDOWN

   lpnmhdr = (LPNMHDR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master) structure that contains additional information about this notification.

</dd> </dl>

## Return value

The return value is ignored by the control.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





