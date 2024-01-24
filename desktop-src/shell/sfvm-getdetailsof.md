---
description: SFVM\_GETDETAILSOF may be altered or unavailable.
ms.assetid: 46a81a7b-527c-4d41-8d25-ce65fd87416e
title: SFVM_GETDETAILSOF message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SFVM\_GETDETAILSOF message

\[**SFVM\_GETDETAILSOF** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Allows the callback object to provide the details for an item in a Shell folder. Use only if a call to [**IShellFolder2::GetDetailsOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder2-getdetailsof) fails and there is no [**IShellDetails::GetDetailsOf**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishelldetails-getdetailsof) method available to call. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishellfolderviewcb-messagesfvcb).


```C++
SFVM_GETDETAILSOF
    wParam = (WPARAM)(int) iColumn;
    lParam = (LPARAM)(DETAILSINFO*) pDi;
            
```



## Parameters

<dl> <dt>

*iColumn* \[in\]
</dt> <dd>

The zero-based ID of the column.

</dd> <dt>

*pDi* \[out\]
</dt> <dd>

A pointer to a [**DETAILSINFO**](/windows/desktop/api/shlobj_core/ns-shlobj_core-detailsinfo) structure filled with the requested information.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| End of client support<br/>    | Windows XP with SP2<br/>                                                      |
| End of server support<br/>    | Windows Server 2003<br/>                                                      |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
