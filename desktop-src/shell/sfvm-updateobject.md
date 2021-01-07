---
description: Updates an object by passing a pointer to an array of two pointers to item identifier lists (PIDLs). Used by SHShellFolderView\_Message.
title: SFVM_UPDATEOBJECT message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 3bd68ace-3ccf-446c-8cf9-52f42444674e
api_name: 
 - SFVM_UPDATEOBJECT
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SFVM\_UPDATEOBJECT message

Updates an object by passing a pointer to an array of two pointers to item identifier lists (PIDLs). Used by [**SHShellFolderView\_Message**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shshellfolderview_message).


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



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




