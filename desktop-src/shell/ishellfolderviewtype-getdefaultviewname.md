---
Description: 'Gets the name of the default view. Call GetDisplayNameOf to retrieve the names of the other views.'
title: 'IShellFolderViewType::GetDefaultViewName method'
---

# IShellFolderViewType::GetDefaultViewName method

Gets the name of the default view. Call [**GetDisplayNameOf**](ishellfolder-getdisplaynameof.md) to retrieve the names of the other views.

## Syntax


```C++
HRESULT GetDefaultViewName(
  [in]  DWORD  uFlags,
  [out] LPWSTR *ppwszName
);
```



## Parameters

<dl> <dt>

*uFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Optional flags; should be set to 0.

</dd> <dt>

*ppwszName* \[out\]
</dt> <dd>

Type: **LPWSTR\***

The address of a string pointer that receives the default view name. The memory for the string is allocated with [**SHStrDup**](shstrdup.md).

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 




