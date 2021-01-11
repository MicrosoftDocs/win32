---
description: Allows the callback object to modify a Windows Explorer pop-up menu before it is displayed. Used by IShellFolderViewCB::MessageSFVCB.
title: SFVM_INITMENUPOPUP message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 9d7e96e9-c52e-43bd-945b-05db33c8dfd0
api_name: 
 - SFVM_INITMENUPOPUP
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SFVM\_INITMENUPOPUP message

Allows the callback object to modify a Windows Explorer pop-up menu before it is displayed. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishellfolderviewcb-messagesfvcb).


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



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



## See also

<dl> <dt>

[**SFVM\_MERGEMENU**](sfvm-mergemenu.md)
</dt> </dl>

 

 
