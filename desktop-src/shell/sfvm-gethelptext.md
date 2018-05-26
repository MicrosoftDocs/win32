---
Description: Allows the callback object to specify a help text string for menu items or toolbar buttons. Used by IShellFolderViewCBMessageSFVCB.
title: SFVM\_GETHELPTEXT message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_GETHELPTEXT message

Allows the callback object to specify a help text string for menu items or toolbar buttons. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


```C++
SFVM_GETHELPTEXT 

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



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




