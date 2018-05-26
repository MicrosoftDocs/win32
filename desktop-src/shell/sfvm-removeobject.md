---
Description: Removes an object from the shell view. Used by SHShellFolderView\_Message.
title: SFVM\_REMOVEOBJECT message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_REMOVEOBJECT message

Removes an object from the shell view. Used by [**SHShellFolderView\_Message**](/windows/win32/shlobj_core/nf-shlobj_core-shshellfolderview_message?branch=master).


```C++
SFVM_REMOVEOBJECT 
    lParam = (LPARAM) pidl;
            
```



## Parameters

<dl> <dt>

*pidl* \[in\]
</dt> <dd>PIDL of the object to remove.</dd> </dl>

## Return value

Returns the index of the item that was removed if an item matching the specified PIDL was found; otherwise, returns -1.

## Remarks

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




