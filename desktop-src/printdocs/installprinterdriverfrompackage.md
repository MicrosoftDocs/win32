---
description: Installs a printer driver from a driver package that is in the print servers driver store.
ms.assetid: 5906d9c6-9fbf-4ec6-81ce-112a9ef6d7c0
title: InstallPrinterDriverFromPackage function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InstallPrinterDriverFromPackage
- InstallPrinterDriverFromPackageA
- InstallPrinterDriverFromPackageW
api_type: 
- DllExport
api_location: 
- Spoolss.dll
---

# InstallPrinterDriverFromPackage function

Installs a printer driver from a driver package that is in the print server's driver store.

## Syntax


```C++
HRESULT InstallPrinterDriverFromPackage(
  _In_ LPCTSTR pszServer,
  _In_ LPCTSTR pszInfPath,
  _In_ LPCTSTR pszDriverName,
  _In_ LPCTSTR pszEnvironment,
  _In_ DWORD   dwFlags
);
```



## Parameters

<dl> <dt>

*pszServer* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the name of the print server. **NULL** means the local computer.

</dd> <dt>

*pszInfPath* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the driver store path to the print driver's .inf file. **NULL** means the driver is in an inf file that shipped with Windows.

</dd> <dt>

*pszDriverName* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the name of the driver.

</dd> <dt>

*pszEnvironment* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the processor architecture (for example, Windows NT x86). This can be **NULL**.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This can only be 0 or IPDFP\_COPY\_ALL\_FILES. A value of 0 means that the printer driver must be added and any files in the printer driver directory that are newer than corresponding files currently in use must be copied. A value of IPDFP\_COPY\_ALL\_FILES means the printer driver and all the files in the printer driver directory must be added. The file time stamps are ignored when *dwFlags* has a value of IPDFP\_COPY\_ALL\_FILES.

</dd> </dl>

## Return value

If the operation succeeds, the return value is S\_OK, otherwise the **HRESULT** will contain an error code.

For more information about COM error codes, see [Error Handling](../com/error-handling-in-com.md).

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The driver store is typically either %windir%\\inf or %windir%\\System32\\DriverStore\\FileRepository.

**InstallPrinterDriverFromPackage** also installs other files in the package, such as color profiles and print processors.

Users must have printer administration rights to install either on a remote computer or on the local computer when the user is logged in with Terminal Services.

Only signed packages can be installed on a remote computer.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Spoolss.dll</dt> </dl>                    |
| Unicode and ANSI names<br/>   | **InstallPrinterDriverFromPackageW** (Unicode) and **InstallPrinterDriverFromPackageA** (ANSI)<br/> |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> </dl>

 

