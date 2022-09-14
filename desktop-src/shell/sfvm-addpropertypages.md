---
description: Allows the callback object to provide a page to add to the Properties property sheet of the selected object. Used by IShellFolderViewCB::MessageSFVCB.
title: SFVM_ADDPROPERTYPAGES message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 54f67d0e-6089-4e75-a547-5313794e1512
api_name: 
 - SFVM_ADDPROPERTYPAGES
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SFVM\_ADDPROPERTYPAGES message

Allows the callback object to provide a page to add to the **Properties** property sheet of the selected object. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishellfolderviewcb-messagesfvcb).


```C++
SFVM_ADDPROPERTYPAGES 

    lParam = (LPARAM)(SFVM_PROPPAGE_DATA*) pData;

            
```



## Parameters

<dl> <dt>

*pData* \[out\]
</dt> <dd>

The address of a [**SFVM\_PROPPAGE\_DATA**](/windows/desktop/api/shlobj_core/ns-shlobj_core-sfvm_proppage_data) structure.

</dd> </dl>

## Remarks

This message serves essentially the same function as [**IShellPropSheetExt::AddPages**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellpropsheetext-addpages). See [Creating Property Sheet Handlers](propsheet-handlers.md) for further discussion.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
