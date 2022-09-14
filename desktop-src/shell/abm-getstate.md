---
description: Retrieves the autohide and always-on-top states of the Windows taskbar.
title: ABM_GETSTATE message (Shellapi.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 18e16752-16be-492b-a4fa-c951e18dc86c
api_name: 
 - ABM_GETSTATE
api_type: 
 - HeaderDef
api_location: 
 - Shellapi.h
topic_type: 
 - APIRef
 - kbSyntax

---

# ABM\_GETSTATE message

Retrieves the autohide and always-on-top states of the Windows taskbar.


```C++
uState = (UINT) SHAppBarMessage(ABM_GETSTATE, pabd);
```



## Parameters

<dl> <dt>

*pabd* 
</dt> <dd>

Pointer to an [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure. You must specify the **cbSize** member when sending this message; all other members are ignored.

</dd> </dl>

## Return value

Returns zero if the taskbar is neither in the autohide nor always-on-top state. Otherwise, the return value is one or both of the following:




| Return code | Description | 
|-------------|-------------|
| <dl><dt><strong>ABS_ALWAYSONTOP</strong></dt></dl> | The taskbar is in the always-on-top state. <br /><blockquote>[!Note]<br />As of Windows 7, ABS_ALWAYSONTOP is no longer returned because the taskbar is always in that state. Older code should be updated to ignore the absence of this value in not assume that return value to mean that the taskbar is not in the always-on-top state.</blockquote><br /> | 
| <dl><dt><strong>ABS_AUTOHIDE</strong></dt></dl> | The taskbar is in the autohide state.<br /> | 




 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



 

 




