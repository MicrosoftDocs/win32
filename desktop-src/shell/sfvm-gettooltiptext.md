---
description: Allows the callback object to specify a tooltip text string for menu items or toolbar buttons. Used by IShellFolderViewCB::MessageSFVCB.
ms.assetid: 29849218-0d30-4412-86c8-5d320bc5dd26
title: SFVM_GETTOOLTIPTEXT message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SFVM\_GETTOOLTIPTEXT message

Allows the callback object to specify a tooltip text string for menu items or toolbar buttons. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishellfolderviewcb-messagesfvcb).


```C++
SFVM_GETTOOLTIPTEXT 

    wParam = (WPARAM)(int) idCmd,cchMax;

    lParam = (LPARAM)(LPTSTR) pszText;

            
```



## Parameters

<dl> <dt>

*idCmd\_cchMax* \[in\]
</dt> <dd>

The low-order word of this parameter holds the command ID. The high-order word holds the number of characters in the *pszText* buffer.

</dd> <dt>

*pszText* \[out\]
</dt> <dd>

A null-terminated string containing the help text.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
