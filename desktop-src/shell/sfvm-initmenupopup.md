---
Description: Allows the callback object to modify a Windows Explorer pop-up menu before it is displayed. Used by IShellFolderViewCB::MessageSFVCB.
title: SFVM\_INITMENUPOPUP message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SFVM\_INITMENUPOPUP message

Allows the callback object to modify a Windows Explorer pop-up menu before it is displayed. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/desktop/api/Shlobj/).


```C++
SFVM_INITMENUPOPUP 

    wParam = (WPARAM)(int) idCmd,nIndex;

    lParam = (LPARAM)(HMENU) hmenu;

            
```



## Parameters

<dl> <dt>

*idCmd\_nIndex* \[in\]
</dt> <dd>

The low-order word of this parameter holds the value of the first command ID reserved for client commands. The high-order word holds the index of the menu.

</dd> <dt>

*hmenu* \[in, out\]
</dt> <dd>

The menu's handle.

</dd> </dl>

## Remarks

The system folder view object sends this message when a menu is selected, but before it is displayed. Process this message if, for instance, you need to enable or disable menu commands. The popup menu can be:

-   The File, Edit, or View menu.
-   A top-level menu defined by the client.
-   A client-defined submenu.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



## See also

<dl> <dt>

[**SFVM\_MERGEMENU**](sfvm-mergemenu.md)
</dt> </dl>

 

 




