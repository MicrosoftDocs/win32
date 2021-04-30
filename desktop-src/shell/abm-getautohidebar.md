---
description: Retrieves the handle to the autohide appbar associated with an edge of the screen. If the system has multiple monitors, the monitor that contains the primary taskbar is used.
title: ABM_GETAUTOHIDEBAR message (Shellapi.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 545dd1d9-8cbb-4ff3-b871-4908ecac56db
api_name: 
 - ABM_GETAUTOHIDEBAR
api_type: 
 - HeaderDef
api_location: 
 - Shellapi.h
topic_type: 
 - APIRef
 - kbSyntax

---

# ABM\_GETAUTOHIDEBAR message

Retrieves the handle to the autohide appbar associated with an edge of the screen. If the system has multiple monitors, the monitor that contains the primary taskbar is used.

> [!Note]  
> To query for an autohide appbar on a specific monitor, use [**ABM\_GETAUTOHIDEBAREX**](abm-getautohidebarex.md).

 


```C++
hwndAutoHide = (HWND) SHAppBarMessage(ABM_GETAUTOHIDEBAR, pabd);
```



## Parameters

<dl> <dt>

*pabd* 
</dt> <dd>

A pointer to an [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure that specifies the screen edge. You must specify the **cbSize** and **uEdge** members when sending this message; all other members are ignored.

</dd> </dl>

## Return value

Returns the handle to the autohide appbar. The return value is **NULL** if an error occurs or if no autohide appbar is associated with the given edge.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



## See also

<dl> <dt>

[**ABM\_SETAUTOHIDEBAR**](abm-setautohidebar.md)
</dt> <dt>

[**ABM\_GETAUTOHIDEBAREX**](abm-getautohidebarex.md)
</dt> <dt>

[**ABM\_SETAUTOHIDEBAREX**](abm-setautohidebarex.md)
</dt> </dl>

 

 




