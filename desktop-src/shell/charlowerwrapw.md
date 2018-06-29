---
Description: Converts a Unicode character string or a single character to lowercase.
ms.assetid: 09b7cf8e-6aed-40f4-9dfa-29be3559ae89
title: CharLowerWrapW function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CharLowerWrapW
api_type: 
- DllExport
api_location: 
- Shlwapi.dll
---

# CharLowerWrapW function

\[**CharLowerWrapW** is available for use in Windows XP. It may not be available in subsequent versions. You should use [**CharLowerW**](https://msdn.microsoft.com/en-us/library/ms647467(v=VS.85).aspx) in its place.\]

Converts a Unicode character string or a single character to lowercase. If the operand is a character string, the function converts the characters in place.

> [!Note]  
> **CharLowerWrapW** is a wrapper for the **CharLowerW** function. See the [**CharLower**](https://msdn.microsoft.com/en-us/library/ms647467(v=VS.85).aspx) page for further usage notes.

 

## Syntax


```C++
LPWSTR CharLowerWrapW(
  _Inout_ LPWSTR pch
);
```



## Parameters

<dl> <dt>

*pch* \[in, out\]
</dt> <dd>

Type: **LPWSTR**

A pointer to a null-terminated Unicode string or a single character. If the high-order word of this parameter is zero, the low-order word must contain only a single character to be converted.

</dd> </dl>

## Return value

Type: **LPWSTR**

If *pch* is a character string, the function returns a pointer to the converted string. Since the string is converted in place, the return value is equal to *pch*.

If *pch* is a single character, the return value is a 32-bit value whose high-order word is zero, and low-order word contains the converted character.

There is no indication of success or failure. Failure is rare. There is no extended error information for this function; do not call [**GetLastError**](https://msdn.microsoft.com/en-us/library/ms679360(v=VS.85).aspx).

## Remarks

The preferred method is to use [**CharLowerW**](https://msdn.microsoft.com/en-us/library/ms647467(v=VS.85).aspx) in conjunction with the Microsoft Layer for Unicode (MSLU).

**CharLowerWrapW** must be called directly from Shlwapi.dll, using ordinal 38.

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shlwapi.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**CharLower**](https://msdn.microsoft.com/en-us/library/ms647467(v=VS.85).aspx)
</dt> </dl>

 

 




