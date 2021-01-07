---
description: Gets the name of the default view. Call GetDisplayNameOf to retrieve the names of the other views.
title: IShellFolderViewType::GetDefaultViewName method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellFolderViewType.GetDefaultViewName
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 99229d13-40dc-4750-81a7-48a2f608b778
api_name: 
 - IShellFolderViewType.GetDefaultViewName
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# IShellFolderViewType::GetDefaultViewName method

Gets the name of the default view. Call [**GetDisplayNameOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof) to retrieve the names of the other views.

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

The address of a string pointer that receives the default view name. The memory for the string is allocated with [**SHStrDup**](/windows/desktop/api/Shlwapi/nf-shlwapi-shstrdupa).

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 




