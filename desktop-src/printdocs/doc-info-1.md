---
description: The DOC\_INFO\_1 structure describes a document that will be printed.
ms.assetid: 142d988b-dd74-4312-8b27-331a7ec70344
title: DOC_INFO_1 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DOC_INFO_1
- _DOC_INFO_1A
- _DOC_INFO_1W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# DOC\_INFO\_1 structure

The **DOC\_INFO\_1** structure describes a document that will be printed.

## Syntax


```C++
typedef struct _DOC_INFO_1 {
  LPTSTR pDocName;
  LPTSTR pOutputFile;
  LPTSTR pDatatype;
} DOC_INFO_1;
```



## Members

<dl> <dt>

**pDocName**
</dt> <dd>

Pointer to a null-terminated string that specifies the name of the document.

</dd> <dt>

**pOutputFile**
</dt> <dd>

Pointer to a null-terminated string that specifies the name of an output file. To print to a printer, set this to **NULL**.

</dd> <dt>

**pDatatype**
</dt> <dd>

Pointer to a null-terminated string that identifies the type of data used to record the document.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_DOC\_INFO\_1W** (Unicode) and **\_DOC\_INFO\_1A** (ANSI)<br/>                                   |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**StartDocPrinter**](startdocprinter.md)
</dt> </dl>

 

 




