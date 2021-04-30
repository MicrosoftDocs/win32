---
description: The AddPort function adds the name of a port to the list of supported ports. The AddPort function is exported by the port monitor.
ms.assetid: 9191d507-9167-4488-a4b4-286590a8a62a
title: AddPort function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AddPort
- AddPortA
- AddPortW
api_type: 
- DllExport
api_location: 
- Spoolss.dll
---

# AddPort function

The **AddPort** function adds the name of a port to the list of supported ports. The **AddPort** function is exported by the port monitor.

## Syntax


```C++
BOOL AddPort(
  _In_ LPTSTR pName,
  _In_ HWND   hWnd,
  _In_ LPTSTR pMonitorName
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a zero-terminated string that specifies the name of the server to which the port is connected. If this parameter is **NULL**, the port is local.

</dd> <dt>

*hWnd* \[in\]
</dt> <dd>

A handle to the parent window of the **AddPort** dialog box.

</dd> <dt>

*pMonitorName* \[in\]
</dt> <dd>

A pointer to a zero-terminated string that specifies the monitor associated with the port.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The **AddPort** function browses the network to find existing ports, and displays a dialog box for the user. The **AddPort** function should validate the port name entered by the user by calling [**EnumPorts**](enumports.md) to ensure that no duplicate names exist.

The caller of the **AddPort** function must have SERVER\_ACCESS\_ADMINISTER access to the server to which the port is connected.

To add a port without displaying a dialog box, call the **XcvData** function instead of **AddPort**. For more information about **XcvData**, see the Microsoft Windows Driver Development Kit (DDK).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Spoolss.dll</dt> </dl>                    |
| Unicode and ANSI names<br/>   | **AddPortW** (Unicode) and **AddPortA** (ANSI)<br/>                                                 |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**DeletePort**](deleteport.md)
</dt> <dt>

[**EnumPorts**](enumports.md)
</dt> <dt>

[**SetPort**](setport.md)
</dt> </dl>

 

 




