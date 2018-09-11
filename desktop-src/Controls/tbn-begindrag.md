---
title: TBN_BEGINDRAG notification code
description: Notifies a toolbar's parent window that the user has begun dragging a button in a toolbar. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 244406e5-e13d-4c80-81fa-81b018b29ec1
keywords:
- TBN_BEGINDRAG notification code Windows Controls
topic_type:
- apiref
api_name:
- TBN_BEGINDRAG
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

# TBN\_BEGINDRAG notification code

Notifies a toolbar's parent window that the user has begun dragging a button in a toolbar. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_BEGINDRAG 

    lpnmtb = (LPNMTOOLBAR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTOOLBAR**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmtoolbara) structure. The **iItem** member contains the command identifier of the button being dragged.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





