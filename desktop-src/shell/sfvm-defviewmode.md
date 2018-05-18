---
Description: 'Allows the callback object to specify the view mode. Used by IShellFolderViewCB::MessageSFVCB.'
title: 'SFVM\_DEFVIEWMODE message'
---

# SFVM\_DEFVIEWMODE message

Allows the callback object to specify the view mode. Used by [**IShellFolderViewCB::MessageSFVCB**](ishellfolderviewcb-messagesfvcb.md).


```C++
SFVM_DEFVIEWMODE 

    lParam = (LPARAM)(FOLDERVIEWMODE*) pViewMode;

            
```



## Parameters

<dl> <dt>

*pViewMode* \[out\]
</dt> <dd>

One of the values from the [**FOLDERVIEWMODE**](folderviewmode.md) enumerated type.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




