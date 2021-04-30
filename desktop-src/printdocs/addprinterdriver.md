---
description: The AddPrinterDriver function installs a local or remote printer driver and associates the configuration, data, and driver files.
ms.assetid: 0f762800-f5a5-40ea-8be1-7fd8bda23788
title: AddPrinterDriver function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AddPrinterDriver
- AddPrinterDriverA
- AddPrinterDriverW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# AddPrinterDriver function

The **AddPrinterDriver** function installs a local or remote printer driver and associates the configuration, data, and driver files.

For more flexibility in installing or upgrading printer drivers, use the [**AddPrinterDriverEx**](addprinterdriverex.md) function because it allows strict upgrade, strict downgrade, copying of newer files only, and copying of all files (regardless of the file time stamps).

> [!Note]  
> Installing a printer driver without a driver package is no longer recommended. Use [**InstallPrinterDriverFromPackage**](installprinterdriverfrompackage.md) instead.

 

## Syntax


```C++
BOOL AddPrinterDriver(
  _In_ LPTSTR pName,
  _In_ DWORD  Level,
  _In_ LPBYTE pDriverInfo
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the server on which the driver should be installed.

If *pName* is **NULL**, the driver will be installed locally.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The version of the structure to which *pDriverInfo* points.

This value can be 2, 3, 4, 6, or 8.

</dd> <dt>

*pDriverInfo* \[in\]
</dt> <dd>

A pointer to a structure containing printer driver information. This depends on the value of *Level*.



| Value | Printer Drive Structure                  |
|-------|------------------------------------------|
| 2     | [**DRIVER\_INFO\_2**](driver-info-2.md) |
| 3     | [**DRIVER\_INFO\_3**](driver-info-3.md) |
| 4     | [**DRIVER\_INFO\_4**](driver-info-4.md) |
| 6     | [**DRIVER\_INFO\_6**](driver-info-6.md) |
| 8     | [**DRIVER\_INFO\_8**](driver-info-8.md) |



 

If the **pEnvironment** member of the structure pointed to by *pDriverInfo* is **NULL**, the current environment of the caller/client (not of the destination/server) is used.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

The caller must have the [SeLoadDriverPrivilege](/windows/desktop/SecAuthZ/authorization-constants).

Before an application calls the **AddPrinterDriver** function, all files required by the driver must be copied to the system's printer-driver directory. An application can retrieve the name of this directory by calling the [**GetPrinterDriverDirectory**](getprinterdriverdirectory.md) function.

An application can determine which printer drivers are currently installed by calling the [**EnumPrinterDrivers**](enumprinterdrivers.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **AddPrinterDriverW** (Unicode) and **AddPrinterDriverA** (ANSI)<br/>                               |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddPrinterDriverEx**](addprinterdriverex.md)
</dt> <dt>

[**DRIVER\_INFO\_2**](driver-info-2.md)
</dt> <dt>

[**DRIVER\_INFO\_3**](driver-info-3.md)
</dt> <dt>

[**DRIVER\_INFO\_4**](driver-info-4.md)
</dt> <dt>

[**DRIVER\_INFO\_6**](driver-info-6.md)
</dt> <dt>

[**EnumPrinterDrivers**](enumprinterdrivers.md)
</dt> <dt>

[**GetPrinterDriverDirectory**](getprinterdriverdirectory.md)
</dt> </dl>

 

