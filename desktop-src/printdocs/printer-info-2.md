---
description: The PRINTER\_INFO\_2 structure specifies detailed printer information.
ms.assetid: 944cbfcd-9edf-4b60-a45c-9bb1839f8141
title: PRINTER_INFO_2 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_INFO_2
- _PRINTER_INFO_2A
- _PRINTER_INFO_2W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_INFO\_2 structure

The **PRINTER\_INFO\_2** structure specifies detailed printer information.

## Syntax


```C++
typedef struct _PRINTER_INFO_2 {
  LPTSTR               pServerName;
  LPTSTR               pPrinterName;
  LPTSTR               pShareName;
  LPTSTR               pPortName;
  LPTSTR               pDriverName;
  LPTSTR               pComment;
  LPTSTR               pLocation;
  LPDEVMODE            pDevMode;
  LPTSTR               pSepFile;
  LPTSTR               pPrintProcessor;
  LPTSTR               pDatatype;
  LPTSTR               pParameters;
  PSECURITY_DESCRIPTOR pSecurityDescriptor;
  DWORD                Attributes;
  DWORD                Priority;
  DWORD                DefaultPriority;
  DWORD                StartTime;
  DWORD                UntilTime;
  DWORD                Status;
  DWORD                cJobs;
  DWORD                AveragePPM;
} PRINTER_INFO_2, *PPRINTER_INFO_2;
```



## Members

<dl> <dt>

**pServerName**
</dt> <dd>

A pointer to a null-terminated string identifying the server that controls the printer. If this string is **NULL**, the printer is controlled locally.

</dd> <dt>

**pPrinterName**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the printer.

</dd> <dt>

**pShareName**
</dt> <dd>

A pointer to a null-terminated string that identifies the share point for the printer. (This string is used only if the PRINTER\_ATTRIBUTE\_SHARED constant was set for the **Attributes** member.)

</dd> <dt>

**pPortName**
</dt> <dd>

A pointer to a null-terminated string that identifies the port(s) used to transmit data to the printer. If a printer is connected to more than one port, the names of each port must be separated by commas (for example, "LPT1:,LPT2:,LPT3:").

</dd> <dt>

**pDriverName**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the printer driver.

</dd> <dt>

**pComment**
</dt> <dd>

A pointer to a null-terminated string that provides a brief description of the printer.

</dd> <dt>

**pLocation**
</dt> <dd>

A pointer to a null-terminated string that specifies the physical location of the printer (for example, "Bldg. 38, Room 1164").

</dd> <dt>

**pDevMode**
</dt> <dd>

A pointer to a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure that defines default printer data such as the paper orientation and the resolution.

</dd> <dt>

**pSepFile**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the file used to create the separator page. This page is used to separate print jobs sent to the printer.

</dd> <dt>

**pPrintProcessor**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the print processor used by the printer. You can use the [**EnumPrintProcessors**](enumprintprocessors.md) function to obtain a list of print processors installed on a server.

</dd> <dt>

**pDatatype**
</dt> <dd>

A pointer to a null-terminated string that specifies the data type used to record the print job. You can use the [**EnumPrintProcessorDatatypes**](enumprintprocessordatatypes.md) function to obtain a list of data types supported by a specific print processor.

</dd> <dt>

**pParameters**
</dt> <dd>

A pointer to a null-terminated string that specifies the default print-processor parameters.

</dd> <dt>

**pSecurityDescriptor**
</dt> <dd>

A pointer to a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) structure for the printer. This member may be **NULL**.

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



 

In Windows Server 2003, the following value can also be used.

| Value                  | Meaning                                                                 |
|------------------------|-------------------------------------------------------------------------|
| PRINTER\_ATTRIBUTE\_TS | Indicates the printer is currently connected through a terminal server. |



 

</dd> <dt>

**Priority**
</dt> <dd>

A priority value that the spooler uses to route print jobs.

</dd> <dt>

