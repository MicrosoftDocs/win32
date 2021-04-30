---
description: The AddPrintProcessor function installs a print processor on the specified server and adds the print-processor name to the list of supported print processors.
ms.assetid: 99899cee-f74d-4405-8ea5-616e3769aba9
title: AddPrintProcessor function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AddPrintProcessor
- AddPrintProcessorA
- AddPrintProcessorW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# AddPrintProcessor function

The **AddPrintProcessor** function installs a print processor on the specified server and adds the print-processor name to the list of supported print processors.

## Syntax


```C++
BOOL AddPrintProcessor(
  _In_ LPTSTR pName,
  _In_ LPTSTR pEnvironment,
  _In_ LPTSTR pPathName,
  _In_ LPTSTR pPrintProcessorName
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the server on which the print processor should be installed. If this parameter is **NULL**, the print processor is installed locally.

</dd> <dt>

*pEnvironment* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the environment (for example, Windows x86, Windows IA64, or Windows x64). If this parameter is **NULL**, the current environment of the caller/client (not of the destination/server) is used.

</dd> <dt>

*pPathName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the file that contains the print processor. This file must be in the system print-processor directory.

</dd> <dt>

*pPrintProcessorName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the print processor.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The caller must have the [SeLoadDriverPrivilege](/windows/desktop/SecAuthZ/authorization-constants).

Before calling the **AddPrintProcessor** function, an application should verify that the file containing the print processor is stored in the system print-processor directory. An application can retrieve the name of the system print-processor directory by calling the [**GetPrintProcessorDirectory**](getprintprocessordirectory.md) function.

An application can determine the name of existing print processors by calling the [**EnumPrintProcessors**](enumprintprocessors.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **AddPrintProcessorW** (Unicode) and **AddPrintProcessorA** (ANSI)<br/>                             |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**EnumPrintProcessors**](enumprintprocessors.md)
</dt> <dt>

[**GetPrintProcessorDirectory**](getprintprocessordirectory.md)
</dt> </dl>

 

