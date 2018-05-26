---
title: RBN\_SPLITTERDRAG notification code
description: Sent by a rebar control when the user drags a splitter. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 7827c971-6a92-452f-b961-1abe6ae66d2a
keywords:
- RBN_SPLITTERDRAG notification code Windows Controls
topic_type:
- apiref
api_name:
- RBN_SPLITTERDRAG
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

# RBN\_SPLITTERDRAG notification code

Sent by a rebar control when the user drags a splitter. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
RBN_SPLITTERDRAG

    lpnmrbspltr = (LPNMREBARSPLITTER) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMREBARSPLITTER**](/windows/win32/Commctrl/ns-commctrl-tagnmrebarsplitter?branch=master) structure that contains information about the notification code.

</dd> </dl>

## Return value

The return value for this notification is not used.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





