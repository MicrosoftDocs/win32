---
description: The DRIVER\_INFO\_6 structure contains printer driver information.
ms.assetid: 9771cbb5-caaa-4b7d-9a96-d24234440bac
title: DRIVER_INFO_6 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DRIVER_INFO_6
- _DRIVER_INFO_6A
- _DRIVER_INFO_6W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# DRIVER\_INFO\_6 structure

The **DRIVER\_INFO\_6** structure contains printer driver information.

## Syntax


```C++
typedef struct _DRIVER_INFO_6 {
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
} DRIVER_INFO_6, *PDRIVER_INFO_6, *LPDRIVER_INFO_6;
```



## Members

<dl> <dt>

**cVersion**
</dt> <dd>

The operating system version for which the driver was written. The supported value is 3.

</dd> <dt>

**pName**
</dt> <dd>

Pointer to a null-terminated string that specifies the name of the driver (for example, QMS 810).

</dd> <dt>

**pEnvironment**
</dt> <dd>

Pointer to a null-terminated string that specifies the environment for which the driver was written (for example, Windows NT x86, Windows IA64, and Windows x64.

</dd> <dt>

**pDriverPath**
</dt> <dd>

Pointer to a null-terminated string that specifies a file name or a full path and file name for the file that contains the device driver (for example, C:\\DRIVERS\\Pscript.dll).

</dd> <dt>

**pDataFile**
</dt> <dd>

Pointer to a null-terminated string that specifies a file name or a full path and file name for the file that contains driver data (for example, C:\\DRIVERS\\Qms810.ppd).

</dd> <dt>

**pConfigFile**
</dt> <dd>

Pointer to a null-terminated string that specifies a file name or a full path and file name for the device driver's configuration dynamic-link library (for example, C:\\DRIVERS\\Pscrptui.dll).

</dd> <dt>

**pHelpFile**
</dt> <dd>

Pointer to a null-terminated string that specifies a file name or a full path and file name for the device driver's help file (for example, C:\\DRIVERS\\Pscrptui.hlp).

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

Version number of the driver. This comes out of the version structure of the driver.

</dd> <dt>

**pszMfgName**
</dt> <dd>

Pointer to a null-terminated string that specifies the manufacturer's name.

</dd> <dt>

**pszOEMUrl**
</dt> <dd>

Pointer to a null-terminated string that specifies the URL for the manufacturer.

</dd> <dt>

**pszHardwareID**
</dt> <dd>

Pointer to a null-terminated string that specifies the hardware ID for the printer driver.

</dd> <dt>

**pszProvider**
</dt> <dd>

Pointer to a null-terminated string that specifies the provider of the printer driver (for example, "Microsoft Windows 2000")

</dd> </dl>

## Remarks

The strings for these members are contained in the .inf file that is used to add the driver.

If you call [**AddPrinterDriver**](addprinterdriver.md) or [**AddPrinterDriverEx**](addprinterdriverex.md) with *Level* not equal to 6, and then you call [**GetPrinterDriver**](getprinterdriver.md) or [**EnumPrinterDrivers**](enumprinterdrivers.md) with *Level* equal to 6, the **DRIVER\_INFO\_6** structure is returned with **pszMfgName**, **pszOEMUrl**, **pszHardwareID**, and **pszProvider** set to **NULL**, **dwlDriverVersion** set to 0, and **ftDriverDate** set to (0,0).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_DRIVER\_INFO\_6W** (Unicode) and **\_DRIVER\_INFO\_6A** (ANSI)<br/>                             |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**AddPrinterDriver**](addprinterdriver.md)
</dt> <dt>

[**AddPrinterDriverEx**](addprinterdriverex.md)
</dt> <dt>

[**EnumPrinterDrivers**](enumprinterdrivers.md)
</dt> <dt>

[**GetPrinterDriver**](getprinterdriver.md)
</dt> </dl>

 

 




