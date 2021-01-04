---
title: CBEN_DELETEITEM notification code (Commctrl.h)
description: Sent when an item has been deleted. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 8b0d03ff-57fa-44dc-ab3e-05089b876e3c
keywords:
- CBEN_DELETEITEM notification code Windows Controls
topic_type:
- apiref
api_name:
- CBEN_DELETEITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CBEN\_DELETEITEM notification code

Sent when an item has been deleted. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
CBEN_DELETEITEM

    pCBEx = (PNMCOMBOBOXEX) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMCOMBOBOXEX**](/windows/desktop/api/Commctrl/ns-commctrl-nmcomboboxexa) structure that contains information about the notification code and the deleted item.

</dd> </dl>

## Return value

The application processing this notification code must return zero.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





