---
description: The EnumPrinterDrivers function enumerates the printer drivers installed on a specified printer server.
ms.assetid: fa3d8cf4-70bc-4362-833e-e4217ed5d43b
title: EnumPrinterDrivers function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnumPrinterDrivers
- EnumPrinterDriversA
- EnumPrinterDriversW
api_type: 
- DllExport
api_location: 
- Winspool.drv
- Ext-MS-Win-Printer-WinSpool-L1-1-3.dll
---

# EnumPrinterDrivers function

The **EnumPrinterDrivers** function enumerates the printer drivers installed on a specified printer server.

## Syntax


```C++
BOOL EnumPrinterDrivers(
  _In_  LPTSTR  pName,
  _In_  LPTSTR  pEnvironment,
  _In_  DWORD   Level,
  _Out_ LPBYTE  pDriverInfo,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pcbNeeded,
  _Out_ LPDWORD pcReturned
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the server on which the printer drivers are enumerated.

If *pName* is **NULL**, the function enumerates the local printer drivers.

</dd> <dt>

*pEnvironment* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the environment (for example, Windows x86, Windows IA64, Windows x64, or Windows NT R4000). If this parameter is **NULL**, the function uses the current environment of the caller/client (not of the destination/server).

If the *pEnvironment* string specifies "all", **EnumPrinterDrivers** enumerates printer drivers for all platforms installed on the specified server.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The type of information structure returned in the *pDriverInfo* buffer. It can be one of the following.



| Value                                                                                                | Meaning                                             |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | [**DRIVER\_INFO\_1**](driver-info-1.md)<br/> |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | [**DRIVER\_INFO\_2**](driver-info-2.md)<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | [**DRIVER\_INFO\_3**](driver-info-3.md)<br/> |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | [**DRIVER\_INFO\_4**](driver-info-4.md)<br/> |
| <span id="5"></span><dl> <dt>**5**</dt> </dl> | [**DRIVER\_INFO\_5**](driver-info-5.md)<br/> |
| <span id="6"></span><dl> <dt>**6**</dt> </dl> | [**DRIVER\_INFO\_6**](driver-info-6.md)<br/> |
| <span id="8"></span><dl> <dt>**8**</dt> </dl> | [**DRIVER\_INFO\_8**](driver-info-8.md)<br/> |



 

</dd> <dt>

*pDriverInfo* \[out\]
</dt> <dd>

A pointer to a buffer that receives an array of DRIVER\_INFO\_\* structures, as specified by *Level*. Each structure contains data that describes an available printer driver. The buffer must be large enough to receive the array of structures and any strings or other data to which the structure members point.

To determine the required buffer size, call **EnumPrinterDrivers** with *cbBuf* set to zero. **EnumPrinterDrivers** fails, [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns ERROR\_INSUFFICIENT\_BUFFER, and the *pcbNeeded* parameter returns the size, in bytes, of the buffer required to hold the array of structures and their data.

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size, in bytes, of the buffer pointed to by *pDriverInfo*

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of bytes copied to the *pDriverInfo* buffer if the function succeeds. If the buffer is too small, the function fails and the variable receives the number of bytes required.

</dd> <dt>

*pcReturned* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of structures returned in the *pDriverInfo* buffer. This is the number of printer drivers installed on the specified print server.

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
| Unicode and ANSI names<br/>   | **EnumPrinterDriversW** (Unicode) and **EnumPrinterDriversA** (ANSI)<br/>                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddPrinterDriver**](addprinterdriver.md)
</dt> <dt>

[**DRIVER\_INFO\_1**](driver-info-1.md)
</dt> <dt>

[**DRIVER\_INFO\_2**](driver-info-2.md)
</dt> <dt>

[**DRIVER\_INFO\_3**](driver-info-3.md)
</dt> <dt>

[**DRIVER\_INFO\_4**](driver-info-4.md)
</dt> <dt>

[**DRIVER\_INFO\_5**](driver-info-5.md)
</dt> <dt>

[**DRIVER\_INFO\_6**](driver-info-6.md)
</dt> <dt>

[**GetPrinterDriver**](getprinterdriver.md)
</dt> </dl>

 

