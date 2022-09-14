---
description: The DeletePrinterConnection function deletes a connection to a printer that was established by a call to AddPrinterConnection or ConnectToPrinterDlg.
ms.assetid: 7b056eea-fbd9-4a08-a2dc-7326caeec387
title: DeletePrinterConnection function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeletePrinterConnection
- DeletePrinterConnectionA
- DeletePrinterConnectionW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# DeletePrinterConnection function

The **DeletePrinterConnection** function deletes a connection to a printer that was established by a call to [**AddPrinterConnection**](addprinterconnection.md) or [**ConnectToPrinterDlg**](connecttoprinterdlg.md).

## Syntax


```C++
BOOL DeletePrinterConnection(
  _In_ LPTSTR pName
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

Pointer to a null-terminated string that specifies the name of the printer connection to delete.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The **DeletePrinterConnection** function does not delete any printer driver files that were copied to the server to which the printer is attached.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **DeletePrinterConnectionW** (Unicode) and **DeletePrinterConnectionA** (ANSI)<br/>                 |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddPrinterConnection**](addprinterconnection.md)
</dt> <dt>

[**AddPrinterConnection2**](addprinterconnection2.md)
</dt> <dt>

[**ConnectToPrinterDlg**](connecttoprinterdlg.md)
</dt> </dl>

 

 




