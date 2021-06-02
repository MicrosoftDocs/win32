---
description: Represents printer capability information.
ms.assetid: 70120739-a4e0-4b87-ac7a-40a42fb509ee
title: PRINTPROCESSOR_CAPS_2 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTPROCESSOR_CAPS_2
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTPROCESSOR\_CAPS\_2 structure

Represents printer capability information.

## Syntax


```C++
typedef struct _PRINTPROCESSOR_CAPS_2 {
  DWORD dwLevel;
  DWORD dwNupOptions;
  DWORD dwPageOrderFlags;
  DWORD dwNumberOfCopies;
  DWORD dwNupDirectionCaps;
  DWORD dwNupBorderCaps;
  DWORD dwBookletHandlingCaps;
  DWORD dwDuplexHandlingCaps;
  DWORD dwScalingCaps;
} PRINTPROCESSOR_CAPS_2, *PPRINTPROCESSOR_CAPS_2;
```



## Members

<dl> <dt>

**dwLevel**
</dt> <dd>

A value that indicates the structure's version number.

</dd> <dt>

**dwNupOptions**
</dt> <dd>

A bit mask representing the various numbers of document pages the printer can print on a single side of a physical sheet. The least significant bit represents one document page per side, the next bit represents 2 document pages per side, and so on. For example, 0x0000810B indicates the printer supports 1, 2, 4, 9, and 16 document pages per physical side.

</dd> <dt>

**dwPageOrderFlags**
</dt> <dd>

A flag value that indicates the order in which pages will be printed. It can be **NORMAL\_PRINT**, **REVERSE\_PRINT**, or **BOOKLET\_PRINT**.

</dd> <dt>

**dwNumberOfCopies**
</dt> <dd>

The maximum number of copies the printer can handle.

</dd> <dt>

**dwNupDirectionCaps**
</dt> <dd>

The available patterns when multiple document pages are printed on the same side of a sheet of paper. The possible flags are the following:



| Value                     | Meaning                                                                                             |
|---------------------------|-----------------------------------------------------------------------------------------------------|
| PPCAPS\_RIGHT\_THEN\_DOWN | Pages appear in rows from right to left, each subsequent row below its predecessor.                 |
| PPCAPS\_DOWN\_THEN\_RIGHT | Pages appear in columns from top to bottom, each subsequent column to the right of its predecessor. |
| PPCAPS\_LEFT\_THEN\_DOWN  | Pages appear in rows from left to right, each subsequent row below its predecessor.                 |
| PPCAPS\_DOWN\_THEN\_LEFT  | Pages appear in columns from top to bottom, each subsequent column to the left of its predecessor.  |



 

</dd> <dt>

**dwNupBorderCaps**
</dt> <dd>

Can be only PPCAPS\_BORDER\_PRINT, indicating that, when multiple document pages are being printed on a single side of a physical sheet, the printer can be told whether or not to print a border around the imageable area of each document page.

</dd> <dt>

**dwBookletHandlingCaps**
</dt> <dd>

Can only be PPCAPS\_BOOKLET\_EDGE, indicating that the printer can print booklet style.

</dd> <dt>**dwDuplexHandlingCaps**</dt> <dd> 

| Value                                         | Meaning                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PPCAPS\_REVERSE\_PAGES\_FOR\_REVERSE\_DUPLEX  | When printing in reverse order and duplexing, the processor can print swap the order of each pair of pages, so instead of printing in order 4,3,2,1, they will print in the order 3,4,1,2.                                                                                                       |
| PPCAPS\_DONT\_SEND\_EXTRA\_PAGES\_FOR\_DUPLEX | When duplexing, the Print Processor can be told not to send an extra page when there is an odd number of document pages. The processor will honor the value as best as it can, but in cases where preventing an extra blank page would cause improper output, the extra pages may still be sent. |



 

</dd> <dt>

**dwScalingCaps**
</dt> <dd>

Can only be PPCAPS\_SQUARE\_SCALING, indicating that the printer can scale the page image.

</dd> </dl>

## Remarks

Values for all structure members are supplied by the **GetPrintProcessorCapabilities** function which is documented in the Windows Driver Kit.

When an application calls [**GetPrinterData**](getprinterdata.md), the spooler calls a print processor's **GetPrintProcessorCapabilities** function and specifies a value name that has a format of **PrintProcCaps\_***datatype*, where *datatype* is the name of an input data type.

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

[**GetPrinterData**](getprinterdata.md)
</dt> </dl>

 

 




