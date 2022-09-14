---
title: RBN_MINMAX notification code (Commctrl.h)
description: Sent by a rebar control prior to maximizing or minimizing a band. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 75619cb0-ef0b-44fa-83b2-15a5e5e92c60
keywords:
- RBN_MINMAX notification code Windows Controls
topic_type:
- apiref
api_name:
- RBN_MINMAX
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RBN\_MINMAX notification code

Sent by a rebar control prior to maximizing or minimizing a band. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
RBN_MINMAX
```



## Parameters

This notification code has no parameters.

## Return value

Return a nonzero value to prevent the operation from taking place, zero to allow it to continue.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





