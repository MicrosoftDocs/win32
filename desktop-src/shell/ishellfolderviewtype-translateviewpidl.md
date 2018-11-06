---
Description: Reconstructs a pointer to an item identifier list (PIDL) from one hierarchical representation of the Shell folder into a different representation.
title: IShellFolderViewType::TranslateViewPidl method
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellFolderViewType.TranslateViewPidl
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellFolderViewType::TranslateViewPidl method

Reconstructs a pointer to an item identifier list (PIDL) from one hierarchical representation of the Shell folder into a different representation.

## Syntax


```C++
HRESULT TranslateViewPidl(
  [in] PCUIDLIST_RELATIVE pidl,
  [in] PCUIDLIST_RELATIVE pidlView,
  [in] PCUIDLIST_RELATIVE *ppidlOut
);
```



## Parameters

<dl> <dt>

*pidl* \[in\]
</dt> <dd>

Type: **PCUIDLIST\_RELATIVE**

The array of item IDs relative to the root folder.

</dd> <dt>

*pidlView* \[in\]
</dt> <dd>

Type: **PCUIDLIST\_RELATIVE**

Special PIDL of the view.

</dd> <dt>

*ppidlOut* \[in\]
</dt> <dd>

Type: **PCUIDLIST\_RELATIVE\***

The address of a PIDL variable to receive the translation.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

When finished, you should free the returned PIDL with [**ILFree**](/windows/desktop/api/shlobj_core/nf-shlobj_core-ilfree).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 




