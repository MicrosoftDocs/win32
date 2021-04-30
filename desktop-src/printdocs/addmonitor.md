---
description: The AddMonitor function installs a local port monitor and links the configuration, data, and monitor files.
ms.assetid: 6a556422-5360-42d2-b177-dba0498c06d8
title: AddMonitor function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AddMonitor
- AddMonitorA
- AddMonitorW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# AddMonitor function

The **AddMonitor** function installs a local port monitor and links the configuration, data, and monitor files.

## Syntax


```C++
BOOL AddMonitor(
  _In_ LPTSTR pName,
  _In_ DWORD  Level,
  _In_ LPBYTE pMonitors
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the server on which the monitor should be installed. For systems that support only local installation of monitors, this string should be **NULL**.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The version of the structure to which *pMonitors* points. This value must be 2.

</dd> <dt>

*pMonitors* \[in\]
</dt> <dd>

A pointer to a [**MONITOR\_INFO\_2**](monitor-info-2.md) structure. If the **pEnvironment** member of the *pMonitors* structure is **NULL**, the current environment of the caller (client), not of the destination (server), is used.

Note that the call will fail if the environment does not match the environment of the server, that is, you can only add a monitor that was written for the architecture of the server.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The caller must have the [SeLoadDriverPrivilege](/windows/desktop/SecAuthZ/authorization-constants).

Before an application calls the **AddMonitor** function, all files required by the monitor must be copied to the SYSTEM32 directory.

To determine the port monitors that are currently installed, call the [**EnumMonitors**](enummonitors.md) function.

To remove a monitor added by **AddMonitor**, call the [**DeleteMonitor**](deletemonitor.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **AddMonitorW** (Unicode) and **AddMonitorA** (ANSI)<br/>                                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**DeleteMonitor**](deletemonitor.md)
</dt> <dt>

[**EnumMonitors**](enummonitors.md)
</dt> <dt>

[**MONITOR\_INFO\_2**](monitor-info-2.md)
</dt> </dl>

 

