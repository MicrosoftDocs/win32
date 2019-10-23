---
Description: SFVM\_DIDDRAGDROP may be altered or unavailable.
ms.assetid: 5d37cf61-d8a7-4afa-9159-fea13d2b1d59
title: SFVM_DIDDRAGDROP message
ms.topic: reference
ms.date: 05/31/2018
---

# SFVM\_DIDDRAGDROP message

\[**SFVM\_DIDDRAGDROP** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Notifies the callback function that a drag-and-drop operation has begun. Used by [**IShellFolderViewCB::MessageSFVCB**](https://msdn.microsoft.com/en-us/library/Bb774968(v=VS.85).aspx).


```C++
SFVM_DIDDRAGDROP 
    wParam = (WPARAM)(DWORD) dwEffect;
    lParam = (LPARAM)(IDataObject*) pIdo;
            
```



## Parameters

<dl> <dt>

*dwEffect* \[in\]
</dt> <dd>

A drop effect specifier from the [**DROPEFFECT**](https://msdn.microsoft.com/en-us/library/ms693457(v=VS.85).aspx) enumeration. This is obtained by calling [**SHDoDragDrop**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shdodragdrop).

</dd> <dt>

*pIdo* \[in\]
</dt> <dd>

A pointer to the [**IDataObject**](https://msdn.microsoft.com/en-us/library/ms688421(v=VS.85).aspx) instance.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| End of client support<br/>    | Windows XP with SP2<br/>                                                      |
| End of server support<br/>    | Windows Server 2003<br/>                                                      |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




