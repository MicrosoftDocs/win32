---
description: The PRINTER\_INFO\_5 structure specifies detailed printer information.
ms.assetid: c8599f2e-3b7c-4fde-a340-ca7d3ddaa106
title: PRINTER_INFO_5 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_INFO_5
- _PRINTER_INFO_5A
- _PRINTER_INFO_5W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_INFO\_5 structure

The **PRINTER\_INFO\_5** structure specifies detailed printer information.

## Syntax


```C++
typedef struct _PRINTER_INFO_5 {
  LPTSTR pPrinterName;
  LPTSTR pPortName;
  DWORD  Attributes;
  DWORD  DeviceNotSelectedTimeout;
  DWORD  TransmissionRetryTimeout;
} PRINTER_INFO_5, *PPRINTER_INFO_5;
```



## Members

<dl> <dt>

**pPrinterName**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the printer.

</dd> <dt>

**pPortName**
</dt> <dd>

A pointer to a null-terminated string that identifies the port(s) used to transmit data to the printer. If a printer is connected to more than one port, the names of each port must be separated by commas (for example, "LPT1:,LPT2:,LPT3:").

</dd> <dt>

**Attributes**
</dt> <dd>

The printer attributes. This member can be any reasonable combination of the following values.

| Value                                   | Meaning                                                                                                                                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRINTER\_ATTRIBUTE\_DIRECT              | Job is sent directly to the printer (it is not spooled).                                                                                                                                |
| PRINTER\_ATTRIBUTE\_DO\_COMPLETE\_FIRST | If set and printer is set for print-while-spooling, any jobs that have completed spooling are scheduled to print before jobs that have not completed spooling.                          |
| PRINTER\_ATTRIBUTE\_ENABLE\_DEVQ        | If set, **DevQueryPrint** is called. **DevQueryPrint** may fail if the document and printer setups do not match. Setting this flag causes mismatched documents to be held in the queue. |
| PRINTER\_ATTRIBUTE\_HIDDEN              | Reserved.                                                                                                                                                                               |
| PRINTER\_ATTRIBUTE\_KEEPPRINTEDJOBS     | If set, jobs are kept after they are printed. If unset, jobs are deleted.                                                                                                               |
| PRINTER\_ATTRIBUTE\_LOCAL               | Printer is a local printer.                                                                                                                                                             |
| PRINTER\_ATTRIBUTE\_NETWORK             | Printer is a network printer connection.                                                                                                                                                |
| PRINTER\_ATTRIBUTE\_PUBLISHED           | Indicates whether the printer is published in the directory service.                                                                                                                    |
| PRINTER\_ATTRIBUTE\_QUEUED              | If set, the printer spools and starts printing after the last page is spooled. If not set and PRINTER\_ATTRIBUTE\_DIRECT is not set, the printer spools and prints while spooling.      |
| PRINTER\_ATTRIBUTE\_RAW\_ONLY           | Indicates that only raw data type print jobs can be spooled.                                                                                                                            |
| PRINTER\_ATTRIBUTE\_SHARED              | Printer is shared.                                                                                                                                                                      |



 

In Windows XP and later versions of Windows, the following value can also be used.

| Value                   | Meaning                                                                                                                                                                                           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRINTER\_ATTRIBUTE\_FAX | If set, printer is a fax printer. This can only be set by [**AddPrinter**](addprinter.md), but it can be retrieved by [**EnumPrinters**](enumprinters.md) and [**GetPrinter**](getprinter.md). |



 

In Windows Vista and later versions of Windows, the following values can also be used.

| Value                               | Meaning                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------|
| PRINTER\_ATTRIBUTE\_FRIENDLY\_NAME  | A computer has connected to this printer and given it a friendly name.           |
| PRINTER\_ATTRIBUTE\_MACHINE         | Printer is a per-machine connection.                                             |
| PRINTER\_ATTRIBUTE\_PUSHED\_USER    | The printer was installed by using the Push Printer Connections user policy.     |
| PRINTER\_ATTRIBUTE\_PUSHED\_MACHINE | The printer was installed by using the Push Printer Connections computer policy. |



 

</dd> <dt>

**DeviceNotSelectedTimeout**
</dt> <dd>

This value is not used.

</dd> <dt>

**TransmissionRetryTimeout**
</dt> <dd>

This value is not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_PRINTER\_INFO\_5W** (Unicode) and **\_PRINTER\_INFO\_5A** (ANSI)<br/>                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**EnumPrinters**](enumprinters.md)
</dt> <dt>

[**GetPrinter**](getprinter.md)
</dt> <dt>

[**SetPrinter**](setprinter.md)
</dt> <dt>

[**PRINTER\_INFO\_1**](printer-info-1.md)
</dt> <dt>

[**PRINTER\_INFO\_2**](printer-info-2.md)
</dt> <dt>

[**PRINTER\_INFO\_3**](printer-info-3.md)
</dt> <dt>

[**PRINTER\_INFO\_4**](printer-info-4.md)
</dt> </dl>

 

 




