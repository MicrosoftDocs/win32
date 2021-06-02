---
description: The ADDJOB\_INFO\_1 structure identifies a print job as well as the directory and file in which an application can store that job.
ms.assetid: de915932-11a7-47e8-9be9-edab76d94189
title: ADDJOB_INFO_1 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ADDJOB_INFO_1
- _ADDJOB_INFO_1A
- _ADDJOB_INFO_1W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# ADDJOB\_INFO\_1 structure

The **ADDJOB\_INFO\_1** structure identifies a print job as well as the directory and file in which an application can store that job.

## Syntax


```C++
typedef struct _ADDJOB_INFO_1 {
  LPTSTR Path;
  DWORD  JobId;
} ADDJOB_INFO_1, *PADDJOB_INFO_1;
```



## Members

<dl> <dt>

**Path**
</dt> <dd>

Pointer to a null-terminated string that contains the path and file name that the application can use to store the print job.

</dd> <dt>

**JobId**
</dt> <dd>

A handle to the print job.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_ADDJOB\_INFO\_1W** (Unicode) and **\_ADDJOB\_INFO\_1A** (ANSI)<br/>                             |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**AddJob**](addjob.md)
</dt> </dl>

 

 




