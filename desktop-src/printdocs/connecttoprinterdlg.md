---
description: The ConnectToPrinterDlg function displays a dialog box that lets users browse and connect to printers on a network.
ms.assetid: 7cb9108b-8b65-4af3-88c8-a69771ed8e3f
title: ConnectToPrinterDlg function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ConnectToPrinterDlg
api_type: 
- DllExport
api_location: 
- WinSpool.drv
---

# ConnectToPrinterDlg function

The **ConnectToPrinterDlg** function displays a dialog box that lets users browse and connect to printers on a network. If the user selects a printer, the function attempts to create a connection to it; if a suitable driver is not installed on the server, the user is given the option of creating a printer locally.

## Syntax


```C++
HANDLE ConnectToPrinterDlg(
  _In_ HWND  hwnd,
  _In_ DWORD Flags
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

Specifies the parent window of the dialog box.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

This parameter is reserved and must be zero.

</dd> </dl>

## Return value

If the function succeeds and the user selects a printer, the return value is a handle to the selected printer.

If the function fails, or the user cancels the dialog box without selecting a printer, the return value is **NULL**.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The **ConnectToPrinterDlg** function attempts to create a connection to the selected printer. However, if the server on which the printer resides does not have a suitable driver installed, the function offers the user the option of creating a printer locally. A calling application can determine whether the function has created a printer locally by calling [**GetPrinter**](getprinter.md) with a [**PRINTER\_INFO\_2**](printer-info-2.md) structure, then examining that structure's **Attributes** member.

An application should call [**DeletePrinter**](deleteprinter.md) to delete a local printer. An application should call [**DeletePrinterConnection**](deleteprinterconnection.md) to delete a connection to a printer.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>WinSpool.drv</dt> </dl>                   |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddPrinterConnection**](addprinterconnection.md)
</dt> <dt>

[**ClosePrinter**](closeprinter.md)
</dt> <dt>

[**DeletePrinter**](deleteprinter.md)
</dt> <dt>

[**DeletePrinterConnection**](deleteprinterconnection.md)
</dt> <dt>

[**GetPrinter**](getprinter.md)
</dt> <dt>

[**PRINTER\_INFO\_2**](printer-info-2.md)
</dt> </dl>

 

 




