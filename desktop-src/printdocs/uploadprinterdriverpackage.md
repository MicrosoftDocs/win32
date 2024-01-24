---
description: Uploads a printer driver to the print servers driver store so that it can be installed by calling InstallPrinterDriverFromPackage.
ms.assetid: dd3b3a3b-8ded-44ae-85dd-e630bc62e898
title: UploadPrinterDriverPackage function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UploadPrinterDriverPackage
- UploadPrinterDriverPackageA
- UploadPrinterDriverPackageW
api_type: 
- DllExport
api_location: 
- Spoolss.dll
---

# UploadPrinterDriverPackage function

Uploads a printer driver to the print server's driver store so that it can be installed by calling [**InstallPrinterDriverFromPackage**](installprinterdriverfrompackage.md).

## Syntax


```C++
HRESULT UploadPrinterDriverPackage(
  _In_    LPCTSTR pszServer,
  _In_    LPCTSTR pszInfPath,
  _In_    LPCTSTR pszEnvironment,
  _In_    DWORD   dwFlags,
  _In_    HWND    hwnd,
  _Out_   LPTSTR  pszDestInfPath,
  _Inout_ PULONG  pcchDestInfPath
);
```



## Parameters

<dl> <dt>

*pszServer* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the name of the print server. Use **NULL** if the server is the local computer.

</dd> <dt>

*pszInfPath* \[in\]
</dt> <dd>

A pointer to a constant ,null-terminated string that specifies the source path to the driver's .inf file.

</dd> <dt>

*pszEnvironment* \[in\]
</dt> <dd>

A pointer to a constant, null-terminated string that specifies the server's processor architecture (for example, Windows NT x86). This can be **NULL**.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This can be any of the following values:



| Value                                                                                                                                                                                     | Meaning                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="UPDP_SILENT_UPLOAD"></span><span id="updp_silent_upload"></span><dl> <dt>**UPDP_SILENT_UPLOAD**</dt> </dl>             | The UI will not be shown during the upload.<br/>                                                                                                             |
| <span id="UPDP_UPLOAD_ALWAYS"></span><span id="updp_upload_always"></span><dl> <dt>**UPDP_UPLOAD_ALWAYS**</dt> </dl>             | The files will be uploaded even if the package is already in the server's driver store.<br/>                                                                 |
| <span id="UPDP_CHECK_DRIVERSTORE"></span><span id="updp_check_driverstore"></span><dl> <dt>**UPDP_CHECK_DRIVERSTORE**</dt> </dl> | The server's driver store will be checked before upload to see if the package is already there. This setting is ignored if UPDP_UPLOAD_ALWAYS is set.<br/> |



 

</dd> <dt>

*hwnd* \[in\]
</dt> <dd>

A handle to the copying user interface.

</dd> <dt>

*pszDestInfPath* \[out\]
</dt> <dd>

A pointer to the destination path, in the driver store, to which the driver's .inf file was copied.

</dd> <dt>

*pcchDestInfPath* \[in, out\]
</dt> <dd>

On input, specifies the size, in characters, of the *pszDestInfPath* buffer. On output, receives the size, in characters, of the path string, including the terminating null character.

</dd> </dl>

## Return value

If the operation succeeds, the return value is S_OK, otherwise the **HRESULT** will contain an error code.

For more information about COM error codes, see [Error Handling](../com/error-handling-in-com.md).

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The driver store is typically either %windir%\\inf or %windir%\\System32\\DriverStore\\FileRepository.

Only one package at a time can be uploaded. If a package is dependent on others, they must be uploaded separately.

Only signed driver packages can be uploaded.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Spoolss.dll</dt> </dl>                    |
| Unicode and ANSI names<br/>   | **UploadPrinterDriverPackageW** (Unicode) and **UploadPrinterDriverPackageA** (ANSI)<br/>           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> </dl>

 

