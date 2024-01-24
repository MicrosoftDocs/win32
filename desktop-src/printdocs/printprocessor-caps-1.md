---
description: The PRINTPROCESSOR\_CAPS\_1 structure is the format for the printer capability information that is returned by the GetPrinterData function in the buffer specified by the pData variable.
ms.assetid: 43c568ff-ccc9-4873-b159-ede09b4a7e51
title: PRINTPROCESSOR_CAPS_1 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTPROCESSOR_CAPS_1
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTPROCESSOR\_CAPS\_1 structure

The **PRINTPROCESSOR\_CAPS\_1** structure is the format for the printer capability information that is returned by the [**GetPrinterData**](getprinterdata.md) function in the buffer specified by the *pData* variable.

## Syntax


```C++
typedef struct _PRINTPROCESSOR_CAPS_1 {
  DWORD dwLevel;
  DWORD dwNupOptions;
  DWORD dwPageOrderFlags;
  DWORD dwNumberOfCopies;
} PRINTPROCESSOR_CAPS_1, *PPRINTPROCESSOR_CAPS_1;
```



## Members

<dl> <dt>

**dwLevel**
</dt> <dd>

The structure's version number. This value must be 1.

</dd> <dt>

**dwNupOptions**
</dt> <dd>

A bit mask representing the various numbers of document pages the printer can print on a physical page. The least significant bit represents 1 document page per page, the next bit represents 2 document pages per page, and so on. For example, 0x0000810B indicates the printer supports 1, 2, 4, 9, and 16 document pages per physical page.

</dd> <dt>

**dwPageOrderFlags**
</dt> <dd>

The order in which pages will be printed. This value can be NORMAL\_PRINT, REVERSE\_PRINT, or BOOKLET\_PRINT.

</dd> <dt>

**dwNumberOfCopies**
</dt> <dd>

The maximum number of copies the printer can handle.

</dd> </dl>

## Remarks

Values for all structure members are supplied by the [**GetPrintProcessorCapabilities**](/windows-hardware/drivers/ddi/content/winsplp/nf-winsplp-getprintprocessorcapabilities) function, which is documented in the Windows Driver Kit (WDK).

The spooler calls a print processor's [**GetPrintProcessorCapabilities**](/windows-hardware/drivers/ddi/content/winsplp/nf-winsplp-getprintprocessorcapabilities) function when an application calls [**GetPrinterData**](getprinterdata.md), specifying a value name with a format of PrintProcCaps\_*datatype*, where *datatype* is the name of an input data type.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**GetPrinterData**](getprinterdata.md)
</dt> </dl>

 

