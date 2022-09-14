---
description: The GetPrinterDataEx function retrieves configuration data for the specified printer or print server.
ms.assetid: 5d9183a7-97cc-46de-848e-e37ce51396eb
title: GetPrinterDataEx function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetPrinterDataEx
- GetPrinterDataExA
- GetPrinterDataExW
api_type: 
- DllExport
api_location: 
- Winspool.drv
- Ext-MS-Win-printer-Winspool-l1-1-1.dll
- Ext-MS-Win-Printer-WinSpool-l1-1-2.dll
- Ext-MS-Win-Printer-WinSpool-L1-1-3.dll
---

# GetPrinterDataEx function

The **GetPrinterDataEx** function retrieves configuration data for the specified printer or print server. **GetPrinterDataEx** can retrieve values that the [**SetPrinterData**](setprinterdata.md) function stored. In addition, **GetPrinterDataEx** can retrieve values that the [**SetPrinterDataEx**](setprinterdataex.md) function stored under a specified key.

## Syntax


```C++
DWORD GetPrinterDataEx(
  _In_  HANDLE  hPrinter,
  _In_  LPCTSTR pKeyName,
  _In_  LPCTSTR pValueName,
  _Out_ LPDWORD pType,
  _Out_ LPBYTE  pData,
  _In_  DWORD   nSize,
  _Out_ LPDWORD pcbNeeded
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer or print server for which the function retrieves configuration data. Use the [**OpenPrinter**](openprinter.md), [**OpenPrinter2**](openprinter2.md), or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*pKeyName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the key containing the value to be retrieved. Use the backslash ( \\ ) character as a delimiter to specify a path that has one or more subkeys.

If *hPrinter* is a handle to a printer and *pKeyName* is **NULL** or an empty string, **GetPrinterDataEx** returns **ERROR\_INVALID\_PARAMETER**.

If *hPrinter* is a handle to a print server, *pKeyName* is ignored.

</dd> <dt>

*pValueName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that identifies the data to retrieve.

For printers, this string specifies the name of a value under the *pKeyName* key.

For print servers, this string is one of the predefined strings listed in the following Remarks section.

</dd> <dt>

*pType* \[out\]
</dt> <dd>

A pointer to a variable that receives the type of data stored in the value. The function returns the type specified in the [**SetPrinterDataEx**](setprinterdataex.md) call when the data was stored. This parameter can be **NULL** if you don't need the information. **GetPrinterDataEx** passes *pType* on as the *lpdwType* parameter of a [**RegQueryValueEx**](/windows/desktop/api/winreg/nf-winreg-regqueryvalueexa) function call.

</dd> <dt>

*pData* \[out\]
</dt> <dd>

A pointer to a buffer that receives the configuration data.

</dd> <dt>

*nSize* \[in\]
</dt> <dd>

The size, in bytes, of the buffer pointed to by *pData*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

A pointer to a variable that receives the size, in bytes, of the configuration data. If the buffer size specified by *nSize* is too small, the function returns **ERROR\_MORE\_DATA**, and *pcbNeeded* indicates the required buffer size.

</dd> </dl>

## Return value

If the function succeeds, the return value is **ERROR\_SUCCESS**.

If the function fails, the return value is an error value.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

**GetPrinterDataEx** retrieves printer-configuration data that was set by the [**SetPrinterDataEx**](setprinterdataex.md) and [**SetPrinterData**](setprinterdata.md) functions.

Calling **GetPrinterDataEx** with the *pKeyName* parameter set to "PrinterDriverData" is equivalent to calling the [**GetPrinterData**](getprinterdata.md) function.

If *hPrinter* is a handle to a print server, *pValueName* can specify one of the following predefined values.



| Value                                                               | Comments                                                                                                                                                                                                                        |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SPLREG\_ALLOW\_USER\_MANAGEFORMS**                                | Windows XP with Service Pack 2 (SP2) and later<br/> Windows Server 2003 with Service Pack 1 (SP1) and later<br/>                                                                                                    |
| **SPLREG\_ARCHITECTURE**                                            |                                                                                                                                                                                                                                 |
| **SPLREG\_BEEP\_ENABLED**                                           |                                                                                                                                                                                                                                 |
| **SPLREG\_DEFAULT\_SPOOL\_DIRECTORY**                               |                                                                                                                                                                                                                                 |
| **SPLREG\_DNS\_MACHINE\_NAME**                                      |                                                                                                                                                                                                                                 |
| **SPLREG\_DS\_PRESENT**                                             | On successful return, *pData* contains 0x0001 if the machine is on a DS domain, 0 otherwise.<br/>                                                                                                                         |
| **SPLREG\_DS\_PRESENT\_FOR\_USER**                                  | On successful return, *pData* contains 0x0001 if the user is logged onto a DS domain, 0 otherwise.<br/>                                                                                                                   |
| **SPLREG\_EVENT\_LOG**                                              |                                                                                                                                                                                                                                 |
| **SPLREG\_MAJOR\_VERSION**                                          |                                                                                                                                                                                                                                 |
| **SPLREG\_MINOR\_VERSION**                                          |                                                                                                                                                                                                                                 |
| **SPLREG\_NET\_POPUP**                                              | Not supported in Windows Server 2003 and later<br/>                                                                                                                                                                       |
| **SPLREG\_NET\_POPUP\_TO\_COMPUTER**                                | On successful return, *pData* contains 1 if job notifications should be sent to the client computer, or 0 if job notifications are to be sent to the user.<br/> Not supported in Windows Server 2003 and later<br/> |
| **SPLREG\_OS\_VERSION**                                             | Windows XP and later<br/>                                                                                                                                                                                                 |
| **SPLREG\_OS\_VERSIONEX**                                           |                                                                                                                                                                                                                                 |
| **SPLREG\_PORT\_THREAD\_PRIORITY\_DEFAULT**                         |                                                                                                                                                                                                                                 |
| **SPLREG\_PORT\_THREAD\_PRIORITY**                                  |                                                                                                                                                                                                                                 |
| **SPLREG\_PRINT\_DRIVER\_ISOLATION\_GROUPS**                        | Windows 7 and later<br/>                                                                                                                                                                                                  |
| **SPLREG\_PRINT\_DRIVER\_ISOLATION\_TIME\_BEFORE\_RECYCLE**         | Windows 7 and later<br/>                                                                                                                                                                                                  |
| **SPLREG\_PRINT\_DRIVER\_ISOLATION\_MAX\_OBJECTS\_BEFORE\_RECYCLE** | Windows 7 and later<br/>                                                                                                                                                                                                  |
| **SPLREG\_PRINT\_DRIVER\_ISOLATION\_IDLE\_TIMEOUT**                 | Windows 7 and later<br/>                                                                                                                                                                                                  |
| **SPLREG\_PRINT\_DRIVER\_ISOLATION\_EXECUTION\_POLICY**             | Windows 7 and later<br/>                                                                                                                                                                                                  |
| **SPLREG\_PRINT\_DRIVER\_ISOLATION\_OVERRIDE\_POLICY**              | Windows 7 and later<br/>                                                                                                                                                                                                  |
| **SPLREG\_REMOTE\_FAX**                                             | On successful return, *pData* contains 0x0001 if the FAX service supports remote clients, 0 otherwise.<br/>                                                                                                               |
| **SPLREG\_RETRY\_POPUP**                                            | On successful return, *pData* contains 1 if server is set to retry pop-up windows for all jobs, or 0 if server does not retry pop-up windows for all jobs.<br/> Not supported in Windows Server 2003 and later<br/> |
| **SPLREG\_SCHEDULER\_THREAD\_PRIORITY**                             |                                                                                                                                                                                                                                 |
| **SPLREG\_SCHEDULER\_THREAD\_PRIORITY\_DEFAULT**                    |                                                                                                                                                                                                                                 |
| **SPLREG\_WEBSHAREMGMT**                                            | Windows Server 2003 and later<br/>                                                                                                                                                                                        |



 

The following values of *pValueName* indicate the pool printing behavior when an error occurs.



| Value                                       | Comments                                                                                                                                                                                              |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SPLREG\_RESTART\_JOB\_ON\_POOL\_ERROR**   | The value of *pData* indicates the time, in seconds, when a job is restarted on another port after an error occurs. This setting is used with **SPLREG\_RESTART\_JOB\_ON\_POOL\_ENABLED**.<br/> |
| **SPLREG\_RESTART\_JOB\_ON\_POOL\_ENABLED** | A nonzero value in *pData* indicates that **SPLREG\_RESTART\_JOB\_ON\_POOL\_ERROR** is enabled.<br/>                                                                                            |



 

The time specified in **SPLREG\_RESTART\_JOB\_ON\_POOL\_ERROR** is a minimum time. The actual time can be longer, depending on the following port monitor settings, which are registry values under this registry key:

**HKLM\\SYSTEM\\CurrentControlSet\\Control\\Print\\Monitors\\<*MonitorName*>\\Ports**

Call the [**RegQueryValueEx**](/windows/win32/api/winreg/nf-winreg-regqueryvalueexa) function to query these values.



| Port monitor setting     | Data type      | Meaning                                                                                                        |
|--------------------------|----------------|----------------------------------------------------------------------------------------------------------------|
| **StatusUpdateEnabled**  | **REG\_DWORD** | If a nonzero value, enables the port monitor to update the spooler with the port status.<br/>            |
| **StatusUpdateInterval** | **REG\_DWORD** | Specifies the interval, in minutes, when the port monitor updates the spooler with the port status.<br/> |



 

If *pKeyName* is one of the predefined Directory Service (DS) keys (see [**SetPrinter**](setprinter.md)) and *pValueName* contains a comma (','), then the portion of *pValueName* before the comma is the value name and the portion of *pValueName* to the right of the comma is the DS Property OID. A subkey called OID is created and a new value that consists of the value name and OID is entered under the OID key. [**SetPrinterDataEx**](setprinterdataex.md) also adds the value name and data under the DS key.

In Windows 7 and later versions of Windows, print jobs that are sent to a print server are rendered on the client by default. The configuration of client-side rendering for a printer can be read by setting *pKeyName* to "PrinterDriverData" and *pValueName* to the setting value in the following table.



| Setting                      | Data type      | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EMFDespoolingSetting**     | **REG\_DWORD** | A value of 0, or if this value is not present in the registry, enables the default client-side rendering of print jobs.<br/> A value of 1 disables client-side rendering of print jobs.<br/>                                                                                                                                                                                                          |
| **ForceClientSideRendering** | **REG\_DWORD** | A value of 0, or if this value is not present in the registry, will cause the print jobs to be rendered on the client. If a print job cannot be rendered on the client, it will be rendered on the server. If a print job cannot be rendered on the server, it will fail.<br/> A value of 1 will render print jobs on the client. If a print job cannot be rendered on the client, it will fail.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **GetPrinterDataExW** (Unicode) and **GetPrinterDataExA** (ANSI)<br/>                               |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**SetPrinterDataEx**](setprinterdataex.md)
</dt> </dl>

 

