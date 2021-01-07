---
description: Contains printer driver information.
ms.assetid: 6237def2-ffd4-4d93-b3a4-56f225793457
title: DRIVER_INFO_8 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DRIVER_INFO_8
- _DRIVER_INFO_8A
- _DRIVER_INFO_8W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# DRIVER\_INFO\_8 structure

Contains printer driver information.

## Syntax


```C++
typedef struct _DRIVER_INFO_8 {
  DWORD     cVersion;
  LPTSTR    pName;
  LPTSTR    pEnvironment;
  LPTSTR    pDriverPath;
  LPTSTR    pDataFile;
  LPTSTR    pConfigFile;
  LPTSTR    pHelpFile;
  LPTSTR    pDependentFiles;
  LPTSTR    pMonitorName;
  LPTSTR    pDefaultDataType;
  LPTSTR    pszzPreviousNames;
  FILETIME  ftDriverDate;
  DWORDLONG dwlDriverVersion;
  LPTSTR    pszMfgName;
  LPTSTR    pszOEMUrl;
  LPTSTR    pszHardwareID;
  LPTSTR    pszProvider;
  LPTSTR    pszPrintProcessor;
  LPTSTR    pszVendorSetup;
  LPTSTR    pszzColorProfiles;
  LPTSTR    pszInfPath;
  DWORD     dwPrinterDriverAttributes;
  LPTSTR    pszzCoreDriverDependencies;
  FILETIME  ftMinInboxDriverVerDate;
  DWORDLONG dwlMinInboxDriverVerVersion;
} DRIVER_INFO_8, *PDRIVER_INFO_8, *LPDRIVER_INFO_8;
```



## Members

<dl> <dt>

**cVersion**
</dt> <dd>

The operating system version for which the driver was written. The supported value is 3.

</dd> <dt>

**pName**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the driver (for example, QMS 810).

</dd> <dt>

**pEnvironment**
</dt> <dd>

