---
description: The DeleteForm function removes a form name from the list of supported forms.
ms.assetid: a2d0345f-2469-46ab-935f-777f2b33b621
title: DeleteForm function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeleteForm
- DeleteFormA
- DeleteFormW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# DeleteForm function

The **DeleteForm** function removes a form name from the list of supported forms.

## Syntax


```C++
BOOL DeleteForm(
  _In_ HANDLE hPrinter,
  _In_ LPTSTR pFormName
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

Indicates the open printer handle that this function is to be performed upon. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> <dt>

*pFormName* \[in\]
</dt> <dd>

Pointer to the form name to be removed.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

**DeleteForm** can only delete form names that were added by using the [**AddForm**](addform.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **DeleteFormW** (Unicode) and **DeleteFormA** (ANSI)<br/>                                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddForm**](addform.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> </dl>

 

 




