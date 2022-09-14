---
description: Represents printer options.
ms.assetid: 7cc3d10c-8bc2-4899-b083-63d802ee16e7
title: PRINTER_OPTIONS structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_OPTIONS
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_OPTIONS structure

Represents printer options.

## Syntax


```C++
typedef struct _PRINTER_OPTIONS {
  UINT  cbSize;
  DWORD dwFlags;
} PRINTER_OPTIONS, *PPRINTER_OPTIONS;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size of the **PRINTER\_OPTIONS** structure.

</dd> <dt>

**dwFlags**
</dt> <dd>

A set of [**PRINTER\_OPTION\_FLAGS**](printer-option-flags.md) that specifies how the handle to a printer returned by [**OpenPrinter2**](openprinter2.md) will be used by other functions.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**OpenPrinter2**](openprinter2.md)
</dt> <dt>

[**PRINTER\_OPTION\_FLAGS**](printer-option-flags.md)
</dt> </dl>

 

 




