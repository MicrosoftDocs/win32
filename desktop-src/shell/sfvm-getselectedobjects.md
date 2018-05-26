---
Description: Retrieves an array of pointers to item identifier lists (PIDLs) for all selected objects. Used by SHShellFolderView\_Message.
title: SFVM\_GETSELECTEDOBJECTS message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_GETSELECTEDOBJECTS message

Retrieves an array of pointers to item identifier lists (PIDLs) for all selected objects. Used by [**SHShellFolderView\_Message**](/windows/win32/shlobj_core/nf-shlobj_core-shshellfolderview_message?branch=master).


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

When finished, you should call [**ILFree**](/windows/win32/shlobj_core/nf-shlobj_core-ilfree?branch=master) on each member of the array to free the memory.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




