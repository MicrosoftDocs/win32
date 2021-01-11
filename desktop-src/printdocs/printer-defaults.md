---
description: The PRINTER\_DEFAULTS structure specifies the default data type, environment, initialization data, and access rights for a printer.
ms.assetid: df29c3a6-b1d1-4d40-887d-5ffc032a5871
title: PRINTER_DEFAULTS structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_DEFAULTS
- _PRINTER_DEFAULTSA
- _PRINTER_DEFAULTSW
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_DEFAULTS structure

The **PRINTER\_DEFAULTS** structure specifies the default data type, environment, initialization data, and access rights for a printer.

## Syntax


```C++
typedef struct _PRINTER_DEFAULTS {
  LPTSTR      pDatatype;
  LPDEVMODE   pDevMode;
  ACCESS_MASK DesiredAccess;
} PRINTER_DEFAULTS, *PPRINTER_DEFAULTS;
```



## Members

<dl> <dt>

**pDatatype**
</dt> <dd>

Pointer to a null-terminated string that specifies the default data type for a printer.

</dd> <dt>

**pDevMode**
</dt> <dd>

Pointer to a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure that identifies the default environment and initialization data for a printer.

</dd> <dt>

**DesiredAccess**
</dt> <dd>

Specifies desired access rights for a printer. The [**OpenPrinter**](openprinter.md) function uses this member to set access rights to the printer. These rights can affect the operation of the [**SetPrinter**](setprinter.md) and [**DeletePrinter**](deleteprinter.md) functions. The access rights can be one of the following.



| Value                                       | Meaning                                                                                                                                                                                      |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRINTER\_ACCESS\_ADMINISTER                 | To perform administrative tasks, such as those provided by [**SetPrinter**](setprinter.md).                                                                                                 |
| PRINTER\_ACCESS\_USE                        | To perform basic printing operations.                                                                                                                                                        |
| PRINTER\_ACCESS\_MANAGE\_LIMITED            | To perform administrative tasks, such as those provided by [**SetPrinter**](setprinter.md) and [**SetPrinterData**](setprinterdata.md). This value is available starting from Windows 8.1. |
| PRINTER\_ALL\_ACCESS                        | To perform all administrative tasks and basic printing operations except for SYNCHRONIZE (see [Standard Access Rights](/windows/desktop/SecAuthZ/standard-access-rights) ).                                   |
| generic security values, such as WRITE\_DAC | To allow specific control access rights. See [Standard Access Rights](/windows/desktop/SecAuthZ/standard-access-rights).                                                                                      |



 

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_PRINTER\_DEFAULTSW** (Unicode) and **\_PRINTER\_DEFAULTSA** (ANSI)<br/>                         |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**DeletePrinter**](deleteprinter.md)
</dt> <dt>

[**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**SetPrinter**](setprinter.md)
</dt> </dl>

 

