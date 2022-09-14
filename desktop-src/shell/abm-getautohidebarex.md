---
description: Retrieves the handle to the autohide appbar associated with an edge of the screen. This message extends ABM\_GETAUTOHIDEBAR by enabling you to specify a particular monitor, for use in multiple monitor situations.
title: ABM_GETAUTOHIDEBAREX message (Shellapi.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 538EA230-06DF-4441-A6AA-9DD613521BE1
api_name: 
 - ABM_GETAUTOHIDEBAREX
api_type: 
 - HeaderDef
api_location: 
 - Shellapi.h
topic_type: 
 - APIRef
 - kbSyntax

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

A pointer to an [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure that specifies the screen edge and monitor. You must specify the **cbSize**, **uEdge**, and **rc** members when sending this message; all other members are ignored.

</dd> </dl>

## Return value

Returns the handle to the autohide appbar. The return value is **NULL** if an error occurs or if no autohide appbar is associated with the given edge of the given monitor.

## Requirements



| Requirement | Value |
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

 

 




