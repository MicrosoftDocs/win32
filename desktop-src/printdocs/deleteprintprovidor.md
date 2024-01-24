---
description: The DeletePrintProvidor function removes a print provider added by the AddPrintProvidor function.
ms.assetid: b7104f9a-111c-4904-a355-063bb4cc81f1
title: DeletePrintProvidor function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeletePrintProvidor
- DeletePrintProvidorA
- DeletePrintProvidorW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# DeletePrintProvidor function

The **DeletePrintProvidor** function removes a print provider added by the [**AddPrintProvidor**](addprintprovidor.md) function.

## Syntax


```C++
BOOL DeletePrintProvidor(
  _In_ LPTSTR pName,
  _In_ LPTSTR pEnvironment,
  _In_ LPTSTR pPrintProviderName
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

Reserved; must be **NULL**.

</dd> <dt>

*pEnvironment* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the environment from which the provider is to be removed (for example, Windows NT x86, Windows IA64, or Windows x64). If this parameter is **NULL**, the provider is removed from the current environment of the calling application and client machine (not of the destination application and print server). **NULL** is the recommended value because it provides maximum portability.

</dd> <dt>

*pPrintProviderName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the provider to be removed.

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
| Unicode and ANSI names<br/>   | **DeletePrintProvidorW** (Unicode) and **DeletePrintProvidorA** (ANSI)<br/>                         |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddPrintProvidor**](addprintprovidor.md)
</dt> </dl>

 

 




