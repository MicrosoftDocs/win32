---
Description: 'Allows the callback object to provide a page to add to the Properties property sheet of the selected object. Used by IShellFolderViewCB::MessageSFVCB.'
title: 'SFVM\_ADDPROPERTYPAGES message'
---

# SFVM\_ADDPROPERTYPAGES message

Allows the callback object to provide a page to add to the **Properties** property sheet of the selected object. Used by [**IShellFolderViewCB::MessageSFVCB**](ishellfolderviewcb-messagesfvcb.md).


```C++
SFVM_ADDPROPERTYPAGES 

    lParam = (LPARAM)(SFVM_PROPPAGE_DATA*) pData;

            
```



## Parameters

<dl> <dt>

*pData* \[out\]
</dt> <dd>

The address of a [**SFVM\_PROPPAGE\_DATA**](sfvm-proppage-data.md) structure.

</dd> </dl>

## Remarks

This message serves essentially the same function as [**IShellPropSheetExt::AddPages**](ishellpropsheetext-addpages.md). See [Creating Property Sheet Handlers](propsheet-handlers.md) for further discussion.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




