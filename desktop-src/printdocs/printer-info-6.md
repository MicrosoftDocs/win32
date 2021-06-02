---
description: The PRINTER\_INFO\_6 specifies the status value of a printer.
ms.assetid: f26fe75b-7c97-47ad-892f-d9e40331fa5d
title: PRINTER_INFO_6 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_INFO_6
- _PRINTER_INFO_6A
- _PRINTER_INFO_6W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_INFO\_6 structure

The **PRINTER\_INFO\_6** specifies the status value of a printer.

## Syntax


```C++
typedef struct _PRINTER_INFO_6 {
  DWORD dwStatus;
} PRINTER_INFO_6, *PPRINTER_INFO_6;
```



## Members

<dl> <dt>

**dwStatus**
</dt> <dd>

The printer status. This member can be any reasonable combination of the following values.



| Value                               | Meaning                                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| PRINTER\_STATUS\_BUSY               | The printer is busy.                                                                                          |
| PRINTER\_STATUS\_DOOR\_OPEN         | The printer door is open.                                                                                     |
| PRINTER\_STATUS\_ERROR              | Not used.                                                                                                     |
| PRINTER\_STATUS\_INITIALIZING       | The printer is initializing.                                                                                  |
| PRINTER\_STATUS\_IO\_ACTIVE         | The printer is in an active input/output state                                                                |
| PRINTER\_STATUS\_MANUAL\_FEED       | The printer is in a manual feed state.                                                                        |
| PRINTER\_STATUS\_NO\_TONER          | The printer is out of toner.                                                                                  |
| PRINTER\_STATUS\_NOT\_AVAILABLE     | The printer is not available for printing.                                                                    |
| PRINTER\_STATUS\_OFFLINE            | The printer is offline.                                                                                       |
| PRINTER\_STATUS\_OUT\_OF\_MEMORY    | The printer has run out of memory.                                                                            |
| PRINTER\_STATUS\_OUTPUT\_BIN\_FULL  | The printer's output bin is full.                                                                             |
| PRINTER\_STATUS\_PAGE\_PUNT         | The printer cannot print the current page.                                                                    |
| PRINTER\_STATUS\_PAPER\_JAM         | Paper is jammed in the printer                                                                                |
| PRINTER\_STATUS\_PAPER\_OUT         | The printer is out of paper.                                                                                  |
| PRINTER\_STATUS\_PAPER\_PROBLEM     | The printer has a paper problem.                                                                              |
| PRINTER\_STATUS\_PAUSED             | The printer is paused.                                                                                        |
| PRINTER\_STATUS\_PENDING\_DELETION  | The printer is pending deletion as a result of a call to the [**DeletePrinter**](deleteprinter.md) function. |
| PRINTER\_STATUS\_POWER\_SAVE        | The printer is in power save mode.                                                                            |
| PRINTER\_STATUS\_PRINTING           | The printer is printing.                                                                                      |
| PRINTER\_STATUS\_PROCESSING         | The printer is processing a command from the [**SetPrinter**](setprinter.md) function.                       |
| PRINTER\_STATUS\_SERVER\_UNKNOWN    | The printer status is unknown.                                                                                |
| PRINTER\_STATUS\_TONER\_LOW         | The printer is low on toner.                                                                                  |
| PRINTER\_STATUS\_USER\_INTERVENTION | The printer has an error that requires the user to do something.                                              |
| PRINTER\_STATUS\_WAITING            | The printer is waiting.                                                                                       |
| PRINTER\_STATUS\_WARMING\_UP        | The printer is warming up.                                                                                    |



 

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_PRINTER\_INFO\_6W** (Unicode) and **\_PRINTER\_INFO\_6A** (ANSI)<br/>                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
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
</dt> <dt>

[**PRINTER\_INFO\_5**](printer-info-5.md)
</dt> </dl>

 

 




