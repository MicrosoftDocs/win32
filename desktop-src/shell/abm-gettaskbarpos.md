---
description: Retrieves the bounding rectangle of the Windows taskbar.
ms.assetid: 8072bb2d-05e6-4baa-a7f4-1377b94fdd45
title: ABM_GETTASKBARPOS message (Shellapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ABM\_GETTASKBARPOS message

Retrieves the bounding rectangle of the Windows taskbar.


```C++
fResult = (BOOL) SHAppBarMessage(ABM_GETTASKBARPOS, pabd);
```



## Parameters

<dl> <dt>

*pabd* 
</dt> <dd>

A pointer to an [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure whose **rc** member receives the bounding rectangle, in screen coordinates, of the taskbar. You must specify the **cbSize** when sending this message; all other members are ignored.

</dd> </dl>

## Return value

Returns **TRUE** if successful; otherwise, **FALSE**.

## Remarks

Note that this applies only to the system taskbar. Other objects, particularly toolbars supplied with third-party software, also can be present. As a result, some of the screen area not covered by the Windows taskbar might not be visible to the user. To retrieve the area of the screen not covered by both the taskbar and other app bars the working area available to your application , use the [**GetMonitorInfo**](/windows/desktop/api/winuser/nf-winuser-getmonitorinfoa) function.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



 

