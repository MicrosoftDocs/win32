---
description: The DeletePrinter function deletes the specified printer object.
ms.assetid: 04d9c073-b795-4307-ba89-d4984bc5b354
title: DeletePrinter function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeletePrinter
api_type: 
- DllExport
api_location: 
- Spoolss.dll
---

# DeletePrinter function

The **DeletePrinter** function deletes the specified printer object.

## Syntax


```C++
BOOL DeletePrinter(
  _Inout_ HANDLE hPrinter
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in, out\]
</dt> <dd>

Handle to a printer object that will be deleted. Use the [**OpenPrinter**](openprinter.md) or [**AddPrinter**](addprinter.md) function to retrieve a printer handle.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

If there are print jobs remaining to be processed for the specified printer, **DeletePrinter** marks the printer for pending deletion, and then deletes it when all the print jobs have been printed. No print jobs can be added to a printer that is marked for pending deletion.

A printer marked for pending deletion cannot be held, but its print jobs can be held, resumed, and restarted. If the printer is held and there are jobs for the printer, **DeletePrinter** fails with ERROR\_ACCESS\_DENIED.

Note that **DeletePrinter** does not close the handle that is passed to it. Thus, the application must still call [**ClosePrinter**](closeprinter.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Spoolss.dll</dt> </dl>                    |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddPrinter**](addprinter.md)
</dt> <dt>

[**EnumPrinters**](enumprinters.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> </dl>

 

 




