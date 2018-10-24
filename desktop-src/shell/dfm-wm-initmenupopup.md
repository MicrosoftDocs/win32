---
Description: Sent when a drop-down menu or submenu is about to become active. This allows an application to modify the menu before it is displayed, without changing the entire menu.
title: DFM_WM_INITMENUPOPUP message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DFM\_WM\_INITMENUPOPUP message

Sent when a drop-down menu or submenu is about to become active. This allows an application to modify the menu before it is displayed, without changing the entire menu.


```C++
DFM_WM_INITMENUPOPUP 

    wParam = (WPARAM);

    lParam = (LPARAM);

            
```



## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

A handle to the drop-down menu or submenu.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

The low-order word specifies the zero-based relative position of the menu item that opens the drop-down menu or submenu.

The high-order word indicates whether the drop-down menu is the window menu. If the menu is the window menu, this parameter is **TRUE**; otherwise, it is **FALSE**.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




