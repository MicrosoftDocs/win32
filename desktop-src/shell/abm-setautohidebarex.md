---
description: Registers or unregisters an autohide appbar for a given edge of the screen. This message extends ABM\_SETAUTOHIDEBAR by enabling you to specify a particular monitor, for use in multiple monitor situations.
title: ABM_SETAUTOHIDEBAREX message (Shellapi.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: C437727C-3FF6-4598-9D81-A39FCC2EF1C4
api_name: 
 - ABM_SETAUTOHIDEBAREX
api_type: 
 - HeaderDef
api_location: 
 - Shellapi.h
topic_type: 
 - APIRef
 - kbSyntax

---

# ABM\_SETAUTOHIDEBAREX message

Registers or unregisters an autohide appbar for a given edge of the screen. This message extends [**ABM\_SETAUTOHIDEBAR**](abm-setautohidebar.md) by enabling you to specify a particular monitor, for use in multiple monitor situations.


```C++
fSuccess = (BOOL) SHAppBarMessage(ABM_SETAUTOHIDEBAR, pabd); 
```



## Parameters

<dl> <dt>

*pabd* 
</dt> <dd>

A pointer to an [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure. Set the **lParam** member is to **TRUE** to register the appbar or **FALSE** to unregister it. You must specify the **cbSize**, **hWnd**, **uEdge**, **rc**, and **lParam** members when sending this message; all other members are ignored.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** if an error occurs or if an autohide appbar is already registered for the given edge on the given monitor.

## Remarks

The system allows only one autohide appbar for each edge of each monitor. The monitor is determined by the **rc** member and the edge is determined by the **uEdge** member of the [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Shellapi.h</dt> </dl> |



## See also

<dl> <dt>

[**ABM\_GETAUTOHIDEBAR**](abm-getautohidebar.md)
</dt> <dt>

[**ABM\_GETAUTOHIDEBAREX**](abm-getautohidebarex.md)
</dt> <dt>

[**ABM\_SETAUTOHIDEBAR**](abm-setautohidebar.md)
</dt> </dl>

 

 




