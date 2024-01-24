---
description: The DeletePort function displays a dialog box that allows the user to delete a port name.
ms.assetid: 5f5788c2-c781-4106-abd2-98556d0a22de
title: DeletePort function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeletePort
- DeletePortA
- DeletePortW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# DeletePort function

The **DeletePort** function displays a dialog box that allows the user to delete a port name.

## Syntax


```C++
BOOL DeletePort(
  _In_ LPTSTR pName,
  _In_ HWND   hWnd,
  _In_ LPTSTR pPortName
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a zero-terminated string that specifies the name of the server for which the port should be deleted. If this parameter is **NULL**, a local port is deleted.

</dd> <dt>

*hWnd* \[in\]
</dt> <dd>

A handle to the parent window of the port-deletion dialog box.

</dd> <dt>

*pPortName* \[in\]
</dt> <dd>

A pointer to a zero-terminated string that specifies the name of the port that should be deleted.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

An application can retrieve the names of valid ports by calling the [**EnumPorts**](enumports.md) function.

The **DeletePort** function returns an error if a printer is currently connected to the specified port.

The caller of the **DeletePort** function must have SERVER\_ACCESS\_ADMINISTER access to the server to which the port is connected.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **DeletePortW** (Unicode) and **DeletePortA** (ANSI)<br/>                                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddPort**](addport.md)
</dt> <dt>

[**EnumPorts**](enumports.md)
</dt> </dl>

 

 




