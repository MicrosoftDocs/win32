---
title: PGN_CALCSIZE notification code (Commctrl.h)
description: Sent by a pager control to obtain the scrollable dimensions of the contained window.
ms.assetid: a15f4191-2f26-4139-bdaf-bab219449b78
keywords:
- PGN_CALCSIZE notification code Windows Controls
topic_type:
- apiref
api_name:
- PGN_CALCSIZE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PGN\_CALCSIZE notification code

Sent by a pager control to obtain the scrollable dimensions of the contained window. These dimensions are used by the pager control to determine the scrollable size of the contained window. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
PGN_CALCSIZE

    lpnmcs = (LPNMPGCALCSIZE) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMPGCALCSIZE**](/windows/desktop/api/Commctrl/ns-commctrl-nmpgcalcsize) structure that contains and receives information about the notification code. The **dwFlag** member of this structure indicates which dimension is being calculated. Depending on the value of **dwFlag**, you should place the desired dimension in the **iWidth** or **iHeight** member of this structure.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





