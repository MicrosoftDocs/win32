---
title: CBEN_INSERTITEM notification code (Commctrl.h)
description: Sent when a new item has been inserted in the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: caf60156-10d2-4cfb-91c4-def6ee99c471
keywords:
- CBEN_INSERTITEM notification code Windows Controls
topic_type:
- apiref
api_name:
- CBEN_INSERTITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CBEN\_INSERTITEM notification code

Sent when a new item has been inserted in the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
CBEN_INSERTITEM

    pNMInfo = (PNMCOMBOBOXEX) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMCOMBOBOXEX**](/windows/desktop/api/Commctrl/ns-commctrl-nmcomboboxexa) structure containing information about the notification code and the item that was inserted.

</dd> </dl>

## Return value

The application processing this notification code must return zero.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





