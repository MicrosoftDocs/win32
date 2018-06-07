---
Description: Retrieves an array of pointers to item identifier lists (PIDLs) for all selected objects. Used by SHShellFolderView\_Message.
title: SFVM\_GETSELECTEDOBJECTS message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SFVM\_GETSELECTEDOBJECTS message

Retrieves an array of pointers to item identifier lists (PIDLs) for all selected objects. Used by [**SHShellFolderView\_Message**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shshellfolderview_message).


```C++
SFVM_GETSELECTEDOBJECTS 

    lParam = (LPARAM*) ppidl;

            
```



## Parameters

<dl> <dt>

*ppidl* \[out\]
</dt> <dd>The address of an array of PIDLs of currently selected objects.</dd> </dl>

## Return value

Returns the number of items in the array.

## Remarks

When finished, you should call [**ILFree**](/windows/desktop/api/shlobj_core/nf-shlobj_core-ilfree) on each member of the array to free the memory.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




