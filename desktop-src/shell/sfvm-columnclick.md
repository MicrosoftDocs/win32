---
description: Notifies the callback object that the user has clicked a column header to sort the list of objects in the folder view. Used by IShellFolderViewCB::MessageSFVCB.
title: SFVM_COLUMNCLICK message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 351be842-6ea5-4223-8162-0e6c4e6a5afb
api_name: 
 - SFVM_COLUMNCLICK
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SFVM\_COLUMNCLICK message

Notifies the callback object that the user has clicked a column header to sort the list of objects in the folder view. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishellfolderviewcb-messagesfvcb).


```C++
SFVM_COLUMNCLICK 

    wParam = (WPARAM)(UINT)iColumn;

            
```



## Parameters

<dl> <dt>

*iColumn* \[in\]
</dt> <dd>

The index of the column that was clicked.

</dd> </dl>

## Remarks

In response to this notification, you should return S\_OK to rearrange the list yourself. To have the system folder view object rearrange the list, return S\_FALSE.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
