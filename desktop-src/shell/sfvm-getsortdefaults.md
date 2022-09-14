---
description: Allows the callback object to specify a default sorting parameter. Used by IShellFolderViewCB::MessageSFVCB.
title: SFVM_GETSORTDEFAULTS message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: edd428f2-50d9-4819-ba77-df51262e33ff
api_name: 
 - SFVM_GETSORTDEFAULTS
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SFVM\_GETSORTDEFAULTS message

Allows the callback object to specify a default sorting parameter. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishellfolderviewcb-messagesfvcb).


```C++
SFVM_GETSORTDEFAULTS 

    wParam = (WPARAM)(int*) iDirection;

    lParam = (LPARAM)(int*) iColumn;

            
```



## Parameters

<dl> <dt>

*iDirection* \[out\]
</dt> <dd>

The default sorting direction. Set this parameter to a positive value to sort in ascending order. Set this parameter to zero or a negative value to sort in descending order.

</dd> <dt>

*iColumn* \[out\]
</dt> <dd>

The column used for the sort. This will be passed to the [**IShellFolder::CompareIDs**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-compareids) in the lower 16 bits of its *lParam* value.

</dd> </dl>

## Remarks

> [!Note]  
> : **SFVM\_GETSORTDEFAULTS** is not recognized by the system folder view object.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
