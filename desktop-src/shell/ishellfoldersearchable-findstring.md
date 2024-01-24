---
description: Begins a search for a specified search string.
ms.assetid: 6ecad03c-e8e0-45ba-8def-b55a029992f2
title: IShellFolderSearchable::FindString method (Mmc.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellFolderSearchable.FindString
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellFolderSearchable::FindString method

Begins a search for a specified search string.

## Syntax


```C++
HRESULT FindString(
  [in]  LPCWSTR      pwszTarget,
  [in]  DWORD        *pdwFlags,
  [in]  IUnknown     *punkOnAsyncSearch,
  [out] LPITEMIDLIST ppidlOut
);
```



## Parameters

<dl> <dt>

*pwszTarget* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to a string that specifies the search keyword.

</dd> <dt>

*pdwFlags* \[in\]
</dt> <dd>

Type: **DWORD\***

No flags are currently defined; set to **NULL**.

</dd> <dt>

*punkOnAsyncSearch* \[in\]
</dt> <dd>

Type: **[**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown)\***

A pointer to an object of type [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown). This object must support the [**IShellFolderSearchableCallback**](ishellfoldersearchablecallback.md) interface. Set to **NULL** if no callback is necessary.

</dd> <dt>

*ppidlOut* \[out\]
</dt> <dd>

Type: **LPITEMIDLIST**

A pointer to an [**ITEMIDLIST**](/windows/desktop/api/Shtypes/ns-shtypes-itemidlist) structure for the search folder.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 
