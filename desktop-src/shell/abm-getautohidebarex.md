---
Description: Retrieves the handle to the autohide appbar associated with an edge of the screen. This message extends ABM\_GETAUTOHIDEBAR by enabling you to specify a particular monitor, for use in multiple monitor situations.
title: ABM_GETAUTOHIDEBAREX message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ABM\_GETAUTOHIDEBAREX message

Retrieves the handle to the autohide appbar associated with an edge of the screen. This message extends [**ABM\_GETAUTOHIDEBAR**](abm-getautohidebar.md) by enabling you to specify a particular monitor, for use in multiple monitor situations.


```C++
hwndAutoHide = (HWND) SHAppBarMessage(ABM_GETAUTOHIDEBAR, pabd);
```



## Parameters

<dl> <dt>

*pabd* 
</dt> <dd>

A pointer to an [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-_appbardata) structure that specifies the screen edge and monitor. You must specify the **cbSize**, **uEdge**, and **rc** members when sending this message; all other members are ignored.

</dd> </dl>

## Return value

Returns the handle to the autohide appbar. The return value is **NULL** if an error occurs or if no autohide appbar is associated with the given edge of the given monitor.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Shellapi.h</dt> </dl> |



## See also

<dl> <dt>

[**ABM\_GETAUTOHIDEBAR**](abm-getautohidebar.md)
</dt> <dt>

[**ABM\_SETAUTOHIDEBAR**](abm-setautohidebar.md)
</dt> <dt>

[**ABM\_SETAUTOHIDEBAREX**](abm-setautohidebarex.md)
</dt> </dl>

 

 




