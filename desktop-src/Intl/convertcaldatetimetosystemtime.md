---
Description: Deprecated. Converts a specified CALDATETIME structure to a SYSTEMTIME structure.
ms.assetid: 0c3f602d-62de-4c27-95d9-d35738f3279d
title: ConvertCalDateTimeToSystemTime function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ConvertCalDateTimeToSystemTime function

Deprecated. Converts a specified [**CALDATETIME**](caldatetime.md) structure to a [**SYSTEMTIME**](base.systemtime_str) structure.

## Syntax


```C++
BOOL ConvertCalDateTimeToSystemTime(
  _In_  const LPCALDATETIME lpCalDateTime,
  _Out_       SYSTEMTIME    *lpSysTime
);
```



## Parameters

<dl> <dt>

*lpCalDateTime* \[in\]
</dt> <dd>

Pointer to the [**CALDATETIME**](caldatetime.md) structure to convert.

</dd> <dt>

*lpSysTime* \[out\]
</dt> <dd>

Pointer to the equivalent [**SYSTEMTIME**](base.systemtime_str) structure.

</dd> </dl>

## Return value

Returns **TRUE** if successful or **FALSE** otherwise. To get extended error information, the application can call [**GetLastError**](base.getlasterror), which can return one of the following error codes:

-   ERROR\_DATE\_OUT\_OF\_RANGE. The specified date was out of range.
-   ERROR\_INVALID\_PARAMETER. Any of the parameter values was invalid.

## Remarks

This function does not have an associated header file or library file. The application can call [**LoadLibrary**](base.loadlibrary) with the DLL name (Kernel32.dll) to obtain a module handle. It can then call [**GetProcAddress**](base.getprocaddress) with the module handle and the name of this function to get the function address.

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

 

 




