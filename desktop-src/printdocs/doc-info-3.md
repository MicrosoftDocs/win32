---
description: The DOC\_INFO\_3 structure describes a document that will be printed.
ms.assetid: 6e7b6727-da04-4f67-af77-6b51c68a4eb3
title: DOC_INFO_3 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DOC_INFO_3
- _DOC_INFO_3A
- _DOC_INFO_3W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# DOC\_INFO\_3 structure

The **DOC\_INFO\_3** structure describes a document that will be printed.

## Syntax


```C++
typedef struct _DOC_INFO_3 {
  LPTSTR pDocName;
  LPTSTR pOutputFile;
  LPTSTR pDatatype;
  DWORD  dwFlags;
} DOC_INFO_3, *PDOC_INFO_3;
```



## Members

<dl> <dt>

**pDocName**
</dt> <dd>

Pointer to a null-terminated string that specifies the name of the document.

</dd> <dt>

**pOutputFile**
</dt> <dd>

Pointer to a null-terminated string that specifies the name of an output file.

</dd> <dt>

**pDatatype**
</dt> <dd>

Pointer to a null-terminated string that identifies the type of data used to record the document.

</dd> <dt>

**dwFlags**
</dt> <dd>

Flags. Currently, it can be **NULL** or the following.



| Flag                 | Meaning                                                                                                                                          |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| DI\_MEMORYMAP\_WRITE | Causes [**StartDocPrinter**](startdocprinter.md) to not use [**AddJob**](addjob.md) and [**ScheduleJob**](schedulejob.md) for local printing. |



 

</dd> </dl>

## Remarks

The DI\_MEMORYMAP\_WRITE setting in **DOC\_INFO\_3** is an optimization. This allows GDI to map spool files in the application and speed up the recording.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_DOC\_INFO\_3W** (Unicode) and **\_DOC\_INFO\_3A** (ANSI)<br/>                                   |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**AddJob**](addjob.md)
</dt> <dt>

[**ScheduleJob**](schedulejob.md)
</dt> <dt>

[**StartDocPrinter**](startdocprinter.md)
</dt> </dl>

 

 




