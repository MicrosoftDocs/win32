---
Description: Sets the points of the currently selected objects to the data object on Copy and Cut commands. Used by SHShellFolderView\_Message.
title: SFVM\_SETPOINTS message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SFVM\_SETPOINTS message

Sets the points of the currently selected objects to the data object on **Copy** and **Cut** commands. Used by [**SHShellFolderView\_Message**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shshellfolderview_message).


```C++
SFVM_SETPOINTS 

    lParam = (LPARAM) pdtobj;

            
```



## Parameters

<dl> <dt>

*pdtobj* \[in\]
</dt> <dd>A pointer to an [**IDataObject**](https://msdn.microsoft.com/8a002deb-2727-456c-8078-a9b0d5893ed4) of the **Copy** and **Cut** commands.</dd> </dl>

## Return value

Always returns zero.

## Remarks

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




