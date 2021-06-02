---
description: The AddPrintProvidor function installs a local print provider and links the configuration, data, and provider files.
ms.assetid: f34549c3-0474-48ba-9307-5b36f02dbe1c
title: AddPrintProvidor function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AddPrintProvidor
- AddPrintProvidorA
- AddPrintProvidorW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# AddPrintProvidor function

The **AddPrintProvidor** function installs a local print provider and links the configuration, data, and provider files.

## Syntax


```C++
BOOL AddPrintProvidor(
  _In_ LPTSTR pName,
  _In_ DWORD  Level,
  _In_ LPBYTE pProviderInfo
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the server on which the provider should be installed. For systems that only support local installation of providers, this parameter should be **NULL**.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The level of the structure to which *pProviderInfo* points. It can be one of the following.



| Value                                                                                                | Meaning                                                                            |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Function uses a [**PROVIDOR\_INFO\_1**](providor-info-1.md) structure.<br/> |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Function uses a [**PROVIDOR\_INFO\_2**](providor-info-2.md) structure.<br/> |



 

</dd> <dt>

*pProviderInfo* \[in\]
</dt> <dd>

A pointer to a print provider structure, as indicated by *Level*.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

Before an application calls the **AddPrintProvidor** function, all files required by the provider must be copied to the SYSTEM32 directory.

A provider added by **AddPrintProvidor** may be removed by calling [**DeletePrintProvidor**](deleteprintprovidor.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **AddPrintProvidorW** (Unicode) and **AddPrintProvidorA** (ANSI)<br/>                               |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**DeletePrintProvidor**](deleteprintprovidor.md)
</dt> <dt>

[**PROVIDOR\_INFO\_1**](providor-info-1.md)
</dt> <dt>

[**PROVIDOR\_INFO\_2**](providor-info-2.md)
</dt> </dl>

 

 




