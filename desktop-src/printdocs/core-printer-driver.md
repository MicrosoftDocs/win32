---
description: Represents a printer driver on which other printer drivers depend.
ms.assetid: b03f9ac1-7ad2-4aee-b496-e1ee15ba7d38
title: CORE_PRINTER_DRIVER structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CORE_PRINTER_DRIVER
- _CORE_PRINTER_DRIVERA
- _CORE_PRINTER_DRIVERW
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# CORE\_PRINTER\_DRIVER structure

Represents a printer driver on which other printer drivers depend.

## Syntax


```C++
typedef struct _CORE_PRINTER_DRIVER {
  GUID      CoreDriverGUID;
  FILETIME  ftDriverDate;
  DWORDLONG dwlDriverVersion;
  TCHAR     szPackageID[MAX_PATH];
} CORE_PRINTER_DRIVER, *PCORE_PRINTER_DRIVER;
```



## Members

<dl> <dt>

**CoreDriverGUID**
</dt> <dd>

The GUID of the core printer driver.

</dd> <dt>

**ftDriverDate**
</dt> <dd>

The date and time of the latest version of the core printer driver.

</dd> <dt>

**dwlDriverVersion**
</dt> <dd>

The version ID of the latest version of the core printer driver.

</dd> <dt>

**szPackageID\[MAX\_PATH\]**
</dt> <dd>

The path to the driver package that contains the core printer driver.

</dd> </dl>

## Remarks

This structure can represent a manufacturer's base driver on which the drivers for various printer models are dependent.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_CORE\_PRINTER\_DRIVERW** (Unicode) and **\_CORE\_PRINTER\_DRIVERA** (ANSI)<br/>                 |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> </dl>

 

 




