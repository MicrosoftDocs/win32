---
description: The PRINTER\_INFO\_1 structure specifies general printer information.
ms.assetid: 0b0e2d0e-2625-4cab-a8f9-536185479443
title: PRINTER_INFO_1 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_INFO_1
- _PRINTER_INFO_1A
- _PRINTER_INFO_1W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_INFO\_1 structure

The **PRINTER\_INFO\_1** structure specifies general printer information.

## Syntax


```C++
typedef struct _PRINTER_INFO_1 {
  DWORD  Flags;
  LPTSTR pDescription;
  LPTSTR pName;
  LPTSTR pComment;
} PRINTER_INFO_1, *PPRINTER_INFO_1;
```



## Members

<dl> <dt>

**Flags**
</dt> <dd>

Specifies information about the returned data. Following are the values for this member.



| Value                    | Meaning                                                                                                                                                                                                                                                   |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRINTER\_ENUM\_EXPAND    | A print provider can set this flag as a hint to a calling application to enumerate this object further if default expansion is enabled. For example, when domains are enumerated, a print provider might indicate the user's domain by setting this flag. |
| PRINTER\_ENUM\_CONTAINER | If this flag is set, the printer object may contain enumerable objects. For example, the object may be a print server that contains printers.                                                                                                             |
| PRINTER\_ENUM\_ICON1     | Indicates that, where appropriate, an application should display an icon identifying the object as a top-level network name, such as Microsoft Windows Network.                                                                                           |
| PRINTER\_ENUM\_ICON2     | Indicates that, where appropriate, an application should display an icon that identifies the object as a network domain.                                                                                                                                  |
| PRINTER\_ENUM\_ICON3     | Indicates that, where appropriate, an application should display an icon that identifies the object as a print server.                                                                                                                                    |
| PRINTER\_ENUM\_ICON4     | Reserved.                                                                                                                                                                                                                                                 |
| PRINTER\_ENUM\_ICON5     | Reserved.                                                                                                                                                                                                                                                 |
| PRINTER\_ENUM\_ICON6     | Reserved.                                                                                                                                                                                                                                                 |
| PRINTER\_ENUM\_ICON7     | Reserved.                                                                                                                                                                                                                                                 |
| PRINTER\_ENUM\_ICON8     | Indicates that, where appropriate, an application should display an icon that identifies the object as a printer.                                                                                                                                         |



 

</dd> <dt>

**pDescription**
</dt> <dd>

Pointer to a null-terminated string that describes the contents of the structure.

</dd> <dt>

**pName**
</dt> <dd>

Pointer to a null-terminated string that names the contents of the structure.

</dd> <dt>

**pComment**
</dt> <dd>

Pointer to a null-terminated string that contains additional data describing the structure.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_PRINTER\_INFO\_1W** (Unicode) and **\_PRINTER\_INFO\_1A** (ANSI)<br/>                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**GetPrinter**](getprinter.md)
</dt> <dt>

[**EnumPrinters**](enumprinters.md)
</dt> <dt>

[**PRINTER\_INFO\_2**](printer-info-2.md)
</dt> <dt>

[**PRINTER\_INFO\_3**](printer-info-3.md)
</dt> <dt>

[**PRINTER\_INFO\_4**](printer-info-4.md)
</dt> </dl>

 

 