**DefaultPriority**
</dt> <dd>

The default priority value assigned to each print job.

</dd> <dt>

**StartTime**
</dt> <dd>

The earliest time at which the printer will print a job. This value is expressed as minutes elapsed since 12:00 AM GMT (Greenwich Mean Time).

</dd> <dt>

**UntilTime**
</dt> <dd>

The latest time at which the printer will print a job. This value is expressed as minutes elapsed since 12:00 AM GMT (Greenwich Mean Time).

</dd> <dt>

**Status**
</dt> <dd>

The printer status. This member can be any reasonable combination of the following values.



| Value                               | Meaning                                                          |
|-------------------------------------|------------------------------------------------------------------|
| PRINTER\_STATUS\_BUSY               | The printer is busy.                                             |
| PRINTER\_STATUS\_DOOR\_OPEN         | The printer door is open.                                        |
| PRINTER\_STATUS\_ERROR              | The printer is in an error state.                                |
| PRINTER\_STATUS\_INITIALIZING       | The printer is initializing.                                     |
| PRINTER\_STATUS\_IO\_ACTIVE         | The printer is in an active input/output state                   |
| PRINTER\_STATUS\_MANUAL\_FEED       | The printer is in a manual feed state.                           |
| PRINTER\_STATUS\_NO\_TONER          | The printer is out of toner.                                     |
| PRINTER\_STATUS\_NOT\_AVAILABLE     | The printer is not available for printing.                       |
| PRINTER\_STATUS\_OFFLINE            | The printer is offline.                                          |
| PRINTER\_STATUS\_OUT\_OF\_MEMORY    | The printer has run out of memory.                               |
| PRINTER\_STATUS\_OUTPUT\_BIN\_FULL  | The printer's output bin is full.                                |
| PRINTER\_STATUS\_PAGE\_PUNT         | The printer cannot print the current page.                       |
| PRINTER\_STATUS\_PAPER\_JAM         | Paper is jammed in the printer                                   |
| PRINTER\_STATUS\_PAPER\_OUT         | The printer is out of paper.                                     |
| PRINTER\_STATUS\_PAPER\_PROBLEM     | The printer has a paper problem.                                 |
| PRINTER\_STATUS\_PAUSED             | The printer is paused.                                           |
| PRINTER\_STATUS\_PENDING\_DELETION  | The printer is being deleted.                                    |
| PRINTER\_STATUS\_POWER\_SAVE        | The printer is in power save mode.                               |
| PRINTER\_STATUS\_PRINTING           | The printer is printing.                                         |
| PRINTER\_STATUS\_PROCESSING         | The printer is processing a print job.                           |
| PRINTER\_STATUS\_SERVER\_UNKNOWN    | The printer status is unknown.                                   |
| PRINTER\_STATUS\_TONER\_LOW         | The printer is low on toner.                                     |
| PRINTER\_STATUS\_USER\_INTERVENTION | The printer has an error that requires the user to do something. |
| PRINTER\_STATUS\_WAITING            | The printer is waiting.                                          |
| PRINTER\_STATUS\_WARMING\_UP        | The printer is warming up.                                       |



 

</dd> <dt>

**cJobs**
</dt> <dd>

The number of print jobs that have been queued for the printer.

</dd> <dt>

**AveragePPM**
</dt> <dd>

The average number of pages per minute that have been printed on the printer.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_PRINTER\_INFO\_2W** (Unicode) and **\_PRINTER\_INFO\_2A** (ANSI)<br/>                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea)
</dt> <dt>

[**EnumPrinters**](enumprinters.md)
</dt> <dt>

[**PRINTER\_INFO\_1**](printer-info-1.md)
</dt> <dt>

[**PRINTER\_INFO\_3**](printer-info-3.md)
</dt> <dt>

[**PRINTER\_INFO\_4**](printer-info-4.md)
</dt> <dt>

[**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor)
</dt> </dl>

 

