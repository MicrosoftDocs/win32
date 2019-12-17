---
Description: Deprecated. Converts a specified SYSTEMTIME structure to a CALDATETIME structure.
ms.assetid: d21f75bc-1a93-4cb9-8b9b-6fa0e81886bf
title: ConvertSystemTimeToCalDateTime function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ConvertSystemTimeToCalDateTime
api_type: 
- DllExport
api_location: 
- Kernel32.dll
- API-MS-Win-Core-calendar-l1-1-0.dll
- kernel32legacy.dll
---

# ConvertSystemTimeToCalDateTime function

Deprecated. Converts a specified [**SYSTEMTIME**](https://msdn.microsoft.com/library/ms724950(v=VS.85).aspx) structure to a [**CALDATETIME**](caldatetime.md) structure.

## Syntax


```C++
BOOL ConvertSystemTimeToCalDateTime(
  _In_  const SYSTEMTIME    lpSysTime,
  _In_        CALID         calId,
  _Out_       LPCALDATETIME lpCalDateTime

);
```



## Parameters

<dl> <dt>

*lpSysTime* \[in\]
</dt> <dd>

Pointer to the [**SYSTEMTIME**](https://msdn.microsoft.com/library/ms724950(v=VS.85).aspx) structure to convert.

</dd> <dt>

*calId* \[in\]
</dt> <dd>

The system [calendar identifier](calendar-identifiers.md) to use in the conversion.

</dd> <dt>

*lpCalDateTime* \[out\]
</dt> <dd>

Pointer to the equivalent [**CALDATETIME**](caldatetime.md) structure.

</dd> </dl>

## Return value

Returns **TRUE** if successful or **FALSE** otherwise. To get extended error information, the application can call [**GetLastError**](https://msdn.microsoft.com/library/ms679360(v=VS.85).aspx), which can return one of the following error codes:

-   ERROR\_INVALID\_PARAMETER. Any of the parameter values was invalid.

## Remarks

The earliest date supported by this function is January 1, 1601.

This function does not have an associated header file or library file. The application can call [**LoadLibrary**](https://msdn.microsoft.com/library/ms684175(v=VS.85).aspx) with the DLL name (Kernel32.dll) to obtain a module handle. It can then call [**GetProcAddress**](https://msdn.microsoft.com/library/ms683212(v=VS.85).aspx) with the module handle and the name of this function to get the function address.

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

[Retrieving Time and Date Information](time-and-date.md)
</dt> </dl>

 

 




