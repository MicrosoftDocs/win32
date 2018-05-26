---
Description: Allows the callback object to specify the view mode. Used by IShellFolderViewCBMessageSFVCB.
title: SFVM\_DEFVIEWMODE message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_DEFVIEWMODE message

Allows the callback object to specify the view mode. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


```C++
SFVM_DEFVIEWMODE 

    lParam = (LPARAM)(FOLDERVIEWMODE*) pViewMode;

            
```



## Parameters

<dl> <dt>

*pViewMode* \[out\]
</dt> <dd>

One of the values from the [**FOLDERVIEWMODE**](/windows/win32/shobjidl_core/ne-shobjidl_core-folderviewmode?branch=master) enumerated type.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




