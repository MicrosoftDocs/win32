---
description: DFM_WM_INITMENUPOPUP message - Sent when a drop-down menu or submenu is about to become active. This allows an application to modify the menu before it is displayed, without changing the entire menu.
title: DFM_WM_INITMENUPOPUP message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 314e83f7-839d-4ca0-b5c1-842c5bf14923
api_name: 
 - DFM_WM_INITMENUPOPUP
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

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



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




