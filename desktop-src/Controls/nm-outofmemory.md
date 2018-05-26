---
title: NM\_OUTOFMEMORY notification code
description: Notifies a controls parent window that the control could not complete an operation because there was not enough memory available. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: d7d80515-ae6c-4817-a698-d486a9d86c4a
keywords:
- NM_OUTOFMEMORY notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_OUTOFMEMORY
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

# NM\_OUTOFMEMORY notification code

Notifies a control's parent window that the control could not complete an operation because there was not enough memory available. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_OUTOFMEMORY

    lpnmh = (LPNMHDR) lParam; 
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
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





