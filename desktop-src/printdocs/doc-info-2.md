---
description: The DOC\_INFO\_2 structure describes a document that will be printed.
ms.assetid: d62333f3-cc39-4c9b-8fb3-02a2d24bbbad
title: DOC_INFO_2 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DOC_INFO_2
- _DOC_INFO_2A
- _DOC_INFO_2W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# DOC\_INFO\_2 structure

The **DOC\_INFO\_2** structure describes a document that will be printed.

## Syntax


```C++
typedef struct _DOC_INFO_2 {
  LPTSTR pDocName;
  LPTSTR pOutputFile;
  LPTSTR pDatatype;
  DWORD  dwMode;
  DWORD  JobId;
} DOC_INFO_2, *PDOC_INFO_2;
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

**dwMode**
</dt> <dd>

Informs the print spooler of the nature of the data to follow. If this value is zero, the print spooler treats the data sent by subsequent calls to [**WritePrinter**](writeprinter.md) as a normal print job (whether or not it is spooled depends on the printer property). If this value is DI\_CHANNEL, only a communications channel is opened. In this case, the data passed into subsequent calls to **WritePrinter** is sent to the printer or subsequent calls to [**ReadPrinter**](readprinter.md) retrieve data from the printer. This mode remains effective until [**EndDoc**](/windows/desktop/api/Wingdi/nf-wingdi-enddoc) is called.

</dd> <dt>

**JobId**
</dt> <dd>

Reserved for internal use; should be zero.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_DOC\_INFO\_2W** (Unicode) and **\_DOC\_INFO\_2A** (ANSI)<br/>                                   |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**EndDoc**](/windows/desktop/api/Wingdi/nf-wingdi-enddoc)
</dt> <dt>

[**ReadPrinter**](readprinter.md)
</dt> <dt>

[**StartDocPrinter**](startdocprinter.md)
</dt> <dt>

[**WritePrinter**](writeprinter.md)
</dt> </dl>

 

 




