---
Description: 'Updates an object by passing a pointer to an array of two pointers to item identifier lists (PIDLs). Used by SHShellFolderView\_Message.'
title: 'SFVM\_UPDATEOBJECT message'
---

# SFVM\_UPDATEOBJECT message

Updates an object by passing a pointer to an array of two pointers to item identifier lists (PIDLs). Used by [**SHShellFolderView\_Message**](shshellfolderview-message.md).


```C++

                SFVM_UPDATEOBJECT 

    lParam = (LPARAM*) ppidl;

            
```



## Parameters

<dl> <dt>

*ppidl* \[in\]
</dt> <dd>

The address of an array of two PIDLs. The first PIDL is the old PIDL. The second one is a copy of the old PIDL with updated information. Control over the copy's lifetime belongs to the view after successful completion of this call.

</dd> </dl>

## Return value

Returns the listview ID of the updated object if the update was successful; otherwise, it returns -1.

## Remarks

If the update was unsuccessful, the caller must free the memory.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




