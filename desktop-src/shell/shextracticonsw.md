---
description: Creates an array of handles to icons extracted from a specified file.
title: SHExtractIconsW function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SHExtractIconsW
- SHExtractIconsW
api_type: 
- DllExport
api_location: 
- Shell32.dll
ms.assetid: 9f138b4e-6a84-4c7e-9521-5f8ffe0eaebf
api_name: 
 - SHExtractIconsW
 - SHExtractIconsW
api_type: 
 - DllExport
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# SHExtractIconsW function

\[**SHExtractIconsW** is available through Windows XP Service Pack 2 (SP2). It might be altered or unavailable in subsequent versions.\]

Creates an array of handles to icons extracted from a specified file.

## Syntax


```C++
UINT SHExtractIconsW(
  _In_  LPCWSTR pszFileName,
  _In_  int     nIconIndex,
  _In_  int     cxIcon,
  _In_  int     cyIcon,
  _Out_ HICON   *phIcon,
  _Out_ UINT    *pIconId,
  _In_  UINT    nIcons,
  _In_  UINT    flags
);
```



## Parameters

<dl> <dt>

*pszFileName* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to the file name from which to extract the icons.

</dd> <dt>

*nIconIndex* \[in\]
</dt> <dd>

Type: **int**

The index of the first icon to extract from the resource named in *pszFileName*.

</dd> <dt>

*cxIcon* \[in\]
</dt> <dd>

Type: **int**

The desired width of the icon. See Remarks.

</dd> <dt>

*cyIcon* \[in\]
</dt> <dd>

Type: **int**

The desired height of the icon. See Remarks.

</dd> <dt>

*phIcon* \[out\]
</dt> <dd>

Type: **HICON\***

When this function returns, contains a pointer to the array of icon handles.

</dd> <dt>

*pIconId* \[out\]
</dt> <dd>

Type: **UINT\***

When this function returns, contains a pointer to the resource identifier of the extracted icon that best fits the current display device. If there is no identifier available for this format, it contains 0xFFFFFFFF. If no identifier can be obtained for any other reason, returns zero.

</dd> <dt>

*nIcons* \[in\]
</dt> <dd>

Type: **UINT**

The number of icons to extract from the resource named in *pszFileName*. This parameter is valid only when the resource is a .exe or .dll file.

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Type: **UINT**

The flags that control this function. For possible values, see the *fuLoad* parameter of the [**LoadImage**](/windows/win32/api/winuser/nf-winuser-loadimagea) function.

</dd> </dl>

## Return value

Type: **UINT**

A nonzero value if successful; otherwise, zero.

## Remarks

**SHExtractIconsW** extracts from the following file types.

-   Executable (.exe)
-   DLL (.dll)
-   Icon (.ico)
-   Cursor (.cur)
-   Animated cursor (.ani)
-   Bitmap (.bmp)

Extractions from Windows 3.*x* 16-bit executable files (.exe or .dll) are also supported.

The *cxIcon* and *cyIcon* parameters specify the size of the icons to extract. Two sizes can be extracted through each parameter by splitting the value between its LOWORD and HIWORD. Put the first desired size in the LOWORD of the parameter and the second size in the HIWORD. For example, [**MAKELONG**](/previous-versions/windows/desktop/legacy/ms632660(v=vs.85))(24, 48) for both *cxIcon* and *cyIcon* extracts both 24 and 48 sized icons.

The calling process is responsible for destroying all icons extracted through this function by calling the [**DestroyIcon**](/windows/win32/api/winuser/nf-winuser-destroyicon) function.

**SHExtractIconsW** is not exported by name or declared in a public header file. To use it, you must declare a matching prototype and use [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) to request a function pointer from Shell32.dll that can be used to call this function.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |
| Unicode and ANSI names<br/>   | **SHExtractIconsW** (Unicode)<br/>                                                                      |



 

 
