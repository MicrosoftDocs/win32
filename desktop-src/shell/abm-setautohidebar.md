---
Description: Registers or unregisters an autohide appbar for a given edge of the screen. If the system has multiple monitors, the monitor that contains the primary taskbar is used.
title: ABM_SETAUTOHIDEBAR message
ms.topic: article
ms.date: 05/31/2018
---

# ABM\_SETAUTOHIDEBAR message

Registers or unregisters an autohide appbar for a given edge of the screen. If the system has multiple monitors, the monitor that contains the primary taskbar is used.

> [!Note]  
> To register or unregister an autohide appbar on a specific monitor, use [**ABM\_SETAUTOHIDEBAREX**](abm-setautohidebarex.md).

 


```C++
fSuccess = (BOOL) SHAppBarMessage(ABM_SETAUTOHIDEBAR, pabd); 
```



## Parameters

<dl> <dt>

*pabd* 
</dt> <dd>

A pointer to an [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-_appbardata) structure. Set the **lParam** member to **TRUE** to register the appbar or **FALSE** to unregister it. You must specify the **cbSize**, **hWnd**, **uEdge**, and **lParam** members when sending this message; all other members are ignored.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** if an error occurs or if an autohide appbar is already registered for the given edge.

## Remarks

The system allows only one autohide appbar for each edge of the screen. This is determined when the member **uEdge** of the [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-_appbardata) structure is set.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



## See also

<dl> <dt>

[**ABM\_SETAUTOHIDEBAR**](abm-getautohidebar.md)
</dt> <dt>

[**ABM\_GETAUTOHIDEBAREX**](abm-getautohidebarex.md)
</dt> <dt>

[**ABM\_SETAUTOHIDEBAREX**](abm-setautohidebarex.md)
</dt> </dl>

 

 




