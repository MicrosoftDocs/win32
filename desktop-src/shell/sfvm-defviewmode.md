---
Description: Allows the callback object to specify the view mode. Used by IShellFolderViewCB::MessageSFVCB.
title: SFVM_DEFVIEWMODE message
ms.topic: article
ms.date: 05/31/2018
---

# SFVM\_DEFVIEWMODE message

Allows the callback object to specify the view mode. Used by [**IShellFolderViewCB::MessageSFVCB**](https://msdn.microsoft.com/en-us/library/Bb774968(v=VS.85).aspx).


```C++
SFVM_DEFVIEWMODE 

    lParam = (LPARAM)(FOLDERVIEWMODE*) pViewMode;

            
```



## Parameters

<dl> <dt>

*pViewMode* \[out\]
</dt> <dd>

One of the values from the [**FOLDERVIEWMODE**](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-folderviewmode) enumerated type.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




