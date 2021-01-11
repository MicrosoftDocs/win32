---
description: The GetForm function retrieves information about a specified form.
ms.assetid: 10b25748-6d7c-46ab-bd2c-9b6126a1d7d1
title: GetForm function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetForm
- GetFormA
- GetFormW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# GetForm function

The **GetForm** function retrieves information about a specified form.

## Syntax


```C++
BOOL GetForm(
  _In_  HANDLE  hPrinter,
  _In_  LPTSTR  pFormName,
  _In_  DWORD   Level,
  _Out_ LPBYTE  pForm,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pcbNeeded
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*pFormName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the form. To get the names of the forms supported by the printer, call the [**EnumForms**](enumforms.md) function.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The version of the structure to which *pForm* points. This value must be 1 or 2.

</dd> <dt>

*pForm* \[out\]
</dt> <dd>

A pointer to an array of bytes that receives the initialized [**FORM\_INFO\_1**](form-info-1.md) or [**FORM\_INFO\_2**](form-info-2.md) structure.

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size, in bytes, of the *pForm* array.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

A pointer to a value that specifies the number of bytes copied if the function succeeds or the number of bytes required if *cbBuf* is too small.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

If the caller is remote, and the *Level* is 2, the **StringType** value of the returned [**FORM\_INFO\_2**](form-info-2.md) will always be STRING\_LANGPAIR.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **GetFormW** (Unicode) and **GetFormA** (ANSI)<br/>                                                 |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddForm**](addform.md)
</dt> <dt>

[**DeleteForm**](deleteform.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**SetForm**](setform.md)
</dt> </dl>

 

 




