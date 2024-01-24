---
description: Retrieves the path to the specified printer driver package on a print server.
ms.assetid: e88e984b-d2c0-43b4-8f70-b05ec202ab14
title: GetPrinterDriverPackagePath function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetPrinterDriverPackagePath
- GetPrinterDriverPackagePathA
- GetPrinterDriverPackagePathW
api_type: 
- DllExport
api_location: 
- Spoolss.dll
---

# GetPrinterDriverPackagePath function

Retrieves the path to the specified printer driver package on a print server.

## Syntax


```C++
HRESULT GetPrinterDriverPackagePath(
  _In_    LPCTSTR pszServer,
  _In_    LPCTSTR pszEnvironment,
  _In_    LPCTSTR pszLanguage,
  _In_    LPCTSTR pszPackageID,
  _Inout_ LPTSTR  pszDriverPackageCab,
  _In_    DWORD   cchDriverPackageCab,
  _Out_   LPDWORD pcchRequiredSize
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

*pszLanguage* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the [Multilingual User Interface](/windows/desktop/Intl/mui-resource-management) language for the driver being installed. This can be **NULL**.

</dd> <dt>

*pszPackageID* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the ID of the driver package.

</dd> <dt>

*pszDriverPackageCab* \[in, out\]
</dt> <dd>

A pointer to a null-terminated string that specifies the path to the cabinet file for the driver package. This can be **NULL**. See Remarks.

</dd> <dt>

*cchDriverPackageCab* \[in\]
</dt> <dd>

The size, in characters, of the *pszDriverPackageCab* buffer. This can be **NULL**.

</dd> <dt>

*pcchRequiredSize* \[out\]
</dt> <dd>

A pointer to the required size of the *pszDriverPackageCab* buffer.

</dd> </dl>

## Return value

If the operation succeeds, the return value is S\_OK, otherwise the **HRESULT** will contain an error code.

For more information about COM error codes, see [Error Handling](../com/error-handling-in-com.md).

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

To obtain a value for *cchDriverPackageCab*, call the function with **NULL** as the value of *pszDriverPackageCab*. Use the value returned in *pcchRequiredSize* as the value of *cchDriverPackageCab* and call the function again.

The *pszPackageID* is typically obtained from a call to [**GetCorePrinterDrivers**](getcoreprinterdrivers.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Spoolss.dll</dt> </dl>                    |
| Unicode and ANSI names<br/>   | **GetPrinterDriverPackagePathW** (Unicode) and **GetPrinterDriverPackagePathA** (ANSI)<br/>         |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> </dl>

 

