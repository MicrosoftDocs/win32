---
description: The DRIVER\_INFO\_5 structure contains printer driver information.
ms.assetid: 6fb63a9f-5227-46a3-97dc-8de1968e9d63
title: DRIVER_INFO_5 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DRIVER_INFO_5
- _DRIVER_INFO_5A
- _DRIVER_INFO_5W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# DRIVER\_INFO\_5 structure

The **DRIVER\_INFO\_5** structure contains printer driver information.

## Syntax


```C++
typedef struct _DRIVER_INFO_5 {
  DWORD  cVersion;
  LPTSTR pName;
  LPTSTR pEnvironment;
  LPTSTR pDriverPath;
  LPTSTR pDataFile;
  LPTSTR pConfigFile;
  DWORD  dwDriverAttributes;
  DWORD  dwConfigVersion;
  DWORD  dwDriverVersion;
} DRIVER_INFO_5, *PDRIVER_INFO_5;
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

Pointer to a null-terminated string that specifies the environment for which the driver was written (for example, Windows x86, Windows IA64, and Windows x64).

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

**dwDriverAttributes**
</dt> <dd>

Driver attributes, like UMPD/KMPD.

</dd> <dt>

**dwConfigVersion**
</dt> <dd>

Number of times the configuration file for this driver has been upgraded or downgraded since the last spooler restart.

</dd> <dt>

**dwDriverVersion**
</dt> <dd>

Number of times the driver file for this driver has been upgraded or downgraded since the last spooler restart.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_DRIVER\_INFO\_5W** (Unicode) and **\_DRIVER\_INFO\_5A** (ANSI)<br/>                             |



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

 

 




