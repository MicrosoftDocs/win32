---
title: BCN_HOTITEMCHANGE notification code (Commctrl.h)
description: Notifies the button control owner that the mouse is entering or leaving the client area of the button control. The button control sends this notification code in the form of a WM\_NOTIFY message.
ms.assetid: 92882e21-b69d-4326-94e9-ae69a0d00a83
keywords:
- BCN_HOTITEMCHANGE notification code Windows Controls
topic_type:
- apiref
api_name:
- BCN_HOTITEMCHANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BCN\_HOTITEMCHANGE notification code

Notifies the button control owner that the mouse is entering or leaving the client area of the button control. The button control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
BCN_HOTITEMCHANGE

    pnmbchotitem = (NMBCHOTITEM*) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**NMBCHOTITEM**](/windows/win32/api/commctrl/ns-commctrl-nmbchotitem) structure.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

> [!Note]  
> To use this notification code, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





