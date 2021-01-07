---
description: The PRINTER\_ENUM\_VALUES structure specifies the value name, type, and data for a printer configuration value returned by the EnumPrinterDataEx function.
ms.assetid: 87eb1452-0d9d-46bd-8af8-0542a11a929b
title: PRINTER_ENUM_VALUES structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_ENUM_VALUES
- _PRINTER_ENUM_VALUESA
- _PRINTER_ENUM_VALUESW
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_ENUM\_VALUES structure

The **PRINTER\_ENUM\_VALUES** structure specifies the value name, type, and data for a printer configuration value returned by the [**EnumPrinterDataEx**](enumprinterdataex.md) function.

## Syntax


```C++
typedef struct _PRINTER_ENUM_VALUES {
  LPTSTR pValueName;
  DWORD  cbValueName;
  DWORD  dwType;
  LPBYTE pData;
  DWORD  cbData;
} PRINTER_ENUM_VALUES, *PPRINTER_ENUM_VALUES;
```



## Members

<dl> <dt>

**pValueName**
</dt> <dd>

Pointer to a null-terminated string that specifies the name of the retrieved value.

</dd> <dt>

**cbValueName**
</dt> <dd>

The number of bytes in the **pValueName** member, including the terminating NULL character.

</dd> <dt>

**dwType**
</dt> <dd>

A code indicating the type of data pointed to by the **pData** member. For a list of the possible type codes, see [Registry Value Types](/windows/desktop/SysInfo/registry-value-types).

</dd> <dt>

**pData**
</dt> <dd>

Pointer to a buffer containing the data for the retrieved value.

</dd> <dt>

**cbData**
</dt> <dd>

The number of bytes retrieved in the **pData** buffer.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_PRINTER\_ENUM\_VALUESW** (Unicode) and **\_PRINTER\_ENUM\_VALUESA** (ANSI)<br/>                 |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**EnumPrinterDataEx**](enumprinterdataex.md)
</dt> </dl>

 

