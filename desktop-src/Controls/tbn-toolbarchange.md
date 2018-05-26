---
title: TBN\_TOOLBARCHANGE notification code
description: Notifies the toolbars parent window that the user has customized a toolbar. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 6c5127e6-391f-4592-8547-4cc3d3ed6cf0
keywords:
- TBN_TOOLBARCHANGE notification code Windows Controls
topic_type:
- apiref
api_name:
- TBN_TOOLBARCHANGE
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

# TBN\_TOOLBARCHANGE notification code

Notifies the toolbar's parent window that the user has customized a toolbar. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_TOOLBARCHANGE 

    lpnmhdr = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master) structure that contains information about the notification code.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





