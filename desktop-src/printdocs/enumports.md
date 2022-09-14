---
description: The EnumPorts function enumerates the ports that are available for printing on a specified server.
ms.assetid: 72ea0e35-bf26-4c12-9451-8f6941990d82
title: EnumPorts function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnumPorts
- EnumPortsA
- EnumPortsW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# EnumPorts function

The **EnumPorts** function enumerates the ports that are available for printing on a specified server.

## Syntax


```C++
BOOL EnumPorts(
  _In_  LPTSTR  pName,
  _In_  DWORD   Level,
  _Out_ LPBYTE  pPorts,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pcbNeeded,
  _Out_ LPDWORD pcReturned
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the server whose printer ports you want to enumerate.

If *pName* is **NULL**, the function enumerates the local machine's printer ports.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The type of information returned in the *pPorts* buffer. If *Level* is 1, *pPorts* receives an array of [**PORT\_INFO\_1**](port-info-1.md) structures. If *Level* is 2, *pPorts* receives an array of [**PORT\_INFO\_2**](port-info-2.md) structures.

</dd> <dt>

*pPorts* \[out\]
</dt> <dd>

A pointer to a buffer that receives an array of [**PORT\_INFO\_1**](port-info-1.md) or [**PORT\_INFO\_2**](port-info-2.md) structures. Each structure contains data that describes an available printer port. The buffer must be large enough to store the strings pointed to by the structure members.

To determine the required buffer size, call **EnumPorts** with *cbBuf* set to zero. **EnumPorts** fails, [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns ERROR\_INSUFFICIENT\_BUFFER, and the *pcbNeeded* parameter returns the size, in bytes, of the buffer required to hold the array of structures and their data.

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size, in bytes, of the buffer pointed to by *pPorts*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of bytes copied to the *pPorts* buffer. If the buffer is too small, the function fails and the variable receives the number of bytes required.

</dd> <dt>

*pcReturned* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of [**PORT\_INFO\_1**](port-info-1.md) or [**PORT\_INFO\_2**](port-info-2.md) structures returned in the *pPorts* buffer. This is the number of printer ports that are available on the specified server.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The **EnumPorts** function can succeed even if the server specified by *pName* does not have a printer defined.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **EnumPortsW** (Unicode) and **EnumPortsA** (ANSI)<br/>                                             |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddPort**](addport.md)
</dt> <dt>

[**DeletePort**](deleteport.md)
</dt> <dt>

[**PORT\_INFO\_1**](port-info-1.md)
</dt> <dt>

[**PORT\_INFO\_2**](port-info-2.md)
</dt> </dl>

 

