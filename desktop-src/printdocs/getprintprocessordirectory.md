---
description: The GetPrintProcessorDirectory function retrieves the path to the print processor directory on the specified server.
ms.assetid: a2443cfd-e5ba-41c6-aaf4-45051a3d0e26
title: GetPrintProcessorDirectory function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetPrintProcessorDirectory
- GetPrintProcessorDirectoryA
- GetPrintProcessorDirectoryW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# GetPrintProcessorDirectory function

The **GetPrintProcessorDirectory** function retrieves the path to the print processor directory on the specified server.

## Syntax


```C++
BOOL GetPrintProcessorDirectory(
  _In_  LPTSTR  pName,
  _In_  LPTSTR  pEnvironment,
  _In_  DWORD   Level,
  _Out_ LPBYTE  pPrintProcessorInfo,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pcbNeeded
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the server. If this parameter is **NULL**, a local path is returned.

</dd> <dt>

*pEnvironment* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the environment (for example, Windows x86, Windows IA64, or Windows x64). If this parameter is **NULL**, the current environment of the calling application and client machine (not of the destination application and print server) is used.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The structure level. This value must be 1.

</dd> <dt>

*pPrintProcessorInfo* \[out\]
</dt> <dd>

A pointer to a buffer that receives the path. Note that, for operating systems prior to Windows Server 2003 SP 1, the path is in the local format for the server, not the true remote format. For example, the path is given as "%Windir%\\System32\\Spool\\Prtprocs\\%Environment%" instead of "\\\\ServerName\\Print$\\Prtprocs\\%Environment%", even when called for a remote server. For the operating systems Windows Server 2003 SP 1 and later, the true remote path is returned.

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size of the buffer pointed to by *pPrintProcessorInfo*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

A pointer to a value that specifies the number of bytes copied if the function succeeds, or the number of bytes required if *cbBuf* is too small.

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
| Unicode and ANSI names<br/>   | **GetPrintProcessorDirectoryW** (Unicode) and **GetPrintProcessorDirectoryA** (ANSI)<br/>           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddPrintProcessor**](addprintprocessor.md)
</dt> </dl>

 

 




