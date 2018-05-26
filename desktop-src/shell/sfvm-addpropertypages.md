---
Description: Allows the callback object to provide a page to add to the Properties property sheet of the selected object. Used by IShellFolderViewCBMessageSFVCB.
title: SFVM\_ADDPROPERTYPAGES message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_ADDPROPERTYPAGES message

Allows the callback object to provide a page to add to the **Properties** property sheet of the selected object. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


```C++
SFVM_ADDPROPERTYPAGES 

    lParam = (LPARAM)(SFVM_PROPPAGE_DATA*) pData;

            
```



## Parameters

<dl> <dt>

*pData* \[out\]
</dt> <dd>

The address of a [**SFVM\_PROPPAGE\_DATA**](/windows/win32/shlobj_core/ns-shlobj_core-_sfvm_proppage_data?branch=master) structure.

</dd> </dl>

## Remarks

This message serves essentially the same function as [**IShellPropSheetExt::AddPages**](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellpropsheetext-addpages?branch=master). See [Creating Property Sheet Handlers](propsheet-handlers.md) for further discussion.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




