---
description: The DRIVER\_INFO\_3 structure contains printer driver information.
ms.assetid: ccf87319-0bcf-4f71-8de3-0190459d2b0e
title: DRIVER_INFO_3 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DRIVER_INFO_3
- _DRIVER_INFO_3A
- _DRIVER_INFO_3W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# DRIVER\_INFO\_3 structure

The **DRIVER\_INFO\_3** structure contains printer driver information.

## Syntax


```C++
typedef struct _DRIVER_INFO_3 {
  DWORD  cVersion;
  LPTSTR pName;
  LPTSTR pEnvironment;
  LPTSTR pDriverPath;
  LPTSTR pDataFile;
  LPTSTR pConfigFile;
  LPTSTR pHelpFile;
  LPTSTR pDependentFiles;
  LPTSTR pMonitorName;
  LPTSTR pDefaultDataType;
} DRIVER_INFO_3, *PDRIVER_INFO_3;
```



## Members

<dl> <dt>

**cVersion**
</dt> <dd>

The operating system version for which the driver was written. The supported values are 3 and 4, which represent the V3 and V4 drivers, respectively.

</dd> <dt>

**pName**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the driver (for example, "QMS 810").

</dd> <dt>

**pEnvironment**
</dt> <dd>

A pointer to a null-terminated string that specifies the environment for which the driver was written (for example, Windows x86, Windows IA64, and Windows x64).

</dd> <dt>

**pDriverPath**
</dt> <dd>

A pointer to a null-terminated string that specifies a file name or full path and file name for the file that contains the device driver (for example, "C:\\DRIVERS\\Pscript.dll").

</dd> <dt>

**pDataFile**
</dt> <dd>

A pointer to a null-terminated string that specifies a file name or a full path and file name for the file that contains driver data (for example, "C:\\DRIVERS\\Qms810.ppd").

</dd> <dt>

**pConfigFile**
</dt> <dd>

A pointer to a null-terminated string that specifies a file name or a full path and file name for the device driver's configuration dynamic-link library (for example, "C:\\DRIVERS\\Pscrptui.dll").

</dd> <dt>

**pHelpFile**
</dt> <dd>

A pointer to a null-terminated string that specifies a file name or a full path and file name for the device driver's help file.

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

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_DRIVER\_INFO\_3W** (Unicode) and **\_DRIVER\_INFO\_3A** (ANSI)<br/>                             |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**AddPrinterDriver**](addprinterdriver.md)
</dt> <dt>

[**EnumPrinterDrivers**](enumprinterdrivers.md)
</dt> <dt>

[**GetPrinterDriver**](getprinterdriver.md)
</dt> </dl>

 

 




