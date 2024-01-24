---
description: Deprecated. Gets the supported date range for a specified calendar.
ms.assetid: fe036ac5-77c0-4e83-8d70-db3fa0f7c803
title: GetCalendarSupportedDateRange function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetCalendarSupportedDateRange
api_type: 
- DllExport
api_location: 
- Kernel32.dll
- API-MS-Win-Core-calendar-l1-1-0.dll
- kernel32legacy.dll
---

# GetCalendarSupportedDateRange function

Deprecated. Gets the supported date range for a specified calendar.

## Syntax


```C++
BOOL GetCalendarSupportedDateRange(
  _In_  CALID         Calendar,
  _Out_ LPCALDATETIME lpCalMinDateTime,
  _Out_ LPCALDATETIME lpCalMaxDateTime
);
```



## Parameters

<dl> <dt>

*Calendar* \[in\]
</dt> <dd>

[Calendar identifier](calendar-identifiers.md) for which to get the supported date range.

</dd> <dt>

*lpCalMinDateTime* \[out\]
</dt> <dd>

Pointer to a [**CALDATETIME**](caldatetime.md) structure defining the minimum supported date.

</dd> <dt>

*lpCalMaxDateTime* \[out\]
</dt> <dd>

Pointer to a [**CALDATETIME**](caldatetime.md) structure defining the maximum supported date.

</dd> </dl>

## Return value

Returns **TRUE** if successful or **FALSE** otherwise. To get extended error information, the application can call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror), which can return one of the following error codes:

-   ERROR\_INVALID\_PARAMETER. Any of the parameter values was invalid.

## Remarks

The earliest date supported by this function is January 1, 1601.

This function does not have an associated header file or library file. The application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (Kernel32.dll) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with the module handle and the name of this function to get the function address.

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
</dt> <dt>

[NLS: Name-based APIs Sample](nls--name-based-apis-sample.md)
</dt> </dl>

 

 
