---
description: Adds a connection to the specified printer for the current user and specifies connection details.
ms.assetid: 5ae98157-5978-449e-beb1-4787110925fa
title: AddPrinterConnection2 function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AddPrinterConnection2
- AddPrinterConnection2W
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# AddPrinterConnection2 function

Adds a connection to the specified printer for the current user and specifies connection details.

## Syntax


```C++
BOOL AddPrinterConnection2(
  _In_ HWND    hWnd,
  _In_ LPCTSTR pszName,
       DWORD   dwLevel,
  _In_ PVOID   pConnectionInfo
);
```



## Parameters

<dl> <dt>

*hWnd* \[in\]
</dt> <dd>

A handle to the parent window in which the dialog box will be displayed if the print system must download a printer driver from the print server for this connection.

</dd> <dt>

*pszName* \[in\]
</dt> <dd>

A pointer to a constant null-terminated string specifying the name of the printer to which the current user wishes to connect.

</dd> <dt>

*dwLevel* 
</dt> <dd>

The version of the structure pointed to by *pConnectionInfo*. Currently, only level 1 is defined so the value of *dwLevel* must be 1.

</dd> <dt>

*pConnectionInfo* \[in\]
</dt> <dd>

A pointer to a [**PRINTER\_CONNECTION\_INFO\_1**](printer-connection-info-1.md) structure. See the Remarks section for more about this parameter.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero. For extended error information, call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

When Windows Vista makes a connection to a printer, it may need to copy printer driver files from the server to which the printer is attached. If the user does not have permission to copy files to the appropriate location, the **AddPrinterConnection2** function fails and [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns ERROR\_ACCESS\_DENIED.

If the printer driver files must be copied from the print server but cannot be copied silently due to the group policies that are in effect and PRINTER\_CONNECTION\_NO\_UI is set in *pConnectionInfo->dwFlags*, no dialog boxes will be displayed and the call will fail.

If the local printer driver can be used to render print jobs for this printer and the version of the local driver must not match the version of the printer driver on the server, set PRINTER\_CONNECTION\_MISMATCH in *pConnectionInfo->dwFlags* and assign the pointer to a string variable that contains the path to the local printer driver to *pConnectionInfo->pszDriverName*.

A printer connection that is established by calling **AddPrinterConnection2** will be enumerated when [**EnumPrinters**](enumprinters.md) is called with *dwType* set to PRINTER\_ENUM\_CONNECTION.

The ANSI version of this function, **AddPrinterConnection2A**, is not supported and returns **ERROR\_NOT\_SUPPORTED**.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **AddPrinterConnection2W** (Unicode)<br/>                                                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**ConnectToPrinterDlg**](connecttoprinterdlg.md)
</dt> <dt>

[**EnumPrinters**](enumprinters.md)
</dt> <dt>

[**DeletePrinterConnection**](deleteprinterconnection.md)
</dt> </dl>

 

