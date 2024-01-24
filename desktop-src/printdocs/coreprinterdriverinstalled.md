---
description: The CorePrinterDriverInstalled function reports whether a core printer driver with a specified GUID, date, and version is installed.
ms.assetid: fb859aca-bb7b-495d-bd38-16ffa084c240
title: CorePrinterDriverInstalled function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CorePrinterDriverInstalled
- CorePrinterDriverInstalledA
- CorePrinterDriverInstalledW
api_type: 
- DllExport
api_location: 
- Spoolss.dll
---

# CorePrinterDriverInstalled function

The **CorePrinterDriverInstalled** function reports whether a core printer driver with a specified GUID, date, and version is installed.

## Syntax


```C++
HRESULT CorePrinterDriverInstalled(
  _In_  LPCTSTR   pszServer,
  _In_  LPCTSTR   pszEnvironment,
  _In_  GUID      CoreDriverGUID,
  _In_  FILETIME  ftDriverDate,
  _In_  DWORDLONG dwlDriverVersion,
  _Out_ BOOL      *pbDriverInstalled
);
```



## Parameters

<dl> <dt>

*pszServer* \[in\]
</dt> <dd>

Pointer to a constant, null-terminated string that specifies the name of the print server. Use **NULL** for the local computer.

</dd> <dt>

*pszEnvironment* \[in\]
</dt> <dd>

Pointer to a constant, null-terminated string that specifies the processor architecture (for example, Windows NT x86). This can be **NULL**.

</dd> <dt>

*CoreDriverGUID* \[in\]
</dt> <dd>

The GUID of the core printer driver.

</dd> <dt>

*ftDriverDate* \[in\]
</dt> <dd>

The date of the core printer driver.

</dd> <dt>

*dwlDriverVersion* \[in\]
</dt> <dd>

The version of the core printer driver.

</dd> <dt>

*pbDriverInstalled* \[out\]
</dt> <dd>

A pointer to **TRUE** if the driver, or a newer version, is installed, **FALSE** otherwise.

</dd> </dl>

## Return value

If the operation succeeds, the return value is S\_OK, otherwise the **HRESULT** will contain an error code.

For more information about COM error codes, see [Error Handling](../com/error-handling-in-com.md).

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Spoolss.dll</dt> </dl>                    |
| Unicode and ANSI names<br/>   | **CorePrinterDriverInstalledW** (Unicode) and **CorePrinterDriverInstalledA** (ANSI)<br/>           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> </dl>

 

