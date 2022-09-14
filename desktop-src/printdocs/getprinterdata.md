---
description: The GetPrinterData function retrieves configuration data for the specified printer or print server.
ms.assetid: b5a44b27-a4aa-4e58-9a64-05be87d12ab5
title: GetPrinterData function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetPrinterData
- GetPrinterDataA
- GetPrinterDataW
api_type: 
- DllExport
api_location: 
- Winspool.drv
- Ext-MS-Win-Printer-WinSpool-l1-1-2.dll
- Ext-MS-Win-Printer-WinSpool-L1-1-3.dll
---

# GetPrinterData function

The **GetPrinterData** function retrieves configuration data for the specified printer or print server.

In Windows 2000 and later versions of Windows, calling **GetPrinterData** is equivalent to calling [**GetPrinterDataEx**](/windows/desktop/printdocs/getprinterdataex) with the *pKeyName* parameter set to "PrinterDriverData".

## Syntax


```C++
DWORD GetPrinterData(
  _In_  HANDLE  hPrinter,
  _In_  LPTSTR  pValueName,
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

*pValueName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that identifies the data to retrieve.

For printers, this string is the name of a registry value under the printer's "PrinterDriverData" key in the registry.

For print servers, this string is one of the predefined strings listed in the following Remarks section.

</dd> <dt>

*pType* \[out\]
</dt> <dd>

A pointer to a variable that receives a value that indicates the type of data retrieved in *pData*. The function returns the type specified in the [**SetPrinterData**](setprinterdata.md) or [**SetPrinterDataEx**](setprinterdataex.md) call that stored the data. Set this parameter to **NULL** if you don't need the data type.

</dd> <dt>

*pData* \[out\]
</dt> <dd>

A pointer to a buffer that receives the configuration data.

</dd> <dt>

*nSize* \[in\]
</dt> <dd>

The size, in bytes, of the buffer that *pData* points to.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

A pointer to a variable that receives the size, in bytes, of the configuration data. If the buffer size specified by *nSize* is too small, the function returns **ERROR\_MORE\_DATA**, and *pcbNeeded* indicates the required buffer size.

</dd> </dl>

## Return value

If the function succeeds, the return value is **ERROR\_SUCCESS**. If the function fails, the return value is an error value.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

**GetPrinterData** retrieves printer configuration data that was set by the [**SetPrinterDataEx**](setprinterdataex.md) or [**SetPrinterData**](setprinterdata.md) function.

**GetPrinterData** might trigger a Windows call to [**GetPrinterDataFromPort**](/previous-versions//ff550506(v=vs.85)), which might write to the registry. If it does, side effects can occur, such as triggering an update or upgrade printer event ID 20 in the client, if the printer is shared in a network.

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



 

In Windows 7 and later versions of Windows, print jobs that are sent to a print server are rendered on the client by default. The following values configure client-side rendering of a print jobs and can be read if you set the following values in *pValueName*.



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
| Unicode and ANSI names<br/>   | **GetPrinterDataW** (Unicode) and **GetPrinterDataA** (ANSI)<br/>                                   |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**GetPrinterDataEx**](getprinterdataex.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**SetPrinter**](setprinter.md)
</dt> <dt>

[**SetPrinterData**](setprinterdata.md)
</dt> <dt>

[**SetPrinterDataEx**](setprinterdataex.md)
</dt> <dt>

[**PRINTPROCESSOR\_CAPS\_1**](printprocessor-caps-1.md)
</dt> </dl>

 

