---
description: The ConfigurePort function displays the port-configuration dialog box for a port on the specified server.
ms.assetid: a65e9876-d6af-48c2-9e6b-8bd8695db130
title: ConfigurePort function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ConfigurePort
- ConfigurePortA
- ConfigurePortW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# ConfigurePort function

The **ConfigurePort** function displays the port-configuration dialog box for a port on the specified server.

## Syntax


```C++
BOOL ConfigurePort(
  _In_ LPTSTR pName,
  _In_ HWND   hWnd,
  _In_ LPTSTR pPortName
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

Pointer to a null-terminated string that specifies the name of the server on which the specified port exists. If this parameter is **NULL**, the port is local.

</dd> <dt>

*hWnd* \[in\]
</dt> <dd>

Handle to the parent window of the port-configuration dialog box.

</dd> <dt>

*pPortName* \[in\]
</dt> <dd>

Pointer to a null-terminated string that specifies the name of the port to be configured.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

Before calling the **ConfigurePort** function, an application should call the [**EnumPorts**](enumports.md) function to determine valid port names.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **ConfigurePortW** (Unicode) and **ConfigurePortA** (ANSI)<br/>                                     |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**EnumPorts**](enumports.md)
</dt> </dl>

 

 




