---
description: Retrieves GUID, version, and date of the specified core printer drivers and the path to their packages.
ms.assetid: 98acad48-cd42-4d2b-be58-81c1366f6912
title: GetCorePrinterDrivers function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetCorePrinterDrivers
- GetCorePrinterDriversA
- GetCorePrinterDriversW
api_type: 
- DllExport
api_location: 
- Spoolss.dll
---

# GetCorePrinterDrivers function

Retrieves GUID, version, and date of the specified core printer drivers and the path to their packages.

## Syntax


```C++
HRESULT GetCorePrinterDrivers(
  _In_  LPCTSTR              pszServer,
  _In_  LPCTSTR              pszEnvironment,
  _In_  LPCTSTR              pszzCoreDriverDependencies,
  _In_  DWORD                cCorePrinterDrivers,
  _Out_ PCORE_PRINTER_DRIVER pCorePrinterDrivers
);
```



## Parameters

<dl> <dt>

*pszServer* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the name of the print server. Use **NULL** for the local computer.

</dd> <dt>

*pszEnvironment* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the processor architecture (for example, Windows NT x86). This can be **NULL**.

</dd> <dt>

*pszzCoreDriverDependencies* \[in\]
</dt> <dd>

A pointer to a null-terminated multi-string that specifies the GUIDs of the core printer drivers.

</dd> <dt>

*cCorePrinterDrivers* \[in\]
</dt> <dd>

The number of strings in *pszzCoreDriverDependencies*.

</dd> <dt>

*pCorePrinterDrivers* \[out\]
</dt> <dd>

A pointer to an array of one or more [**CORE\_PRINTER\_DRIVER**](core-printer-driver.md) structures.

</dd> </dl>

## Return value

If the operation succeeds, the return value is S\_OK, otherwise the **HRESULT** will contain an error code.

For more information about COM error codes, see [Error Handling](../com/error-handling-in-com.md).

## Remarks

This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Spoolss.dll</dt> </dl>                    |
| Unicode and ANSI names<br/>   | **GetCorePrinterDriversW** (Unicode) and **GetCorePrinterDriversA** (ANSI)<br/>                     |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> </dl>

 

