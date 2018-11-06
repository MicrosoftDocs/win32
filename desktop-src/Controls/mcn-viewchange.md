---
title: MCN_VIEWCHANGE notification code
description: Sent by a month calendar control when the current view changes. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: ee35ac1d-9aeb-4d75-9cef-016487f23602
keywords:
- MCN_VIEWCHANGE notification code Windows Controls
topic_type:
- apiref
api_name:
- MCN_VIEWCHANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# MCN\_VIEWCHANGE notification code

Sent by a month calendar control when the current view changes. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
MCN_VIEWCHANGE

    lpNMViewChange = (LPNMVIEWCHANGE) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMVIEWCHANGE**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmviewchange) structure that contains information about the current view.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





