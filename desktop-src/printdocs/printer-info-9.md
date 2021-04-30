---
description: The PRINTER\_INFO\_9 structure specifies the per-user default printer settings.
ms.assetid: 8bafb995-f31c-46e3-a950-45e240c678aa
title: PRINTER_INFO_9 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_INFO_9
- _PRINTER_INFO_9A
- _PRINTER_INFO_9W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_INFO\_9 structure

The **PRINTER\_INFO\_9** structure specifies the per-user default printer settings.

## Syntax


```C++
typedef struct _PRINTER_INFO_9 {
  LPDEVMODE pDevMode;
} PRINTER_INFO_9, *PPRINTER_INFO_9;
```



## Members

<dl> <dt>

**pDevMode**
</dt> <dd>

A pointer to a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure that defines the per-user default printer data such as the paper orientation and the resolution. The **DEVMODE** is stored in the user's registry.

</dd> </dl>

## Remarks

The per-user defaults will affect only a particular user or anyone who uses the profile. In contrast, the global defaults are set by the administrator of a printer that can be used by anyone. For global defaults, use [**PRINTER\_INFO\_8**](printer-info-8.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_PRINTER\_INFO\_9W** (Unicode) and **\_PRINTER\_INFO\_9A** (ANSI)<br/>                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**GetPrinter**](getprinter.md)
</dt> <dt>

[**SetPrinter**](setprinter.md)
</dt> <dt>

[**PRINTER\_INFO\_8**](printer-info-8.md)
</dt> </dl>

 

 




