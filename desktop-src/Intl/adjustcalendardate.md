---
Description: Deprecated. Adjusts a date by a specified number of years, months, weeks, or days.
ms.assetid: be8d61fd-efa3-4386-969f-30216c282ebc
title: AdjustCalendarDate function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Returns **TRUE** if successful or **FALSE** otherwise. To get extended error information, the application can call [**GetLastError**](https://msdn.microsoft.com/d852e148-985c-416f-a5a7-27b6914b45d4), which can return one of the following error codes:

-   ERROR\_DATE\_OUT\_OF\_RANGE. The specified date was out of range.
-   ERROR\_INVALID\_PARAMETER. Any of the parameter values was invalid.

## Remarks

This function does not have an associated header file or library file. The application can call [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) with the DLL name (Kernel32.dll) to obtain a module handle. It can then call [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) with the module handle and the name of this function to get the function address.

## Requirements



|                                     |                                                                                         |
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

 

 




