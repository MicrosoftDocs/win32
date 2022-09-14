---
description: Flushes the shim database cache. This function should be called after installing a new shim database.
ms.assetid: 7e5bbdca-7b58-4c51-9cd1-105b05ee7fbe
title: ShimFlushCache function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShimFlushCache
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# ShimFlushCache function

Flushes the shim database cache. This function should be called after installing a new shim database.

## Syntax


```C++
BOOL WINAPI ShimFlushCache(
  _In_opt_ HWND      hwnd,
  _In_opt_ HINSTANCE hInstance,
  _In_opt_ LPCSTR    lpszCmdLine,
  _In_     int       nCmdShow
);
```



## Parameters

<dl> <dt>

*hwnd* \[in, optional\]
</dt> <dd>

Unused; must be 0.

</dd> <dt>

*hInstance* \[in, optional\]
</dt> <dd>

Unused; must be 0.

</dd> <dt>

*lpszCmdLine* \[in, optional\]
</dt> <dd>

Unused; must be 0.

</dd> <dt>

*nCmdShow* \[in\]
</dt> <dd>

Unused; must be 0.

</dd> </dl>

## Return value

The function returns **TRUE** on success or **FALSE** on failure.

## Remarks

The caller must be an administrator.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**BaseFlushAppcompatCache**](baseflushappcompatcache.md)
</dt> </dl>

 

 




