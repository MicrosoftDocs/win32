---
Description: The PRINTER\_ENUM\_VALUES structure specifies the value name, type, and data for a printer configuration value returned by the EnumPrinterDataEx function.
ms.assetid: 87eb1452-0d9d-46bd-8af8-0542a11a929b
title: PRINTER\_ENUM\_VALUES structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
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

A code indicating the type of data pointed to by the **pData** member. For a list of the possible type codes, see [Registry Value Types](https://msdn.microsoft.com/library/windows/desktop/ms724884).

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



|                                     |                                                                                                           |
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

 

 




