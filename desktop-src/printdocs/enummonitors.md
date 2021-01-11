---
description: The EnumMonitors function retrieves information about the port monitors installed on the specified server.
ms.assetid: 4d4fbed2-193f-426c-8463-eeb6b1eaf316
title: EnumMonitors function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnumMonitors
- EnumMonitorsA
- EnumMonitorsW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# EnumMonitors function

The **EnumMonitors** function retrieves information about the port monitors installed on the specified server.

## Syntax


```C++
BOOL EnumMonitors(
  _In_  LPTSTR  pName,
  _In_  DWORD   Level,
  _Out_ LPBYTE  pMonitors,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pcbNeeded,
  _Out_ LPDWORD pcReturned
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the server on which the monitors reside. If this parameter is **NULL**, the local monitors are enumerated.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The version of the structure pointed to by *pMonitors*.

This value can be 1 or 2.

</dd> <dt>

*pMonitors* \[out\]
</dt> <dd>

A pointer to a buffer that receives an array of structures. The buffer must be large enough to store the strings referenced by the structure members.

To determine the required buffer size, call **EnumMonitors** with *cbBuf* set to zero. **EnumMonitors** fails, [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns ERROR\_INSUFFICIENT\_BUFFER, and the *pcbNeeded* parameter returns the size, in bytes, of the buffer required to hold the array of structures and their data.

The buffer receives an array of [**MONITOR\_INFO\_1**](monitor-info-1.md) structures if *Level* is 1, or [**MONITOR\_INFO\_2**](monitor-info-2.md) structures if *Level* is 2.

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size, in bytes, of the buffer pointed to by *pMonitors*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of bytes copied if the function succeeds or the number of bytes required if *cbBuf* is too small.

</dd> <dt>

*pcReturned* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of structures that were returned in the buffer pointed to by *pMonitors*.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **EnumMonitorsW** (Unicode) and **EnumMonitorsA** (ANSI)<br/>                                       |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**MONITOR\_INFO\_1**](monitor-info-1.md)
</dt> <dt>

[**MONITOR\_INFO\_2**](monitor-info-2.md)
</dt> </dl>

 

