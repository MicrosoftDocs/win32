---
description: Notifies the system that an appbar has been activated. An appbar should call this message in response to the WM\_ACTIVATE message.
ms.assetid: 16011302-7c2d-4c34-9953-51cceb96e4b3
title: ABM_ACTIVATE message (Shellapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ABM\_ACTIVATE message

Notifies the system that an appbar has been activated. An appbar should call this message in response to the [**WM\_ACTIVATE**](/windows/desktop/inputdev/wm-activate) message.


```C++

SHAppBarMessage(ABM_ACTIVATE, pabd); 

            
```



## Parameters

<dl> <dt>

*pabd* 
</dt> <dd>

A pointer to an [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure that identifies the appbar to activate. You must specify the **cbSize** and **hWnd** members when sending this message; all other members are ignored.

</dd> </dl>

## Return value

Always returns **TRUE**.

## Remarks

This message is ignored if the **hWnd** member of the structure pointed to by *pabd* identifies an autohide appbar. The system automatically sets the z-order for autohide appbars.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



 

