---
Description: Adds an object to the Shell view. Used by SHShellFolderView\_Message.
title: SFVM_ADDOBJECT message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SFVM\_ADDOBJECT message

Adds an object to the Shell view. Used by [**SHShellFolderView\_Message**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shshellfolderview_message).


```C++
SFVM_ADDOBJECT 

    lParam = (LPARAM) pidl;

            
```



## Parameters

<dl> <dt>

*pidl* \[in\]
</dt> <dd>A pointer to the object of interest to add.</dd> </dl>

## Return value

Returns the new listview item ID of the added object if the process was successful; otherwise, returns -1.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




