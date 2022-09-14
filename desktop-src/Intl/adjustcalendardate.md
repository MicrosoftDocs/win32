---
description: Deprecated. Adjusts a date by a specified number of years, months, weeks, or days.
ms.assetid: be8d61fd-efa3-4386-969f-30216c282ebc
title: AdjustCalendarDate function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AdjustCalendarDate
api_type: 
- DllExport
api_location: 
- Kernel32.dll
- API-MS-Win-Core-calendar-l1-1-0.dll
- kernel32legacy.dll
---

# AdjustCalendarDate function

Deprecated. Adjusts a date by a specified number of years, months, weeks, or days.

## Syntax


```C++
BOOL AdjustCalendarDate(
  _Inout_ LPCALDATETIME        lpCalDateTime,
  _In_    CALDATETIME_DATEUNIT calUnit,
  _Out_   INT                  amount
);
```



## Parameters

<dl> <dt>

*lpCalDateTime* \[in, out\]
</dt> <dd>

Pointer to a [**CALDATETIME**](caldatetime.md) structure that contains the date and calendar information to adjust.

</dd> <dt>

*calUnit* \[in\]
</dt> <dd>

The [**CALDATETIME\_DATEUNIT**](caldatetime-dateunit.md) enumeration value indicating the date unit, for example, DayUnit.

</dd> <dt>

*amount* \[out\]
</dt> <dd>

The amount by which to adjust the specified date.

</dd> </dl>

## Return value

Returns **TRUE** if successful or **FALSE** otherwise. To get extended error information, the application can call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror), which can return one of the following error codes:

-   ERROR\_DATE\_OUT\_OF\_RANGE. The specified date was out of range.
-   ERROR\_INVALID\_PARAMETER. Any of the parameter values was invalid.

## Remarks

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

 

 
