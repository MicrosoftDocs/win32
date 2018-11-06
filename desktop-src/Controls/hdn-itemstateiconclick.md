---
title: HDN_ITEMSTATEICONCLICK message
description: Notifies a header control's parent window that the user clicked an item's state icon. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: a1969579-3a69-49ff-b06e-4b7450146a92
keywords:
- HDN_ITEMSTATEICONCLICK message Windows Controls
topic_type:
- apiref
api_name:
- HDN_ITEMSTATEICONCLICK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# HDN\_ITEMSTATEICONCLICK message

Notifies a header control's parent window that the user clicked an item's state icon. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_ITEMSTATEICONCLICK

   pNMHeader = (LPNMHEADER) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmheadera) structure that contains additional information about the state icon that was clicked on.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





