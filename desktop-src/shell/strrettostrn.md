---
description: Takes an STRRET structure returned by IShellFolder::GetDisplayNameOf, converts it to a string, and places the result in a buffer.
title: StrRetToStrN function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- StrRetToStrN
api_type: 
- DllExport
api_location: 
- Shell32.dll
ms.assetid: a816fb5f-8320-4b63-a85d-dd4c59596ead

---

# StrRetToStrN function

Takes an [**STRRET**](/windows/desktop/api/Shtypes/ns-shtypes-strret) structure returned by [**IShellFolder::GetDisplayNameOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof), converts it to a string, and places the result in a buffer.

## Syntax


```C++
BOOL StrRetToStrN(
  _Out_   LPTSTR        pszOut,
  _In_    UINT          cchOut,
  _Inout_ LPSTRRET      pStrRet,
  _In_    LPCITEMIDLIST pidl
);
```



## Parameters

<dl> <dt>

*pszOut* \[out\]
</dt> <dd>

Type: **LPTSTR**

Buffer to hold the display name. It will be returned as a null-terminated string. If *cchOut* is too small, the name will be truncated to fit.

</dd> <dt>

*cchOut* \[in\]
</dt> <dd>

Type: **UINT**

Size of *pszOut*, in characters. If *cchOut* is too small, the string will be truncated to fit.

</dd> <dt>

*pStrRet* \[in, out\]
</dt> <dd>

Type: **LPSTRRET**

Pointer to an [**STRRET**](/windows/desktop/api/Shtypes/ns-shtypes-strret) structure. When the function returns, this pointer will no longer be valid.

</dd> <dt>

*pidl* \[in\]
</dt> <dd>

Type: **LPCITEMIDLIST**

Pointer to the item's [**ITEMIDLIST**](/windows/desktop/api/Shtypes/ns-shtypes-itemidlist) structure.

</dd> </dl>

## Return value

Type: **BOOL**

**TRUE** for success, **FALSE** for failure.

## Remarks

> [!Note]  
> As of Shell32.dll version 5.0, calling this function is equivalent to calling [**StrRetToBuf**](/windows/desktop/api/Shlwapi/nf-shlwapi-strrettobufa).

 

**StrRetToStrN** is not exported by name. To use it, you must use [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) and request ordinal 96 from Shell32.dll to obtain a function pointer.

If the **uType** member of the structure pointed to by *pStrRet* is set to **STRRET\_WSTR**, the **pOleStr** member of that structure will be freed on return.

Note that this function is exported from Shell32.dll rather than Shlwapi.dll. It is also included in Shlobj.h rather than Shlwapi.h.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



## See also

<dl> <dt>

[**StrRetToStr**](/windows/desktop/api/Shlwapi/nf-shlwapi-strrettostra)
</dt> <dt>

[**StrRetToBuf**](/windows/desktop/api/Shlwapi/nf-shlwapi-strrettobufa)
</dt> </dl>

 

 
