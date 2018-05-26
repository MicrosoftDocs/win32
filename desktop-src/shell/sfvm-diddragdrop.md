---
Description: SFVM\_DIDDRAGDROP may be altered or unavailable.
ms.assetid: 5d37cf61-d8a7-4afa-9159-fea13d2b1d59
title: SFVM\_DIDDRAGDROP message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_DIDDRAGDROP message

\[**SFVM\_DIDDRAGDROP** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Notifies the callback function that a drag-and-drop operation has begun. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


```C++
SFVM_DIDDRAGDROP 
    wParam = (WPARAM)(DWORD) dwEffect;
    lParam = (LPARAM)(IDataObject*) pIdo;
            
```



## Parameters

<dl> <dt>

*dwEffect* \[in\]
</dt> <dd>

A drop effect specifier from the [**DROPEFFECT**](com.dropeffect_constants) enumeration. This is obtained by calling [**SHDoDragDrop**](/windows/win32/shlobj_core/nf-shlobj_core-shdodragdrop?branch=master).

</dd> <dt>

*pIdo* \[in\]
</dt> <dd>

A pointer to the [**IDataObject**](com.idataobject) instance.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| End of client support<br/>    | Windows XP with SP2<br/>                                                      |
| End of server support<br/>    | Windows Server 2003<br/>                                                      |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




