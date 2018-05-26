---
Description: Begins the process of canceling a pending asynchronous search.
title: IShellFolderSearchableCancelAsyncSearch method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IShellFolderSearchable::CancelAsyncSearch method

Begins the process of canceling a pending asynchronous search.

## Syntax


```C++
HRESULT CancelAsyncSearch(
  [in] LPCITEMIDLIST pidlSearch,
  [in] DWORD         *pdwFlags
);
```



## Parameters

<dl> <dt>

*pidlSearch* \[in\]
</dt> <dd>

Type: **LPCITEMIDLIST**

A pointer to an [**ITEMIDLIST**](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) for the search.

</dd> <dt>

*pdwFlags* \[in\]
</dt> <dd>

Type: **DWORD\***

No flags are currently defined; set to **NULL**.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if canceling, or S\_FALSE if search is not running.

## Remarks

When the search is actually canceled, [**RunEnd**](ishellfoldersearchablecallback-runend.md) will be called.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 




