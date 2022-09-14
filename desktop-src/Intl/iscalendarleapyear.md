---
description: Deprecated. Identifies whether the specified year is a leap year within the given era for the specific calendar.
ms.assetid: 91f58915-f0c6-4c7a-9d9a-96e255d799fd
title: IsCalendarLeapYear function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IsCalendarLeapYear
api_type: 
- DllExport
api_location: 
- Kernel32.dll
- API-MS-Win-Core-calendar-l1-1-0.dll
- kernel32legacy.dll
---

# IsCalendarLeapYear function

Deprecated. Identifies whether the specified year is a leap year within the given era for the specific calendar.

## Syntax


```C++
BOOL IsCalendarLeapYear(
  _In_ CALID calId,
  _In_ UINT  year,
  _In_ UINT  era
);
```



## Parameters

<dl> <dt>

*calId* \[in\]
</dt> <dd>

The [calendar identifier](calendar-identifiers.md) to use for checking leap year.

</dd> <dt>

*year* \[in\]
</dt> <dd>

The year to check.

</dd> <dt>

*era* \[in\]
</dt> <dd>

The era to check.

</dd> </dl>

## Return value

Returns **TRUE** if the specified year is a leap year, or **FALSE** otherwise. To get extended error information, the application can call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror), which can return one of the following error codes:

-   ERROR\_INVALID\_PARAMETER. Any of the parameter values was invalid.

## Remarks

This function does not have an associated header file or library file. The application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (Kernel32.dll) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with that module handle and the name of this function to get the function address.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Kernel32.dll</dt> </dl> |



## See also

<dl> <dt>

[National Language Support](national-language-support.md)
</dt> <dt>

[National Language Support Functions](national-language-support-functions.md)
</dt> </dl>

 

 
