---
description: Deletes a printer driver package from the driver store.
ms.assetid: a43a94d1-097e-457c-bce9-d4c434ecfa93
title: DeletePrinterDriverPackage function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeletePrinterDriverPackage
- DeletePrinterDriverPackageA
- DeletePrinterDriverPackageW
api_type: 
- DllExport
api_location: 
- Spoolss.dll
---

# DeletePrinterDriverPackage function

Deletes a printer driver package from the driver store.

## Syntax


```C++
HRESULT DeletePrinterDriverPackage(
  _In_ LPCTSTR pszServer,
  _In_ LPCTSTR pszInfPath,
  _In_ LPCTSTR pszEnvironment
);
```



## Parameters

<dl> <dt>

*pszServer* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the name of the print server from which the driver package is being deleted. A **NULL** pointer value means the local computer.

</dd> <dt>

*pszInfPath* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the path to the driver's \*.inf file.

</dd> <dt>

*pszEnvironment* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the processor architecture (for example, Windows NT x86). This can be **NULL**.

</dd> </dl>

## Return value

S\_OK, if the operation succeeds.

E\_ACCESSDENIED, if the package was shipped with Windows.

HRESULT\_CODE(ERROR\_PRINT\_DRIVER\_PACKAGE\_IN\_USE), if the package is being used.

Otherwise the **HRESULT** will contain an error code.

For more information about COM error codes, see [Error Handling](../com/error-handling-in-com.md).

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The driver store is typically %windir%\\inf or %windir%\\System32\\DriverStore\\FileRepository.

A driver package that shipped with Windows cannot be removed with this function.

The user must have printer administration privileges.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Spoolss.dll</dt> </dl>                    |
| Unicode and ANSI names<br/>   | **DeletePrinterDriverPackageW** (Unicode) and **DeletePrinterDriverPackageA** (ANSI)<br/>           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> </dl>

 

