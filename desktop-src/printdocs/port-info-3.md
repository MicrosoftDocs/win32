---
description: The PORT\_INFO\_3 structure specifies the status value of a printer port.
ms.assetid: 0939353f-284b-4dbb-89a2-04918c934430
title: PORT_INFO_3 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PORT_INFO_3
- _PORT_INFO_3A
- _PORT_INFO_3W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PORT\_INFO\_3 structure

The **PORT\_INFO\_3** structure specifies the status value of a printer port.

## Syntax


```C++
typedef struct _PORT_INFO_3 {
  DWORD  dwStatus;
  LPTSTR pszStatus;
  DWORD  dwSeverity;
} PORT_INFO_3, *PPORT_INFO_3;
```



## Members

<dl> <dt>

**dwStatus**
</dt> <dd>

The new port status value. This value is used only if the **pszStatus** member is **NULL**.

This member can be one of the following values.



| Value                            | Meaning                                             |
|----------------------------------|-----------------------------------------------------|
| 0                                | Clears the printer port status.                     |
| PORT\_STATUS\_OFFLINE            | The port's printer is offline.                      |
| PORT\_STATUS\_PAPER\_JAM         | The port's printer has a paper jam.                 |
| PORT\_STATUS\_PAPER\_OUT         | The port's printer is out of paper.                 |
| PORT\_STATUS\_OUTPUT\_BIN\_FULL  | The port's printer's output bin is full.            |
| PORT\_STATUS\_PAPER\_PROBLEM     | The port's printer has a paper problem.             |
| PORT\_STATUS\_NO\_TONER          | The port's printer is out of toner.                 |
| PORT\_STATUS\_DOOR\_OPEN         | The door of the port's printer is open.             |
| PORT\_STATUS\_USER\_INTERVENTION | The port's printer requires user intervention.      |
| PORT\_STATUS\_OUT\_OF\_MEMORY    | The port's printer is out of memory.                |
| PORT\_STATUS\_TONER\_LOW         | The port's printer is low on toner.                 |
| PORT\_STATUS\_WARMING\_UP        | The port's printer is warming up.                   |
| PORT\_STATUS\_POWER\_SAVE        | The port's printer is in a power-conservation mode. |



 

</dd> <dt>

**pszStatus**
</dt> <dd>

Pointer to a new printer port status value string to set. Use this member if there is no suitable status value among those listed for **dwStatus**.

</dd> <dt>

**dwSeverity**
</dt> <dd>

The severity of the port status value.

This member can be one of the following values.



| Value                       | Meaning                                   |
|-----------------------------|-------------------------------------------|
| PORT\_STATUS\_TYPE\_ERROR   | The port status value indicates an error. |
| PORT\_STATUS\_TYPE\_WARNING | The port status value is a warning.       |
| PORT\_STATUS\_TYPE\_INFO    | The port status value is informational.   |



 

</dd> </dl>

## Remarks

When you set a printer port status value with the severity value PORT\_STATUS\_TYPE\_ERROR, the print spooler stops sending jobs to the port. The print spooler does not resume sending jobs to the port until another [**SetPort**](setport.md) call is made to clear the status.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_PORT\_INFO\_3W** (Unicode) and **\_PORT\_INFO\_3A** (ANSI)<br/>                                 |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**SetPort**](setport.md)
</dt> </dl>

 

 




