---
description: Makes this pointer to an item identifier list (PIDL) an invalid portion of the Shell folder.
title: IShellFolderSearchable::InvalidateSearch method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellFolderSearchable.InvalidateSearch
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 6985a299-8547-4db4-99f9-d46dafe4789b

---

# IShellFolderSearchable::InvalidateSearch method

Makes this pointer to an item identifier list (PIDL) an invalid portion of the Shell folder.

## Syntax


```C++
HRESULT InvalidateSearch(
  [in] LPCITEMIDLIST pidlSearch,
  [in] DWORD         *pdwFlags
);
```



## Parameters

<dl> <dt>

*pidlSearch* \[in\]
</dt> <dd>

Type: **LPCITEMIDLIST**

A pointer to the [**ITEMIDLIST**](/windows/desktop/api/Shtypes/ns-shtypes-itemidlist) structure for the search folder.

</dd> <dt>

*pdwFlags* \[in\]
</dt> <dd>

Type: **DWORD\***

No flags are currently defined; set to **NULL**.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

When a search folder is invalidated, it can perform cleanup of any resources it has used. The **IShellFolderSearchable::InvalidateSearch** method may cause an asynchronous search to be canceled and will result in the eventual release of the [**IShellFolderSearchableCallback**](ishellfoldersearchablecallback.md) interface object.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 




