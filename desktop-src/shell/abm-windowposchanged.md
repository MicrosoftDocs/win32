---
description: Notifies the system when an appbar's position has changed. An appbar should call this message in response to the WM\_WINDOWPOSCHANGED message.
ms.assetid: 8ca51f5f-b6cf-4f2c-98f4-69c992679320
title: ABM_WINDOWPOSCHANGED message (Shellapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ABM\_WINDOWPOSCHANGED message

Notifies the system when an appbar's position has changed. An appbar should call this message in response to the [**WM\_WINDOWPOSCHANGED**](/windows/desktop/winmsg/wm-windowposchanged) message.


```C++
SHAppBarMessage(ABM_WINDOWPOSCHANGED, pabd); 
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

This message is ignored if the **hWnd** member of the structure pointed to by *pabd* identifies an autohide appbar.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



 

