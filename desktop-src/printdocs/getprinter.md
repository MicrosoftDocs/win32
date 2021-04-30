---
description: The GetPrinter function retrieves information about a specified printer.
ms.assetid: f162edbb-83ee-40c3-8710-9c867301d652
title: GetPrinter function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetPrinter
- GetPrinterA
- GetPrinterW
api_type: 
- DllExport
api_location: 
- Winspool.drv
- Ext-MS-Win-printer-Winspool-l1-1-0.dll
- Ext-MS-Win-printer-Winspool-l1-1-1.dll
- Ext-MS-Win-Printer-WinSpool-l1-1-2.dll
- Ext-MS-Win-Printer-WinSpool-L1-1-3.dll
---

# GetPrinter function

The **GetPrinter** function retrieves information about a specified printer.

## Syntax


```C++
BOOL GetPrinter(
  _In_  HANDLE  hPrinter,
  _In_  DWORD   Level,
  _Out_ LPBYTE  pPrinter,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pcbNeeded
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer for which the function retrieves information. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The level or type of structure that the function stores into the buffer pointed to by *pPrinter*.

This value can be 1, 2, 3, 4, 5, 6, 7, 8 or 9.

</dd> <dt>

*pPrinter* \[out\]
</dt> <dd>

A pointer to a buffer that receives a structure containing information about the specified printer. The buffer must be large enough to receive the structure and any strings or other data to which the structure members point. If the buffer is too small, the *pcbNeeded* parameter returns the required buffer size.

The type of structure is determined by the value of *Level*.



| Level                                                                                                | Structure                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | A [**PRINTER\_INFO\_1**](printer-info-1.md) structure containing general printer information.<br/>                                                                                                        |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | A [**PRINTER\_INFO\_2**](printer-info-2.md) structure containing detailed information about the printer.<br/>                                                                                             |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | A [**PRINTER\_INFO\_3**](printer-info-3.md) structure containing the printer's security information.<br/>                                                                                                 |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | A [**PRINTER\_INFO\_4**](printer-info-4.md) structure containing minimal printer information, including the name of the printer, the name of the server, and whether the printer is remote or local.<br/> |
| <span id="5"></span><dl> <dt>**5**</dt> </dl> | A [**PRINTER\_INFO\_5**](printer-info-5.md) structure containing printer information such as printer attributes and time-out settings.<br/>                                                               |
| <span id="6"></span><dl> <dt>**6**</dt> </dl> | A [**PRINTER\_INFO\_6**](printer-info-6.md) structure specifying the status value of a printer.<br/>                                                                                                      |
| <span id="7"></span><dl> <dt>**7**</dt> </dl> | A [**PRINTER\_INFO\_7**](printer-info-7.md) structure that indicates whether the printer is published in the directory service.<br/>                                                                      |
| <span id="8"></span><dl> <dt>**8**</dt> </dl> | A [**PRINTER\_INFO\_8**](printer-info-8.md) structure specifying the global default printer settings.<br/>                                                                                                |
| <span id="9"></span><dl> <dt>**9**</dt> </dl> | A [**PRINTER\_INFO\_9**](printer-info-9.md) structure specifying the per-user default printer settings.<br/>                                                                                              |



 

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size, in bytes, of the buffer pointed to by *pPrinter*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

A pointer to a variable that the function sets to the size, in bytes, of the printer information. If *cbBuf* is smaller than this value, **GetPrinter** fails, and the value represents the required buffer size. If *cbBuf* is equal to or greater than this value, **GetPrinter** succeeds, and the value represents the number of bytes stored in the buffer.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The **pDevMode** member in the [**PRINTER\_INFO\_2**](printer-info-2.md), [**PRINTER\_INFO\_8**](printer-info-8.md), and [**PRINTER\_INFO\_9**](printer-info-9.md) structures can be **NULL**. When this happens, the printer is unusable until the driver is reinstalled successfully.

For the [**PRINTER\_INFO\_2**](printer-info-2.md) and [**PRINTER\_INFO\_3**](printer-info-3.md) structures that contain a pointer to a security descriptor, the function retrieves only those components of the security descriptor that the caller has permission to read. To retrieve particular security descriptor components, you must specify the necessary access rights when you call the [**OpenPrinter**](openprinter.md) function to retrieve a handle to the printer. The following table shows the access rights required to read the various security descriptor components.



| Access Right                        | Security Descriptor Component                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| READ\_CONTROL<br/>            | Owner<br/> Primary group<br/> Discretionary access-control list (DACL)<br/> |
| ACCESS\_SYSTEM\_SECURITY<br/> | System access-control list (SACL)<br/>                                                  |



 

If you specify level 7, the **dwAction** member of [**PRINTER\_INFO\_7**](printer-info-7.md) returns one of the following values to indicate whether the printer is published in the directory service.



| dwAction value     | Meaning                                                                                                                                                                                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DSPRINT\_PUBLISH   | The printer is published. The **pszObjectGUID** member contains the GUID of the directory services print queue object associated with the printer.                                                                                                       |
| DSPRINT\_UNPUBLISH | The printer is not published.                                                                                                                                                                                                                            |
| DSPRINT\_PENDING   | Indicates that the system is attempting to complete a publish or unpublish operation. If a [**SetPrinter**](setprinter.md) call fails to publish or unpublish a printer, the system makes further attempts to complete the operation in the background. |



 

Starting with Windows Vista, the printer data returned by **GetPrinter** is retrieved from a local cache when *hPrinter* refers to a printer hosted by a print server and there is at least one open connection to the print server. In all other configurations, the printer data is queried from the print server.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **GetPrinterW** (Unicode) and **GetPrinterA** (ANSI)<br/>                                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AbortPrinter**](abortprinter.md)
</dt> <dt>

[**AddPrinter**](addprinter.md)
</dt> <dt>

[**ClosePrinter**](closeprinter.md)
</dt> <dt>

[**DeletePrinter**](deleteprinter.md)
</dt> <dt>

[**EnumPrinters**](enumprinters.md)
</dt> <dt>

[**PRINTER\_INFO\_1**](printer-info-1.md)
</dt> <dt>

[**PRINTER\_INFO\_2**](printer-info-2.md)
</dt> <dt>

[**PRINTER\_INFO\_3**](printer-info-3.md)
</dt> <dt>

[**PRINTER\_INFO\_4**](printer-info-4.md)
</dt> <dt>

[**PRINTER\_INFO\_5**](printer-info-5.md)
</dt> <dt>

[**PRINTER\_INFO\_7**](printer-info-7.md)
</dt> <dt>

[**PRINTER\_INFO\_8**](printer-info-8.md)
</dt> <dt>

[**PRINTER\_INFO\_9**](printer-info-9.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**SetPrinter**](setprinter.md)
</dt> </dl>

 

 




