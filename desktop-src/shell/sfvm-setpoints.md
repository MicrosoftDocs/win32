---
Description: 'Sets the points of the currently selected objects to the data object on Copy and Cut commands. Used by SHShellFolderView\_Message.'
title: 'SFVM\_SETPOINTS message'
---

# SFVM\_SETPOINTS message

Sets the points of the currently selected objects to the data object on **Copy** and **Cut** commands. Used by [**SHShellFolderView\_Message**](shshellfolderview-message.md).


```C++
SFVM_SETPOINTS 

    lParam = (LPARAM) pdtobj;

            
```



## Parameters

<dl> <dt>

*pdtobj* \[in\]
</dt> <dd>A pointer to an [**IDataObject**](com.idataobject) of the **Copy** and **Cut** commands.</dd> </dl>

## Return value

Always returns zero.

## Remarks

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




