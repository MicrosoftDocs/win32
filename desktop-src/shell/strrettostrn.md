---
Description: Takes an STRRET structure returned by IShellFolderGetDisplayNameOf, converts it to a string, and places the result in a buffer.
title: StrRetToStrN function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StrRetToStrN function

Takes an [**STRRET**](/windows/win32/Shtypes/ns-shtypes-_strret?branch=master) structure returned by [**IShellFolder::GetDisplayNameOf**](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof?branch=master), converts it to a string, and places the result in a buffer.

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

Pointer to an [**STRRET**](/windows/win32/Shtypes/ns-shtypes-_strret?branch=master) structure. When the function returns, this pointer will no longer be valid.

</dd> <dt>

*pidl* \[in\]
</dt> <dd>

Type: **LPCITEMIDLIST**

Pointer to the item's [**ITEMIDLIST**](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.

</dd> </dl>

## Return value

Type: **BOOL**

**TRUE** for success, **FALSE** for failure.

## Remarks

> [!Note]  
> As of Shell32.dll version 5.0, calling this function is equivalent to calling [**StrRetToBuf**](/windows/win32/Shlwapi/nf-shlwapi-strrettobufa?branch=master).

 

**StrRetToStrN** is not exported by name. To use it, you must use [**GetProcAddress**](base.getprocaddress) and request ordinal 96 from Shell32.dll to obtain a function pointer.

If the **uType** member of the structure pointed to by *pStrRet* is set to **STRRET\_WSTR**, the **pOleStr** member of that structure will be freed on return.

Note that this function is exported from Shell32.dll rather than Shlwapi.dll. It is also included in Shlobj.h rather than Shlwapi.h.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



## See also

<dl> <dt>

[**StrRetToStr**](/windows/win32/Shlwapi/nf-shlwapi-strrettostra?branch=master)
</dt> <dt>

[**StrRetToBuf**](/windows/win32/Shlwapi/nf-shlwapi-strrettobufa?branch=master)
</dt> </dl>

 

 




