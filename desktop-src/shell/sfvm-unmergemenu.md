---
Description: Notifies the callback object that a menu is being removed. Used by IShellFolderViewCBMessageSFVCB.
title: SFVM\_UNMERGEMENU message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_UNMERGEMENU message

Notifies the callback object that a menu is being removed. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


```C++
SFVM_UNMERGEMENU 

    lParam = (LPARAM)(HMENU) hmenuCurrent;

            
```



## Parameters

<dl> <dt>

*hmenuCurrent* \[in\]
</dt> <dd>

The handle of the menu that is being removed.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