A pointer to a null-terminated string that specifies the environment for which the driver was written (for example, Windows x86, Windows IA64, and Windows x64.

</dd> <dt>

**pDriverPath**
</dt> <dd>

A pointer to a null-terminated string that specifies a file name or a full path and file name for the file that contains the device driver (for example, C:\\DRIVERS\\Pscript.dll).

</dd> <dt>

**pDataFile**
</dt> <dd>

A pointer to a null-terminated string that specifies a file name or a full path and file name for the file that contains driver data (for example, C:\\DRIVERS\\Qms810.ppd).

</dd> <dt>

**pConfigFile**
</dt> <dd>

A pointer to a null-terminated string that specifies a file name or a full path and file name for the device driver's configuration dynamic-link library (for example, C:\\DRIVERS\\Pscrptui.dll).

</dd> <dt>

**pHelpFile**
</dt> <dd>

A pointer to a null-terminated string that specifies a file name or a full path and file name for the device driver's help file (for example, C:\\DRIVERS\\Pscrptui.hlp).

</dd> <dt>

**pDependentFiles**
</dt> <dd>

A pointer to a MultiSZ buffer that contains a sequence of null-terminated strings. Each null-terminated string in the buffer contains the name of a file the driver depends on. The sequence of strings is terminated by an empty, zero-length string. If **pDependentFiles** is not **NULL** and does not contain any file names, it will point to a buffer that contains two empty strings.

</dd> <dt>

**pMonitorName**
</dt> <dd>

A pointer to a null-terminated string that specifies a language monitor (for example, "PJL monitor"). This member can be **NULL** and should be specified only for printers capable of bidirectional communication.

</dd> <dt>

**pDefaultDataType**
</dt> <dd>

A pointer to a null-terminated string that specifies the default data type of the print job (for example, "EMF").

</dd> <dt>

**pszzPreviousNames**
</dt> <dd>

A pointer to a null-terminated string that specifies previous printer driver names that are compatible with this driver. For example, OldName1\\0OldName2\\0\\0.

</dd> <dt>

**ftDriverDate**
</dt> <dd>

The date of the driver package, as coded in the driver files.

</dd> <dt>

**dwlDriverVersion**
</dt> <dd>

The version number of the driver. This comes from the version structure of the driver.

</dd> <dt>

**pszMfgName**
</dt> <dd>

A pointer to a null-terminated string that specifies the manufacturer's name.

</dd> <dt>

**pszOEMUrl**
</dt> <dd>

A pointer to a null-terminated string that specifies the URL for the manufacturer.

</dd> <dt>

**pszHardwareID**
</dt> <dd>

A pointer to a null-terminated string that specifies the hardware ID for the printer driver.

</dd> <dt>

**pszProvider**
</dt> <dd>

A pointer to a null-terminated string that specifies the provider of the printer driver (for example, "Microsoft Windows 2000").

</dd> <dt>

**pszPrintProcessor**
</dt> <dd>

A pointer to a null-terminated string that specifies the print processor (for example, "WinPrint").

</dd> <dt>

**pszVendorSetup**
</dt> <dd>

A pointer to a null-terminated string that specifies the vendor's driver setup DLL and entry point.

</dd> <dt>

**pszzColorProfiles**
</dt> <dd>

A pointer to a null-terminated string that specifies the color profiles associated with the driver.

</dd> <dt>

**pszInfPath**
</dt> <dd>

A pointer to a null-terminated string that specifies the path to the driver's .inf file in the driver store. (See Remarks.) This must be **NULL** if the DRIVER\_INFO\_8 is being passed to [**AddPrinterDriver**](addprinterdriver.md) or [**AddPrinterDriverEx**](addprinterdriverex.md).

</dd> <dt>

**dwPrinterDriverAttributes**
</dt> <dd>

Attribute flags for printer drivers. This must be 0 if the DRIVER\_INFO\_8 is being passed to [**AddPrinterDriver**](addprinterdriver.md) or [**AddPrinterDriverEx**](addprinterdriverex.md). Otherwise, it can be any combination of the following flags:



| Flag name/value                                                         | Meaning                                                                                                                                                                                                                                                                                                                                             | Minimum OS                                             |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| PRINTER\_DRIVER\_PACKAGE\_AWARE<br/> 0x00000001<br/>        | The printer driver is part of a driver package.                                                                                                                                                                                                                                                                                                     | Windows Vista                                          |
| PRINTER\_DRIVER\_XPS<br/> 0x00000002<br/>                   | The printer driver supports the Microsoft XPS format described in the [XML Paper Specification: Overview](/previous-versions/windows/hardware/design/dn641615(v=vs.85)), and also in [Product Behavior, section <27>](/openspecs/windows_protocols/ms-rprn/e81cbc09-ab05-4a32-ae4a-8ec57b436c43).                        | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_SANDBOX\_ENABLED<br/> 0x00000004<br/>      | The printer driver is compatible with [printer driver isolation](/openspecs/windows_protocols/ms-rprn/831cd729-be7c-451e-b729-bd8d84ce4d24). For more information, see [Product Behavior, section <28>](/openspecs/windows_protocols/ms-rprn/e81cbc09-ab05-4a32-ae4a-8ec57b436c43). | Windows 7<br/> Windows Server 2008 R2<br/> |
| PRINTER\_DRIVER\_CLASS<br/> 0x00000008<br/>                 | The printer driver is a [class printer driver](/openspecs/windows_protocols/ms-rprn/831cd729-be7c-451e-b729-bd8d84ce4d24).                                                                                                                                                                                       | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_DERIVED<br/> 0x00000010<br/>               | The printer driver is a [derived printer driver](/openspecs/windows_protocols/ms-rprn/831cd729-be7c-451e-b729-bd8d84ce4d24).                                                                                                                                                                                   | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_NOT\_SHAREABLE<br/> 0x00000020<br/>        | Printers using this printer driver cannot be shared.                                                                                                                                                                                                                                                                                                | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_CATEGORY\_FAX<br/> 0x00000040<br/>         | The printer driver is intended for use with [fax printers](/openspecs/windows_protocols/ms-rprn/831cd729-be7c-451e-b729-bd8d84ce4d24).                                                                                                                                                                                    | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_CATEGORY\_FILE<br/> 0x00000080<br/>        | The printer driver is intended for use with [file printers](/openspecs/windows_protocols/ms-rprn/831cd729-be7c-451e-b729-bd8d84ce4d24).                                                                                                                                                                                  | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_CATEGORY\_VIRTUAL<br/> 0x00000100<br/>     | The printer driver is intended for use with [virtual printers](/openspecs/windows_protocols/ms-rprn/831cd729-be7c-451e-b729-bd8d84ce4d24).                                                                                                                                                                            | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_CATEGORY\_SERVICE<br/> 0x00000200<br/>     | The printer driver is intended for use with [service printers](/openspecs/windows_protocols/ms-rprn/831cd729-be7c-451e-b729-bd8d84ce4d24).                                                                                                                                                                            | Windows 8<br/> Windows Server 2012<br/>    |
| PRINTER\_DRIVER\_SOFT\_RESET\_REQUIRED<br/> 0x00000400<br/> | Printers that use this printer driver should follow the guidelines outlined in the USB Device Class Definition. For more information, see [Product Behavior, section <36>](/openspecs/windows_protocols/ms-rprn/e81cbc09-ab05-4a32-ae4a-8ec57b436c43)                                                                      | Windows 8<br/> Windows Server 2012<br/>    |



 

</dd> <dt>

**pszzCoreDriverDependencies**
</dt> <dd>

A pointer to a null-terminated multi-string that specifies all the core printer drivers that the driver depends on. This must be **NULL** if the **DRIVER\_INFO\_8** is being passed to [**AddPrinterDriver**](addprinterdriver.md) or [**AddPrinterDriverEx**](addprinterdriverex.md).

</dd> <dt>

**ftMinInboxDriverVerDate**
</dt> <dd>

The earliest allowed date of any drivers that shipped with Windows and on which this driver depends.

</dd> <dt>

**dwlMinInboxDriverVerVersion**
</dt> <dd>

The earliest allowed version of any drivers that shipped with Windows and on which this driver depends.

</dd> </dl>

## Remarks

The strings for these members are contained in the .inf file that is used to add the driver.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_DRIVER\_INFO\_8W** (Unicode) and **\_DRIVER\_INFO\_8A** (ANSI)<br/>                             |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**AddPrinterDriver**](addprinterdriver.md)
</dt> <dt>

[**AddPrinterDriverEx**](addprinterdriverex.md)
</dt> </dl>

 

