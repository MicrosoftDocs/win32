---
title: NM\_NCHITTEST notification code
description: Sent by a rebar control when the control receives a WM\_NCHITTEST message. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 0e088b14-b912-4f60-9d25-cd0a0ba264c3
keywords:
- NM_NCHITTEST notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_NCHITTEST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NM\_NCHITTEST notification code

Sent by a rebar control when the control receives a [**WM\_NCHITTEST**](https://msdn.microsoft.com/library/windows/desktop/ms645618) message. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_NCHITTEST
        
    lpnmmouse = (LPNMMOUSE) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**NMMOUSE**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmmouse) structure that contains information about the notification code. The *pt* member contains the mouse coordinates of the hit test message.

</dd> </dl>

## Return value

Unless otherwise specified, return zero to allow the control to perform default processing of the hit test message, or return one of the HT\* values documented under [**WM\_NCHITTEST**](https://msdn.microsoft.com/library/windows/desktop/ms645618) to override the default hit test processing.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





